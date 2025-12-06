---
video_id: lwCwmbQM7Bg
video_url: https://www.youtube.com/watch?v=lwCwmbQM7Bg
is_generated: False
is_translatable: True
summary: |
  Brian Beach used a 20-minute code talk to show how Kiro, AWS’s agentic IDE, can be taught organization-specific languages and libraries so it produces correct code on the first try. He framed the problem many enterprises face: developers rely on custom logging packages, in-house frameworks, or even proprietary DSLs, yet general-purpose models are oblivious to them. Starting with a fictional MathJSON DSL, he ran through four increasingly capable demos to show how Kiro’s context tools—Model Context Protocol (MCP) and steering files—let teams iteratively teach the agent the rules, when to apply them, and how to validate the output.
  After a quick recap of Kiro’s evolution from CodeWhisperer to Q Developer to today’s agentic workflow engine, Brian introduced Kiro’s two main levers. MCP supplies fresh external knowledge and capabilities via tools like get_file_contents, while steering captures enterprise policies (“what good looks like”) in a structured file loaded on every request. The baseline demo asked Kiro to implement mortgage overpayment in MathJSON without any context; it predictably produced Python. Feeding it a raw MathJSON function reference helped slightly, but only when Brian explicitly prompted “using MathJSON,” exposing the need for more prescriptive guidance.
  To close that gap, he used Kiro’s Refine button to shrink an 1,100-line reference down to the essentials (~100 lines) and then added clear guardrails: always use MathJSON for math tasks, honor file extensions, and run the provided linter. That version produced the right artifact automatically and validated it with the built-in lint command. He noted that refinement can also expand terse docs when the model needs more explicit instructions, and that reducing redundancy cuts context bloat.
  The next iteration removed stale copies entirely by letting the agent fetch fresh source documentation at run time via MCP. A concise steering file now simply declared the DSL, when to invoke it, lint commands, and where to look for truth; Kiro then called MCP to pull current function references from GitHub, generated MathJSON with the correct .math extension, linted it, and even created README/tests. This pattern keeps teams from maintaining divergent “shadow” docs and allows many small repositories to stay in sync without manual updates.
  Brian closed with best practices for making agents self-improving: ask Kiro to update its own steering file when it encounters complexity, consider hosting documentation in vector or semantic stores (e.g., Bedrock Knowledge Bases, OpenSearch) to fetch only relevant slices, and embed security or style rules in steering so they are enforced with every run. He pointed attendees to hands-on experiences at the House of Kiro, kiosks, and Builder Loft sessions, positioning Kiro as a way to bring real enterprise rules, not just generic codegen, into the agentic era.
keywords: Kiro, agentic IDE, steering, Model Context Protocol, MathJSON
---

- Hello, everyone. My name is Brian Beach. I'm the tech lead for our Next Gen Developer
Experience team within AWS. And so I spend my time helping developers, customers who are developers, with all of our developer tools, so things like CI/CD,
infrastructure as code and more recently, I've been
spending most of my time in the agentic AI space, specifically for software development. So I'm wearing a Kiro shirt. I spend most of my time
talking about Kiro these days. This session today, I'm
gonna talk a little bit about teaching your AI tools all about your custom languages and libraries that you might have as part of your organization. Nearly every customer I work with has a series of custom tools. This might be something really simple, like you've got a custom logging library that you're supposed to
use when you write code within your organization, or it might be a whole tech stack that the the large language
models have never seen and are unaware of, or even to the most extreme is, you've written your own
domain-specific language and you need to teach your
AI tool how to do that. And so I'm gonna walk you
through how we do that with Kiro. Most of what I'm gonna talk about is applicable to other tools as well, but I'm gonna walk through
using some of the constructs that exist in Kiro, since
that's the one that I know best. And that's what we'll do
for the next very short, only 20 minutes here. So quick agenda, I will start with just a brief introduction to Kiro. I promise to keep that really short, just two or three slides to get us going. And then I'm gonna talk just a little bit about some of the tools that Kiro has for context management. Okay, again, most of this is
applicable to other tools, but I'll be doing this demoing in Kiro. So, let's talk a little
bit about how that works. And then I'm gonna introduce a domain-specific
language called MathJSON. This is totally fictional. I made it up, or more specifically Kiro
made it up for this demo, and a blog post that I put out. And what we're gonna
do is we'll go through a whole series of demos
working with MathJSON. Being a language that we just made up, none of the large language
models are trained on this. None of them know how to use it. And so we're gonna just
start from the ground up and work through a couple iterations. In the first demo, the baseline, Kiro will know nothing about this language and will fail spectacularly. And then we'll keep iterating
and building on top of that, bringing additional constructs in to be able to teach it how
to work with this language that it's never seen before. And I'm working with a
domain-specific language, but everything that I'm gonna talk about is applicable to you if you were just maybe
doing a custom library. It doesn't have to be a whole language. All of this will make sense as we go. So with that, let's do just
a brief introduction to Kiro. Is everyone aware of Kiro? Maybe, who hasn't heard of Kiro? Okay, so Kiro is an agentic IDE that we launched a few months back. It launched in the summer, and just went GA last
month in mid-November. So it's very recently GA. You're gonna see stuff all about it. If you go to the Venetian, we
have this cool haunted house, you can do a tour of the haunted house and learn a little bit more about it. I'll tell you at the end how to get all the different opportunities
to learn more about Kiro. So let's do just a quick history. This is my third year doing
some version of this talk. So I did this back in
2023 about CodeWhisperer and talked about how to
customize CodeWhisperer. And if you've seen CodeWhisperer, it predicted the rest of
the line you were typing or the next couple of lines, helped you as a developer
develop code a little bit faster. We've come a long way since then. Then last year I did this
talk about Amazon Q Developer, and when we got to Q, it
was much more about chat. We had evolved a lot, and I could go in and have conversations about the architecture and ask it to write code on my behalf and have it do quite a bit more work than it used to be able to do. Now, 2025, this year, I'm sure you know, is all about agents. And so we've really embraced
this agentic approach where we can use some
of these larger models that have reasoning capability
and are goal-seeking. I can say, "I want to accomplish this," and let Kiro take over all the work of going through the architecture and then writing the
code to implement that, really broadening the
scope of what's possible. And so as we move into this agentic era, what would the development
experience look like if we could take full
advantage of those agents? And that's what we're
bringing to you with Kiro. That's what Kiro is, right? Kiro takes all the way from
prototype to production, to go all the way from the design phase all the way through software
development into deployment. And I know that's really quick, we'll see it in action in a minute, but I wanna talk about just
a couple of basic features to give you a sense of the capabilities that we're gonna use today. There's a bunch more that
I'm not talking about that Kiro can do that you'll
learn about in other sessions, but there's a few things
you need to understand for the demos that I'm
gonna do here today. All right, and this is all about
how you manage the context. What does Kiro know
about your environment? And there's two tools that
we're gonna use for this. The first is MCP. I assume, is everyone familiar with MCP? It stands for model context protocol. This is what gives your agent access to additional
information that it doesn't know and allows it to act on
the environment around it. The second thing that we're gonna bring in is what Kiro calls steering. And steering is just the set of rules that are unique to me,
how I want it to act. So I'm providing it the rules necessary to steer it in the direction
that is meaningful to me. And to give you a little more
sense of what that looks like, this is an example of an
agent steering file in Kiro. And you can see this is a set
of Python coding standards. This is what I think good looks like. I don't need to teach
Kiro how to write Python, but I need to teach it the
way I want it to write Python. And so the two things
I'm telling it to do here are for documentation, I
always want docstrings. That might be my organizational standard or just my preference, but I always wanna see docstrings in all the code that you write. And so I tell it, "You need to do that." I also like to see type hints. I wanna see everything typed. And so again, I put that in, and now Kiro will see these, this gets injected, if you
see at the top that wild card, anytime I'm working on a Python file, these rules get injected into
the context automatically and then Kiro knows that it
needs to go do these things. So this is called steering. We'll use this later to teach it about a custom language that it's never seen before. The other tool that we're
gonna use is MCP, right? Again, model context protocol. This is what connects me
into external systems. And so you can see here I'm
connected to two things. I've got a GitHub connector in MCP and I've got my Postgres
database connected, and I've got Postgres opened up there. You can see that this MCP
server provides me two tools. One is to run a query and the
other is to get table schema. So if I'm asking kiro
to write queries for me, it's gonna need to understand what my database schema looks like. This is probably something
it was never trained on because this is unique to me. So now I can go and
discover that in real time, and this makes it much more effective. And letting it run queries allows it to go and execute
some of these and say, "Hey, is this right? Is
this syntactically correct?" I can now test it and see if
I'm getting back what I expect. And we're gonna use these two
things together in concert in a minute to teach kiro about MathJSON. So before we do that,
before we jump into demos, let's just do a quick
introduction to MathJSON. And MathJSON, as the name suggests, is a JSON syntax for
writing math equations. All right, it can handle simple things like adding and subtracting. It can also do more complicated things that we're not gonna get to today, like trig and logs and on and on. It uses a file extension called .math, but it's written in JSON syntax. And this is completely fictitious. I am in no way suggesting that anyone should use MathJSON, right? We made this up just as a proxy to what I see so many customers doing. So many customers have custom vocabularies in XML or JSON syntax that
these models know nothing about. You use them for workflows
or to describe business logic and business rules. And so this is a way
that you can teach it. That's all that this is meant, is a proxy to the things that you have in your organizations. I don't want you to actually use this. And here's an example of what
MathJSON looks like, right? Again, it's just a JSON syntax. This is the formula for
calculating the area of a circle given an input radius, okay? Marked up as this
fictitious JSON language. And I keep this in a GitHub repository. Note at the top, this
is a private repository. So the models have never
been trained on this. They are unaware that MathJSON exists or how to work with it. And notice there's a whole bunch of documentation that's available here. If I brought in a new hire, I would point them here and say, "Go read through all the documentation so that you understand
the function reference and you know what's available. You know how to use environment variables, you know how to troubleshoot." All of that's well documented. I have to onboard the agent the same way that I onboard a new
hire in my organization. And so with that quick foundation, let's look at a couple of demos to get a sense of what this looks like. And again, I'm gonna
start with a baseline, and this is not going to work, right? I haven't done anything yet,
I haven't taught it anything. So I'm in Kiro here. Hopefully that's big enough to see. Bottom right corner, I'm asking kiro in this
case to create a function to look at mortgage overpayment. How much savings am I going to
have over the life of a loan if I overpay on my mortgage? So let's let that happen. And you see Kiro starts
thinking about that and says, "Okay, let me work on this." And you see right away that it starts writing a Python function. Okay? Over here on the, I just need to make this a little bigger so I can see what I'm doing here. But you see over there, it starts building this mortgage
calculator Python function, which is of course not what I want. I want it to do this in MathJSON, but it doesn't know that MathJSON exists. It does an excellent job, by the way, of doing this in Python. It's a really well-documented code. You can see over on the
right, it also tested it, it executed a few times to make sure that it's working right, but it's not what I wanted. I need to go and teach it
about the things that I want. So issues after our first
demo, this is obvious. Kiro has no awareness of MathJSON. Doesn't know that it exists. So the first thing I'm gonna do is we talked a little bit about
the existence of steering. These are the rules that can guide and steer kiro about
how I want it to work. And so the simple, the naive approach is I'm just gonna go in here and I'm gonna grab one of
those documents that I had, in this case, the function reference which teaches it how to use all
the different function types and I'm just gonna stick it in steering. Okay, so you see over on the left side, I stuck that into steering there. And if we come in here, you can see this is that documentation that I brought down from GitHub. It's a little easier to see
this if we go into preview. So lemme preview that. And you can see it walks through, like, here's
how to do arithmetic. And it gives me the prototype,
gives me a couple examples of simple and more complex,
moves into subtraction. And if we kept scrolling, we'd go through all the
different math types that are supported in here. So I'm gonna go through, and let's ask the same question again. Again, "Give me a function to
model mortgage overpayment." And you can see again, Kiro was once again doing Python, right, despite the fact that I gave
it the MathJSON document, it's doing Python while it's working. I just wanna give you a
sense of the scope of this. We scroll down, there's about 1,100 lines of documentation in just
one of the dozen files that were available in GitHub. I've given it all of this, but it's still not doing
what I want, right? It's still writing a Python function. So I could come in here and you can see kinda highlighted there, I just simply changed my
prompt ever so slightly to say, "Using MathJSON." And I ask it this again. And this time, it will start
to do the right thing, okay? It's building a JSON file this time. It should have a .math
extension. We covered that. Doesn't know that yet. I didn't tell it yet
what it needs to know. But it's getting the beginnings of this. But I had to tell it what to do. I had to be prescriptive in my prompt and say, "I want you to
do this with MathJSON." So what happened, right? We were on the second of four demos. What was the issue here? First, we were not prescriptive enough. I was not prescriptive enough. I gave it documentation
for the function reference, it told it what it could do, but I didn't tell it
what I expected it to do. I didn't tell it when
to use MathJSON, right? It also didn't use the
correct file extension because that's not covered in
that piece of documentation. Also, I will note at this point the docs are very repetitive. If you go through there, that
doc was written for a human and it's just given me
examples over and over again, the same information
for add, for subtract, for multiply, for divide. It's super redundant and I'm dumping a lot of
stuff into the context that I probably don't need. So the next thing I wanna do is I want to continue to iterate. I'm just gonna refine that
steering document a little bit. So I'll come back in here. Again, we're about 1,100
lines of documentation, and I'm simply gonna come up
and ask Kiro to refine this. So there's this nice
Refine button up here. And when I click that, what
I'm asking Kiro to do is, say, "Go read through all this documentation and essentially refine it down
to what you actually need." So what do you think you need out of this? And this is gonna be a theme here. I'm gonna keep asking Kiro to do things rather than trying to do them myself. Let it make decisions
about what it needs to do. The models are getting really smart. I sped this one up. This is a pretty complex ask. It takes it about 90 seconds to go through and analyze this doc and figure
out how to refine it down. Note, sometimes when you refine it, it'll actually expand the document. If you have a really
terse, simple statement, it will make some assumptions and expand it and you can look it over. But generally, it's gonna make it smaller. So you can see here now it went through and really refined down what was 1,100 lines and took this down to just about 100. So it got it down to about
10% of its original size. And if you looked at those examples, it gave me one example of how to write the syntax
and how to nest things. It didn't repeat that for every type, because it's the same over and over again. So it did, in my opinion,
a pretty good job of refining this down. I haven't been prescriptive yet, though. I've shrunk it, but I haven't added that prescriptive element. So let's go in and do that too. And I'm just gonna take off this header. And what I wanna do now
is I'm gonna just paste in this much more descriptive
statement that says, "Hey, this project uses MathJSON," right? This is when to use it, "You must use MathJSON
anytime you're doing math." And I also tell it about
the linters and how to run, how do you actually execute
these so you can test so that, like it did in Python, it can actually go and test this and make sure that it's working right? Okay. And now, I'll come back in. Let's start a new fresh prompt. And I'm gonna come back
to that same question I've been asking over and over again about writing a function to
model mortgage overpayment. And you can see now, right away, it finally
got the extension right. It's nailing it. And I didn't have to go in and be explicit and say, "Using MathJSON." It knows that it's doing math and it must use MathJSON because the steering
file is now prescriptive. So I'm starting to give it
all of the elements it needs to understand how to
do this, when to do it, how to run the linter. And you can see now it's
actually executing the linter and validating that this is correct. All right, so we've mostly
gotten to my goal at this point, but we added a couple
issues in the process that maybe you're thinking about, and some of those things
that bother me a little bit about this implementation is first I just created
this derivative copy of the original. I took this 1,100-line file
out of the GitHub repository, I went through this refinement, and now I've got this derivative copy, and if the original changes, we're still working on
and iterating on MathJSON, now I've got this stale copy
that's gonna be outta date. So I don't want to do that. Also, we only grabbed one of about a dozen
documents that were available. So what I wanna do now is
layer in MCP into this. And so I'm gonna grab
this get_file_contents. All right, and I'm gonna use
that tool from the MCP server and I'm gonna update, I've updated the file a little
bit here to just tell it, "Hey, when you need to
learn about MathJSON, you can go use the MCP server. Here's a pointer to the documentation so you can learn more." All right, I left in some
of the best practices, some of the guidance and how to use linters
and stuff like that. But I've mostly condensed
this down quite a bit and gotten rid of that
derivative copy altogether. And so now again, let's come in and ask the same question that I've been asking over and over again. And you can see here, he reads in first the steering doc and then you see him start
to make those MCP calls and say, "Okay, I'm gonna reach out and I'm gonna read the documentation." Here it is reading that function reference that we've accessed
multiple times along the way to pull in the information
it needs in real time. Rather than leaning on
that copy that we made, it's able to just go as it needs it and pull it out of GitHub. Or wherever you're keeping it, of course, it doesn't have to be GitHub. And now it comes through and writes that, writing the MathJSON and giving it the right
file extension here. All right, you see it doing, it adds a readme file and whatnot that I don't think is
terribly important to look at. Also, if we jump ahead here, you can see it going through
and also executing the linter and saying, "Okay, I'm gonna lint this and make sure that all of these are right, these five files look correct." And then finally writes a test case, writes a couple unit tests essentially, and goes through and
executes them as well. So pretty quickly, I'm able to get from Kiro knows nothing about this till I'm giving it the steering file to say, "Hey, this exists, this is when you should use MathJSON and here's all the pointers you need to go learn more about this." And you can go read the documentation in real time as you need it. All right, so with that,
I'm almost outta time. I've mostly accomplished
what I want to cover, but there's a few things
that I just couldn't cram into this really short 20-minute session. So I do wanna talk a little
bit about other things that you could do to make this even better
that I didn't get to. And one of them is asking Kiro
to make updates on its own. I mentioned this when I
said, "Use the Refine button to shrink down the steering file," but you should always
be thinking in this way. In this example here, there was a time where I was playing with MathJSON, Kiro's working on a big file and it says, "Hey, I'm realizing that this
is getting really complex. I'm gonna try a new approach." We've probably all seen
the AI models do this. We're like, "Hey, this
is getting outta hand. Let me rethink this and
try a different approach." This is a great time to go in and say, "Hey, you said this is too complex. Do you want to go update
the steering file? Would you like to go
update your own guidance so that you don't make this
mistake in the future?" So think about finding times to do that. The second thing is, while we move the
documentation out to GitHub, we're pointing at pretty big docs. Getting them into some kind of either vector database like
Bedrock Knowledge Bases or into a semantic database like an OpenSearch or Elasticsearch is a great way to allow it to go in and just grab out the piece
of the puzzle that it needs so that it can go and just
grab the addition portion if it just needs to know about addition without reading the entire doc. So that's an optimization you
might think about adding in for a big project. And with that, I'm just gonna
point you to a few more things that are happening across
re:Invent this week if you want to learn more about Kiro. So if you've been to the Venetian, you probably saw the House of Kiro, it's the big haunted
house up on level two, right outside the expo. Get some time and go through that. It's a really cool experience
to get you introduced. Also at Venetian, we are running a Kiro
kiosk in the AWS Village in the Expo Center. Stop by there. We have a competition running where you can win some
cool swag and prizes. We're giving some swag away too there, and a lot to be learned. And if you're spending your
week down here at Mandalay Bay, over in the corner here
is the Builder Loft. We are there every day at noon and at 4:30 doing sessions there. So drop in there and you can
meet with the service team and talk to people about it. And with that, thank you. I appreciate it. (audience applauds)

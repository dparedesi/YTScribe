---
video_id: VRw3g-v4B00
video_url: https://www.youtube.com/watch?v=VRw3g-v4B00
is_generated: False
is_translatable: True
---

- [Ryan Yanchuleff] Thank you
for coming out this afternoon for our session on Kiro. We'll be talking about
how to build applications and we're gonna be
building a live application in front of you here this afternoon. So I am Ryan Yanchuleff, I'm one of our specialist
solutions architects here at AWS. I'm part of the Next Generation
Developer Experience team. So we work with customers who are looking to roll out generative
AI development tools inside of their organizations. And with me, I have Ryan. - [Ryan Bachman] And I am
also Ryan, Ryan Bachman, same team, same responsibilities, same everything that he just said. As we get into the session,
who's done a code talk before? Anybody? Anyone done a code talk before? Okay. These sessions are
really meant to be interactive. So while we are gonna
be doing live coding, I also encourage us to
engage, learn from each other. I'll be walking around as
he's presenting and coding. We'll have some dev time, ask questions. I'll go ahead and amplify that question and we can kind of talk about it, right? Whatever you want to talk about, learn, we're here to talk about agentic AI or spec-driven development
as well with Kiro. So yeah, let's just feel free, share your opinions, share your thoughts. I will be polling the
audience numerous times today. - [Ryan Yanchuleff] Yeah,
we are going to be building an application from scratch inside of Kiro live on the screen. And we're going to build an application that you guys and gals recommend. So Ryan's gonna poll the
audience here in just a minute, and we're gonna take the
two or three best ideas and we're gonna build them
live here on the screen. We'll build the best
one live on the screen, so, you know, be thinking
about that as we walk through the next couple of slides here. So before we dive into it, wanna just kind of set the stage, talk a little bit about what Kiro is so that everybody's familiar with it. It's a relatively new product
that we released this year, and it just went general availability about two weeks before today. So with that, one of the
questions that we get asked a lot is why did we build another tool? There's a lot of them out there. So why did we build another one? And I think it's helpful
to kind of understand where things have gone
and how they've evolved. So if you go back a couple of years, we started out with generative AI that just did sort of general helping. It was a glorified IntelliSense, auto complete, simple chat
questions and interactions and things like that. And then more recently
we got into a situation where we could do assistance. We could say, "Hey, I want to go and make a change to this function." Or, "I want to go and debug
this particular log file." Or, "Help me out with this thing." Very specific tasks that we could, again, ask the generative AI tools
to go in and help us with. And then in the current age,
we have what we call agents, which is where I take
more complex problems. I say, "Here's what I want to do, here's what I want to build. I wanna build an application. I want to add a new feature
to my existing application. I wanna modernize this
part of my application. I wanna migrate this
piece of application code and I need you to help me out with that." And that involves
multiple different steps. "I've gotta run things
on the command line. I've gotta talk to third-party tools. I've got to generate code. I've gotta modify existing code." And we call this agentic development. The term "agentic" gets overloaded a lot. So I think it's helpful
to kind of understand what we mean when we say that. So the promise here was
that we get autonomy. We could all go sit on the beach while we let the generative AI tools go and write code for us. We get more collaboration. We have a back and forth conversation with this generative AI tool and we chat along and we tell funny jokes and we get work done, just like you do with
your other coworkers. And then we, of course,
get high-quality code. Nobody's producing junk when we do this 'cause we're all professionals. And so this is the promise. The challenge though, that we
saw with customers starting to use these tools in their
production environments centered around three major things. And it was these three major things that we set out to solve
for when we built Kiro. And these three things really are laid out here for you on the screen. The first one and the biggest
one is how do you scale? So it's great when I
wanna build Tic-Tac-Toe and I'm just one developer in a corner hacking out some code. But when I have an existing
production application with 1.2 million lines of
code and I've got a team of 150 developers who
are all working together, this becomes really important
because I need my LLM to be able to understand all that code. I need it to be able to
understand that code consistently. And I need it to be able
to produce similar results for all 150 developers along the way. It does me no good if the
non-deterministic nature of the LLMs creates working solutions for all 150 developers, but it does so in very incompatible ways, which is possible when you think about the non-deterministic
aspects of generative AI. So how do we do this at scale? How do we solve for
large development teams and how do we solve for
large existing code bases? The other piece is the idea of control. We talked about, in the previous slide, about this true collaboration concept, but that's not really what
we have in generative AI. What we have in generative
AI is we take this prompt that we kind of concoct and
and throw into the chat box, we throw it over the wall and
we say, "Make me something." And it goes off and it
writes a 1,000 lines of code and it says, "I made you something." And then it hands it to you
and hopefully it did it right. But more than likely what happened is that it got to a lot of
different decision points, a lot of details that you
left out of your prompt that it now has to go
and fill in the blanks. And maybe it got it right, maybe it chose the option
you would've chosen, maybe it didn't, but now it's
up to you to figure that out. And now you've got a 1,000 lines of code that you've gotta go
and figure it out with. And then the last piece is when you take those
two factors together, both of those negatively impact the overall quality of the code. What you're getting is code
that you don't really want. It doesn't really do
what you wanted it to do, and it doesn't really do it
the way you wanted it to do. And it does it differently for all the different
developers on your team, which is not helpful. So what we created for Kiro and what we tightly
integrated into the solution is something that we call
spec-driven development. And it's a return back to first principles of software development. We don't bring a team of
developers into a room, write four bullet points on a whiteboard, and say, "Guys, we'll check
in on you in six months. Let us know how it goes." That would be chaos, and for good reason. What we do is we step back and we say, "All right, what are the requirements? Let's detail those. Let's bring in our stakeholders, let's bring in all the key
players and lay that out." Then we say, "All right, well
these are the requirements. How are we gonna build this?" And we build a design document and we say, "What are all of the
different design specs and the technical details?" And we lay all of those out and we bring in all the stakeholders. And then we say, "All right, well, what
is the project plan?" We build one of those fun Gantt charts with all of the different
tasks that we can do in parallel and in serial
and we lay those things out. And then once we have those, then we bring the team
of developers in the room and we say, "Here's what you're building. Here's how you're building it. And here's all the different
tasks that you need to do." And we use those to go off and actually do the implementation. And that's how we solve for this problem of building at scale. So what spec-driven development does is it takes generative AI and
it applies the same model. It says, "Give me your
prompt that you concocted, that's missing a lot of details, and instead of going off and
writing a 1,000 lines of code, I'm gonna go and I'm gonna
generate a requirements document. And then I'm gonna
generate a design document. And then I'm gonna
generate a project plan. And you're gonna have the opportunity to review all those things. 'cause they're just text documents. And then when you're
happy with all of those, then we'll start building." And whether it's just you
on a greenfield application, like what we're gonna do here in a moment, or whether you've got a
team of a 100 developers and hundreds of thousands
of lines of code, we're gonna get very similar results because we're working
with the same context. We're working with the same details, and we've had a chance in advance to review all of the different details that might have gotten
left out from your prompt. And we can fill in the blanks and we can validate them
all and then we can move on. And so that's what
spec-driven development is, and that's really what makes Kiro unique. So if you could build an application and take advantage of that, how
would you go about doing it? And so this is where
we're gonna switch over and we're gonna switch
to a live coding demo. And so I'm gonna need some ideas because I've got a blank, empty screen and I need something to build. - [Ryan Bachman] Yep. Anybody that's been to
like an improv show, I'm gonna try this out. Like, you know, you shout
out like random ideas and then we're gonna maybe
combine a couple or two. So this is where we need the audience. So, like, don't raise your
hand, just like yell out- - Fitness app.
- What's that? - A fitness app.
- Alright, a fitness app. Anyone else? - [Audience Member] That
focuses on the trainer. - [Ryan Bachman] Fitness app
that focuses on the trainer. - [Audience Member] AWS event app. - AWS what now?
- Event app. Event manager. That's my app. - Is that your-
- I came up with that app. - Any other-
- That's what I normally do in my demos. - [Ryan Bachman] I don't know
how to combine those two. - [Audience Member] Virtual concierge. - [Ryan Bachman] Virtual concierge? - For hotels
- Oh, hotel. - There you go.
- All right. So we got a fitness app, concierge app, and I don't know how to
combine all three of those. - [Ryan Yanchuleff] All right, let's see. Let's see what we can come up with here. - [Ryan Bachman] How
about a fitness app for- - [Ryan Yanchuleff] "I want
to build a web application to manage my fitness-" - [Audience Member] Track
your steps through AWS. - There you go.
- "Activities and determine if I actually did them
and how many calories I burned in the process." - Perfect.
- Alright, we have 40 minutes. So I'm simplifying this down a little bit. But, okay, so here's my prompt. If you look at that prompt, you can tell pretty quickly right away that there's a lot of detail missing here. I have specified that I
want a web application, I have not specified what I want it to be. Could be React, could be
Python, could be .NET, could be some esoteric
language from 40 years ago. We haven't really defined that. We haven't specified a
lot of things in here like do we want authentication? That's probably a good idea
for a personal fitness app. We haven't specified what
a lot of the features are. We haven't defined whether
we want a full stack app with a data layer and a business
layer and a front layer, or whether we want to
build this all together like a Next.js app, for instance. We haven't said if we
want it to be mobile. Well, actually we did. We said we wanted it to
be a web application, so we specified that. But you get the point. There are a lot of details here. And in Kiro, I have the ability to switch between two different modes. So if I were to put this into Vibe mode, which is what you'd get from a traditional generative AI tool, and
I were to hit "Go" here, it would go off and it would
immediately start building. And what would it start building? Well, it would figure out some strategy to build a web application. It might pick React, it might pick Python, it might pick something else. And if there were five
of us up here on stage, it might pick something
different for each one of us because generative AI, by
definition, is non-deterministic, so we're not guaranteed the same results. But I'm gonna put it into Spec mode and I'm gonna kick this off. And so what's gonna
happen now is that Kiro, instead of going off and
actually writing the code, is it's going to start
generating what we call a spec. And a spec here is going
to define what it is that we wanna build before we
actually start building it. And so we're gonna let
this run in real-time to kind of give you a
sense of how much time this actually takes. The spoiler alert, it
doesn't take very long, assuming that our network holds up here. And so it's going to create
for us a requirements document. And you can see here, it's opened it up for me on the screen. And so I've got my requirements
document on the screen here. And this requirements document starts out with a high-level introduction. So it's given me kind of a
general summary of what I put in. I wrote one sentence
into the prompt box here. I've gotten a paragraph of
details that are laid out. I've also gotten a glossary of terms so that we are clear on
what we're talking about. It's laid out a lot of different details like what's a user? What's an activity? What kind of activity types are there? How do we calculate calorie consumption? How do we deal with the activity logs? All of these different
things here are laid out. These are all important things if I'm gonna go and build this application that I didn't specify
in my original prompt. And then we're gonna get
into the meat of this, which is the requirements themselves. So each requirement is
gonna have a user story and it's gonna have a set
of acceptance criteria. And so the user story combined
with the acceptance criteria is going to detail all of the
different things that I want. And you can see here that it came up with seven requirements, which is not bad considering
that I gave it one sentence. Now, is that enough requirements to build a full fledged web application for fitness tracking with auth and all of those other details? Probably not. But it does get us
quite a bit farther down the road than we would've been if we had just taken this prompt and thrown it over the wall. And one of the things that's important to understand about specs is that they're not really designed to be used to write an
entire operating system. You want to use something like a spec to do feature development. So our application here is
going to evolve over time. There are going to be things
that we want to add to it. There are gonna be things as
we show off our initial MVP to our stakeholders. There are gonna be things
that they're gonna say, "Well, this is really cool,
but I want to add this thing. This is really cool, but
I wanna change this piece. I hate this thing. I can't believe you built this." And we're gonna go a couple
different routes here and we're gonna be able
to evolve as we go. So we've got our user stories here and they follow a specific format. They follow what we call EARS. It's an industry standard
for writing requirements is it's Easy Accessible
Requirements System Spec, something like that. I never remember what
that acronym stands for, but it follows that key system, which is that it creates a user story and then it creates acceptance criteria. And so what we can do now is we can say, "All right, let's review this. Do we like this? Does it capture the things that we want? Did we think of something
else in the five minutes that it took to create this document that we want to add to this?" And so we can evaluate and iterate on this and we can make adjustments. For the sake of time, I'm
gonna leave it here as it is. But it says here, like, "As a user, I want to create
and manage fitness activities." That's a good start. That kind of aligns with
the prompt that I have here so that I can plan and
track my exercise routines. Cool. "I want to mark the
activities as completed with their actual duration, so that I can track what
I actually accomplished." And you can see here that each
one has acceptance criteria. So when a user creates a new activity, the application should store
that activity with the details, with the type, with the planned duration, with the planned date, all of that information
should get tracked. Maybe I want to add
another attribute there, maybe you want to track location as well. And so now is my
opportunity to come in here and make an adjustment. And I can say I want to
add location to my data that's being stored. All I'm doing here is
modifying a markdown file. So once I'm happy with the requirements, I move on to the design phase. And I say, "All right,
well, this is great, but now I wanna know how am I
actually going to build this? What language am I gonna write it in? What libraries am I gonna use? What am I gonna do for authentication? How am I gonna handle error handling? What am I gonna do for testing?" All of these different details
need to be captured here. And so we gave it no details
except for a web application. So we're all gonna find out together what this thing actually decides to build and how it decides to build it. And this is gonna be
our opportunity to say, "No. I don't wanna build it with Python, I want to build it with React. I don't wanna build it with React, I want to build it with Go. I want to build it with a SQL database. I don't wanna build it
with a SQL database. I want to build it with NoSQL databases." This is my opportunity to
correct for all of these things. Because at this point, if we, again, just threw this over the
wall with vibe coding, the LLM would make
those decisions for you. It would say, "You didn't tell me what kind of database you wanted. I feel like SQL today,
I'm going that route." And if you wanted NoSQL,
you're out of luck. You're gonna have to go back and rebuild that code after the fact. And so that creates
complications and it takes time to evaluate for all of those things. So at this point, we're
gonna get an evaluation. And you can see here one of the things that it's doing is it's saying that it's formalizing the requirements for correctness properties. What this is, so Kiro has a feature in it called property-based testing. And property-based testing
is a really fancy term for essentially testing with edge cases. But it's going to evaluate my requirements and it's going to say, what are the things that
need to be checked for? How am I going to check for them? And not just the happy path, but what are all the edge cases? You say that you want to know what your planned duration
is for your activity. Well, what happens if you enter a bunch of letters into that field? What's it gonna do? Is it gonna give you an error? Is it gonna crash? Is it gonna blow up? How's it gonna handle that? So that's just one example. But you can see here that it's looking at the different prompts there or the different
requirements and it's saying, "All right, well, what do we need to do to test for all of that?" And so when we go now and we
look at the design document, what we have here is
another summary at the top with all of these details. We have more architecture. So we have a foundation layer,
we have a business layer, we have a data access layer, we have our browser's local
storage, we have a tech stack. It looks like it's using
React with TypeScript here. That's what it's settled on. It's gonna use the React context
API for state management, it's gonna use Tailwind for my UI. So a lot of different things
here are being specified. And, again, if I don't
like any of those things, it's pretty simple. I just go in and modify
this document here, and I'm good to go. So it's gonna lay out, again, the stack for all of the
different models that I have. We're gonna get into the data layer, we're gonna get into the
correctness properties and all of the different ways
in which we're gonna do that. So what happens if I have a planned and... Stop that. What happens if we have a
planned and actual duration? Do they both get preserved? So how are we gonna calculate that? What are we gonna do for
triggering the calorie calculation? A whole lot of different details there. Then we get into error
handling, input validation. We get into business logic errors. We get into testing
strategies, including employing all of those different
property-based tests that we outlined above. What do we do for unit testing and integration and test execution? So there's a lot of detail
here that's captured. You got some questions over here? - Go ahead.
- So the question was two things. The MCP servers, is that the
default or did you add those? I saw agent steering. What is that?
- Okay. So just, I mean, for the room too, so the questions are we
have some MCP servers that are configured, you
can see in this video and then also agent steering. What is agent steering? - [Ryan Yanchuleff] Yeah. So
the MCP servers I installed. So by default Kiro doesn't come installed with any MCP servers. It has support though
for local MCP servers and for remote MCP servers. So you can go through the
remote MCP server flow, you can do OAuth to connect
to your remote MCP servers if you want to do that. Or you can install local MCP servers and you can configure them. I have these installed at the user level, which means that they work for all the different
projects that I open. You can also install MCP
servers at the project level, so they're only relevant
to the specific project. So these MCP servers here happen to be installed
locally on my machine. I don't know that we're
necessarily gonna use them over the course of our demo here, but you can install whatever you want. They don't come pre-installed. Now the question about agent steering. So over here on the left hand side, this is my Kiro panel here
on the left hand side. I get to it by clicking
on the little ghost here. Kiro by default is a a VS Code fork. So if you're looking at this going, "This looks pretty familiar," it's because it's a VS Code fork. And so a lot of the UI and elements here are gonna be very familiar to you. But there's a section here at the bottom with the little ghost
that brings up the details that are unique to Kiro. And you can see here at the top, the spec that we're
working on is listed here. And so I can see the
spec that I have here. I can create as many specs as I want. So I'm not limited to one spec. I don't have to try and build
my entire project in one go. I can create multiple different specs and I can track them all as I go along. We'll finish this one
out here in a moment. But down here I have Agent Steering. So what is Agent Steering? Well, if you've used other
generative AI tools before, you're familiar with the idea of context, or you're familiar with the idea of rules. So in Q Developer, for instance,
we have the idea of rules. What a rule is, is essentially
just a piece of context that sort of provides guidelines
for the LLM to follow. Whenever you document or
whenever you write a function, I want you to include a comment block that looks like you know,
X, Y, Z at the top of it. And so that's a rule, I want
Kiro to to do that for me. Steering documents though,
and particularly this button called Generate Steering Documents, deal with one of the challenges that we talked about in
the slide presentation, which is how do I deal with projects that have existing code? How do I deal with a project that has hundreds of
thousands of lines of code? Well, in order to do
that, what I need to do is I need to document that somehow, I need to create some context around it, I need to summarize it, and I need to make that
available to the LLM in the form of rules or
context or something like that. And so what Generate
Steering Documents does is that the first time I... Or whenever I open up a
new code base in Kiro, and by "new" here, I mean new to Kiro. So maybe I've been working
on this project for 10 years, but I'm gonna open it up in
Kiro and I'm gonna go down and I'm gonna hit that Generate
Steering Documents button. And what it's gonna do for me is it's going to reverse
analyze that code for me. So it's gonna go through
all of that source code and it's going to summarize it for me. and it's gonna say, "All
right, here are the details that I need to be aware of when you ask me to make a change to this code." And so it's going to create
a file called product. And the product file is a natural language summary of the code. It's a layout of what is this code doing that I as as a reader, as a human, could quickly pull up and say, "All right, give me a summary of what this 800,000 line
code project is doing," and I can read through that. Then it's gonna build a tech file. And the tech file is really gonna mirror what our design document
file looks like here. It's gonna be the tech stack. What language is it written in? What libraries is it using? What's its strategy for error handling? What's its strategy for testing? What are the commands necessary
to boot the dev server? What's the command necessary
to run the test suite? All of those different things are gonna get captured in the tech file. And then it's gonna build the... I'm blanking on the last name. The product file, I
think is the last file, is essentially the roadmap. And so the roadmap file is gonna lay out, here's the directory
structure of this project, here's all of the different
directories, here's the code, the files that are in
each of these directories. Here's what's relevant about
each of these directories in each of these files. Here's the major classes and modules and elements inside of these. And equally as important, if I ask you to make a change
to this particular module, what's the blast radius? So I ask you to make a change to the authentication component
in my 800,000 line project. If I go in and modify that, how many other things in this project are gonna be impacted by that change? And in order to know the answer to that, I need to know what the
spiderweb looks like of how these different modules
interact with each other. And so Kiro is gonna capture
all of that information for me in the form of these three steering files. And it's gonna do that
for me automatically when I press that button. But that steering directory is open-ended, so I can add whatever other
things I want to add there. So if I have a rule about how
I do software development, I can generate that and add
it to the steering directory. If I have a rule about... Or if I have information about a third-party API that I talk to and I want to be able to be aware of that, I want the LLM to understand
how do I use that API, what does it do, how does it work? I can document that and add
it to the steering directory. And all of these files they live, if we go back to the File Explorer, they live inside of this .kiro directory at the root of my project. So you can see here, we're
starting out from scratch. I don't have anything
in my File Explorer yet except the specs that I created. But as we start generating out more code, this will all get captured
in here as we go along. So does that answer your question? - Yes. Thank you.
- Perfect. - [Ryan Bachman] There's a question. - [Audience Member] Yeah. So you mentioned that we're not gonna
build an OS ever in life in this sort of like
single prompt fashion, which like from a process
perspective probably makes sense, small increments and like a human needs to also understand the
instrument they're working on. Like technical limits. We are blurting out a lot of context. Is there going to be a technical limit? - [Ryan Yanchuleff] Yeah.
So the question there is, is there a technical context limit that we need to be aware of? And just like every LLM
there are context... There's a context window that applies. Kiro has a 200,000 character
context window at the moment. - [Ryan Bachman] Token. - [Ryan Yanchuleff] Yeah, token. Sorry, what did I say, "character"? - Character.
- Sorry. Token window. We have some plans to
release bigger token windows. As the models are evolving, the
token windows are expanding. And so the product is kind
of evolving along with that. If you get to a point where
your token window is full, Kiro will ask you if you want to compact your current session down
and start with, you know, essentially reset your context window. But one of the things about using specs and using them with steering documents, to the question that was asked earlier, is that the combination of steering files and spec files is a really
powerful combination in the sense that all of this information is already documented, largely,
in these markdown files. So if I need to reset my session, if I want to go on vacation
and come back on Monday, I can do that and I
haven't lost a whole lot because I'm detailing everything
here in these static files and I can share these
files across the team. So if somebody else needs to come in and pick up where I left off and do it from their own machine, we don't need to worry about transferring the session details because we've captured all of the major important
points in these markdown files. And so that's a big part
of why we're doing this is because, again, we want
to work on collaboration. We wanna be able to make
sure that every member of the team is working
with the same context and moving in the same direction so that we cut out all of those variables. So to keep things moving here, I'm gonna move from
the design document now and I'm gonna move on to
the implementation plan. And while it's doing that, if we have more questions, I
can certainly answer those. - [Audience Member]
Yeah. I have a question. So let's say we have team where we have business
analysts that use Jira to enter the spec and that. - [Ryan Bachman] So the question is how does this interact
with something like Jira for like product management
and stuff like that? Like, what's the interaction look like? - [Ryan Yanchuleff] Yeah.
So as an organization, my product managers are writing
their user stories in Jira, and I want to be able to use
spectrum and development, but I don't want to create
multiple sources of truth. I don't want to take what's in Jira and replicate it into my repo and then have to deal with drift and the potential of
things splitting apart. And so the way in which you
solve for that is twofold. One, you can install an MCP server. So I can install the Jira MCP server and I can integrate that
with my Jira project. I can enter my credentials, I can use a remote MCP
server, I can use a local one. And I can enter the details
for my Jira project. And then in the prompt here I can say, "Hey, go get the user story ABC." Or "Go get the user story for adding the authentication module to my application and poll that in." And so what that does is it goes in, it gets the information from Jira and it polls that information in and it reads that information and it uses that to create the spec. And so that's how I bridge
that gap from Kiro to Jira. But that doesn't necessarily
entirely solve my problem, it does get me access to that information. It helps me build the spec
so I don't have to write or copy paste all that
information into the prompt block. But what happens if I make a change to the design document or what
happens if I make a change to the requirements document? I say, "I want to tweak
one of these user stories." Or, "I wanna make an adjustment to one of these acceptance criteria." I want to be able to
reflect that information back into Jira so that my
data is staying in sync so that I'm not creating
that drift situation. And the way in which I do that is using the last feature of Kiro that we haven't talked about
yet, which is Agent Hooks. And so what Agent Hooks are, and I'll create one for
you here in a moment. But what an a what an Agent hook is is essentially an event-driven prompt. So I take a prompt and my
prompt in this case would be, "Whenever there's a change
to my requirements document, I want you to summarize that change and reflect it back to the
appropriate user story in Jira. And I want you to run
this prompt automatically whenever there's a change
to a requirements.md file. So whenever you detect a file save event on a requirements.md file, summarize the change and push it back to the appropriate Jira user story." And so what this does now is it creates a circular feedback loop. So in the prompt I say,
"Go get the details for the user story
related to my auth module and poll that in and
generate the spec for it." And then when I go and I make a change to one of the acceptance
criteria in that spec, my Agent Hook says, "I detect you made a file save event in your requirements document. I'm gonna go and summarize that and push that change back to Jira." And that's all happening, that connection there is
happening via the MCP server. The MCP server doesn't just
allow me to read information, it also allows me to write, assuming I have the correct
permissions to do so. And then it summarizes
it and it pushes it back. And so now I have my user
stories are staying in sync with my third-party tools. So things like Jira can
be managed that way. A lot of companies have
their design standards or their software development standards documented in something like Confluence. They have an internal Wiki or they have a SharePoint
server that lays out how we do design, how we
do software development, how we do all of those things. And we can solve for that as well with an MCP server that connects to that. And then a steering file that says, "Hey, whenever you
generate a design document, make sure you go and refer
to our design standards or our architecture standards
available at this MCP server and use that information
so that you're not just inventing some standard
for how you want me to do software development. Use the standards that
I've already established." So that's how you would go about kind of creating that feedback loop. So we can see here now that
we've created our requirements, we've created our design, and now we've created our task list. So our task list here is
essentially the project plan. What are the things that I need to do to go and implement these requirements to this particular design standard? And what Kiro comes back
with is it comes back with this list of things
that need to be implemented, and it's fairly exhaustive. We have, let's see, 17,
18 tasks in this list. And you can see that some
of them are grayed out, some of them are bold and
some of them are grayed out. And some of our tasks have sub tasks, like task two has a task
2.1 and a 2.2 and a 2.3. Some of them are grayed out. What that means is that some
of these tasks are optional. So Kiro's gonna make a
distinction here for me now and it's gonna say, "All right, well are you building an MVP. Do you just want something quick and dirty that you can kind of test out
and see what it looks like? Or are you building a
production grade application? In which case we need
to make sure we cover all the bells and whistles?" And so it's gonna ask me
here in the execution log, "Which one are you making? Are you making a quick MVP? Or are you making a
comprehensive production app?" Since we're pressed on time here, I'm gonna say we're gonna make a MVP, and I'm gonna leave those things optional. And, really, those
tasks are around testing and they're around documentation. Our quick and dirty MVP application here doesn't need a robust unit testing and documentation strategy for it. We just want something
that we can test out and give it a try. And if we look at these
individual tasks here now, we can see that each task
has a checkbox next to it that's gonna track our progress. It's gonna tell us, "Is this task done? Is it in progress? Has it not been started yet?" It's gonna lay out some of the details that that task involves. And then in blue there at the
bottom, it's going to say, "Well, which of the
requirements are we fulfilling by doing these particular tasks?" So we're gonna get some traceability here from the requirements to
the actual implementation. So the first task here has
a button at the top of it that says "Start Task." And when I click that "Start Task" button, it's going to go now
and it's going to switch from Spec mode and it's
gonna switch into Vibe mode. So when I click the "Start Task" button, it's actually gonna go
and it's gonna start actually producing the
code to implement this. So this is gonna involve running commands, it's going to need to
be able to set up React, it's gonna need to be able
to configure TypeScript, it's gonna have to
install the dependencies. And you can see here now that it's gonna get started on that. So it's going to start out by running the create vite command, and it's gonna ask me for
my permission to do so, 'cause it's about to run a
command on my command line, so it's gonna make some
changes to my local code or to my local environment, and I'm gonna have to approve this. And so I can either accept this command, I can add this command to
a trusted list of commands, essentially saying, "I'll
give you permission to this and don't ask me about this again. So the next time you come across a command that looks like this, go
and do it automatically, don't ask me." I can reject the command or
I can modify the command. So here, to keep this simple, we're gonna go ahead and
tell it to run the command. And we can see right here
it ran into a problem. I have Node installed. Why is it not... All right. In its effort
to be helpful here, it's gonna try and figure out
how to do this automatically without the fact that
I have Node installed. We're gonna let this run
and we'll see how it goes. But essentially what it's gonna do here is it's going to kick off and you can see that it's running in the terminal
window here at the bottom. And it's going to start to generate the files that are necessary. So it's creating the vite config file, it's creating the TypeScript config file, it's creating a git ignore
file and the package.json and all of the different
things that are necessary here. So it's creating our main file,
our app.tsx file, our index. So it's going to go through and it's going to create the structure
for my application. And if we switch over to
the File Explorer here, we can see that it is generating
all of the different files in our repository here. So we're getting all of
these things built out for us as it goes along. And we'll figure out why it can't find Node here in a moment. But it's gonna go through this. And you can see in the task list here that it marks this as task in progress. And we've got a little
hash here in the checkbox denoting the fact that
this is in progress. And we can view the changes here that are happening in a git diff. So if I click on this, I can see all the different
files that are being modified and the changes that
are being made to them. And since we're starting
everything from scratch, this is not gonna be a
particularly exciting diff to look at, but you can see
here exactly what's happening. And when it finishes, we'll be able to look at
the execution log as well. So now you can see that
the task is completed, we can view the changes and
we can view the execution log, which means we can come
back and we can see what exactly happened
in the execution log, what commands did it run, and what were the results
of those commands. Notably, we'll figure
out that surprisingly, I don't have Node installed on my machine, and the issue that that created. And so it works through that. At the end of this too, it also tells me how many credits it used, and how much time it took to run. So this particular command,
or this particular task took 2.3 credits, you'll
note the decimal there. Credits can be consumed
in partial fractions. So it's not going to charge
me for three credits, it's gonna charge me for 2.3 credits rather than rounding up. And it took two minutes
and 59 seconds to complete. And so we've got our task here. And so the task now, if we come back to the File Explorer, these files are captured in the repo. So now I can go and I can do a git commit and I can check this
code into my repository and I can say, "All
right, here are the specs that I'm working from." And so if I have multiple
developers, I can say, "All right, well, I want this
developer to do task one, and I want this developer to do task two, and I want this developer
to do task three." And I can divvy out the workload, but they're all working from
the same requirements document and the same design document
and the same task list. So we're all moving in the same direction. And if we had an existing code base here, we could say they're all working from the same steering documents as well. So they all have the same understanding of that core code base. We're not relying on three
different inferences of the LLM to draw the same conclusions
about that existing code. It's all happening and it's documented and it's shared across the team. So we get that collaborative nature that we were talking about. Now somebody asked about what
do we do with Agent Hooks? And so with an agent hook, I can come in here and I can say, "All right, I'm gonna
create an agent hook." I'm gonna say, "Whenever a change is made to a requirements.md file, summarize the changes
and reflect them back to the associated Jira user story." And I'm gonna kick this off. And what I'm gonna do
is I'm gonna tell Kiro to go and create a hook that does this. Now I specified what
I want the hook to do. I want it to summarize changes and reflect them back to Jira. And I told it what files I care about, namely the requirements.md file. It's gonna go off and it's
gonna do the rest here. (audience laughing) - [Audience Member] Looks great. - [Ryan Bachman] Looks good. - [Ryan Yanchuleff] That looks- - [Audience Member] Looks accurate. - [Ryan Yanchuleff] I love live demos. - [Ryan Bachman] Obfuscated code. - [Ryan Yanchuleff] So we can
see here in the hook panel, it's created a hook here with the title, "Requirements to Jira Sync." It's created a description. This is gonna monitor
the requirements.md files and it's going to automatically
summarize those changes and reflect them back to
the associated Jira story. It's going to look for a file save event. There's a couple of
different options in here. I've got File Created, File Saved, File Deleted, or a manual trigger. Essentially that's just a saved prompt. A manual hook is essentially
just a saved prompt that I can run whenever
I want to kick it off. It's gonna tell me the
file paths to look for. It's gonna look for anything
that's called requirements.md. I could tell it to look for any file in a particular directory. I could add multiple different things that I want it to look for. And then we get the actual prompt itself. This is the prompt that it generated based on that input that I gave it. So a requirements.md
file has been modified, please analyze the changes, summarize the changes in
clear and concise way, identify the associated Jira story, and then push the changes
up to that Jira story when you're done. And so we've gotten now an Agent Hook. And just like my specs
and my steering files, these hooks get stored inside
of this .kiro directory, so I've got my hooks here as well. What that means now is that all the users on the team have the same hooks. All the developers now
have the same specs, they have the same steering
files, they have the same hooks. And so everybody is working from the same set of information. And this is how we
solve for, again, scale. It's how we solve for collaboration and it's how we solve for visibility into the actual
understanding of what the LLM is going to do. So how is it going to behave? What are the things that
it's going to perform? And how is it going to go about and actually perform them? Wanna open it up for some more questions? - [Ryan Bachman] Yeah, yeah, we got- - [Ryan Yanchuleff] We are unfortunately not going to have enough
time to actually build this entire application
in the next 15 minutes. And Kiro is spitting a little
bit of gibberish here anyway. - [Audience Member]
Deterministic this process is because it has to be repeatable, right? For everybody? - [Ryan Bachman] Yeah. So the question is how deterministic is this process? - [Ryan Yanchuleff] So LLMs are, as we've said a couple times now, LLMs are by definition non-deterministic. The way in which you make
them more deterministic is to provide more context. So the more guardrails and guidelines and context you can provide, the more consistent the output you'll get. So if I say, for instance, "Generate a web application,"
and that's all I say, and I ask that five times, I'm gonna get a React
application, a Python application, a Rails application, maybe
another React application. I'm gonna get a lot of variability there. But if I add context and I say, "Generate a React application," all five times it's gonna generate a React application for me. So the point being, the
more context I provide, the more detail I lay out, the more deterministic the output will be. And the challenge with
that is that, historically, writing the context of
these three spec files into the prompt every time
I want to do something, it's not particularly scalable because the more expansive
I'm trying to build, the more details there
are and the more gaps I have to fill when I
generate that prompt. And I have to rely on every
member of the team to do that, which is not realistic. So what we're trying to solve for here is we're trying to solve for... Or we're trying to provide
that context upfront. We're trying to give everybody visibility into what that context is
and give them the opportunity to change that context if
they so deem appropriate before we've gone off and
actually done the work. But once we have that design file, once we have those requirements files, once we've laid out what the tasks are, once we've coupled that
with our steering files, we've got a fairly high
deterministic output in the sense that we've
covered all the gaps, we've closed a lot of the variables that the LLM would normally have to go off and figure out for itself. So it's still not 100% deterministic. There's still room for variability. And that's why we don't want it to remove the human in the loop. We don't want Kiro to just take this code and deploy it into
production sight unseen. We still wanna do our poll requests, our code reviews and
those types of things. But what we are trying to solve for here is a lot of wasted time reviewing code that is obviously wrong
because the context wasn't specified upfront. And so by doing this work upfront, we can cut down on the amount
of wasted code generated and we can improve the likelihood that a particular poll
request can be approved as is and merged in. - [Ryan Bachman] Yeah. And
the other thing I'll say to that too is the actual
code that's written, right? If he were to take the spec file, these requirements, and
blow away all the code and regenerate it, it's gonna look different
each time he does it. But that's implementation details, right? The requirements stay the same. How those requirements are satisfied is strictly implementation details. And what we're doing here, I think in essence is abstracting away the details of the code and focusing on the business requirements and acceptance criteria. 'Cause the actual specifics
of the code implementation while able to change is not as important as satisfying the requirements. And that's where you're
gonna see the consistency. I haven't come to this side of the room, so I'm gonna start over here 'cause they've been ignored so far. What you got? - [Audience Member] How do you share things like hooks across across projects? - [Ryan Bachman] Hooks across projects? - [Ryan Yanchuleff] Hooks across projects are shared by the fact that
they're checked into the repo. Oh, sorry, you asked how do
you share them across projects, not across developers. So the way in which you
share hooks across projects at the moment is that you have to copy that hook into another project. You take that JSON file and you copy it into another project. That's not a particularly
scalable approach. And we do have some things on the roadmap and in the pipeline to make
those things more manageable at the organization level to
be able to push those down from an administrative level. But today, in order to
share hooks across projects, you need to replicate the JSON file into the appropriate repo. - [Audience Member] My question
is Kiro ran into some issue. How reliable is this? How often do we run into this? - [Ryan Bachman] How reliable is Kiro? - [Ryan Yanchuleff] How reliable is Kiro? Well, normally I would tell
you that it's very reliable. Now obviously it struggled
on the generation of that Agent Hook. The issue with Node I think
is actually a local problem on my machine, which I will
figure out after this session. But generally speaking, Kiro is fairly reliable in the sense that it has a good
understanding of the source code and it generates source
code fairly reliably. You'll also find as in many cases when it does run into a challenge, and you could see this
actually in the task that we completed, it ran
the command and it said, "Oh, you don't have Node installed." And so it actually self-corrected there and it said, "Well, let
me try something else." And it tried that and
that didn't work either 'cause I don't have NPX
installed either, apparently. And so then it said, "All right, well now I'm gonna go and I'm just gonna generate
the code for you manually. And so I'm gonna skip that
step and I'm gonna keep going." And the point that I wanna make there is that these LLMs are designed
to be helpful by nature. So they want to produce results for you. And so given the context that's there, they're getting increasingly
intelligent in how they work. And so they're gonna try
a particular strategy and if that strategy doesn't work, they're gonna move on
to a different strategy and they're going to
problem solve along the way. And so generally speaking, Kiro is pretty effective
in that regard in saying, "Hey, this is the approach
that I want to take. Wait a minute, this approach didn't work. Let me try a different approach and see if that solves the problem. And I'm gonna keep going." And at any point I can
step in and I can intervene and I can say, "You know what? You're right, I forgot to install Node. So let me pause you right
here and go take care of that and then pick it back up again and have you keep going rather than trying to solve for something that I obviously know is not right." So generally speaking, KIRO is pretty reliable in that sense. This particular example notwithstanding. - [Audience Member] So if
I want to make a change to a requirements document, do I directly do it in that
document or do I ask Kiro? If I'm directly making the change, does Kiro check whether it
will break any other part? - [Ryan Yanchuleff] Yeah.
So the question there was if I need to make a change
to the requirements document, so in this particular
case, we have this spec and we've actually
started building the code. So we actually have
already run the first task in the task list. So what happens now, as is common in life, somebody comes back and they say, "Hey, you know, this requirement change, we don't want red, we want blue. And we need to make an adjustment." What do I do? How do I
actually implement that? There's two ways you can do that. You can actually come back into the prompt and you can say, "Kiro, I need to make an
adjustment to this spec. I need to change it from red to blue." And Kiro will go off and it
will make that change for me. Or I can change it manually. I can say, "You know what? I wanna get the planned date here and also a planned location." And if I put that change in
there manually like that, what I can do is I can hit
the "Refine" button up here. And when I hit the "Refine" button, what Kiro does is it actually goes and it evaluates the
change that I just made to that requirements document. And not only is it going to refresh the requirements document to make sure that this
is logically consistent because I only changed it
in one acceptance criteria, the likelihood is that this is probably gonna need to be reflected in a couple different acceptance criteria. It's also gonna make changes
though to the design. So in the design document, we laid out what the models looked like, what the database tables looked like, all of those different things. Well, now we've gone and
added a new attribute, so we're gonna need to make
an adjustment to that model. So we need to reflect
these changes downstream. So we need to make the change
not only in the requirements, but also in the design document. And potentially, you
know, what this involves, if we had gotten far
enough in the task list that we'd actually implemented
those tables already, we'd actually written the code for them, we would then need to create another task to go in and modify those tables. And so we wanna reflect that
in the task list as well. So what Kiro does when we
hit the "Refine" button is that it says, "All right, I can see
that you've made a change. I've gone through and I've
validated the requirements. Now I'm gonna move on to the design phase and I'm gonna make the adjustments there, and I'm gonna carry that downstream. And if I need to create more tasks because we've already implemented
this piece of the code, then I'll add some new tasks." If we haven't implemented this yet, then I can just modify
the task and I can say, "Hey, do it the the new way
when you go and implement it." So I have a couple of
different strategies there for how to deal with this. But generally speaking that's
how you would adjust for that. You'd make the change. You can either ask Kiro
to make the change for you in the prompt or you can do it manually and then hit the "Refine" button and let Kiro run it through downstream. - [Audience Member] In both cases, Kiro does all these processes? - [Ryan Yanchuleff] Correct. And it's gonna trace that downstream. - [Audience Member] I see that it created a few architectural diagrams. Can it understand these backgrounds if I provide mine for him? - [Ryan Yanchuleff] Yeah. So two strategies there. It created architectural diagrams in the design document
using ASCII text here. And so you can provide ASCII text files that have similar design
diagrams and it can infer those. You can also just draw a design
document on a whiteboard, take a picture of it and
upload it as an image file, and then have it say, "Go and implement this
architecture diagram based on this image," and it will evaluate the image file, infer the contents of that image and go off and actually do the spec or the implementation based on that. So you can do it based
on either ASCII text, those types of implementations, or you can do it based on an image file like a PNG or a GIF or
whatever the case may be there. - [Audience Member] If
I have a Lucid chart? - [Ryan Yanchuleff] Yeah.
If you have a Lucid chart, you can do that, most
likely with a screenshot uploaded of the Lucid
diagram and then use that. - [Audience Member] I have a question. You said that a project can
have more than one spec. - [Ryan Yanchuleff] Correct. - [Audience Member] How
do you define a spec? - [Ryan Yanchuleff] What do you mean "How do you define a spec?" - [Audience Member] In this
particular example (indistinct). - [Ryan Yanchuleff] Yep. - [Audience Member] (indistinct). - [Ryan Yanchuleff] So I want to say, "I want to add an authentication layer to my fitness tracker app to keep track of which user is doing the activity." I'm gonna, again, put this into Spec mode. I'm gonna type in my prompt
here and I'm gonna hit "Go." And what it's gonna do here is that it's going to
create another spec for me. And so... I've got a couple things running here. It's gonna go and it's
gonna create another spec. So the specs here are laid out. I've got a spec directory and
I've got a subdirectory here for the fitness activity tracker. And so that subdirectory
there has my design file, my requirements file,
and my task file in it. Now I've kicked it off and
I've asked it to generate a new spec for my authentication layer. So now I'm gonna add a new feature to my existing application. And so now what it's going to do is it's going to start
building out a new spec for me. And it's going to say... It's actually making changes
to the existing spec for me 'cause I haven't implemented it yet. If it were to build another spec, it would just create
another subdirectory there with three new files, a requirements file, a design file and a tasks file. - [Audience Member] My
question is (indistinct). Requirements for the spec, right? And how do you maintain best practices? - [Ryan Yanchuleff] Sure. The question is around best practices. What's the best way to think about a spec or how to treat it? Generally speaking the way... And, Ryan, you may have
different opinions on this, but generally speaking,
the way I treat a spec is I treat it as a bounded feature. So in this case an authentication layer. And that feature has a
specific set of things that I want to get done. If those things are not done yet, so in this case, we've
got a whole lot of tasks that haven't been implemented
yet, and something changes, I need to add another field, I need to change a color, then it makes sense to go
in and modify that spec. You know, add that feature, whatever. If that spec is done,
all the tasks are done, they're finished and
we've completed that spec, and now you come to me and you say, "Hey, I want to add another thing to it. I wanna make a change." Generally speaking, what I would do is create another spec there. So that spec is done, it's finished, we're gonna put a bow on it, we're gonna slide it over to the side, and now we're gonna create a
new spec for this new thing. Whether it's a change, whether it's a new feature,
we're gonna create a new spec. So I generally try to treat my specs as kind of contained entities. So when I've done the work there, I slide it over, I say, "This is done." If I need to make any more changes, I'm gonna create a new spec
and I'm gonna deal with it there so that I have this
kind of running list of specs. You, technically, can go back
and modify an existing spec, even if all the tasks are done. But I find that that makes it really muddy to be able to keep track
of the work I've done and how I've done it and
to manage it that way. So I don't know if you have any
other thoughts on that, but- - [Ryan Bachman] No. I
mean, I definitely think it's more art than it is science. I mean, there's obviously
gonna be general... Don't put too much into it, right? Like, you have to get a sense. I think what you put into spec also influences how you
organize around that spec. While there is
collaboration aspects of it, I don't think I can divvy up a spec to three different teams, right? So think about boundaries
of the way you work, how you work, and the other, I think to emphasize your point is clear exit criteria, right? Like, it's not an ongoing thing. It's a defined thing that we know we have concrete, discrete
acceptance criteria that we can call done, essentially,
the acceptance of done, and then ship it before
we create another one. So they're not long-living, they're organized around
how we are organized. And, I mean, I don't know, Fibonacci, I wouldn't put in more
than, I don't know, 21? Is 21 Fibonacci.? I don't know, I'm just
making that number up. Nothing too big. - Question?
- Developers? - [Ryan Yanchuleff] Yeah. What
do you do with the developers who are using something other than VS Code and who would rather die
with their VIM application than migrate to something newer? It's a fair question and there
isn't a great answer for it. Q Developer has a number
of different plugins that can be installed. We have a JetBrains
plugin for Q Developer. What we have found though is
trying to maintain plugins for every conceivable IDE under the sun is a very complicated
process and you end up with a lot of leapfrogging and a lack of parity between them. So the strategy that we
have generally gone to there is to recommend the CLI. So the CLI allows you to do a lot of these things directly from the terminal and you can open up a terminal window in JetBrains or in Eclipse or in VS Code, the native version of VS
Code or in Visual Studio and you can do whatever
work you want to do there and benefit from the generative
AI capabilities there in the CLI. And that's generally the strategy we would we propose there. And understanding that that's not entirely the same experience as what you have here, but it allows you to
keep your preferred IDE and still get some of those benefits. - [Audience Member] So
it does come with a CLI? - [Ryan Yanchuleff] It
does come with a CLI. Yes? - [Audience Member] How do you prevent Kiro from hallucinations? - [Ryan Yanchuleff] How do you prevent Kiro from hallucinations? So hallucinations really
are a product of the model and how good the model is and
the training data in the model and then the context that the model has in responding to the prompt. The models that we are
using have all been vetted. Kiro doesn't have a a bring
your own API key strategy to it. So we have a predefined set of models. We have support right
now for Sonnet 4.5 and 4. We have support for Haiku, and we have support for Opus, yeah. So those models are there
and we've vetted them and we've made sure that
they generally understand the context well. And then the steering
files and the spec files add the necessary context. It doesn't guarantee that
you won't see hallucinations, but it does reduce the
load fairly substantially. - [Audience Member] The second part was are you gonna open it
up for like local LLMs? - [Ryan Yanchuleff] We
are looking at local LLMs, but if we do that, they will be defined the same way we define
our remote LLMs as well. So there'll be a defined set of LLMs that you can use that would work there. All right, I think we
have run out of time here. But I appreciate everybody coming out. Hopefully you found this useful. We didn't succeed in building
a fitness application, but hopefully you get a sense for how you would approach that and walk through that process. And I will make sure I have
Node installed next time. Thank you, everybody. (audience applauding)
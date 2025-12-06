---
video_id: 3Y1G9najGiI
video_url: https://www.youtube.com/watch?v=3Y1G9najGiI
title: AWS re:Invent 2025 - Keynote with Dr. Werner Vogels
author: AWS Events
published_date: 2025-12-04
length_minutes: 76.28
views: 17527
description: "Join Amazon.com CTO Dr. Werner Vogels for the definitive developer keynote of 2025. Software developers and architects will discover how their tools, patterns, and practices are evolving in an AI-driven world that demands scalable, reliable, and price-performant solutions. Drawing from AWS's pioneering work, they'll share real-world insights and architectural principles that are shaping modern development. Learn how AI innovations are transforming software development and operations within AWS, ..."
keywords: AWS, Amazon Web Services, AWS Cloud, Amazon Cloud, AWS re:Invent, AWS Summit, AWS re:Inforce, AWS reInforce, AWS reInvent, AWS Events
is_translatable: True
summary: "In his final re:Invent keynote after 14 years, Amazon CTO Dr. Werner Vogels delivers a defining address on the future of software development in the age of AI. Vogels introduces the framework of the \"Renaissance Developer,\" a guide for engineers to evolve and thrive amidst rapid technological change. He dismisses the fear that AI will make developers obsolete, arguing instead that while tools change—from assembly to the cloud, and now to AI—the core role of the builder remains essential. He emphasizes **curiosity** and the willingness to fail as engines of learning, drawing parallels to the scientific explosion of the original Renaissance.\n\nVogels breaks down the essential qualities of this new era's developer: **Systems Thinking**, citing Donella Meadows and the ecological impact of wolves in Yellowstone to illustrate interconnectedness and feedback loops; **Communication**, where he invites Clare Liguori to demonstrate how **Spec-Driven Development** with the **Kiro IDE** can bridge the gap between ambiguous natural language and precise software requirements; **Ownership**, reiterating his famous \"you build it, you run it\" philosophy while warning against \"vibe coding\" without comprehension; and finally, becoming a **Polymath** or T-shaped developer, who combines deep expertise with broad knowledge across disciplines. The keynote serves as both a farewell and a rallying cry for developers to take pride in their craft, build responsibly, and maintain operational excellence even when no one is watching."
keywords:
  - Werner Vogels
  - Renaissance Developer
  - Systems Thinking
  - Spec-Driven Development
  - Kiro IDE
  - AI-Assisted Coding
  - Operational Excellence
  - T-shaped Developer
  - Feedback Loops
  - Software Craftsmanship
---

>> And of the developer. I've
heard that before. >> Hi there Lorraine. What are you doing?
>> Oh, you know, organizing yesterday's program cards,
which got dropped. Figuring out why the machine keeps stopping
on card 442. Logging this really awkward bug in the
compiler and talking to you. Anything new at head office?
>> I've been reading about this. Bubble.
>> Yes, that's the new high level language.
>> It's amazing. Now anyone can write code.
>> I don't know about anyone. Writing software is pretty
tricky. >> Soft.
>> What software? >> Where?
>> You. Marty? >> What you reading?
>> Learning some VB. >> Visual programing. Code
history. Marty. Drag and drop is the future.
>> Drag and drop is still code. It still has bugs. And it still
needs an engineer. >> Everything feels all the
time. >> Is this for real? Could
Claude mean there will be less engineers?
>> Less engineers? Time for an airdrop.
>> Servers in minutes. Scale on demand. Pay as you go. Wow. You
learn something new every day. >> You build it, you run it.
>> WAN. >> Don't forget to call mom.
>> Why there. Marty? Nice wormhole, isn't it? Mind if I
join you? >> Boy? You can skip this one.
>> Is this the end of development as we know it?
>> Or is it just another new beginning?
>> Please welcome the Vice President and CTO of Amazon.com.
Dr. Werner Vogels. >> Okay. Trust. I seek and I
find in you something new for us every day. For us something
new. An open mind for a different view. And nothing
else matters. Good morning. Oh, no it's not. Hello, guys. So
the video showed you every generation of developers that
face the new wave of change. Yeah. Tools evolve,
architectures evolve, expectations evolve. And so do
we. But before we talk about that. Let's talk about the
elephant in the room. Yeah. I've been giving this keynote
since 2012 and I've done all of them. That's a lot of t shirts,
by the way. Yeah. But today this streak ends. This is my
final re:Invent keynote. Yeah. I've still things to do. I'm
not leaving Amazon or anything like that. But I think that
after 14 of re:Invent, you guys are owned young, fresh, new
voices. There are so many amazing engineers at Amazon
that have great stories to tell, to teach, to help you, to
educate you. And I think it's time for those younger,
different voices of AWS to be in front of you. But nobody
forced me to do this. I'm not leaving Amazon or anything like
this. This is my decision to make sure that you get to hear
different voices than just mine. Now let's talk about the other
elephant in the room. Yeah, I visited AWS customers all over
the world, and there is this. There is one question that
keeps coming up in every country and in every city. Wale
AI take my job. Maybe. Yeah, I was transform. Some tasks will
be automated. Some skills will become obsolete. New ones will
emerge. So maybe we should rephrase and reframe this
question. Yeah. Will AI make me obsolete? Absolutely not. Yeah.
If you evolve, there are. And if I look at the past years at,
at Amazon where, you know, we've been using all these new
tools, we've seen how you can evolve over time and still be a
great engineer. We've just a new set of tools in your hands
because we evolve as developers. Yeah, so and so must the tools.
And so change is constant. And this has always been the case.
It's nothing new. Yeah, yeah. Let's go back in time a little
bit. Just for the heck when I went to school, I was taught
68,000 assembler, COBOL and Pascal. Yeah, none of these
languages are being used anymore. And in the 60s, we got
suddenly got compilers, and you didn't really matter any more.
What kind of assembly you those, those compilers spit out,
however, by learning assembly, I knew I learned how that loop
in Pascal actually translated into machine code. And so that
was important to me. And over time, you know, comparison
became the highest level abstractions that most
developers needed. In the 70s. Suddenly structured programing
became popular. Yeah, we're moving towards that. Compilers
are the Bell Labs and Berkeley. They supported this shift. They
give developers a clearer control over flow and help them
escape the chaos of unstructured code. And then a
few years later, Bjarne Stroustrup, he started
exploring how to model real world concepts directly into
coding objects and classes, and that became C++ and helped
shape object oriented programing. In late 1990s.
Amazon was still running as a monolith in 98, and this is his
famous moment. Yeah, the the growth accelerated to such a
point that the team began breaking off pieces of these
monolith into services. And each each service had ownership
of their service, had their own interface. And it completely
changed how developers worked. They moved faster. They became
independent of other teams. They owned. Their systems end
to end. And over time, the industry at large became
adopting these kind of practices as a practical model
for building and and operating large scale distributed systems.
Actually. And what about the tools in those days? Yeah, but
in the 2000, most developers, they were still building and
deploying things on premise. Yeah. And writing code meant
wrestling with hardware, capacity, planning, long
procurement cycles. And when Cloud services arrived, they
changed the expectation of the role again. Developers suddenly
had on demand infrastructure, freedom to experiment without
waiting for hardware, and this required new skills in
developers everywhere adopted the world where Cloud
infrastructure just became the normal way to build and operate
software. My first I'd any guess vi no, I'm not an Emacs
person. Yeah, this is a. IDE. Actually, they evolved with us.
Remember we got Microsoft, had some moment you could actually
draw boxes on the screen, and you had this first real IDE,
and later we got Visual Studio, and Visual Studio Code became
the default because of all the amazing plugins in all of that.
And today's environment are Cursor and Kiro, and that's the
new workflow. Is there a new new workflow next year, five
years from now? Ten years from now? Of course there is. Yeah.
Our tools today, though, I think are kind of extraordinary.
In in Massimo, we already saw examples of developers becoming
dramatically more productive with AI assisted workflows, but
none of this removes the work that only you can do. Remember,
the work is yours, not that of the tools. It is your work that
matters. Yeah, our tools change so many times over the course
of my career, and they will continue to change. We're still
builders. We're still important. Nothing has changed. Yeah.
There's never been a time to be more excited about being a
developer. Bezos not that long ago in an interview, he talked
about this as that we're living at the epicenter of of a
multiple simultaneous golden ages coming together, you know,
space travel, artificial intelligence, robotics, each
are advancing at an incredible pace. But what makes this
moment different is how these breakthroughs actually
re:Inforce each other. Progress in one field accelerates
progress in other fields. And this actually made me think
back in history at the time when that was kind of similar.
Yeah, the Renaissance, the rebirth. Came after a period of
darkness, the dark Ages, the, the, the Middle Ages, the death
plague. And anyone who knows Monty Python knows about how
that looked like. Yeah, but the Renaissance was a period where
everything changed because people became curious.
Curiosity was absolutely exploding. And the result of
that is amazing. Scientists and philosophers. And if you look
at this, you know, the Medici is probably the first version
of a venture capitalist or philanthropist or whoever you
want to name it. Galileo and Copernicus were amazing
scientists. Petrarch, one of the first philosophers. Da
Vinci, will come back to him. But but also evolved at the
same time where their tools, it's not just them because of
curiosity, a pencil was invented. That seems nothing to
be invented today. But there was a major thing. You know,
the fact that they start thinking about something called
a vanishing point. Well, suddenly that if you compare
paintings and drawings before the Renaissance, they were all
flat. Yeah. In Renaissance, suddenly depth appeared and
different lighting appeared in paintings and drawings. And
then these tools, like the microscope and the telescope,
of course, invented by Dutch people. Yeah. Not saying
anything, you know. And then, you know, the printing press,
of course, we all see as sort of the, the pinnacle of
invention in the Renaissance. But that was not just one
invention. And Gutenberg actually used a wine press as
his first step. But that was not the only thing he needed to
invent. He needed to invent Movable Type. Yeah, basically
that you have characters that you can put together. You had
to invent an ink that actually could be put on those
characters. And then paper went to press on imaginary on,
almost imaginary in those days. Yeah. It was a time where art
and science were part of the same conversation. Creativity
and technology evolved together. Now spend some time to think
about what made people so effective in that world. They
were curious. They questioned assumptions. They learned
broadly and applied that learning deeply. They didn't
see boundaries between fields. They built bridges between them.
They were also bold experimenters. They sketched,
they measured. They failed. They tried again. They learned
by doing so. If I take all of that in, I think by putting
that together, I think we are again, in a time of Renaissance.
And you are the new Renaissance Developer. Yeah. Those those
qualities of those scientists in Renaissance are just as
relevant today. So I've brought them together into a framework
that I call the Renaissance Developer. And I want to show
you today, this framework hopefully help you evolve and
be successful in this new era as well. What is crucial, and
all of this is the first quality that you need to
nurture is you need to be curious. Curiosity is critical.
As developers, you always have to continuously learn because
everything changed all the time. And every developer I've met
has this instinct to take something apart and then look
at how it works. And it's also a crisis here. The desire to
understand, to improve, to build, you have to protect that
instinct. Stay curious because curiosity leads to learning and
invention. Equally important for learning is two things.
Yeah, for all new inventions, you need to experiment. And to
experiment. Well, you need to be willing to fail. After all,
da Vinci modeled an airplane that never flew. But we're
flying now. Yeah, and by the way, an experiment is not an
experiment. If you already know the outcome. Yeah, it drives
experimentation, drives to learning. And this willingness
to fail is crucial. But I learned a new language, whether
that is Dutch or English or Portuguese or German. I find
that the same principles apply. The best way to learn is fail
and be gently corrected. You can study grammar all you like,
but relearning begins when you stumble into a conversation and
someone helps you to get it right. Software works the same
way. You can read documentation endlessly, but it is the failed
builds and the broken assumptions that really teach
you how a system behaves. And any of you who have recently
used the Rust compiler knows how much feedback you can
really get. And there is some things that you can only do and
only learn by doing, reading. Watching, listening only takes
you so far, but real learning happens when you engage. When
there is some pressure, when the outcome matters, there is a
relationship between stress and performance called the
Yerkes-Dodson law. The picture is a bell curve. You know too
little pressure and you disengage. Too much pressure
and you're overwhelmed. The sweet spot is somewhere on that
rising slope where curiosity meets challenge. That's when
your brain is fully alert, focused, and ready to grow.
Yeah, you can't reach that point by sitting comfortably.
You have to put yourself in positions that test you. Now,
there's a whole story behind this and that newspaper that
you all found on your seats today, the kernel. There's an
article in there by Andy Warfield who writes about this.
I urge you all to read that article if you really want to
understand more of that. Now learning, there's another side
to it. Learning is social. Yeah, we're not here only to sit in
the room and listen to one person telling you exactly what
to do. The thing you really learn is by talking to each
other. Learning isn't just cognitive, it is social. You
have to touch the glass occasionally. And by that I
mean you have to get out of your usual environment, go to a
user group, attend a conference like re:Invent do I have coffee
with a friend and talk about systems? One of the best ways
to stay sharp is to be around other people who are building
things. And for me, that often happens when I'm on the road. I
travel a lot for work, and those trips keep me connected
to how people are actually using technology, not just how
we imagine they might. This year I was very fortunate. I
took two months long trips, one to Africa, sub-Sahara Africa
and the other to Latin America. In both regions I gave some
talks, but the mostly meet with customers and the real thing I
do is learning from those customers. Here are a few
examples. Yes. Here's AJE. This is actually. Also. It took me
21 years to actually end up on the Amazon. Yeah, and so Grupo
AJE is a beverage company. They support communities along the
Amazon River in a way that they give young people an economic
future so that they don't leave their villages to go to the big
towns. It is a brilliant experience and a great example
of how doing good can be profitable. At the same time.
The Amazon River was was beautiful. I saw pink dolphins.
Yeah, but it reminded something else that I learned that not
all of this is so great. Early in the year I spoke with Boyan
Slat from the Ocean Cleanup Project during an episode of
the podcast, and he told me that 80% of the plastic found
in the ocean originates from just a thousandth of the
world's 3 million rivers. Through the oceans of plastic.
They need not only to clean up what is already out there, but
also to stop new plastics from entering the ocean via these
rivers. And they do that. They've created a River Model
using drones, AI, camera analysis, even GPS tagged dummy
plastic. The place where we went into onto the Amazon. They
actually took plastics and put it in the river. See where it
ended up? Turns out the Amazon is not a big polluter at all.
But this computational model that they've built, these AI
cameras that are on bridges that are on the back of ships.
Yeah, they create a computational model that
predicts how and where this plastic will traffic and
helping them position their cleanup systems for maximum
impact. Now, another thing that totally blew me away on this
trip was actually in Rwanda. In Rwanda, this is the
headquarters of the Ministry of Health. Yeah. And this is their
health intelligence center. In their operation center, huge
screens display near real time data from four different tiers
of health care facilities across the country. They've
built an impressive system that ingests and processes vast
amount of healthcare data, visualizing everything from
disease outbreaks to maternal health outcomes. And they use
it to create new policies. Ekta. They've created this model
which shows that which parts of the country are more than a 30
minute walk away from a healthcare provider, and they
use this data to strategically place new maternal health
facilities in underserved areas. They use data to drive policy
and to actually implement that policy. Another visit that
actually, I mean, most of these trips, I get blown away every
time, especially about how young companies are attacking
some of the world's hardest problems. In this case, we're
we're in Nairobi. And I learned that in many places there,
people will just borrow a dollar or $2 in the morning,
buy some goods, go and sell it to the market or on the street.
And in the evening they will give these dollars back and
hopefully have 40 or $0.50, which they made that day. And
that's enough to go buy some food. Great. It is not enough,
though, to also buy the gas to cook your food. So in those
poorer parts it's all burned on carbon, which is massively
polluting. So this young company called KOKO Networks,
they came up with a completely different solution. They
basically built this kind of ATM machines with ethanol in
them, and a small canister that people have, and they can
basically walk up to the attached to the machine, plug
in that canister and ask for $0.05 of gas, which will be
enough to cook their food that night. Yeah. This is what
happens when developers apply their skills to real human
challenges. Developers have always driven progress. You
have built the foundations of the digital world, and today
you're the ones tuning Turing to AI from from possibility
into something useful, safe and scalable. And developers like
you were essential in the past. They're essential today and you
will be essential in the future. The United Nations expects that
by 2050, we have 2 billion more people on this planet. How are
we going to feed them? How are we going to make sure they have
an economic future? How can we make sure they have health care
that's on us to develop technologies such that we can
help solve some of the world's biggest problems? As as
technologists have that ability to do. And if I look at some of
you who spent so much of their time, not just to actually
build some things in the corner of your room, but actually help
others, the AWS heroes. Yeah, we now have 200. Yeah, they
they deserve an applause. Oh, they're. So smart. Community
builders. I've met AWS heroes, and these are people that are
solving hard problems in their own corners of the world.
They're now 265 heroes across 58 countries. But what
constantly amaze me is how much we can learn from them. By the
way, this year, Now Go Build award goes to Rafael Vincent
Wang Rafael. Rafi Rafi absolutely embodies the
Renaissance Developer. He doesn't just write code, he
builds communities, he mentors others, and he co-leads the AWS
user group in the Philippines. Since 2013. Come on Rafi, one
more round of applause for him. So the first quality, I think
that a Renaissance Developer needs to have is to be curious.
And I like this quote from Walt Whitman. Yeah, we are not what
we know, but what we are willing to learn. Another
quality that I think the Renaissance Developer has is
that he thinks in systems. Yeah. And let me just come with me
for a moment. If you don't really understand it, don't
mean the computer system in this case, but in a big system.
So in the 70s, an ecologist called Donella Meadows Backend
studying how complex systems behave. And she was a computer
scientist. But her insights described our world of software
perfectly. And she wrote, yeah, a system is a set of things,
people, cells or whatever, interconnected in such a way
that they produce their own patterns of behavior over time.
And that was an extraordinary definition, because it captures
what every engineer eventually learns that our systems have
lives of their own. Let me give you an example, by the way,
that is not computer related. One of the most striking
examples of systems comes from ecology. In the early 20th
century, the wolves were removed from Yellowstone
National Park. It seems logical. Yeah, fewer predators meant
more elk meant more life. Yeah, but the opposite happens. The
valleys were overgrazed, the trees disappeared. The rivers
became too began to erode. And this phenomenon is called the
Trophic Cascade. When we reintroduced in 2010 wolves
back into the park. Slowly the park started to heal.
Vegetation returned, beavers came back. Even rivers changed
course. The wolves. The wolves came back. Even rivers changed
course. The wolves. The wolves didn't move the rivers. Yeah
they didn't. They changed the behavior of the overall system.
That single feedback loop, predator and prey reshaped the
balance of the entire system. And when structure changes,
behavior changes. And when feedback changes, outcome
changes. That's what's called systems thinking. So when
thinking in systems, we think in complete systems, not just
in isolated parts. Every service, every API, every Q is
part of a larger system. You can't change one part in
isolation, alter retry policy and you affect load. You add a
cache, you change traffic load, you change traffic flow, you
shift team ownership. You change the pace of delivery.
Each change creates new patterns, some stable, some not.
Every dynamic system is shaped by feedback loops. Reinforcing
loops, sometimes called positive loops, Amplify change
balancing loops or negative loops counteract the change and
push the system back into an equilibrium. May those thoughts
that once you see patterns like this, you start to see where
small, well placed changes might shift the overall systems
behavior. Donella wrote a paper very papers called Leverage
Point places to intervene in a system where you put all of
these things together. There's some words that we know from
computer science on a daily basis. Positive and negative
feedback loops. But you really should read this paper. Call
this homework. Yeah. Come up. Take a picture of the QR code
and that's your homework for the coming week. Yeah. The
Renaissance Developer thinks in systems and to build resilient
systems you need to understand the bigger picture. If I think
about a third quality of the Renaissance Developer is
communication. He she communicates. Yeah. And if you
step into this broader view, you realize that the ability to
express your thinking clearly is just as critical as the
thinking itself. And this is why I believe that one of the
most important things that an engineer or a technical leader
can do for their career is to practice, develop strong
communication skills. Let me give you an example. Let's go
back two years when we did The Frugal Architect. I don't know
if you remember this picture. This is the the Amazon homepage.
And then I explained to you how we had divided that home page
or the overall Amazon system into three different tiers.
Tier one is something that is absolutely necessary to make
the system work. Search, browse, shopping cart checkout, and
reviews. Without those five things, the site doesn't work.
Tier one. Tier two are things that are important to our
customers personalization, recommendations, things like
that. And tier three might be nice to have kind of parts to
be able to do. This is important not just for us as
engineers, but as communication tools towards the business. You
go and sit around the table with the business and talk
about how many nines available does one need to be? O for
nines that will cost you that much? Yeah. Or tier two? Maybe
three nines. Tier three. Maybe you don't care at all. Two
nines, we think. Well, you know, we'll do a manual failover if
the data center data center goes offline. But it's a
communication that you need to have. You need to be able to
clearly describe your system and the capabilities and the
opportunities to the business. Communication is crucial. Now,
human languages, it's a bit of a challenge, isn't it? Yeah.
Although because natural language is ambiguous. Yeah,
but we have so many different senses at the same time. Yeah.
That we can turn this natural language into something less
ambiguous. Yeah. Do we, do we put grammar on the grill or are
we having dinner tonight? Yeah. Even without a comma, you
probably already have figured this one out. Yeah. Now, we've
always communicated to machines through programing languages
because they were precise. We could precisely indicate to the
machine what we wanted it to do. Yeah, but in today's world of
AI assisted coding, we increasingly communicate with
the machine in natural language, which is ambiguous. So we need
to help to develop mechanisms to reduce the ambiguity of that
language and reduce ambiguity of of the human, such that the
machine can create logic. Yeah. Specifications reduce ambiguity,
and our history is rife with stories of spec driven
development. Dijkstra's structured programing
environment before it was based on formal specifications, but
that proved program correctness before you even implemented it.
The Apollo Guidance System relied on meticulous
specifications that guided its 145,000 lines of code, a
blueprint so precise that it helped land people on the moon.
And to talk more to you about specifications, I'd like to
welcome Clare Liguori, Senior Principal Developer on the Kiro
team. Claire, up to you. >> Thank you. Werner. Sometime
last year I started noticing that as I was vibe coding more
and more, I had a communication problem. I was spending more
and more time trying to describe to the AI what I
wanted. The code that the AI generated was good, but the end
software didn't do what I wanted it to do. I would often
try to start over with a new prompt and start all over again
and try again. I noticed that over time I wrote longer and
longer, more detailed prompts trying to define what the
software should do. I would write these long, detailed
prompts in Obsidian and Markdown, and then I would copy
and paste it over to my coding assistant. I was essentially
creating a specification to better communicate with the AI
what I wanted. Software better communicate with the AI
what I wanted. Software specifications can clearly
communicate how a system should behave, what it should and
shouldn't do. And like Werner said, many systems in history
have been based on specifications like Apollo
missions. It felt like specifications were exactly
what was missing from my interactions with my coding
assistant. But then I thought, how could we use this idea of
specs as prompts? What would spec driven development look
like? And this spark of an idea led us to start work on the
Kiro IDE. With this idea, though, we now had a new
communication challenge. How can we communicate and validate
this idea with potential users? We didn't know what it would
look like and we didn't know what users wanted. It was also
kind of difficult to describe what spec driven development
was. They hadn't seen it before and we hadn't built it yet. One
of the best ways to get your ideas across is to quickly
build a prototype, something that your users can see and
touch. Rapid prototyping is, of course, not a new idea. Let's
go back to the 60s to the time of punch cards. In 1964, Doug
Engelbart at Sri had a rough idea for a device that had
wheels on the bottom, and you would slide it across the
tabletop to point to something on a computer screen. And we
can probably all picture this device in our head. But can you
imagine going back to the 60s and trying to describe what a
mouse is to this guy? Engelbart's team rapidly built
a prototype out of a block of wood. It was a wooden shell. It
had wheels on the bottom and a button on top, and this rough
prototype communicated better. What a mouse was better than
any drawing or description could have. It let people put
their hands on it and get the concept immediately. It had
great ergonomics. It felt great in their hands and like the
mouse, rapid prototyping was crucial for Kiro. We knew that
the ergonomics of spectrum and development was going to be
important. How it felt in the hands of a developer. We
rapidly built prototypes of how we thought spectrum and
development could work, and we put those prototypes in the
hands of some internal users, and we asked them to use Kiro
every day. That was going to be the best way for us to
understand what felt good and what didn't feel good. This is
a great example of what AI can do for us now. AI has
fundamentally enabled rapid prototyping for software. I'm
sure that in the past, we've all spent months manually
coding a single idea, and now we can give our users real
working prototypes in minutes to get feedback about what
feels right. Rapidly prototyping Kiro even let us
use Kiro to build Kiro. Our very first prototype of the
Kiro IDE could only do coding, but from that moment on, we
were able to use the Kiro IDE to generate the code for the
Kiro IDE. And by using the Kiro IDE to build out the product,
we were able to iterate through many ideas of how spectrum and
development could work. One idea was test driven
development specs. Taking inspiration from TDD techniques,
you would describe a change that you wanted, and Kiro would
generate tests to validate the behavior that you described.
Kiro would then generate application code and made sure
that it passed those tests, but we found that developers
couldn't always capture the nuance of what they wanted
their software to do or look like. With tests only, we tried
out traditional technical specifications similar to those
that Werner described for the Apollo Guidance System. They
described the system as a whole and each component in detail.
With this, you'd add a new feature to the overall spec,
and Kiro would kick off coding tasks based on the changes that
you described. These specs were great context for the AI, and
even for developers who weren't very familiar with this code
base. But for real world projects, they sometimes became
overwhelmingly long, so it was difficult to figure out where
in this long spec, you should put your changes for your new
feature. We took a step back and we looked at how we already
worked as a team, and we had a new feature idea. We would
describe it, we would work through product requirements,
review a design doc, and create sprint tasks. And we thought
that perhaps specs could follow the same pattern and that
became feature driven specs. We separated the flow into three
documents requirements, designs, and tasks, and we found that
this gave developers more control over the AI and let
them better communicate what they wanted. All of these rapid
prototypes gave us critical user feedback that led to
today's spec driven development workflow. That's in the Kiro
IDE. With a spec workflow now in place in Kiro, we could use
it more effectively to keep building out the product,
because now we could communicate more precisely with
the AI what we wanted. Often with five coding, I find that
we give these very ambiguous tasks to the AI. We might say
build me a web trivia game, and out of this very short prompt,
there's probably a million possible different final
outcomes. But probably only one of those is what you have in
your head. With five coding, the AI is going to take its
best guess as to what you meant. It'll generate code, but that
leaves you to iterate on the code with the AI instead of on
what you were originally meant. With spec driven development,
you have an opportunity to refine what you mean more
precisely through specs. You can give the Kiro IDE that same
ambiguous task, but instead of jumping into the code right
away, it's going to first generate requirements, designs,
tasks. And if those don't match what's in your head, you have
the opportunity to ask Kiro to change it and refine it. Let's
walk through a real example of a production feature that we
built in the Kiro IDE, using spectrum in development system
notifications. We started here with a little annoyance that we
ourselves experience with an early version of the Kiro IDE.
Agents can take a while to complete their coding work, and
meanwhile we would switch away to a different app, but then
the agent would need user input, or it would complete its work
and we would have no idea that it was sitting there idle while
we were away doing other work. So we set out to build a
feature that would notify the user when the agent needed its
attention. We started by having Kiro generate a spec, and the
generator requirements actually helped us to think through some
details, like which agent actions should trigger
notifications to the user. When we got to the design phase,
we'd expected this to be a pretty simple integration into
the Kiro agent code, but instead Kiro generated this
very complex design that would build an entirely new
notification system directly in our agent code. Now, if we had
vibe coded this, we would have ended up with a lot of code
that we didn't actually want, but instead, the spec process
helped us quickly realize this was a much bigger project than
we originally thought. We iterated on the spec to first
focus on building a notification system directly
outside of the agent code and directly in the underlying IDE
code. This needed to be built on top of electrons. Native
notification API Kiro IDE is based on code OS, which is a
code base that spans ten years based on code OS, which is a
code base that spans ten years of development and 2 million
lines of code. It can be difficult for any developer to
figure out where they need to make changes in this code base,
but Kiro spec workflow actually helped us to explore and
understand where these changes needed to be made. And once
these changes were in place, we were again able to use spec
driven development to integrate it into our agent code.
Throughout this project, we were able to quickly iterate on
our specs until we got exactly what we wanted from the AI.
With spec driven development, we would have shipped this. We
shipped this agent in roughly half the time, as if we had
coded it. In our experience building Kiro, we realized that
AI has changed how we communicate and how fast we can
iterate. We can iterate on the software design by
communicating with the AI through specs, and we can
iterate on what the software does by putting real working
applications fast into our users hands and get feedback.
AI and spec driven development helped us to build a better
Kiro IDE, and this was in large part due to more precise
communication with our users through rapid prototypes and
with AI through specs. Natural language doesn't have to mean
high ambiguity. And personally, this is what I think makes Kiro
IDE so special. Kiro IDE brings precision to natural language,
and with that, I'll hand it back over to Werner.
>> Thanks, Claire. Communication is so important
that Claire shows it leads to systems that have fewer
mistakes. Actually. So let me tell you a story again, sort of
out of my own youth, when I went to to computer science
school, there was a class called Interview Technique. And
I go, why interviews? Because you think about journalists and
things like that. No, it was how to learn to talk to your
customer, to really trying to understand what he or she
actually really wanted because they may come to you, or maybe
with a technology solution without knowing anything about
technology. Would it be the first time these days when I
meet a customer who says, what should I be doing with GenAI?
And then because you really trained in trying to figure out
into depth, they are very, very apologized. To answer your
question with a question, but why are you asking me this?
Most of this is fear of missing out. And so really diving into
it with the customer to understand what's the problem
they want to solve, what's the opportunity that they see. All
of that is communication that we as engineers should have.
Now let's go to the fourth, what I call the fourth quality
of the Renaissance Developer. Yeah, the developer is an owner
ownership. I've spoken about it before, but today I want to
focus on one part of it, owning the quality of your software.
AI will let us build things bigger systems, explore more
ideas, move faster than ever before. These tools will, as
the modern day philosophers that punk once said, help us
build harder, better, faster and stronger. And if we use
these tools correctly, they can help us produce high quality
software. But there is a risk in how some developers are
starting to use these tools. Vipin coding is fine, but only
if you pay close attention to what is being built. We can't
just pull a lever on your IDE and hope that something good
comes out. That's not software engineering, that's gambling,
and you need to be out there somewhere for that. Yeah,
remember what I said at the beginning? The work is yours,
not the tools. If you subject to regulatory requirements,
let's say healthcare, financial services and whatever, if I
create some code that suddenly violates the regulatory
requirement, you can't go to the regulator and say, oh, was
I know it's still your responsibility. The work is
yours, not that of the tools. Now, now the other is changing.
You will write less code because generation is so fast.
You will review more code because understanding it takes
time. And when you write the code yourself, comprehension
comes with the act of creation. When the machine writes it, you
will have to rebuild that comprehension during review.
That's what's called verification depth. And it's
one of the two main challenges that I hear when I speak with
developers about this new style of work. AI can generate code
faster than you can understand it. Code arrives instantly, but
comprehension does not. That gap allows software to move
towards production before anyone has truly validated what
it actually does. The second challenge, of course, is
hallucination. Claire showed already a perfect of example of
that. Earlier, the model produced a design that looked
confident but was completely wrong for the architecture.
Some APIs change and LLMs invent attributes that do not
exist. Sometimes they propose solutions that are completely
inappropriate or overengineered, or ignore your system's own
patterns. These outputs look plausible, but are not grounded
in reality. I think we're making progress there. Yeah,
we're developing practices that like spec driven development,
which Claire showed. How can how it can dramatically improve
quality. Byron Swami keynote showed how tools like Kiro can
actually use automated reasoning with your
specification to create code that is verified. He showed how
we can also use automatic reasoning to ensure that code
generated against AWS APIs is correct. I also see many
developers looking at their CI/CD pipelines, then building
more and more automated testing. Yeah, these are all types of
mechanisms here. I want to make a change here. I want I want
you to really understand these two things. There are
mechanisms and there are good intentions. They're not the
same. And let me do that by again, going back a little bit
in the past and telling you a story about Jeff Bezos. In the
early days of Amazon, these executives were required each
year to spend two days with customer service and take calls
from customers so that we would truly understand what the
customers were going through, and not just us lowly
executives, Jeff himself as well. So Jeff sits next to this
customer service agent, phone goes and automated system
already spits up on the order histories of this customer. And
before that, the customer says anything. The customer agent
says to Jeff she's going to return the table. And indeed
the customer returns, wants to return the table because it's
damaged. Code is over. And Jeff looks at the agent, says, how
did you know that? She says, well, 70% of those tables are
coming back because there's some dropshipper that actually
doesn't really know how to package them. Right? Of course,
you know, Jeff gets everybody in the room. And starts to
think about sort of, you know, everybody has good intentions.
No, of course we don't want this to happen. But without a
mechanism, nothing changed because everybody already has
good intentions. So he introduced a new mechanism,
Amazon's version of Toyota's famous Andon Cord. So the Andon
Cord in Toyota was the principle was no car should
leave the production line with a known defect, and then any
engineer working on the line could pull this cord and bring
the whole manufacturing line to a standstill until the defect
was fixed. The Andon Cord that this, the customer service
agents got was a button to make the product unviable. That made
alarms go off. If the people that were responsible for the
polish to go and fix it. But you know, before this,
everybody already had good intentions. But until we
introduced the mechanism, nothing changed. Yeah. Now
let's go back to our technology world. Mechanisms take many
forms. Each team builds their own one that fits the scale and
nature of their work. The S3 team, for example, uses
something which they call durability reviews. When an
engineer proposes a change that might touch durability, they
pause and model the risks. They write down the changes. They
list every threat imaginable, map out the guardrails to keep
the data safe in its mechanism with a very powerful effect. It
turns durability from a property of code into the habit
of the organization. It makes engineers think in failure
modes, not happy paths. And it shows why mechanisms matter.
They convert good intentions into consistent outcomes. Now,
if you think about it, code reviews are also mechanism and
I know it. We all hate code reviews. It's like being 12
years old and standing in front of the class. Yeah, but they're
a very important mechanism because they create a moment
where intent and implementation meet, where another engineer
can question assumptions and catch things that the author no
longer sees. In an AI driven world, they matter more than
ever. In an AI driven world, they are crucial. Models can
generate code faster than we can understand it. So the
review becomes the control point to restore balance. It is
where we bring human judgment back into the loop and make
sure that the software actually does what we expect it to do. I
encourage all of you to continue, and you increase your
human to human code reviews. When senior engineer engineers
work through code together, it becomes one of the most
effective learning mechanisms we have. Seniors bring pattern
recognition and hard earned judgment. Juniors bring fresh
eyes and often spot details others overlook. This is how
WeTransfer knowledge and how we grow the next generation of
builders. AI will change many things, but the craft is still
learned person to person. So the fourth quality in my eyes
of the Renaissance Developer is an owner. You build it, you own
it. The last quality that I want to talk to you about is
that I think you, the future Renaissance developers, need to
become a polymath. Now. My has nothing to do with math, by the
way. It's not mathematics or maths or whatever you want to
call it. It's actually the word polymath has nothing to do with
that. It actually means many because it comes from the. The
math comes from the Greek word Matt Eglin, which means to
learn. It's about having deep domain experience, but also
have knowledge that spans many different subjects. Da Vinci
probably was the absolute best example of a polymath because
he worked across so many different disciplines. He was a
painter, he was an engineer, he was an anatomist, and he was an
inventor. Yeah. Now, I do not expect you all to become a da
Vinci. Yeah, but you should expand your knowledge just
beyond deep domain expertise. Yeah. This is what I would call
an eye developer. An eye shape developer is someone who is
really deep and really highly specialized in one area. Let me
tell you again an interesting story out of my own experience.
This is my old mentor and friend Jim Gray, and Jim got
the Turing Award because actually, you should all know
Jim Gray because he's the inventor of transactions. Every
transaction you do today, we have Jim to thank for this, but
he also had this great mind. He was interested in so many more
things than just databases, and this is one of his famous sort
of challenges. Give me 20 questions, 20 important
questions that you want to ask of your data, and I will design
the system for you. Yeah. One of the first ones he worked on
was the. Sloan, the Sloan Digital Sky Survey. This was
one of the first massive data sets that were out there. It
was groundbreaking work in developing the Sky survey. Yeah.
Jim's in-depth knowledge as a database expert was
transformative for the computation in astronomy data.
Jens actually a really funny story about that. At some
moment Jim goes to Philadelphia. Baltimore, where where the
group is, and he walks into the server room 30s later he walks
out and he tells them that the database layout is wrong, and
everybody looks at him and says, how do you know that? By just
listening to the rattling of the disks, he knew that there
was way too much random access. This intuition, built from
decades of experience, had given him a sixth sense of how
systems should behave. He advised him to redesign the
architecture, and performance improved dramatically. Now, Jim
wasn't what I would call an eye shaped developer at all. His
curiosity reached far beyond databases. He understood people,
he understood business, and he understood a wide range of
technologies. And like great technologists, I would describe
him as T-shaped. Yeah, deep in one domain, but broad in
understanding. The skills you need to be successful in your
job are a unique mix of personal skills, functional
depth, industry knowledge, a database developer who
understands front end performance or cost, where
architectures can make a better architectural choices because
they see how their work shapes the overall system. That
breadth of knowledge gives you the perspective to improve what
you build, because you understand the trade offs.
T-shaped developers combine depth with breadth. They can
dive deep into a specific problems, but will also
understand how it fits into a larger system. That is my
advice to all of you. Build both. Develop depth in your
domain, but cultivate. Cultivate a range to connect to
multiple disciplines and ideas. So the last takeaway from the
Renaissance Developer is become a polymath. Well, I don't
expect you all to become that, but you should broaden your
team. Great developers are T-shaped. They're experts in
their field who understand their work fits into a larger
system. You must broaden your team. Now, if you look at sort
of the Renaissance Developer throughout this talk, I've
called them different ways. Yeah, I think you need to be
curious and keep learning. Thinking systems communicate
with precision. Be an owner. If you build it, you own it and
finally become a polymath. Expand your knowledge. Then
you'll have plenty of time next week to start putting all of
this into practice. But for tonight. Join me at the Las
Vegas Festival Grounds. There'll be great food, some
crazy games, and of course, live music headlined by Beck
and Kaskade. It's a chance to celebrate with your teams and
unwind after a week of serious learning and building. Now
there's one more thing. I want you to leave you with this year.
When you build something like an app, do you customers ever
thought about all the work that goes underneath there? And
Amazon customer will click a button and a package arrives.
Does it think about the people that actually maintain the
catalog, that make that do the supply chain, all of that work?
Nobody sees that. Yeah. Your customers are never going to
tell you that. Your database engineers are doing amazing
work and they love what they've done. Only you understand that
work that goes into it. I believe it is important for all
of us to have pride in our work, in the unseen systems that stay
up for the night, in clean deployments, the rollbacks that
nobody notices most of what we build, nobody will ever see.
And the only reason why we do this well is our own
professional pride in operational excellence. That is
what defines the best builders. They do the things properly
even when nobody is watching. And when I look at the work
that you deliver every day, I see that commitment everywhere.
So for that, I am immensely proud of you. Thank you for all
that you do. Two more. Oh. Two Two more words Werner, out.
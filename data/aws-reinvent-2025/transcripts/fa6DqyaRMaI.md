---
video_id: fa6DqyaRMaI
video_url: https://www.youtube.com/watch?v=fa6DqyaRMaI
is_generated: False
is_translatable: True
---

- Just quick introductions. I'm Kevin Mah, director for Amazon Connect. I've been on the team
largely since the beginning, since we first launched Amazon Connect a little over eight and a half years ago. And it's certainly been the best job and best experience of my life to get to take this business from nothing to being one of the fastest
growing services in AWS history. And I saw recently in the Amazon earnings, we announced that we had achieved a billion run rate as a business, which is a massive
personal milestone for me to be a part of that journey. I'm joined today by Corey and Matt who are gonna come up and talk and have way more interesting
things to say to me about Traeger grills
and customer experience. But I wanted to set a quick baseline today about what a great customer
experience looks like. And I always struggle with this question, which is a weird thing to say considering the role that I'm in, but it's both a really hard question and a really easy question. If I polled the room,
I'd get a bunch of stuff about personalization, efficiency, some intuitiveness and
kind of understanding and all this stuff around, like, getting to know me and adding value. But what I find, like,
it's also really easy because when you see it, you know it. And I'll give you an example. I booked a trip for my
family to go to Asia probably about six months ago. I've been looking
forward to this all year. I want my kids to see their grandparents. And I booked this trip and it's seared into my
brain for December 19th. And I was thinking, it's
the Friday before Christmas, the kids probably won't
have much to school, work will be chill. So I booked it, locked it in, flights, hotels,
excursions, train tickets, the whole deal, had it loaded, and that was the key date, December 19th. Then I find out, this
is five-ish weeks ago, that my son was singing in his
school's Christmas concert. And guess what date it
landed on, December 19th. That wasn't something
I was willing to miss and so suddenly I had
to change everything. And first step, call the airline, is like, okay, I need a different flight. Can I move it, like, 12 hours? Can I move it the next day? What does that look like? And then I had to call the hotel, I had to change the train reservations, I had to change excursions. This was a pretty
frustrating experience, like, and all of these things
were awkward and difficult. Did I have to navigate cancellation fees? Did I have move from
some transferring agent who could do the cancellation and then someone else who
could do the rebooking? And I had some stuff
booked with the points. It was pretty awful, and I think any of us
who are in technology can kind of understand, like, it doesn't have to be that hard. Like, I wasn't doing
anything super complicated. These systems should be able
to understand each other. We could all look and see, a great customer experience would be like, I just need to move it a day. Could you just figure this out for me? But I also think the realists in this room understand why it's not that easy. And so what happens is... oh, I pressed the wrong button, sorry. There's a gap. There's a gap between
the customer experience that we all kind of understand
and should be able to deliver and the thing that we
can practically deliver. And so you look across this complexity, you've got internal systems, you've got siloed data architectures. I've got this private backend database that doesn't have an API next to it. I've got legacy tech debt and suddenly mountains upon mountains of, you know, issues come in that prevent us from providing the amazing
customer experience that I think we all
intuitively understand. And as I kind of tackle this problem, this is probably the number one question I get from executives and
when I go visit customers. It's like, okay, I understand, I want to transform
customer experience with AI, sprinkle some magic AI pixie dust on here and make it agentic and
it's gonna be awesome. Doesn't really work that way,
and the question is, like, how do we get started? Like, what am I actually
gonna do to pull this off? And I typically have
three pieces of advice. The first is something that
we do a lot of at Amazon and what we do is we start from the end. We call this process working backwards. And at Amazon, this process means we write a press release
with a bunch of FAQs and we date it multiple
years down the line and I say, "This is
what I'm gonna launch." And I keep that crystal
clear locked in my mind. And what that does is, as I'm developing and as
I'm adding new features, I never compromise because I always know what that crystal clear
experience would be. And I always encourage customers to do that for themselves too. Like, think about what is this
amazing customer experience you want to provide? Write it down, lock it
in, do not compromise. And that will allow you
to kind of build your way to the end state there. And then my second piece of advice is, if you can kind of put
this down, articulate it, get it to a place where you like it, the next thing that you want to do is start to find ways to
deliver incremental value. And you start looking, it's like, okay, I can't tackle the giant
ocean of going from A to Z, but what are the ways that
I can meaningfully change from A to B? And what are some incremental ways that I can add value, and certainly, like,
demonstrate business value. It'll be kind of one of those CFO things. Like, okay, why are you guys
migrating to Amazon Connect? What's my payback gonna be? How am I gonna shift from a
cost center to a profit center? It's kind of these common
things that you get to make a migration or, you know, change in your technology
stack makes sense. And I think if you have the
vision, you can start saying, these are the pieces, these are the steps that I'm gonna take to get there. So not only can I make
meaningful incremental steps, I can articulate why they're accretive to a longer term vision. And then the third piece of advice, which is a really tough one, and I've only seen, like, the most forward thinking
CTOs kind of pull this off, is to get your data right. I think we all live and work in companies where the data is not in a
place where we need to be. We don't have the full
context of our customers and their experiences
and their interactions and the things they do on
different parts of the website. And if you're looking ahead to the future where we have AI coming
in and personalize things and helping you drive business outcomes, I think the way you're
gonna do this effectively is with data. And if you kind of want to have this immense personalization, getting the underlying
data infrastructure correct is one of those no-brainer investments. You know in the future the data's gonna need to be structured and organized in a way if you're gonna realize
any of this AI value that you kind of need to get up front and say, "Okay, I'm gonna
set up my underlying data, I'm gonna set up the subsystems,
I'm gonna set up in a way that they can all interact to each other." And I think if you can do those things, you set this foundation
to preparing yourselves for what is probably gonna be one of the most
fundamental transformations in our lifetimes. Jumping ahead to Amazon Connect, this is something where I feel this was just kind of the
perfect timing and opportunity and the reason Amazon
Connect came into existence. Like, this was the mindset that we had when we first started this business, knowing that we were gonna need to power these kind of cross business interactions and being able to have AI integrated. And honestly, like, AI has been
pretty good for a long time. It just hasn't been as adopted till we've had this kind of boom over the past few years where the LLMs and generative AI has really inspired people and lowered the barrier to entry to what they can do with AI. And Amazon Connect came in with this mindset from the beginning. One way that I like to
think about Amazon Connect, for some more tech forward people, is that at the end of the day, like, we're an AWS service that's powered by a whole
bunch of public APIs. And if I think of the
Amazon Connect product, it's almost just an
abstraction of a bunch of APIs. You could kind of rebuild Amazon Connect if you wanted to on top of the underlying
APIs that we provide. And the reason that's
important and empowering as part of this kind of agentic future is all of these APIs can
now have MCP servers. All of them can be
understood and talked to across a series of different AI agents. And it gives you this kind of foundation that lets you be ready for whatever AI is gonna throw
at you in the coming years and it almost future proofs
your contact center today. And so I'll skip through the
fun stuff, lots of logos. We are growing like crazy. It's been an incredible
and rewarding thing for me to get to be a
part of this business. 12 billions of customer interactions analyzed with AI over the past year has just been an
incredible amount of scale. We started as an internal contact center for Amazon over 15 years ago and we've grown it to be
something incredible today that I think has fundamentally disrupted what was almost a legacy, kind
of, incumbent stodgy space. This other slide, to kind
of emphasize that point, just shows how much we've grown. When I started this business, the number one customer
question I would get is like, "How serious is Amazon really
about the contact center?" This is not your bread and butter. Like, this is not something that we would've ever
expected Amazon to get into. And that was something I
had to prove constantly in the first three years of the business. Like, I promise we're really
in this, it's gonna be awesome. We might be feature light now, but we are investing and it is growing and it's the thing that we know is great because it powers amazon.com. I don't have to really
defend that anymore, as you can kind of see by our growth, the amount of features we launched, how far we've come, we are very, very serious
about this business. Not only from a higher up the
stack application standpoint, but it has just become
this foundational way that people think about
applying AI to their business. We are one of the most, kind of, proven battle tested applications of AI that is driving real results. And so as we get to Amazon Connect and its approach to AI, I like to think a little bit about this kind of spectrum between, you know, this self-service where
there's less humans involved and on this side there's
more humans involved. The other question you
get all the time is like, "Is AI gonna come and replace jobs and am I gonna need less agents and less humans and interactions?" And we've been at this for a while now and I'm not really
seeing that be the case. What we're seeing instead is humans are becoming way more capable than they have been before and the value that the
contact center provides is becoming much more
than it ever has been. And one of these catchphrases
that we're seeing a lot is the contact center
shifting from the cost center to the profit center. Instead of being this awful bill that your COO has to pay each year, now they see it as an
opportunity to drive revenue, to drive a better customer experience and to drive the things in
your brand that you want. And the great part is, like, we engage at all levels of this spectrum, and I think AI is going to
supercharge these humans that these agents that you already have that are, like, embraced and
well-versed in your business and can now do, you know, 10 x the things that they ever could before. And the only other thing I
wanted to talk about with AI and the way we've kind of approached it, we are seeing a bit of a
sea change in our business where rather than kind
of AI for AI's sake, what we're seeing is people are using AI to drive business outcomes. And some of the legacy
contact center metrics that you might've thought of before, average handle time and, you know, longest contact in
queue, things like that, still good, still
meaningful, still valuable, but I see more and more
companies now shifting to, you know, what is the
revenue conversion rate? How am I actually driving, kind of, top line or bottom line fundamental changes to my business? And what happens is, it forces you to think of your contact center as more than just the contact center. It's this piece that
kind of is the lifeblood and the heart of your business and allows you to extend what your contact center
agents had been doing into other parts of your business and finding other ways to add value. And the other part of this kind of pipeline for AI that we're seeing is that what's happening is, Amazon Connect is
treating your human agents the same way that we treat the AI agents. It's the same set of tooling,
it's the same set of software. And when you can kind of do it that way, I have this performance
evaluation product that says, "Hey, let me see, was
this agent empathetic? Did they solve the problem? Are they, you know, selling
the right conversion rate and things like that." I can apply that exact same
evaluation to an AI agent. And you start to get this pipeline where what you're learning
from your human agents gets to be something that you
can teach to your AI agents and you start to build things that were more human involved
into less human involved. And you're learning and building this flywheel for your data and that data is eventually the thing that is driving the business outcomes. And at Amazon, you know, we were founded on the idea of flywheels and I think every contact center, every business here has the opportunity to use their data, use their customer experience
to drive their own flywheels. And so enough about me kind
of just talking the talk, I want to introduce an incredible customer who actually walks the walks and delivers an amazing
customer experience. Welcome, Corey. - Yeah. Good afternoon, everyone. My name is Corey Savory and I am the Senior Vice
President of Customer Experience for Traeger grills. Anyone hear of Traeger? All right, great. It was a busy week for me last week, I'm sure you can imagine. Thanksgiving is the number
one cooking day of the year and it was exceptionally busy this year with everyone cooking on their grills. I joined Traeger going,
oh, over six years ago. At the time I was living, when
I got the call from Traeger, in the Boston area, which is
where I'm originally from. I had moved back there after considerable time on the west coast working for companies like DirecTV and moving out to the east coast to take leadership of CX for a company called iRobot that makes cute, adorable little vacuums, little robot vacuums. And I was really happy,
I was finally home. I was around people whose
accent sounded like mine and I felt really, really good. And then I got this call from
a company called Traeger. And what I loved about it, is I had been a customer
of Traeger for years. I bought my first Traeger grill when I was living in the Denver area. I assembled it myself. I reloaded that grill around the country from one state to another all the way to Massachusetts. And I'd been in Tokyo on business. I was out visiting my
team in the Tokyo area, came home, and on my back
deck, for Mother's Day, was a brand new Ironwood 885,
a connected Traeger grill. I'm gonna say it's the best grill. It's my absolute favorite. Trust the person that
runs customer service, it's an amazing grill. And a week later, coincidence, I get a call from a recruiter asking me if I've ever heard
of a company called Traeger and they were looking for someone to come lead CX for Traeger, where it was pretty easy to convince me to move back to the west to go work for such an amazing company. And the thing that really lured me in about working for Traeger wasn't just that I was
familiar with the product and I had been using it for
over 10 years at the time, but because of the way that they described the state of customer service and customer experience at Traeger. There was no CX process. Customer experience as
a concept didn't exist. They were strictly talking call center. They were strictly talking, we need to stand up customer service. The state of customer service was abysmal. And I thought that that sounded
like the absolute best thing that I could have the
opportunity to go tackle. So when I came to Traeger
in September of 2019 with the global pandemic on the horizon that I had no idea about, what I walked into was a state where we had zero control
over our technology. The only technology that
Traeger had at the time was a CRM designed by a team of people who I don't think ever
once sat next to an agent or ever once walked into a contact center. Everything else we relied
on our BPO partners, their IVR, their data, their reporting. They would report to us
how they were performing. Sounds like a great situation. They actually told me
that they had 85% CSAT and 80% first contact resolution. I knew that wasn't the case. And when I was able to
stand up Amazon Connect in over a weekend, immediately having access to our own data and was able to baseline
for the first time, what the reality was,
was we were at a 35% CSAT and a 30% first contact resolution. But Amazon Connect, we
were an early adopter. We got in super early
and had been partnering with the Amazon Connect
team from the beginning to help us design our customer experience infrastructure and technology and leverage it as a
really robust ecosystem. So working with the Amazon Connect team over the last six years,
we started small, right. We took on telephony, we were able to start
taking calls, routing calls. We also stood up QuickSight. I love QuickSight. I tell everybody that is in the business how much QuickSight has
really allowed me and my team to hone in on areas of opportunity
and data visualization. And now with a lot of new
features built in with AI where you're able to have a conversation with your data, it's just great. We then adopted sentiment
analysis transcriptions, allowing us to start standing up a true customer experience ecosystem where now we can analyze our data and not just take calls, understand why people are calling us, understand why, when we send
a part on a particular grill for a particular reason,
it isn't fixing the issue, allowing us to start elevating issues coming through the call center to our product and engineering teams. That was very exciting at Traeger. Previous to that, customer
service was seen as, as I said, the call center. And then this is really what enabled us to have a seat at the table and truly help the business understand what customer experience is and how the data that we have should feed into product development and should feed into product roadmap and understanding customer experience. We've also launched chat. We've built video streaming. For anyone who does
technical troubleshooting in a call center, I will tell you video
streaming is a game changer. We're able to, through our
Amazon Connect instance, send our customers a text
message that you can click on. The customer then, it activates the camera on the back of your smartphone and streaming live to
our agent's desktops, we can see exactly what
the customer's seeing, not spend time asking 20 questions and trying to get the customer
to explain in their words what they think is going on. Our agents can now see with their own eyes exactly what our customers are seeing. And that really helped us improve our first contact resolution. We've launched screen
recording with Amazon Connect, also been a game changer
in helping us understand process improvement opportunities. And then the end phase six and
seven and whatever is beyond, I'm gonna be talking to you today more later in my presentation about two things that
we've been working on. One that I've coined as
self-healing contact center and the other is our single
pane of glass instance where we're using generative AI. - Hi, hey everybody, I'm Matt Richards. I'm a senior solutions architect at AWS and I have the distinct pleasure of working with Corey
and the team at Traeger. And I'm just here to hype Corey up and talk a little bit more
about their evolving story here. So, let's talk about what comes next after Corey spent this
time building up a mature modern customer experience organization, they recognized that there
were still limitations in place and most of these limitations were around the experience of the agents. As we have a lot of these conversations about a modern call center, a lot of the conversations center around how to make the agents more effective, how to let them have more efficient access to data, to resources, help them help the
customer more efficiently. And what they recognized is that evolving their agent experience beyond what was in place was getting increasingly difficult. And that was mostly because of a lot of disparate user experiences for the various parts of their ecosystem. For instance, a lot of
the customizations came in through customizing their CRM for doing things like case management and basic customer management. And the agent would have
to go back and forth between their Amazon Connect experience for the live calls and the chats with their CRM to handle the casework. And because of these
disparate experiences, the agent would constantly have to hop between many different screens. There was a lot of cognitive overload, it caused a lot of
additional training time and then adding on any additional
customizations after that really took a lot of
work and a lot of time. So these are the challenges
that they were up against. They wanted to find the next step to make the agents more effective. And so this is where we get
into Amazon Connect Cases. Connect Cases is an integrated
feature of Amazon Connect that allows for agents
to do customer issue work that may require more than one interaction with that customer. And the thing that this could really give was an integrated user
experience for that agent where they could be in the
Amazon Connect experience and handle every part of the lifecycle of that customer interaction,
that customer touch, without any additional screens to go to, without looking through manuals of what's the tool I need to go into to get this thing done. Makes the agents more effective, it gets the new agents
onboarded much, much quicker. And they didn't have to
spend a bunch of time customizing a legacy CRM and everything could be a one stop shop. And this was really, really huge for them. And it was also extremely important because Traeger had another
big evolution in their company in the form of Meater. I'm gonna pass it back to Corey to talk about this
specific set of challenges. - Yeah, thanks. Anyone hear of Meater, M-E-A-T-E-R? All right, so in 2021, our world got, welcomed a new friend
into the Traeger hood with our acquisition of
a company called Meater, a wireless meat thermometer,
intelligent meat thermometer. And we let them stand alone for years. They operated out of Leicester, England. They were very much keep at arms length, let them operate on their own. And we let it go that
way for years on end. Until last year, the beginning of last
year, January of 2024, I was asked to take on
customer service leadership for the Meater brand as well and integrate Meater customer support into Traeger customer support,
into our contact centers. Well, we'd spent years
building our tools and systems to work for Traeger, for how Traeger tools and systems work, how we do warranty claims on Traeger. And then within a matter of four months, we had to stand up a complete
customer service organization to bring Meater into the contact centers. Of course that includes writing training, writing a knowledge base that didn't exist and doing all of the additional prep work. But from a systems perspective, we were shoehorning Meater into a system that was built for Traeger. And it was enough for us to limp along, but it was a very awkward agent experience when they take a call. And if it is a Traeger call, I have to handle it this way. If it's the same type
of call but it's Meater, I now have a whole
different set of screens and a different way that
they had to process support on the Meater side because we had to run
really, really, really fast. We had a deadline for when the phone calls
were gonna start coming in and we had to start
taking on Meater support. So now I have this system
that wasn't too bad, that now isn't working
exceptionally well at all for our agents and adding additional cognitive load and stress and pain on them to have a second set of systems and our main CRM that isn't designed to be able to support Meater. So that was another great
opportunity, just like I said, when I was super excited
to come to Traeger, when I heard just how bad things were and what a great opportunity it is to build from the ground up, we had the choice to make, to say, do we take the time and the investment to go into our CRM and modify it and rework everything
to do with making Meater flow a lot better? Or do we leapfrog in
technology to something modern that we can build from the beginning, that has the right process flows and the right agent experience
for both of our brands and do so simultaneously. And that's what we opted to do. We wanted to evolve our
experience in customer service. We didn't wanna take a step back in any of the great work
that we did with Traeger. We didn't wanna lose a
whole year of our innovation and the way that we move fast to take the time to rebuild Meater. We made the decision
to move to Amazon Cases within Amazon Connect. We refer to it as single pane of glass because to our agents, they have the experience
of a contact coming in. Based on the phone number called we know if it's a Traeger interaction or a Meater interaction. The account information pops, the agent is then just
asked to pick a button. Is this an about an order or is this a technical
support interaction? If it's about an order, up
pop the customer's orders. Is it one of these? If it's about a technical interaction, up pop the devices that are
registered to the account. Whether it's Traeger
grills or Meater probes, the agent can select, it's about this one. If they have to register it, the agent can then enter the serial number and register a new product. We're also working with
some modern AI technology and another partner on
IVR bots and chatbots to assist us with handling
some of that registration work offline from our agents. But what we wanted to focus
on was not necessarily about trying to get contacts
out of our call center. It wasn't about how to remove
the customer from the agent. It's what Kevin was talking about. It's more about how do we
make the job of the agent one that is easier, more streamlined, something where our agents
are able to spend less time thinking about what screen to navigate to and what piece of information
that they're looking to find, but that they can focus
on the interaction. At Traeger, we talk
about the Traeger hood, it's all over our advertising. But if you ever come to our office, you'll see that we live and breathe it. We have lunch together. Matt, I think comes a lot for lunch to Salt Lake, to our office, but we do have a full
culinary staff on site. They do all of our recipe testing and all of our recipe writing and they cook delicious
food for us every day where we sit around a table, and we're really passionate
about the Traeger hood. And the feeling that we wanna
give in customer service when you're speaking to an agent is as if you are talking to
someone on your back deck, that feeling of a neighbor
next door that you are helping. Grilling, cooking, cooking
with Meater probes, cooking with our grills, is really about the emotional connection around food and around preparing food and sharing a meal with
someone that you care about. Hopefully you don't have
people at your table that you don't, but that's the feeling that we wanna give when we talk to our customers
in the Traeger hood. It isn't us trying to keep
you from contacting us or having a organic
interaction with our agents. We really wanna focus on
how do we make the job of the agent easier, faster, so that they really lean
in and spend that time creating an amazing relationship
in the Traeger hood. So we deployed Amazon Cases, our single pane of glass solution, where all of the process flows, where agents would have
to use a knowledge base that would tell them step 1, 2, 3, 4, of how to process this
particular type of transaction. Now we don't need that anymore because the tool is so intuitive. As I said, the agent clicks on the button, this is what I want to do. And we've built it in a way that it is seamless to the agent what's happening on the back end. It doesn't matter which
order management system is processing the order
for Traeger versus Meater. The agent just needs to
tell single pane of glass what it is that they want to do. And we've built everything on the back end to be completely seamless for them to have to actually process
any of the transactions. We built it in four to five months. We had a goal that we wanted to deploy in June of this year and we started working
on it in about February, I think, February. We put requirements together. We documented our requirements
in December, January. We started working on it in February and we were up in, in four to five months with a complete build of this solution on top of our Amazon Connect instance. We deployed in June and July. We rolled to our contact centers and immediate removal of our old CRM, which was a huge cost savings for us from moving from a licensing model to, you know, the model with AWS where you're paying for
data and not licensing. And that was also part of our deadline, was we were about to hit
renewal with our CRM in June and had to get out, (chuckles),
before the renewal hit. So a little bit of added pressure, but it was a very, very
quick implementation timeline for something that really is a complete new CRM, essentially. But for us, the benefit is our agents had already been using
Amazon Connect for years for interfacing with our
telephony and our chats and sending those text messages, and video streaming was all built within our Amazon Connect instance. So the tool itself was
familiar to our agents where we just provided
them this new experience. And what that led to was a 40% reduction in
training for new hires. Our path to proficiency
is light speed now. When bringing somebody in off the street, now we have to train them, of course, on how our products
work, how a grill works, how a Meater probe functions. But we were able to carve
out over a week of training that was based specifically on how to navigate this CRM and how to process transactions, because the actual processing, as I said, of the transactions is
removed from our agents. And what we're finding is agents who we brought in and trained only knowing single pane
of glass as an experience outperformed tenured agents within hitting the
floor in nesting period. And we also have seen a bump in our agent satisfaction as well. We operate in the 92 to 93% top box CSAT, and this has allowed our agents to improve our scores around connection and relationship building with our customers on the phone because they don't have to spend the time focused on what they're
doing in their tools and how to do it. Ah, there's our Traeger hood. That looks really good. All right, so what are
some of the other benefits of our single pane of glass instance? It's not just about the workflows
that have been built in, it's also AI generated
case notes and emails. So the time that it takes agents to type what happened on an interaction, what they did, to leave
notes for the next agent, our agents don't do that anymore. The AI that is present
within the interactions is doing all of the case summaries and leaving case notes on single pane of glass
for the next agent. So the time it takes to do
that, as well as emails. If you're a Traeger customer,
anytime you contact us, we will follow up that
interaction with an email to you with important information
that you need to know. It would take time for our
agents to generate those emails and because we didn't use templates, we wanted everything to feel
Traeger hood and very familiar. I will tell you our agentic email bot is a lot better at writing
emails than our agents ever were. (Corey chuckles) And I think that it's
also important to note that due to budget constraints that I think that we all
feel as a cost center in being asked consistently
to optimize and reduce costs, we've moved our contact centers, not just offshore but really offshore. We are in Cairo, Egypt now and we are in Johannesburg. Native English speakers in Johannesburg, but certainly not in Cairo. And we've been in Costa Rica
and Guatemala for a while. We found a lot of complexity
in moving to Egypt with our agent base being
native Arabic speakers and that it would take them a long time to write notes to leave on the account, to write those emails
follow ups to customers. And I think regardless of the location of where your contact centers are, one agent to another, the variability in how
one agent takes notes versus another agent takes notes. Some, you tell that agent, you didn't need to spend a
half an hour writing this book. Another agent, you might coach them that they could have added more context to the notes that they left. And because now we've left that to, up to single pane of
glass to our agentic bot that is working with us in Amazon Cases, our agents don't have to do that anymore and the consistency and
variability is removed. Easy for anyone to understand. And as I said, I keep calling her a she 'cause we have a bot we call Traegy. But anyhoo, whether it's Traegy or our Amazon Connect instance, the consistency, the tone, and the way that we can
train how to write these is really providing, in my opinion, a really great customer experience. Alright, a few other things. I mentioned this thing called
self-healing contact center. Who's ever had a catastrophic event where maybe your website
went down or your app crashed and all of a sudden, unplanned for volume hits your contact center? Right, you can staff as much as you can. You do your intervals, you know how many agents you need, but when something unexpected happens, it can topple a call center. And this happened to us a few times. I won't go into details, but what happens is your call center becomes flooded very, very quickly. Right, and you scramble
to maybe put a message at the top of your IVR saying, "Hey, if you're calling
about the website being down, we know. (chuckles) Or if you're calling
about the app crashing, we know." But by the time that you
have identified the issue, that you have taken the time to put a message to your customers, they've missed it, they're in queue, and now you're buried. So what we've worked with Amazon Connect, the AWS team, on last year was this concept of self-healing, where the tool is smart enough to know how many agents I have working, what my handle time is, what the volume is coming in and at what rate that
I'm going to get buried. And at the rate that it sees that we're about to get to a point where we are never gonna dig out of the debt hole that we are in, we turn off callbacks automatically. We stop offering them. We turn chat off to stop ghost chats from coming in. And we monitor it. And by we, I mean the
tool, not me, (chuckles). The tool monitors itself to the point where it
knows I'm caught up again. It's okay, turn back
on offering callbacks, turn back on some of
these other functions. What we want to do is be able to deliver the best service that we can. But if you've ever been in a position where your customers have left the chat and you're just answering
ghost chats all day and trying to find a customer
at the other end of the line and you've got hundreds
of customers in queue, if your call center can note that itself and start to look for
opportunities to reduce those, you continuing to build upon the problem. And then I also mentioned, we are working with a
partner on AI technologies in our chat and in our IVR. As I mentioned, her name is Traegy. We don't tell customers that
that's her name, internally, and we love her and she
does a fantastic job. So we are doing things
like where's my order and, like, trying to actually
reduce those contacts from ever getting to agents. But what we found more successful and better fit for our, ooh, our philosophy on customer
service in the Traeger hood is looking for non-value added
work that we can have her do. Like, you contact in, you're saying that you're
having a technical problem with your device. She can say, "I noticed you
don't have a registered product. Before I pass you to an agent, can I just take a moment and have you text me a
picture of your serial number and I'll get that product
registered for you?" So trying to not be
invasive with the customer but also trying to strip away work that is non-value add for an agent to take the time for you to say an alpha numeric serial number that's 17 characters long. That takes time on a contact where we want our agents
focused on other things. And we're seeing great success there and looking forward to
continuing to work and develop. So as I wrap up what I
have to share for today, the other thing that we absolutely love about working with Amazon Connect is that we can move fast. As I mentioned, we
brought Amazon Connect up over the course of a weekend. The speed at which we can
develop where we're now, especially in single pane of glass, and we have no ties to any further development
within our old CRM. We can move as fast as we can code as opposed to the situation
that we were in before. And thank you. Matt. - Alright, well we're
going to get into the Q&A in a minute here. Before we do, wanna do a quick plug. There's gonna be a lot of
really great conversation about Amazon Connect and other customer experience topics happening through the
rest of the conference. You can see here there's two per day through the rest of the week. So if you wanna spend your entire time immersing yourself in Amazon Connect and all the Amazon Connect things, plenty of opportunity. Take a picture, go to those sessions, they're all gonna be wonderful. - Well, thank you for the opportunity to talk with y'all today. - Yeah, thanks everybody.
- Thank you. (audience claps)
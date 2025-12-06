---
video_id: YOQlbZojPB4
video_url: https://www.youtube.com/watch?v=YOQlbZojPB4
is_generated: False
is_translatable: True
---

- Alright. Hey, welcome to re:Invent. This is our first talk for re:Invent. Probably for a lot of you
is your first talk as well. Thank you for coming. We really appreciate you
guys coming and your support. Today's topic is gonna
be really interesting for many of you. If you haven't been under a rock for the last year, you've
heard something about GenAI, you've heard something
about the agentic experience that's creeping into
all of our landscapes. For many of us, this means
taking the existing applications we have and transforming them to be part of the agentic revolution, right? It's not enough to simply say, Hey, we've got this existing application. We're gonna just rewrite everything. Most of us who live in the real world, know we have to deal with all of our applications and
everything that we we've built. So today's topic, transforming from SaaS to multi-tenant agentic
SaaS is really topical for a lot of the people that I talk to. The customers who talk
to me aren't interested in just creating new things and toys. They have applications,
they have customers, and they wanna make these things that they have work for their customers. This is a 300 level talk. So we are gonna set the
baseline a little bit in terms of some of the basics. We're gonna talk about the
SaaS fundamentals a little. We're gonna talk about
some agentic fundamentals. We're mostly gonna focus on
the transformation aspect of how you take existing applications and build them into an
agentic SaaS application. My name is Bill Tarr. I'm a principal partner
solutions architect, and I'm lucky enough to be
joined by Ranjith Raman, also a principal partner
solutions architect. Before I dive into this,
I wanna spend a tiny bit of time telling you about
something else that's going on. This year a couple of our
breakout talks are lucky enough to be accompanied by a workshop. So if you're someone who
likes to get hands on, if you wanna get your
hands dirty, you like going through a workshop
flow, feel free to come. We actually have two sessions
Monday and Wednesday. Now, they're both listed as
full on the catalog already, but as you can see, not everybody shows up for every session. These workshops that we have for SaaS are definitely
worth waiting in line for. If you have the opportunity to go and check them out, please do. If you don't, don't stress. One of the things I regret most after every re:Invent is a lot of people don't realize all
of our workshops are public. If you see them here, you can go find them in our workshop catalog. If you don't reach out
to your account essay, and they will help you walk
through these workshops and find them. They're great resources. They're also generally
backed by GitHub repos. You can usually find the code that lives behind the
workshop as well, publicly. So with that, let's move into
the content a little bit. The SaaS value proposition. I said I'd set the
table just a little bit. If you've ever heard us
talk over the last six years about SaaS, you've heard
a lot of these topics. How do you scale an application? What does it mean to be
efficient in building and operating your solution? How do you achieve the agility to rapidly add innovation
for your customers? And how do you let your
customers gain value out of your software as quickly as possible with frictionless onboarding? And then getting into
the more technical side, how do we deploy our SaaS applications? What does it mean to have
isolation between our topics? How do we do different price tiering and then data partitioning even? How do we take our data, our tenant data, and separate it out from other tenant data for cost and operational efficiency? All of these are just the
general SaaS value propositions, and most of, you're probably
familiar with them already. Now, in this new world of agentic SaaS, what we're seeing, and what
I think is gonna remain true, and you'll see throughout
this talk, is all of those SaaS value
propositions are inherited by an agentic SaaS solution. We don't absolve ourselves
from the responsibility to do any of these other
things in agentic solution. Yes, they're fast to build. You can crank out an
agentic application quickly, but it doesn't absolve us from having to think about what it
means to deliver that, that agent at scale
about how to operate it. And so people aren't
constantly crunching buttons and redoing the same tasks. How do you create agility? How
do you do tenant isolation? All of these topics are the foundation of what we're gonna be talking about in terms of agentic SaaS. Now and into the near future as we start to see more of these
agentic applications start to reach production and actual customers. What do we mean by Agentic AI? Well, just in general, when
we're talking about agentic AI, what we mean is a system that
has a high degree of autonomy and the ability to make decisions. But maybe the last part of
this, where we're actually (chuckles) saying what it's not highlighted
with minimal human insight is what I'd like to highlight
and emphasize for you. Because agentic solutions
have a lot of capabilities, but they don't have the capability to continually make decisions
on independently, especially in highly valuable or
highly regulated industries. Being able to make it easier
for humans to do a lot of the existing tasks is
really the cornerstone of what I'd say is important for a SaaS transformation
into agentic SaaS. Taking off some of that heavy lifting from your individual
operators and putting that into agentic solution to
help make them more optimal. That's when we're starting
to talk about agentic SaaS, because we're talking about
injecting SaaS app agents that do planning, building, and operating, which are the same tasks that humans do today in
operating a SaaS solution. And agents behave
similarly, but not the same. They have different usage patterns, which unlocks new capabilities. There are things that agents can do that humans simply couldn't
have done operating a SaaS. They can't sit there 24
hours monitoring the state of your customer's application. Agents can't. They can
replace outdated processes. Oftentimes, we have lots of humans mashing buttons
running reports over and over again, or monitoring operations. Those can be replaced or
enhanced by SaaS, SaaS agents. And of course, just removing
the undifferentiated heavy lifting of things that we
have to do repetitively, like onboarding processes. Now, when we talk about SaaS,
you've probably heard us say before, SaaS is a business solution that has technical implementations. We always wanna start
from a business use case and work backwards from
that into the tech. So when we're thinking about SaaS agents, or agentic SaaS, we wanna
start thinking about that technical implementation and what that means from
an agentic perspective. For example, attracting new
customers is pretty much key to any SaaS application. If you're not attracting new customers, you're probably not gonna
be particularly successful. Maybe some of the ways we can
do agentic implementations that might enhance that business strategy,
it's model selection. Could having different level of models and different price points allow
us to differentiate product for different types of customers. So we can go up or down market in terms of the offerings we're making. Could we do different integrations? So A2A agent, technology,
MCP model, context, protocol. Both of these might be
familiar to already. They're simply how we talk
to systems either remotely or locally that allow us to
unlock additional capabilities. Again, in SaaS, very few
SaaS applications are simply a bunch of code. They're a bunch of code that integrates with third party providers. Are you using Stripe as
your billing provider? Are you using Datadog
for your observability? All these different platforms are evolving to have their own A2A and MCP stories. Now, what does this mean
for attracting customers? Again, it can give you some flexibility. Can you integrate with different products that you couldn't before? Can that unlock different capabilities for your customers,
perhaps in new industries, which weren't inaccessible to you before? And how do you retain customers? Well, if you operated a SaaS, reliability is the cornerstone of this. If your system isn't reliable, if they're having irregular experiences, of course they're not gonna
be happy with your platform. Can you actually do agent evaluation? Can you do additional
testing to your platform that you couldn't before
because of how AgentCore and the different operations
it unlocks can do? Could you actually enhance
your customer success story? And this is one of the real stories that we're hearing more
and more from customers, is that the customer success teams
are increasingly using some of these tools like
automation and user flows. Not to eliminate the humans who know what they're operating on, but simply focusing them, bringing them to the right tasks at the
right time to help customers who have specific needs. And easy discovery and onboarding. This could mean all sorts of things, but how you select frameworks
in terms of your agentic story that make it easier for you
to rapidly onboard customers. And of course, identity and authorization has
always been a little bit of a sticky widget in terms
of onboarding customers. Can the agentic story reach out and figure out how, what
those identity stories are and help customers set them
up without human interaction? All of these can be ways that you can improve your SaaS business by using agentic implementations. Now, agentic SaaS comes in
a few different flavors. And we are talking about
transformations today, right? So sort of keep in the back of your mind. There's gonna be lots of
talks about how you just write a new SaaS, new application
in terms of an agent. We are talking about
applications that exist today and what it means to build them out. So think about agent ready SaaS, right? This would simply be, you know, we can take a existing application, we can wrap it in say MCP or A2A and make this available
through new channels for either existing or new customers. And again, like we were talking about with our own capabilities of
using third party software, and third parties can
also use our software. And this may unlock
different patterns for them to consume our software. Embedded agent SaaS, right? And this is actually
having automated workflows that come into our system. So this is probably kind of
closest to what we think about from most SaaS applications. Can I just take agents, stick
'em somewhere in the workflows that I have today. Human facing agents, we're all kind of familiar with this modality, right? A chat bot or something that
actually lets you interface with an application that before
you would've been clicking through a bunch of buttons. And agents facing agents. This is sort of the new frontier that we're all thinking
about and talking about. Will there come a point where
an agent will simply talk to an agent without any human in between? Can two different third party software that you're using can
Stripe talk to Datadog and figure out, well, like a particular
integration that you have without you even needing
to tell it what to do? This is kind of an interesting
one from a sort of a mindset of what we're gonna be talking about next. When we think about
existing transformations, transformations for existing
SaaS applications, I want you to think in terms of layers
work your way downwards. Most human interactions
and workflows happen at the solutions API layer, right? API UI layer. Humans are interacting with these, systems are being designed
to interact with these. There's business logic and
there's data underneath. But the easiest place to
inject agentic experiences into existing applications is usually at that front edge. Model your human interactions. Think about what those workflows are and figure out how agents can
enhance those experiences, either for your customers
or for your own operators. And you're probably gonna be pretty happy with the experience overall
because it's gonna enable you to inject agentic
experiences non-invasively, but still visibly to your
customers and operators, and remove some of the
undifferentiated heavy lifting that they're probably
already experiencing. Don't ignore the data in
the business logic layer. If you have opportunities
to inject the data agents into there, yeah, please do. But maybe focus on that front edge first as you're thinking about
transforming your applications. And I think you'll probably find a lot of opportunities to inject
agents into that experience. So which flavor of
agentic SaaS really fits for my domain and customers? Let's get a just a tad more technical. Yes, I've been sort of
skimming along the top of this. We haven't really even seen
a technical architecture. Let's start thinking about what it means for agents in these. Well, you can have an
agent as a product, right? We already sort of said, Hey, you could simply have
an agentic experience. We've already seen this.
ROS is a perfect example. ROS, like Revenue Operating Systems, agents, all the way down. They built on agents, they run agents, everything they do is agents. A really interesting
solution, very innovative, but that's a brand new solution, right? And we're thinking about transformation. This may or may not be a fit for how we're thinking about things unless we have entirely new
work streams we want to develop. On the other hand, this probably
resembles your architecture a little bit more today. You probably have a front end, you've got an API, you
got some microservices, some databases behind there, perhaps. Maybe we can inject agents
into some existing workflows. Maybe we can replace some microservices. Maybe we can think about how
we can add new functionality, which is really the easier
path to agentic solutions. Can we take the existing
functionality we have and enhance it with additional workflows that involve agents? Or can we simply, again, that,
you know, chat bot modality, can't we stick agents in the front of this and simply let them talk to the customer and have our application
move behind a step and have an API, MCP layer that talks to that new modality. But for today, we're gonna be
focusing on this middle one, as I said, probably resembles your architecture a little bit more, right? This is closer to an
existing SaaS application that we might recognize. So that'll be the focus of
today's talk a little bit, even though you'll see, I think some clues that will help you in the
other directions as well. Agent deployment models. So just getting a little bit more specific about what we mean here. When we talk about agents and we talk about SaaS, you've probably heard us use the word dedicated or siloed before. This simply means in a SaaS term, everybody gets their
own stack of software. In a dig agentic term, guess
what? It means the same thing. Everyone gets their own agent. Everyone gets their own knowledge bases. Everyone gets their
own tenant data stores. All of the agentic parts that make up the complete
architecture of an agent. Everybody gets their own stack. And compare this to shared
or pooled architectures where in fact one agent is
operating from multiple tenants. In this world, we have to
make different decisions and they have to think
about who's operating on that agent at any given time. And again, our knowledge
bases, our data stores, everything else could
be shared in this model. But with that comes a little
bit of responsibility. 'Cause when agents meet multi-tenancy and agentic SaaS, we now have to think about how we're deploying them. There are interesting aspects of agents that are gonna push us a
little bit toward the limit compared to where we were before. There were already SaaS solutions. You know, think about like Dremio or Datadog where a lot of the system ran in the customer's account. In agentic solutions, you'll
be challenged even more to bring your agents closer
to your customer's data. So those remote deployments
will be on the table for a lot of solutions. We have to sort of open
up our mind and think about how we would operate
those types of solutions. Those are still dedicated though, right? If we're thinking about
those in terms of isolation, if you deploy at your customer's account, they're the only one who can access it. Still a dedicated solution. We'll spend a lot of time thinking and talking about shared as always though. What does it mean to
have a shared solution? The biggest thing we're
adding to the slide over the last one is tenant context. And you are gonna hear us
dive into what it means to do identity and tenant
context in AgentCore and in agents in general. Injecting that tenant context,
making sure it proliferates through the whole agentic
system that we've created. All the way from the front
end back to the data sources. And back to the observability story is really how you make
agentic stories multi-tenant. So with that, yeah, with that, we wanna think a little bit
about what the agent story is. What is an agent even, right? So if we think about agents holistically, we wanna break it down into parts. These are traditional parts.
None of this is new to us. We have an agent that's your compute. If you've ever written any
application, there was compute, there's a compute behind
that is a prompt, right? For a model, that's what makes it an agent in a sort of pedantic model, right? Okay, now it's an agent, it's got a model. But really we have to think
about all these other parts. What are the goals or instructions that
we're passing into it? What are the tools that has capabilities for capabilities to do? What is the context? If you've worked with
any agentic solutions, you realize there's a context
that's going conversation to conversation that's going with it. How do we store those? How do we think about those
in terms of isolation? That'll be what we're talking about. And then the downstream thoughts.
What about observability? What about the actions we can take in the environments
that they take part on? And with that, we're gonna start to get into the agentic
transformation strategy, right? And with that, we're gonna
hand it off to Ranjith and he is gonna take you
through the next parts. - Thanks Bill. Alright, so Bill, set it up really nicely by introducing why companies and especially SaaS companies may have to undergo an agent transformation, right? So now what I will be doing
in this section is take you through some practical
approaches in terms of how do you navigate that
transformation, right? And I'll also show you some examples on how to build and
implement AI agents as part of your SaaS application, right? So what you're looking
at is a pretty simple and a straightforward representation of a CRM SaaS application, right? So CRM stands for customer
relationship management, right? And I assume this is a sales
management function within a CRM app, right? So there is lead management,
there is a creation of opportunity or a task, right? And what you see on the
top is a control plane, which is very standard,
typical for any SaaS, right? So you have services
like onboarding services that sets up identity
billing metering, right? So basically services that has sort of this crosscutting concern
across the entire app, right? And below that is the application plane, which is where your tenant workloads are actually running, right? Now in terms of the request flow, right? So you have a user coming in through your front-end application, right? CloudFront static assets are from an Amazon S3 bucket, right? The user gets authenticated and the authenticated request flows through API Gateway, right? So pretty standard and
something that you would've done or you would've seen, right? And then there's JWT or a JSON web token that's flowing around
the request chain, right? And that jot tokens reaches
application plane services, right? So pretty standard. Pretty
standard for a SaaS application. You know, we are using Lambda,
you could use containers for your application plane services, that's totally fine, right? But if you think about this, there's typically some
kind of a user experience or UI on top of this, you
know, experience, right? So there is some kind of a form where somebody's entering
the contact details or somebody's entering the
opportunity or task details. Right? Now, if I'm a SaaS
provider, I'm thinking, well, that's a user workflow that
is ripe for disruption, right? So that is something that
I could potentially move it over to an AI agent and
have an AI agent handle that manual sort of, you know, user entry and that pull workflow, right? So how do you go about doing that is exactly what we
are gonna talk about, or I'm gonna cover as part of, you know, during the rest of the session. So what we recommend is taking
a phased approach, right? So when I say a phased approach, right? So there are four phases here. The first phase would be
your domain analysis, right? So this is your domain
analysis and modeling, and you know, this is where
you identify your domain, your sub-domains, your bounded context, and folks that have already
done domain driven design, you'll be already familiar with this. So it's about identifying
what your domains are, what the objects within your domains are, what are the boundaries,
you know, for those objects. And then you orchestrate the flow between those bounded contexts, right? So that's essentially phase one. And if you already have an
application, this is an exercise that you've already done, right? So this is something that
would've already done and have, but if you have not done it, we highly recommend doing that right? Now, phase two is the agent
capability development. So once you have done the
whole process of identifying a domain, sub-domains,
bounded context, right? So you would take those learnings and start creating your
initial agent, right? And you start mapping the
agent responsibilities to those bounded context
that you have determined or yeah, that you figured out in the phase one of this process, right? Phase three is the infrastructure,
which is super important. And this is probably
where I'm gonna spend most of my time on, is, you know,
you need the right kind of infrastructure to, you
know, run your agents, right? Something that's managed,
something that provides you with the runtime identity and access control,
memory management, right? So all that is super important. So that's picking the right
infrastructure is definitely an important part of this process. And finally, you know, phase
four is scaling and monitoring. This is where you are monitoring
the agent performance, coming up with scaling strategies, right? And just like any application, right? So this is critical as well
when you're going through or undergoing an agentic
transformation, right? So these are the four phases
and the phases is evolving, like there could be other phases or more phases that might come up, right? But from what we observe,
from what we see, so this is how we would recommend
approaching your transformation to agentic. I'll quickly go through this again, like I said, phase one is domain analysis. So this is where you're
identifying the different domains within your application, right? So because our example
is a CRM SaaS app, right? So there's a sales management domain than objects within that domain, right? There's customer support,
there's marketing automations, and there could be more domains, right? So there could be a payment domain or account management, right? So the first step is really identifying
the different domains and then you would orchestrate the flow between those domains. Like how are those
domains connected, right? So this is classic, you
know, domain driven design if you have done it
right, if you have gone from a monolithic architecture
to a microservices or you know, sort of architecture, right? So this is something that
you've already done, right? So, and that's where we would
recommend to start the process and then start with a
single domain, right? So pick a domain, let's say you pick the sales management domain, right? And you start mapping the capabilities into the agent, right? So you would add the customer
capability or the lead, or the opportunity or the task. And what you would see is
we have something called the tools, I mean, which
are basically, APA calls or your business logic. So tools are a way, you know,
where your agent gets access to external data or gets access to certain capabilities, right? So this is perhaps, you
know, some, you know, a way you could start
the whole process, right? So you'll start with a single agent and start adding
capabilities into that agent. But at some point you'll see that, or notice that, you know, as you add, keep on adding tools, it can
potentially overwhelm the LLM and the context of the LLM, right? So when you send a prompt into
the LLM, it may not be able to figure out which tool
to invoke or call, right? So at some point you
may want to break it up into multiple agents, right? This again, goes back to the whole domain driven concept, right? Where you have separation
of concerns, right? So you may not want one
agent to expose, you know, whatever they're doing to
a different agent, right? Or a different tool, right? So you come up with, you
know, some kind of a boundary and create separate agents, right? Now, when you have separate
agents, you need some kind of an orchestrator or a supervisor agent that knows which agent
to call or which agent to invoke when there is a
request coming in, right? And the supervisor agent
is the one that would look at the incoming prompt and
it knows which agent to call. Right? Now this process can get a
little bit complex, right? So you have the user request
coming in, you have it goes to the supervisor agent, and then the supervisor agent
determines which agent to call. And if you look at the customer
agent, it has a local tool. If you look at the lead agent,
it's calling an MCP server, which has, you know, more tools, right? And then there are some common tools that the agent has to invoke. Now add in an external tool call, right? And also identity, this whole
process can get really heavy and really complex, right? And yeah, I mean, it gets complex because there is obviously
multi-agent collaboration, you have to orchestrate
between those agents. Like I said, you know, tools and tool execution becomes
a challenge, right? As your number of tools increases and the context increases as well, right? Now, there are some frameworks out there, which I'm sure a lot of
you would've heard of or even use like LangGraph,
LangChain, crewAI, strands agents from Amazon that we
built and we open source, right? So these are, you know,
perfect, you know, choices because they give, you know,
these frameworks, they give you that sort of prebuilt abstractions,
but you as a developer or architect or engineer, you don't have to do a lot of the heavy lifting. The frameworks handle that for you, right? It does that multi-age and
collaboration, it knows how to orchestrate and all that, right? But you know, oftentimes, like we have seen developers,
they still face challenges. They hit the sort of brick
wall when they're trying to move their proof of
concept to production, right? So they still find it challenging, they still find it hard, right? And now you add tenancy
into the mix, right? So you have your agent, you have multiple tenants
accessing the same agent, right? Some tenants might be okay to
share a particular construct like memory while others may not, right? Because they're in an enterprise tier or premium tier, you know,
customers or tenants, right? And then the same goes with knowledge base and tools like some might be okay to share and they say, okay, like
it depends on the plan or the tier that the
tenant is signing, right? If they're in the basic tier,
it's going probably going to be share things are gonna
be shared or pooled, right? But if you're a enterprise tier tenant, you know, you may wanna
provide them better isolation, better quality of service. So things are going to
be more dedicated, right? So when you add multi-tenancy or tenancy into the mix, things get
even more complex right? Now, throw in identity, right? So you, you have your enterprise,
you have your employees, you have, you know, batch
processes or some kind of a process talking to the
agent, how does the agent know? Is this the right source? Like, can they allow that
request to come through, right? Then you having your tenant users going to the agents, right? Agent calling other agents, which calls external services. Agent could call other
external agents, right? So there are a lot of
considerations when it comes to a security and identity
perspective, right? Things like access control, authorization, managing the lifecycle,
identity lifecycle, integrating with third party applications, right? And the whole governance
and compliance aspect can get really complex
and challenging, right? And that gets us into a phase three, which is picking the right infrastructure and picking the right place
to deploy your agents, right? You need something that does
all the undifferentiated heavy lifting of, you know, securely
running your AgentCore and remembering past interactions, right? The whole memory aspect of it, right? Identity and access control agent tool use where you execute complex
workflows, be able to discover other agents
that are out there, right? And also finally auditing
every single interactions that happening within that
whole sort of ecosystem, right? And this is where AgentCore, Amazon Bedrock AgentCore comes in. So, which is a managed service from AWS, which lets you
deploy and operate agents in production, you know,
in a highly secure, safe and a reliable manner. And as you see here, AgentCore has a lot of services and components, right? And I'm not going to go deep
into every single one of those, but we are gonna focus on a few of them. And the first one is going
to be the runtime, right? So AgentCore Runtime, think of it. So this is a compute, right? So this is where your
agents are actually deployed and this is where it's running, right? And you can, like I said, you can build
your agent using any framework, LangChain, graphs,
Strands, doesn't matter. You can use any model
that's available right? Through Bedrock. You can develop that and
bring that and deploy that into AgentCore Runtime and
it's just gonna work, right? And then, you know, towards
the top, right? Yep. Top right, you have the
AgentCore Gateway, right? So this is where you want your agents to discover other agents or other tools, external, internal, right? Perhaps you, there is a
business unit that have, that has exposed their own agents, right? Or tools, right? And you want your agent that's running within
the runtime to access that over MCP, right? Which is, I'm sure a lot of
is a model context protocol. AgentCore provides a really
nice abstraction, really nice way to invoke or access
those external tools or targets, right? And we'll get into, you know,
how that whole thing works in a little bit here. Then there is browser, which is for browser, AgentCore Interpreter, it gives you a sandbox for executing code. Not gonna go super deep into those, but AgentCore Identity is
central to this whole sort of authentication and security experience. So I'll definitely be covering that. Then you have observability
and AgentCore memory, right? So like I said, AgentCore
provides a really nice way to deploy and operate your
agents in a safe, secure, and relatable manner, right? Alright, so you're ready
to deploy your first agent into AgentCore Runtime. So what you're looking at
is, again, a really simple, straightforward implementation
of an agent, right? It's using the Strands SDK
and something to notice is the decorator called
app entry point, right? So app entry point is where like when you invoke an agent, that's where it's going to enter, right? So that's the function that'll get called the My Agent function. Again, this is a Python representation. You know, you could do the
same thing in other languages as well, but Abdo entry point is where the request would enter. And then if you want to take this agent, so you have this running locally, you want to take this and deploy
that into AgentCore. All you need to do is, you know, come up with a Docker file, package
up your dependencies. And when you say Launch AgentCore launch, it's going create an image and push that to an ECR Elastic Container
Registry repository, and then it'll pull down
into AgentCore Runtime and it'll deploy that AgentCore, agent into the AgentCore Runtime, right? So you have your first CRM agent, right? I mean, sort of the monolithic agent that we saw a few slides ago deployed into AgentCore Runtime. So now you may ask like, how
do I access this agent, right? It's pretty straightforward, right? So all you have to do is
AgentCore Runtime exposes an endpoint and you just do AHJDP request and you're able to access or invoke the agent using that endpoint. Now, let's go back to the request flow that we, you know, that
I started with, right? So a tenant comes in, right? The authenticated request flows in, right? There's some kind of a JSON web token or a jot that the IDP,
you know, provided, right? So that flowing through the proxy, and then from the proxy to the runtime, you pass in the Jot
token or the JWT token, and it should be the access token, right? So when you call agent deployed with an AgentCore Runtime,
you would use the access token from the proxy when you're
making that call, right? And what AgentCore Runtime does is before it forwards the
request to an agent deployed, it sends it to AgentCore
Identity, the other service and AgentCore Identity would go back and validate that request
with the Identity provider. In this case it's Cognito
and it ensures it's a valid, it's coming from a valid
source, it's a valid user, valid identity before it sends a request to the agent that's deployed, right? And I'll get into, you know, somewhat, I'll go into the weeds
(chuckles) on this flow in a little bit, or I
think it's right here. So this is basically a refresher on OAuth, which even today, I mean, I find it somewhat
difficult to understand. So it's a quick sort of refresher. So let's say you have a tenant user, the user's browser connects
to the front end, right? And the front end, right? So you have the user sign in and they make an authorization
request to an IDP, right? In this case Cognito, then Cognito returns an authorization grant code
back to the front end, right? The front end comes back
with an authorization code, comes back with the
Client_id client secret. And then Cognito is like,
okay, I recognize this user, I authenticate, so here are
the ID tokens, access tokens, and the refresh tokens, right? And those tokens, it flows
around through the request chain and it reaches the proxy lambda. And the proxy Lambda uses one
of those tokens, which is, like I said, the access token to access the AgentCore Runtime. Okay? So now AgentCore Runtime, before it sends the request
to the agent, it sends it to AgentCore Identity,
validates the agent, and then it returns what's called a workload access token, right? So this is a new
construct within AgentCore that we have introduced. And this is opaque to you, like you don't have to
do anything here, right? So this is an additional layer of security that AgentCore has introduced
with workload access token. Right? Now, what is a
workload access token? So when you deploy an agent
with an AgentCore Runtime, every agent gets its own identity. So we call it the agent identity or the, or an agent workload identity, right? Then you have the incoming access token. So a combination of the
incoming access token and the agent identity is
a workload access token. And this is not something you are doing the service does it automatically, right? So you don't have to worry
about, you know, creating an workload access token, right? Sort of a slightly
different representation of the same thing, right? So you have the agent
identity, incoming access token request goes to AgentCore Identity, right? It gets validated and then
AgentCore Identity creates this workload access token. And what happens with this token is that any outbound communication
or you know, request that the agent, the CRM agent makes, it uses a workload access token
from this point on, right? So if it's calling an MCP server,
if it's calling a gateway, or if it's calling a tool, it
uses a workload access token to, you know, as part
of that request chain. Now, what happens when there
are multiple users, right? Because we are talking
about a multi-tenant, multi-user system, right? If it can quickly go
through the flow, right? So you have a tenant,
one user, they come in with their access token, they get their own workload
access token, right? The same thing for tenant two user. They come in with their
own access token, again, they get their own workload
access token, right? So, you know, security is sort of inbuilt, the isolation is sort of inbuilt
as part of the AgentCore. And AgentCore Runtime provides
that by default, right? And once you have the
access token, obviously like I said, you can, the
agent is able to make any kind of outbound authentication
calls that it has to make. Let's look at some code hope that's okay. Well, there's no going back
(chuckles) now, right? Right. So what you're looking at is the proxy calling the
AgentCore Runtime, right? So you have the access token, right? Like I said a few times, right? Step one is the URL to call
AgentCore Runtime, right? So if you notice there's
an ARN or an escaped ARN. So we have to escape RNA, the
RNA is the AWS resource name, it has all the slashes and
all that right of the colons. So you're escaping that,
and you would add that as part of the URL in your calling. So this represents basically which agent you're calling
within the runtime, right? If you have a supervisor
agent, the ARN is probably for the most likely for
the supervisor agent that's deployed, right, so that's a URL. Then you would create the payload, which has a prompt, right? And then you add the payload as part of AHJDP request, right? So there's a history P
call that you're making to the AgentCore Runtime. You're passing the token, like
I've said a few times, right? So it's passed as part of
the authorization header, and finally they're adding the tenant ID as part of the header. So this would make sure that
Tenant_id flows through, you know, across to the agent running within the AgentCore Runtime
so that the agent is able to take actions on the tenant, you know, set up isolation policies and
all that good stuff, right? So it's important to make
sure, you know, some kind of a tenant identifier
is passed from the proxy into the AgentCore or the agent running within AgentCore, right? So this is a calling side. Now this is the agent
implementation, right? So the receiving side, right? So like I said, Abdo entry point by now, it should be familiar to you, right? So that's the entry point
into the agent when the call comes in, right? We are retrieving the tenant ID that was passed in the
previous step, right? Now, convert lead, convert lead is, and I'll get into what
this particular tool is. So it's a tool, it has business logic. And if you remember where I
started off the presentation, I said, you know, there are user workflows that you want to automate, right? So there are people entering
opportunities manually, there are people filling up forms, right? The goal or the idea here is to have an AI agent automate
that for you, right? You wanna have that business logic because it's a, it's a, you know, create read credit operation,
right, update lead operation. You want that as part of an agent, right? So that's what Convert Lead does. And I'll show you, show you the code for the Convert lead in my next slide. But the idea is you have a
tool called Convert Lead, you're providing that
tool to the agent, right? So it has, so now this agent has access to that particular tool, right? And you can add more tools, right? I mean, I mean obviously you
can see that it's an RNA. If you have multiple tools, you can just do a comma separated list and provide that, right? Bedrock model. It's a class
within the Strands SDK, right? Which you provide the Model_id and some of the other parameters, right? Agent comes from the Strands SDK. Again, you provided the model
and also the system prompt. And then finally, you know,
so that's a prompt, right? And as part of the prompt, you
have to specify the tenant ID to make sure it goes to the right tenant and all that, right? It operates on the right tenant. So this is a snippet of
the agent implementation or AgentCore, right? Now the tool code, right? So I talked about the convert lead, right? So you start with the actor
tool decorator, again, it comes from the Strands SDK, right? And you make sure there's
a tenant ID, right? If you don't have, have a tenant ID or see a tenant ID, you, you know, you kick back the request, right? But if you do have a tenant id, then you do the credit
operations for step three is basically where you're
getting the opportunities stable or the task stable, right? And step four is where
you're, you know, updating, or in this case it's creating
a new upgrade, right? So, you know, you can
see that we have sort of taken the user workflows, right? Where someone was entering the form and we have moved that
into an agent, right? To a tool and we have provided this tool to the agent, right? So we have transformed
that experience, right? Again, sort of a simplistic
or a simple example, but you get the idea, right? Okay, so up until now we have been focused on the agent deployed within
the AgentCore Runtime. It had access to some tools, right? So we talked about the convert lead tool, it could have access
to other tools, right? Like you see here, that's totally fine, but there are cases where, you know, when you want your agent
to access other tools or other targets that ex
it could be external that, you know, third parties have exposed or perhaps a different
business unit within your company as exposed, right? So you want your agent
to have access to that and that is enabled or achieved using the
AgentCore Gateway, right? If I mean, like I said,
AgentCore Gateway provides a way to discover new tools and
integrate with new targets. Now, what are some of the targets that AgentCore Gateway supports, right? You can have an API Gateway Target, right? So any APIs that you
expose, you know, as part of a API Gateway, the agent
now has access to that. OpenAPI Target, right? So you can have a Lambda Target, right? So if you have a Lambda
function, you know, AgentCore Gateway, can
MCPFI that Lambda function and provide that to the agent, right? So the idea is your CRM agent
deployed within runtime has more intelligence, right? By having access to these
additional tools, right? So you can have an MCP
server Target as well, right? So the gateway provides a
really nice way, you know, it provides an abstraction where
it's able to provide access to multiple tools and provide that to the agent running within the run time. Now there's an arrow
coming from, you know, or going from AgentCore
Gateway to identity, right? So again, security and identity is sort
of first class citizen or construct in this whole experience. So any request coming
into AgentCore Gateway has to be authenticated, you
know, so the agent has to send an access token
into the gateway, right? And that token gets authenticated or validated using Cognito. And then that's how Gateway
would process that request. If it doesn't find an access token, it wouldn't process the request, right? So this is the gateway
implementation, right? So the code, now you have the CRM agent with running within your runtime, right? It is trying to access the gateway, right? The first thing that it needs
is the Gateway_id, right? So you would have the gateway deployed, you get the Gateway_id, right? In this case it's stored in a SSM in a parameter store, right? Systems manager parameter
store, you get the Gateway_id, add that as part of the URL. Like I said, you need the access token to access the gateway as well. Like, just like you need an
access token to access runtime, you need an access token
to access gateway as well. So you get the access
token, you can see that there is an a requires_access_token. So that comes from the Strands SDK. So you don't have to do a lot
of wiring or heavy lifting. You get the access token
using that decorator. If you just add that as part
of your Python implementation. And something to take a
note is the auth flow, it's M2M, right? So M2M stands for machine to machine because you have an agent
calling another agent, right? So it's different from
the earlier auth flow because that, that was from
web to an agent, right? So this is that is an
authorization code grand flow. So this is a machine
to machine flow, right? And then once we have that, see that we are using MCPClient,
MCPClient, it's part of the Strands SDK, right? And then you use streamable HCDP client and passing the token. And then number seven is important, right? Because this is slightly different from the earlier implementation, right? You still have the convert lead tool, but you're giving your agent
access to other tools, right? That's coming from the gateway now, right? So you're listing the tools,
there is also a semantic search or a semantic, you know, so
you could use that as well, but you're listing the tools
that sitting behind the gateway and you're providing that to
the agent in this case, right? So the agent has more intelligence,
has access to more tools to take a decision, right? Alright, alright, so this
is a really nice feature that this literally came, or
I wanna say last week, right? So the request coming into
the gateway, you're now able to examine it, inspect it,
or intercept it, right? And you're able to add
things to the header, right? So this is, especially
if you wanna, you know, and you can attach a
Lambda function to it. If you worked with API
Gateway, this is very similar to the Lambda authorizer that
you attach to an API Gateway. So same concept, right? And so, you know, this will
be helpful if you wanna inject some tenant specific
values or variables before the request goes
to the downstream targets or downstream systems, right? And the same thing, when
the response comes back from the downstream systems, you
can have a lambda interceptor process the response and
send it back, you know, process the response
before it gets sent back to the caller, right? You can inject more, you
know, values, tenant specific and whatnot as part of the
response as well, right? Oh, I'm sorry, I can go back. Okay, so this is basically a summary of the end-to-end
authentication flow, right? So you have the user, you have users that wants to access agent, right? So we talked about this at length, right? They get authenticated, AgentCore Runtime, there's an inbound auth right? Now, AgentCore Runtime Gateway, right? There is an outbound
auth which uses OAuth, but you can also use IAM
outbound authentication if your agent wants to
access AWS resources, right? Like a, you know, your agent
wants to access DynamoDB or any AWS resource it, you can use IAM outbound auth as well. And the call to the gateway,
you know, like I said before, you can use OAuth and then even Gateway, if you
see there is an inbound auth, there is also an outbound auth going for the calls, going from
the gateway to other external or third party services, right? So Gateway has both inbound and as well as outbound oath as well. Okay? So up until now we have
looked at, you know, something where you had a single
runtime, single gateway, right? And a few tools, but there could be
situations where you have, because typically in SaaS
you have customers that are of different shapes and sizes, like they
have requirements, right? So you could have someone
in the basic tier, you could have someone in
the premium tier, right? So you could absolutely create
a dedicated runtime gateway for your premium tier customers. It would look something like this, right? But it's still important
to maintain, you know, have some kind of an identity, right? So you would have AgentCore Identity and what you can do as part
of your identity provider is create separate application IDs, right? So client applications, right? So for example, you could create
a basic client application for your basic tier customers and for a premium tier customers, you can create their own
application IDs, right? And that's how AgentCore Identity would recognize the request coming in. If it's coming from a premium,
you know, to your customer, it would go authenticated
against a premium application id, right? You get the idea, right? So if,
if there are more enterprise to your customers, you can,
you know, achieve isolation by creating their own
application IDs, right? Finally, there is a
session isolation built in because every agent session
that gets created, it, it gets created in its own MicroVM. And we use the firecracker technology that AWS invented, right? So every session runs in a
completely isolated MicroVM. It has its own memory,
it has its own compute, it has its own file system, right? Because if without that session isolation, there is a possibility that local files and state could be accessed can bleed over and potentially be exposed. So every agent session, it's
created within its own MicroVM. And this is the final
thing before I hand it over to Bill, AgentCore memory, right? So super important
within an agentic system, because you want the agent to retrieve past interactions
that you had with it, right? So an AgentCore memory, it's a service within agent Bedrock AgentCore,
it has a short term memory and a long-term memory, right? So short term memory is where
the interactions are stored within a single session, right? Yeah. So that's what
short term memory is like. It stores all the past interactions
within a single session. And the long-term memory is, it spans across sessions, right? So it stores interactions
across multiple sessions. Now, in terms of isolation
with AgentCore memory, AgentCore memory provides
some really nice features. So you can have like session tags. So there is something called for short term memory, there's
something called actorid. So you can dedicate certain tenant and users their own actorids, right? And long term memory, you can create their own namespace, right? And the way you would access
that from your front end or from your agent is you
extract the tenant_id, you know, like we saw from the incoming,
token, you would map that to an IAM session tag, right? So this is something, you know, you may have already done, right? So you, you create an IAM policy for with placeholders, right? And then you use the tenant
IDs, update that, right? And then you assume that role and then you can use the
STS the token service to get temporary credentials
that's specific for that tenant, right, that
made the request, right? So now, now you have tenant
scoped credentials using which you can access the
specific, you know, part of region within the
memory, short-term memory or the long-term memory, right? So really nice way to
achieve, you know, isolation when you're using AgentCore memory, right? Alright, so I think I've covered a lot of things here to talk about phase four, which is the final phase. I'll hand it over to Bill. Yep. - Thank you Ranjith. So we've
covered a lot of ground. We've covered three phases already. The last one, and hopefully
the one you didn't forget is observability. 'Cause when we talk to SaaS
customers, when we're talking to customers with the
existing SaaS products, often people don't spend quite
enough time thinking about the observability story
and how to build that in. If you're building agentic
solutions, I want you to be thinking about this right at the front edge of your application. I want this to be a part of your original planning phases in part because it's fairly complex. Now this part of the story
hasn't changed all that much. And when we've talked about
SaaS solutions in the past. We've always said, Hey, you're gonna have
different tiers of customers. There's gonna be some complexity. Out of everything that they call, we wanna be emitting some
specific SaaS context, right? So it has always kind of looked like this. We've simply added agents into this story. Instead of saying, Hey,
you're calling a function, you're calling a microservice,
whatever you're calling, we wanna omit very specific metrics that talk about what
the consumer is doing. Are they using a specific
agent? Where are they using it? What feature are they
using? What's the tenant id? What's the tier that they belong to? Any of those that could
be relevant downstream to your business users to help
them to break down this usage by, you know, different pricing
tiers, different regions. However they need to think about how to successfully operate
their SaaS business. Those are the metrics
that we need to omit. 'Cause downstream there's
gonna be a whole nother story for how they visualize these things. If we don't provide them the
data, they're not gonna be able to dig into that data and get to the observability story they need. We've talked about all
sorts of different parts of AgentCore and of course
observability has its own functionality within AgentCore. It provides a lot of things out the box. It has really nice agentic
dashboards that come out of the box in CloudWatch. Those are worth looking into right away. Now the caveat I'll give you to both that and the third party dashboards
that we'll be taking a look at are very few observability platforms. Consider Tenant_id to be
a first class concept. What do I mean by that? When you look into of your
observability dashboards, it will talk about what
agent are you using? You know, what platform are you using? What region did you deploy in? It will not talk about
your tenant identifier. This is a business concept
that's specific to you. 'Cause you're a SaaS provider. To them it's just another
piece of metadata. Now that's problematic because
downstream we want tenant ID to be a first class concept. We want our dashboards to
drive off of tenant id. So regardless, take a look
at the agent dashboards. They're great, really nice
functionality outta the box. You're not gonna find an
easy way to simply say, Hey look, I can see tenant id.
You'll see it in your logs. They'll be there if you admit it, but it's not gonna occur to be automatic into those dashboards. Just keep that in mind, especially as we're going through this next example. So I took a look at some of the examples that come out of the box. If you haven't looked, there's a GitHub out there
called AgentCore Samples. It's great. It gives you examples of all of the stuff we've been
talking about today, including third party observability. And they actually built
out a nice little example with the Jupyter Notebook for Langfuse, which is an AWS partner that
has a completed agent platform including observability for agents. I dug into that a little
bit, sorry for the wall of text of code, but
there really isn't much to show here except for code. Honestly, if you're doing observability, you're sending data from your agent off to their third party solution. It's really just how you configure it. So I wanted to call it a
couple specific things on here. We're disabling the built-in
open telemetry solution for AgentCore. This is because we're gonna directly send these metrics off to Langfuse. You can see just setting up a private key and some endpoints. This is all pretty basic stuff in terms of setup, it
looks a little complex 'cause there's a few lines. If you think about it,
there's a URL, there's a key and we're sending data to it. That's really all there is to this setup. When we get onto this, the
example uses Strands telemetry, which has built a built-in
OTLP exporter that you can use and you simply have to make sure that however, we're sending that data off to our third party, Langfuse in this case, you're emitting tenant metrics. I did it in two different ways
here and I'll tell you why. I admitted Tenant_id as a trace attribute, which turns into metadata
on Langfuse's side. And I also did it as a tag. Now this was important because when I first set this
up, I created my metadata as Tenant_id and I sent it off to Langfuse and I started looking at the dashboards and I couldn't find it. And this again is the problem where Tenant_id is not
a first class concept for almost any third party solution. You have to figure out where
that Tenant_id is gonna surface in the dashboards. When I put the Tenant_id
into the tags for Langfuse, it immediately surfaced
up into the dashboards and as able to create interesting. So there's my tenant id, I was able to create interesting
models, you know, just again, this is just a query, logging it. Here's the metadata as
it shows up in Langfuse. So because now I have Langfuse here, umbrella-corp-004, which you could see down there in the bottom. That's my tenant. It's metadata and it's also a
tag which allowed me to create some interesting dashboards like this one. All I'm really doing here
is I'm sorting the count of Tenant_id calls for
this specific agent. I can create much more
sophisticated models based on the Agent_id based on region
and everything else. But that Tenant_id has to be
a first class concept in here for the dashboarding to properly work. Now Agent Fuse is, is aware of this. There's actually even
a ticket out there open on GitHub to make the tenant ID and the metadata available
to the dashboards. But what you'll find consistently
across all observably platforms is you have to be the
one thinking about tenant ID and how that surfaces
through your BI tools. Whether your customers are
are using third party tools, whether they're using AWS tools, you or as you're developing
your application, have to think about how that's
gonna out to the end users. There's also an interesting case for this. Our example here is a CRM. So this year I was lucky enough to work with Salesforce working on
their agent force platform alongside our AgentCore and talking about the
interoperability between the two. With Agentic platforms, we're
increasingly gonna be pushed to talk about the interoperability of multiple agentic platforms. We'd love for you to build
everything on AgentCore. That's awesome. Chances
are you have other products that also have agentic stories. How are you going to
reconcile this as a developer? As an operator? Well, using third party
solutions like Langfuse and having all of your
different agentic systems, sending your telemetry off
to a single source is one of the ways as a SaaS
provider you can sort of streamline this operation. And really when we was working with Salesforce, it was great. It was easy 'cause there was two of us talking to each other. It was, Hey, what do you see in your logs? Oh okay, what do I see in my logs? Right? Let's just compare. In a real world operating solution, that's not how things work. Being having a single point
for you to create dashboards for you to visualize all of that data is actually pretty helpful. So going back to our original
use case we're talking about here, for a CRM solution or
anything else you're building where there's multiple parts and multiple tools, it'd be
awesome if you could figure out a way to use a single tool
like an operate like Langfuse and send all your data over there. I'm gonna hint, (laughs) and that's actually a fifth phase of this. You just quickly talk about what it means to do pricing in SaaS. We're almost at time, I'm gonna shortchange
this just a little bit. This could be an hour
talk in and of itself. Growth unhinged, which
is a website I really like has been spending a little bit of time thinking about how
to price agentic features. And they've sort of broken it down by this metrics activity-based model versus outcome-based model. Outcome-based model is starting to evolve in the agentic world
when we price not just on how many widgets did you consume but how many widgets successfully did something you wanted them to do. And it's an interesting mental model. And then there's sort of this
fixed versus variable model that we always think about in SaaS. Do people want to have a fixed price? They want have a variable price? And when they broke this down, you started to see pattern emerge. When you wanted do outcome-based and you wanted to be fixed,
you can do per workflow. So when a workflow completes,
we're gonna charge on that. If you wanna have a variable
outcome based process, you could do a per agent outcome, right? So you can actually
measure more granularly and this gets a little bit more like consumption based pricing. Activity based, you can do fixed per agent like a monthly fee. Hey, you get an entitlement
to this many agent executions versus variable for activity based, which it very much starts to resemble consumption based pricing as we're familiar with it. So this is actually a great
website growth unhinged. If you haven't looked into it before, I think it's worth taking a look at. Now where do we start in terms of this? You wanna focus on that
agentic business strategy. We haven't spent too
much time talking about the overarching strategy, but think about this transformation. How did you get here
and where are you going? Identify how and where your agents are gonna enrich your offering. Be strategic. Think of that
top down model we talked about. Develop new agentic pricing strategies. Again, have you considered
whether your customers are willing to do outcome based pricing or consumption based pricing? These are important
questions to ask upfront. How do we scale? How do we
remain agile and efficient? How do we model our agents
for tenant onboarding? 'Cause this is probably one
of the key areas that we see that's gonna evolve very quickly. And how do we introduce
new metrics, evaluations, operating models that are gonna
make our existing operations the things that humans are
beating their heads into today, more efficient and work better. So I'll quickly throw
this, the takeaways up here so I'm not running into
anyone else's time. SaaS is a business. It's one
size, not one size fits all. Be diligent about who planned this. You can take a picture and
you could read the rest of this on your own time
'cause we are out of time. Thank you all very much for coming. I hope you enjoyed the talk. I will once again make a reminder. Ranjith has a workshop that
covers a lot of this topic. If you didn't take a picture
before, come up and bug him and ask when it's gonna be. Thank you all. (audience clapping)
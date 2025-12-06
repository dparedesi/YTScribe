---
video_id: GtBFC27Buc8
video_url: https://www.youtube.com/watch?v=GtBFC27Buc8
is_generated: False
is_translatable: True
---

- Good morning everyone. I hope everyone's having a
great start to re:Invent. And you know, first of all, welcome. Thank you for choosing to be here with us for the next one hour. We understand there are a lot of interesting sessions
happening out there. So before we delve into today's topic, I just wanna quickly set agenda as to what this session is and is not about. This session is not about
any specific product or service or any specific technology, or architecture pattern for that matter. You're gonna be attending a lot of those deep dives through the week. Instead, as you begin your
week here at re:Invent, navigating through all the announcements of all the products and services, and, you know, exploring all
these solutions and innovations that our partners are
showcasing at the expo, and of course, not to
mention all things gen AI and agentic AI, we realize
it can be very overwhelming. So keeping that in mind, we designed this session to help us as a cloud community of
technology practitioners and decision makers to
collectively take a step back and gain a meta perspective
about technology choices and technology systems architecture. And secondly, we want to leave you all with a simple mental model and a practical framework using which you can deal with
technology, especially in this age of constant technology
disruption that we live in. So with that, my name is Mukund Rao. I'm a worldwide partner
solutions architect at the Technology Consulting
Center of Excellence here at AWS, and over the last five years, I've had the opportunity
to work with hundreds of customers across different
size and scale and industries and also with some of our
strategic AWS partners to help our customers undergo what we call business transformation through technology modernization. And including my time here at AWS, I've spent about 16 years
on the AWS ecosystem and most of it I spent as a
hands-on engineering architect and as an AWS customer building
and scaling things on AWS. So it's exciting for me to be here and sharing my perspectives. And I have with me Sushanth. So the way we are going to
structure today's session is we are going to start with why. I am going to be setting the context on why do we need capability framework and then Sushanth is going to dive into what is the capability framework. And then we are going
to apply this framework and trace through a couple of practical examples and use cases. And then we are going to discuss some FAQs and then we are gonna wrap it. So that's the structure today. Alright, let's begin. And let's actually begin
by rewinding our clocks by about two decades to 2005. And back then, as
technologists and builders, our lives was much simpler because we had fewer choices to make. You know, back then we had a handful of programming languages. A server simply meant
an application server or a bare metal machine. And you know, relational database was all and satisfied most of the use cases. And even with architectural
patterns, you know, we lived in the era of simple
three-tier architecture with your presentation layer, your application layer
for your business logic, and your data layer and that's it. And if you had to scale these systems, it simply meant that you
threw more resources at them, whether that is CPU or memory, and you vertically scaled these systems. Of course, that was not the
most efficient way to scale. It had its own set of challenges. But the point is we lived with a lot of technology constraints and these constraints
actually forced clarity. So we were more deliberate and intentional about our technology decisions and our systems were easier
to reason with, isn't it? And fast forward to today, we live in a world with
dizzying array of choices, with most things in life, right? I mean, take something as simple as water. And if you walk into
any nearby supermarket in a hydration aisle,
you can find yourself surrounded with so many options. You know, water, sparkling
water, soda, energy drinks, sugar-free, sugarless,
what have you, right? The same applies to technology as well. We actually live in an era
of technology abundance. And if you take something as AWS, we have about 240 plus fully
qualified services today. And this list is likely going to grow with all the announcements
that's gonna happen through this week, right? And if you take something
as simple as compute, other than 900 permutation
and combination ways of launching EC2 instances
of various types and sizes, you also have the container
orchestration platforms, you have serverless
options, and so on, right? And even data, you know, what was once a relational database, we now have a plethora of options and we live in the era
of polyglot persistence, or, you know, purpose-built
data engines, right? So we have document storage,
we have time series database, and increasingly now, you know, we are starting to notice increasing use of vector databases and
knowledge databases, supporting new class
of applications, right? So it's not just the services. And when you look at our marketplace, we have about 25,000 products and services that has been published by more than 6,000
independent software vendors. So that's a massive amount of choice of services and solutions, right? And it's not just the
services and solutions. The architectural landscape
itself is expanding, right? What was once the simplicity
of a three-tier architecture, now we live in thereof
cloud-native architectures with highly distributed microservices, application mesh,
event-driven architectures, real-time streaming
architectures, and now, you know, developing agent
application patterns, right? Even on the data side, for that matter, what was once a
traditional data warehouse, we now have modern data architectures. We have data lakes and lake houses and medallion lake houses
and zero ETL architectures. And it's not just with
application and data, right? You can even take
security and other domains and there are so many patterns like Zero Trust security, et cetera. So there are so many architectural patterns available out there. While having this choice, whether it is of services or solutions or architectural patterns is great, right? It has of course unlocked
a lot of potential for a lot of businesses out there. But it has also multiplied
complexity, right? And it has created a
new kind of challenge, what we call the choice paralysis. So what is happening as a result of this challenge is businesses, instead of building and
delivering value using technology, they're just stuck in
this maze of technology. They're lost in internet searches. They're, you know, stuck in documentation and they're taking architectural guidance from opinion-based internet forums. And as a result, you know, they're evaluating multiple vendors, resulting in long evaluation cycles, POCs that never see the light of the day. Overall, there is a delay
in value realization from technology that
we are noticing, right? And on top of it, add to what we call as the shiny-new-toy syndrome
of businesses wanting to adopt every new technology
pattern out there, right? It has created, you know, it has created a couple of consequences. One is there is, you know, they end up creating solutions for which they have to
force with problems, right? And secondly, they end
up creating sprawling and inefficient architectures
that contribute to, you know, consume more resources
and contribute to waste. So it's also a sustainability issue. So this is the state of technology and technology architectures
today, you know? Abundance has caused a
lot of problems, right? It's also worthwhile to take a look at the relationship between
technology and business because at the end of the day, you know, the objective of ME technology is to support a business outcome, right? And as you can see on the screen, over the past few decades, the relationship between
these two entities has dramatically changed, right? And in today's day and age, having a technology-led differentiator, is no longer sufficient. You know, this was kind of very normal probably like a decade ago, but having a technology-led
differentiation today is not sufficient. And what we are noticing is increasingly, technology is becoming
the front and center and at the core of every
digital-first business out there. And it's a trend that
we continue to notice and it has accelerated
since the pandemic, right? And as a result, you know,
businesses are having to... And you know, add to this the macroeconomic conditions, right? The kind of very dynamic
world that we live in today with the increasing AI workforce, companies are having to do more with less. They're having to innovate faster, and they're having to
compete harder, right? So given the scenario, it's
becoming extremely important to be able to translate
the business intent into technology choices
and much more faster at it than ever before, right? But let's be honest, you know, when we talk about
business and technology, them aligning with one another and moving in lockstep and all of that, for us AWS architects, it
sounds very cliche, you know? It sounds like one of these oldest lines in digital transformation playbook that gets repeated over
and over again, right? But the reality is this, right? From our vantage point as AWS architects, we notice that the businesses
out there are surrounded and paralyzed by technology choices, and constantly weighed down by increasing complexities
of their architectures that are becoming distributed and dynamic. And add to this the new
building blocks being redefined by gen AI, it is
contributing to more choice and it's amplifying the
problem further, right? So given this context, there is a need to refocus our attention
on a very fundamental, yet a very critical concept, called evolutionary architectures or evolvable architectures. Now, this concept of evolutionary
architectures is not new. It's been there in systems
design since the seventies, but it is especially more important and relevant and urgent today because of the barrage of AI products and services and tools, which continues to confuse a lot of businesses out there. And then when we talk about
evolutionary architectures, it also means that we need to rethink at how we look at our architectures. It's no longer sufficient
to look at your architecture and say, "Okay, it's
integration and a bunch of like tools and services
working together." Rather, we have to start looking
at them as living systems, and we need to actually have a plan to continuously, cost-effectively and efficiently evolve them. So that is the biggest mindset shift we need to do for us to rethink how we look at architectures. And to do that, what
we're going to do today for the next few minutes
is we're gonna take lessons from a couple of sources, right? So one is of course the lessons from our own customer journeys. We notice all sorts of
customer journeys on AWS from migration and how
they go on to modernize, how they go on to become
fully cloud native, and all the tactics that
works and that doesn't work. So we get visibility into that. And secondly, we are going to be drawing some lessons
from evolutionary biology because nature has been
here conducting experiments in evolution for millions of years, much before any of us humans existed or any of agentic AI
technology existed, right? So with that, I want to
highlight this timeless quote from Charles Darwin, and he says, "It is not the strongest
or the most intelligent of the species that survive, but it's the most responsive
to change," right? So this is a very profound
and a very timeless quote. And this applies to technology and technology architectures as well. So that brings me to the first lesson, or the first takeaway from today is around architectural adaptability. When we talk about
architectural adaptability, when we look at nature, you can see that evolution
doesn't happen overnight. It takes millions of years to evolve. And the same applies to
technology as well, right? Architectural evolution is
not an overnight journey. It happens in phases. Not implying that it should
take millions of years, that would defeat the whole purpose. But I'm implying that there needs to be an adaptable set of changes, right? And when we talk about
architectural adaptability, there is one thing that is very revealing and one factor that actually tells how well customers are doing
adaptability, good or not. And that is the success rate of their modernization initiatives. And what we have noticed
is for the customers that are more successful on AWS, they actually treat modernization and evolution as a continuous process. They have a plan for it and they end up doing incremental changes. That's the key word here, right? Incremental changes. And the contrary is true as well. You know, what we notice is majority of the organizations actually
fail at modernization efforts because they either try to boil the ocean or they try to do everything at once, and they try to rewrite the
systems without an actual plan to organically evolve your architecture. So that is one of the biggest
things I want you to remember. Adaptability is the key. The second lesson is around what I call the cost of evolution. And that cost is usually
paid in terms of tech debt. Now we know what is technical debt. And it can come from many layers, right? It can come from application layer, it can come from data layer, it can come from poor documentation, it can come from fragile
integrations of different services. But whatever it is, technical debt, like financial debt is
not all that bad, right? As long as you have a plan
to intelligently incur it and pay it off, right? And you don't want to acquire a big debt and that'll sink you, just
like financial debt, right? And it's also important to be able to measure the technical debt. Because if you don't
measure technical debt, you end up acquiring unknown costs, right? And, you know, this visual here explains this vicious cycle really well, right? So if you don't have a plan to evolve and you're not thinking
about proactive adaptability and making incremental changes, you end up acquiring technical debt today or tomorrow, whenever it is, if you're treating your architectures as static systems, right? That will result in more complexity and that will feed into the cycle and just go on and on and on. And we have noticed there
are many organizations, they don't treat technical
debt as importantly as seriously as they should. And over a period of time, because of how unmaintainable
their system becomes, you know, it starts showing
on business outcome as well. So it's very important to
address that technical debt. Now, the third lesson and
the final lesson is around what I call is the locus
of evolution, right? So, so far we have established why do we need evolvable architectures and how do we go about
evolving our architectures by making small, adaptable
and incremental changes and addressing the cost that naturally, the question comes, how do
we evolve the architecture and what do we evolve our
architectures around, right? So when that question comes, the natural inclination is
going with technology, right? And that is unfortunately
the reality that we see with many organizations out there, right? But as we just discussed, if you anchor your architectural
evolution with technology, you're gonna be chasing a moving target because whatever is latest and greatest today will be obsolete in a few years from now, right? So instead, the right
way to do evolution is to anchor what we call capabilities as the center of your
architectural evolution. And that's going to help you evolve your architectures much better. And to learn about what capabilities are and what this capability framework is, I now invite up on Sushanth. - Thank you, Mukund. Hi everyone, my name is Sushanth Mangalore and I'm a solutions architect here at AWS. I work with independent
software vendor customers who build software and SaaS products for large-scale consumption on AWS. Prior to taking on this role, I used to work as a software architect or an application architect. And I see many parallels
between cloud architecture and software architecture. Your software and the
infrastructure that it runs on come together to deliver a unified experience to your consumers. Your consumers don't see
them as two separate things, they consume them as one. So borrowing some lessons from software architecture
can be really useful in defining your cloud architecture. And you'll see this as a theme as we progress through this session today. So with that, we want to
provide you a mental model of three Cs, starting with the first C, which is capabilities. So think of a typical enterprise. An enterprise can have
one or more workloads. Now we define a workload as
a collection of resources and code that come together
to deliver business value. But from that definition, a workload could be something as simple as a single-page application, or it could be this large, sprawling, complex system with many moving parts. Imagine something like a CRM solution, an e-commerce system, a banking solution. For some organizations, one workload could be their
entire business, right? So when you are architecting such large and complex systems,
it helps to break down or organize your workloads by smaller, more manageable portions
and targeted solutions for each of those portions. So with that, I want to introduce to you the idea of capabilities. So workload capabilities
represent business intent for the portions of the workload that you're determined
to be your capabilities. And these are what I call logical subunits that you can independently solution for. The capabilities represent
the business intent or things that your
business need to deliver for a sustained period of time. And you can choose to
implement these capabilities with one set of technologies today, but you retain the ability to
switch out these technologies as newer, faster, cheaper, more efficient options become
available in the future. And it inevitably will, right? So that way, you are taking an approach where you can independently
evolve capabilities and that way, from individual
evolution of capabilities, your workload stands
to benefit as a whole. Now, you may have heard
the word capability in many different contexts. But for the rest of this session, we will use the word capability to mean logical portions of your workload with well-defined business intent. Now, at a workload level, we have the Well-Architected Framework, and this baselines your workload across common architectural dimensions that are defined by the six pillars of Well-Architected Framework. Now, you may be familiar with the idea of Well-Architected Framework as a review mechanism to identify and address high-risk items that are affecting your workload. However, the principles and guidelines that make up Well-Architected
Framework are all there for you to be used at any point in time. So you can use them even during your planning and design stage. And the earlier you adopt the
Well-Architected Framework, the sooner your workload is on its way to being well-architected. So by the time your
workload hits production, it's already halfway there in terms of being well-architected. So well-architected gives
you that foundational layer. And upon the well-architected foundation, you can architect individual capabilities and provide targeted solutions to them. So how do you organize your
workload into capabilities? So we have a few different
techniques that work very well. The first one is business ownership. This is especially applicable
to very large workloads. Think of something like
an e-commerce solution. The product recommendations
capability may be owned by the Product Marketing Department. Customer support chatbot may
be owned by Customer Success. And each of these business units will have their own success criteria, their own business
goals, their own budget, their own skills and staff. And this way, you can draw boundaries around these functionalities
as capabilities. Now, this can sometimes run
up against Conway's law, and Conway's law states that
businesses build software that mirrors their organizational
communication structure. Now, if your organization
is already building teams that align with business,
then it is usually simpler to arrive at your
architecture to make sure that the business intent is being met. If you have very large technology centers of excellence or technology-aligned teams, sometimes the technology choices made by those technology-aligned
teams can influence or even limit how you
achieve your business intent. It's a hard problem to solve for sure, and it's not something
that we're really going to be able to solve here, but just something to keep in mind as you organize your
workload by capabilities. The next technique borrows
from software architecture and uses the idea of
domain-driven design, or DDD. So DDD promotes this idea
of organizing your workloads by bounded contexts. And each bounded context
represents a business domain. Event storming is a popular technique by which you can identify
your domain boundaries or bounded context. And this is a one-day workshop where key stakeholders come together and work together to
identify the bounded context. And once you identify
these bounded contexts, they can become your
workload capabilities. The next technique is
less formal than DDD. It just makes use of basic
good architectural practices. And I would call it Architecture
101, if you will, right? So it brings together
related functionalities that achieve a common objective and groups them into a capability. So this is what I would
call functional cohesion. And once you identify
capabilities in this manner, you would wall them off
from other capabilities within your workload,
loosely coupling them. So we are making use of coupling and cohesion as two driving factors to identify our capabilities. And this way, each
capability can be operated and evolved independently. And the last technique I want to talk about here is
distinguishing traits. So distinguishing traits are
portions of your workload that exhibit certain
qualities that set them apart. These usually translate to
your competitive advantage or business differentiator. Imagine offering something like the easiest insurance quoting process or the fastest checkout in e-commerce. These are all reasons why
someone will use your solution or something else that's out
there in the market, right? So once you identify
portions of your workload that need to be solutioned with distinguishing traits in mind, you can draw your boundary around those functionalities as your capability. Now, irrespective of how
you slice up your workload into capabilities, you'll see that distinguishing traits really matter as we talk about this later
in the session as well. And you can use either one or a combination of these techniques to arrive at your capabilities. But just keep in mind that the idea is to not wholesale solution your
workload as one giant thing, but instead slice them
up into smaller portions, making it easier to solution for them. In the absence of something like this, it's very common that you try to solution with a broad stroke of brush, you try to standardize with a common set of technologies across your workload or even across your enterprise. And that can lead to a situation where your technology
choices are suboptimal for portions of your system where better options may exist. Alright, so now that we know how to break your workload
into capabilities, let's talk about what
makes up a capability. Alright, so capability is
made up of two factors. Sounds straightforward enough. So there is functional requirements and non-functional requirements, NFRs. So functional requirements
are well understood, usually they are well stated. Your product team talks to your business, documents them in the form of epics, user stories, requirement specs, and your engineering team
goes and builds them. NFRs, on the other hand, although everybody realizes
the importance of NFRs, having security, availability, performance, these all matter, but usually they are not
well stated in advance and your engineering
team has to discover them and ensure that these
are not an afterthought and not bolted on later. So what our approach
promotes here is elevating non-functional requirements
to first-class status. They should be at the forefront of any technology decisions that you make. So what happens when you do not have non-functional requirements
well stated by your business? So in that situation, you need to discover or elicit them. So the technique that we use here is called dialogue-based discovery. Now, the business intent can
exist at multiple levels. At a workload level, they usually align with some sort of a CXO objective or a board-level objective. You want to improve your profit margins, you want to increase
your top-line revenue. Or it's some sort of a
risk-reduction initiative or a compliance initiative. At the capability level, the business intent tends
to have a leaner focus. So you would talk to your business and try to understand what they're trying to achieve with any given capability. And you will hear terms like this. Let's take for example that you want to improve your customer satisfaction. Now, customers could be dissatisfied for many different reasons. You may find that shopping
carts are being abandoned. You may find that you're getting a lot of incidents and tickets, you are getting a lot
of complaints, right? But for us architects,
we need to understand what is causing the dissatisfaction and ask business more
pointed questions like, "Hey, are the users seeing errors in critical user journeys?" "Is the application slow?" "Is the application
unavailable when they need it?" And through these kind of questions, we can discover our
non-functional requirements by arriving at certain qualities, right? So each of these statements that business has stated
in plain English can result in non-functional requirements. So in the customer satisfaction scenario, we ended up with performance,
resilience, and availability. But these are by no
means exhaustive, right? There could also be other reasons like usability or
responsiveness of the system, which could be causing
user dissatisfaction. Now, this alone is still not sufficient for engineers to go build. You need some concrete
metrics or SLOs to chase. So you dive a level deeper and ask more pointed questions that, "Is it okay for the page load time to be two seconds, 99th-percentile time?" Is it okay for the system to be unavailable for a few minutes, five minutes in a month?" And that will lead you
to more concrete SLOs that the engineering
team can now go chase. So that's how you arrive
from your business intent to your non-functional requirements. But imagine you come out of a conversation with your business and you end up with a dozen NFRs, right? Everything sounds great. We want performance, we want security, we want resilience, we
want cost-effectiveness, and there is nothing that
I want to really leave out. But you'll notice that once you start to put these NFRs side-by-side, they are at healthy
tension with each other. If you're building a highly performant, highly resilient system with
redundant infrastructure, expensive hardware, it's obviously going to go against cost-effectiveness. So that is that trade-off. And you need to have this
trade-off conversation because you want to end up with what we call architectural
characteristics, which is our second C, right? So architectural characteristics are what I would call the non-negotiable NFRs that are disproportionately more important and vital to the success
of your capability. And these are what define your capability and are separate from the aspirational non-functional requirements
that you want to meet. These are critical for your
capability to be successful. And you really want to
chase a handful of these, literally something that you
can count on one hand, right? If you start to chase about
six or seven of these, then it becomes hard to engineer for. You may end up with an
over-engineered system or you may dilute their
significance altogether. So really, you want to keep them limited so that you can target
them and achieve them. So let's understand this with an example. So imagine a workload
that's a trading system which has a capability
for order management, which allows you to place trades. So here, you will have a conversation with your business and you'll determine that scalability,
reliability, performance, and regulatory compliance
are your critical NFRs that are your architectural
characteristics. And in achieving these, you may need to trade off some other NFRs. You may need to trade off cost for the reasons that I mentioned before. So this is a complex engineered system, high-performance hardware,
redundant infrastructure, and highly scalable, right? So cost is at odds with those qualities. Simplicity is nice to have for any system, but just the inherent
domain that you're operating in here makes simplicity
hard to achieve, right? So no matter how many
technologies you can throw at it, it'll always be like a complex solution. Lastly, agility is another
thing you may need to trade off because when you're engineering a system for high reliability, high
performance, and scalability, you want to ensure that any new changes are not causing any regression. So you want to meticulously
validate any new changes and that can result in
longer release cycles. Which is okay, we are
prioritizing the effectiveness of those architectural characteristics and trading off certain other qualities. Now underneath this, we still have the well-architected baseline, right? So well-architected is still giving you those architectural dimensions that every workload on AWS should have. But architectural characteristics
take this a step further and enhance your capability
for what sets them apart and becomes your competitive advantage. Now let's take a look
at another capability within the same workload. This time, it's end-of-day
reporting of trades, right? And this is something that is emailed to your traders before the start of the next business
day or next market day. So in this situation, you are prioritizing cost-effectiveness, you are prioritizing
ease of implementation and ease of maintenance. And in achieving that, you may actually trade
off scalability, right? You don't need your report generation to be massively scalable because
you can batch them, right? You don't need the performance
to be highly optimized because your users don't care
how long it took the report to generate just as long
as they receive them in their inbox before the end of next day, or before the start of next day, right? So in this case, a separate capability within the same workload is resulting in a completely different
set of characteristics. And these capabilities come together to achieve the overarching
goal of the workload. So as they say, the whole is greater than the sum of the parts, right? So in this case, the
whole is your workload and the parts are your capabilities. And I try to draw a parallel with a team sport like soccer, right? There are multiple players
that make up a team and each player has specific skills or technical attributes
that make them successful for the role that they play in the team. Now, the coach of the team runs
them through a standard set of drills to prepare them for match days with the intent of winning the game. And that's what I would equate to the Well-Architected Framework. Each capability within
your workload benefits from the Well-Architected
Framework equally. But beyond this, there
are also individual drills that are catered to specific positions or specific roles in the team. So goalkeeper will have its own drills. The forward will have their own drills, so they'll take shooting practice, free kicks, and all of that. So these are what I would
equate to capabilities and their specific characteristics. And together, the players come to help the team achieve their objectives. Now, keep in mind that in a team sport, there is also this idea
of a marquee player or a franchise player. You know that if that
player has a great day, your team is more likely to win. Similarly, within your workload, you may have certain capabilities that are like your flagship capabilities, and the success of your workload depends on that one capability. So sometimes you may need
to pay extra attention to certain capabilities and you may find that
you are investing more in that capability, which is normal. Alright, so having said all that, how does this all tie back
to AWS services, right? We are after all here to
simplify our technology choices when it comes to AWS services. So AWS services exhibit the
architectural characteristics of our services just from the definition. So if you see the words highlighted here, you can see that Amazon S3
is an object storage service and it offers scalability, data
availability or durability, security, and performance as
its standout characteristics. So if your solution
needs an object storage and if the characteristics
that you're trying to achieve for your capability match
yourself with what S3 offers, then that's a straight fit. And you start to see
this across our services. If I had a dollar for every time I answered the ECS versus EKS question, I'd be pretty wealthy right now. But ECS offers simplicity of deployment, manageability, and scaling. So if you're looking for something like that within your workload, then ECS may be the right choice. Let's look at one last example, DynamoDB. Fully managed, serverless, high performance, high scalability. So as long as your data storage and data access patterns
match what DynamoDB offers and the characteristics that you're trying to achieve for your capability coincides with what DynamoDB offers, DynamoDB may be a good
fit for your architecture. Alright, so with that, you now know that you can use
architectural characteristics to pick your services. We're taking a real
jobs-to-be-done approach here. So if you're familiar with that idea, you have a job and you're hiring a service or a product to do that job. And the job in this case is
defined by the capability and the characteristics that you're trying to achieve for that capability. And you can always fire the service if the service doesn't do the job. Alright, that brings us to our third C, which is constraints, right? So constraints are
something that are inherent to a business or an enterprise, right? And these are things that relate to concerns like your
budget, your timelines, the skills that you
have on hand, any risks. So with that, you are usually... The constraints are beyond the control of the team that is
building the architecture. It's just something that you
need to learn to work with because these are
inherent to your business and not something that
you can change overnight. And constraints come with a bit of a negative connotation, right? They impose restrictions on you, they reduce your flexibility, and they limit your options, right? But we want to also take
another view on constraints. Constraints can actually
be beneficial to you. So constraints encourage
creativity in your solution, they promote frugality. A couple of years ago at re:Invent, Werner Vogels, our CTO, introduced the idea of frugal architect. So constraints actually help you be frugal with your architectural choices. And you may see that I'm saying limits options again as a positive. But in this case, what limits
options is actually doing for you is it's simplifying
your choices, right? It is narrowing your solution space and allowing you to arrive at your technology choices faster. If your constraints are outright eliminating some
technology choices for you, what's remaining is what your
solution space is, right? So this way, we are solving
for that choice paralysis and we are actually using
constraints to our advantage. So these constraints are
what I would call essential or inherent constraints of your business. But there are also artificial constraints or accidental constraints
that sometimes get introduced. And usually they manifest in the form of enterprise guidelines. So if you are familiar
with some statements that you see here, these
are not uncommon at all and it exists in pretty much
every enterprise, right? They usually enforce or restrict use of certain technologies, certain architectural patterns, and most likely, they exist with... Most commonly also, they exist
with very good intent, right? These are based on some past research, some past evaluations,
some past experiences, or an effort to standardize. But what they can also result in is they are imposing restrictions
on you artificially and you're not able to
solution for the capability the way it would result
in the best solution. So what we recommend instead is using your three Cs, capabilities, constraints,
and characteristics, to arrive at your technology decisions and then evaluate them against
your enterprise guidelines. If your enterprise guidelines are actually improving your solution, by all means, borrow from
your enterprise guidelines. And by no means saying go have a fight with your architectural review board, throw away all the guidelines. No, no, they are still
very important, right? But what we are promoting is this idea that don't let them set in stone and stand back in a time
that has not moved, right? Your enterprise guidelines
can advise your solution, but any new discoveries that
you make through your three Cs and the intentionality
that you have established behind your technology choices, those new discoveries should feed back into your enterprise guidelines. And that way, they don't stay stagnant and they are continuously
evolving as well. So it's very common that
enterprise guidelines are outdated or something from five years ago and not fit for the purpose anymore. This is an intentional
forcing function for you to continuously evolve
your enterprise guidelines and it can be really
serendipitous when this happens. Alright, so we've taken all this time to establish the intentionality
behind our architecture. We don't want to skimp on the last step, which is an important step as us technologists are not very fond of documentation, right? But what we are suggesting
here is not write pages of documentation, but
instead use a concept that most of you are likely
already familiar with. And that's the idea of
architectural decision records or ADRs, right? And ADRs are this lightweight base of documenting your architecture. And I say that ADRs and the architectural
diagram is all you need to document your architecture. You don't need pages of
documentation in a confluence page or a wiki to understand your architecture. So for those of you unfamiliar with ADRs, I want to just run through
what makes up an ADR. So you would start with the title. And here, you define what your architectural decision is for, and here you can specify what capability you're trying to achieve. The status goes through different stages like proposed, under review,
accepted, or rejected. And rejected decisions are
also good to have around because you don't want to go through that same evaluation cycle again if something was already
evaluated and rejected. And if the ADR is no longer required, it can also be deprecated. The next stage is the context where you'd actually describe your problem statement in detail. And here, you specify all the things that are governing your decision. And lastly, in the decision, you actually specify what you're using as your technology choices, the ultimate decision
that you ended up making. And along with decision, we also want to document our consequences. What are the consequences
of this decision? What are the trade-offs you had to make? What are your fallback options if the decision doesn't pan
out the way you expected it to? And in some cases, you would've
evaluated some alternatives, it's useful to document them too because those could be your fallbacks. If something closely lost
out to the ultimate decision, if the decision doesn't pan out, that alternative may become your actual architectural choice, right? In addition to these standard ADR fields, we also recommend documenting
some additional fields. So we recommend documenting
the stakeholders who are involved in making the decision, the actual people who were involved in coming up with this decision, because these decisions are
never made by one person. So even though you are the architect, you likely did not come
up with this on your own. So usually, there's a
product team involved, engineering team involved,
architecture involved. So put the names of the actual people who are involved in making the decision. That also sets some accountability and conviction behind the decision. And if you ever need somebody to blame, you know where to go, right? Additionally, we also recommend documenting your characteristics and constraints as separate fields. You could of course have them stated within the context as well. But sometimes if the
context gets very verbose, they can get lost in there. So if you surface up your constraints and characteristics as their own field, it creates a shared understanding of what drove this decision
in the first place. Alright, so having said all that, let's walk through a practical example. And we'll take a workload
like e-commerce system and pick a capability
which is product catalog. So for the product catalog, our business intent is that we want to offer a diverse collection of products with best-in-class user experience. And for this, we had a
conversation with our business and determined that the
architectural characteristics of scalable, reliable,
and performant are going to be really important for this
capability to be successful. This is what will lead to the adoption. We're also working with
a couple of constraints. We want to use containers, but we have very limited
containers experience of running workloads in production. We also want to support a wide variety of products across many regions and we're not selling only
particular types of products. So with that, we arrive at
our architectural decision. First, let's look at the alternatives. So we start with the
idea of serverless first, but we believe that millions of users will use this
capability on day one and they'll use it around the clock. So we feel like provision compute with autoscaling will work better. But we want to use a
containers-based architecture. We do not want to directly deploy on VMs. But we do not have any
Kubernetes experience because we only really
started getting started with our containers journey. So that's the compute aspect. For databases, we evaluated
relational databases and we found that our product schema, because of how many different types of products we want to support or how many regions we want to support, it was very hard to
standardize on a data model. So we ruled out relational
databases temporarily. And for storage, we
evaluated network file system and we are mostly dealing here with static data like product
images and product videos. And because of that, we found that network file
systems were not working out, were not being very cost-effective. So what we ended up with
in our actual solution, we still went with a
containers-based architecture, what we picked: Amazon ECS with Fargate. So it gives us the
scalability that we need and we can also engineer our applications to be reliable and performant. In addition to that, we
chose no SQL as our database because the characteristics offered by DynamoDB matches up
with the characteristics that we are trying to achieve. And we are able to make
the data access patterns of DynamoDB and the data
shape of DynamoDB work for us. And lastly, we went for an object store because object stores are well
optimized for static data, and Amazon S3 offers the characteristics that match up with the
architectural characteristics that we want to achieve. So this way, you see how we can go from a workload distilled to a capability, use our three Cs, characteristics, capabilities, and constraints, to arrive at our architectural choices. Let's quickly reinforce
this with another example. - Yeah, I think in the interest of time, what we'll do is we'll... You saw in detail how Sushanth
walked through one example. So you can take another example of something like Amazon Rufus. You might have been using
Amazon Rufus to help you shop. So let's say a e-commerce company wants to build in that capability. And the architectural characteristics are that it needs to be cost-effective,
maintainable, and agile with the constraints that you have limited in-house AI ML skills and you don't have too much time because guess what, today
is Cyber Monday, right? So given these three Cs, you know, of course you can evaluate between whether to self host them or not because you don't have the skills, you would rather settle
with Amazon Bedrock. And then similarly, you
don't want to be building and maintaining a
commercially vector database. So you'd rather use Amazon Bedrock. So this is how we arrive at decisions. You can probably take
photo of this just as to show you how to
practically apply this, right? Next, one of the common
questions that we get is, alright, we have workload, we have multiple capabilities
within the workload, and these capabilities can have conflicting characteristics. Then, how do we go about reasoning them and how do we make sure that the characteristics
don't cancel out each other? - Yep, that's a very vital question. And you can have multiple
capabilities within a workload. And if they have the same
set of characteristics, they usually work together to
achieve the common objective. But when they have
conflicting characteristics, for example, if capability A is optimized for performance and capability B is not, capability B can actually
weigh capability A down. And they communicate to
well-defined interfaces. So a couple of ways in which we can solve for this is we still have the
well-architected baseline. So this is uniformly affecting
all your capabilities, influencing all your capabilities. So they should really not be
too far apart from each other. But in addition to that, you already optimized
capability A for performance. So capability A needs to
protect its characteristics. So that brings us to our next concept, which is isolation boundaries. So isolation boundaries
are a conceptual idea that allow each capability to protect its characteristics even when they are interacting with
other capabilities, right? And these can be implemented
in many different forms, right? There are things like circuit breakers, exponential back-offs and retries, queuing, asynchronous communication. And you can even do it
through your application code. But know that good fences
make good neighbors, and similarly, isolation boundaries help capabilities protect
their characteristics. The next question we often get is, everybody understands ADRs are useful and there is consensus
around their usefulness. But many organizations have a
problem either getting started with ADRs or consistently
doing it over a period of time. So how we go about that is
when we'll talk about next. - Yeah, so ADRs is easier
said than done, right? Of course, we all hate documentation. So it feels like there
is additional effort to actually get started
with the ADR process. But here are simple
three tips that we have, you know, synthesized here based on what customer journeys
we have seen on AWS. Start with simple cross-functional teams because you need to have
that dialogue with business, with product and engineering, and also the business
stakeholders so that we know what capabilities we are
building for that system. And then keep the team lean. You don't want to build a big team and get, you know, stuck
in making decisions. That's not the intention of it. It needs to be a lean
cross-functional team. The second aspect is
around the process, right? So there needs to be a process to store these ADRs, and most importantly, it needs to be centralized and accessible. And third important thing is it needs to be version controlled because you can actually see
the evolutionary thread, right? You need to be able to see how we have taken decisions
over a period of time. And lastly, governance, right? After all that is said and done, if you just a bunch of
ADRs in a weekly page, that might not necessarily everyone follow those guidance, right? So you need to be able
to enforce these ADRs. And the way to do it is, you know, simple things like
leveraging AWS services, like AWS organizations and
service control policies where you can control which
services can be launched within a particular AWS account. Additionally, you can even
use services like AWS Config for driving more granular
enforcement, right? So the next question is that we commonly get from our customers when we discuss this framework is, does this apply to greenfield? Does this apply to brownfield? And how do we go about reasoning
with those two scenarios? - Yeah, so this framework
is equally applicable to both greenfield and
brownfield solutions. But the way you approach
these characteristics is going to differ, right? So in a greenfield capability situation, you are mostly working
based off of projections and doing what we call
qualitative analysis. You work with your business and identify the
architectural characteristics to build your capability, but nobody has really
used your application in production yet. So you don't know the real usage patterns or how your application or capability will actually
be used in production. So until you are actually in production and seeing that usage, you're mostly working
based on projections. And you are definitely going to do some market research to arrive at your architectural characteristics, but you are kind of hoping that what you made the right choices. With brownfield, you actually
have well-defined metrics and usage patterns already
established in production. So if you optimize your capability for scalability or performance, you know exactly what level of scalability and performance you're getting today. And if you need to improve that, you have a baseline to go off of. So this time, you are using real metrics and that gives you the ability
to use quantitative analysis, and that way, brownfield can sometimes actually be an advantage. So I know us engineers love to
work on greenfield solutions because it gives us a blank slate to implement all our ideas, but brownfield has also
its advantages compared to greenfield, right? So with that, we have the opportunity to still break the
workload into capabilities the same way in both
brownfield and greenfield. But the way you determine your
architectural characteristics will be different for
greenfield and brownfield. In fact, if you don't have
your workloads broken out into capabilities today
in brownfield situations, after today's session may
be a time to go revisit and see how you can break
down your large workloads into smaller capabilities. - Perfect, so now that we
have seen this framework on the three Cs, let's
bring it together, right? So always start with capabilities, right? And the default reaction
and default trend we see is starting with technologies,
please don't do that. Start with capabilities
and pay extra attention to those non-functional capabilities because we are proposing that those needs to be your first-class citizens
in this approach, right? Second, extract the characteristics
from these capabilities. And again, make sure that you are not picking too many characteristics, and like Sushanth mentioned, just give it a single handful, right? And after you have the characteristics, you're then going to be shortlisting your technology choices. As you can see, clearly it's not until step three you're thinking about any specific technology. So that's when you shortlist your options. And when you do shortlist your options, keep in mind the decision framework of, you know, factoring in
the enterprise guidelines with the three Cs. That is something
important to keep in mind. And then you arrive at your
architectural patterns, depending on your business. And the most important thing
to do here is that it's not, the job is not done when
your architecture is decided. That is actually when your
first iteration begins, right? You got to evaluate your architecture. Like we said, architecture evolution is a continuous process. So by doing this over
and over and over again, you're going to be able to evolve your architectures
more organically and more consistently
over long periods of time so that it'll quickly
and dynamically support any business outcome, right? So with that, recap,
the final slide, right? So as you finish your
week here at re:Invent, I know you're gonna
have tons of information about new products and services and features and solutions, and yet another architectural pattern. But the first thing we
would love for you to do is start shifting that mindset to start looking at your architectures as living systems, one, and then recognize that
there is an evolution that is going on, is that reactive? And, "Is there something that I can be doing proactively?" So have a plan for
evolution, step one, right? And let capabilities be anchored at the center of your
architectural evolution. Like we have discussed before, it's not technology, it's the three Cs and capabilities, right? And then have a plan to evolve incrementally and proactively. And ADRs, we've provided some tips, so please get started on ADRs. We are actually starting
to see customers build knowledge based-based ADR application. So who knows, that might be the easiest thing to actually build. And lastly, consult with
your AWS account team, right? So we as AWS architects, you know, we get to see what works
and what doesn't works when we look at thousands
of customer journeys or AWS. So we have learnings from all of this and we are here to share that with you. So please consult with your AWS team. And remember, at the end of the day, what matters is a disciplined approach to architectural practice. Focus on capabilities
instead of technologies and consistency of approach
to evolve the architecture. So that's what matters. So with that, thank you very much. We would appreciate if you
can pull up your phones and provide feedback. And lastly, if you want,
so this is the framework. We also do a workshop around this. So if you feel like this
workshop would benefit you to apply this framework to
your particular use case, you can reach out to your account teams and they'll facilitate that. And lastly, if you would
like to see an ADR kind of a tool within your AWS console, please indicate so in the
feedback because who knows, next year we may just have it, right? So with that, thank you very much. We'll be available in the hallway to my right or to your left if you wanna have any further discussions. Thank you.
- Thank you. (audience applauding)
---
video_id: rG8OKTYK6o8
video_url: https://www.youtube.com/watch?v=rG8OKTYK6o8
title: AWS re:Invent 2025 - A leader's guide to agentic AI (SNR201)
author: AWS Events
published_date: 2025-12-02
length_minutes: 47.68
views: 2452
description: "In a landscape of rapid AI evolution and daily headlines, senior leaders need clarity on what Agentic AI means for their business. This session cuts through the noise to provide a practical understanding of autonomous AI agents and their strategic implications for your organization. We will demystify Agentic AI and focus on what matters most to leaders. We will share how both management and architecture models will need to evolve to get value out of the autonomous AI systems.  Learn more: AWS re..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
---

- [Ishit] Good morning. - [Audience] Good morning. - Well that's great. I love this crowd. (audience chuckles) Well, welcome to re:Invent and Las Vegas. I'm excited to be here with you today. This is my 13th re:Invent. I attended first six like
many of you in this room as a customer of AWS, and this is my seventh one
as a builder here at AWS. Now in my role at AWS, I wear dual hat. I get to lead and build and solve business problem
using technology and AI. And I also get to work
with C-Suite and executives of some of our largest
customers like yourselves. How many of you in the room
are first time at re:Invent, show of hand? Well, wow, many. Welcome. Any veterans here? Five plus years? Excellent. Well, I hope you have a
fantastic week because it's an amazing time to be a senior
leader in the organization. What a privilege that we
all have to become the agent of change and lead our organizations beyond just automation to high agency. So in this session over
next 40 minutes or so, I'm going to talk about
what do leaders need to do to lead in this new era of high agency? What are the mental model shifts that we require as leadership team? How do we re-envision
our business processes and then go slightly deeper
into some of the technical and architectural capability that help bring this vision to life. So let's dive in. Now, I'm sure many of you
have seen lot of things being labeled as agents, but when you peel back that wrapper, underneath that you find
many of these things. You have just good old scripted automation that takes repetitive predictable task and in a fixed set of workflows, codes it. As you move up that autonomy chain, you have generative AI assistance and the chat bots that
provide useful information, has access to data,
can respond to queries, can actually summarize the
document and information and has an ability to respond, but very limited ability to act. As you move up that autonomy chain, we start to see higher order business task and the goal that these agents can do. The goal and task-based
agents are optimized for completing a specific
task by working with humans. This is where we start
to see lot higher value. And then at pretty high up is
the highest level of autonomy of agentic system where
multiple agents work together, take a much higher order complex and sometimes ambiguous task and are able to break that down
into steps and pursue that. So this is a good mental model to think about when your teams come and talk to you about
automation or AI agents. Now this is not to say that
one is better than the other. As senior leaders, it is
important that we understand what tool to apply to solve which problem. So the question that I really
find useful when I'm talking to my team is to what are the behaviors or attributes that makes
something an agentic system? So let's talk about what
are some of those behaviors. Agentic systems are goal driven. As I talked about, they
take a higher order goal or an intent and have an
ability to break that into multiple chunk- chunks of
tasks to go and complete. They are resourceful, they have an ability to access the tools, the data,
the context, the hierarchy and the roles inside of your organization to take those action. They remember, they have a memory, so that you don't start again when you have a new transaction. They remember that there was an issue with the billing last time
I tried to do something. They learn and adapt. They get better with the feedback and they use escalation not just as a mechanism when something is wrong, but as an inbuilt trust mechanism to involve human in the loop. So it's good to keep this framing in mind when you think about agentic system. Now you might ask, but
we've been on this journey for a couple of years now, so why now? What has changed? And there are two fundamental shifts that are happening very, very rapidly that we as senior leaders
need to pay attention to. The first thing that is happening
is that the unit of task or the length of task
that AI can do is doubling roughly every seven months or so. So you now can take a
lot more complex tasks and give agents to go and
accomplish those tasks. Now as senior leaders, we know
that just having a technology or tool that is very
intelligent and highly capable but is extremely
expensive and unaffordable is not very useful, is it? So what is also happening on the other end is that the unit price
or the cost to access this intelligence is
continuously dropping as well. MMLU is a standard benchmark, massive multi-language understand- massive multi-language task understanding and that is used to
benchmark language models. And just to give you the context, an MMLU of 43 is similar to
a struggling high schooler. They mostly are guessing answers, but they're very confident. I have one at home so I
know how that feels like, I'm sure many of you do too. But MMLU of 83 is like a PhD level expert. They understand the nuance, they are able to deal with ambiguity. And so we can see that
MMLU and the unit price to access both of this is dropping. So we are in this sweet where
the capability are increasing and the unit price and
the cost is dropping. And this is why we are starting to see real world applications of agents. Druva is a data security company I'm sure many of you
in this room use them. Now when you're dealing with
a cybersecurity incident, a ransomware attack, you
don't have time to go through like thousands of pieces of logs and information manually
to sift through that when you're in middle of the crisis. And so Druva worked with
AWS to build Dru AI. These are agents that don't just respond, but they take action. They look at proactively the logs and autonomously detect the system issues and then they take corrective action, they move the data around,
they update the policies, they move the data through
a storage that is lot more cost effective based on
the data retention in the policies that you set,
driving lot higher value. But to take advantage of this requires a change in how we lead. If you think about historically, leadership has been mainly about
optimizing for determinism. We are all rewarded for lowering and reducing deviation, having repeatable, predictable processes that
do the same thing over and over again by reducing the error rate. And now this works today. But the non-determinism,
the ability to improvise, the ability to adapt, the
ability to take different action based on the context
and changing requirement with agent is a feature, not a bug. Now I'm sure this might
make some of us nervous, especially from regulated industries. So this is not about just
stepping into the wild west. This is about us as leaders being aware that the non-determinism is
what gives agents the power and how do we safely harness this by setting up the right guardrails. And the mental model that I
find useful is to think about how we work with some of
our high agency teammates. You don't call your high
agency teammate every Monday and say, hey, I'm going
to sit down with you to give you specific
tasks that you are going to execute every single day
and then you're going to come and at the end of the day,
report to me what you did. Right? We actually give them a strategic higher order intent, we
give them the boundaries within which they can operate, we empower them with the right resources and access that they
need to get the job done, and then we trust them to escalate to us and involve us as needed. And so to lead in this
high agency requires a shift in the leadership model because we are no longer
managing automation, we are managing thousands
of agents at scale. And that intelligent autonomy and managing that at scale
requires shift into four key areas of leadership. Now, please keep in mind
that the mental model that I'm going to share
are just mental models. They are not recipes or
strict operating model. So take them with that lens and four areas that I'm
going to cover starting with governance. Now traditionally,
whether it is in software or in compliance, we have
gate based governance system moves, comes to a
complete stop, waits for someone to verify a series of
things via a checklist that has been defined and maybe audited a
couple of times a year. They approve it, then
the system moves again, stops again at the next toll gate. Now this works today, but
when you have hundreds and thousands of agents, you can't put these toll booths in front of them consistently. That will just slow it down. Instead, the mental model that is useful is to think about providing
that strategic intent and then having a policy engine that can govern this at scale. And as I was thinking about,
well, what governs like this? The, the thing that came to
my mind is that if you look at how board of directors
actually work with the CEO. Once again, they don't go to CEO and say, I'm going to tell you exactly how to run your company every single day. Board and CEO typically align on a strategic direction and the vision, periodically they go
and audit and calibrate. But there is also
specific guardrails around what requires board approval and the management team knows
when to engage the board. So it's a useful mental model to think about governance this way. The second shift is in risk. Now today, our risk management
controls are pretty much like a factory floor. On a factory floor you have
fixed threshold, right? Even today in many of our organizations, we have fixed threshold regardless of the exposure of the risk. So if a purchase order
is more than $2 million, it requires approval of a vice president. If it is beyond $10 million,
it must go to the CFO. Now these controls for risk
break down when you're dealing with autonomy at scale. The mental model that I find
useful is to think about managing the risk like a trading floor. And on our trading floor, the risk is actually managed
lot more aggressively, but it is managed through real
time visibility and control. Traders have a portfolio that
they can play the trades in. Not every move is managed,
but if the portfolio or a particular transaction
violates the policy, then there are circuit breakers
that stops the trading. Let's say the portfolio drops by 20%, the circuit breaker kicks
in and stops the trading. And so we need to think
about agents this way where agents have to earn their liquidity by operating within the risk controls and the boundaries that we design and have it with real time
visibility and automation. And it's also not about
managing every single agentic transaction, but also
monitoring the systematic drift in a multi-agent system. When that happens, you want the
circuit breakers to kick in. One of the most fundamental
change though is going to be in the organization structure. And again, as leaders, we all know this. Every single time there has been a major technological change, that
has required us to reimagine and rethink how we organize. Before cloud, we had application
and development teams and then infrastructure and
technology operation team. When cloud came, these
boundaries got blurred. You started to get full
stack engineering teams that can operate at all
layers of the stack. In fact, with agents, we
are seeing this inside of our own teams where boundaries
beyond just engineering, including the business process
roles, product management, engineering, TPMs are all getting blurred because you have an ability to execute and work with agents throughout
the entire value chain. Historically, our org structures
are vertically optimized. Now this structure provides a stability, but it is not designed to move fast. If a customer has an
issue that gets handed off sequentially between the
department from customer support to supply chain to distribution
to return and refund and it slows it down. But the mental model to use in
terms of how do you organize for agents is like an immune system. How does our body's immune system work? If there is a threat or
if there is a problem our white blood cells don't wait for a memo from the brain, right? They don't call a meeting with the lungs, they actually swarm that problem and then figure out how to solve that. So the cross-functional
teams that are organized around a business workflow, regardless of the current departmental structure is how you really get outcome from agents. The other thing that happens in this kind of art structure is that
system learns constantly. So it's sort of like
creating antibodies, right? So when you have this responsive swarm, it gets better with period of time. The last piece, and so before, before I go
there, really what we need to think about is that
agents should not be limited by your org chart. They should be limited by the objective that they're pursuing. That brings us to the last part of this leadership mental model
and that is around culture. Historically, we have all optimized the culture for precision. It's sort of like, well, you gotta almost hit a
bullseye every single time. That's what we reward,
a perfect execution. But what happens in a
research lab like culture, that culture is open to new discovery, sometimes good, sometimes bad. But if those mistakes happen, they are used as a learning mechanism. They're documented,
they are shared widely, and the new discovery and
adaptation is once again a feature, not a bug in
this kind of a culture. And so that's the shift that we need because what we are trying
to scale is not obedience. We are actually trying
to scale the intelligence throughout our organization. And so the four key
leadership mental model shifts that I talked about, governance
like board of directors, that provides strategic direction, the continuous calibration
and the guardrail risk management like a trading floor where you have real time
visibility and circuit breakers. And then agents earn their liquidity and authority to operate
by consistently showing us that they're operating
within those risk controls. The organization structure
that is like an immune system that is a lot more fluid and responsive. And then finally, the culture that is like a research
lab culture that is open to new discoveries. If you wanna read more,
you can scan that QR code and dive deeper into some
of these mental models. Now I wanna talk about
the business process and I'm going to pick a business process that I'm pretty sure
most of us in this room are familiar with, which
is accounts payable. Now traditionally the goal
of an accounts payable business process has been to pay invoices on time and accurately. And I want all of us to time
travel to pre-ERP days, right? So just stay with me here. In the pre-ERP days,
what happened was that an account payable system
had a fixed goal to pay every invoice on time and accurately, but the workflows were vertical. So procurement will process the PO, receiving will confirm
the receipt of the goods, treasury will make the payment, and AP will post the invoice and so on. The SOPs were all
vertically inside of each of the department and the function and then there was sequential
handoff that happened. Now in this kind of a system,
if there was any error or an issue, it'll manually
get kicked back into the previous process. Somebody will have to call the
department to fix that issue. How many of you in the room have been part of an ERP implementation or run an ERP? Okay, several of you. Now, what happened during ERP is that we could not look at
these vertical processes. We had to re-engineer an
AP process horizontally. We had to connect the dots
between procurement, receiving, treasury, AP and so on. That- that forced us to talk
across department and function to relay out our business process. But that- there was still limitation because the goal was
still fixed, which was to pay the invoices on
time and accurately. And if there was an issue,
anytime during the process it'll get kicked back and
then manually you'll have to handle the exception. Now, what if in an agentic
system that I described earlier, we take a lot higher magnitude goal. What if the goal of AP is not
just to pay invoice on time but to optimize our cash flow? And the system has the
freedom to operate fluidly within the boundaries that we set. So a particular invoice will
go through all of the steps, but then a second invoice comes in and the agents will know
that this invoice is in Euro and I have a 60 day payment
term on this particular invoice. That means I'm going to
call a Forex trading agent and say, can I invest this for 59 days and actually improve my cash flow? Or a third invoice comes
in and it recognizes that last four times I
approved this particular vendor payment, it had to go into dispute because we did not like the quality of the deliverable that the vendor had. And so this time, I'm going to proactively bring human in the loop and say, even though approval
processes have confirmed, I'm going to enroll the human and say, hey, last four times we didn't
like what happened here. Do you still want me to pay? And so that's a lot higher order task, but also a lot more fluid workflows that are happening here. Today, though as I was talking about, we are already seeing
goal-based agents being in play. This is where you have a planning agent or a planner that takes
this higher order task, breaks it into manageable chunk, and then you have orchestrator
that works across individual agents inside of each of the
function like procurement, receiving, AP, treasury and
goods to get to the payment and reduce the cycle time. In fact, we are seeing
this in Amazon as well. I'll give you an example of
an orchestrator within Amazon. In our warehouses, we
have over a million robots that actually help us safely and quickly move the packages around. And we have this orchestrator
called deep fleet sort of think about this as
a brain of this robotic fleet that manages these 1
million robots distributed all over the world, across our warehouses. And by constantly optimizing that, we are able to reduce
the travel time by 10%. Now, 10% may not sound a lot, but at our scale with million robots and multiple hundreds,
hundreds of warehouses and distribution center,
that means that we are able to get the packages faster to you. And so that's an example of an orchestrator operating at scale, optimizing the business outcome. Now, earlier I talked about the behaviors of an agentic system. Let's double click. We talked about the behaviors, we talked about the
leadership mental model, as well as the business process changes. Let's double click and say what are the technical capabilities that bring these behaviors to life? And there are three
things that agents need. And again, if you wanna
geek out a little bit more in architectural implication,
you can scan this QR code and read an article
that dives a lot deeper into the architectural
implication in your environment. But really, agents need three things. They need intelligence, they need context, and they need trust. And, and if we were to think
of agent as sort of human body, here is how that looks like. The intelligence is sort of like the brain of the agentic system. And your models including
your thinking models for chain of thought,
reasoning, reflection, they provide the brain an
ability to take the intent and break it into task. But just having a brain is
sort of like having a brain in a jar, right? It cannot take any action. So you then have the access, the context, which provides agent and ability
to access the right data. It provides an ability
to actually take action. It provides an ability
to access the tools to go and make things happen. And that's sort of like having the hands to go and do the work. But without trust, none of this matters. And so the final layer
of this is the trust. It is sort of like having an ID badge. What is the agent's identity? Who are they operating on behalf? What are their authorizations
to execute and do this task? And then what are the guardrails that they are going to operate within, to make sure that they're
doing this safely? And so let's double
click on each one of them and say, what are some of
the implication in terms of technical choices that we have to make? So the first thing is that
agents need intelligence. Now in a, in an ideal world, we would want the most intelligent agent
at the lowest possible price at the fastest possible speed that we want to optimize
on all three of them. But in real life, based on your use case, based on the problem that
you're trying to solve, you might not need all three
of these in equal measure. In fact, there is a trade off. So if you're working with an
agent that is legal agent, you might say, hey, you know what? I cannot compromise on
accuracy and intelligence here, but I'm okay if it takes
half a day or few more hours or even a day to gimme the response. So I'm going to optimize for intelligence, but I'm okay to trade
off on speed of response. On the other hand, if you're dealing with a customer service
agent, you want fast, quick responses because your
customers are not going to wait for 10 minutes for agent to come back with a hundred percent accurate answer. And so this is where
you optimize for speed, but then you can trade off
on intelligence or the cost. And this is why when we are thinking of enabling the intelligence
in the agentic system, the choice of models, having
access to different types of model is very important because every model has
a different strength. Some models are good with reasoning, others are very good with quick responses. Some do text-based task really well, others do images and
mathematical task really well. And so this is why our
approach with Amazon Bedrock has been to make the broadest and the widest set of models available, including open source model,
Amazon's own model with Nova, as well as a lot of third party models. And we see this application
inside of Amazon businesses across our company. Take example of pharmacy. Now at Amazon Pharmacy, our
goal is to reduce the time it takes to fill your prescription
and do that accurately. And sometimes the prescriptions
are handwritten notes. And this is where we use models and intelligence to reduce the time by 90% while reducing
the error rate by 50%. On the other hand, on Amazon ad site, we wanna provide the
ability for brands who want to advertise to take an
image of their product and actually touch it
up and make it better and make it a lot more
compelling when they list it. And this is where we optimize for ability to generate compelling images. On the prime video side, any, any football fans in the house? All right, some of you? If, if you're like me,
you always join the game a little bit late and then
you're like, what did I miss? And so you have the
feature of rapid recap, which is where model is going and saying, here are the key things
or key plays that happen and let me catch you up as you comment. Or next gen stats, which actually provides lot more probability and
information to the viewer, bringing them closer to the action. All of these use cases
require different behaviors and different models. Take example of our customer, Syngenta. Now farming, if you think about it, is a, is one of the most complex
multi-variate problem, right? A farmer has to take into
account so many different things. What is the weather
condition? What seed to plant? When do I plant it? What pesticide to use? How much should I spray?
Do I fertilize or not? When do I fertilize it? Now these are just the factors
that are in their control, but they're all dependent on
so many other external factors. The soil condition, the
moisture, the weather pattern, the pest activity in that particular area. And this is why Syngenta work with AWS to develop Cropwise AI, a series of agents that take information from
multiple different data sources including soil condition,
historical yield, the seed quality, but also
80,000 different growth stages of crop to provide specific
action plan to farmers on what they need to do when. Including here's the
prediction of what might happen next week and this is what
you should be doing right now, increasing the yield 5%. Now again, that is sustainable, but it is also providing
a direct business outcome, making it easier for the farmers. So we talked about intelligence, but as I said, just having
intelligence is sort of like having a brain
but not an ability to add. So let's talk about context. Now, context is sometimes misunderstood as this is all about just data. But as I'll show you,
context is lot more than just your existing data. In fact, there's a tongue
in cheek statement, and by the way, this is tongue in cheek, so take it with that, from a senior scientist at
Amazon that talks about the fact that like if you think about this, anything out of an LLM is a hallucination. It is our job because
it's basically predicting the next token and the world. But it is our job to
provide it the right context to make sure that that
hallucination is relevant to what we are trying to solve for. And this is why there
is a growing importance of context engineering. When we think about just
optimizing the prompt, you're just providing a
one-time input with text. Now sometimes you give one
shot, you give multiple example, but it is still back and forth. With context in your organization, especially when you're
targeting complex workflow, you need agents to understand
the role, the hierarchy, the data, the system, the tools. And this is why we are seeing emergence of context engineering
roles in this competency in many of the organizations. So to provide this context,
let's talk about what are some of the technical
capabilities that you need. The first thing is that
agents need to understand the relationships in your data. And take example of a
relationship looks like, right? Gartner evaluates magic quadrant and magic quadrant evaluates
technology vendors, right? That's the relationship
between different objects and domain inside of your data. If you're a retailer, if
you're a media company, if you are a bank, you have many objects, whether it is customer,
transaction, their trade, their viewership behavior, where you need to establish this relationship
so that agents understand how to navigate your workflows. And this is why knowledge graph becomes important in your data strategy. The second thing that agents
need is that they need to understand semantics,
which is the adjacency. Because especially around adaptation and understanding the ambiguity,
you're not always going to have an exit term that
an agent is going to go and search and look for. This is why they need to
understand what is closer to what other thing. So in this example, if we were to envision this in a
three dimensional space, cat and dogs both are pets, so
they're closer to each other. And Gartner magic quadrant and the leading cloud
providers are sort of far away from cats and dog. But if you actually go
into second dimension, cats and dog are not the same family and so they are farther apart and the Gartner Magic
Quadrant is a lot closer to the leading cloud provider. And this is why the semantic
understanding of your data is what AI and agents need. And this is where vector
databases come into play. Because vector is the
language that agents speak, it provides that you need to
provide them relationship, you need to provide them the semantics. But all of this won't matter
if you don't have the memory. And when it comes to
memory, I wanna focus on the bottom right, the four
things on the bottom right. Think about priming. Now, priming is sort of like a mindset. It's giving a role to your agent that you are a financial service agent. That means you're staying in character, you understand what the
role you are playing. You then have procedural
memory which provides the agent the how, right? This is our email system, this is our ERP. And so they have the ability
to remember who I am, what I'm allowed to do and where it is. Then you have Symantec. Symantec is sort of like
your world knowledge. So the memory needs to
understand not just all of the knowledge that is
available in the world, but also understand here
is my Q3 sales strategy and then finally the
episodic memory so that agents remember what happened last time. So hey, you know, this particular invoice, as I shared in the AP example, had issues four times in previous run. So I better remember to
address this next time when I'm encountering this problem. Because if you don't
provide memory to the agent, it is sort of like
having a goldfish, right? It forgets everything and then
you don't get the outcome. And that creates not only
poor customer experience, it also destroys some of those behaviors that I talked about earlier
that it needs to get better, it needs to remember, it needs to constantly
optimize and improve. So we talked about in the
context the relationship and knowledge graph, semantics,
the vector databases, four different types of
memory that the agent needs. But a lot of us know,
especially in large enterprises, that a lot of our content
is not even in databases, it is actually in documents that look like this, right? And they are designed
typically for all of us as humans to understand. We know when we look at this memo to say it is a large bolded test-
text that looks like a title, there are section with
numbering and the bullets, that means I'm looking at a list, there's a paragraph and a break. We know how to read
this, but agents don't. And this is where we need to
focus on taking the content that is in a lot of these documents and convert that into .md
machine readable files that are friendlier to agent. Here's a wonderful example from Stripe and you can read more about it in terms of what they have published,
but which is taking our SOPs, our documents, our workflows,
our org charts, and making into machine readable agent
friendly documentation. Because it's the combination
of structured data, memory, as well as content which is
going to give the ability for agents to have this context. And then the final piece
of this context is ability to access the tools and
actually take action. Now before MCP model context
protocol, those of you who have dealt with lot of APIs know this, that every time when you don't
have a standard protocol, you're trying to connect to a system, you're building a point
to point integration and that is very, very difficult to scale. What MCP has done is it's
sort of like a USC port for giving agent an ability
to access a lot of your tools. And it allows you to
have a standard interface across your systems,
your tools, your data, so that agents have the context
and an ability to access the tool and the
information that they need. So the combination of these pieces, the relationship, semantics,
memory, better content and MCP or any other
protocol that actually allows it to access to the tool,
allows us to move from data just being an asset, which we
have heard many, many times to actually having
knowledge as a capability. Because when we are leading
in intelligent autonomy, we need an ability for
humans and agent to share the knowledge and be
able to share back that with each other as well. And we see this that when
you provide the context, the outcomes are amazing. Rufus is Amazon's shopping assistant and it provides personalized
contextual advice. So if you're, you know, buying something and say, does it need AAA
battery or AA battery, or hey, I bought this
other thing in the past, does it actually work with the product that I've already bought? This year alone, over 250
million shoppers have used Rufus throughout the year, and
those who use Rufus are 60% more likely to complete a purchase. And that happens because Rufus understands and maintains the context and provides the useful information to the customer. The last piece is the trust. Because an intelligent
agent that has an ability and the context, but the
one that we cannot trust will never scale in an enterprise. And one way we can be
sure about the trust is by setting guardrails. And as part of Amazon Bedrock, we have m- we have Amazon Bedrock
guardrails, which allow you to set specific guardrails
depending on the industry, your company policy. For example, before I joined AWS was a CTO for a global media and
entertainment company. And that meant that we
could not use certain term during prime time in our show. Now imagine having to apply this rule agent by agent throughout the enterprise. Well, that will not scale, right? But Amazon Bedrock Guardrail allows you to mention the denied topics to say, hey, never provide financial advice, do not mention competitor. And then that applies to
every agentic workflow and every model that
you're using from Bedrock. So you can be confident
that these guardrails are consistently applied. Think about the sensitive
information filter, the PII, you don't want that to be exposed. You can define some of those
rules in the guardrails. Contextual grounding checks,
which provides information to all of your agents
that are at a policy level to say, you know what? Our return policy is 90 days. You define it here and every time there's an interaction it can. And if there's a conflict,
guardrail will make sure that that is grounded in the
policy that you defined there. But one particular area that
I wanna highlight in the trust is automated reasoning checks. Now, automated reasoning
checks is a search for a mathematical proof
that a function, a program, an agent did something
that it was supposed to do. Now you're doing this mathematically, and I'll give you an example
of how this actually works. So let's say we want to say, how do we know that
Pythagorean Theorem is correct? Well, one way to do this is
to try and draw every symbol- every single variation
of a triangle and then go and manually measure
everything to make sure that the theorem is correct. But that is not practical, right? That is not how we can prove
the Pythagorean Theorem. The way we actually establish that is by having a mathematical
proof that this is correct without having to manually go and draw and measure every single
variation of a triangle. That is exactly how
automated reasoning works. And as part of Amazon Bedrock guardrail, automated reasoning checks are available that reduce the hallucination by over 99%. And even before agentic AI, we've been using automated reasoning for provable security across
AWS for a number of years. So S3's public storage and blocking that or VPC access analyzer where you can say, hey, does my database
have access to internet? Well, how do you actually
prove that mathematically so that you have approvable security? We do this through
Automated Reasoning Check. And that's one of those
tools that allow us to trust the agent and make sure
that we are able to effectively scale them in our companies. I'll share an example from
Amazon Tax and Compliance. Now, when you're dealing with tax rules and compliance all over the world, you have different policies,
different documents, and again, it's very
difficult to do this manually. And so our tax and compliance
team worked with agents to look at 600 different
companies around the world, including the tax policies and the rules to do the benchmarking. Now that's an example where
the trust is very important and you have the provable
security to establish that trust. Now after looking at all
of this, when you start to move agents and operate
multiple agents in production, it is still hard. It requires you to have
better runtime so that you can isolate each of the
runtime, as I talked about, it needs memory so that it
remembers different types of memory that I mentioned earlier. You need to provide an
identity to that agent so that you know who's
that acting on behalf of and what it is allowed to do. It needs access to different
tools, it needs gateway that it can access information from, and then it needs observability
so that you can validate and audit and feel
confident that it is doing what you want it to do. Now all of this requires a set of solid primitives. And if you as senior
leaders, if you go back to like just basic
components of primitives or the building blocks, if you had compute and storage, we pretty much can build many different application. You can create a website,
you can create an ERP, you can create a CRM with
just compute and storage. We believe that inference is going to become another building block of all of the applications that
are going to come out. And this is why with AgentCore and Amazon Bedrock, we
provide these building blocks and perimeters so that all of the things that I talked about
from identity to memory to providing access to
the tool across any model, across any protocol, not just models that are on Bedrock, AgentCore
allows you to do that. So that you can provide agent memory, you can manage the agent identity,
you can provide a runtime that you know is secure and is isolated, you can provide the gateway that manages the connection
with the other tools. And this is why we are
pretty excited about what we can build using these primitives. Now, one of the questions
we often get from leaders is what are some good places to get started? Now, as I talked about earlier, while this is not automation,
it is also not full autonomy. It- they are still early days. And so let's keep in mind that
these are still early days and we make sure that we don't think of agents as a magic wand. In fact, if you have
a predictable workflow with fixed steps, very limited tool use, then just basic automation,
some gen AI assistant works. Agents are really good when you
want dynamic tool selection, when you want to take
advantage of that adaptability and learning where you want
to do pattern recognition and matching, where you are
looking at things like latency and the cost implication
based on the business problem that you're trying to solve. And the three specific areas
where we see the biggest value is in software development,
customer support and customer care and the
knowledge work, especially when you're handling exception
loop type processes. Now, how many of you
in the room do not have any technical debt? (audience laughing) Well, that was a trick question. Pretty much all of us have technical debt, and that's a wonderful example where agents can actually
help us move fast. Because paying off technical
debt locks in a lot of our engineering resources
into doing something that must be done, but doesn't
always necessarily give better business outcome or features. It is sort of like managing the risk. And here's an example
from Thomson Reuters. They had a lot of .net
legacy code that they had to modernize and they use AWS transform, which is our agentic AI
based modernization agent. And they were able to reduce and move that modernization 4x faster. That meant that their
product and engineering teams can actually solve the business
problems rather than just paying off the debt. And so this is a wonderful
example where agents are already helping us drive better outcomes. So I would look at your businesses
and find areas like that where you can start to apply the agent. Now, none of this matters
if we don't prepare our organizations with skill and training. And this is why over last 25 years, we have invested heavily into the training and certification. To build the competency
across not only the companies, but around the countries,
across the world, so that we have the
right talent as leaders to take advantage of this. A lot of this training
is available for free, so I encourage not only all of you, but also encourage your teams
to take advantage of it. One of my favorite things
here is the AWS AI League. What I've found leading
product and engineering teams for a long time is that
gamification is always a great way to get people highly engaged. It's a low friction way,
you're making it fun, people get to learn something. And that's what AWS AI League does. Where you can actually host
a competitive fun league inside of your own company. We also, I believe, announced
yesterday that there's going to be a championship
league with $50,000 price where teams can compete into. And finally, you're going to need experts and we are here to help. There is guidance from AWS experts, many of the folks from our
executive and residence team and other experts throughout the company. We have made over a hundred
million dollar investment in AWS generative AI Innovation Center where we bring machine
learning and AI experts from all over the company to work
alongside you to help you solve a business problem. And then AWS marketplace where
you can quickly get access to some of the prebuilt agents
and tools that you can start to deploy today in your organization. It is really a fascinating
and fantastic future that is ahead of you, and
I'm really excited to see what you all build together. I hope you have a fantastic
re:Invent and rest of the week. Thank you so much. (audience applause)
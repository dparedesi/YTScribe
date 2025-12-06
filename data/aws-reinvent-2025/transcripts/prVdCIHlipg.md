---
video_id: prVdCIHlipg
video_url: https://www.youtube.com/watch?v=prVdCIHlipg
title: AWS re:Invent 2025 - Keynote with Dr. Swami Sivasubramanian
author: AWS Events
published_date: 2025-12-03
length_minutes: 101.42
views: 16553
description: "Join Dr. Swami Sivasubramanian, Vice President of Agentic AI, to learn how Agentic AI is poised to transform the way we live and work. In this keynote you’ll hear about the tools and services you can use to build, deploy, and run secure, reliable, and scalable agents on AWS. We will also dive deep into the engineering innovations that power your agentic systems and give you a glimpse of the future.  1:20 Welcome & opening 11:39 LAUNCH: Strands Agents - Support for Typescript and Robotics 21:12 L..."
keywords: AWS, Amazon Web Services, AWS Cloud, Amazon Cloud, AWS re:Invent, AWS Summit, AWS re:Inforce, AWS reInforce, AWS reInvent, AWS Events
is_generated: False
is_translatable: True
---

I want you to close your eyes
for a moment. I want you to think back to the time you
first successfully built your first program. Do you remember
that sense of accomplishment and freedom that you can create
anything you want? That exhilarating feeling that you
just unlocked a whole new world of possibilities. Now open your
eyes. For me, it was when I first wrote a program for a
scientific calculator. Back in early days of my high school.
You might be wondering, like, what a bizarre choice. Why did
you pick that? It's because I didn't have a scientific
calculator. I had a simple kind. But then it took me a few tries
before I got it right, as I didn't have a computer in my
home when I was growing up. And my high school had one computer
that all of us shared. So I got access to it like 10 to 20
minutes a week. So I had to type fast whenever I got access
to it and then try. And of course, I didn't get it right
the first time because I didn't get all the corner cases or
string parsing and various things. Right. But then when I
finally got it right, I was so proud that I built something I
didn't have before. Suddenly, the kid in me felt that I could
solve extremely hard problems and build things I didn't have.
Finally, I was free to imagine and create. Today, builders
around the world are experiencing that same sense of
freedom with the help of AI agents. But what makes this
moment special and a game changer in the tech industry in
the history of tech are two things. First, who can build a
rapidly changing? We are no longer constrained by the
familiarity of the syntax of language, or having to remember
hundreds of API calls and parameters and whatnot. Second,
how quickly you can build is also changing what used to take
years now or months, what used to take months or now weeks if
not days. We are living in times of great change. For the
first time in history, we can describe what we want to
accomplish in natural language, and agents generate the plan.
They write the code, call the necessary tools and execute the
complete solution. Agents give you the freedom to build
without limits. Accelerating how quickly you can go from
idea to impact in a big way. Take, for example, Ocean
Cleanup that's tackling a really important planet wide
problem by removing plastic debris from our oceans and
rivers. They are harnessing the power of AI to protect marine
life and ecosystems, while also preventing microplastics from
entering our food chain. Their AI system is able to optimize
plastic detection models, predict debris movement
patterns, and maximize the efficiency of their cleanup
operations so that they can operate in the most impactful
locations around the globe, or the Island Institute that's
developing an advanced neural net model for analyzing single
cell, multi-modal brain cell data in hopes to unlock
groundbreaking new therapies. But the reality is, building
and scaling these amazing agentic AI systems are harder
than the problems they are trying to solve. So let's start
by looking at the tools, protocols, and frameworks that
make it easy for you to build reliable, accurate, and
scalable agentic AI systems end to end. But first, let's take a
look at what is an agent. Agents are those that can sense
and interact with the digital environment, and they can
convert high level objectives into series of executable steps.
And they constantly learn and improve their efficiency over
time. But many of you might be wondering, how is an agent
different from a Generative AI? Chatbot. Now imagine that over
the course of the last few days, the traffic to your website
decreased by 40%. Now, if you were to ask a chatbot saying
like why did my traffic go down? It would respond something
similar to this, saying like, that's really concerning. You
should check your analytics to see which pages were affected.
And of course, review any recent changes and look at your
server logs and so forth. Really nice helpful advice, but
not at all useful. But then agent on the other hand, will
pull analytics data to identify affected pages. They query your
deployment system for recent code changes. They scan the
server error logs. And then once it identifies the issues,
it will create a bug ticket with the problem and the
affected code, and even provide a fix for the engineering team
to review and deploy. In effect, the chatbot tells you what to
investigate, whereas the agent investigates, diagnoses the
problem, and initiates the solution. Today, agents are
transforming industries from software development to drug
research, from precision agriculture to architectural
design. Their ability to use and manipulate interfaces the
same way we as humans do, is fundamentally changing how we
build applications, dramatically lowering the
technical barriers to creating powerful, useful solutions. Now,
at their core, every agent is built from three important
components. The first is a model that serves as the brain
of an agent responsible for reasoning, planning, and
execution. Second, the code that identifies or defines the
agent's identity. It establishes its capabilities
and guides through the decision making process. And then the
third is the tools. These are the things that bring agents to
life, whether they are the Backend APIs or access to
knowledge base and databases, code interpreters, or web
browsers that enable real world action. The true power lies in
how you orchestrate all these components together.
Historically, wiring these AI components together was a
really labor intensive and brittle process. Yes,
frameworks help, but they still demand a deep expertise.
Developers found themselves hard coding complex decision
trees. These are the intricate state machines with rigid,
predefined workflows for every conceivable scenario. This
created mountains of boilerplate code that was not
only difficult to maintain, but nearly impossible to adapt in a
dynamic world. Because models couldn't reliably reason about
the next step. Developers had to manually orchestrate every
single tool, call, and state transition. And when something
unexpected happened, and it always did, agents would often
fail. But then, as models became more sophisticated and
gained true reasoning capabilities, everything
changed when errors occurred or there was ambiguity. The model
didn't just fail, it could reason through the alternatives.
We didn't need static orchestration anymore in this
new world. We believed how you build agents should be really
simple, where the agent autonomously plants its actions,
they chain to the all the tools creatively, and they adapt in
real time to unexpected situation. And the developers
simply defines these components the model, the code and the
tools. This is what inspired our teams to build the Strands
Agents SDK. As our teams started building agents for our
own products, we took a step back to rethink what the agent
SDK of the future would look like, one that enables
developers to create agents with minimal code strands
embraces a model driven approach where modern LLMs can
autonomously handle any scenario an agent might face.
This eliminates the need for all these predefined workflows
and complex orchestration code, while also improving agent
accuracy and code maintenance. And boy strands really
delivered. We eliminated thousands of lines of code
across our agent systems while improving agent accuracy and
code maintenance. Realizing its potential. Be open source
strands so we could empower every developer to build their
own agents. And since launching in preview in May, we have
worked tirelessly with the community to add new future
features and capabilities. We have hundreds of community
contributions to help add features such as new model
providers, A2A support multi-agent hooks so you can
build more robust and extensible agents. And this
week, today we are adding two new exciting capabilities. The
first is support for Typescript, extending strands to one of the
world's most popular programing language. And the second is
support for edge devices. You should check out the Cool
Robotics demo where they are unlocking new agent
capabilities and automotive, gaming and robotics, enabling
autonomous AI agents to run at the edge. Developers across
every industry now are loving the simplicity and
extensibility of Strands Agent, so it's no surprise that in
just a period of very few months, strands has been
downloaded more than 5 million times. And today, we live in a
world where almost every developer is starting to
experiment and build AI agents on their laptops. But all so
much activity going on and so many proof of concepts are
happening now. Leaders are asking why, when they can see
all these amazing agents running in production. The
problem is that most experiments and proof of
concepts are not designed to be production ready. We need to
close this gap and break out of this proof of concept jail. The
first thing you need to get to production faster is that you
want the ability to rapidly deploy agents at scale. This
means having the infrastructure that can rapidly go from zero
to thousands of concurrent sessions. And it's the ability
to support all these long running agents with the right
session isolation that can stop sensitive data from being
shared with other agents. Next, your agents must navigate
massive amount of data and edge cases to get to production.
Your agents need sophisticated memory systems that can manage
context within conversation and interactions, and remember user
preferences across sessions. Then comes the challenge of
identity and access management. Without proper security
controls, agents can inadvertently access or expose
sensitive data that they shouldn't in production. You
need rock solid identity and access management to
authenticate users and authorize which tools agents
can access on their behalf, and manage these credentials across
AWS and third party services. And then, of course, as you
move to production, your agent is not going to live in
isolation. It will be part of a wider system, one that can't
fall apart if an integration breaks. So you need seamless
tool connectivity that enable agents to securely integrate
with APIs, databases and services that your application
needs. And finally, you need the ability to observe and
quickly debug issues arise because you simply can't fix
what you can't see. POCs are never designed with these
requirements in mind, and most off the shelf solutions are not
equipped to handle all these changes effectively. They are
rigid and they lack modularity, so you end up building custom
logic that taping all these solutions together, adding
unnecessary complexity that turns your really cool
prototype into a maintenance nightmare that slows down the
innovation. That's why we built Amazon Bedrock AgentCore. It's
the most advanced agent platform to build, deploy, and
operate agents securely at scale. It's like having a
toolbox, but every tool is built for the problems that you
will deal with while building and operating agents. And
people love it because it works with any agent framework and
any model, giving you the freedom to use the tools that
works best for your use case. And it's modular so that you
can mix and match using just the pieces you need for your
solution. And AgentCore does the heavy lifting so you can
focus on what matters most. Creating these breakthrough
experiences that solve real world business problem. Now let
me show you the difference this makes in practice. Take the
example of identity and access management. One of the
notorious time sinks that can derail any project with
AgentCore identity. You get seamless identity access
management across AWS apps and third party apps like Slack and
Zoom, all in just a few lines of code. Now imagine building
the same capability from scratch. Picture weeks of
authentication flow, security protocols, API integration,
endless edge cases. Which one would you rather write and
maintain? The ease of agent building that comes from using
AgentCore and strands is already helping customers
transform their business. Like Cox Automotive, they have
reinvented how they build and deploy agents across their
entire organization. Now let's see their story.
>> If you think about running a dealership or an auto
manufacturer, those have back office processes. Oftentimes
those are manual. They're cumbersome and Cox Automotive.
We are in hyperdrive, moving aggressively towards disruptive
positive value to change the game, change how you shop for a
car. Change how you sell a car. Change how you service a car,
and helping our customers level up their own operations in ways
they never thought possible. We also took an internal use case
with an energetic solution that we call Fleet Mate. So
something that actually took two days per estimator, we got
that down to less than 30 minutes per vehicle. AWS really
shows up as a true partner. AgentCore has allowed us to be
able to move fast, building agents, allowing agents to work
with other agents. They are allowing us to be inside the
product roadmap and help shape what we need in order to
innovate at the speed that our customers are expecting us to.
Bringing agents to life allowed us to work across our different
areas of business, and find opportunities where we could
bring Agentic thinking into a workflow and drive value. One
of the most exciting things about our story is seeing an
engineer using tools like AgentCore Strands and Bedrock
and building Agentic solutions. Their mind gets blown. They can
go from not knowing the tool, not knowing how to use it, and
producing something in days, sometimes hours, things they
never thought were possible. And that is super exciting to
see. >> Wow, it's exciting to see
how Cox transformation is opening a world of
possibilities. It's stories like these that fuel our
innovation engine. And just yesterday, Matt unveiled two
new capabilities that came directly from you in terms of
feedback AgentCore Policy that provides control over agent
interactions and behavior while giving agents the freedom to
reason and take the best action to fulfill a request so that
you can build trusted agent capabilities and AgentCore
rivals, which enables evaluating and testing agents
in thousands of simulated scenarios before they meet your
customers. So, no longer do you have to cross your fingers and
hope for the best when you launch an agent. But today, I
want to explore something that gets to the heart of what makes
agents truly intelligent memory. Think about the experience at
your favorite local restaurant. What made it exceptional? It's
because they remembered you. They know your name. They know
your seating preferences, and they know your favorite meal.
In the ancient world, we have short term memory handling, the
immediate conversational flow and long term memory, capturing
the insights across sessions. But something was missing. The
when and the why behind user behavior. For example, picture
this you're rushing to catch a flight for work. As a solo
traveler. I travel carry on only, and I like to be the last
one on the plane. That means my agent travel agent books my
Writer ROI 45 minutes before departure with all my TSA pre
and clear and whatever else will come, I will do it with
perfect timing. But then three months. But this time I'm
wrangling a four year old and a ten year old, plus enough
luggage with my wife for a small army. My agents needs to
remember the chaotic family trip from last summer. It needs
to recognize the pattern and automatically book my ride to
arrive at the airport at least two hours early. Because
traveling with kids changes everything. So what you need is
not just the memory of the past, but also the context of the
current interaction. That's why we launched Episodic Memory, a
new functionality with AgentCore long term memory, so
that agents can remember and learn from the past experiences.
This new feature gives the ability to build agents that
truly understand user behavior, and they adapt automatically by
recognizing patterns across similar situations. And they
proactively offer solutions that work. It enables agents to
store and recall specific experiences or interactions as
discrete episodes, similar to how we remember particular
events in our lives. The more your agents experience, the
smarter they become. Now, let's look at how customers are
unlocking the freedom to innovate with AgentCore Heroku,
who helps companies build and deploy apps in The Cloud with
their AI as a platform service. They use AgentCore to build
Heroku, enabling anybody to build and run entire web apps
using natural language with AgentCore runtime. They were
able to speed up their development velocity and went
from proof of concept to launch in just five weeks, and the PGA
TOUR, a pioneer in innovation, leader in sports. They have
built a multi-agent content generation system to create
articles for their digital platform. That new solution
built on AgentCore enables the PGA TOUR to provide
comprehensive coverage for every player in the field by
increasing content writing speed by 1,000%, while also
achieving a 95% reduction in cost. And finally, Caylent, a
next gen Cloud services company that helps companies build and
scale their Cloud journey by rebuilding on AgentCore,
Caylent deleted thousands of lines of custom orchestration,
code, routing and memory and replaced it with a managed
serverless agent platform that just works. Now they are
shipping new integrations in days instead of weeks, and they
cut their ops overhead by 70% and unlock new capabilities
like HR workflows and Multi-turn agent reasoning that
simply weren't possible on their custom built system. Next,
I would like to invite William Brennan VP of Tech
Transformation at Blue Origin to explain how they are
leveraging AWS for their AI powered space exploration.
>> Good morning everybody. At Blue Origin. We're building the
road to space for the benefit of Earth. In pop culture, space
explorers have always had AI partners. Just think of some of
those famous explorer duos from your childhood. The farm boy
and his droids, the starship captain and his voice activated
ship's computer. And yes, even the mission commander whose AI
went rogue. We've long dreamed of a world where artificial
intelligence and space exploration go together. From
rockets to AI at Blue Origin. We're not dreaming of the
future anymore. We're building it. This isn't new for us. Our
New Shepard rocket became the first spaceship to autonomously
launch and land vertically, making automation and
reusability safe and reliable partners. Since then, 86 humans
have trusted their lives to New Shepard's automation across 15
flights, experiencing a view of Earth they've always dreamed of,
the road to space grew visibly and powerfully, and last month,
successful launch and landing of our New Glenn orbital rocket.
This next frontier an increased launch cadence, lunar landers a
permanent presence on the moon is building on that automation
and extending it using the latest innovations in AI. Our
mission to reduce the cost of access to space is accelerated
through agentic AI that learns, adapts, makes decisions that
reasons, plans, and explains its thinking. That's why,
frankly, I think I literally have the coolest job in the
world. We're going back to the moon this time to stay in
agentic AI is one of our new teammates, helping us get there
faster and cheaper. Across blue. The road to space is being
built by incredibly talented and creative people engineering,
manufacturing, software supply chain. As a vertically
integrated company, we run the full life cycle of a space
mission from concept to operations. Building and
launching rockets requires tremendous specialization from
dozens of these disciplines, and that practical knowledge
isn't found in general Large Language Models. It's buried in
our systems, databases, and tribal knowledge. Agentic AI is
the ability to create teams of domain expert agents with
access to specific knowledge and custom tools has completely
transformed the application of AI at blue, taking a
democratized approach to AI, everyone at blue is expected to
build and collaborate with AI agents to do their work better
and faster. By equipping our teams with knowledgeable and
capable agents, we were able to dramatically accelerate the
product life cycle, increase production rate, and most
importantly, reduce the cost of access to space. The starting
point for our builders and creators is our internal
Generative AI platform we call BlueGPT. It's a there we go
blue team. It's a secure LLM and MCP gateway agent,
Marketplace and multi-agent orchestration system built on
core AWS primitives. Bedrock Strands Agents SDK EKS
OpenSearch RDS Lambda. Giving our agents access to all 
leading models, custom Knowledge Bases, and dozens of
tools. Agentic AI has exploded at blue through organic
disruptive adoption. Over 2700 agents have been created and
are in use in production in the agent Marketplace, driving over
3.5 million interactions across 70% of our employees in the
last month. There are so many examples I could give on how
Team Blue is using agents to work better and faster. 95% of
our software engineers are using agents to write code. New
Glenn is using agents to accelerate launch approvals,
supply chain and manufacturing use agents for design changes
and work orders. But what I really want to talk about are
Tearex's. No, not space dinosaurs, but rather an
innovative project at Blue Origin. Tearex stands for
Thermal Energy Advanced Regolith Extraction, and it's a
brand new capability being developed by our In Space
Exploration Systems group to solve one of the toughest
challenges surviving the lunar night. Equivalent to 14 Earth
days of freezing darkness. I have I have part of it right
here with me. And this thing is amazing. As you can see in the
video, the battery, the Tearex takes lunar regolith, or moon
dust from the surface of the moon, circulates it through
this chamber and then extracting the heat through a
lightweight heat exchanger, and then runs it through this
cylinder to save the rest of the the machine from the
sensitive and abrasive rocks. Designed to run for years, this
heat cycle is then reversed during the lunar day to
recharge regolith for use during the next night, turning
moon dust into a battery. While Tearex is amazing, what's even
more amazing is the team of AI agents that helped build it. A
BlueGPT agent helped us with the detailed requirements.
Another agent helped us create the system architecture. One of
my favorite agents, though, is our simulation and analysis
agent, where we're able to automate the iterative design
loops, rapidly improving the product with custom Knowledge
Bases and connected to AI native tools like Ntop for mass
and performance optimization and Asteroid Digital for
deterministic validation and artifact management. The agents
run complex physics simulations, iterate on the design based on
the results, and execute until the requirements are met. All
running on GPU accelerated EC2. Tearex is a great example of
what we see as the future of engineering teams at blue,
small teams of experts working with large teams of AI agents
to deliver the works of Tens and at orders of magnitude
faster than before. The benefits are immense. Using
 agents, our engineers were able to deliver a
performant product over 75% faster than traditional
approaches, with mass 40% improved over the original
designs. Now I get it. Most of you aren't building rockets or
lunar infrastructure, but you do deal with specialized
knowledge and custom tools, and I think could benefit from a
few of our learnings with agents. First, I'd consider you
to think of adoption of AI as everyone's job, not just the
technology teams. Democratize agent creation and use a simple,
user friendly interface led to 70% company adoption. Second, I
encourage you to let the process for innovation be messy,
but discovery easy. A public Marketplace or agent app store
has really helped us here, providing easy to use eval
tools to allow your teams to test and discover their agents.
Third, let AWS handle the LLM agent primitives and scaling,
and focus on building with those tools to solve problems
for yourselves and for your customers. With agentic AI, we
believe that the future is now. It's just not evenly
distributed. We aren't yet developing all of our products
using AI, but we will be. With millions of people living and
working in space. We believe in a world where we can agentic AI
design an entire rocket, where we can launch 100 rockets with
one person, rather than one rocket with 100 people. Our
work with AWS isn't slowing down. We are building an
enterprise knowledge graph on AgentCore, transforming the AI
accessibility of all of our data. And we're excited to test
some of our own custom built models with our autonomous
lunar rover on the moon trained on AWS GPUs. Our talented team
of Blue Origin employees and AI agents will continue to be the
fuel for this rapid innovation. As we build the road to space
for the benefit of Earth. Thank you very much.
>> Thank you William. It's fascinating to see how
customers are leveraging agents even in space exploration. Now,
as agents become easier to build, the next big question
emerges how do we make them more efficient? Today's off the
shelf models have broad intelligence. They can handle
complex tool use, multi-step reasoning, and unexpected
situation, but they aren't always the most efficient. And
this efficiency is not just about cost, it's about latency.
How quickly can your agent respond? It's about scale. Can
it handle peak demand? It's about agility. Can you iterate
and improve quickly? And these are the practical realities of
deploying AI at scale. So how do we address these challenges?
The majority of the agents depending they spend most of
their time on routine operations. These are like
writing code, analyzing search results, creating content, and
executing predefined workflows. If we know these tasks upfront,
we can customize models specifically for them. Model
customization enables us to build agents that are efficient
to deploy at scale while achieving the right performance.
So the question isn't whether you should customize your
models, but how quickly can you get started? So now let's
explore the techniques available and how we can help
you turn this vision into reality. The first technique we
will look at is supervised fine tuning. Think of it as teaching
your AI agent to be a specialist instead of a
generalist, like turning your family doctor into a
cardiologist who is laser focused on exactly what you
need. This is where most teams start, and for really good
reason. It's practical. You don't need massive compute
budgets or a Ph.D. in Machine Learning to get started. You
start with a pre-trained model and train it on curated agent
specific data sets containing tool use, pattern, multi-step
reasoning traces, and successful task completion.
This creates permanent behavior changes and they don't require
lengthy prompts and can dramatically improve
performance on specific tasks by the base model struggles.
But here is the catch your model can get so focused on
specific tasks due to overtraining that it might lose
those amazing capabilities that made you choose the big model
in the first place. So the key to success here is quality over
quantity. A data set with 10,000 carefully curated agent
interactions will outperform millions of generic examples.
Think of it this way would you rather learn surgery from
10,000 recordings of world class surgeons performing your
exact procedure, or from millions of random YouTube
videos? The choice is obvious. The next technique is model
distillation. You should use model distillation when you
have deployment constraints like memory limitation, and you
need to deploy a smaller, faster model. Think of this
method as something like creating a brilliant apprentice
who learns from a master craftsman, but they can work
twice as fast with half the tools. So you take a large,
powerful teacher model and train a much smaller student
model to mimic not just the answer, but also how they think
through and reason. The student learns entire confidence levels,
decision patterns, and even recognition strategies. Here we
often see up to ten x speedup with models retraining 95 to
98% of the teacher's performance. And that's the
difference between a three second latency for customer
calls versus getting an almost instant response. The trade off.
You need that high performing teacher model, and distillation
requires substantial compute resources. But once you get
that efficient digital model, it pays dividends with every
deployment, and then you have reinforcement learning, where
models learn from the outcomes of their actions by getting
rewards for good outcomes and penalties for bad ones. And
there are two flavors of RL RL from human feedback and RL from
AI feedback. But human feedback. Here you show people multiple
AI responses to the same customer inquiry and ask them
to rank from best to worst. Now we use these rankings to train
a reward model that learns to think like these human
evaluators becoming your automated quality scorer. Here
is how it works. Your agent executes an action, and then
the reward model gives it a gold star. SCAs to bad try
again. The agent learns through trial and error, just like we
do. In many cases. This approach shines when outcomes
are impossible to define programmatically. How do you
code up a sound, empathetic but professional? You simply can't,
but humans know it when they see it, and now your model can
learn to recognize it too. In reinforcement learning with AI
feedback instead of human rankings, we use a powerful LLM
to evaluate and rank these responses. This is much faster,
much cheaper, and more consistent than humans. It's
perfect for outcomes with clear right or wrong answers, and
lets us scale to millions of examples. It also rewards good
processes, not just the answers. The model learns to think
strategically step by step, which is exactly what agents
need. Think about it when an agent is troubleshooting a
complex issue, you don't just want the final answer, you want
the logical diagnostic steps, the right clarifying questions,
and methodical problem solving. That is strategic thinking. And
that's what RL teaches. Well, RL is incredibly powerful.
Implementation of RL techniques can be a challenge. You need
Ph.D. level expertise and reward modeling, policy
optimization and integrating feedback. Then there is setting
up complex distributed infrastructure and spending
months in development with no guarantee it is ever going to
work. And the cost? We will be talking 6 to 12 month projects
running on high end compute resources, and most companies
simply can't afford it. So you have to compromise. You either
settle for the generic models with poor performance, or you
spend millions customizing models with reinforcement
learning. And then when your workload patterns change, you
start this entire expensive process all over again. So we
thought, what if we could take away all the complexity and
cost while still giving you access to these advanced
training techniques? That's why today we are making
reinforcement fine tuning available in Amazon Bedrock.
Reinforcement fine tuning RFT helps customers improve model
accuracy without needing deep Machine Learning expertise or
large sums of labeled data. Bedrock automates the entire
RFT workflow by making this advanced model customization
technique accessible to every day. Developers. Here you can
start today with Amazon Nova, and we will be starting support
for open model weights really soon. Here it works very simple.
You start by selecting the base model you want to modify,
pointed at your Bedrock logs and select a reward function,
the easiest of which is an LLM based judge. And that's it.
Behind the scenes, Bedrock handles all the complexity of
reinforcement learning implementation, striking the
right balance of customization and ease of use for most use
cases, and it provides delivering 66% accuracy gains
on average over the base models. That is how powerful these
techniques are now, while Bedrock offers an easy and
powerful way to fine tune models, there are many more
customers that want the full control over their
customization techniques and want to leverage that data.
Think about it a legal firms competitive advantage is its
accumulated knowledge base and reasoning patterns. Here,
training a model from scratch ensures this proprietary
expertise remains confidential while also giving them a
competitive advantage. A healthcare provider needs
models trained on their specific patient outcomes, not
just generic medical data. That's exactly why we built
SageMaker. AI. SageMaker gives you everything you need to
build, train, and deploy AI models that are uniquely yours
at whatever scale it supports knowledge distillation,
supervised fine tuning, and direct preference optimization.
You can do full weight training or parameter parameter
efficient fine tuning, whatever your use case demands. Betz,
SageMaker AI, IDE, and MLops capabilities. You can go from
idea to production in weeks, not months. Now, customers like
Dhan India, who built a large language model that deeply
understands the complexities of Indian financial market. They
started with Mistral-7B as the base model. They built IAM, a
specialized Stephen Bowie parameter model, using a
combination of training methods like continual pre-training,
fine tuning and knowledge distillation. Their solution
used Amazon SageMaker for the model building and training,
and use Bedrock for the teacher model. Support. The new
customized model runs on a single GPU Infra, and
outperforms state of the art models 88% of the time, while
providing better performance at a fraction of the operational
cost. However, the very flexibility that SageMaker AI
makes it so capable also means that you must navigate numerous
decisions and technical hurdles to achieve your goals. Think
about what you're actually signing up for when you want to
customize a model with your data. First, you are defining
the goals and picking evaluation criteria. Are you
optimizing for accuracy or latency or cost? Then you are
choosing fine tuning, RAG or maybe pre-training from scratch.
Then comes the fun part data prep. You are cleaning data
sets, checking for biases, making sure everything is
properly formatted, and anyone who has done this, it's never
as clean as you hope it will be. And then you are spinning up
infrastructure, configuring training jobs, watching these
loss curves, and tweaking all these hyperparameters. And when
something breaks at 2 a.m. guess who is getting that alert?
Finally, after weeks of work, you have a model. But wait, now
you need to evaluate it and optimize it for production and
making sure it meets your company's AI governance
standards. Then the result? What should be a really
exciting AI project turns into months of laborious,
challenging work before you see any business value. What if we
could compress that journey from months down to just days?
That's why today I'm thrilled to announce the release of new
serverless model customization capabilities in SageMaker AI.
With this release, you can customize popular models such
as Amazon Nova, Qwen, Lama Deep Set and deploy them directly on
Bedrock or SageMaker in just a few steps. Better add this
concept to experiences and you can choose the right approach
based on your comfort level. A self guided approach for those
who like to be in the driver's seat, and an agent driven
experience that uses an AI expert for folks who like to
turn on autopilot in their cars. Each of these parts provide you
access to new RL techniques like RL, AI, FM, RLVR, and DPO,
and are based on the best model for the job either your choice
or the agent's. Now the agentic AI experience launching in
preview removes the heavy lifting so that you can focus
on the outcome. You use natural language to explain your use
case, and the AI agent guides you through the full
customization workflow. It first analyzes your scenario to
recommend the right fine tuning technique. Then, if needed, it
will generate the synthetic data set for your model
customization. And then it sets up the entire serverless Infra
to train the model without any manual intervention. And then
finally, it evaluates the trained model against the base
model to determine if the customization was successful.
So now what used to take, like many ML engineers and months of
trial and error, now happens in just days, all guided by an
agent that knows the best practices and does the heavy
lifting for you. Now, while these model customization
techniques enables you to build agents that are efficient to
deploy at scale, working closely with customers helped
us identify another key gap. Traditional techniques can't
deliver the domain specific intelligence, accuracy and
price performance that competitive applications need,
especially when you need models that deeply understand your
industry data and workflows. For example, a drug discovery
company needs an AI model that deeply understands molecular
structures, protein interactions, and clinical data
specific to their therapeutic area. Generic models. They lack
their specialized knowledge and fine tuning simply can't embed
the foundational understanding of their proprietary research.
Now, many of you might ask saying like Swami, why can't
you use any of the customization techniques we
talked about earlier? The simple answer is that these
techniques add knowledge on top of a model that wasn't designed
for that domain. It's the difference between teaching a
general translator, some medical terms versus training
of medical translator. From the beginning. This means today, if
you want to truly customize foundational models, you end up
starting from scratch. You need millions of dollars in compute,
months of training time, and specialized ML experts, and you
have to manage massive Infra. And you are starting from zero
with no proven baseline or guarantee of success. This is
why custom foundational models have been the exclusive domain
of well-funded organizations and AI startups. But now with
Nova Forge, which Matt launched yesterday, you have a first of
its kind program that offers you the easiest and most cost
effective way to build your own frontier model. With Amazon
Nova, you get access to intermediate checkpoints, and
you can mix in your proprietary data with Amazon curated data
during training cycle without having to worry about the
compute, data and time needed for the full model training.
The result a model with frontier intelligence tailored
to your industry and use case while retaining Noa's
foundational knowledge, safety and reliability, all without
the cost and effort of the full training lifecycle. Now,
another area we are focused on a lot is to help you build and
run cost effective and performant agencies
infrastructure. This is where SageMaker HyperPod comes in.
HyperPod has transformed the traditional, complex and time
consuming process of managing Infra for training and
deploying models into a fully managed service. It removes the
undifferentiated heavy lifting and scales across thousands of
AI accelerators with automatic workload prioritization, and
reduces model development costs by up to 40%. And most
critically, it gives you full visibility and control over how
different tasks are prioritized and how compute resources are
allocated to each task so that you can maximize these
expensive resources. However, when you're building or
training a model, it's not uncommon to have failures. And
as your models become bigger and they require even larger
training clusters, the failures become even more frequent and
they take longer to resolve. So to deal with these unexpected
failures, HyperPod automatically saves these model
snapshots or checkpoints, and when a failure occurs, they
recover from a previously saved checkpoint. But this
traditional checkpoint based recovery is not always easy.
You have to pass the entire cluster and then diagnose the
issue, and then restore from the saved checkpoints, all the
while leaving expensive AI resources idle for hours,
keeping your CFO up at night. So we thought, what if we could
find a way to improve training resiliency, and reduce drown
time? That's why today we are announcing Checkpointless
training on SageMaker HyperPod. With this new feature, we
significantly reduce the recovery overhead since the
process no longer requires rolling back a partial training,
no more than a partial training step. This is a paradigm shift
in model training that automatically recovers from
Infra faults in minutes with zero manual intervention, even
with clusters that span hundreds of thousands of AI
accelerators. The way we achieve this is by continuously
preserving the model state across the distributed cluster.
So when something goes wrong, there is no need to panic and
rollback to some old checkpoint. Instead, it smoothly swaps out
the faulty hardware and uses peer to peer transfer to grab
the exact model state from healthy accelerators nearby. So
now you get faster recovery and significant cost savings in
your model training. And now with all of these launches we
have announced today, we are excited to give you the tools
you need to build highly efficient models. Now let's
hear from Guillermo Roche, CEO and founder of Vercel, who has
put these principles into practice leveraging AWS to
build efficient and scalable tools that deliver real value
to millions of developers today. >> Hi everyone! It's so great
to be here with you all in The Cloud! When I was growing up in
Argentina, I deconstruct sites on our family computer and
bring my own ideas to life by typing a file to a server and
sharing a link with my friends. It was the best feeling I could
just build and I never stopped building. I built with every
tool and every framework, which eventually led me to create my
own framework as one does Next.js. With Next.js, we made
building high quality applications accessible to
anyone from the biggest enterprises on the planet to
solo developers starting out with just an idea. The problem
was that even with Next.js, I built an app in a couple hours
and then spent weeks setting up infrastructure to get it out
into the world, and I didn't just want easy, I wanted peak
performance at scale and I wanted it now. That idea led me
to build Vercel. Ten years later, Vercel now empowers more
than 11 million customers to build, scale and secure global
web applications without managing infrastructure. With
more than 1 trillion requests served every month, now AI is
changing. What and how we build interfaces are becoming
conversations and workflows are becoming autonomous. We're
witnessing the shift from web pages to AI agents. This is
perhaps the most important transformation we'll see in our
careers as developers and technologists. And this is how
the Vercel AI Cloud was born to redefine fully managed
infrastructure for the AI era. We call this self-driving
infrastructure. You write an app, you push your code, and
automatically the best possible infrastructure is provisioned,
orchestrated and optimized for you. Vercel operates as an
always on system that observes every input from the code you
write, the code you ship to the traffic your users generate,
and turns that data into real time insights and optimizations.
You get to focus on your business, your products, your
customers. And we know this works because we prove it at
scale every day with our customers, but also because we
build Vercel. Guess what? With Vercel on Vercel and Vercel is
powered by AWS, which means with just one git push, you
reap the benefits of fully self-driving AWS infrastructure.
So let's look at this in action first v0. V0 is the realization
of that original dream. The thing I wished existed when I
was hacking together my websites. In Argentina. You
speak your mind and in seconds you have a live working
application. Since its launch, v0 has been serving millions of
requests per day. And that was possible because under the hood
v0 runs on Vercel, which runs on AWS with model inference
provided by Amazon Bedrock. When we were building v0, our
engineers could just write code, deploy it over cell, and scale
without configuring AWS primitives. And so this freed
up the team's time, the v0 team's time to focus on the
novel AI challenges with new models and new ideas and new
techniques coming up every week. So to keep up and move at the
speed of AI, we built the AI SDK. So think of it as Next.js
with Next.js did for building pages. AI SDK does for building
agents. So first, of course we build it for ourselves, and
then we made it available for everyone. It makes AI simple,
model agnostic and scalable. Today, AI SDK is downloaded
about 5 million times per week, and with AI SDK, anyone can
build with AI. Whether it's your first AI app or your at
scale like Thomson Reuters, there are co-counsel AI
assistant serves attorneys, accountants, audit teams. They
used AI, SDK and Vercel, and a team of just three developers
built their tax advisory agent in just two months, and it's
already in use by 1300 accounting firms. Now they're
migrating their entire code base to AI SDK, deprecating
thousands of lines of code across ten providers and
consolidating everything into one composable and scalable
system. Three developers, two months, thousands of firms
could be any of you. And so as we move from pages to agents
and pixels to tokens, it's helpful to reuse lessons from
the past. The web scaled thanks to CDNs, which increased speed
and reliability. And that's why we built the AI Gateway. Think
of it as a CDN of tokens. It routes inference automatically.
It adds failover in critical controls. AI Gateway is built
on the same global network that solves all of our customers
across 20 regions, close to your users and your AWS data.
This network runs on battle tested AWS infrastructure,
Global Xcelerator shield, S3, EC2, and more. But here's the
next challenge AI is changing the profile of our workloads.
While traditional apps need to load in milliseconds, agents
can think over minutes or even hours and soon days. So
serverless has been great for scaling on demand, right? So
which we also need for agents. But it hasn't been so great for
what we call idle time. That's what we built. Fluid Compute.
It's compute optimized for AI powered by AWS fluid adapts to
every workload, whether it's pages or agents. Your functions
scale on demand, but crucially, you pay only for what you
actually use. Active CPU time. This is fully self-driving
compute infrastructure. Our AI Cloud goes beyond Vercel's own
services, providing seamless access to even more AWS
solutions like AgentCore, Kiro, and RDS. How we build the web
is changing. You'll be working with agents like v0 and Kiro.
These agents will be writing code using frameworks like
Next.js and AI SDK, and they'll deploy to self-driving
infrastructure. This is the future of the web, powered by
Vercel backed by AWS. Thank you. >> Thanks, Gemma. Vercel is a
great example of how quickly agents can help a business grow
and thrive. Not only are they helping their end users build
and run intelligent agents, but they are also helping their
builders at Vercel enable entirely new developer
ecosystem. Now, as we hand over more tasks to AI agents and ask
them to act autonomously on our behalf, we need to be able to
trust that they will perform things as they expected. While
most of us have spent our entire careers building an
accurate and reliable systems, Agents introduces a whole new
set of challenges that require radical new approaches. At AWS,
one of the first agents we built a couple of years ago was
an early prototype for what is now Kiro CLI. We found that
while it worked great, but in some cases LLMs would
hallucinate API calls. And of course, we can't just always
say, hey, it's okay if it hallucinates. Then we got
together and brought a bunch of our scientists. Machine
Learning scientists. And also we reached out to our automated
reasoning team to see if we could solve this problem with
what is now. We call it as Neurosymbolic AI. In effect, we
are creating the yang to the LLM in so to speak. So we have
a special treat for you today. We brought Byron Cook AWS,
distinguished scientist and the foremost authority in automated
reasoning to explain how we are leveraging automated reasoning
across AWS to help our agents be more trustworthy.
>> NKI Swami. All right, so let's start with a question.
How much do you trust agents today? For example, do you
trust that they'll send money to the right place? Or do you
trust that they'll follow local laws when operating on your
behalf? Giving an agent access to your credit card is like
giving a teenager access to your credit card to go use on
the internet. Like, sure, they'll probably get a lot done
on your behalf, but you might end up owning like a pony or a
warehouse full of candy. So the challenge is that agents are
based on Large Language Models and Large Language Models.
Hallucinate, right? They make mistakes in the face of complex
rules or logic. Their their their reasoning contains
logical errors. So imagine an agent is interpreting a ticket
returns policy and it's making mistakes. Now we're giving away
money where we shouldn't. That's not the sort of agent
we're going to keep in production for very long. So to
make matters worse, LLMs can be tricked, right? Bad actors can
craft inputs to trick LLMs. It's actually not hard to do
today. So this is because most of the genetic systems are
using statistical methods like LLM as a judge to enforce their
guidelines. That's never going to work in situations where
since sensitive matters like trust or our money or human
lives are at stake. So when we don't trust agents, we tend to
overcompensate, right? We we introduce a additional human
oversight on every step. Right? We we we hard code the steps
that they'll take. So both of these techniques reduce the
creativity and the the autonomy that agents have, which is
precisely the reason we're excited about agents in the
first place. So what we want is an easy way to specify our
constraints on agents at the outset, right? Giving agents as
much freedom as possible while defining the envelope in which
they can operate safely. We then want assurance that
they'll follow those constraints even when the
constraints are subtle or complex. And so the good news
is that we have much of the technology we need for this
purpose. And that's why Swami has asked me to come up on
stage today to tell you about my scientific discipline of
automated reasoning and how we're applying it to agentic AI.
So automated reasoning is the search for and also the very
detailed checking of proofs in mathematical logic. It's the
same type of reasoning performed by people like Euclid
during the time of the ancient Greeks. So in our context, we
can reason about all possible executions of a computer
program in the same way that Euclid reasoned about all
possible right angle triangles when proving the Pythagorean
theorem. So we've we've come full circle in a sense, right.
We're taking ideas from 2000 years ago and applying them to
one of today's most vexing, vexing challenges in the tech
space. So consider a system where we we want to know that
the data is encrypted before it's stored, so we can encode
that property into a logical formula, namely like a temporal
logic, and then use techniques from mathematical logic to
prove that that that that property is in fact always true.
Furthermore, we're using symbolic techniques, symbolic
logic, and that allows us to to know that we're reasoning about
all possible inputs to the system, and also all possible
configurations that the system might reach during its
execution. So within AWS, we've actually been using this
technique for over a decade. We've been reasoning about our
internal AWS systems. So for example, our virtualization
stack, our cryptography stack, our identity, our networking.
And then externally customers have direct access to tools
from this from this discipline. So IAM Access Analyzer VPC,
Reachability Analyzer and S3 block public access are all
based on this technology. And then outside of AWS, we see
people using the space in mission critical systems. So
mission critical situations. So like aerospace and railway
switching and industrial control systems, basically any
place where failure is unacceptable. And now we're
bringing that same technology to the world of agentic AI. So
this fusion SaaS Swami mentioned this fusion of formal
reasoning and Large Language Models is typically called
Neurosymbolic AI, where the neuron represents the
statistical methods we're using and the symbolic represents the
symbolic formulae or or symbolic logic we're using
under the hood. So how do we use automated reasoning with
LLMs. So one method is to use automated reasoning to verify
the output. So the output might be programs that might be
instructions for agents or it might be Q&A pairs. If the
automated reasoning tool signs off on the answer from the
large language model, we're good to go, right? But if we
find a problem, we can then go push back on the language model
and and it can try again. So this creates a this creates a
feedback cycle that gives us a proof. Another method is to
flip the equation around. So to to train the language model
over the output of automated reasoning. So for example, many
model providers today use the lean theorem prover to create
unbounded amounts of well-reasoned and sound
training data. So DXC is an example of a model provider
that trains using the lean theorem prover. And then the
third method is to embed an automated reasoning verifier
deep inside an LLM inference infrastructure. So an example
of this is called constraint So imagine an LLM that's responding to a question like
what's the capital of France. And it's answering with
a token like B. Right. So if we sidecar the formal reasoning
representation next to the language model, we don't need
to allow the language model to completely answer. What we can
do instead is ask the representation during the
inference state to check the answers with regards to with
regards to the formal reasoning model, and then we can nudge
the language model instead of answering with the letter B to
instead to to answer with the letter P for Paris. So in some
sense we're shifting the the reasoning left into the
inference infrastructure. So this summer we launched Kiro,
Amazon's new Agentic IDE. So with Kiro, developers can use
natural language features to define entire applications or
features and applications. So what makes Kiro different is
it's specification driven approach to software
development. So specifications hold a very special place in my
heart. They're the really the foundation in automated
reasoning specifications are how we define the behavioral
properties that we want to prove or disprove of our
systems. So inspired by the success of automated reasoning
and specification in AWS, the Kiro team has brought the idea
of specification into the into Kiro itself. So imagine you're
building a calculator app and that needs to handle many
different scenarios as well as potential error states. So
during the design phase, Kiro might analyze the application
and identify a set of acceptance criteria. So for
example, it might state when an error occurs, the app will
eventually display a clear error message in the display
area. Kiro can then convert this criteria into a
specification. And then there's a lot of things we can do with
that, right? So we can use the specification to guide the
language model as it attempts to find the code to implement
the application. So today in Kiro, you can also use that
specification to generate tests that then that that uses the
structure of the specification to drive the to the application
into interesting spaces, to help us raise assurance that
the program implements the specification correctly, but
also to help us pressure test the environment that it's going
to operate in, our assumptions about that environment. And
it's not escaped our notice that we can also use automated
reasoning to prove the correctness of the program
against the specification. So another challenge in the in the
genetic development space is to keep up with the APIs that the
code that we're generating is programing against. So take AWS
for example. AWS is evolving faster than the model providers
can update their models. And so one way we can solve this is to
develop and maintain a formal model of the APIs, and then
reason about the programs that are being synthesized by the
tool and how they respect the APIs. So we can keep up to date.
So finally yesterday Matt mentioned policy and AgentCore.
So with policy you get real time deterministic and
auditable controls over how your agents interact with
outside tools and data. You can describe in natural language
the actions you want to allow. And then we translate them into
a formal representation called Cedar. So Cedar is something we
actually launched two years ago. It's a open source
authorization language. Its semantics are formalized in the
lean theorem prover. And then we've recently added an
automated reasoning based analysis to allow you to reason
about the semantics of your policies. So let's look at an
example. Imagine we're building an agent to help us
troubleshoot issues in production. So what we'd like
is for the agent to access production data and run
diagnostics to help us figure out how to resolve issues. But
what we don't want is for the agent to go make changes in
production until we've agreed on what those changes are, and
so we can use natural language to write the following policy.
Block any agent from performing update operations on resources
in the AWS production account. So under the hood, this type of
constraint can then be automatically converted into a
Cedar policy that we can run through. For example, automated
reasoning to to verify that it aligns with our various
requirements. So those might come from sovereignty, they
might come from privacy availability, durability,
security and so on. So this type of combination of sound
formal reasoning capabilities, together with the agentic AI,
represents a game changer for making trustworthy agents.
We're super excited about this work. We're super excited about
the projects that are underway, and they're going to help you
build a genetic systems that are not just powerful, but also
trustworthy and secure at any scale. Thank you very much.
>> Thanks, Byron. I hope my daughter does not learn how to
use these AI agents to order a pony. But anyway, while
automated reasoning helps us build agents that are accurate,
we also need them to be reliable for everyday use.
Reliability, if you look at it, is the level of certainty with
which a task gets completed across multiple agentic AI runs.
And when it comes to agents, businesses need high
reliability when it is automating their workflows.
Today, we see agents that get a task right once, but they
struggle when you ask them to do it again, let alone over and
over. When we think about automation back to the early
days of 2000, the challenge of automation was handled by
Robotic Process Automation, or RPA. They were designed to fill
the gap between legacy systems and modern business needs by
mimicking human workers. These products could log into
applications and handle data entry, but they were limited in
their flexibility and they would break when they
encountered UI variations or complex workflows. And then
came LLMs. They could handle UI variations and adapt to
complexity far better than RPA did. They could navigate
browsers, and they could reason through problems to
successfully automate workflows, even across diverse interfaces.
But the problem is, orchestrating. These models are
so complex, you need to build an error handling and
backtracing because unlike a traditional script where you
know exactly what failed and LLM might keep going on down a
failed path for several weeks before it recognized an error.
So for many businesses using these Large Language Models for
large scale computer use, automation is simply too
consuming and error prone to be practical. What a business
really needed to begin with was that automation that was simple
and reliable. So we asked ourselves, how can we make this
easier? The answer was not just to train a better model, we
needed a better model. Of course that. But that needs to
be part of an end to end automation service. Tightly
integrating Amazon Nova Bedrock AgentCore. So that's exactly
what we built. Today, I'm excited to announce the general
availability of Amazon Nova Act. Nova. RT is a new service to
build and manage fleets of agents for automating
production UI workflows with high reliability, ease of
implementation, and fastest time to value at any scale. It
achieves 90% reliability in the enterprise workflow settings
that it was trained to perform. So what makes Nova different?
It is because it is made up of tightly integrated components
that work together to deliver this. The model is optimized to
deliver best outcomes for workflow automation. Here we
started with Nova 2 Lite model and then post trained it to
target common enterprise workflows. So here the
orchestrator sends screenshots of your browser to the model,
and then it routes commands such as clicking and typing to
the actuator. It's what enables Act to use a browser the same
way a person would. And finally, the SDK is your entry point to
Nova act. It enables you to build browser automation agents
using simple natural language commands. And they make it easy
to break down highly complex workflows into straightforward
task. This tight vertical integration across the
orchestrator Model Actuators tools, along with the SDK,
enables act to better reliable than off the shelf models and
frameworks. Because today one of the problems is that many
models are trained separately from the components that plan
and execute these actions, and they can negatively impact
reliability. For example, imagine you're building an
agent to control a robot. Training a model separately
from the orchestrator and actuators is like growing a
robot's brain in a jar and then putting it into the robot after
the fact. Here we are, training the brain together with the
arms and the legs so that it comes out of the box knowing
how to walk. To make this work, it required us to rethink how
you train agents the entire stack that the agent is trained
on is consistent for both training and production,
enabling us to perform end to end post-training that accounts
for everything agents will interact with. But this alone
is not enough. How you train really matters. Historically,
agents were trained with something what we call as
imitation learning, where the agent learns by observing and
even mimicking expert behavior. This is where we started to.
But the downside of imitation learning is that the agent
never learns to understand the cause and the effect of its
actions. So that's why we trained Nova. And for that, we
turn to reinforcement learning. One of the customization
techniques I talked about earlier. And we focus training
on workflows that enterprises encounter frequently, such as
completing hardware requests, automating workflows, and
updating customer records in a CRM. But the basis of
reinforcement learning is allowing the agents to try
workflows in an environment that enables them to learn from
the outcomes of their actions. So to do that, we created
reinforcement learning gems where these models could train
and improve. Just like when you go to the gym to workout. The
RL gems be created. They replicate real enterprise
environments where agents can take actions and learn from
their outcomes without interfering with their
production environments. In an enterprise, anything you use
that has a browser or UI interface could be a gem. For
instance, your CRM, your HR system, or task trackers or
issue management system. In the gym, the agent is given a task
or a workflow to solve and through trial and error, learns
to solve it. So we built hundreds of gems and had agents
run thousands of workflows on each of them in parallel for
each successful task completion. The Nova act got a reward, and
for each failure it got a penalty. So over hundreds of
thousands of these interactions, these gems helped Nova learn
patterns so it could reliably solve real world enterprise use
cases. And all of this has enabled us to create a better
service and a more intelligent model in key benchmarks like
real bench and screen spot. We see Nova act as performing
really well as well, or better than some of the best models in
this space, and we are already seeing customers transform
their businesses and workflows with the high reliability of
Nova act. And if you're interested in seeing how it
performs in action, check out the Nova Act Playground or
install the Nova act IDE extension in Kiro, VS Code or
Clojure. Now, the future of agentic AI is in agents that
can do anything. It's agents we can rely on to do everything. I
truly believe AI agents mark one of the most transformative
steps of our time, and AWS is the best place to build and run
these agents. We offer you the best tools and SDK to quickly
and effortlessly go from idea to production with AgentCore
and strands. We provide the easiest path to customizing and
fine tuning models with Bedrock, SageMaker, and Nova Forge, so
you can maximize the efficiency of these agents. And we deeply
invest in innovative techniques like automated reasoning and
reinforcement learning, so that you can meet the high accuracy
and reliability needed for these modern workflows. And we
didn't just stop there. When all of these things come
together, the way we work is changing. We are moving from
automation of individual tasks to collaboration that
accelerates entire industries. Let's take a look at some
examples. Yesterday, Matt announced three powerful new
Frontier Agents. These agents are autonomous, massively
scalable, and they are persistent, able to work for
hours or days in pursuit of their goals without requiring
intervention or direction. Each one purpose built to work
alongside teams of people, and first is the Kiro autonomous
agent that works alongside developers to resolve backlogs,
triage bugs, and improve code coverage. Then we have AWS
Security Agent that helps you build apps that are secure from
right from the get go. It brings deep security expertise
to review the design docs and also scan code for
vulnerabilities. Accelerate Pentesting and provide tailored
guidance based on your company's unique security
policies. And then we have AWS DevOps Agent, which integrates
with observability tools like CloudWatch, Dynatrace, Datadog,
New Relic, Splunk, and many more. And it integrates with
your Runbooks code repos and CI/CD pipelines so that it can
engage and be your on call assistant to triage issues, but
also prevent them by being proactive. These Frontier
Agents work with higher levels of autonomy and persistence,
and in doing so are able to work alongside us. Another
example of these AgentCore teammates is Amazon QuickSight,
where AI agents work alongside business users to do research
on your behalf and to find business insights and automate
routine tasks with workflows and create multi-agent
workflows, all without ever needing to write a single line
of code. Our vision for the future of work is that every
person in an organization have intelligent agent teammates
that amplifies their capability and eliminate all the tedious
tasks so that they can focus on the work they love the most and
unlock insights that drive real business transformation. To
share more of what we are doing in this area, I'm excited to
welcome Colleen Aubrey, our SVP of applied AI solutions.
>> Thank you Swami. I believe that over the next few years, a
genetic teammates will be essential to every team. As
essential as the people sitting right next to you. They will
fundamentally transform how companies build and deliver for
their customers. At the heart of this transformation is AI
woven into daily operations, embedded in every workflow and
as natural as checking your phone in the morning. But when
do we pull the trigger? Do you wait until every question about
AI is answered, every risk mapped out, every unknown
eliminated? That's the trap, isn't it? We convince ourselves
that clarity equals confidence, that predictability equals
efficiency. But luckily, here's what I've learned. Building at
Amazon. Transformation and agility. They're not opposites.
They're actually partners. And real efficiency isn't static.
It's alive and it adapts. Now, making meaningful change is
also not about automation. Automation assumes that the
current approach is optimal, that the ultimate prize is less
effort. But many times the status quo is not optimal. The
real prize of AI is new products, new services, better
customer experiences, and new business models, not less
effort. But there's a journey to get there. And we all know
this is a journey that is accelerating. It's possible
that the biggest limitation to transformative change is not a
technical limitation. It's our own ability to reimagine how we
work, how we collaborate, and how we make AI part of the team.
So what does it look like to have an Agentic teammate? One
of the first places we've put agents to work as teammates is
in Amazon Connect connect is an easy to use, Cloud based,
omnichannel AI native customer service application. It's based
on the same technology we use within Amazon to power our own
customer service, and it's used around the world to power
billions of customer conversations. Customers like
DXC Technology, they're a global provider of IT and
consulting services. They help companies to modernize their
systems. They use connect to intelligently determine which
interactions to route to which people, and then empower those
people with real time assistance that pulls in from
internal Knowledge Bases and, well, respecting the access and
security controls. This is this enables DXC to deliver very
personalized, context aware support across every channel.
What we see across many customers is that the center of
gravity for customer experience is the same. It's starting in
the context center. But let's be clear the contact center
have expanded beyond just the interactions today. They're
about the operational backbone for customer relationships, and
the agentic capabilities of Amazon Connect are there to
help through each challenge. So let's see it in action. Many
transactions involve bank or credit card or digital payment.
And as a cardholder, one of the sort of most concerning moments
is when you see a transaction on your account that you just
do not recognize. It can happen to anyone, even me. Earlier
today, I saw several transactions on my account that
I didn't recognize. So let's let's see if we can call
customer service and see if they can help.
>> Good morning Colleen. Before we get started, let me verify
your identity. Can you tell me your passphrase?
>> Sure. It's. Show me the money.
>> And can you tell me one of your recent transactions?
>> Yeah, let me think. This morning, I got a cortado at
Illy. >> Thanks, Colleen. I was able
to verify your account. I see in your account notes you're
traveling right now. Are you having problems with your card?
>> Yeah. So this morning, I saw several transactions that I
just. I just don't recognize them.
>> I'm sorry to hear that, Colleen. Which transactions?
>> There was a bunch at gas stations that I've never been
to. But also, I'm not even driving while I'm here.
>> Okay, I see them. I am locking your cards so we can
start an investigation. >> Whoa, whoa, wait. I'm at a
conference. This is the only card I have with me. I need to
use it while I'm here. >> Not to worry. I see you've
added this card to Apple Pay. We will only block transactions
with your physical card. So you can continue using tap to pay
on your phone and registered devices. And I'll also expedite
having a new card sent to your home address.
>> Okay, great. That works. But what about these transactions?
How do they happen? Is there some fraud going on?
>> I'm taking a look now. I'll need to review the details to
see if I can identify a pattern. I'd like to connect you to my
colleague. While I do this, I'll share what I find while
they talk with you. Let's see if we can get to the bottom of
this quickly. >> Okay, great. Let's do that.
>> Hi, Colleen. I'm hector. I'm the investigator assigned to
your case. The agent gave me all your information.
>> I thank God I thought I was going to have to repeat.
>> All of it. >> Nope. Don't worry. And let
me just say I'm so sorry this is happening to you. Especially
when you're a big conference. >> Thanks, Hector. So what
happened? Are my other accounts at risk?
>> Let me pull the transactions and take a look.
>> Okay. That sounds great. >> All right, so analyzing and
verifying fraudulent activity is a process that often takes
hours or days. Using my teammate to help me. I'm going
to do all of this in just a few minutes. So let's get started.
All right. Let's see this. All right. I see the agent has
already flagged the suspicious activity and analyzed them all.
And they found that the geographic pattern of the
transaction seems suspicious. So let's take a look.
Transactions on a map. And I can see these transactions
happen all across the US. And as far as I know, Colleen can't
teleport, so I agree this looks super sus. As my daughter says.
The agent also tells me this pattern inconsistent with a SIM
card. Let's see if we can verify this by asking the agent
to look for patterns across other cases. And in just a few
seconds, the agent was able to confirm likely fraud. As
already suggested, our standard operating procedure for this
type of activity, which is to create a police report and
share the details. So I'll go ahead and do that. Great. Okay,
so we handle the fraud. But that's one problem solved. And
Colleen was also worried about the other problem. So let's
check those out. I'll switch to Colleen to connect agents
building experience so I can create custom agents that will
be able to watch Colleen's account for any suspicious
activity. I just give the agent a name type configuration
template and a quick description. I can defend this
behavior by providing a simple prompt. Next, I need to apply
guardrails for the agent. And that's it. Let's get back to
Colleen and tell her what we did. All right Colleen, it
looks like your card was most likely skimmed and an ATM you
use at the airport. >> What? Really?
>> Yeah, really. But analyze all your other accounts and
good news. There's nothing abnormal. For extra peace of
mind, I set up automatic health checks on all your accounts.
That will alert you via secure message if anything suspicious
does happen. >> Okay, great. Thanks. I
travel a lot for work. This is super frustrating. Is there
anything we can do to stop this going forward?
>> Yes, super frustrating, but let me see what else I can do.
I have AI analyzing your full account and transaction history
to see if there's anything else I can offer you, and it looks
like you qualify for a secure travel account that comes with
a more secure card and won't cost you anything.
>> Okay, sounds promising, but what about travel benefits?
>> Well, this new account gives great travel rewards from
transactions. I found that you have a reservation at the MGM
Grand later tonight. >> Yes. L'Atelier. I love that
place. Have you been? >> Me? No, I don't go to
restaurants. I can't pronounce the name, but, you know, sounds
nice. >> Okay, so let me get this
straight. More security, more perks, and it doesn't cost me
anything extra. >> Yep. That's right.
>> Okay, that sounds great. Let's do that.
>> All right, well, your new card information is available
in your app so you can configure it with Apple Pay.
Enjoy your day. And your lovely dinner, Colleen.
>> Okay, so I don't suppose anyone had joined a customer
service call on your bingo card today. That's okay. Being able
to make a meaningful difference in customers lives and build
relationships, that makes that human agent collaboration so
powerful. And as we work across multiple modalities with agents,
our need for seamless escalations and human
interaction still exists. And it's exactly why we keep
investing in capabilities that make people and AI agents true
partners. In fact, earlier this week, we launched eight new
capabilities in Amazon Connect from Nova 2 Sonic integration
that enables customers to problem solve through spoken
conversations that sound natural, like the one you just
heard. To agents that make real time recommendations based on
the customer conversation itself and automatically
suggest next steps, then to AI powered predictive insights
that combine clickstream data customer profiles to make
highly personalized suggestions. Over the next few years, human
AI teams will fundamentally rewire how work gets done.
They'll change how we build, how we ship, and how we serve
customers. And here's what excites me the most. This isn't
just about doing the same things faster, it's about
unlocking capabilities we couldn't even imagine. Thank
you. >> Thanks, Scott.
>> Connect is a great example of how agents and humans can
work together to solve problems efficiently. So everything we
have shown today and everything we are building, it's all just
the beginning of what's possible with agentic AI. And
when I think about the innovation that will happen
between now and when we are back here next year, I can't
help but be optimistic in every step. We are making it easier
for anyone to build and use these agents, but the
technology we built is just one part of the equation. The other,
more critical part is you. It's the community of builders
inventing and building these incredible things. In October,
AWS builders Partners and schools in West Java, Indonesia,
had a goal to create 2000 GenAI apps. They far surpassed this,
setting a Guinness World Record for most apps made in an on
site event. Over 15,000 GenAI apps. Almost all of these apps
were dreamed up by high school students, who were able to
bring them to life with the help of their teachers and a
few nonprofit staff. And on September 8th, we launched the
AWS AI Agent Global Hackathon. The challenge was simple build
autonomous AI agents that solve real world problems. This year,
we saw 9500 developers from across 127 countries
participate in this global hackathon, and they were
challenged to build, develop and deploy working AI agents
using Bedrock, SageMaker, strands, AgentCore, Kiro, and
many more. And we received 625 agents covering use cases, from
fraud detection to infrastructure monitoring to
agriculture health monitoring, showcasing how AI agents are
being deployed across virtually every industry out there. But
the winning agent was built by Ajito Nelson. Ajito is from the
country of Timor-Leste, but base management is an
incredible challenge. The capital city of Dili produces
over 300 tons of daily waste, yet more than 100 tons go
uncollected each day, clogging the drainage systems, causing
devastating floods and creating serious health hazards. Ajito
built EcoLafaek, an autonomous AI agent that transforms every
smartphone into environmental monitoring tool, empowering
citizens to become guardians of their communities. Cleanliness.
He used Amazon Bedrock with Nova Pro for multimodal
analysis, Titan for semantic similarity search, AgentCore
with Code Interpreter and web browser for automation, and AWS
LightSail with S3 storage. Then citizens can now photograph
waste issues and the AI instantly classifies base types,
assesses severity, and then identifies hotspots so that
giving authorities the tailored guidance they need to
prioritize clean up efforts. This year we also had a
fantastic initiative called Road to re:Invent that teams
got on busses with a challenge to build an agentic AI app and
route to Vegas and compete for the grand prize of $50,000. And
finally, I also want to congratulate the winners of
this year's AI League and AWS program. Builders compete by
customizing and fine tuning LLMs and agents for specific
tasks. And in 2026, we are going even bigger, increasing
the grand prize to $50,000. You can check them out in export
today. The energy and the excitement we are seeing around
agentic AI is truly incredible. The winner from this year's
championship and Road to re:Invent are here with us
today. Please stand and take a bow. Now I want you to think
about the feeling again. That moment when you first made
something work, when you first felt that rush of creation,
that feeling is not just a memory anymore. With agentic AI,
we are living in that moment every single day. We are at a
point where anyone with an idea, whether you are cleaning our
oceans, unlocking the mysteries of the human brain, or solving
challenges that we haven't even discovered yet has the freedom
to build it. The freedom to move from concept to impact at
an unprecedented speed, to tackle problems that once
seemed impossible, the freedom to create without limits
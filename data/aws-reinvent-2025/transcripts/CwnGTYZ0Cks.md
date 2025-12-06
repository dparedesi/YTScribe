---
video_id: CwnGTYZ0Cks
video_url: https://www.youtube.com/watch?v=CwnGTYZ0Cks
is_generated: False
is_translatable: True
---

- Thank you, Chris, thanks. So we're gonna be... We are all here in the
Gen AI, is that right? Everybody's building
yourself and 10 other agents. So we're gonna be talking about that, and I'll hand it over to Aneesh. My name is Mohammad Zaman. I go by Mo. I lead the AWS Strategic
Partnership for Cybage. And with me, Aneesh, he leads our cloud, data,
and AI practice at Cybage. And we're gonna be building some stuff, and you get to know it. And, also, after this, if
you have more questions, come to Booth 12. - Thank you so much. Oh, I'll use the handheld
maybe. Hello? Hey. Okay, I will use this.
Thanks everyone for coming. We're gonna talk quickly about production grade AI workloads, the first and only AI
session at re:Invent. That's a lie, but we'll cover
some interesting things here. So there are key ways that
different organizations, both software companies and enterprises, are thinking about AI in their stack. You think about typical
three-tiered stack, either we have some people
working on their data layer to get it prepared to sell to
foundation model providers. So this is a lot of
publications, media houses, are working on sending their data to model providers in a
more effective manner. You have people who are
working on, obviously, AI-assisted development and code. And it's also changing the way you view an application stack. In the sense that,
previously, you had APIs, which are doing the most heavy lifting of business logic in an application. Now, APIs are getting much thinner. You have AI agents that work
on top of lighter-weight APIs that are largely doing crowd operations, where agents can take on
more of that workload, more of that logic, more
of that orchestration, more of what the platform and the meat of the platform really is. And this is being seen across the bottom. We'll talk a little bit
about what this means in terms of actual real
production-grade architectures. AWS services have evolved
immensely alongside this journey. So back in the day, it started with foundation
models on Bedrock. Now, we have a whole host of services. We have AgentCore, which gives you real-time
runtime with agents as well. So people are adapting, and AWS is providing
the end-to-end services for all of those different workloads. We'll jump into a few quick examples of real production-grade implementations that we're working on at Cybage. And, hopefully, you can
go away with some tips, ideas, as well. So one massive and recurring
issue that comes up is the ability to separate
what is a prototype, or a proof of concept,
within AI development versus what is a production-grade effort implementation architecture. We think about this a lot in Cybage. And what the main takeaway
from this slide is, don't over-engineer prototypes
in the space of Gen AI. AWS has great low-code services, we have Bedrock knowledge
bases, we have Kendra. We have a bunch of services
which are meant for you to prove a concept, and it ends at that. You're not meant to take
those implementation and take them to production. So what we usually design
is a team that works on design and experimentation
in an enterprise. They are only focusing on
sandbox AWS environments, on using low-code services, and proving a concept
for different use cases. Then, you have a higher complexity
data ingestion workflow. All your AI use cases
in the enterprise need real-time data connectors, ingestion. Sometimes, it has to be
custom built from ground up. And then, you have your agents
that work from that data, at least in typical RAG applications, as well as in agentic applications. Where, with AgentCore, now, you can have agents that work
across different MCP servers. So one really useful aspect, and we try to implement
that in our designs, are differentiating between
MCP servers or tools, and then the agents to use those servers. The same MCP server, for
example, in this case, web browsing, or context retrieval, can be utilized by multiple agents. So this separation of tools
with agentic workflows is something that we really,
really focus on in our designs and in our applications. AI gateways are really picking up as well. So there are tools like Lite LLM. AWS also has many offerings here. Having a centralized
place to log, monitor, and observe your workloads is
becoming extremely essential. And the way to do that is
through observability tooling. So AWS now allows you to ingest your Gen AI logs in CloudWatch, which lets you do end-to-end
traceability of sessions, of traces. And observability has
massive importance here. You need to know whether the
workloads you're running, and they're facing issues, are they happening at
the stage of retrieval? Are they happening at
the stage of generation? Are they happening because
users are still figuring out how to use your platform? And observability helps
you separate that as well. So this last layer here,
in terms of LiteLLM, and orchestration and observability, becomes extremely essential. So just the takeaway here
is, don't over engineer POCs. They're meant to prove a concept. Once you've proved that, think about production-grade
workloads on AWS, and what that means. In some other cases, one of our largest
implementations recently was focused on building AI
layers on top of legacy APIs and legacy software products. A lot of us here, even
every booth that you see, we ship software. That's
our bread and butter. It's about, can I ingrain, and
can I infuse agentic layers, on top of those product APIs? But in that process, multiple
challenges do come up. APIs that we've currently
built, and host in the world, are not made for agentic consumption. They are made for consumption
by typical user interfaces. And this can cause multiple issues. I'll give you a simple example. A lot of product APIs
return 100-plus results in their responses, very noisy responses, a lot of garbage-adjacent
responses coming from those APIs. Neither would an agentic
solution ever want to use an API like that, because the way you interact with an agent is probably chat based, which means that you're
sending smaller workloads and smaller results to that chat. Nor would an agent successfully
be able to reason through that massive API response. So API readiness is something
that is extremely essential before you build agentic
workloads on top of it. Another example, APIs
often have dependencies. So we built this application, which did agentic
orchestration on legacy APIs, and one issue we faced was latency. Many people are currently
struggling with it. Our LLM would hop and would
do two consecutive trips to first get authentication
tokens to first call APIs, and then, with the results of
that, call downstream APIs. Again, these APIs have not been built for agentic consumption. If you know how users
are going to interact with your agents, what type of workforce
are they going to run, what type of prompts
are they going to run, you can better design your APIs with an agentic-first mindset. That has nothing to do with LLMs, that has nothing to do with generation, that is about logical
design in your API schemas. So that's something that we focus a lot on in Cybage as well. Out here as well, observability and monitoring
become extremely essential. The good part about tool
calling and function calling is that observability
is more deterministic. What do I mean by that? With open-ended chat responses, you have to create evaluation
matrices that are subjective, that are not completely accurate. With tool calling, and agent
calling, and API calling, you can have more deterministic
evaluation metrics. So if I build an agent that
sits on top of my APIs, I can get to accuracy scores about how successfully it's
able to call the APIs I need it to call for a
certain set of prompts. That determinism is super
useful in evaluation, which you can't get in basic chat. You can't get in just freeform chat. For that, you have to use
custom evaluation metrics. So evaluation, again, I'll focus on, and it's something that we
work on a lot at Cybage. It's something that we infuse in a lot of our agentic development as well. So moving to some of the
real production grade issues that people are currently facing. And we'll talk about each one. We'll talk about how those
are being solved as well. One massive issue, and I'll start in the third box actually, security and governance. The moment you introduce tools
to an agentic implementation, the security concerns, they
multiply by magnitudes. You have your CISOs
getting extremely concerned with context mixing
between different tools that have different permission levels. And the other part there is that people are extremely
apprehensive, obviously, and rightfully so, of sending
PII for LLM model calls. How do you screen out? How do you put guardrails, both
at inputs and output stages? So that's something
that we focus a lot on. You can use services like Macie in AWS for PII detection and PII masking. You can use guardrails. There are some open source frameworks. You can use custom guardrails
to rail your applications, both pre-generation and post-generation. And you can bind user
groups to the right tools that they have access to. This is an extremely essential part of building these applications is that we need to reflect enterprise
access permission levels with agentic permissions. If you're building an
application for internal users, or for your end customer users, each of them have tiered permissions, those need to be reflected with the tools that they have access to. With AgentCore, this
becomes extremely powerful because you can use dynamic tool binding. So AgentCore allows you to bind
tools dynamically for a user so you can build in that pipeline binding that respects
permission levels of that user. So that's something that we focus a lot on in Cybage as well. So that's the security
and governance side. I'll focus, also, a
little bit on the adoption and monetization side
because we have some time. Again, it's not as technical, but token-based pricing is
not working out very well for people trying to ship
out products with AI. What I mean by that is,
if I'm a software company, and a lot of us are
representing software companies, and I push out a feature that
uses LLMs at the backend, people are not willing to
spend on token-based pricing for those end features. People are trying to bake that
into subscription pricing. Either you have a new tier of subscription that demands higher AI workloads. But there are innovative
ways that we've seen some of our clients work
on that pricing mechanism. So imagine you've built an agent that runs a certain defined workload. Maybe it runs a certain
content generation workload, a report generation workload. Maybe it runs a certain action, an actionable output, a research report. Try to price AI-based features
on output and not tokens. That's something that
we're seeing a lot of in different companies, is that, the only way to get
adoption from your end users is to price these features
based off end outputs, instead of on tokens. So that's another interesting
feature that we've learned. And, for that, your API and AI gateway
layers become important. What I mentioned earlier
around platforms like LiteLLM, integrating CloudWatch in AWS, these aspects are required before you differentially throttle AI workloads between different user groups. If I've decided to price an
AI feature differentially by user groups, I need to make sure that I'm
throttling the right groups by their AI usage. So that gateway layer
that gates your calls for agentic layers with end LLMs becomes extremely essential as well. So these are some real
production grade issues and solutions that we're
working on in Cybage. If there are any questions,
any further topics, you can find us at Booth 1231. We're building, with AWS, these
production grade solutions. We'd love to get more into the details. And that is all from us today, so thank you so much for coming. Hopefully, you're leaving
with some tangible learnings, and excited to talk to you all further. Thank you.
---
video_id: 0sfKGUZ6kcg
video_url: https://www.youtube.com/watch?v=0sfKGUZ6kcg
title: AWS re:Invent 2025 - Build a well-architected foundation for scaling generative AI and agentic apps
author: AWS Events
published_date: 2025-12-02
length_minutes: 57.3
views: 1161
description: "You've seen the potential of agentic AI through proof-of-concepts, and you're ready to build a foundation that can support all AI applications across your organization. Enter the complexities: model access and management, tool discovery, memory and state handling, observability, plus deployment and operations at scale! In this session we'll demonstrate how to build a well-architected foundation that seamlessly integrates model access, orchestration workflows, agents, tools and domain-specific da..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
---

- Good morning, everyone. Thank you for being here. I like the Monday morning sessions, right? We are fresh and early in the week, not influenced by other things. Still excited and eager, so this is good. So I'm glad you're here. My name is Chaitra. I am a genAI specialist at AWS. And today I'm joined
by my colleague, Aamna. - Hello, everybody. I'm Aamna. I'm a senior specialist
solutions architect for generative AI. - And we have Dave from Sage, who is one of our AWS customers. - Hi, I am Dave Senior. I'm based out of Dublin, Ireland, and I'm the head of data and AI for Central Services team in Sage. We're part of the product org. Everything we build is customer-facing. - Thank you. So, why are we here today? What are we going to learn about? This is what, you know,
started to happen, right? Chatbots. And it seems very simple. You put a prompt, you get a response. That's how it started a few years ago. But we know, in reality, it's
much more complex than that. There's orchestration and agents and RAG and, you know, applying safeguards. So it's not as simple as this kind of LLM that generates everything. Imagine this, right? You're talking about
one application before. Now, we are at a stage where we are going to put a
lot of this in production. So what are some of the
challenges and complexities here? It's not a trivial job,
it's really complex. So that's what we will try and
address in this talk today. We will see what that
strong foundation looks like for you to take these generative AI and agentic applications to production and even at scale. It is a comprehensive
foundation that we have defined, but we'll just dive
into a couple of layers, look what are the details there. And then we'll have a demo of a foundation that Aamna has developed just to demonstrate how it,
in real life, it looks like, what happens when you start to put all of these foundations together? Then we'll hear from Dave of their journey of building this agentic mesh platform. We'll look at operating
agents and then we'll wrap up. We'll show you a few
resources to take back. Can I get a show of hands of people who have developed proof of concepts, either generative AI or agents? Nice. What about taking it to production? That's more than I thought,
and I hope that's all on AWS. (Chaitra and audience laughing) Okay, so we know that it's not trivial. We already understood
scale is a challenge. But even taking a few
applications to production is a challenge. And all of the challenges
we have talked about before, taking things to cloud, taking things to production
are still valid here, but it is a little bit more than that. In terms of performance,
agents are not just reactive. The reason, they plan, they
act over extended sessions. So low latency and
performance is important, and that is a really hard
optimization challenge. Scalability. When you put thousands
of agents in production, you want to look at some
purpose-built orchestration, some purpose-built infrastructure
to handle that scale. And these agents are
accessing sensitive data. They may. And they may access tools that have access to sensitive data. So without proper isolation controls and identity controls in place, even a small error can
cause catastrophic problems. And these agents need context, right? And evolving context. And they have to be updated
regularly and at scale and they have to be secure. This memory has to be secure. That is another technical challenge to give a memory that
scales and is secure. Till we built generative AI applications, applying safeguards was good, right? Guardrails. But now with agents, you have to continuously
monitor, continuously evaluate, continuously audit, and maybe even have
human oversight in place so that these agents are aligned. Okay, we all understand,
it's very complex. So, what are we saying? We are saying that have
strong foundations in place. And what does that mean? You can look at it two ways. It's either you're building
one or many applications and you want to set up the foundational architecture in place, or you can look at it another way that you are a platform team, an IT team, you are setting up the central platform, and you're onboarding different
lines of business or teams, and what does that look like? So I'm not go into detail here. I have another slide which
talks more in detail. But the idea is that you start
to consolidate components and offer a shared services, and you have this kind of governance centrally control in place. So it may be any policy,
compliance, security, even you get, you start to
see cost efficiencies, right? So one example of a shared service could be that a model catalog, everybody who builds the application don't have to have a
model catalog to access. You can put that in a central
place as a platform offering. And, you know, the team sort of building these
applications can access that. But what does that look like? So we are saying, it's a
comprehensive foundation. At the core of it is the hub, which is the model hub and
the agents and tools hub, and giving access to these via gateways. And then you're building these agents, you are customizing these models, you're building these tools, you need an execution environment,
a runtime to host these. Data. Data is in silos, data is in
data lake, data warehouse, but you don't need all of that data to build these applications. So this layer concerns about
building ingestion pipelines, building indexing pipelines, taking that data and
putting into vector stores, and having a long-term and short-term memory store for agents. Then on top of the orchestration. Orchestration is more about, okay, I have access to all of these. How do I really build this flow? It could be a workflow, which means a known
series of steps, right? You know, query, calls a
model, there's another prompt, maybe you're chaining different models, you're building a RAG architecture, or it could be agents, but that doesn't necessarily mean it's part of the foundations, but orchestration can
become an important layer. If you want to give templates, right? There is a common data. You want to give a RAG a template for that so that everybody can use. It's a good place to put that
in the orchestration layer. Then you have clients
accessing all of these. And let's not forget the
three most important pillars, operational excellence,
observability, and security. Observability is very,
very, very important. To get some insights
into what is going on, these are black boxes. So how do you really know what
is happening under the hood? And we'll talk a bit more on that. You know, operations, it's not just about
operating the foundation, it's about what do you
offer to these applications as part of this foundation
that helps them operationalize. It could be something like
a prompt management store to store and version the prompt templates. It could be part of the foundation that these consumers'
consuming applications and teams can use, right? And let's not forget security,
data privacy, data isolation, all of that comes into play. Now I know it looks like this big thing, but we'll, you know, dive
into a couple of them. Before I dive into the layers, there are two services I wanna talk about, which is Amazon Bedrock, which
is our fully managed service that lets you build
generative AI applications. And you get access to
state-of-the-art models, first-party and third-party. You're able to scale cost effectively because you have different
consumption modes, you have a lot of features here that lets you balance out
latency, cost, and accuracy. And you can customize
the models with the data or build RAG architectures. And then you can apply guardrails using the Guardrails feature. The other service I wanna talk about which will help you build that foundation is Amazon Bedrock AgentCore. You may or may not have, maybe familiar. This went GA a few weeks ago, and this is our fully
managed agentic platform that gives you a lot of managed services to build and scale agents. It gives a secure runtime to
build and deploy these agents. It gives memory, long-term
and short-term managed memory. It has a gateway to access tools. And all observability and
instrumentation of traces all built into the platform. So when you put the two of them together, this is what it looks like, right? You have Amazon Bedrock. We talked about the model
catalog and the gateway, Bedrock will help satisfy that
model catalog requirement. And then we are talking about runtime to deploy agents and tools. And Amazon Bedrock AgentCore
will help you do that. Now, the big advantage of
Amazon Bedrock AgentCore is that you can use many
different open source frameworks, Strands, Crew AI, LangChain, LlamaIndex, to build these agents, and you'll still be able
to deploy all of them in the runtime, right? You containerize them and deploy them. That's it. You know, the service manages it for you. So this is good, right? We looked at what a comprehensive
foundation looks like, let's dive into one of them, gateway. Now, we are seeing a few patterns emerge. One is called the LLM gateway, and this has been there
for a bit, I would say. This is all about giving secure access to a model catalog, right? And it gives a unified API, so that developers
don't have to, you know, worry about accessing different models with different API specs,
different prompt templates. So this can handle all of that. Now, the two other
patterns that are emerging are that one is tool gateway and one is the agent gateway, right? These are becoming popular. Tool gateway is about, you know, it secures and standardizes
actions and integration, and registry is a
central registry of tools that agents can access. Similarly, agent gateway
gives access to agents, and agent registry is a catalog of agents which are deployed, all of their capabilities, metadata, even registering and
deregistering agents all happen. Now the question might be,
do you need all of them? Not necessarily. It depends on what kind of
use case are you building. So, for example, if you
look at the LLM gateway, why do you need an LLM gateway, right? If the models are on Amazon
Bedrock, which is our service. If you may have customized
models and put it on SageMaker. That is also one of our managed service. Or it may be on EKS that you have hosted. Or it not even be on AWS, it
may be from another provider. Now you want to reduce that
friction for developers in accessing all these
different models, right? You don't want them to worry about it. So the gateway takes care
of that orchestration. It gives a unified API. Mostly it is an OpenAI
specification that we have seen with all of these tools. And most of the cost that we see is a token cost that you want to control, you wanna attribute, and
this can do cost attribution. So as use cases come in, you can see which use cases
using the most number of tokens, causing the most number of, causing the most dent in the budget. And you're able to apply rate limits to all of these different teams. And the way it's done
is you hand over API key to all of these different teams or users and then you can start to track costs and all of the actions. Now, the other big advantages,
you can apply guardrails. Let's say, enterprise-wide,
you have some guardrails that you want to apply always, whoever builds application
accessing these models need to use those guardrails. This is a great place to put them. Now, all the foundation that we showed doesn't mean that we have a service for every one of those layers. No, we do have gaps. And one of them here, what we have done is we
have published a solution that shows how can you deploy,
in a well-architected manner, a solution offering that is
available outside on AWS, securely, cost-effectively, and reliably. Now this takes a open source
solution called LiteLLM. You may have heard... Can I get a show of hands
if anybody has used? Yes. So they have two versions,
an STK and a proxy server. So this takes the proxy server and puts it in EKS or ECS and deploys it. Now, LiteLLM comes with
all of the features that we talked about for
an LLM gateway, right? So this is just about taking
it and containerizing it and deploying it on AWS. There are a lot of
other solutions as well. For example, Kong AI Gateway
has this, Envoy, OpenRouter. So there are a lot of solutions
that you could explore. Now the question is, if you are just accessing
models on one provider, one service, you may not need this. But still, if you are looking
to do cost attribution and segregating and isolation
between different teams, it's a great thing to have a gateway in
front of the model access. Now, the next thing we wanna look at is the tool and agent registry. Now, the pattern that's coming is, yes, there are purpose-built gateways and registries for each of these, but they can also be combined. There are solutions that are coming that are combining these two
things and giving as a service. One of the example of tool gateway is AgentCore Gateway that
comes as part of AgentCore. It provides unified access
to all of the tools. It could be that agents are
running in AgentCore or outside, it doesn't matter, you
could still use the gateway. And you are able to access
either API endpoints, lambda functions, MCP servers,
you attach them as targets. This creates an MCP
endpoint for all of those, and the agents are able to discover these using semantic search
capability of the gateway. So this is an example of tool gateway that gives kind of a registry and the gateway to access the tools. Now, the other solution I wanna show you is this open source solution that some of our colleagues developed. This is like a comprehensive
gateway and registry. MCPs, agents, and to access both of these. It's open source, it's available, so feel free to check it out. And one of the good things is, is enterprise-ready observability
is integrated into it. So the way it works is there's
an agentic server endpoint in the front, and rest, everything is
deployed as MCP servers in an EKS cluster. Now it also supports two
types of authentication, M2M using Jot, and then
the 3LO authentication. So it's really good, works as both, and a lot of development is happening. Even you are free to contribute. It's open source, so take a look. Okay, so we looked at gateway, there are a lot of different layers. We are not gonna go into everything. But I do want to talk about
one very important topic, that's observability. Now, we know I have built
software applications. I've been in this
industry for a long time, so I've built them. So at that point, observability for those apps was more about keeping
the systems alive, right? We were worried about
uptime, latency, and errors. But now what has happened is it's about keeping the systems aligned. You are worried about
quality, bias, right? Is there any toxicity,
hallucinations that are going on? So whereas earlier, it was
infrastructure monitoring. Now you're almost monitoring intelligence. So why do we need it? Quality is very, very important. You wanna understand the
quality of the response. You wanna understand the tools are being, the right tools are being selected, right? Agent works by having
access to many tools. So is there right tools at its disposal? Is it picking the right tool? Is it converging the right path? Convergence means is it
taking the shortest path to get to the response. So all of that is quality, right? Cost implied, you wanna
definitely understand cost. Latency, not the system latency, but why is an agent
taking time to respond? Which step in the process is taking time? And then you also want to measure risk. Risk is the most important thing. And how do you measure it? Seeing if there is any PII leakage, is there any toxic output. There are ways to do it, and I'll talk about how
you would do that, right? So this is how an observability
system works, right? Your agents are generating operational and semantic signals in the
form of logs, traces, metrics. And another important
metric is user feedback. It has to be collected. Now what the observability
platform/tool will do is it'll aggregate and
visualize these signals. And another important thing, which a lot of times it's not set up as the evaluation layer, right? It's job is to interpret the quality and risk using some evaluations. You can collect all the metrices you want, but if you do not use it, if
you do not use for evaluation, then there is no benefit,
other than understanding costs. So once the evaluation layer,
you evaluate all of this, then it's the optimization loop
that happens where you know, okay, it didn't really
generate the output I want, so now I'll use a different model. I'll use different prompts. Or you make some changes
and this loop continues. This observability
platform could be any tool. Langfuse, for example, is a great tool. AgentCore has observability. That is a great tool. So you can plug any one
of those tools here. Now, what are you measuring? Functional, we understand
quality is what is important. As I was talking about,
even in, let's say, a retrieval augmented generation app, is a retrieval relevant of
what is happening, right? Because a chunks are extracted
from the vector databases based on the prompt. Is it identifying the right chunks? And is it finding the right tools? Is it passing the right
parameters to the tool? That's the second quadrant. And the fourth quadrant, user
feedback, is also important. Yes or no. And then this response works
or this response works, giving them two choices. And you could also imply
certain attributes. Like, for example, if
the user is prompting the same thing again and again, maybe the answer is not satisfactory. Safety, toxicity, and PIL leaks, and bias, very critical to measure all of these. This is not a comprehensive list. There are many more that
you can start to measure, but these are very, very
key and important metrics. There are two types of evaluation. Offline is done during development. Integrate this into your DevOps pipeline. Continuously evaluate the
system and applications. And here, the dataset that you use is kind of a golden dataset
that you have created. And it could be user-annotated
or synthetic dataset. And once that is done, then
comes the online evaluation wherein real user interactions
are being measured. This is in the live system. Now you don't have to measure every trace that's coming out of the
observability system. But if it's a very high-risk
application that you have, it makes sense to measure every output and see if it's performing
the way you're expecting. Otherwise, you can sample
certain dataset, 5%, 10%, and start to evaluate those. And then continuous
iteration is important. Now, just the lifecycle. You start, you define
your goals and metrics, and then you curate this golden dataset. Do not forget that. That golden dataset is so important. You may think, "I will just
develop the application, put it in production,
and see how it works." No. You develop the application,
you test with a golden dataset, and then you put it in production. And then test, test, test. Test under different conditions. And the way to test are there are three
different ways to test. One is you use automated evaluation, which means you're using some
kind of coding to evaluate, or you do some kind of Regex, or you are comparing it
to a ground truth dataset. The second way is to use another LLM, another model to look
at the output and say, "Hey, here is a prompt,
here is the output, and give me some measurement." And the prompt for that
LLM should be very good. Use a really good LLM. And this is called LLM as a judge. The third is you can use
humans, the most expensive, but you can create cues, you can have humans evaluate
maybe more close to accuracy, but also think about the cost. And then the continuous optimization. Now, how would you do this? Observability can be integrated
and implemented two ways. One is all of these observability
tools come with an SDK. You can use that SDK, build that instrumentation
into the application. Like, for example, Langfuse. Langfuse will have an
SDK that you can use. The other way to do it is you collect all the traces feedback into an OTel collector. It's a standard for collecting and processing telemetry data. And then you can feed that
off into different systems of how you wanna measure. Means it can go into CloudWatch,
which is a service of AWS, and there you can create dashboards or it can go to Amazon S3, which
is our scalable data store. And from there, you can
do some offline analysis. Or it can feed into these
systems, like Langfuse, from where you can do a lot of insights. You can analyze that and feed
it into evaluation layer. Now let's look at a demo from Aamna. And sorry, you're looking at my clock. That clock is not working, so come on. - Thank you. Thank you, Chaitra. Really excited to share the stage with Chaitra and Dave today. Chaitra walked us through the journey of building foundational components to scale generative AI
applications into production. But how many of you are wondering how this looks live in action and how you envision this tangibly? So I'm really excited to share that my team has open
sourced an accelerator called the Agentic AI
Foundation Accelerator, which basically ties or stitches together a lot of the foundational components that Chaitra was talking about, including a generative AI gateway, observability, offline evaluation, guardrails to safeguard your application, and also infrastructure
as code deployment. So this is a lightweight but
well-architected foundation that gives you, you know, the opportunity to deploy this solution, leveraging infrastructure
as code using Terraform, and helps you host your agent in a secure and scalable fashion, leveraging Amazon Bedrock
AgentCore Runtime. So what you see here,
right, on the center top is Amazon Bedrock AgentCore Runtime that helps you host the agent. So in this demo, we are leveraging an open source
framework called LangGraph, but you could possibly
bring your own framework. It could be Strands, Crew
AI, your own code logic, your own implementation,
and host it on Runtime. And then you see on the
bottom, in the center, the LLM gateway, right? So in our accelerator, we are leveraging light LLM guidance that Chaitra mentioned earlier to enable the agent to invoke
any model of your choice that's not just on AWS landscape, so not just on Bedrock, but also beyond. So our accelerator also
helps you leverage models that are on SageMaker, or
by third-party providers. So that's also another aspect. The other thing is that
the LangGraph agent that we have in our case is
using three different tools. So the use case that I
will demonstrate today is a very simple customer
service chat application. But you can also basically
adapt this foundation to your use case to your industry. The foundations remain the same. You basically, again, you know, do the code and the implementation
based on your processes. So in our example, the agent
is leveraging three tools behind the AgentCore Gateway, right? So Chaitra also mentioned
the tools gateway. So behind this tools gateway,
what we have is three tools. The first one is a RAG-based tool, which is helping you retrieve context from your enterprise indexed data. This is leveraging Amazon
Bedrock knowledge base. The other tool that we are
leveraging is third-party APIs for creating and providing
information for support tickets. So, for example, your agent is not able to
answer a customer query. So then the agent routes this
and creates a support ticket. The third tool is a web search tool, which is also behind the gateway. It's leveraging third-party
API with Tavily. Now all of this is then being audited with the help of not
just Amazon CloudWatch that you see on the right end, but also a third-party
observability tool called Langfuse. So we are basically collecting traces of the agent interaction, and then on top of that,
running offline evaluation during the development phase to make sure that this application is working as expected. So to showcase you how all
of this works in action, what we've put at the top
is front-end application powered by Streamlit. So all of this is kind
of, I'm going to demo and show you how all
of this works together, but we've also open-sourced this. And at the end of the presentation, we are gonna share the GitHub,
you know, resources with you so that you can also,
you know, try it hands on or take it to your
builders and get feedback on how all of these foundational
components work together. So, as I mentioned, right, this is basically a customer
service chat application that is leveraging LiteLLM gateway built on AWS infrastructure. So this agent has access
to your choice of models. And it has two modes. It has a local mode, as well as a mode where
the agent is hosted on AgentCore Runtime. So you test it locally and
then you deploy it on AWS, and you provide the ARN. So the identifier, the region, as well as it supports authentication. So you provide the user access token that authenticates the user. And as you can see, it's
integrated with LiteLLM gateway. So this agent has a list of
models that it can access, not just Bedrock models, but
also models outside of Bedrock. So OpenAI models, for example. And then you also have user
identifier to tag your traces. So I'm basically gonna
send it a hello, right? So I'm sending it a quick hello, and the agent responds based on the system prompt that I've set. So it's a customer service
agent for any company, it's a dummy company, and I have some data
that I've indexed, right? So I ask about how to reset my router hub. So there's a device that
any company supports. And then the agent goes and,
you know, provides an answer. So it's basically leveraging
the retrieve_context tool to provide me with an answer. And you can see that it
also kind of lists down the sources that it leveraged. So which documents did it
use to answer the question, and also, what's the
relevance of the retrieval. It also tells me other things
like what model was used, what tools were used, and
what was the citation, so what document, page
number, and all of that. And also adds a trace
ID for observability. I go on to ask another question, right? So I try to reset the router
hub based on the answer, but it does not work. The agent goes ahead and provides me with another
addition set of steps, but then goes and says, "I can create a support ticket for you if this is not satisfactory." So I go ahead and say,
"Yes, let's create one." The agent then uses that information to further query and ask
me about further details about my email ID, my
problem, description, all of that, right, my details, which I go ahead and provide. So the agent is intelligent enough to pick all of that information
to use as parameters for my create_support_ticket
tool call, right? So you're not explicitly mentioning what are those parameters. So I'm just kind of in natural language, providing all of that information, and the agent is going to pick that up and understand that it needs to call the create_support_ticket tool that is hosted behind
the AgentCore Gateway. So in this case, you can see
that a ticket was created using a third-party API. It provides me with
all of the information. And then I can also see that the create_support_ticket tool was invoked in this process. Now, I take a different route, right? So I ask the agent if it also happens to
provide investment advice. And it tells me that your
input contains content that violates a policy. So what we've also done is integrate it with Bedrock Guardrails to make sure that this application
is safe and trustworthy. You can also have PII detection in place and other capabilities. I go ahead and then ask what
device did I ask help for. This is an example of short-term memory for session management. So I don't need to repeat
information for the same session. It knows that I asked a
question about the router hub and I created a support ticket. Now what I'm doing is I'm switching from local
mode to the AgentCore mode. So I am very happy and
satisfied with my agent and I hosted it on AgentCore Runtime. I provide it with the
identifier for my agent and a user access token, right? So as I said, it also
has OAuth integrated. So I provide with that
authentication token. And it now says that it's
connected to AgentCore Runtime. So now it's interacting
with the agent on the cloud. So I again go and ask
similar questions, right? So, what kinds of devices are supported by any company broadband? It goes on, and then again, does the retrieve_context tool call and behaves in a similar fashion. What I'm trying to show you here is that you know the local mode then can be hosted on the cloud. Here, you can see is LiteLLM. Chaitra talked us through,
you know, this gateway, I'm showing you this UI, which
shows you a model catalog that is basically the shared component. All of the different models and providers that are supported in your enterprise via the LiteLLM gateway
can be checked out here on the UI of LiteLLM. You can create access key,
as Chaitra was mentioning, an API key for your team or your use case, and then attribute cost to that team or to that use case, right? There's also a playground, where you can basically use
that key and test it out. And then you also have a very, you know, comprehensive usage dashboard which tells you what
is your spend per team, what are the top API keys,
what are the top models, what are the top providers that are being consumed in
your organization, right? So moreover, there's also logs available. So as Chaitra was talking
about logs and traces, these are logs for model invocation. So every invocation that my agent made, I now know what were the total
tokens, what was the cost, was it a success, or was it a failure. So this is how light LLM looks like. I now switch to the observability
tool, which is Langfuse. In this example, what I'm going to do is I'm
going to look at the traces generated for my agent invocation, right, via the Streamlit application. So I go to this tracing
tab for my platform and I just filter down
for the latest trace, which was the trace of the interaction that
you just observed, right? So in our code, we also tag these traces. So very easily you can filter out and categorize all these traces when you're, you know,
creating metrics on top. So in my case, it's a LangGraph customer
service agent trace. And this is the user ID that you also saw in the
front end application. So you can attribute it
to user IDs, project IDs, so on and so forth. And these are the different metadata that's being collected as output
of your agent trace, right? You have a timeline view, so you can also check what
time it took for every step. So if you see that your
agent is really slow, you know, was it the retrieve contact step or was it the create support ticket step that took a long time, and you can easily optimize the speed and the latency of your agent. So here, you know, there
are different steps, and I'll, you know, it has different kinds of metadata, right? So the create support step, for example, has all the parameters that were used to invoke this tool call. So for your retrieve context also, you can also get details like
what was the relevance score, what were the items that were retrieved, and so on and so forth. What I'm now going to do is also show you how we are
collecting user feedback, right? So as Chaitra also mentioned, this is another important
metric that we collect, right? So I'm going to ask a couple
of questions to my application. So the agent is going to
answer these questions. And if I am satisfied, which I am, I'm going to put like a
helpful, like, thumbs up, and also provide certain, you know, natural language comment, which can be, you know,
kind of worked upon to gain insights about the performance. And we are collecting
this as well on Langfuse. So as you can see, we have
something called user feedback, which we are normalizing and also collecting
some, you know, comments to understand how all of this works. I'm now basically gonna demonstrate how offline evaluation works. So this is a basic Python
script that we've created, where we are using some ground truth data to kind of send some queries to my agent. And then I'm collecting
the traces from Langfuse to use LLM as a judge to
create certain metrics like latency, you know,
faithfulness, correctness, also tool accuracy. So my expected tool call
was, say, retrieve_context, and the agent went and
created a support ticket. So, you know, the accuracy was zero. So these kind of things you can create during
the development phase and incorporate in your DevOps pipeline. So as I said, we've open-sourced this. So also looking forward
for you to check this out. Chaitra is gonna share the
resources with you later. But just to kind of recap, right? So we have the LLM gateway that leverages Bedrock and other models. You have the tools gateway
that leverages different tools. And then you also have
different components like observability and offline evaluation, where you bring in your golden dataset and then create different metrics, right? So I have a query, how
do I reset my router hub? And I have expected tool
calls like retrieve context. And we are using some Python
logic to create tool accuracy, parameter accuracy,
and also LLM as a judge to create response quality metrics like faithfulness and so on. Moreover, you know, we also
provide infrastructure as code, as I was mentioning. So it's available in Terraform. And the main purpose of this is that developers and
builders can quickly deploy and test out the solution end-to-end to understand how all of
these foundational components are being stitched together. So everything that you see and everything that was
deployed as part of the demo can be deployed end-to-end
with infrastructure as code. So, yeah, this was basically the demo. We saw a lot of things there, right? So we saw the LiteLLM gateway. We saw AgentCore Runtime
hosting your agent. We also saw AgentCore Gateway, which had different tools behind it. All of this was tracked and
monitored with Langfuse, and then we had offline evaluation on top. This is all I had for the demo, but we have more in store for you. And it's a pleasure to move
on to the next segment. I would really like to
in invite David Senior, Dave Senior on stage, who
will tell us more about how Sage is implementing
agentic AI in their organization and leveraging foundational components. Welcome on stage. - Thank you, and thanks for the invitation
to present here today. So we'll start off with a
little bit about who Sage is and what we do. We have... We mainly work in the
areas of accountancy, HR, and payroll. We produce software in those domains. We've got some growth numbers
there on the screen as well. There's 11,000 employees worldwide, well, slightly more than that,
spread across 20 countries. We have 6 million businesses worldwide that use Sage products. And a kind of fun fact there is 1/4 of the U.K. employees
are paid via Sage software. So, what have we got
today in the agent space? We have our Help Search. I think everybody's building
these types of solutions at the moment. So RAG-based Health Search. Our product teams can
integrate this into a product within five days into production, which is a great performance. We have our Instant Analysis. So Instant Analysis uses LLMs to summarize financial reports and answer customer questions on them. We have our Accounting Agent. This actually wraps up
a lot of functionality, where we allow customers
interact with the product through some natural language, and also we delivered insights
into changes in their data, potential errors in their data entry. And then we have our Agent
for Close is another example, where we have a an agent that helps customers do a period close in the accounting product. But we have some challenges as well. So we have a very
distributed architecture. Sage has over 200 products worldwide, and we've grown massively over the years through acquisitions. Because we have such a big organization, decision-making is distributed as well. And while my team is a
Central Services team and we're building AI solutions, we're not the only team in
Sage that are working with AI. Everybody's working with AI. In order to address our suite strategy, where we want to sell software
in packages to customers, we also need to have an AI experience that straddles those products. So that means that a customer needs to be able to use our agents to interact with our HR products from our accounting
products, and vice versa. We also want to be able
to work with a payroll. So this is where our agent
mesh approach comes in. So just a moment on
agentic mesh architectures. We've got a few examples here on screen. We've got the basic mesh, which would be for a smaller setup, maybe with an agent registry, maybe not, which allows agents to
interact with each other using the agent-to-agent protocol. We have the gateway mesh. So a gateway mesh would
require all agentic requests to go to a central point to be routed to the appropriate agent. So the challenge with that is when you have a large organization trying to centralize everything like that, you build a single point of failure and you build a requirement on every team in your organization to
interact, integrate with that. We've also got an example
here of a hierarchical mesh, where we have, as it describes, a hierarchy of orchestrators and agents. And then a more complex mesh
would be a federated mesh, where you've got bridges
between multiple meshes and maybe multiple
authentication sources as well. But this, sorry. So this is what we've come
up with for our architecture. This is our agentic strategy for Sage, and it's using a combination
of the different meshes that we showed previously. So if we talk about this, from the left, from the right to the left, we can talk about what we've got today and what we're working on for the future. So we have our tools on the
extreme right-hand side. We have our MCP servers. We also have MCP-like
solutions that we built pre-MCP before the industry had
settled on that standard. Workflow orchestrators
and solutions like that. And now we're starting to use the AgentCore Gateway for MCP as well. And we have these spread
across multiple business units and multiple products in Sage today. So in front of our gateways,
then we have our agents. We have three types of agents that we've defined in our architecture. We have specialized agents that do particular role-based tasks. We have planning agents that
can plan complicated tasks to be orchestrated across
those role-based services. Our agents, sorry. And then we have our main agent. Our main agent is our orchestrator. Our main agent would be the point of entry for the agentic experience
within a product. When a customer opens up
the agentic experience within the product, they'd be
connected to the main agent. And based on the user's request, the agent may need to
use the planning agent to request a complex workflow to be orchestrated across
the specialist agents, or they may just trigger
a specialist agents for a simple task. The other alternative is that the user is requested in action that is not supported
in the local product. So in that example, maybe you're doing some data entry in your accounting software, and then you remember you've
got a new start next week. So you ask your agent to create a new user in the HR platform. In this situation, the main agent will have
to go to the agent mesh, it will look up the
customer's entitlements based on the tenant that they're
signed in, in context of, and then it will, I'm sorry,
that's happening via MCP. So we have an MCP gateway for that, where we're looking up
our entitlement service, we're getting the HR product that this customer's tenant
has purchased from Sage. And then we would do an
agent-to-agent handoff to a main agent for that product using the agent-to-agent protocol. The user can then interact
with the main agent for HR in a similar manner,
where maybe it's a complex task that a plan needs to be
generated by the planning agent or it's a simple task that's just triggering a role-based agent. Outside of our products
domain, within our mesh, we also have observability. Because as was mentioned earlier, in order to have a good understanding of what is happening
within your environment, you must have observability. We need to be able to trace, not just the agent interactions, but the triggers that go
through our products as well. So if a user is triggering
an API within our product, we need to be able to see
the successful completion of that action or the failure. We also have a centralized identity, which is part of our mesh here
using our Sage ID service. All users are authenticated via Sage ID. However, access control
is not centralized. Access control exists
within a product domain. So if you did request an
action for the HR agent, you may or may not have permission
to complete that action. That action would have to be, the agent would have to
look up the entitlements within the local product and understand whether
or not you can perform, they can perform that
action on your behalf. We intend to also build a just-in-time elevation of privilege, where you could actually, the agent could request
to a more privileged user to perform the action on your
behalf for that one time. So, what's next? We're looking at modernizing
the agents that we've built to use Bedrock AgentCore. Most of what we've built
today within my team has been built on AWS services. So the phrase, modernize,
is kind of funny to use, considering how new AI and
LLMs and this world is, but that's how fast
the industry is moving. So we're looking at bringing
our architecture up to date with Bedrock AgentCores and
consolidating into our mesh. Today, there's a lot of isolated
AI experiences within Sage. We want to bring this
together as a single mesh. And then our next step after
that is to build more agents. So we will be publishing internally our own reference architecture for how we need to build agents. Thank you for your time. I'm going to hand you back over now for another piece on AgentOps. Thanks. - Hello. Okay. AgentOps. Now, it's not a single
solution that we can provide. It's not a single tool, right? Ops is a collection of processes and tools so that you are able to take these and manage it in production. Now, if you take the lifecycle
from prototype to production, every step is ops is about
giving that capability and components to move
to the next step, right? So prototype, in the prototype phase, developers need access
to different models. So a way to experiment quickly with all of these different models, way to experiment with
different agent frameworks and do some kind of AB testing. Then when it goes to development, giving an environment where they can, like a sandbox environment
where they can deploy this and start to integrate
observability into it, start to run evaluation. Dev also can do evaluation. And then integrate into
these other services that we talked about,
like gateways, right? And then when it comes to testing, it's more about end-to-end QA testing, but you can also run evaluations there, because maybe you have a different
set of data in QA system. Then once it goes to
production, live monitoring, which we already talked about, but it's also about security
and governance, right? Keeping auditability, doing audit, auditing the system regularly, and then having all of
this bias and toxicity and risk assessment done regularly. Now, it's also about the
DevOps process, right? Managing the lifecycle of
these applications and agents. Agents have to be decommissioned, models undergo version changes. So, how do you put all of this together? That forms the big term,
what we call operations. Now, giving an example of, you know, what does maybe a pipeline look like? Let's say an agent has developed an agent, agent developer has developed an agent. You can have git flows
to check out that code, build a container. I'm talking about a container here because I'm giving an
example of AgentCore, deploy to AgentCore, and
then run some evaluation. And this evaluation could be that it is run in the dev
account, let's say as a container, but not necessarily. As Aamna was showing, you
can run a script locally, test that dev endpoint
against a golden dataset, make sure it's performing as expected. All good. You put it in a registry. Agent registry is something,
there are some tools out there, or you can start to
store this metadata here, I'm showing some kind of a database that you can start to store. And from there, you're deploying it to QA, run more evaluation. Maybe this dataset is
different than the dev dataset. And all of the time you
are sending traces to here, as an example, Langfuse. Now Langfuse has a feature
called Environments, where you can have dev, QA, prod, so that you're isolating these traces, and that's a very good way to architect these different accounts. And if it is not as expected,
you start to optimize, all the cycle begins
again, make more changes, maybe use different models,
maybe use different prompts. And then once everything is okay, here, it's a manual approval always before going to production,
and you deploy to prod. Here, you're doing online evaluation. Now this online evaluation
could be something you build, or these tools also have capabilities to do online evaluation. For example, if you use Langfuse, you can use their online
evaluation capability to do that. Just make sure you're
sampling certain required data to be able to do that. And then you're collecting
user feedback from the app. Everything goes into the
observability system. And this is an example of how
an agent DevOps can be set up. Not necessarily saying
everything has to be this way, but just an example for you to look at. What is operating at
enterprise scale means. Let's say you're a platform
team or an IT team, and you are setting up this foundation. And how do you set it up? If you go back to the
cloud operating models that we all have seen, centralized gives lot
of good standardization, decentralized gives lot of
agility to those end teams, but federated, where it's
kind of a balanced approach. So maybe where I say the platform core, that is our foundation, maybe that gives some shared services. For example, model catalog and
gateway is a great example. That could be a centrally hosted thing. Now that doesn't mean it's one deployment. It could be several deployments,
but you are controlling it, you're governing it in a central fashion. Agent foundations, what I mean
by that is runtimes, memory. Tools can also be part of the platform. If you are customizing models, means fine-tuning, pre-training, that infrastructure can be
part of the central platform. And then, observability. Now on the left-hand side is what these consuming applications are. Either they own their data, a lot of time, platform
team does not want to bother about the data, so maybe it's the consuming
team's responsibility. Again, this can be sliced
and diced in a different way. I think the key thing to understand is adjust to your operating model the way you have been organized. Just to recap, this was the foundation we talked about. And it is extensive. What you need to keep in mind is set up the core capabilities. You don't need everything. What do you need to
build those applications is more important. But there are certain things that you absolutely have to build, which is observability and safety. Have a platform mindset. I think it is more and more important because governance is a big
piece of, especially agentic AI. How do you centralize this governance? How do you manage the risk centrally? So having that kind of
platform mindset is good, not that much that it stifles innovation. So design for flexibility. You know, a lot of times,
when you centralize, it stops the agility factor of it, right? You become a bottleneck for
all of these different teams to build and deploy these applications. So there is a fine balance,
like we talked in federated. Here are some resources for you. All that we talked about. Not all of it. Some of it is in the first
blog, which is the first one. The second one is a
blog that we published, talking about the LLM gateway
solution that we showed. The first one at the bottom is the guidance that
Aamna was talking about, the solution they have
published, it's open source. So take a look. It will give you that leg up to start to build your foundation. And then the second one at the bottom is the MCP registry and agent registry, our solution that we talked about. If you wanna continue building
your agentic AI skills, here is a skill builder link. Please feel free to explore that. Do not forget to take the survey. It's important for us to
get feedback, good and bad. So thank you for your time. Appreciate all of you being here. Thank you. (audience clapping)
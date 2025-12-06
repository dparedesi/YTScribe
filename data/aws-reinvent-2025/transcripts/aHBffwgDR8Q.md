---
video_id: aHBffwgDR8Q
video_url: https://www.youtube.com/watch?v=aHBffwgDR8Q
is_generated: False
is_translatable: True
---

- Thanks everyone for joining
this late afternoon session and welcome again to re:Invent. My name is Stefano Sandrini, I currently lead a team
of solutions architect, covering small and medium business in Europe South and France. So covering Italy, France,
Spain, and Portugal. Today, with me, we will
have David Gonzalez, CTO of Cires21. Together, we will show you how Cires21 is revolutionizing
advanced video workflows using AI on AWS. In the last seven, eight years, I've been lucky enough working for AWS to work with many media and
entertainment customers. In general at AWS, what we see based on our
conversations globally with these customers is
that industry leaders and decision makers decide to use AWS to run their media entertainment workflows mainly because of three main key reasons. The first one is the deep expertise and knowledge of AWS in
this specific industry. So decision makers, basically they want to leverage these expertise to drive and accelerate the digital
transformation of their company. The second reason is about technology. So as AWS, we provide
purpose-built services as well as pre-built solutions
that our customer can use to leverage cloud data and AI technology, again, to accelerate the innovation, innovation of their product, innovation of their services,
innovation of their platform, innovation of their operations. The third reason is about partners. There's a large ecosystem of AWS partners that are heavily focused on media and entertainment use cases. So when we work together with these customers in the
media entertainment industry, these customers can find the right partner for the use case, the right partner that can fit their business needs and unique business requirements. And together with us and the partners, we can accelerate the time to value for those customers. So these are the three main reasons. And when we start working
together, AWS, the customer, and the partner, we see
impact in six main areas. So we have like six solutions areas for media and entertainment. Of course, there are areas
related to classic media and entertainment use cases
like content production, media supply chain, archive, broadcast, live production, direct
to consumer and streaming. But there are two areas
that I want to highlight because they are related to a very common and important topic nowadays in media and entertainment industry. And the topic is reinventing monetization across all channels. This is mainly due to
the fact that of course, the media entertainment industry is going through a transformation
in these years, right? And media entertainment
customer, they want to actually use data and analytics to have a better understanding
of their customer base, to enhance the customer experience while consuming media contents, of course. But of course, also to provide
a hyper personalized set of contents for those customer or for types of customer,
cohorts of customers, right? But also the data is used
to acquire new customer, for example, by doing
specific advertising, specific targeted
advertising based on the data that we can collect together. But it's not just about
these six main areas is of course about talking on the impact of generative AI in the media
and entertainment industry. You see here, five main
and common use cases of Generative AI applied
to media and entertainment, archival restoration, enhanced
broadcasting, localization. Very important of course
for market penetration. You create a content
for a specific language and a specific geography, and then you want to
penetrate other markets by doing automatic dubbing or automatic closed caption,
for example. Very classic. We already talk about
hyper personalization, but there's one more thing which is video semantic understanding, something that I really
like to talk about. So understanding the semantic
meaning of the video content. So then I can search using semantic search and I can create new contents based on what I already created
in the past for repurpose, for example, for social
media and social channels. We will see some of these use
cases together with David. So without any further ado,
I would like to ask David to join me on stage to show
the MediaCopilot from Cires21. - Thank you, Stefano. Hi, everyone. Cires21 started its business
almost 20 years ago. We are a company very focused on providing live
streaming services in Spain or my clients are broadcasters. And two years ago, we started to develop our own AI pipelines. As we work with our customers, with our clients very close, we know very well their workflows. So we noticed that they were
using different applications with a very fragmented
ecosystem of applications for their regular operations. This caused low content
delivery and high cost. And there was a lot of
duplicated work even. So that's why we decided
to develop MediaCopilot. MediaCopilot is unified platform that integrates lot of different
capabilities of AI models. It's orchestrated by agents. It offers faster content
delivery and lower cost. So let me dive into the
details of the architecture. This is a classic serverless architecture. We decided to go serverless because it's a much faster time to market and it offers reliability and scalability. So the API is Lambda, API gateway, we use step
functions as the core of orchestrator of all the
workflows of MediaCopilot. We also use SageMaker. We'll talk about SageMaker later. Amazon Cognito that
offers us the capability to offer two-factor
authentications, single sign-on, and also Amazon CloudFront, an S3 that offers not only delivery
or worldwide delivery, but also content protection. So one of the main reasons why we chose AWS was media services. Media services offer us the services that we need to transcode video. So we use MediaConvert, for instance, to transcode all the assets
that have been unlocked by our clients to seam up,
to send the video to the rest of the AI models. And we use media live and media package to receive live feeds. And we use harvest jobs to, to do live clipping of the live feed. On top of this, we have
developed a video editor that is quite useful for
live clipping creation and it's also add the possibility to add subtitling and branding
and styling capabilities. So as I said previously, we
have developed AI pipelines. So we have custom automatic
speed recognition models. We have voice activity detectors, diarization, scene detection. We don't only process
audio but also video. And we use also Amazon Bedrock to create more complex metadata
like subtitles, highlights, summaries, things like that. All the capabilities of
MediaCopilot are available through the API. In most of our clients use
the API instead of the UI because they integrate MediaCopilot into their system
workflow, into their CMS, into their media asset management or their live clipping service. So here, MediaCopilot act
as a AI layer for them. And two months ago, more or less, we started to develop
agents for MediaCopilot. Fortunately, AWS released AgentCore, which is a very interesting service that offers different
services like runtime and gateway, identity,
observability, memory, which are quite interesting and very, very scalable,
very secure, extensible. So it was very suitable for us . So we started by
developing the MCP server. An MCP server basically is a server that has different tools. Tools that have capabilities that allows to connect to different elements like databases, APIs, code. The first version of the MCP server that we developed was
developed using Gateway. Gateway, this is a service that allows us to deploy an MCP server in minutes instead of hours because
you only need to provide the open API specification of your API and it automatically creates
all the tools available for applications and agents. Then we started to develop the agent. We developed the agent
with AgentCore runtime. This is very interesting
because AgentCore runtime is stateless, it handles
automatically the session. So for each session, AgentCore deploys specific resources for that session, encapsulating the context of the session. So this is critical for us
because content protection and privacy are our main rules. So this is a very cool feature. In this specific example,
the user is asking the agent to perform a complex task
like finding the best moment or the most viral moment of an interview. Create vertical clip for social media and then burn the subtitles and export everything with the captions to external metadata automatically. So this is one simple example of what the agent can do. We also use memory. Memory is a service of AgentCore that provides short term
memory and long term memory. Very useful to recover all
the context of past sessions. And we use long-term memory to store preferences of the user so the agent can learn from the user, what are the preferences
in terms of styling or in terms of text generation. Observability is also a very
important service for us because it allows us to monitor everything that is happening in
sessions of the agent. So we can identify bottlenecks or we can optimize the workflow. And the lessons we have learned so far. Developing MediaCopilot
has been very challenging. One of the lessons that we learned is that it's quite important to select the right deployment model in SageMaker. SageMaker offers different
deployment models. We are using a synchronous
inference endpoint that is very good for VOD,
but it is not enough for live. For live, you need to
use real-time serverless or serverless service. We are starting to integrate
segmented video processing because if you can segment your video and process the different segment, you can run everything in parallel and reduce the time of the inferences and serverless was key for
us, as I said previously. So next steps, real-time
processing for life so we can make decision
while life is happening. We are starting to develop
specialized AI agents. We find that as you use
less tools in your agents, then you can save more
tokens in the elements. So more agents with specialized
capabilities are better. And we are also integrating new models, especially visual model to
add more context to the agent. And that's all. Thank you.
---
video_id: keGFISzeSXw
video_url: https://www.youtube.com/watch?v=keGFISzeSXw
is_generated: False
is_translatable: True
---

- Hi everyone. A very nice audience here, I'm super happy to present. So my name is Aza. I flew 16 hours all the
way from Tokyo, Japan to do this presentation for you, about our product, about our startup and what kind of amazing
technology we're building. Okay? So um, the title as you can see, is "How to build an AI Engine to generate "near real time insights
for videos at scale." Which means our company's building next generation search engine, AI based search engine for large scale video data sets. So we provide a search engine, you can search for anything
in the video content you want. Alright, so I'll go into
details in a moment. Cool. So let's start with the problem. What kind of problem we're trying to solve with our technology first. So as you know at the moment, the world is being recorded every time. So I see several cameras, everyone's recording me at the moment. That's also a video, right? But they unfortunately,
all this recorded video gets stored and never analyzed, right? So if you look at the
whole entire internet data, more than 80% of the data is video. And then enterprises have like
from three to eight petabytes of data stored, never analyzed. So we call it the "dark data." About 90% of the data
never is analyzed for on the, on the video content, right? So we call it like the "dark data crisis." And the main problem why,
it's the, it's the case is that current technology
does not really allow in a cheap and accurate way to analyze the video content
and make it searchable. The problem is this basically the technology is not there yet and my company is trying
to solve this problem for large enterprises, basically make this data searchable, analyzable. So there's interesting concept here, like if you look into this
is from points to lines. So I'll explain this concept. So currently you have bunch AI models that actually allow to
do basic understanding. You can do object detection,
you can do face detection, you can do like some point to point understanding of the video. But what we're trying to
build is basically lines, meaning we would like
to understand the video through the time, understand the causes or
like this causal relationship between events within the video, and then provide kind
of a general story of what happened in the video, right? So basically we're providing this next level of understanding human level of understanding
for video content. And in order to achieve
this is we are, you know, currently developing our foundational video understanding model that will have these four
different capabilities. One is basically the
"Causal Event Reasoning." I'll explain it a bit later. That tells like the, the under- the, the answers the question
why inside the video. So we'll see the example soon. Then "Omnimodal Retrieval",
what it means is that most of the currently
available technologies allow you to search
through the visual elements or separately on the audio. What we're building is
basically we're combining every single modality of
the video into single space and make the entire video searchable. Then the other thing is the
"Precise Temporal Grounding." What it means is that we
can actually understand the time nature of the
video content as well. We can search through a specific moment for specific events in the
video with the natural language. And lastly, because you know, you can't really solve these hard problems like hard questions with just simple like clip based understanding, we are trying to solve the, you know, the problem of long-context understanding. So we would like to understand not a single like 30 minutes clip, but like hours or days or weeks or even years of video content. So you can ask and understand, like ask any questions you want. So let's go one by one. So for the causal event
reasoning, so here's an example. Imagine you have a security camera, right? And then you know, record it and then you saw a
person running somewhere, but you don't really know the reason. Now, unless you go back in time and watch the video yourself, you wouldn't understand
why this person is running. But now you can ask a question, "Hey, you know why this
person is running?" Then our video understanding
model will actually reason about the past events and provide you the exact answer, alright? So that's what we're trying to solve. The next use case is, again,
"Precise Temporal Grounding", which means finding exact moments and providing you the answer. So what it means is, here's an example. Like let's say you have a four hours of kind of meeting
happened and eventually, you know, the person
signed a contract, right? About a year ago. Now you wanna find exact moment how the contract was
signed and what was spoken. Then you pass this video to
our system, we understand, and you can ask basically
find the exact time, the moment when the contract was signed. We can actually pull that out for that five seconds when
the contract is signed and you can actually understand specifically that moment, right? So that kind of capability
we're currently building. Then the next one is
"Omnimodal Retrieval", which is also a very
interesting kind of use case, which is, you know, the video is not only
the the images, right? It's like basically frames
plus you have a text, you have, you have a audio as well, and many things contained in a single, you know, the data point. Now what we're trying to do is basically we're trying to combine
all different modalities into single space and make it searchable. So for example, you
might search, like again, if you have like some, an
accident at in your home or in your facility and you wanna find an incident where glass break sound happened and it coincides with a person running, which means the model needs
to have a good understanding of the audio as well as the visual nature in the video content, right? So we basically combine
all of this, you know, capabilities and find your exact moments in the video content. And then lastly, um the
"Long-Context Understanding", basically understanding as long
as lengthy video as possible is, you know, one of the use
cases could be the security. For example, forensic research. Imagine you have a, you
know, you are a police and you would like to find a- a suspect and you basically get a footage
from all across the city and you have like, you know,
hundreds of hours of footage and you would like to basically track the, the suspect across all
different camera angles, right? Now, because we provide this kind of long context understanding the, the, the model can actually memorize what happened across all
the time, all the events, and you can actually ask questions like track suspect whatever, across 12 cameras over the six hours. Then we can actually, you know, scan through all the video content and provide you exact
moments when that person or when that suspect was
running around, right? So these are the four capabilities that is we say is like next level, next generation video search engine that the enterprises need at the moment. Now, we actually developed
initial, you know, the technology and infrastructure and we deployed in Japan for
a very specific use case. I mean we are the Japanese startup and you know, we deployed for
one of the use cases in Japan, which is the TV broadcasting. So current, we're tracking
all TV broadcasting in Japan and make it everything searchable. So you can search for
products, brands, locations, you know, names, phone
numbers on the video content that you know, that is
broadcasted on TV, right? So that's one of the use cases. And then from there you
can summarize the video, you can basically extract the sentiments, uh you can, you know, the segment stuff, you can
track certain events, et cetera. So that's what we're doing for
our customers at the moment, utilizing this technology. Then after discussing to
so many different customers in different industries, we found out that this
technology is extremely useful not only for TV broadcasting, but like for security, for manufacturing, for retail, et cetera. So in order to adjust our base model for different kinds of use cases, we're building what we call fine tuning or like, you know, adaptation factory. We have our base model that
we can actually fine tune through different kinds
of use cases quickly that should be able to
provide kind of the best model for that specific use case in the video understanding space, right? So that's what we're basically
currently developing as well. And then some of the use
cases that we're, you know, considering at the moment and also working with the customers is apart from the, you know, the
TV broadcasting and media is retail intelligence to
be able to understand like shopper's journey within
the retail space, right? So that through the
video we can understand pretty much all the user behavior. Then the manufacturing,
the quality control, the safety control, the
product productivity control, et cetera. So we're actually, you know,
experimenting at the moment. And then the last piece is security. I mean the, the most obvious use case, which is based on
forensic research, right? And how we are actually doing that is we are partnering with AWS to utilize all available
technologies, right? We're mainly using currently
the ParallelCluster to train our models
using Slurm and you know, the S3 and EC2 and different
kinds of like environment. We are also deploying, I mean, you know, utilizing different kinds
of Nvidia GPUs, right? The H100, L40S, B200, et cetera. So Amazon environ- ecosystems is kind of providing this kind of technology for us. And of course we store a lot of data terabytes and terabytes, maybe
close to petabyte of data to actually train this
kind of model, right? Then we use, you know,
the, the S3 bucket, FSX to actually mount into the AWS clusters and actually train our models, right? So this is the ecosystem that
we are currently building and as you know, for the
enterprise customers specifically, the, the quality, the
trust, the robustness and security really matters. And since we are a bit tiny startup, we're really growing fast in the next upcoming quarters, we're gonna basically clear the SOC2, you know, security clearance. And then at the same time we're
developing this, you know, the application that contains our model that you can deploy on our secure, on your secure environment so that we don't really see your data at all. You can actually analyze,
query your video content with our technology, right? Yeah, that's pretty much it,
and if you have any, you know, use cases, any, you know,
the customers, et cetera, I would love to kind of talk and discuss about different use cases. So, you know, feel free
to scan this QR code. We have a nice website or like just, you know, feel free to reach us out at info@infinimind.io and we're happy to answer your,
any, any of your questions and you know, do some kind
of experimentation with you. Yeah, so unlock your
in intel- intelligence in your video data. We're happy to, to support
you on this journey. Thank you so much.
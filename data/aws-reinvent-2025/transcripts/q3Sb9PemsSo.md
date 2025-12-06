---
video_id: q3Sb9PemsSo
video_url: https://www.youtube.com/watch?v=q3Sb9PemsSo
title: AWS re:Invent 2025 - Keynote with CEO Matt Garman
author: AWS Events
published_date: 2025-12-02
length_minutes: 128.12
views: 47367
description: "Join AWS CEO Matt Garman to hear how AWS is innovating across every aspect of the world’s leading cloud. He explores how we are reinventing foundational building blocks as well as developing brand new experiences, all to empower customers and partners with what they need to build a better future.  Kiro for Startups: https://kiro.dev/startups/  2:51 Welcome & Opening 15:56 LAUNCH: P6e-GB300 (GA) 17:43 LAUNCH: AWS AI Factories (GA) 22:32 LAUNCH: Amazon EC2 Trn3 Ultraservers (Preview) 25:10 LAUNCH:..."
keywords: AWS, Amazon Web Services, AWS Cloud, Amazon Cloud, AWS re:Invent, AWS Summit, AWS re:Inforce, AWS reInforce, AWS reInvent, AWS Events
is_generated: False
is_translatable: True
---

(bright energetic music) (crowd cheering) (vehicles whirring) (bright energetic music swells) - [Narrator] Please welcome
(audience applauds and cheers) the CEO of AWS, Matt Garman. (bright energetic music) - Welcome, everyone, to
the 14th Annual re:Invent. It's so awesome to be here. We have over 60,000 people
here with us in person, and almost 2 million watching online, including a bunch of
you that are joining us from "Fortnite" out there It's where we're streaming the
keynote for the first time. Welcome to everybody. And thank you all for joining us. It is incredible to feel the energy as you walk through the
halls here in Las Vegas, and it matches a lot of what
I've been seeing recently as I've been talking to
you in recent months. It has been an unbelievable year. AWS has grown to be a $132 billion business, accelerating 20% year over year. I wanna put this a little
bit in perspective. The amount we grew in the last year alone, it's about $22 billion, that absolute growth
over the last 12 months is larger than the annual revenue of more than half of the Fortune 500, and that growth is coming
from across the business. S3 continues to grow, with customers storing more
than 500 trillion objects, hundreds of exabytes of data, and everyday averaging over
200 million requests a second. For the third year in a row, more than half of the CPU capacity that we've added to the AWS
Cloud comes from Graviton. We have millions of customers
using our database services, and Amazon Bedrock is
now powering AI inference for more than 100,000
companies around the world. This year, we gave you
the first building blocks for deploying and operating
highly capable agents securely at enterprise scale
with Bedrock AgentCore, and we're seeing incredibly
strong momentum from AgentCore. In fact, just a few months since launch, the AgentCore SDK has
already been downloaded more than 2 million times. And we announced Ocelot, our first quantum
computing chip prototype. Ocelot is a breakthrough in
making quantum a reality, reducing the costs of implementing a quantum error correction
by more than 90%. Now, all of this starts with a foundation of secure, available, and resilient planet-scale infrastructure that is frankly unmatched anywhere. AWS has by far the largest
and most broadly deployed AI cloud infrastructure
anywhere in the world. Our global network of data
centers spans 38 regions, 120 availability zones, and we've already announced
plans for three more regions. In fact, in the last year alone, we've added 3.8 gigawatts
of data center capacity, more than anyone in the world. And we have the world's
largest private network, which has increased 50%
over the last 12 months to now be more than 9 million kilometers of terrestrial and subsea cable. That's enough optical cabling to reach from the Earth to the
moon and back over 11 times. But at Amazon, everything
starts with the customer. So I wanna start off
by thanking all of you. Today, we have millions of customers running every imaginable use case, the largest enterprises in the world across every single industry and vertical running their businesses on us. You've transformed industries
like financial services, healthcare, media entertainment,
telecommunication, even government agencies
all around the world. And as you all know, at AWS, security is priority one. For us, everything is
built on that foundation. This is the reason why the
U.S. Intelligence Community has chosen AWS as its cloud of choice for more than a decade. It's why companies like Nasdaq have moved their trading markets to AWS and why Pfizer chose AWS as their core for their
digital transformation. And since the beginning, we've known how important partners would
be to our customer success. That's why we're so proud to have such a massive
network of partners. Many of them are here with us this week. Thank you to all of our partners, SaaS providers, system integrators,
and solution providers, serving our massive set of
customers all around the world. We couldn't do it without you. And while I personally
appreciate all of our customers, I will tell you that I
have a special affinity for our startup customers. More unicorn startups
have been built on AWS than anywhere else, and
it isn't even close. Thank you to all of you,
the innovators out there. More than ever, every startup, and AI
startups in particular, are flocking to AWS. 85% of the Forbes 2025 AI 50, 85% of the CNBC Disruptor 50 are all running on AWS. It's incredibly amazing,
and I'm personally amazed at what these founders are inventing, and I thought you all might like to hear from some of them today. Let's hear from the first, AudioShake, who was the winner of last year's re:Invent
Unicorn Tank pitch competition. - [Jessica] Let's take a rainforest. Or a playground. Or no, better yet, three
musicians on a street corner. Okay, what if we could
just isolate the music? Now, the car driving by.
(gravel crunching) Or just the conversation going on between the people in the background. (people chattering faintly) - [Person] Wait, where's our car? - At AudioShake, we separate sound so that humans and machines can access it, make sense of it, and understand it in
all kinds of new ways. Our multi-speaker separator, which is the world's first
high-resolution separator of speakers into different streams. So it could be isolating individual voices in environments like call centers. We're also used across
media and entertainment. But if we think about hearing and speaking impairments, there's a lot that sound
separation can do to help. We work with some nonprofits
that work in the ALS space where they're using old
recordings of their patients, separating the voices so
that then it can be cloned and the patient can speak
with their original voice before the voice started to degrade. When we first started, we
were a three-person team. Having the infrastructure to actually get our models in the hands of real
customers is something that we couldn't have done without AWS. We run our entire
production pipeline on AWS, so everything from inference and storage through to job orchestration
and all of production. We are moving into a world where sound should be
a lot more customizable than it is today. Eventually, sound separation
should be able to help people who have hearing challenges to hear the way they want to hear, while also simultaneously going deeper into helping machines make
sense of the real world. (audience applauds) - Very cool. And thank you to the
AudioShake team for sharing. Now, none of what we do at AWS happens without builders,
and specifically developers. AWS has always been
passionate about developers, and this conference is, and frankly it always has
been, a learning conference. It's a little bit different, and it's dedicated to
all of you out there. Thank you to every developer out there and the millions of additional AWS developers
all around the world. A special call out to
our AWS Heroes over here. I see you. Thank you so much. Awesome.
(audience cheers and applauds) And thank you also to
the million-plus members of our user group community in 129 countries all around the world. (audience cheers and applauds) So why do we do this? What motivates us? Why are we just as passionate today as we were 20 years ago
when we first launched AWS? What drives us every day is giving you all the freedom to invent. This has been our motivation since when we started
AWS, the very beginning. We wanted to make it
possible for every developer or inventor in her dorm room or garage to access the technology
infrastructure and capabilities so that they could build
whatever they could imagine. 20 years ago, it just wasn't possible
for developers or builders to get the servers or compute
capacity that they needed without investing
significant capital and time. Developers were spending
way too much of their time procuring servers,
managing infrastructure, and not enough of that time building. We've actually felt this
ourselves inside of Amazon. We had a company full of builders who had these incredible ideas of how they could make our
customers' lives better, but they couldn't move
as fast as they wanted. So we asked ourselves, why not? Why couldn't developers focus on building instead of on infrastructure? Why couldn't we bring the time and the cost of
experimentation down to zero? Why not make every idea possible? And we've spent the last two decades innovating towards those goals. Giving all of you the freedom to keep inventing is why we're here today. And right now, we're witnessing an explosion of invention with AI. Every single customer experience, every single company, frankly, every single industry
is in the process right now of being reinvented, and we're still in the early days of what AI is gonna deliver, and the technology is iterating faster than anything any of us
have ever witnessed before. It wasn't that long ago
that we were all testing and experimenting with chatbots, and now it seems like there's
something new every day. But when I speak to customers and many of you out there, you haven't yet seen the returns that match up to the promise of AI. The true value of AI has
not yet been unlocked, but a lot of that is changing fast too. AI assistants are starting
to give way to AI agents that can perform tasks and
automate on your behalf. This is where we're starting to see material business returns
from your AI investments. I believe that the advent of AI agents has brought us to an inflection
point in AI's trajectory. It's turning from a technical wonder into something that
delivers us real value. This change is gonna have as
much impact on your business as the internet or the cloud. I believe that in the
future, there's gonna be billions of agents inside of every company and across every imaginable field. Already, we see agents accelerating
healthcare discoveries, improving customer service, making payroll processing more efficient, and agents are also starting
to scale people's impact up by 10x in some cases so they have more time to invent more. Wouldn't it be awesome
if everyone could see that level of impact? We think so, and that's why
we ask the question, why not? Getting to a future of billions of agents where every organization
is getting real-world value and results from AI is gonna require us to push the limits of what's possible with
the infrastructure. We're gonna have to
invent new building blocks for agentic systems and applications. We wanna reimagine every single process and the way that all of us work. At AWS, we've been innovating
at all of the layers of the stack to give you all the freedom to invent what's next. We have a lot to share. Let's get started. First off, what are the
components that you need to deliver agents that are gonna truly
deliver value for you? It starts with having the most scalable and powerful AI infrastructure
to power everything. You have to have a highly
scalable and secure cloud that delivers the
absolute best performance for your AI workloads, and you're gonna want it
at the lowest possible cost across your model training and
customization and inference. Now, that's quite easy to say, but to deliver that requires optimizing across every single layer
of hardware and software, and that is something that only AWS does. It turns out there are no shortcuts. Now, when you think
about AI infrastructure, one of the first things
that comes to mind is GPUs, and AWS is by far the best
place to run Nvidia GPUs. We were actually the first offer
in Nvidia GPUs in the cloud and we've been collaborating
together with Nvidia for over 15 years. And what that means is that we've learned to operate GPUs at scale. In fact, if you talk to anyone who's run large GPU clusters
at any other provider, they'll tell you that AWS
is by far the most stable at running A GPU cluster. We're much better at
avoiding node failures and definitely deliver
the best reliability. And the reason for that is
because we sweat the details. Minor things like debugging
bios to prevent GPU reboots. If you go to other places,
they just kind of accept that as how it works, and it's just you go
on about your business. Not us. We'll investigate and root-cause
every single one of them. And then we collaborate
with our partners in Nvidia to make sure that we're
making constant improvements. Nothing is too small
for us to be focused on. Those details really matter, and it's why we lead the
industry in GPU reliability. It takes hard work and real
engineering to make that happen. And we improve on those new dimensions
with every generation. This year, we launched our P6
generation of EC2 instances, featuring the Nvidia Blackwell processor, the P6e GB 200 UltraServer, which provides over 20x the compute compared to our previous P5en generation. These are ideal for
customers that are working with really large AI models out there. And we're doing that again today. I'm excited to announce the new P6e-GB300. (audience applauds) These are powered by Nvidia's
latest GB300 NVL72 systems, and we continue to bring you
the best-in-class compute for the most demanding AI workloads. Our full stack approach
to hardware and software plus operational rigor delivers you the absolute best
performance and reliability for the biggest
organizations in the world. This includes Nvidia
themselves, by the way, who run their large-scale
Gen AI cluster project, Ceiba, on AWS, and many others like OpenAI who are actively running on AWS today. They're using clusters of EC2 UltraServers with hundreds of thousands of chips, today, GB200s and soon GB300s, and they have the ability to scale to more than tens of millions of CPUs to manage their agentic workflows. All of this is to support
their ChatGPT application, which I'm sure many of you use, as well as the training of
their next-generation models. Or take Humain. Humain is Saudi Arabia's
newly created company that's responsible for driving
AI innovation in the region. We recently announced
a partnership together on this groundbreaking AI zone for the Kingdom of Saudi Arabia. This partnership will bring customers high-performing infrastructure, models, AI services like SageMaker and Bedrock, all while helping meet
the kingdom's standards for security, privacy, and
responsible AI standards. Now, this type of work has
sparked some interest in others, large government organizations
in the public sector who are interested in a similar concept. And so we sat back and asked ourselves, "Could we deliver this type of AI zone to a broader set of customers, maybe even something that could leverage customers'
existing data centers?" And that's why today, we're excited to announce AWS AI Factories. (audience applauds) With this launch, we're enabling customers to deploy dedicated AI
infrastructure for AWS in their own data centers for exclusive use for them. Effectively, AWS AI Factories operate like a private AWS region, letting customers leverage
their own data center space and power capacity that
they've already acquired. We also give them access to leading AWS AI
infrastructure and services, including the very latest
in training of UltraServers or Nvidia GPUs and access to services
like SageMaker and Bedrock. The AI Factories operate
exclusively for each customer, and it helps with that separation, maintaining the security and reliability that you get from AWS while also meeting stringent compliance and sovereignty requirements. We're super excited to see what these AI Factories
unlock for customers. Now, at AWS, we have
always been about choice, and if you want to have the absolute best in AI infrastructure, you need to have the best compute for AI training and inference. And AWS is by far leading the way with the broadest set of options, including our groundbreaking
purpose-built AI processors. AWS Trainium is our custom AI chip designed to offer the
best price performance for AI workloads. Now, customers love Trainium for what it achieves for
the training workloads, but I'm gonna have to pause and be a little bit
vocally self-critical here. People often give us a little bit of a hard time
about product naming in AWS. No, no, it's true. Well, it turns out
Trainium is no exception. We named it Trainium 'cause it's designed to be an
awesome chip for AI training. And it is, but as it turns out, Trainium2 is actually the
best systems in the world currently for inference. Customers often ask me, "How can I best take advantage of the benefits of Trainium?" And what I tell 'em is, "You probably are already using it and you just didn't know it." In fact, if you look at all the inference that's running in Amazon Bedrock today, the majority is actually
powered by Trainium already, and the performance advantage of Trainium is really noticeable. If you're using any of Claude's latest
generation models in Bedrock, all of that traffic is
running on Trainium, which is delivering the best
end-to-end response times compared to any other major provider. And that's part of the reason why we've deployed over
1 million Trainium chips already to date. Now, we've gotten to a
million chips in record speed, and that's because the whole process, we control the whole stack. We can optimize end to
end how we roll it out and it allows us to move even faster. In fact, we've been
able to ramp the volumes of Trainium2 in our data center 4x faster than the next fastest AI chip we've ever ramped, and we're selling those as
fast as we can make them. Trainium already represents a multi-billion dollar business today and continues to grow really rapidly. Now, what does it look like when all of this comes
together in a system purpose-built around Trainium? It wasn't that long ago
that people had this saying where they said that the data
center was the new computer. Well, when you're training
this next generation of models, it turns out that the data center campus is the new computer. One of the best models in the world today is Anthropic's Claude. We wanted to give you
a little bit of a look behind the scenes at how a model like this is born, made possible by Trainium
and Project Rainier. Let's take a look. (upbeat dramatic music) (audience applauds) Really cool to see the massive scale that we've got to with
Trainium so quickly. So what's next? Last year, we announced that we were already hard
at work on our next chip, Trainium3, designed to make AI workloads better, faster, and more cost effective. Today, I'm excited to announce that Trainium3 UltraServers
are now generally available. (audience applauds) Now, these UltraServers
are our most advanced, containing the very first
three-nanometer AI chip in the AWS Cloud. Trainium3 offers the industry's
best price performance for large-scale AI training and inference. Now, we've talked about
the incredible results that we've seen with
Trainium2 this past year, but Trainium3 UltraServers
bring another huge leap forward. 4.4x more compute, 3.9 times the memory bandwidth, and this one is super important, five times more AI tokens
per megawatt of power. And as a special surprise, I have a rack of our UltraServers
on stage with me today. (audience cheers and applauds) Our largest Trn3 UltraServers combine 144 total Trainium3 chips acting together in a
single scale-up domain connected by custom neuron switches. This delivers a massive 362
FP8 petaflops of compute over 700 terabytes per second of aggregate bandwidth, and all in a single compute instance. And our custom-built EFA networks support scaling these out to clusters of hundreds
of thousands of chips. No one else can deliver this for you. It requires all of these
system-level pieces to be co-designed together. It requires multiple
types of custom silicon. It requires scale-up and
scale-out networking. It requires a detailed and
integrated software stack, and of course, the industry's
leading data centers. In a real-world example of
how performance improves, we ran through a number
of open-source models, open-weights models, that we've been optimized
to run on Trainium2 and we wanted to see how
they'd run on Trainium3. As one example, here's an inference benchmark for a popular open-source
gpt-oss-120b model from OpenAI, and we ran it on both
Trainium2 and Trainium3. As you see here, with Trn3, we get remarkable efficiency
gains over Trainium2. You see over 5x higher
output tokens per megawatt, all while maintaining the
same latency per user, what we call interactivity
in this chart here. And this is just one example. We see similar results as we run this across a number of different
models, which is fantastic. We're excited to see what Trn3 is gonna unlock for customers, but we're also not stopping there. I wanted to give you a bit of sneak peek as to what's coming around the corner. And that's why I'm excited to announce that we're already hard
at work on Trainium4. (audience applauds) We're well into designing it, and we're excited about
what we're seeing already. Trainium4 is gonna bring massive leaps across every single dimension. Compared to Trainium3, Trainium4 will deliver six times the FP4 compute performance, four times more memory bandwidth, two times more high
memory bandwidth capacity to support the very largest models that you have in the world. Trainium continues to push
the bounds of what's possible with AI infrastructure, so you all can be freed to push the bounds of your industry. Let's hear from a startup that's using AWS's
massive AI infrastructure to transform computational biology. - We're trying to create a kind of beautiful mind for science that can be a polymath across fields, material science, chemistry, and life, but the internet and prior
data only take you so far. You have to be capable of
testing things in the real world. Lila is building the first of what we call AI science factories, which are an infrastructure through which AI can
autonomously propose hypotheses, design experiments, and
then run those experiments in the real world with all of the results of
the successes and failures flowing into wireless models, and become super intelligent within them by running the scientific method itself. It won't surprise anybody that building scientific superintelligence requires a lot of computing. Lila is at trillions of tokens of scientific reasoning today. We expect that to go up by no less than 100x
over the next few years. AWS is an incredible partner because as the scale and
speed and intelligence of science goes up, the scale, speed of computing and the security of that process is gonna be more important than ever. AWS is the best in the
world at that combination. What this means for humankind is that building a very broad,
new kind of scientific mind and infrastructure that can
scalably set that mind in motion to find cures, new energy technologies, new materials, and more, that we can collectively pull a better future into the present. (audience applauds) - Really amazing to see what this scale of compute is enabling for customers like Lila
be able to accomplish. It's just incredible invention that's happening at the
infrastructure layer. But we also know that infrastructure is just a part of the story. We're seeing nearly
every single application in the world be it reinvented by AI, and we're moving to a future where inference is such an integral part of every single application
that everyone builds. Now, to be successful in that future, you need a secure, scalable,
feature-rich inference platform that you all can build on, and that's why we
developed Amazon Bedrock. Bedrock is a comprehensive platform that helps you fast-track your
generative AI applications as you move from
prototype into production. With Bedrock, you get a broad choice of all the latest models. You have the ability to
customize these models for your individual use case
and your performance needs. You get the tools to
integrate them into your data and the capabilities to add
guardrails as you need 'em. All of this with the security and integrations that make it
easy to build on applications and data that you already have in AWS. And companies of every size and in every industry all around the world are using Bedrock. Customers like BMW, GoDaddy, Strava, those are just a few, with more than twice as many
customers building on Bedrock compared to just this time last year. Bedrock is seeing unprecedented momentum, but it's not just the number
of customers that are using it, it's actually the volume of the usage that's quite astounding. In fact, some customers are processing a huge number of requests through Bedrock. Today, some of the
largest-scale AI applications in the world all run on this platform. I actually asked the team to check for me, we now how have over 50 customers that have processed more
than 1 trillion tokens each through Bedrock. Incredible scale and momentum. Now, when you all start
building a Gen AI application, the very first thing you likely decide on is which model are you gonna use. Which is the one that
gives you the best cost, the lowest latency? What's gonna give you the best answers? And a lot of times, actually, the right answer is a
mix of different models for your applications or your agents, which is why we think model
choice is so critical. We've never believed that there was gonna be
one model to rule them all, but rather that there would be a ton of great models out there, and it's why we've continued to rapidly build upon an already
wide selection of models. We have open-weights models
and proprietary models, general purpose or specialized ones, we have really large
ones and small models, and we've nearly doubled
the number of models that we offer in Bedrock
over the last year. Today, I'm pleased to announce that we're introducing a whole host of new open-weights models. (audience cheers and applauds) These models include
ones like Google's Gemma, MiniMax M2, and Nvidia's Nemotron, and today, we have a couple of new models that are debuting to the
world for the very first time. I'm excited to announce
that today from Mistral AI and available immediately on Bedrock are two new sets of open-weights models. (audience applauds) The first is Mistral Large, which is a big leap forward
from their Large 2 model doubling the context window size and vastly increasing the
number of model parameters by more than five times. We're also launching today Ministral 3, which is a cool set of three models that offer really great
deployment flexibility for ultra-efficient edge devices
or single GPU deployments or advanced local operations. It's gonna be super fun
to see how you all use all of these open-weights models. Now, in addition to
providing a huge selection of third-party models on Bedrock, last year we announced Amazon Nova, which is Amazon's family
of foundation models, delivering the industry's
best price performance for many workloads out there. Over the last year, we've
actually extended the Nova family to support more use cases and deliver more possibilities for you that deliver real value. We've unlocked speech-to-speech
use cases as an example with Amazon's Sonic, and just a few weeks ago, we launched the industry's
best-performing model for creating embeddings
across multiple modalities with Nova's Multimodal Embeddings. And the momentum has
been really fantastic. Nova has grown to be used by tens of thousands of customers today, everyone from marketing giants like dentsu to tech leaders like Infosys
or Blue Origin or Robinhood to innovative startups like Ninja Tech AI. And today, we're making Nova even better, announcing a new generation
of Nova with Nova 2. (audience applauds) Nova 2 delivers cost-optimized
low-latency models with frontier-level intelligence. The Nova 2 family includes Nova 2 Lite, which is our fast and
cost-effective reasoning model suitable for broad set of workloads, and Nova 2 Pro, which is our most
intelligent reasoning model for highly complex workloads. We're also introducing Nova 2 Sonic, which is our next generation
speech-to-speech model that enables real-time,
human-like conversational AI for all of your applications. Now, Nova 2 Lite delivers
incredible price performance for many workloads that we
actually see our customers wanting to deliver in production. Nova 2 Lite compares really favorably in industry benchmarks to
models like Claude Haiku 4.5, GPT-5 mini, and Gemini Flash 2.5. In particular, Nova 2 Lite excels at things like instruction calling, following tool calling, generating code, and extracting information from documents, often matching or
exceeding the performance that we see from these comparable models at an industry-leading cost performance. We think that Nova 2 Lite
is gonna be a real workhorse and is gonna be really
popular for a wide variety of your use cases out there. Nova 2 Pro is our most
intelligent reasoning model, and it's gonna be great for when you have those really complex workloads. In particular, we look
at really important areas where you need your agents to be great, and that's where Nova 2 Pro really shines, where skills like instruction following and agentic tool use are critical. In fact, for those, Nova 2 is
frequently coming out on top. And if you look at artificial
analysis benchmarks in those areas, Nova 2 Pro
delivers better absolute results compared to leading models like GPT 5.1, Gemini 3 Pro, and Claude 4.5 Sonnet. And for applications that
need voice capabilities, Nova 2 Sonic offers industry-leading conversational quality at awesome price performance. With improved latency and significantly
expanded language support, we think you're gonna love it. Now, I also have one more Nova model that I want to talk about that has a unique set of capabilities. Now, today's models out
there are actually quite good at reasoning across one type of modality. Say they're looking at an image or listening to audio or outputting text and then maybe outputting
in a different modality, say they may be reading texts
and then creating an image. But in the real world, you have to understand multiple
modalities at the same time. Take for example this keynote. If you wanted a model to try to understand all that was going on
in the keynote today, you'd want to get the nuance and understanding of
everything that we're saying. That means you'd have to
listen to what I'm saying, you'd have to understand the
contents of all these slides, you'd have to be able to watch the videos and understand what's going
on and what we're showing. Now, let's say you want
to take that same model and produce a summary
output for your sales team where it had a summary of all the launches we announced today, along with some images
and marketing material. Now, if you wanted to do
this, you could, right? This is possible today, but it means testing a wide
variety of different models, stitching them all together, and trying to accomplish this outcome, which is totally doable but is quite hard. It'd be easier if you had a single model that could do all of that, and that's why I'm excited
to announce Nova 2 Omni. (audience applauds) It's a unified model
for multimodal reasoning and image generation. Nova 2 Omni the industry's
first reasoning model that supports text, image,
video, and audio input and then supports text and
image generation output. So that's four new industry
leading models from Amazon Nova and we're just getting started. Up next, let's hear from Gradial who's building some
pretty cool capabilities with Nova and Bedrock. (bright music) - The biggest slowdown in
marketing isn't creativity. It's everything that happens after, and Gradial helps achieve that. Today, the content operations
world is fairly manual. To get from a creative
brief onto a website takes four to six weeks and involves 20 different steps that require designers, engineers, copywriters, and web strategists. And so what Gradial's done is we've connected all of those
different systems in place so that we can take it
from idea to action. Our orchestration agent
decides which subagents that it actually uses, if it's going to use the authoring agent, the Figma agent, the Sitecore agent, and it will combine each of those agents to actually get a task done, right, and actually making recommendations of how your content can convert
audiences better and faster. We will forever live
in a multi-model world. There isn't one model fits all, and so AWS Bedrock and Nova gives us the freedom to use
efficiency where we need it, use power when we need it, and use reasoning when we need it. That was crucial for us. AWS is extremely invested
in startup success, and that is very clear. I don't think that
anybody got into marketing to do a link swap. I think that folks got into
marketing to be creative. If you free up that time,
just imagine all of the things that will be created years from now. (audience applauds) - Really amazing to see what Gradial has been able to do with Bedrock. Now, the models that are available today are really incredible, and
it continues to impress me what everyone out there is
able to accomplish with them. But as these models are used to power more and more mission-critical
line-of-business applications and your agentic workloads, it turns out that the AI's ability to understand your company's data is what really starts
to deliver huge value for your company and for your customers. And I'll just pause here, I can't stress this strongly enough, your data is unique. It's what differentiates
you from the competition. And I see this over and over again. If your models have
more specific knowledge about you and your data
and your processes, you can do a lot more. Now, the wizardry here comes
when you can deeply integrate a model with your unique data and IP. But in order to do this well, it's critical that you have
your data in the cloud. So what are the best
ways to get these models to access your data? Clearly, third-party models don't start with access to your data. They don't natively know
about your business, and frankly, you wouldn't want them to, since you didn't want
your proprietary data embedded in those models so
that everyone else could use it. It's why actually the
isolation that we provide inside of Bedrock is so important to prevent your data from
leaking back to the core models. Now, the most common techniques that we see people successfully use today to combine your data with the models are things like leveraging
RAG or vector data to provide your chosen model
with context at inference time. And these are quite
effective to help your models more effectively navigate
your massive set of data and return relevant results. Usually what we see though
is this only goes so far. Almost every customer I talk to wishes that they could
somehow teach the model to really understand their data, really understand their
deep domain knowledge, the expertise, they want the model to know their expertise when
it's making its decisions. Let's take for a second, you work at a hardware company that's looking to accelerate
R&D for new products. You'd optimally want a model that understands your past products, your manufacturing preferences, your historical success and failure rates, whatever process
constraints you might have, and then you want something
that could combine all of these to provide an intelligent guidance for your design engineers. And it turns out whatever your company is, you have this incredibly
vast corpus of IP and data that would be super valuable if it was integrated
into the model you use. Now, the natural question is, why not just train a custom model? It turns out there's only really
two ways to do this today. You could build your
own model from scratch, include your own data in that. But of course, this is super expensive and frankly, you probably
don't have all of the data that you would need to build the general intelligence in the model. And then even if you did, you may not have the in-house expertise to
pre-train a frontier model anyway. So that's probably not very
practical for most companies. What most people do instead is they start with an open-weights model and you modify 'em. And there's lots of
ability to customize there. You can tune weights with techniques like fine-tuning, reinforcement learning, and you can try to build something that really focuses on your use case. However, it turns out
there's actually limits to how effective this is as well. It's really hard to teach a model a completely new domain that it wasn't already pre-trained on, and it turns out the more
you customize models, the more you add a bunch
of data in post-training, these models tend to forget some of that interesting
stuff that it learned earlier, the core reasoning. It's a little bit like humans
trying to learn new language. When you start, when you're really young, it's actually relatively easy to pick up, but when you try to learn a
new language later in life, it's actually much, much harder. Model training is kind of like this too. Now, there's been some pretty cool things done with the limit ability that you have to tune
these open weights models, but you can only go so far. Today, you just don't have a great way to get a frontier model that deeply understands
your data and your domain. But what if it was possible? What if you could integrate your data at the right time during the
training of a frontier model and then create a proprietary
model that was just for you? I think this is actually
what customers really want, and so we asked ourselves, why not? And today, I'm excited to
announce Amazon Nova Forge. (audience applauds and cheers) Nova Forge is a new
service that introduces the concept of open training models. With Nova Forge, you get exclusive access to a variety of Nova training checkpoints, and then you get the ability for you to blend in your
own proprietary data together with an
Amazon-curated training dataset at every stage of the model training. This allows you to produce a model that deeply understands your information, all without forgetting
the core information that the thing has been trained on. We call these resulting models Novellas, and then we allow you to
easily upload your Novella and run it in Bedrock. Lemme show you how this works. Let's say you're that
hardware manufacturer that we discussed earlier. You have several hundreds
of gigabytes of data, billions of tokens related to your past
designs, your failure modes, your review notes, et cetera, and you decide that you're gonna start from an 80% pre-trained
Nova 2 Lite checkpoint. Using our provided tool set, you blend all of your data in with that Amazon-curated training dataset, and then you run the provided recipes to finish pre-training that model, but this time with all
of your data included. This introduces your
domain-specific knowledge, all without losing the important
foundational capabilities of the model-like reasoning. Nova Forge also provides the ability to use remote reward functions
and reinforcement fine-tuning to further improve your model, letting you plug real-world environments into the training loop. And because your baseline model already understands your business, these post-training techniques are actually much more effective. Once you're ready, you import
this model, your Novella, into Bedrock and you run inference on it just like you would any
other Bedrock model. Now, your industrial engineers
can ask questions like, "What are the pros and cons
of design A versus design B?" and get responses that are specific to your company's historical results, manufacturing constraints,
and customer preferences. We've already been working
with a few customers to test out Nova Forge, and they're already seeing
transformative results from customizing Nova's
open training models. Let's dive a little bit into
the example with Reddit. Reddit uses Gen AI to moderate content for multiple different safety dimensions across their chats and searches. Fine-tuning existing models didn't get them the
performance they needed. They even tried using multiple models of different safety dimensions,
but it was super complex and even then, they couldn't
get the accuracy they wanted for the specific requirements
of their community. With Forge, however, Reddit
was able to integrate their own proprietary domain
data during pre-training, enabling the model to develop integrated representations that naturally combined the
general language understanding with their own
community-specific knowledge. For the first time, they
were able to produce a model that met their accuracy and
cost-efficiency targets, and at the same time, it was much easier to deploy and operate. We think this idea of open training models is gonna completely transform what companies can invent with AI. Now here to share how Sony is transforming and reinventing
their business on AWS, please welcome Chief Digital Officer and Corporate Executive Officer from Sony Group Corporation, John Kodera. (dramatic music)
(audience applauds) - Good morning. Today, I'd like to talk
to you about the word that holds a very special
place for Sony, kando. The direct translation of the
word into English is emotion, but kando means more
than that in Japanese. It captures feelings of
deep emotional connections and experiences when watching a movie, listening to music, or playing a game. For us at Sony, kando is what we strive to create and deliver to our customers in all aspects of our work. Kando is at the core of who we are. Our founders created Sony in 1946 with the dream to enrich people's lives through the power of technology, a world where technology can deliver new experiences,
lifestyles, and kando. Driven, by this vision, we have delivered innovative products, creating entirely new industries and customer experiences along the way. With each era of technology,
from analog to digital, the internet, the cloud, Sony has reinvented
itself again and again. Today, Sony is more than a
hardware technology company. We are also a leader in entertainment across games, music, pictures, anime. There is no other company
in the world like Sony with the depths of our business
portfolio and touchpoint with fans and creators. One of the most remarkable
successes this year is the anime movie "Demon Slayer: Kimetsu no
Yaiba Infinity Castle." As of late November, this film has become the highest ever grossing
Japanese film released worldwide and fifth highest grossing film across all categories in 2025. As we've done with Demon Slayer, we hope to keep delivering new kando by marrying the creator's vision with a deep understanding of their fans, and our relationship with AWS plays a pivotal role to make this happen. One example started in the early 2010s when I was president of the network service company for PlayStation and other Sony devices. We chose AWS as our provider for its global footprint, high standards in
availability, and scalability. In 2020, for the launch of PlayStation 5, we utilized AWS building blocks for our network architecture. These services allowed us to scale out at a moment's notice and accelerated our
shift to microservices, increasing deployment by 400% with the 1/10 the lead time. Today, our relationship with AWS supports safe, secure, and high-quality gaming experiences for up to 129 million gamers to connect and experience kando together. Moving forward, we see
incredible potential for growing the fam,
community-connecting fans with similar taste and interests across our diverse
portfolio of content IPs. At the same time, we also want to better
serve our creator community by providing them with
more tools, connection, and insights to their fan base. We call this the Sony Engagement Platform, creating deeper
understanding and connection between the fans who experience content and the creators who are making it. And one of the building blocks for the Engagement Platform
is the Sony Data Ocean. It utilize data insights generated from multiple
connected data lakes. built using AWS services, it enable us to process up to 760 terabyte of data from more than 500 data across Sony Group. Of course, to make the most
effective use of our data and deliver kando to our customers, we have to effectively harness the power of AI and agents to empower our employees and augment our business capabilities. To maximize our productivity
in the enterprise setting, we are actively promoting
the usage of generative AI, our home-grown enterprise LLM built using Amazon Bedrock, over 57,000 users today since its introduction two years ago, and we are serving 150,000
inference requests per day. And today, we are integrating
new agent capabilities into our platform to enable a new level of advanced operational
efficiency across our businesses. By placing Amazon Bedrock AgentCore at the center of our agentic AI system, we gained the ability to
easily govern, deploy, and manage more useful
agentic capabilities to accelerate our enterprise
AI transformation. And today, we are pleased to share that we are adopting Nova Forge to apply state-of-the-art
customized models to our unique business and operations. We fine-tuned a Nova 2.0 Lite model that outperform baseline models for tasks like reference consistency
and document grounding. We are now aiming to
increase the efficiency of Sony's compliance review and assessment processes by 100x. In addition to the enterprise setting, Sony is fully committed to the responsible and ethical development and use of AI in the creative domain. We hold ourselves against
the highest standard and respect toward the rights of creators and performers. So where are we going from here? We will continue to
create and deliver kando, fulfilling the aspirations
of both fans and creators, building meaningful
connection between them. In the future, we will continue to expand our fans' engagement with their favorite content IP across multiple entertainment genres. As we have done with "Uncharted"
and "The Last of Us," we hope to connect fans and creators in both virtual and physical environments, including location-based entertainment. Realizing our vision will require even greater and stronger
collaboration with AWS, as well as our creative
and technology partners in the audience. We look forward to creating and delivering even greater kando to our fans across the world. Thanks for listening. Thank you. (audience applauds)
(upbeat music) - Thank you so much, Kodera-san. Such a great story. And just like Sony has
seen, a key to their success over the long run is having the right foundation
for that innovation. What really excites me about Sony's story is that because they have their data and their applications
in the cloud in AWS, it's that much easier for them
to deal with any uncertainty that comes their way. Not many companies have
been able to transition as successfully as Sony, from an electronics device company into a global digital media business, such a major change, and so cool to see. Having the right
technology platform in AWS has helped them on that journey. Now, when you have your data in the cloud, it turns out you can move more rapidly and you can adjust to any of those unexpected
changes that come your way. Now, the world is not slowing down. In fact, if there's one thing that I think we can all count on, it's that more change is coming. Now, one of the biggest opportunities that is gonna change
everyone's business is agents. Agents are exciting,
because they can take action and they can get things done. They can reason dynamically,
and they create workflows to solve a job in the best way without you needing to pre-program 'em. These agents work in
non-deterministic ways, which is part of what
makes them so powerful, but it also means that
the foundation and tools that got us to where we
are, building software, aren't necessarily the ones
that we need for agents. And that's why we launched
Amazon's Bedrock AgentCore, delivering the most
advanced agentic platform so that you all could build, deploy, and operate agents securely at scale. We designed AgentCore at the
same time to be comprehensive, but also modular. It has a secure serverless runtime that can deliver to agents so that agents can run in a
complete session isolation. AgentCore Memory enables
agents to keep context, handling both short- and long-term memory so that they can learn
and get better over time. We provide an AgentCore Gateway so agents can easily discover and securely connect to
tools, data, and other agents. We have AgentCore Identity that provides you a way to
do secure authentication and gives you controls
over what tools and data your agents can access. AgentCore Observability gives
you real-time visibility in the deployed agent
workflows that you have. And we have a variety
of foundational tools that allow your agents to securely execute real-world workflows. Things like Code Interpreter
that gives you access to a secure code execution environment, or our managed browser service, which provides a managed environment that makes it easy for your
agents to access the internet. AgentCore is truly
unique in what it enables for building of agents, and it's significantly different than anything else out there. And we built AgentCore
to be open and modular, so you can use it with
a variety of frameworks, things like Crew AI or
LlamaIndex, or LangChain or AWS's Strands agent. You can also use it with
any model out there, whether it's from the variety of models that we have in Bedrock or from models like OpenAI's
GPT or Gemini models. You only have to use the
building blocks that you need. We don't force you as builders to go down a single fixed path. We allow you to pick and
choose which services you want for your own situation. AgentCore also then makes it easy to deploy your agents
privately and securely inside of your Amazon VPC and then allows you to scale
to thousands of sessions to support high traffic use cases. It's also super fast and
easy to deploy your agents. Agents can be deployed in under a minute with just drag and drop
or a few lines of code. And this is part of why we're seeing so much momentum with AgentCore, as our customers rapidly adopt it as the foundation for
their agentic applications. We see it across industries, from companies like regulated industries like Visa or National
Australia Bank or Rio Tinto. We see it from ISVs like Lummi and ADP or startups like Cohere
Health and Snorkel AI. And the momentum is really accelerating. I'm gonna talk about a few of them. Adena Friedman is the CEO of Nasdaq, and she and her team are moving
really fast to build agents that can do real work in core areas of their business. Now, before AgentCore, they were planning on
dedicating a whole team to build a foundation infrastructure that they needed to reliably operate and build resilient agents to meet their very high standards. AgentCore, however, now frees
them from this heavy lifting so they can just focus
on building great agents. Bristol-Myers Squibb built a new agent that's able to evaluate more than 10,000 compounds across multiple hypotheses
in less than an hour. This is a process that used to take their researchers
four to six weeks. The company's drug discovery
agent uses AgentCore Runtime for its ability to seamlessly
and dynamically scale and to keep their sensitive
data secure and isolated. We see ISVs like Workday who are building the software
of the future on AgentCore. AgentCore's Code Interpreter delivered exactly what they needed, the essential features
and security requirements and data protection that was needed to power
their planning agent. This capability reduces the time spent on routine planning analysis by 30%, saving 'em nearly a hundred
hours of work every month. You don't have to build
your own agents either. Many companies are using AWS marketplace as the trusted place to publish and procure prebuilt agents, tools, solutions, and
professional services, and this is where AWS Partners can help you all move even faster. We're really excited what
customers have been able to do with AgentCore, but we're far from done. One big challenge that we've seen when you're building agents is how do you get them
to behave predictably and in line with your intents? What makes agents powerful is this ability to reason and act autonomously. But that also makes it hard for you to have complete confidence that your agents aren't gonna
stray way out of bounds. This is a little bit
like raising a teenager. I currently have two awesome
teenagers myself at home. Now, as your kids get older, you have to start giving them
more autonomy and freedom so that they can learn, or
adulting as they like to call it. But you also wanna put
some ground rules in place to avoid major issues. Think about when your kids start driving. This is this current
situation that I'm in. All of a sudden, the kids
have all of this autonomy. There's a ton of things that they can go and do by themselves, but you still kinda want to
have those guardrails in place, like you have to be home by a certain time or you don't want to drive more than, say, five miles an
hour over the speed limit, things like that. One way you can actually
build trust in agents is by making sure that they
have the right permissions to access your tools and your data. AgentCore Identity provides
a great way to do this today, but while permissions on your tools that your agents can
access is a good start, what you really want to be able to control is the specific actions that your agents can or
cannot take with those tools. You have actions like, what is the agent gonna
do with those tools? How can they use them? Who are the tools for? And today, customers struggle with this. You can embed policies inside
directly in your agent's code, but because agents generate and execute their own code on the fly, these safeguards are really best effort and can only provide you weak guarantees, and they're really difficult to audit. In practice, this means today you can't with certainty control what your agent does or does not do, while also giving it the agency to go and complete these
workflows on its own. As a result, most customers feel that they're blocked from
being able to deploy agents to their most valuable,
critical use cases. And today, that's why we're
announcing Policy in AgentCore. (audience applauds) Policy provides you with
real-time deterministic controls for how your agents interact with your enterprise tools and your data. Now, you can set up these
policies that can define which tools that your agents can access, but also how they access them, so whether they're APIs or
Lambda functions or MCP servers or popular third-party services
like Salesforce or Slack. And you also can then define what actions they can perform
and under what conditions. So what AgentCore does
is it then evaluates every single agent action
against this policy before ever granting access
to your tools or your data. We'll walk through a simple example. Let's say you're in AgentCore Policy, and just using natural
language, you define a policy. Say something like, "I want you to block all
refunds from customers when the reimbursement amount
is greater than $1,000." Then under the hood, what
happens is your prompt is converted to Cedar, which is a popular open-source language that's powered by our
automated reasoning work across authorization and
our verifiable systems inside of AWS. Once established, these
policies are then deployed to your AgentCore Gateway and they're evaluated in milliseconds, which ensures that all of your actions are checked instantly and consistently to keep your agent workflows
fast and responsive. And the design of where this sits is actually super important. Because this policy enforcement is outside of your
agent's application code, the policy evaluation actually
sits in between your agent and all of your data
and your APIs and tools, so you can predictably
control their behavior. Going back to our example
in the refund policy, if every agent action is
checked against your policies before the agent is able
to access the tools, so let's pretend a situation happens where a refund is over the
limit that you've defined, the agent is blocked from
now issuing that refund. Now that you have these
clear policies in place, organizations can much more deeply trust the agents that they're
building and deploying, knowing that they'll stay inside the boundaries that you've defined. Now, of course, you all need agents to do more than just
follow the explicit rules that you define. You have to know that they're
behaving in the right way. Trust, but verify is a phrase that we've kind of co-opted at Amazon as a mental model for
how you manage at scale. At AWS, we give our teams
incredible autonomy. I trust our teams to go
and invent for customers and execute on that mission. But I also have mechanisms
that allow me to dive deep and inspect when things are on track. I wanna check that our
strategic initiatives that we've identified are in fact getting done in
the way that we've intended. If I go back one more
time to our teenagers, I generally trust that
they're following the rules, but I can still check my ring camera to ensure that they got home on time, and I can always check the
status of my Life360 app to ensure that they're within
the bounds of where I expect. This same thing applies to agents. To gain confidence, you want visibility
into how they're acting. Now, customers love what they're getting with AgentCore Observability. You get real-time visibility into all your operational metrics, you can see your agent response times, you can see the computational
power that's being used and your error rates and which tools and
functions are being accessed. That's all great. But in addition to how agents
are performing operationally, there's other things that
you actually wanna know. You wanna know things like, are your agents making
the right decisions? Are they using the best tool for the job? Are their answers correct and appropriate? Are they even on brand? These are things that are
super hard to measure. Today, it usually actually requires you to have a data scientist. The data scientist is gonna build some complex data pipeline. They're gonna select a model that's gonna try to judge
the outputs of their agents. They have to build the infrastructure to serve these evaluations and then manage quotas and throttling. And each time you wanna
roll out a new agent or you want to upgrade to
a new version of a model that you're using, you have to do all of
this work all over again. But unlike traditional software, actually testing and pre-prod
here even then is really hard. You only know how your agents
are gonna react and respond when you have them out
there in the real world. That means you have to
continuously monitor and evaluate your agent
behavior in real time and then quickly react if you see 'em doing
something that you don't like. We think we can make this a lot better, Today, I'm excited to announce
AgentCore Evaluations. (audience applauds) Evaluations is a new AgentCore service that helps developers
continuously inspect the quality of their agent based
on real-world behavior. Evaluations can help you
analyze agent behavior for specific criteria,
like the ones I mentioned, correctfullness, helpfulness, harmfulness, and they come with 13 pre-built evaluators for common quality dimensions. Of course, you can always create your own custom scoring system with your own preferred
prompts and models as well. And you can easily evaluate
agents in this testing phase to correct any issues before you end up deploying them broadly. So now, if you're gonna
upgrade to a newer version of a model, as an example, you run your Evaluations
to evaluate your agent and you wanna make sure that it maintains the same level of
helpfulness, for example, that you have in your current release. You can actually also use
evaluations in production to catch any of those hard-defined
quality degradations really quickly. You'll see your results in CloudWatch right alongside your AgentCore
Observability insights. And AgentCore Evaluation automates what used to take specialized expertise and a bunch of
infrastructure heavy lifting into something that everyone can access and allows you to continually improve the quality of your agents. We're quite excited about it. All right, so this is AgentCore, the agentic platform that's powering the next wave of agents. We're helping you move quickly to get your agents into production without compromising or
making any sacrifices, which this is what we're all about. We want you to move fast so you have the broadest
set of capabilities to build for your own customers. Today, we're really excited that we've added two new
powerful capabilities in Policy and Evaluations, and I'm really excited to see how this unlocks some real
powerful production use cases. Now to tell us more about how they're building
agents of their own to transform their business and how they're using AWS as a key part of their
agentic transformation, please welcome Shantanu
Narayen, CEO and chair of Adobe. (audience applauds)
(upbeat music) (vocalist vocalizing) - Thanks, Matt. Good morning.
(audience applauds) Hello, everyone. I'm thrilled to join you at
this transformative time. We're clearly witnessing a
golden area of creativity where AI is amplifying human ingenuity and enabling people to bring
their imagination to life. Adobe has been at the
forefront of this revolution. From the invention of desktop publishing to the origins of digital documents to groundbreaking advances
in imaging and video, we're constantly pushing the
boundaries of what's possible. It was actually our transformation to a cloud-based subscription
model over a decade ago that marked the beginning
of our relationship with AWS because it was services
like Amazon's EC2 and S3 that actually provided
us with the scalable as well as secure foundation
for Adobe's innovation. As we transition into this era of AI, AWS is actually helping us innovate faster with the core services that we need, as Matt said, to train models
as well as deploy agents. And this allows us to focus
on what Adobe does best, unleashing creativity across every facet of digital experiences for our business, which span business
professionals, consumers, creators, creative professionals, as well as marketing and IT professionals. When it comes to AI for creativity, we're re-imagining every
stage of the process for people of every skill level. We do this with the knowledge
that over 90% of creators actively are using creative-focused
generative AI today. And to support them, we're infusing AI into Adobe Firefly, our all-in-one destination
for creative workflows driven by AI, in our flagship Creative Cloud
applications, like Photoshop, and in Adobe Express, the quick and easy app to
create on-brand content. It's just an example. Our Adobe Firefly model that powers capabilities
like sketch to image. text to video, generative
fill, and generative recolor have actually been trained and are using both P5 and P6 instances with all the data stored
in S3 and FSx for Lustre. These models have actually been used to generate over 29 billion assets and enable creators to create content with unmatched creative control. And our AI assistant now in Adobe Express helps users redefine
entire creative process using conversational editing. And these agentic experiences are now powered by our AI platform, and our relationship with AWS helps ensure that these agents operate efficiently and more importantly, securely. When it comes to productivity, PDF remains the way that
people consume information. Over 40 billion PDFs have been opened and
shared with Adobe Acrobat, and every year more than
18 billion PDF files are created and edited by our
customers around the world. Today, we're integrating productivity for billions of business
professionals and consumers through AI capabilities,
including an AI assistant. In August, we announced
Adobe Acrobat Studio, a first-of-its-kind platform that brings together Acrobat, Adobe Express, and AI agents to enable users like you
to work more efficiently with both structured and
unstructured information. Our collaboration with AWS
is absolutely key here, given Acrobat Studio
uses Amazon SageMaker, as well as Amazon Bedrock, to access our and third-party models, helping millions of users research, strategize, analyze, and
collaborate even faster. Adobe PDF is also a new
offering that helps consumers and business professionals now collaborate with conversational knowledge hubs that are supported by the
personalized AI assistance. And finally, in the AI era, we all know that the role of marketers has evolved to the orchestration of engaging customer experiences for their consumers and customers, to support them by
unifying the key elements of customer engagement, the content supply chain,
as well as brand visibility. Adobe Experience Platform
is the core foundation for driving this customer engagement, bringing together
AI-powered apps and agents to drive engagement and loyalty. It operates at the scale of over 35 trillion segment evaluations and more than 70 billion
profile activations per day. An experience platform runs
using AWS building blocks as well as an innovative
cellular architecture. Our joint customers can now ingest data from sources like Redshift into the Adobe experience platform to create these profiles, hydrate them, and use these audiences in Adobe's real-time
customer data platform. Key I think to this customer engagement is creating on-brand content that's delivered in the right time in the right channel at exactly the right moment, because marketers expect
that the demand for content will grow 5x over the next two years and every business needs
a content supply chain to manage this. Adobe GenStudio is our solution to address this in an end-to-end fashion. And Amazon Ads is a key
collaboration even here by integrating our creative and customer experiences with how creative and marketers can now bring all of
these ideas to market. And finally, brand visibility
is clearly top of mind for CMOs as we all turn to these LLMs for information, recommendations, as well as purchase decisions. We actually observed a 1100%
year-over-year increase in AI traffic to U.S. retail
sites as recently as September. And with products like
Adobe Experience Manager as well as the newly
available Adobe LLM Optimizer and Adobe Brand Concierge, we're helping brands stay
in front of the AI search. We're really excited about the promise of AgentCore and Kiro
to help us accelerate the deployment of all these
new agentic capabilities. We've already had numerous successful AgentCore proof of concepts. For example, our Adobe commerce team was able to run a prototype
migration assessment using AgentCore to help our customers identify as well as solve
compatibility challenges as they move to this SAS product. Adobe has incorporated AI into
our tools for over 15 years, delivering hundreds of advances that enhance this efficiency
and collaboration. 99% of Fortune 100
companies have used Adobe AI in an application. Across all these categories, AWS is helping us to innovate faster, operate more efficiently, and deploy new technologies at scale. Whether it's in the data
layer where we train our category-leading Adobe
Firefly Foundation models, whether, as Matt said, in making sure that we offer choice in AI models so we can continue to innovate
in creative categories, through agent orchestration where we're augmenting this ecosystem, and finally, integrating
AI into all of our apps, making it easy for customers of all types to adopt and realize value
where they do their work today. It's an incredibly exciting time to stand at this intersection of human and computer interaction, and the AI transformation Adobe and AWS are driving together, I believe will redefine
digital experiences for billions of people around the world, and we couldn't be more excited
to work with all of you. Thank you. (audience applauds)
(upbeat music) - That's great, Shantanu. Thanks so much. It's really exciting to see how Adobe is pioneering
across digital experiences all on top of AWS. Now, with the tools and
services we're providing, we know that our customers
and partners out there are gonna build a huge number of incredibly impactful agents, but you can also expect that some of the most capable,
powerful agentic solutions are gonna come direct from AWS. Let's dive into a few of those now. Now, as we thought about
what agents should we build and which experiences could we reimagine, we focused on areas where we thought we could bring some differentiated
expertise to our customers. For example, turns out Amazon has a very large,
heterogeneous global workforce, and we understand the importance and frankly the complexity of tying together all of your
enterprise data and systems to empower those employees. We set off to build something
that would empower Amazon and our customer set
of corporate employees, which is why we built Amazon Quick. With Quick, our goal is
to give every employee a consumer AI experience, that consumer AI experience
that they've come to embrace, but with the context and the data and the security that you all
need to get your work done. Just earlier today, I
talked about how important deep access to your company's data is when you're trying to
make critical decisions, and that's one of the
things that makes Quick unique and powerful. It brings together all your data sources, your structured data like
BI data and your databases and your data warehouses, your data from apps like Microsoft
365 or Jira or ServiceNow or HubSpot or Salesforce, as well as all your unstructured data, things like your own documents or your files that you have in SharePoint or Google Drive or Box, all of that data that you
need to make great decisions, and we make it accessible to a powerful suite of powerful agents. With Quick, you get a rich
set of BI capabilities that make it easy for
anyone to discover insights across all of those sources of structured and unstructured data. You get a capability to do deep research. This is actually one of my
personal favorite features. And it allows Quick to
investigate complex topics, but then it can pull information from your internal data repositories as well as external source
of data on the internet to pull together a thoughtful,
detailed research report complete with source citations so you know exactly where
the information comes from. And you can create Quick Flows which give you the ability to create these little mini personal agents that can automate flows for
your everyday, repetitive tasks to drive efficiency for
you as an individual. And this can help your
teams at your companies be much more efficient
and productive at work. A few months ago, we released Quick internally at Amazon and today, we already have
hundreds of thousands of users inside of the company. The value that our own
employees are getting from Quick has quite frankly blown us away. Teams are telling us that
they're completing tasks in 1/10 the time that it used to take. Take for one example that I have where I heard from our our
internal Amazon tax team where they built a Quick agent that helps them consolidate all of their sources of tax data, whether they're projects from audits or details from the internet, and it performs deep research into any tax code changes
or policies changes that might be made, and it presents all of
this tax information from all those sources of data
in a single view for them. They then use Quick to
visualize that information, and it allows them to track
your regulatory changes in real time. Now, these weren't developers,
these were tax people, and they were able to do
this without writing any code or pulling any manual reports. Now, when a new tax law emerges, everyone can act on it quickly. It eliminated this siloed set of systems and enabled the team to stay compliant and proactive rather than reactive. And we're hearing stories
across the company like this over and over again. Another place where we use agents to transform what's possible for you all is in customer service. This turns out, like, that's another area an area where Amazon knows a lot about. Amazon Connect is a leading
cloud contact center solution and it transforms customer experiences across organizations of all sizes. Connect was a pioneer in bringing
AI to the contact center. with AI-powered self
service, it allows you to intelligently,
automatically resolve issues, but it also combines it with
AI-driven recommendations so that you can guide your human agents. Connect gives you this ability to deliver personalized, exceptional experiences for all of your customers. And it's impressive to see
how quickly Connect has grown to lead the transformation from these legacy on-prem environments into a cloud, AI, and
agent-powered contact center. And it's done this for global enterprises like Toyota and State Farm and Capital One and National Australia Bank, as well as for hundreds
and hundreds of startups. Customers are seeing the impact
of this move to the cloud, and we're seeing this momentum really accelerate the business. In fact, it's being shown
in the business results earlier this year, the
Connect business passed the 1 billion annualized run rate mark while helping tens of
thousands of customers grow their business faster. Thank you to all of you who use Connect. (audience applauds) Quick and Connect are just two examples of AWS delivering
impactful agentic solutions for our customers. Up next, we're gonna hear
from a fast growing startup that's also helping
enterprises get more work done. To share their story about how they're
transforming what's possible with agents in the enterprise, please welcome May Habib, CEO of Writer. (audience applauds)
(upbeat music) - What if Mars, one of the world's largest
consumer goods companies in the world, could run every ad image
through compliance in seconds, saving thousands of hours as checks are done instantly? What if AstraZeneca, makers of some of the
most innovative drugs, could automate the paperwork needed to get treatments approved
all over the world, saving months of painstaking manual work and getting life-saving
treatments to people faster? And what if Qualcomm, the global technology leader, could uncover the most efficient places to put marketing spend in real time, dramatically boosting campaign performance while saving millions in the process? This is not just the promise of AI, this is all happening today, right now, with agentic AI from Writer. I'm May Habib, Writer's
co-founder and CEO. And over the last five years, we've worked with the
world's largest companies in the most highly regulated industries to build a platform for agentic work. Early on, we saw a gap between the amazing things
these LLMs were capable of and what would meet the enterprise's bar for reliability, security, and control. We made a bold decision to
be a full-stack platform, one that has the precision and compliance that enterprises need. It's powered by our own
enterprise-grade Palmyra LLMs and delivers agents that handle the toughest
enterprise workflows. To truly scale our full-stack vision, we needed an infrastructure provider that was resilient, secure, and engineered for the enterprise. The majority of the
Fortune 500 run on AWS, including so many of our customers. So teaming up with AWS was a no-brainer. AWS stands alone as the cloud provider that enables us to both
train our frontier models and deploy our entire platform securely to our enterprise customers. Our work with AWS started two years ago
with the model layer. We had just launched
our latest Palmyra LLM, and it was posting top
scores on leaderboards. But as our models got larger, the computational power that was needed for both training and
inference was growing, and that's where the depth of the AWS stack became
a strategic advantage. Our foundation is built
on SageMaker HyperPod, which gives us a powerful service for large-scale model training. We use P5 instances,
and soon P6 instances, to handle the heavy GPU workloads, and they're connected with
Elastic Fabric Adapter, which is what makes the
high-speed communication between nodes possible so our training runs stay
fast and synchronized. We've also paired HyperPod
with Amazon FSx for Lustre, so we get data at the
speed our models need, while keeping costs under control. And the results have been enormous. We've been able to do
runs at 1/3 of the time, going from six weeks down to two weeks, and our training pipelines
have become 90% more reliable. All that work gives us
the power and stability to build our latest frontier model, Palmyra X5 trained right on HyperPod. X5 gives exceptional adaptive reasoning, a massive 1-million token context window, and near-perfect accuracy in
extracting business insights from even the most
complex, high-volume data. And it delivers this
with incredible speed. A million-token prompt in just 22 seconds and multi-turn function
calls in 300 milliseconds, outpacing other frontier models at 1/4 of the cost. But our relationship with AWS was never just about creating
fast, powerful models. It's always been about building
a breakthrough AI platform that can transform how businesses operate. And with Palmyra X5 as the engine, we're delivering on that vision. With Writer, enterprise teams at companies like Mars and AstraZeneca
and Qualcomm work smarter by connecting agents to
the data, to the context, and to the business knowhow that transforms critical processes, all without business users needing to write a single line of code. Playbooks are central to Writer. They let teams capture a process once, linking the tools, the data,
and the systems they rely on and turning them into
repeatable, intelligent agents. A playbook becomes a
living, dynamic blueprint for how great work gets done. And because they're shared across teams, the highest-impact playbooks can be scaled across
organizations instantly. And very soon, with the help of AWS, Writer is going to be including our next generation of self-evolving LLMs that can learn how organizations operate and anticipate requests on the fly. They're going to be the
world's first agents that improve the more that you use them. But there is a question
hanging over all of this, and for the leaders in IT, security, and compliance in the room, those who are held accountable for when something goes wrong, how do we empower
business teams to innovate but do it safely and securely? Writer has to be first and foremost an interoperable platform, one that can observe, control, and connect your agents at scale with the tools and
safeguards you already trust. Today, we're bringing
that paradigm to Writer by launching a powerful suite of supervision tools built
specifically for the enterprise. We're giving organizations full visibility and control across the agent lifecycle. Every session tracked,
every output compliant, and every data connector
governed in real time. True interoperability means connecting to the systems you trust. So our platform works
with the observability, guardrails, and systems
that you already use. And beginning today, we're very excited to announce Amazon Bedrock Guardrails
now integrate directly with our platform. (audience applauds)
Thank you. That means if you've
already set up your policies and safety rules in Bedrock, you can apply those exact same
guardrails to use in Writer. You don't have to rebuild anything, and you get one consistent compliant layer of control across
your entire AI stack. We also know that model choice is really important to enterprises. So also starting today, models from Amazon Bedrock are available directly inside
of the Writer platform. That means AWS and Writer customers can now build agents on
Writer using a catalog of different models, from our own Palmyra family to the awesome Nova models
you just heard about today and many more, all within a single governed environment. It's the ultimate flexibility without compromising on security. For organizations like Vanguard, long-time customers of Writer and AWS, where trust is non-negotiable, the Writer and Bedrock integrations give them the control they need to innovate responsibly at scale. And trust is how companies
go from a few scattered POCs to a truly governed, enterprise-wide,
impactful AI strategy. You can't scale what you don't trust. At Writer, our vision is to
empower people to transform work and we're very proud to do it with AWS. Thank you. (audience applauds)
(upbeat music) - Thanks a lot, May. We're very excited to
help customers like Writer make AI and agents real
for their customers. All right, one end user that we haven't talked much
yet about is developers. And this turns out to be an area where AWS and Amazon have
a really deep expertise. We know that by far one of
the biggest pain points today for development teams who are trying to rapidly
modernize their applications is dealing with their technical debt. Accenture estimates that tech debt cost companies a combined
$2.4 trillion a year in the U.S. alone. And Gartner says 70% of IT budgets today are consumed by
maintaining legacy systems. We knew this is an area
where AI could help. And this is why we built AWS Transform, to customers move away from
their legacy platforms, things like VMware and
mainframes and windows .NET. With mainframe
modernization as an example, our customers have already used Transform to analyze over a billion
lines of mainframe code as they move those mainframe
applications into the cloud. Using Transform, Thomson Reuters is modernizing over 1.5
million lines of code per month as they move from Windows onto Linux. We knew that helping you modernize faster would be really popular, but man, it turns out you all really dislike
your legacy platforms. Yesterday, at the festival
grounds here in Las Vegas, some of you might have seen, many of you and tuned in and cheered as we dropped an old
decommissioned rack of servers from a crane and blew them up as an ode to crushing tech
debt with AWS Transform. Now, this was pretty fun, but there's a lot more legacy platforms that we need to go after. A lot more. After we launched Transform last year, we actually quickly sat back and we started prioritizing which transformations
would we go after next. We had a ton of ideas, Lambda function upgrades, Python upgrades, maybe
Postgres version upgrades, or maybe people who wanted to move from C to Rust migrations. But then we thought
about, what about updates to proprietary applications and libraries? The list is almost infinite. So we asked ourselves, why not support all modernizations? Just yesterday, we launched
AWS Transform Custom, which gives you the ability to- Thank you. Those guys are excited about AWS Custom. (audience applauds) It gives you the ability to create custom code transformation agents to modernize any code or API or framework or runtime or language translation, even programming languages or frameworks that are
only used by your company, and customers are already flocking to it. We've already seen customers doing Angular to React migrations, converting VBA scripts that are embedded in their Excel sheets into Python, converting Bash shell scripts into Rust. One great customer example is with QAD, a provider of cloud-based ERP
solutions and supply chain. Their customers struggled with modernizing from customized old versions
of Progress Software's proprietary advanced business language to their QAD adaptive ERB platform. QAD turned to AWS Transform. They had these engagements
that were taking a minimum of two weeks to modernize, and all of a sudden,
they were completing 'em in under three days. We're really excited to see what legacy code you're
all able to transform. Now, one of the great things about making all these
transformations easier is that it leaves a lot more
time for developers to invent and that's what we get excited about. And it turns out that developers today are building faster than ever. AI software tools have seen rapid changes over the last year. We've moved from things
that are doing, like, inline tab completion to
authoring chunks of code to actually completing
simple multi-part tasks. We really see the potential for the entire developer experience, and frankly, the way
that software is built to be completely reimagined. We're taking what's exciting about AI-powered software development, but we thought that there was opportunity to add structure to it to make it ready for enterprises to adopt and for high-velocity co-development teams to use more effectively. And this is why we launched Kiro, the agentic development environment for structured AI coding. Kiro helps developers take advantage of the speed of AI coding, but with more structure where they're in the driver's
seat every step of the way. Kiro has popularized this idea of spec-driven development. From simple to complex projects, Kiro works alongside developers and teams, turning prompts into these detailed specs and then into working code
by its advanced agents. So what you get and what gets built is exactly
what you want and expect. Kiro understands the
intent behind your prompts and helps you and your team
implement very complex features in large code bases and in fewer shots. Now, the reception to Kiro has been quite frankly overwhelming. Hundreds of thousands of
developers have already used Kiro since the preview of the
launch just a few months ago. Let's hear directly from them on how transformative Kiro
has been to their work. - I use Kiro in almost
all the development I do. I ask it questions, I
create specs with it. - With Kiro, I was able to ship more code in the last five months
than in the past 10 years. - With Kiro, I'm able
to work with a partner so it feels like we're collaborating on the project together. - It operates the way my brain operates when solving a problem. I can just say, "Hey, Kiro, remember that feature we outed in? Can you also write a test as well?" - I can be hands off once
I break the problem down and just let Kiro deliver for me. - I feel like my world has just opened up to a completely different perspective. - Everything feels possible now. - You can go from zero
to POC 10 times faster. - Kiro makes me want to build more. - Honestly, KIRO is just (beep) awesome. (upbeat music) (audience cheers and applauds) - We think you're all gonna love how Kiro will transform
your development work. And so, I'm excited to announce today that for any qualified startup, we're giving away a year's worth of Kiro, up to a hundred seats, if you apply in the next month. (audience applauds) We are so excited about the impact that Kiro is having on
making developers' lives better each and every day. And I've frankly been amazed at the impact that this development velocity
has seen inside of Amazon. In fact, we've been so
blown away that last week, all of Amazon decided
to standardize on Kiro as our official AI development
environment internally. We took a look at all of the
tools out there in the market and we recognized that the best way for us to make our developers
faster and more productive was to double down on Kiro. And many of you all are
rapidly doing the same. Now, I want to take a quick moment and dive deeper into one of the stories
we heard in this video, 'cause I think the details
are pretty eye-opening. Now, this was a quote from Anthony, one of our distinguished engineers. Now, Anthony is working on a significant re-architecture project, and he and the team originally thought that they would need about 30 developers working for 18 months
to complete this work. Now, Anthony and the team were intrigued by the
potential of agentic AI and the potential for it to
really supercharge their output. So they decided that they
were gonna fully leverage Kiro to deliver the project. It turned out as the team
started really digging in and seeing the full
potential of agentic tools, it was better than they expected. And they saw that by leaning
in on agentic development, a much smaller team could actually deliver incredible results. Instead of taking 30 developers 18 months to complete the project, they delivered the entire re-architecture with only six people in
76 days, and with Kiro. This is not just the 10
to 20% efficiency gains that people were seeing with the first generation
of AI coding tools. This is orders of
magnitude more efficiency. Now, I think this is a
super powerful story, and I've related it to a couple of customers
over the last month or so, and invariably I get the
question, "How did they do it?" Well, at first it turns
out it took the team a little bit of time to fully understand how to best leverage agentic tools. They started to see of course some efficiency gains right away. But these were honestly a little bit more incremental
than transformative. But a few weeks in,
they had an a-ha moment. They realized that they
couldn't keep operating the same way they always operated. They realized to get the
most out of the agents meant changing their workflows, and they wanted to lean
in to the strengths of what the agents were, and then they had to question some of the assumptions they always had about how they wrote software. The team learned a ton along the way and was able to spot a whole
series of new opportunities for how agents could enable
teams to ship faster. The first learning they had, which was how they interacted
with these Kiro agents, in the beginning, they would feed the tools small tasks to ensure that they got
the reliable results back, and they would go back and forth with all their tools constantly. But as they learned what
the agents were good and what were not good at, there was this inflection point where they moved from
babysitting individual tasks into directing broad, goal-driven outcome. And this is when they saw their velocity on shipping features rapidly accelerate. Second then, they thought
about moving even faster, and they recognized
that they were thinking much too linearly in
assigning tasks to the agent. They realized that the team's velocity was tied to how many
concurrent agentic tasks they could run. And if they could have the agent do more in parallel, they'd go faster. And so they kept looking for ways to scale out their workloads. Finally, the team observed
that as they scaled out, they themselves became the bottlenecks. They had to keep unblocking
the agents as they came back 'cause they needed a human
intervention or direction. It turns out that the
longer they could get these agents to work
independently, the better. One clear example actually is when the looked at their commit graphs, not surprisingly, they
saw that progress stopped when everyone went to sleep. They hypothesized that if the agents could use that time to clear the backlog, the team would be able
to wake up in the morning with lots more code to review and be able to keep moving faster. So we sat back and
reflected on these learnings and we asked ourselves, "Why can't we have agents that are able to do all of these things?" And that's why today we're
introducing frontier agents. Frontier agents are a new class of agents that are a step-function change, more capable than what we have today. We generally think about three things that differentiate frontier agents. One, they're autonomous. You direct them towards a goal and they figure out how to achieve it. Two, they have to be massively scalable. Of course, individually they can perform multiple concurrent tasks, but you have to be able to distribute work across multiple instances
of each type of agent. And three, these agents
need to be long-running. They may be working for
hours, maybe even days in pursuit of ambitious, sometimes frankly amorphous goals without requiring human
intervention or direction. Lemme introduce the first frontier agent we'll be launching today, and that is the Kiro autonomous agent. (audience applauds) The Kiro agent is an agent that transforms how developers and teams build software, vastly increasing your developers team's capacity to invent. The Kiro autonomous agent runs alongside your workflow, maintaining context and
automating development tasks so that your team never loses momentum. You simply assign a complex
task from the backlog and it independently figures
out how to get that work done. Kiro can now autonomously tackle a full range of things
your developer might need, from delivering new
features to triaging bugs, even improving code coverage. And all of this takes
place in the background so that your engineers can
stay in their flow state, focusing on the big ideas. Kiro autonomous agent
connects with your tools that you already use like
Jira and GitHub and Slack and it does that to build
a shared understanding of your team and your work. One of the super cool things is that the Kiro agent is just like another member of your team. It actually learns how you like to work and it continues to deepen
its understanding of your code and your products and the standards that your team follows over time. It weaves together everything you do, every spec, every discussion,
every pull request, and it builds this collective memory that fuels smarter development. Let's take an example. Let's say you need to
upgrade a critical library that's used across 15
different microservices. Now, if you were to do
this with Kiro today, you'd have to first open a repo, prompt it to update the library, then you'd review those
changes, fix anything it missed, run your tests, and create a pull request. Then you'd move on to repo
two and you'd start all over, re-explaining your context, re-prompting for similar changes, and you'd do that 14 more times. Each time you did it, you'd have to approve the changes, and if you paused or went home for the day or anything like that, you'd have to remind
Kiro of all the context when you start back up since it doesn't maintain
state in between sessions. Let's take a look and
see what this looks like with the new Kiro autonomous agent. First, you'll get started in kiro.dev and kick off a task associated
with your GitHub repo. You'll describe the problem
that you're trying to solve, and then the agent uses that, and it uses all of its reasoning and knowledge from
previous implementations to ask clarifying questions that it doesn't understand
as it tries to plan tasks. With its deep knowledge
of your entire code base, it then quickly identifies where it needs to make updates in all the selected repositories where it needs to go
update your libraries. The agent identifies every
affected repo that you have, analyzes how every service
that you have uses a library, and updates the code
following your patterns. It runs full test suites and then it opens 15 tested,
merge-ready pull requests. All of this is in the background while you work on something else. And to go even faster, it scales out to more parallel tasks, each with its own context so that while you have Kiro off there implementing your new library, you can also have it fix a
bug that you found last night. And this agent isn't session-based. It doesn't forget. When you give it feedback on one of your pull requests
about error handling, it applies that learning to the next 14. When it sees similar architectural
decisions in the past, it references the work
that you've done before. You're not re-explaining
your code base every time. It already knows how you work and it gets better with every
single task that it does. We think that this will help
you move much more quickly and it's gonna completely change the way that you think about writing code. So that's the Kiro autonomous agent, and we're really excited about how it's gonna allow you to ship more code more quickly. But one other thing that
our teams quickly discovered as we started writing
tons and tons more code is that you can't just
accelerate writing code alone. It's only the beginning. You have to make sure that every stage of the
software development lifecycle can scale and accelerate at the same rate. Otherwise, you're just gonna
create new bottlenecks. We realized that the same
lessons that we learned, directing outcomes, scaling out, extending agent autonomy, apply to almost every aspect
of the development lifecycle. Now, as we've said this once,
we'll say it a thousand times, security has always been our
number one priority at AWS, and we've been working with
you, all our customers, to help you all secure
your products in the cloud for nearly two decades. So we naturally thought next about what a security frontier
agent would look like. We know that every customer wants their products to be secure, but you have trade-offs. Where do you spend your time? Do you prioritize improving the security
of existing features or do you prioritize time
on shipping new ones? At Amazon and at AWS, security is so deeply embedded
in everything that we do in our development
culture, in our practices. We perform code reviews, we conduct security reviews
of systems architecture, we do tons of pen testing with huge teams consisting of both internal
and external experts that look for vulnerabilities all before any code
ever reaches production. But it turns out, most customers can't afford
to do this continually. So what happens is either
you don't do all of this or you just do it a couple times a year. And now when development
is so accelerated with AI, this can mean that
there's multiple releases that are going out the door before your code is rigorously
assessed for security risks. We have a firm belief that in
order to get security right, you have to build it into everything you do from the ground up. And so I'm very excited to announce the launch of the AWS Security Agent. (audience cheers and applauds) This agent will help
you build applications that are secure from the very beginning. AWS Security Agent helps you
ship with more confidence. It embeds security expertise upstream and enables you to secure
your systems more often. It proactively reviews
your design documents, and it also scans your
code for vulnerabilities. And since a Security Agent integrates directly with your GitHub pull requests, it provides your developers with feedback directly
into their workflows. Security Agent also helps
with penetration testing. It turns pen testing in from
this practice that was slow and an expensive process into something that's
an on-demand practice. It allows you to continuously validate your application security posture. I'll quickly show you how it works. Let's say your company has an approved way of storing and processing
credit card information. But let's say you have a developer that inadvertently works
with the wrong approach. This can mean a ton of rework, and late in the development process, it possibly could mean
throwing away months of work. However, the AWS Security Agent can catch these issues early. It can even catch it from
your design documents before you write a line of code by always looking to ensure that you're following your
team's best practices. Then when the time does
come to submit your code, AWS Security Agent can
review your pull request against those same requirements and flag any issues, providing you with
concise remediation steps for anything that it finds. When your code's complete, you simply initiate a pen test and that agent will
immediately jump on it, giving you real-time
visibility into its progress. When it's done, you actually
get validated findings complete with suggested remediation code to fix any issues that it does find. No more waiting for resources, no expensive external consultants. And let's say you have multiple apps that are ready to deploy in production. You can just launch multiple
Security Agents in parallel so you can get and test
all of your applications and not get bottlenecked. Now, you're writing code faster and you're deploying it just as fast because you know it's secure. Now, of course, you know what comes next. You have to operate that code. And we all know that as systems grow, the surface area of what
you're operating grows as well. And that means growing DevOps work. This is something that our own teams inside of Amazon have a
ton of experience with. At Amazon, we've always believed that the best way to create
a great customer experience is to have developers
operate their own code. We've been living DevOps for many years, and what we've learned, that frankly, as your service scales, operations can eat up more
and more of your time. We thought this is another area where we could put our
expertise in your hands. Introducing the AWS DevOps Agent. (audience applauds) This agent is a frontier agent that resolves and proactively
prevents incidents, continuously improving your reliability and your performance. The AWS DevOps Agent
investigates incidents and identifies operational improvements, just like your experienced
DevOps engineers would. It learns from your resources,
their relationships, and including things like your existing
observability solutions, runbooks, code repositories,
and CI/CD pipelines. It then correlates all
that telemetry and code and deployment data across
all of those sources and allows 'em to understand relationships between your application resources, including, by the way, applications in multi-cloud
and hybrid environments. Let me show you how this can
transform incident response. Let's say an incident
happens, an alarm goes off. Before your on-call
engineer can even check in, AWS DevOps Agent instantly responds, diagnosing that it found some elevated authentication error rates from a Lambda function that was trying to
connect to your database. It uses knowledge of
your application topology and the relationship between
all those different components to independently work back from the alert to find the root cause of the problem. In this example, let's
say you use Dynatrace for your observability solution. The AWS DevOps Agent uses its built-in
integration with Dynatrace to provide more context for the incident. It understands all of your dependencies and knows your deployment stack that created each and every resource. When it's found the problem, let's say in this case it was a change that was made to your Lambda
function's IAM policy, it then tells you what
introduced that change. It turns out it was a simple mistake in your CDK code deployment. By the time your on-call engineer logs on, the DevOps frontier agent
already has found the issue, suggested a change, and is ready for your on-call to review the change and approve the fix. What's even better is that it lets you
prevent such an incident from happening in the future by recommending some CI/CD guardrails to catch these type of policy changes before they're ever deployed. And that's it. The DevOps Agent is always
on call, fast and accurate, making instant response
and operations work easy. Together these three frontier agents, Kiro autonomous agent, AWS Security Agent, and the AWS DevOps Agent, are gonna completely
transform the way your teams build, secure, and operate your software. Let's take a quick look at what your future might look like here. (employees chattering faintly) (keys clacking) - Hey, did you run a pen test? - Pen test? I'm still working on these unit tests. - (chuckling) You're funny. Like we have time for pen tests. (energetic music) (notifications chiming)
(keys clacking) (text beeping) Why does upgrading one package
break five others? (sighs) - Weird. Worked for me. - Love that for you. Morning. You look nice. - Got paged at 4:00 AM. I feel awful. - Cheers. (notifications chiming) - "Did you use the latest
pull request format?" (sighs) Classic. (notifications chiming) (chip crunches) (mouse clicks) - We're green across the board. - Yes!
- Oh my god. (laughs) - Wow!
- We got it. - Look at that. (laughs)
- Oh my god. (text chiming) (employees chattering faintly) (employee sighs) (footsteps pattering) (audience applauding)
- Today, I'm excited to announce the next leap forward. We're launching three new frontier agents. These agents can reduce a lot of the time that's spent on these really important but repetitive, time-consuming and frankly, unfulfilling tasks. This takes what used to be
months of work into hours. - Whoa. - [Matt] They are gonna transform the way you and your teams build,
secure, and operate software. (bright music) - Any dumpster fires last night? - Nope. Solved for me. Approved it and went back
to sleep in a few minutes. - Look at you. - Thank you. - All right, let's go. I've got some fire ideas for you guys. - Oh, cool. - Now, with added pen tests. - We think that we're
only at the beginning of frontier agents, and we're super excited to see what you all achieve with them. - System automatically balances the load across the charging stations.
- That's awesome. - [Employee] Good work. (audience applauds) - I think we can all agree that's a future we'd be excited about. Today is a big leap forward in the journey unlocking the value of AI. We're bringing you powerful innovations at every single layer of the stack. The innovation that's happening
across AI and agents today is truly incredible. But it turns out it's not just
our AI and agentic services that are developing a
ton of new innovation this week here at re:Invent. There's a bunch of launches
that AWS is very excited about. And because AWS is so broad, I know many of you were hoping to hear about our fantastic additions to our core non-AI services as well. It turns out it's actually
one of the hardest things of planning and doing
this re:Invent keynote. What do you cut from the talk? How do you fit it all in? Well, teams asked us, when our teams were delivering, they said, "I'm gonna keep doing
the pace of innovation." And I said, "Well, I don't know how to fit
it into one keynote." But I said, "You know, why not try?" So I said, "If our AWS teams can
deliver at such a rapid pace, I can up my keynote game too." I'm gonna try, we'll see. So if everybody can hang with me for just a few minutes
longer, we're not done yet. I have 25 exciting new product launches across our core AWS services to unveil, and I'm gonna give myself
just 10 minutes to do it. To keep me honest here, the team is rolling out a shot clock and you all can keep track. Okay. All right. (audience cheers and applauds)
All right. All right. Buckle up, everybody. Let's get to it. Let's start with our compute offerings. We know that one of the
things that you all love is that AWS continues to offer the broadest
selection of instances. So you always have the
best possible instance for your application. Now, lots of you run memory-intensive
applications out there like SAP HANA or SQL Server or EDA. So today, I'm excited to
announce our next generation of X family of large memory instances. (audience applauds) They're powered by custom
Intel Xeon 6 processors, and these instances can
provide up to 50% more memory. And I'm excited to announce
the next generation of our AMD EPYC memory processors as well, giving you three terabytes of memory. Now, you've also told us that you have a lot of really demanding CPU-heavy applications out there, like batch processing and gaming. So today, we're launching
our C8a instances, which are based on the
latest AMD EPYC processors and give 30% higher performance. Many of you also run EC2 instances that run security or network applications. And those applications
need a lot of compute and super fast networking. For those, we're announcing
our C8ine instances powered by custom Intel Xeon 6 processors using the latest Nitro v6 cards. These instances deliver 2.5 times higher packet
performance per vCPU. What about applications that need really ultra-fast
single-thread frequency compute? You got that too. Introducing our M8azn instances, with the absolute fastest
CPU clock frequency available anywhere in the cloud. These instances are ideal for applications like multiplayer gaming, high-frequency trading, and
real-time data analytics. Today, AWS is still the only provider that offers Apple Mac-based instances, and they are really popular. So today, I'm happy to
announce two new instances powered by the latest Apple hardware, announcing the EC2 M3 Ultra Mac and the EC2 M4 Max Mac Instances. Developers can now use
the latest Apple hardware to build, test and sign Apple apps in AWS. All right, customers love using Lambda to quickly build functions
and run code at scale. Lambda works great when you
want to execute code quickly, but sometimes you have a use case where your Lambda function
needs to wait for a response, like waiting on an agent that's
working in the background for several hours or maybe even days. We wanted to make it easy for you to program wait times directly
into your Lambda functions. So today, we're announcing
Lambda durable functions. (audience cheers and applauds) Durable functions make it
easy for you to manage state, build long-running workloads
with built-in error handling and automatic recovery. All right, how are we doing? All right, eight launches
in about three minutes. All right. I better pick it up. All right, let's move on to storage. We know you love S3. I mentioned earlier that S3 stores more than 500 trillion objects, hundreds of exabytes of data. That is a lot of data. When we launched S3 in 2006, we had a five-gigabyte max object size. Then a couple years later, we increased that to be five terabytes, and that has been sufficiently
large for the past decade. But data has gotten a lot bigger in the past couple of years. So we asked ourselves, "What would be the object size that would meet all of your needs today? Should we double it? Triple it? How about 10x it?" I'm pleased today to announce that we're increasing the
maximum object size in S3 by 10x to 50 terabytes. (audience applauds) But not just bigger, though. We knew you also wanted to make S3 faster for batch operations. So starting today, we're
improving the performance of batch operations where large batch jobs now run 10x faster. (audience applauds) Last year at re:Invent,
I announced S3 Tables, which is a new bucket type
optimized for Iceberg tables. It's been incredibly popular, but as the volumes of table data has started to quickly rise, you all have asked for ways that we can help you save money. So today, we're announcing Intelligent-Tiering for S3 Tables. (audience cheers and applauds) This can save you up
to 80% on storage costs for the data in your S3
table buckets automatically. You also asked us to make it easier to replicate these tables between regions so that you can get consistent query
performance from anywhere. So as of today, you can now automatically
replicate your S3 tables across AWS regions and accounts. (audience applauds) Earlier this year, we
introduced S3 access points for Fsx, for OpenZFS. This allows you to access your
ZFS file system information as if it was data inside of S3. And today, we're making it
possible for you to access even more of your file data this way by expanding S3 access points to FSx to include support for NetApp ONTAP. Now, ONTAP customers can also
access their data seamlessly, just as if it was in S3. Now, one of the fastest growing data types that you all have are vector embeddings, which are used to make it easier for your AI models to search for and make sense of your data. Earlier this year, we announced
a preview of S3 Vectors, which is the first cloud object store with native support to
store in query vectors. And today, I'm happy to announce the general availability of S3 vectors. (audience cheers and applauds) You can now store trillions of
vectors in a single S3 bucket and reduce the cost of storing
and querying them by 90%. Now, I expect that many
of you will use S3 vectors in concert with a
high-performance vector database. Today, the most popular way to do that at low latency search of
your vector embeddings is with an index in Amazon OpenSearch. But many of you have asked us, "Is there a way that you
can speed up the process of creating that index
for all of my data?" So today, we're excited to
announce GPU acceleration for vector indices in Amazon OpenSearch. (audience applauds) By using GPUs to index that data, you can now index data 10x
faster at 1/4 the cost. All right, how are we doing? Four minutes left? Awesome. All right, 15 launches and
just a few minutes left. Let's keep going. Let's move on to EMR, which is our popular big
data processing service. We launched EMR Serverless four years ago and customers love it because it takes a lot of the muck out of running petabyte-scale processing, but it turns out today,
it isn't quite muck-free. Customers still have to provision and manage their EMR storage. But not anymore. As of today, we're eliminating the need for you to have to provision local storage for your EMR serverless clusters. (audience applauds) All right, let's move on to security. Today, tens of thousands
of you rely on GuardDuty to monitor and protect your accounts, applications, and data from threats. This past summer, we added GuardDuty's
extended threat detection to Amazon EKS, and we're pleased with
the momentum we're seeing. So of course, naturally,
we didn't stop there. And today, we're adding
this capability to ECS. Now, you can use AWS's most advanced threat
detection capabilities for all of your containers and all of your EC2 instances as well. These are both enabled for all GuardDuty customers
at no additional cost. Every customer wants to find and fix security issues quickly. The faster and easier, the better. That's why we have Security Hub, which aggregates security data from AWS and third-party sources and helps you identify
potential security problems. Earlier this year, we previewed an enhanced
version of Security Hub, and today, I'm excited to
announce that Security Hub is GA. Today, we're also announcing
several new capabilities, including near real-time risk analytics, a trends dashboard, and a new streamlined pricing model. Ops teams out there live
and die by their log data, but that log data is everywhere. They're in CloudTrail logs
and VPC flow logs and WAF logs and logs from third parties
like Okta and CrowdStrike. We thought that we could make that better. So today, we're announcing a new unified data store in CloudWatch for all of your operational
security and compliance data. (audience applauds) It automates log data collection
from AWS and third parties and they'll store it in
S3 data, or in S3 Tables, to make it easier and faster to find issues and unlock new insights. All right, stick with me
everyone. We're almost there. We're on the home stretch.
Let's move on to databases. Now, I'm not gonna make you
raise your hand, don't worry. But I know that many of you
out there are still supporting some legacy SQL Server
and Oracle databases. Getting off of them is hard, but at least AWS makes
it easier to manage them. We see you out there, and don't
worry, we're here to help. One thing I hear from many of you is that your legacy databases have grown very large over time. They're actually bigger
than what we support in RDS. So I'm excited to announce we're increasing the storage capacity for RDS for SQL Server and Oracle from 64 terabytes to 256 terabytes. This also delivers a 4x improvement in IOPS and I/O bandwidth. This is gonna make it a lot easier to migrate existing workloads from on-prem to scale them on AWS. We also wanna provide
you with more controls to help you optimize
your SQL Server licenses and manage your costs. So we're doing a couple of things. Starting today, you can specify the number of vCPUs that are enabled for your SQL Server database instance. This helps you reduce
your CPU licensing costs that you get from Microsoft. And today, we're also adding support for SQL Server Developer Edition, so you can build and test your applications with no licensing fee. (bright music) Oh, the loop music's coming on. All right, that means I only
have a few seconds left, but there's one last thing that I think all of you are gonna love. Several years ago, we launched Compute Savings Plans as a way to simplify making commitments across our entire set
of compute offerings. And since that day, I've
regularly been asked, "When can I get a unified
savings plan for databases?" And here it is. Starting today, we're launching
database savings plans. (audience cheers and applauds) These can save you up to 35% across all your usage
for database services. (buzzer buzzes) (audience applauds and cheers)
Woo. All right, boom. Did it. A whole second keynote's
worth of new capabilities for all of you in under 10 minutes. Now, you have four full
days to go out and learn. Dive deep into the details
and start inventing. (basketball thuds) Thank you all for coming to re:Invent. Enjoy. (audience cheers and applauds) (upbeat music)
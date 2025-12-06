---
video_id: JeUpUK0nhC0
video_url: https://www.youtube.com/watch?v=JeUpUK0nhC0
title: AWS re:Invent 2025 - Keynote with Peter DeSantis and Dave Brown
author: AWS Events
published_date: 2025-12-04
length_minutes: 84.85
views: 5651
description: "Join AWS SVP Peter DeSantis and Dave Brown, Vice President of Compute and Machine Learning Services as they dive deep into the technology that powers AWS services. Get a closer look at how our unique approach and culture of innovation help create leading-edge solutions, from silicon to services.  20:14 LAUNCH AWS Graviton5-based Amazon EC2 M9g instances  Learn more about AWS events: https://go.aws/events   Subscribe:  More AWS videos: http://bit.ly/2O3zS75  More AWS events videos: http://bit.ly/..."
keywords: AWS, Amazon Web Services, AWS Cloud, Amazon Cloud, AWS re:Invent, AWS Summit, AWS re:Inforce, AWS reInforce, AWS reInvent, AWS Events
is_generated: False
is_translatable: True
summary: AWS's foundational infrastructure innovations centered on Nitro silicon, Graviton processors, and Trainium AI accelerators demonstrate how two decades of relentless investment in custom chip design, system architecture optimization, and performance engineering enable cloud attributes including security, availability, elasticity, cost efficiency, and agility that become increasingly critical during AI transformation where unprecedented compute demands, inference costs, and application scale requirements necessitate infrastructure specifically designed for cloud workloads rather than adapted commodity hardware repurposed from enterprise data centers. The Nitro system origin story beginning in 2010 addressed fundamental virtualization jitter where EC2 delivered excellent average performance but experienced frustrating outlier latencies of hundreds of microseconds sufficient to impact demanding workloads, with conventional wisdom declaring virtualization inherently unsuitable for performance-critical applications unable to match bare-metal servers, until AWS engineers systematically eliminated jitter sources through week-after-week optimization eventually recognizing virtualization tax remained unavoidable using traditional approaches, catalyzing revolutionary decision to move virtualization off servers onto dedicated custom silicon completely eliminating jitter while achieving performance exceeding bare metal through specialized hardware design, simultaneously improving security, increasing performance headroom, and enabling diverse instance type support. The Nitro achievement validates AWS's willingness to challenge fundamental assumptions and invest in multi-year custom silicon development when existing solutions prove insufficient for customer needs, with recognition manifested through inclusion in seventh edition of canonical computer science textbook originally studied during undergraduate education, now teaching students worldwide about Nitro and Graviton as examples of modern cloud infrastructure innovations alongside traditional operating systems and networking concepts, representing ultimate validation when academic institutions incorporate proprietary technologies into foundational curriculum acknowledging their transformative impact on computer science field. Graviton processor development emerged naturally from Nitro's success demonstrating custom silicon's ability to deliver performance and efficiency gains unavailable through commodity hardware, prompting fundamental question about whether compute processors designed specifically for cloud workloads from ground up rather than adapted or repurposed could achieve similar breakthroughs, leading to ARM-based Graviton delivering best price-performance for cloud applications through purpose-built design optimized for multi-tenant environments, elastic scaling patterns, and diverse workload characteristics fundamentally different from traditional enterprise computing assumptions embedded in general-purpose processor architectures. The launch of M9g instances powered by Graviton5 represents latest generation delivering continued performance improvements, cost reductions, and energy efficiency gains enabling customers to run more workloads using fewer resources while reducing environmental impact, with particular emphasis on AI and machine learning workloads where training and inference operations benefit from specialized acceleration capabilities integrated directly into processor architecture rather than requiring separate accelerator cards increasing complexity and cost. Trainium AI chip addresses specific challenge where AI workload costs threaten to consume tens of billions of dollars in data center investments as industry pursues AI transformation, with AWS simultaneously expanding capacity to meet unprecedented demand while investing deeply in cost reduction through purpose-built training and inference accelerators delivering superior price-performance compared to general-purpose GPUs, enabling customers to build and deploy AI applications at scale without prohibitive infrastructure expenses preventing innovation or limiting deployment scope due to budget constraints.
---

>> Please welcome the senior vice president of Utility
computing at AWS, Peter DeSantis.
>> Good morning. Welcome to the penultimate day of re:Invent
2025. Thank you all for your participation this week. It's
been a great week. I hope you had as much fun as we did. Now,
I expect many of you probably came this morning expecting to
see Werner I get it, we switched things up. You've been
busy all week, so I came prepared for this. If you just
direct your attention to the screens at the side. Hopefully
this feels a little more familiar. For those of you that
don't know me, I usually do the Monday night keynote. Now, I
asked about beer, but apparently you can't do beer at
a morning keynote. Makes sense, but I apologize. I'm more
interesting after a couple beers. Okay, if my transition
didn't help you get a fix, you can catch the real Werner this
afternoon at the closing keynote, as he says, they'll be
the last thing standing between you and the party. Now, I'm not
going to spoil anything, but Werner tells me he's going to
talk about what this AI transformation is going to mean
for us developers. And that got me thinking what is this AI
transformation going to mean for The Cloud? Well, I think
it's pretty obvious. This new generation of AI driven
applications is going to drive a ton of innovation in
infrastructure, and that's exciting for us. But I want to
start out talking about what's probably not going to change.
And these are the things that we've been focused on
delivering since the first days of AWS, the things that we
really care about. I would argue these things are maybe
even more important. These are the core attributes of the AWS
Cloud, and delivering on these attributes has guided every
service, every API, every technical decision that we've
made and continue to make. We think about these things a lot,
and we make big, deep, long term investments to support
these attributes. Take security. As you probably already know,
it's not just the good guys that are getting more
productive with AI. The bad guys are using the same tools
to attack your products, your customers and your
infrastructure. So it's never been a more important time to
know that your Cloud providers first priority is security or.
Right there behind security, availability, and the sheer
size and scale of the applications that are being
built right now. Demand. Performance from security or
from databases, analytics networks. So there's never been
a better time to build on a Cloud that's been tested,
running the most demanding workloads of the last decade.
And what about elasticity? One of the most important things
about The Cloud is it takes away capacity planning. It
wasn't long ago that one of the first things startups would
need to do is plan and provision their infrastructure.
What a complete waste of time. And worse yet, there's no right
answer to the question how much capacity do I need? If you plan
too little, you miss your big moment. Plan too much. You
might not afford to be able to get to your big moment. Now,
today, capacity planning is likely something that you don't
do at all. And that's a great thing. AWS is ready to scale
when you need us, but we're not done here. AI workloads have
led to an unprecedented increase in the demand over the
last few years, and we see this as an opportunity to take the
innovations that we've been working on for the last couple
of decades and apply them to these new technologies. Our
goal is to give you the same elasticity that you get from a
service, such as S3 with your AI workloads, and you're going
to hear a little bit more about how we're doing that this
morning. And that brings us to cost. The promise of AI is
exciting, and it will transform every aspect of our life. But
one thing that anyone who's put an AI application into
production knows is that AI ain't cheap. It's really,
really expensive to build these highly capable models and more
expensive still to run the massive amount of inference
that we need to transform our lives with these models, you
see almost daily headlines of the tens of billions of dollars
that are being invested in data centers power and capacity to
support this AI transformation. And AWS is investing massively
in this expansion as well. But we're doing something else.
We're investing deeply in lowering the cost of building
these models and running these workloads. You've heard a
little bit about Trainium this week, but later this morning,
we'll share a bit more about how we're building Trainium to
meaningfully lower the cost of these workloads. That leaves us
with Agility. When we launched AWS almost 20 years ago, I
think the attribute that most contributed to the success of
The Cloud was Agility. It became quickly apparent that
the companies who adopted The Cloud were able to move faster
than the companies that stayed On-Premises. They were able to
innovate faster. They were able to deliver value to their
customers faster. They were able to grow faster with fewer
issues. And most importantly, they were able to pivot faster.
That's Agility. That's the magic of The Cloud. You can
launch, optimize, pivot quickly. Now, doesn't that sound exactly
like what you're going to need during this AI transformation?
There's a lot of ways that AWS helps you be more agile, but
one of the ways is by making sure that you have the right
tool for the job. Whether you're a startup, inventing
something new or an enterprise modernizing old systems, we
give you the building blocks to create anything that you can
imagine, and this breadth and depth approach. It isn't an
accident. It's a deliberate choice that we make year after
year to keep investing in new services and new capabilities
and new ways for you to build. Because we believe that when we
remove constraints, when we give you every possible
building block, that's when the real magic happens. That's when
you can stop asking, can I build this and start asking,
what shall I build next? And the really exciting thing is,
the power of these building blocks is only going to be
magnified through Agentic development. So the things that
matter in the world of AI are the exact same things that
we've been obsessing over for the last 20 years, but these
capabilities don't happen by accident. You don't just wake
up one day and say, I want better security or lower cost.
These attributes come from a very deep commitment and
investment over time. Let me give you my favorite example.
I'll set the stage. It's 2010, a few years after we launched
EC2. By this time, it was abundantly clear that customers
loved EC2 and they wanted to run all sorts of workloads on
it. And for the most part, they could do it. Our performance
was just fine. But for a few of the most demanding workloads,
we faced the challenge. While our systems delivered great
performance, most of the time we'd see these frustrating
outlier latencies or something we call jitter, where
performance would suddenly drop off just a few hundred
microseconds, but enough to impact these applications.
These excursions came from the virtualization layer. Now,
virtualization was one of the key enablers of EC2, and it
works really well. But common wisdom at the time is that
virtualization wouldn't work, would work fine for less
demanding workloads, but it could simply never deliver the
performance of a bare metal server. But that wasn't
compatible with our vision for EC2, where we wanted to run
every workload. So we got really focused on fixing the
jitter problem. Basically, we aim to put jitter where it
belonged. Week after week, our engineers would deep dive into
the data and tackle these outlier latencies. We made
impressive progress with optimizations and achieved
results, frankly, that many people didn't think we could.
But eventually it became clear we didn't have a path to bare
metal performance. There was just always going to be some
virtualization tax. So of course you have to change
what's possible. And that's where the Nitro system came in.
Nitro is our AWS designed custom silicon. It moves
virtualization off the server and onto dedicated hardware,
and this allowed us to completely eliminate the jitter
problem and actually get exactly the same. In fact,
better performance than bare metal. Nitro also improves
security, delivers higher performance, and allows us to
support a wide range of instance types. The Nitro
system is an excellent example of the deep investments that
we've made, in this case actually building our own chips
to enable these key product attributes that I just talked
about. Now, for those of you that have joined me on Monday
night, you're probably thinking I'm about to get into a deep CS
lesson on how Nitro works, but I have something better this
morning. This is one of my favorite textbooks from my
undergraduate degree. It's an excellent book, and it's an
undeniable part of the CS canon written by a couple of
luminaries in our field. This is an image of my actual
textbook from undergrad, which I still have. This is the
second edition, and it turns out that's a bit dated. At this
point. The industry has changed a lot. In fact, the seventh
edition of this textbook just recently came out. And this
edition actually has a section that covers the Nitro system.
How cool is that? You can now actually learn about Nitro and
Graviton in this CS textbook. And to celebrate, we're going
to give away some copies of this book. This morning. I'm
going to put a QR code up on the screen in a second. If you
scan it, you can get a copy of this book. The first 1000
people here in the room can take this book home if you're
lucky. Ready? Here we go. Okay if you're lucky enough to snag a
copy, you'll be able to pick it up at the expo hall after the
keynote. But really, even if you didn't get a copy, everyone,
including our friends online, have one today because you
didn't need to sit through my CS lesson. All right. Nitro is
a great example of the deep investments we've been making
for the past 20 years. It's also the reason that AWS
started building our own chips, which now include graviton, our
custom AWS server process, and Trainium, our AI chip. So to
start off this morning, we'd like to tell you more about
graviton. And to do that, please welcome to the stage
Dave Brown. >> Well, as Peter mentioned
earlier, Nitro changed what people thought was possible in
The Cloud. It showed that if you could control the silicon,
the hardware and the system architecture, you could get
performance and efficiency gains that were simply not
available using commodity hardware. And as we spent more
time with ARM inside the Nitro system, a natural question
emerged. If custom silicon could improve network and
storage so meaningfully, why couldn't we apply that to
compute? And so we took a step back and asked, what if a
server processor, what would it look like if we designed it
specifically for Cloud workloads, not adapted, not
repurposed, but built for The Cloud from the ground up. And
that's where the graviton processor came from, a brand
new design based on delivering the best price performance for
workloads that customers run every day in The Cloud and
across industries. Organizations are getting
better performance and lower cost with graviton. Adobe is
cutting emissions by 37%. Epic Games is powering massive, low
latency global gaming workloads and Formula 1. One of my
favorite sports is running simulations at 40% faster.
Pinterest is lowering costs by 47%, and SAP has seen a 35%
performance improvement with their SAP Hana Cloud. Now,
these aren't just demos. These are production systems running
faster, cleaner and cheaper with graviton. And we've seen
the same enthusiasm from our software partners. They're
tuning compilers, reworking runtimes, optimizing libraries,
and building native support across their platforms for
graviton. And they're leaning in because they see clear
performance benefits, cost benefits, and a strong long
term architecture. And industry collaboration around graviton
continues to grow and mature, now delivering the best price
performance in EC2 takes attention at every layer. It
starts with building great performance into our silicon,
but it also comes from how we build and operate the systems
around that silicon. Because we designed both the processor and
the servers, we can optimize across the full stack, and that
includes something customers don't often think about cooling.
This is the traditional cooling approach that most processors
use. You have the silicon and then a thermal interface
material or TIM, and then a protective lid, and then more
TIM and then the heatsink. Now it's a reliable and easy to
manufacture, and it's been the industry standard design for
decades. But let's dig in a bit here because the physics is
fascinating. Heat transfer is straightforward physics. Every
layer in the thermal path slows heat movement, so more
resistance leads to higher junction temperatures and
higher temperatures, increases leakage and higher leakage
increases power consumption. It's an area where the
inefficiency can stack up really, really quickly. Now,
traditional CPUs use this design because they must
support many systems, many form factors, and many cooling
solutions, and that lid provides a stable interface.
But since we control the entire system for graviton, we had the
opportunity to think differently. So instead of
following the traditional model, we designed a direct to silicon
cooling solution. We removed the lid along with a layer of
TIM, and that reduced the resistance and allows heat to
move more efficiently. Now it requires precision
manufacturing and carefully selected materials, but the
result is meaningful. Our fan power drops by 33%, and
remember, we're only able to do this because we control the
entire stack. Now, improving system efficiency is just one
part of delivering great performance. The silicon itself
has to keep getting better generation after generation,
and chip development is both iterative and long term. Each
generation of graviton expands the set of workloads that we
can serve, and every time a new set of workloads comes along,
we learn where the next set of bottlenecks are and that
learning feeds directly into the next generation. It's a
continuous improvement cycle. Each graviton processor builds
on what came before it and continues to push the
architecture forward. Now, last year I talked about optimizing
graviton for real world application performance, and
with Graviton3, we saw that the L2 cache misses were having a
notable impact on real world workload performance. The cache
is one of the most important predictors of CPU performance.
And so it became a real priority area for us. When a
core needs data, it checks the cache first. Cache is small and
extremely fast, and it's designed to hold frequently
access data. And when that data isn't available in the cache,
the processor must go all the way out to main memory, which
is much, much slower. Now, modern CPU architectures use a
three level cache hierarchy L1, L2, and L3. L1 is the fastest,
L2 is larger but slightly slower, and L3 is larger still
and shared amongst the cores, now, missing all three levels
of cache means you have to go to the DRAM, which can take up
to 100 nanoseconds. That's a long, long time in CPU cycles,
and this is why we love big caches. The more data you can
keep close to the core, the fewer slow memory trips you
have to take. So with Graviton4, we doubled the size of the L2
cache from 1MB to 2MB per core, and that was one of the
contributors that led to graviton for delivering up to
30% better performance than Graviton3. And as you'd expect,
doubling the L2 cache significantly reduced L2 cache
misses, but designing a CPU is always about trade offs, so in
Graviton4 we also increased the core count by 50% and the L3
cache by about 12%. And that was the right balance for the
scale up workloads that we wanted to serve at the time.
But with more cores sharing, the relatively smaller increase
in L3 cache, each core ended up with less L3 cache than before.
And that's why we saw an increase in L3 cache misses.
And these are the kinds of tradeoffs that you're
constantly evaluating when you're designing silicon. And
also, we made a major architectural change by adding
a coherent link between two CPUs. And this allowed us to
deliver up to 192 vCPUs for databases and large analytical
workloads. But linking processes introduces new
latency paths. And when it needs to access memory on the
other CPU, the request has to move across that interconnect
and that adds latency, extra protocol overhead and sometimes
even queuing. And in certain scenarios it can take up to
three times longer. And so we asked whether we could deliver
192 cores with uniform fast access to memory and more cache,
all in a single package. And today we're excited to
introduce Graviton5. The Graviton5 delivers 192 cores in
one package, and provides over five times the L3 cache of
previous generations. And that means each core now gets up to
2.6 times more L3 cache, and that leads to better overall
performance and better consistency. And all of this
comes together in our preview of M9g instances, powered by
Graviton5. M9g delivers up to 25% better performance than M8g
and offers the best price performance in EC2 today. And
we're already seeing incredible results from some of our early
customers. Airbnb has seen up to 25% better performance.
Atlassian has seen 20% lower latency. Honeycomb.io has seen
36% better performance per core, and SAP will SAP has seen an
incredible 60% better performance on their OLTP
queries for SAP Hana in The Cloud. These are significant
real world improvements and they represent a major
generational step forward. And now I'd like to bring up a
guest who has been influential in shaping how developers build
on AWS. Please join me in welcoming the Vice President of
Cloud Systems and Platforms at Apple Payam Mirrashidi.
>> Thanks, Dave. Hi, I'm Payam Mirrashidi at Apple. We're
driven by the idea that the products and services we create
should help people unleash their creativity and potential.
We build some of the largest internet services on the planet,
and many of them run on AWS. My team works on services such as
App Store, Apple Music, Apple TV, and podcasts. The service
has billions of you use every day, and what I like to call
the fun stuff. We also build the underlying Cloud
infrastructure across AWS and our own data centers. That
makes it all possible. Wow. That's a lot of technology
power on one slide, and not just the kind you see in the F1
move, but the kind that powers experiences for billions of
users all over the world. And that's why we're always looking
for ways to optimize how we develop and deliver our
services. Now, many of you are navigating a hybrid world,
balancing your own infrastructure with the power
of AWS. And let me tell you, at Apple, we get that. We face the
same pressures and challenges you do. We're in a massive
operation. We're tackling the same problems scalability,
performance and reliability. And we're solving it with AWS.
Like many of you, my journey as a developer started with coding
in C, and then in 2002, when I joined Apple as an engineer on
the original iTunes store, where a Java shop. We're a
small team with big dreams that had to change how the world
consumed music. Over the years, we mostly stuck with Java and
when we needed more performance, we use C++. But it was, well,
cumbersome to develop and even more difficult to support at
scale in production. And as our services scaled, we also face
new coding challenges. The tools we had when always up to
the task. Now, around the same time, Apple's own operating
system team was creating Swift, initially the premiere language
for developing the apps you know and love on your iPhones
and Macs. Swift's performance, modern design, and built in
safety features reveal this potential for server side
development. Now I know introducing a new language,
especially on the server, can raise eyebrows, but with Swift,
a single developer can often handle both client and server
side. You can turn client side logic into a library, run it
server side, maintaining a single code base. The power of
having the same logic on both client and server is immense,
and I think you'll find it incredibly valuable for your
teams to. Today. Apple uses Swift to power everything from
Apple Silicon all the way up to the pixels rendered on your
screen. It's with this easy to learn scales beautifully from
embedded systems to massive architectures, and is perfect
for building distributed services or complex system
software. Apple is processing billions of requests per day,
with apps built in Swift running directly on AWS
Graviton. We've seen a 40% increase in performance and a
30% reduction in cost by rewriting core services in
Swift and moving workloads to graviton. The transition from
x86 has been seamless, with a near drop in replacement for
Java thanks to graviton. Apple moved to ARM more than a decade
ago to power our devices, and now we're seeing the same value
moving to ARM based graviton. To get more out of our
infrastructure, higher throughput means fewer
instances, lower costs, and a smaller footprint. A win for
our customers and for the planet. A great example is our
spam detection feature in iOS 26. We use Swift on Graviton to
scale the compute heavy operations behind the service
that helps us detect suspicious phone numbers while maintaining
privacy for hundreds of millions of users. In fact, the
messages app running on your phone, the spam detection
feature running on the server are using the same language and
scaling seamlessly. This feature is built with
homomorphic encryption using a Swift library that we open
sourced, enabling private and secure computation of data
without the server ever decrypting it. This allows us
to handle massive volumes of data and protect billions of
users with incredible speed. In an era of vibe coding and AI
development. The languages we choose are critical, so it's
legibility and safety. Make it a great addition to your AI
toolbox. Ten years ago this month, we open sourced Swift
and shared this incredible language with the world and the
response has been remarkable. Today, Swift is available on
Linux, windows, Android and more. It's embraced by a
vibrant community, and millions of developers globally are
building apps from everything from devices to data centers.
It's time to consider Swift for your next project. Check out
Swift.org for language that's fast, expressive, and safe.
Running on the next generation infrastructure of AWS and
graviton. And in case you haven't heard, there's now a
native Swift toolchain available for Amazon Linux the
first distribution to have an official package to the AWS and
Swift on server community. Thank you for your vision and
your partnership. I'd also like to thank Dave for having me
here today. We can't wait to see what you all create with
Swift on AWS Graviton. Thank you.
>> And thank you, Payam. The work that you and the team of
Apple have been doing with Swift on Graviton is really,
really impressive. Now, one of the biggest transformations
that The Cloud brought was how quickly companies could move.
Developers stopped waiting on hardware and instead could spin
up resources in minutes and even seconds. And that speed
the ability to experiment, to iterate, to fail fast and
hopefully succeed fast is now essential. And over the last 20
years, we've done more than just bring you faster computers.
We've given you our customers, faster building blocks and
tools that remove the undifferentiated heavy lifting
so that you can focus your workloads and time and
energy on what truly workloads and time and
energy on what truly differentiates your business.
Now, I want to take us back to 2013, a moment when a very
small group of engineers within AWS asked a question that
sounded almost impossible at the time. What if a developer
could just hand their code to AWS and have it run? No servers,
no provisioning, no capacity planning, no scaling? And the
engineers that came up with this idea, well, they weren't
even on the EC2 team because the EC2 team, myself included,
was deeply focused on servers, instance types, armies or
scaling groups, load balancers, and of course, putting Jitter
where it belonged. And when you're focused on servers, you
don't naturally ask the question, what if there were no
servers at all? But that was the breakthrough. The point
wasn't to make servers simpler, it was to remove servers from
the experience entirely. And you see, at the time, the S3
team was handling millions of thumbnails, profile pictures,
product photos, social media, images all pouring into buckets
across the the S3 fleet. And every time a new image arrived,
a lot of work had to be done. It had to be resized and
cropped and watermarked. Whatever the application
required. And to do that, customers had to run fleets of
EC2 instances and they'd pull the image from S3, they'd
process it and they'd push back the results. Now those servers,
the scaling logic, the orchestration was all managed
by the customer, and it was a ton of undifferentiated heavy
lifting triggered every time a new object arrived in S3. And
the S3 team had an elegant insight. If they attached a
little bit of compute directly to the storage layer, they
could run a small function the moment a new object landed. No
fleets, no data shuttling, and no orchestration. Upload an
image. Compute runs. Thumbnails appear. And that simple idea
bringing compute to data became the seed of something much,
much larger. And as the concept evolved, we realized that it
wasn't just about those thumbnails. This was a new
application model. Customers didn't just want to run the
logic. When a new image arrived, they wanted to react to
database events, log systems, IoT messages, API calls any
event that the system may introduce. And when we launched
Lambda in 2014, it changed the landscape for the first time.
Developers didn't start with servers. They started with code.
Lambda handled the execution, the scaling, the availability,
and the fleet. And you only paid when your code ran. And
Lambda wasn't just a new service, it was a new mindset.
And as customers immediately embraced it, startups moved
faster. Enterprises modernized workloads that had been stuck
for years. Event driven architectures, real time
processing, data pipelines, whole new patterns emerged. And
a decade later, Lambda still remains the fastest way to go
from an idea to production. And customers love it because it
removes so much of the operational weight. And of
course, as usage grew, people pushed Lambda into new
territories. So we kept expanding it. More runtimes,
container support, VPC networking, predictable
performance options, snapstart and function URLs all without
adding any operational weight. But as usage grew even further,
customers continued to push Lambda into new territory, and
they wanted access to the latest EC2 technologies. They
wanted predictable performance at very, very high scale. They
wanted more network throughput. They wanted submillisecond
latency, and they didn't want to trade away any of Lambda's
simplicity to get those things. And this created an inflection
point. Well, a couple of years ago, we brought the Lambda and
EC2 teams under one organization for the first time
ever. And when we did that, these two groups, one rooted in
servers and one rooted in serverless, started looking at
the entire space of compute together. And we began to think
of compute not as rigid boxes, EC2 containers, and serverless,
but as a spectrum of choices. And that naturally led us to a
deeper question what is serverless? Is it no service?
Is it no operations? Is it? Don't make me think about the
infrastructure. Is it just run my code? Well, customers were
telling us something clear we love Lambda because we don't
have to manage infrastructure, but we want control over the
performance. And we do want access to the hardware that we
need. And so we asked ourselves another bold question. Could we
preserve everything that customers love about serverless?
Serverless. The simplicity, the automatic scaling the
operational model while giving them the performance choice of
EC2. And this week, we thrilled to answer that question with
Lambda managed instances. Lambda managed instances
elegantly bridges the gap between serverless simplicity
and infrastructure control. With managed instances, your
Lambda functions run on EC2 instances inside your account,
and Lambda manages the provisioning, patching,
availability, and scaling. You choose the instance type, you
choose the hardware. Lambda handles the rest. It's the next
evolution of serverless compute. And the best part? Your
existing Lambda functions continue to work as is. No
rearchitecture, no code changes, and no operational burden. You
get the performance characteristics of EC2 with the
developer experience of Lambda. And we think this opens the
door to workloads that historically lived outside
Lambda. Video processing, ML pre-processing, high throughput
analytics. And I'm sure there are many, many more. Lambda
Managed Instances isn't a departure from serverless, it's
an expansion of it. It brings more choice, more performance,
more capability to customers without adding any operational
weight. You see, serverless was never about the absence of
service. It was always about the absence of server
management. It's about removing the heavy lifting so developers
can focus entirely on their code and their business logic.
And with managed instances, we're pushing that vision
forward, giving builders the power of EC2 with the
simplicity of Lambda and letting them move faster than
ever before. Now, over the last year, we've seen a major shift
in the types of workloads that customers are running.
Inference is obviously moved to the center, and it behaves very
differently from traditional compute patterns that we've
been optimizing for for over the last two decades. And as we
dug into these workloads, it became clear that the
elasticity that customers rely on in The Cloud doesn't
automatically transfer over to inference. And so we've been
focused on how do we deliver that same flexibility,
responsiveness and efficiency that customers expect from AWS.
Even in a world where demand can spike instantly and the
cost of getting it wrong is incredibly high. And to
understand why inference is such a hard problem, you have
to look at what happens inside a single inference request. Now,
this is not just take text in, get text out. It's a four stage
pipeline. Tokenization prefill decode detokenization. And each
stage stresses the system in different ways. Tokenization
breaks the input into tokens that the model can understand.
Prefill processes that full prompt and builds the key value
cache that the model will use during the decode stage. The
decode generates the responses one token at a time, guided by
that key value cache, and then Detokenization turns those
tokens back into a language that we can understand. And at
any moment you're running workloads that are CPU bound,
GPU compute bound, memory bandwidth bound, and latency
sensitive all at the same time. And some requests are tiny.
Others involve huge documents. Some must return immediately,
and others can take their time, and the resource profile of a
single request changes dramatically as it moves
through this pipeline. Now imagine doing all of this at
global scale. Thousands of customers, millions of requests,
dozens of models, each with different shapes, sizes and
urgency. It's a completely different scaling challenge.
And to do it well, you need an architecture that can adapt in
real time. Now, if you were building an inference service
from scratch, you might start with an architecture that we
all know, a load balancer and a fleet of accelerators. And that
model works well for many applications. It's a proven and
effective pattern of for traditional web services. And
when we built Bedrock, we started with some of these
proven patterns. And they served you well. But as models
evolved and usage grew, it became clear that inference
needed a different architecture. So we went back to the basics
and asked if we were designing an inference service. Today,
with everything that we now know about running real
customer workloads at massive scale, what would it look like?
And that's what's led us to Project Mantle, a new inference
engine that now powers many of Amazon Bedrock models. And one
of the biggest insights was that not all inference requests
have the same urgency. And so instead of AWS guessing, we
wanted to allow customers to tell us. So we launched Bedrock
service tiers, allowing customers to assign their
request to one of three lanes priority for real time latency
sensitive interactions, the standard for steady and
predictable workloads and flexible background jobs with
efficiency matters more than speed. And this lets customers
optimize what they care about, and it lets us allocate
resources more intelligently. And the result is consistent
low latency for priority workloads while still driving
optimized, optimized performance across everything
else. And the second big, big challenge that we addressed
with Mantle was fairness. In a shared system, one customer's
burst shouldn't degrade the performance of others. The
Bedrock solves this by giving each customer their own queue.
Your performance is determined by your usage, not someone
else's. And if another customer spikes, it affects their queue,
not yours. And because Bedrock learns your typical usage
patterns, it anticipates how much capacity you're likely to
need and ensures that it's available when you need it.
This combination of queue isolation and adaptive capacity
sharing gives customers much more predictable performance,
even under heavy load. And when you put all this together
prioritization, fairness, smarter batching, better
scheduling, you get significant gains. Latency becomes more
consistent, throughput increases, utilization improves,
and the overall system becomes more resilient. But to make
this architecture fully reliable, especially for long
running requests, we needed one more component a durable record
of work happening across the fleet. And we call this journal.
The journal already powers service services like DynamoDB
and S3 today. And it's a highly reliable and durable
transaction log. Inference requests can run for a long
time, and if something fails, whether that's a hardware fault
or a networking issue or maybe just a retry, you don't want to
restart the entire request that wastes compute and increases
latency. Now, with Journal, Bedrock continuously captures
the state of each request. If something goes wrong, you can
resume exactly where you left off. And this makes the system
far more fault tolerant. And it also enables advanced
scheduling strategies that weren't possible before. And
one of those advanced scheduling strategies is fine
tuning. The fine tuning is super compute intensive and can
take hours. A traditional systems require separate
training environments, separate schedulers that often sit idle
waiting for load. WAN Bedrock fine tuning becomes just a long
running job if a surge of real time traffic arrives, the fine
tuning job pauses. And when that surge subsides, it resumes
right where it left off. And this now gives customers access
to incredibly efficient fine tuning right within Bedrock,
without having to manage training clusters or worry
about wasted compute. And as we redesigned the inference engine,
we also raised the bar on security and privacy. And as
Nitro was done and transformed EC2 by creating a secure,
isolated environment for compute, the Bedrock integrates
confidential computing to protect model weights and
customer data during inference. Data always is encrypted and
operators can't access the environment, and customers get
cryptographic assurance that their requests ran in a
verified and trusted place. Now, for organizations with strict
privacy and compliance need, this is a huge step forward.
And because we have a strong, consistent, reliable foundation,
we can integrate it deeply with the rest of AWS. We've added
tool calling support so your model can invoke Lambda
functions for real time, real time data directly from Bedrock.
We've added support for OpenAI's responses API for long
running jobs, and we've integrated with IAM for
permissions and CloudWatch for observability. All the things
that enterprises rely on to run their most important workloads.
This isn't just about model hosting. It's a fully managed,
production ready platform for Generative AI, and everything
we've built in Bedrock reflects what we've learned at operating
services at massive scale for over nearly two decades now.
Inference is a new kind of compute. It has its own scaling
patterns, its own constraints, and its own requirements. And
Bedrock gives us and you, our customers, the foundation to
run those workloads reliably, efficiently and securely. And
behind every API is a sophisticated engine doing
scheduling, fairness, resilience and performance so
customers can stay focused on building. You see, that's what
we do at AWS. We take on the hard problems, we solve them,
and we give customers the tools that they need to invent the
future. And with that, let me hand it back to Peter.
>> All right. Thank you Dave. Now, I know Dave talked about
innovating faster already, but we like innovating. So I'm
going to talk a little bit more about that. One of the ways
that we like to innovate faster is by giving you access to
important new capabilities across our broad range of
services. And I think a great example of this is the work
we've been doing to enable vector search across AWS. Now
this is a picture of Smokey or smug or SmugMug as he likes to
be called. You can see this isn't just the picture of
Smokey, and when we look at it, we don't just see pixels, we
see physical attributes. Bat ears, big tongue. We also see
that expression that says, I know what I did, I don't care.
Your brain processes all these concepts and ideas
simultaneously, and it understands the relationships
and then it connects it to other things. Perhaps you're
thinking about your dog, or perhaps you're thinking about
that messy eater you're sat next to at dinner last night.
These associations are sometimes strong and obvious,
sometimes subtle. That's what humans do. And vectors allow
computers to work the same way. The simplest way to think about
a vector is a data point that places it in mathematical space.
And our contrived example here I have three dimensions. One
represents color, another represents size, and another
shape. And you can see now that you can place images or ideas
on these three axes. Now the exact location of the where
things get placed is not so interesting. What's interesting
is the relative location of the vector to other vectors. Very
different objects like Christmas ornaments and apples
or tennis balls and limes might end up close together. And it's
these associations that are interesting in a vector search.
Of course, what we have here isn't going to reveal anything
particularly interesting, but that's because we have a very
simple, contrived example. In the real world, vectors are far
more than three dimensions. In fact, a rich vector encoding
space today might have 3000 dimensions. You can see we
struggle to illustrate that here. And each dimension isn't
something as simple as size or color. It's actually an
undefined concept entirely, something itself generated by
AI a special kind of AI called an Embedding Model. Now you
train an Embedding Model on lots and lots of data, and the
model itself starts recognizing patterns. It learns about
different types of dog ears and different shapes. And with
enough data, it learns to cluster these objects together
in that mathematical space. Sometimes an obvious, but other
times surprising ways. And so, for example, you might be
wondering, well, what do we do with these vectors? Well, as I
said, the most interesting thing about vectors is when you
search them in a database. So this is where unlike a
traditional database that just stores rows and columns, a
vector database is built specifically to find nearest
matches to these vectors. So you encode your query and then
it finds objects in the database, other vectors that
are close to that.  So in our example all the
French bulldogs might be clustered in one place and all
the other dogs might be clustered nearby. And cats. I'm
not sure where the cats are clustered. Who cares? But maybe
the ones that like to destroy their toys are next to the
French bulldogs. All right, so let's look at what vectors can
do in the real world. Think about all the data your company
has right now. Your institutional knowledge isn't
organized into rows and columns that can be inserted into a
database. It's buried in PDFs. It's captured and recorded
video calls. Maybe there's some pictures of whiteboards that
people have written down. It's scattered in documents across
dozens of systems. And the challenge probably isn't that
you don't have the data you need. The problem is you can't
find the data you need. And now you might be thinking, well,
creating a vector database might be a great way to find
that database. And that is true. But unfortunately there's a
challenge. Existing embedding models are highly specialized
to handle certain types of data images or text. And so if you
want to benefit from the wealth of unstructured data you might
have, it means you likely have to combine models. But the
catch is you can't really combine models because you
can't search vectors across different embeddings models,
because those abstract dimensions that we talked about
likely hold entirely different concepts. So this is precisely
the challenge that we set out to handle with the new Nova
Multimodal Embeddings model. Now, this is a state of the art
embeddings model that support text, documents, images, video
and audio. And it converts all of these concepts into a shared
vector space, creating a unified understanding of your
data. And better yet, the Nova Multimodal Embeddings model
does this all with industry leading precision. But now
having a great Embedding Model is only part of how we're
enabling you to use vector search on your data. You see,
the real magic happens when the vector search capabilities are
available on all of your data wherever it lives. If you think
about how your teams work today, they're already deeply invested
in specific databases and analytics platforms. And when
vector capabilities are built directly into these services, a
couple of great things happen. First, they don't need to
invest time and energy to learn a brand new vector database.
And you don't need to pay for something entirely new. So you
get Agility and cost savings. And this is why at AWS we're
approaching vectors, the way we approach everything with both
breadth and depth of capabilities. You don't need to
learn an entirely new technology stack or manage a
complex data pipeline. We've integrated vector capabilities
across our services. Let's take a look at OpenSearch now.
Amazon OpenSearch has long been a backbone of search and
analytics, and it's well known for its exact match
capabilities. But you're not just looking for exact match
capabilities anymore. You want to ask questions in natural
language and get intelligent responses. But that doesn't
mean you want to give up the ability to run an exact match
search, either. So today, OpenSearch has evolved into a
vector driven intelligence engine. With OpenSearch, you
don't have to choose between a traditional keyword search or a
semantic search. Hybrid search gives you the keyword based
precision, and semantic search allows you to get even better
results. Now you're probably thinking OpenSearch is a fairly
obvious place for us to add vector capabilities, and I'd
agree. In fact, we've added vector search capabilities to
most of our database and analytics services. But we've
also asked what would it mean if we brought the power of
vector search to our largest data service? And with S3
Vectors, we brought the cost, structure and scale of S3 to
vector storage. And this actually did surprise a few
people, even those that know vectors quite well, because
this isn't easy. What's great is you can create a vector
index the exact same way you can create an S3 bucket, and
this enables you to build vector databases of any size.
With the simplicity of storing data in S3, no provisioning
works at any scale. You pay for only what you use. It's that
simple. Now, earlier this week, Matt announced the GA of S3
Vectors, which included some significant improvements to
query performance and scale. It turns out that searching for
the closest vector in a high dimensional space on a massive
vector database is really hard to find. The nearest neighbor,
the exact nearest neighbor. You essentially have to compare
every vector in your database to the search database, and
that requires doing lots of math over all those dimensions.
Even in a smaller database where you keep everything in
memory, this is often too expensive. So instead you
typically employ something called an approximate nearest
neighbor algorithm. And there's a lot of innovation in these
algorithms today. They're super interesting. They don't
guarantee the absolute closest vector, but they do pretty well.
And they scale much, much better. But the challenge that
we have with S3 is we aren't storing all these vectors in
memory. We're storing them in more economical storage with S3.
So how can we provide really low latency on search for
vector databases that grow into the billions of vectors and
need to run on S3? The approach the S3 team developed is to
pre-compute a bunch of vector neighborhoods for every vector
database. A good way to think about a vector neighborhood is
a place where a bunch of vectors are clustered, 
perhaps French bulldogs or cats that destroy
their toys, and these neighborhoods are computed
ahead of time offline, so they don't impact your query
performance. And every time a new vector is inserted into S3,
the vector gets added to one or more of these vector
neighborhoods based on where it's located. Now, when a user
goes to execute a query, a much smaller search is done to find
the nearby neighborhoods. This is then just the vectors that
were in these vector neighborhoods are loaded from
S3 into fast memory, where the team then applies an
approximate nearest neighbor algorithm, and this can all be
done quite quickly, and it returns really good results.
How well does this work? Turns out really well. We're seeing
sub 100 millisecond query times with vector databases with 2
billion vectors in production. That's the scale and
performance of S3 Vectors. And it's going to open up all sorts
of new use cases for customers. The response to S3 Vectors has
been great in just four months since we put it out in preview.
Over 250,000 vector indexes have been created, and we've
ingested more than 4 billion vectors and performed over 1
billion vector searches. Now, this type of adoption tells us
we're on to something and we're solving a real customer problem.
And one of those early customers is using S3 Vectors
to understand video the way humans do. Please welcome to
the stage Jae Lee CEO and co-founder of TwelveLabs.
>> Thanks for having me, Peter. I'm incredibly excited to be
here today. So excited. In fact, I wanted to watch all of
Peter's past keynotes to prepare. But to be honest, I've
been really busy running TwelveLabs and needed help. So
I decided to have our models watch the keynotes for me. I
indexed over 12 hours of keynotes from the last eight
years and asked our models to analyze them to pick out the
key insights to learn more about them. First, I asked,
what are Peter's favorite topics to talk about? Thanks a
lot, and I learned really quickly that these are his
favorites. Then I searched for the clips where Peter is
talking about these topics, and it was really easy for me to
find and watch specific clips from each of his keynotes. Now,
what started as a fun way to do my research was actually a
perfect example of what TwelveLabs does every day,
turning hours of video into structured intelligence. We're
living in a world where about 90% of data today is
unstructured, and most of that by far comes from video. But
even though video is the biggest source of data, it's
also incredibly complex. It combines visuals, audio,
movement, and most importantly, time. Now, combine that across
petabytes of footage in industries like media,
entertainment, law enforcement, and enterprises of every kind.
That's millions and millions of hours of video. Did you know
that 1,000,000 hours of video is equivalent to 114 years? If
you watch this straight through, the scale is absolutely
staggering and finding meaning in it, finding the moments that
matter is even harder. At TwelveLabs, we're building
Foundation Models that understand video the way humans
do, not as a sequence of frames or transcripts, but as a
unified story across sight, sound, and time. Our models,
Marengo and Pegasus are some of the heaviest multi-petabyte
scale video AI workloads in the world, running inference on
millions of hours of video Marengo is our multi-modal
Embedding Model that powers precise video search and
retrieval. Our latest version, Marengo 3, allows you to find
the moments that matter across your massive archives, using
any to any modality. Search Pegasus. Our video language
model turns video into insights. It performs deep analysis and
excels at generating text like summaries, captions, or
metadata to power downstream video workflows. Now we'd like
to say TwelveLabs was born on AWS. From the beginning, the
AWS startup programs and credits literally changed our
trajectory. Those credits didn't just help us train
models, they gave us the momentum to productize our
research, running our stack on AWS shortens the distance
between innovation and deployment for us. The backbone
of our data infrastructure is on Amazon S3. When a customer
sends requests to one of our model APIs on the TwelveLabs
platform, the the system seamlessly ingests, indexes and
embeds video and petabyte scale without ever moving their data
out of S3. Now, with as capable as our models are, they require
equally competent vector storage. What unlocked
innovation for our Marengo model was the integration of
Amazon S3 Vectors to deliver an optimized video intelligence
offering at scale. Now, vectors are at the heart of what we do.
Each scene audio segment, text and video gets encoded by
Marengo into a multi-dimensional vector
embedding that captures semantic meaning across space
and time. Now what does that look like? Let's assume for a
single audio video that's thousands of vectors now, but
we're talking about customers processing millions
of hours of video. That's processing millions
of hours of video. That's billions of embeddings. Well.
These embeddings flow directly into S3 vector indices. No data
migration, no reacrchitecting the infrastructure. The same S3
buckets already storing the source video now store the
embeddings that make it searchable with the same
durability and scalability guarantee. For example, when a
user types a natural language query like people watching a
space shuttle take off from a distance, the query gets
embedded by Marengo into the same vector space. S3 Vectors
then performs an approximate nearest neighbor search across
billions of stored embeddings, and returns video results with
metadata like video IDs and timestamps that pinpoint the
the moment that matter, the moment that matched the query.
From there, our customers can take these video results and
use them to power downstream video tools and workflows. Now
one of our customers, ArcXP, is a perfect example, an extension
of the Washington Post. They provide a media management
platform powering news organizations around the world.
Built on S3, ArcXP enables editorial teams to not only
store and manage their massive archives, but now they can
personalize the stories they create with it. Now, a single
video or article can be transformed into tailored
variations of for for different audiences. They leverage
TwelveLabs models to quickly analyze and enrich archived
video content and discover related clips to build new
stories. That is what accessibility means to us, not
just API's, but infrastructure on AWS that makes video
intelligence viable at any scale. Our partnership with S3
enables us to deliver an incredibly efficient product
offering directly to our customers infrastructure. Now,
given the scale of the data we handle, that has a meaningful
impact on our customers. Unit economics, which unlocks new
possibilities. I started by telling you I used our own
models to prepare for this keynote. That's not just a demo
trick. For decades, video has been a write only medium, but
now we capture everything. Every game, every meeting,
every moment. But we couldn't find it, learn from it, or
build on it. Today that's changed. We're turning the
world's video into knowledge that's actually usable. Every
organization has their own version of Peter's keynotes
institutional knowledge trapped in video footage that could
teach you something if you could only ask it a question.
And now you can. We can't wait to see what you build. Thank
you. >> Thanks, Jae. It's fun to see
those old videos. All right. Earlier, Dave covered the work
we're doing with graviton to lower cost and improve
performance. And there's no place where making deeper
investments in our infrastructure than supporting
AI workloads, and that the reason is pretty easy to
understand. AI workloads are growing explosively and running
these workloads is expensive, power hungry, and capacity
constrained. And that's why we built Trainium. Trainium
supports almost every imaginable AI workload. Our
naming convention is not ideal, but as you've heard, Trainium
is optimized for both training and inference. And if you're
using Anthropic models, whether from Bedrock or from their one
P, you're probably already benefiting from Trainium.
Trainium supports the full spectrum of model architectures,
from dense transformers to Mixture of Experts to State
Space Models, and it supports all sorts of modalities text,
image, video, you name it. Simply put, Trainium can handle
every AI workload that you want to run today, and anything you
can imagine building. And Trainium supports all these
workloads with great performance. Performance can
mean lots of things. It can mean building the largest
training cluster like Project Rainier, or it can mean
processing an inference request and generating your answer as
quickly as possible at the best possible efficiency. There's
lots of ways to optimize performance, but Trainium gives
builders the tools to deliver great performance with their
models and applications, and Trainium supports these
workloads at meaningfully lower costs. As you've heard this
week, Trainium3 will provide up to 40% lower cost than even the
most demanding AI workloads 40% lower cost. That's a big deal
when you're spending tens of billions of dollars on
infrastructure. Let me show you a little bit more about how
we're achieving this, okay? This is our second generation
Trainium UltraServer. An UltraServer is where we combine
lots of Trainium servers into a single AI supercomputer. And
this second generation is a significant step forward from
the first generation we launched last year. First, it's
based on Trainium3 chips and lots of them. There's 144
Trainium3 chips across two racks combined into a single
UltraServer. But I want to draw your attention to the devices
in the middle of these racks. Those are neuron switches, and
they're used to interconnect all the Trainium3 chips in this
rack to create that one massive AI supercomputer. But these are
not your typical network switches. These switches are
specifically designed to provide full bisectional bandwidth
at extremely low latencies directly to those training
chips. So what kind of performance can this provide?
Well, the key performance dimensions that matter in AI
supercomputers are compute and memory. And this UltraServer
has a lot of both 360 PetaFLOPS of eight bit precision floating
point compute and 20TB of High Bandwidth Memory with 700TB per
second memory bandwidth. That's 4.4 times higher raw compute
performance and 3.9 times more bandwidth than last year's
Trainium UltraServer, and this makes it one of the most
powerful AI supercomputers available, allowing us to run
or build even the very largest models. Let's take a closer
look. These are just sticker stats. And those of you that
heard me, you have to look deeper than the sticker stats.
So let's take a closer look at the Trainium3 server and chip
to understand how they're able to deliver great performance
and differentiated cost. Okay, this is one of the Trainium
sleds. You could pull this right out of the UltraServer.
There's 36 of these sleds interconnected with all those
neuron switches in one of those UltraServers. Now let me point
out a few really cool things. First, this represents our
first system where we use all three AWS custom designed chips
on the same server board. You'll see the four Trainium3
accelerators are located on the far end of the board, and right
next to those is a graviton processor. Now graviton gives
us the high speed I/O necessary to keep these accelerators busy.
And by having graviton co-located on the same sled as
the Trainium, we avoid the need for a dedicated head node in
our rack. And that gives us additional space to build an
even bigger UltraServer. Additionally, having that
graviton server there lets us do maintenance on just this one
sled without taking the other sleds out of production. And
that has the benefit of keeping our capacity where it should be
in production. Running your code. And speaking of
maintenance, another key differentiator you can see here
is everything is top serviceable on this sled. This
is unique with an AI server. And it's this design pays
dividends in a few ways. First, it enables entirely robotic
assembly of the server. And that lets us put these Trainium
chips into our fleet faster. And second, when we need to
service these systems in production, we can do it
quickly and efficiently. Okay, finally, you'll see that we
have two Nitro cards to provide very high speed networking.
Nitro enables EFA or Elastic Fabric Adapter, which enables
Trainium servers to share memory with thousands 
of other Trainium servers directly reading and
writing from each other's memory over encrypted channels
with built in network multipathing and fault
tolerance. Now that's exactly what you need. If you want to
build a massive training cluster and build a big model.
Of course, building a great system is only part of the
story. You need a great chip. Dave talked about this earlier
this morning, but you don't just wake up one morning and
decide you want a great ship. Building. A great chip is the
result of relentless execution over a long period of time. And
that's what we've been doing with Trainium. We've been
working with our customers, internal and external, for many
years. Every time we build a new chip, we learn from how
customers use it and that learning fuels our future
generations. A cycle of customer driven innovation. And
we don't focus on benchmarks. We focus on real customer
workloads and find innovative ways to make those workloads
more productive. So what does that look like? On Trainium?
We've added a number of Microarchitectural capabilities
to Trainium. Optimizations like this don't show up on the
sticker, but all of these new optimizations make Trainium run
more efficiently. Solving common Machine Learning
problems. Take micro scaling, which allows you to use lower
precision floating point numbers while preserving the
accuracy of the models. The larger parameters, or faster
softmax or tensor dereference or background transpose. These
optimize common AI computing problems and free up the
compute engines to do other work, or take things like
traffic shaping, memory add right memory, hash spraying.
These make your memory and network more efficient, and
that keeps your Trainium chips fed with the data. Because
while AI chips might provide hundreds of flights of floating
point calculations on their spec sheet, that only matters
if you can keep the data flowing into the compute
engines. Now, almost every AI workload that we're aware of
will benefit from one or likely multiple of these new chip
capabilities. And this is a good time to mention that it's
not just about having the best chip or the best hardware. You
need the right tools to build on that hardware, and this is a
place where investing deeply to differentiate Trainium for
customers looking to extract every bit of performance they
need to control things like memory allocation, pipeline
depth to maximize the performance of their workload.
Our solution here starts with NKI or the Neuron Kernel
Interface. It's a language that combines the simplicity of
matrix operations with direct instruction level access to all
of Trainium hardware capabilities, all done inside a
familiar Python programing environment. Those features we
just looked at are all accessible from NKI. Take
Decart AI, for example. That's the company that built the cool
application that turned me into a cartoon of Werner earlier
this morning that was running on Trainium3 Decart AI used NKI
to optimize their real time video generation models on
Trainium3, and reported drastically faster performance
on Trainium3 than any other hardware platform they tested.
And they told us the optimization process with NKI
was quick and intuitive. Now they're going to be up on stage
in a minute to tell you more about this. Which brings me to
today's update on NKI. NKI is going to be generally available
in Q1, and we're really excited to get this powerful tool in
more of our customers hands. We're also open sourcing all
aspects of the neuron NKI stack. Nothing is worse than a
compiler surprising you. When Nothing is worse than a
compiler surprising you. When you're working. And so having
complete visibility into the compiler and the code stack is
going to make it even easier for you to get maximum
performance from the hardware. Now, if you've ever worked on
deep performance engineering, you know that your best friend
is strong coffee and a great profiler. A profiler lets you
see what's happening on the hardware in detail. Where are
the bottlenecks? Where should I focus my attention? That's
exactly what we provide with the neuron profiler. But here's
what makes it special. Trainium has dedicated hardware
capabilities on the chip for profiling your code without
impacting performance, and this means you can profile actual
production code running in in a real environment, and you can
get instruction level precision. So that means you have all the
information you need to optimize your code. And today
I'm excited to share that we've taken it one step further with
Neuron Explorer. Neuron explorer takes all that
detailed profiling data, and it presents it in an intuitive
interface that makes it easy to understand what's happening and
to identify opportunities for improvement. In fact, Neuron
Explorer automatically detects your bottlenecks and suggests
optimizations. This allows you to spend more time fixing
things and less time hunting for problems. Okay, we've
looked a lot at how we are investing for great performance
for Trainium3 and the tools you can use to achieve that, but
let's look at those actual performance numbers. Here's the
open source GPT-OSS 120 billion parameter model from OpenAI,
running on both Trainium two UltraServers and Trainium three
UltraServers. Now, as I mentioned, the Trainium free
UltraServer has 4.4 times more compute than that Trainium two
UltraServer. So to make this a fair fight, we normalized
everything to output tokens per megawatt. And look at these
gains five x higher output tokens per megawatt while
maintaining the same user visible latency. This should
give you a sense about why we're so excited about Trainium
three. By the way, for those of you interested in going deeper,
we'll be open sourcing this code, including the relevant
NKI kernels so you can learn from it and reuse it. I've
covered a lot about how we built Trainium to run any AI
workload you can throw at it, and how we're working to make
it possible to get differentiated performance and
lower costs with Trainium. But we have been working on one
more really important thing that's making it easy for
everyone to use Trainium without having to learn a whole
new chip and a whole new programing language. And that's
why I'm thrilled to share that Trainium is becoming PyTorch
native. What does this mean? Well, let me show you. We'll
port some code. Okay, here's the code that's running our
model on our trusty NVIDIA GPUs. Now, if we change the simple
line from two Cuda to neuron, we're ready to run on Trainium.
That's it. That's all it takes. Now everyone researchers,
students, even Dave can use Trainium without having to run
a brand new software stack. Okay, this seamless integration
is made possible by phenomenal work from the PyTorch team,
allowing us to support different backends. We already
have this working with some customers, and we expect to
release it broadly early in the new year. Of course, the most
exciting thing about building chips is getting them in our
customers hands. And with Trainium3, we're delighted with
the early feedback from our customers, and our partnership
with Anthropic is a great example of our deep
collaboration with customers that's helping us produce
leading AI accelerators, but we're also excited about some
of the innovative startups that are doing new and exciting
things with Trainium right now. I want to bring one of those
customers on stage already building with Trainium3 and NKI.
Please join me in welcoming Dean Leitersdorf, CEO of Decart.
>> Thank you Peter. >> And it's exciting to
announce what we've been working on together. Today I'm
going to show you something that's completely new,
something the world hasn't seen before. It's a new category of
GenAI Foundation Models called real Time Live Visual
Intelligence. Take a look at the screens to my left and
right. We're all here right now at re:Invent. But what if we
want it to be all powered up? Earlier, when Peter walked on
stage, he looked like Werner and that was our model's art.
Decart Foundation Models running on Trainium3 live.
Every pixel you see right now is being generated on this
stage in real time. At Decart, we're an efficiency first AI
research lab, and we're building foundational models
for visual intelligence. Vision is how we see the world.
It's how we communicate. It's how humans understand each
other, and it's how robots will be able to understand our world,
to train themselves in generative simulations. This
this is what video and world models are all about. And it's
happening right now live. Because for the first time, we
could take foundational models for LLMs and video diffusion
models and get them to run at the same time with zero latency.
Trainium3 has been a huge enabler for our workload, and
creating this new GenAI category of real time visual
intelligence. At Decart, we have a lot of proprietary IP
that allows us to train and inference models much faster
and more efficiently, and we worked closely with the AWS
team to port our model stack, to port our infrastructure to
Trainium, to let us work with Trainium for building models
and running them. And we optimize it all using NKI
language, which Peter just talked about, and it made the
transition just much faster than what we expected. I'm
talking that we're on a path to getting to four x, better
performance in frames per second than what we can do in
state of the art GPUs. It's 80% Tensor Core utilization. These
are metrics we just don't hear of in AI. Now, the reason we
get this performance, it's a it's a result of how we combine
Trainium and our models. So the models that we train at Decart,
they have three components. An LLM that does reasoning
understands the world, a video model that understands pixels,
it understands structure, and an encoder that lets the the
two connect and run together. So usually we have to run these
in sequence one after the other. But we're able to build a
Trainium megakernel that we wrote and it got it to run all
three at the same time with zero latency on the same chip,
achieving maximum HBM memory utilization, tensor engine
utilization all at the same time with no latency. We're
already seeing how our models are changing how we behave
online. On Twitch, we have streamers that create new,
compelling experiences with our audiences. In shopping. Imagine
you see this cool lamp, and before you buy it, you see it.
Next time you watch a movie, it gets placed in that movie just
for you. We're trying to make sure that every product before
you buy it online, you can try it on on yourself and your home,
see what you feel about it. See how it looks. One of the
experiences I love most is basketball. So you're watching
the game and to keep your kids engaged, you let them watch the
Decart AI cartoon version, which is being generated live
from the match. We're taking AI and we're putting it into live
sports in the arena, in your living rooms for gaming, we're
creating a completely new foundation where it's games
that generate themselves as they're being played. And
frankly, everything you just saw, all these experiences, we
didn't come up with them. It was builders. It was developers
that took our API. You guys know your industry's way better
than we do, and you can understand how to take these
models and extract value out of them for your customers, for
your industries. If we step into the future step a few
years of the future. I really believe in taking this tech to
robotics and simulations. Robots are already using models
like this to envision infinite possibilities, infinite
outcomes on the road, in homes, factories, manufacturing, and
in the future, we'll be able to train robots fully in
generative simulations before they ever hit the ground. And
when they hit the ground, they will use live visual
intelligence to understand the world around them, to
understand the human environment. I'm really excited
to be here and announce with AWS this new category of GenAI
Live Visual Intelligence. We're taking it to every industry,
every market at any scale on powered by Trainium3 using the
cart models. Everything we build, we put it on our API.
Every few weeks, we launch it at our mobile app and the world
is shifting for the first time. We can take stuff that's in our
imagination and connect it to what we see with our eyes in
reality. Live. I really can't wait to see what all of you
build with it. Thank you all. >> All right. Thanks, Dean.
Well, we started out this morning by asking what AI means
for our infrastructure. And after everything we've explored,
I hope the answer is clear. The fundamentals matter more than
ever. Security. Availability. Elasticity. Agility. Cost.
These aren't relics of a pre AI world. They're the foundation
upon what the future applications will be built on.
The investments we've made from Nitro to Graviton to Lambda
weren't just about solving yesterday's problems. They were
about preparing for exactly this moment. Today you saw what
that preparation looks like. Graviton5 delivers 192 cores in
a big Ole cache. Lambda managed instances, expanding the
meaning of serverless vectors, becoming the connective tissue
of your data, and Trainium3 bringing great performance and
lower cost to every AI workload you can imagine. But here's
what excites me the most. It's still day one with AI. There's
going to be twists and turns that none of us can predict.
New architectures will emerge. New possibilities will unfold,
and AWS will be here, just like we've been for the past 20
years. Removing constraints, providing building blocks, and
helping you navigate whatever's next. So what will you build
next? But first remember, don’t miss the closing keynote with
Werner. Thank you and enjoy the rest of your week.
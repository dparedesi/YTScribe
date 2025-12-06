---
video_id: tlNxhm9LF4U
video_url: https://www.youtube.com/watch?v=tlNxhm9LF4U
is_generated: False
is_translatable: True
summary: NBCUniversal Sky's transformation of their global streaming platform through Redis Cloud demonstrates how strategic architectural redesign addressing performance bottlenecks, cost inefficiencies, and scalability limitations can unlock product innovation while reducing operational complexity, specifically solving the challenge of managing millions of bookmark operations per second across their worldwide streaming audience through intelligent data tier separation and managed service adoption. The original architecture relied heavily on self-managed Cassandra as a monolithic persistent layer handling both real-time bookmark updates and historical data storage without caching buffers, creating constant high-cadence pressure where every page load generated potentially millions of reads and every content interaction triggered immediate writes, resulting in infrastructure strain that prevented meeting critical product requirements like expanding bookmark retention periods and scaling for major live events, with attempts to migrate to AWS Keyspaces blocked by the same fundamental scalability limitations. Redis Cloud emerged as the solution after evaluating Redis Open Source, which offered core capabilities but required significant operational overhead for maintenance, scaling, and expertise at Sky's global scale, while Redis Cloud's fully managed service eliminated operational burdens through auto-scaling as the biggest differentiator, allowing development teams to focus on features rather than infrastructure management, cross-region replication with minimal latency supporting global deployments, two-second flash-to-disk capability ensuring data durability without manual intervention, support for modern data structures including hash, JSON, string, and sorted sets enabling massive cost savings, TTL-based eviction policies automatically cleaning clusters and simplifying cache management, and hybrid search capabilities positioning the platform for future generative AI applications. The reimagined architecture implements Redis Cloud as an intelligent caching layer with dual-cluster design separating write-heavy string clusters handling immediate bookmark updates at full ingestion cadence with O1 time complexity for rapid deduplication operations, while sorted set clusters maintain ordered views functioning like leaderboards that process data separately without impacting customer-facing reads, with a background service asynchronously persisting mature bookmarks to AWS Keyspaces long-term storage after at least ten minutes in Redis, fundamentally separating hot frequently-accessed data requiring sub-millisecond latency from cold historical bookmarks suitable for eventual consistency storage. The proof-of-concept journey validated architectural decisions through functional testing, non-functional testing, scale testing, load testing, and latency benchmarking using Redis-provided Memtier library, revealing 20-40 times reduction in writes to persistent databases representing massive cost savings, with latency observations leading to collaborative optimization between Sky and Redis engineering teams resulting in Redis 8.2 performance improvements specifically addressing charge behavior during load scaling, while production readiness required AWS PrivateLink support to avoid public internet exposure, with Redis roadmapping and collaborating with AWS to deliver this capability enabling Sky's launch with zero incidents since going live. The transformational results include 20x reduction in write pressure allowing databases to focus on complex queries and long-term storage rather than handling millions of bookmark updates, removing performance bottlenecks that enable product teams to build features previously constrained by infrastructure limitations and pursue ambitious roadmap items previously infeasible, delivering performance capabilities to handle traffic spikes without degradation with particular confidence for upcoming exclusive NFL events in December requiring massive scale, and generating significant cost reduction by storing only frequently accessed bookmarks in expensive persistent storage while hot data resides in cost-effective Redis tiers. The successful migration to AWS Keyspaces, previously blocked by Cassandra limitations, became possible through Redis caching reducing write pressure, providing managed service benefits handling infrastructure, backups, and maintenance without operational overhead, scaling to millions of operations per second without downtime, delivering five nines high availability with data replicated across multiple availability zones for disaster recovery and regional failures, integrating seamlessly with AWS ecosystem including CloudWatch monitoring and IAM authentication, and offering predictable on-demand pricing eliminating capacity planning concerns. Future strategic directions include leveraging Redis's generative AI capabilities through their purpose-built platform handling vector search, semantic caching, and context management for large language models, with Sky exploring integration with their Gen AI platform "Shpy" to enhance recommendation engines, content discovery, and personalized viewer experiences, utilizing Redis's vector search supporting multiple indexing algorithms and distance metrics for similarity searches, semantic caching reducing LLM API costs by caching responses to semantically similar questions enabling faster response times and cost optimization, and session management maintaining conversation context and user preferences across interactions enabling more personalized AI-driven experiences. The partnership exemplifies successful cloud-native architecture evolution where managed services like Redis Cloud and AWS Keyspaces eliminate undifferentiated heavy lifting, allowing engineering teams to concentrate on delivering customer value through innovative features rather than managing infrastructure complexity, while intelligent data architecture separating hot and cold data tiers optimizes both performance and cost, with careful proof-of-concept validation de-risking production deployments ensuring smooth transitions that maintain service quality while delivering transformational business benefits including unlocked product roadmaps, improved reliability, reduced operational burden, and significant cost savings that collectively position Sky's streaming platform for continued growth and innovation.
keywords: Redis Cloud, streaming platform, bookmark caching, AWS Keyspaces, performance optimization
---

- All right, folks. Thanks for coming out. This presentation is
Streaming Without Limits, How Sky scale's bookmarking
and powers the future of streaming with Redis Cloud. I'm here with Lena Youssef, the Engineering Manager
in Global Streaming at NBCUniversal Sky. I'm Jon Fritz, I'm the Chief
Product Officer of Redis. So thanks for coming out. Hopefully your re:Invent
is off to a great start. It's gonna be an exciting week. Real quick, an agenda. I'm gonna take about 10 or 15 minutes, give a quick little introduction, and talk a little bit about
some of the new innovations in the Redis world around
Redis Cloud and Redis for AI. Then I'm gonna hand it over to Lena. She's gonna talk all about how Sky has reinvented their streaming
platform using Redis Cloud, some of the execution and outcomes, and some of the next
steps in thinking forward about their thoughts for generative AI. But I'll kinda get started. So how many folks here
are familiar with Redis? All right, not surprised that pretty much everyone raised their hand. It's the most popular database, in-memory caching database in the world. And a few stats I'd love to share. We've recently passed
10 billion Docker pulls, and I think we're the second
Datastore database project to ever pass that amount
of Docker activity. And it's growing, right? It's not slowing down. We also have a couple of
other facts I'd like to share. In the Stack Overflow survey, the most loved non-relational database, I think we're just behind sort of out of the whole database
ranking Postgres, and recently voted the most
used data management tool for agents in generative AI as well, sort of speaking to the ubiquitous nature of Redis as an AI building block. And with that, I wanted to also share that Redis 8.4 recently
just released in open source and will be available in our cloud product and enterprise software soon,
is the fastest Redis ever. It's really breaking the limits on speed, scalability, and performance. With up to a 90% latency improvement, scales much faster, you can
get much higher throughput in a variety of the Redis
multimodal situations, and also better memory
compression as well, so you can save costs on
your in-memory database and caching workloads. So 8.4 just came out. I encourage you to check it out. But all you are familiar with Redis, how many folks are
familiar with Redis Cloud by a show of hands or
use Redis Cloud today? So not nearly as many. So I wanna share just a
couple of things about it before handing it over to Lina to talk about the use case at Sky. So Redis Cloud, it's the
most reliable and available, secure, cost-effective, and
integrated way to scale Redis to power applications and AI agents in any cloud environment. So any cloud environment,
but we're here at re:Invent, so we should be talking about AWS, and wanted to share
quickly the two flavors of Redis Cloud because they're useful for different use cases and worth sharing. So the first is Redis Cloud Essentials. This is a fully serverless platform and the lowest cost actually per gigabyte Redis or Redis API compatible
platform out there. So super easy to get started,
super cost-effective, built for slightly medium,
smaller scale applications, and there's actually a free tier. So we've got thousands
and thousands of customers building on this platform, trying it out, experimenting, and then scaling up. We also have Redis Cloud Pro. That's sort of the more high-scale, the highest availability, highest performance
edition of Redis Cloud. You have things around
sort of dedicated clusters with multi-tenancies so
you can choose really how to build your own private
serverless environment. Active Active with up to
five nines of availability. That's the highest you can get. Smooth and fast scaling, really
great enterprise support, and you can get started with a free trial. Variety of different flavors depending on if you wanna get started quick, scale in a serverless environment, or run these globally highly
available applications in a unique way. One other thing I wanted
to note is we actually have two deployment models in AWS
as well for Redis Cloud Pro. We have our hosted compute model, which is sort of the similar SaaS cloud database type approach. You launch a database, all of the compute is hosted in Redis Cloud,
very easy to get started, minimal networking configuration, and you're sort of off to the races. However, we also have a
bring your own cloud model, which we find customers who
have very, very specific security requirements, or
customers that might have sort of a high or pretty
good EC2 direct discount through a deal with
AWS, and looking around, I know some of you in here do. To be able to use the EC2 directly, launching the Redis
cluster in the VPC you own on EC2 instance that you own, meaning that no data leaves your VPC, and so for some customers,
that's very important from a data residency perspective. And also, you can utilize
up your EC2 RI spend, leverage those discounts, and oftentimes, get the lowest cost Redis footprint in your environment that you can. So that's a little bit of background about sort of the flavors of Redis Cloud on AWS. I wanted to talk about a
few things we just shipped in the last few weeks that really help deliver on that mission
of what I was saying, sort of our goal with Redis Cloud is. The first is, Redis Flex is now launched on Redis Cloud Pro. So if you're wondering what Redis Flex is, it's the ability to use both RAM and SSD for your database,
allowing you to basically scale much larger, and at a lower cost. What's interesting here, a couple points. The first is that you
actually get to choose the ratio of RAM to SSD, depending on the price performance you
want for your workload. And you can actually scale up to 10% RAM and 90% SSD. And you can scale these databases huge, up to 50 terabytes, right? And, also interestingly enough, is you can get up to a
75% discount per gigabyte using Flex. So taking a step back,
what does that give you? Well, it sort of gives a
different price performance dial on your Redis databases,
unlocking a lot of workloads that might have just not
been the right fit for Redis, either from a TCO perspective
or a scale perspective. Now you can run those on
Redis in a cost-effective way, in an easy way to scale. And for many workloads,
the performance impact is actually not that much, right? If you think about it,
if most of your reads are from a smaller set of data, but you want your long tail,
this is actually very common, so like a feature store use case. There's some other use cases as well. The performance hit is
actually not a whole lot, but you get these massive cost savings. And so Flex on Cloud Pro, check
it out, it's available now. We've also built a couple of features to really improve the
resilience and scalability of Redis Cloud as well. There's much faster scaling. We've made some huge
improvements in our cloud fabric to scale up and down 40% faster. Also, there's actually more coming, right? I mentioned Redis 8.4. We put a new feature in open source called Atomic Slot Migration, and that's gonna be
leveraged once Redis 8.4 is in Redis Cloud to drive even better and faster scalability as
well, and that's coming soon. We also shipped a feature
called Smart Client Handoffs. The goal of that is to really eliminate any disruption you might
have in your application during planned events. This is like scale up or scale down when you add or remove
nodes from your cluster, or upgrading a cluster, right? Times when nodes are changing. We've built basically a
way for the Redis client to communicate with Redis Cloud, to work in unison to basically update where all the nodes
are before they change, and so the client can sort
of proactively fail over between one node or the other, reducing disruption greatly. So once again, it's sort of
an interesting innovation. That's sort of what I'm
showing on the slide. Utilizing both the client
and server together in a unique way, and
there's more ideas we have on leveraging those two components in a way to make a much better experience when running your
applications on Redis Cloud. Finally, just better
performance across the board. We recently upgraded Redis Cloud to use the AWS Graviton-based instances. That gives you lower
latency, better performance. We're big fans of the
Graviton instance class. Okay, so we talked about Flex. That's new. We talked about smart client
handoffs and faster scaling. I also wanted to share that we have now Redis Data Integration, RDI, available in public preview
in Redis Cloud as well. For those of you who aren't
as familiar with RDI, it was in our software product before. RDI is a way to basically sync data out of source databases in real time, sort of in a CDC-like way, transform from the data
model that's coming in into Redis data structures, and then sort of update
them real time in Redis. So that gives you, it
makes it easy to unlock and accelerate data assets
across your enterprise in a variety of different database systems into Redis and give
sort of the scalability for that data set, but also the developer experience, right? Developers love building
with Redis data structures, and you can expose data from
a variety of source systems as these Redis data structures. You can stream from things
like Postgres, Oracle, MongoDB, data warehouses like Snowflake, which is a common thing
for taking out information and creating feature stores out of it. RDI has a variety of transforms. We recently acquired a company, Decodable, to accelerate sort of
our real-time streaming transformations that you can do and sort of more complex things you can do when transforming it into
Redis data structures. And then finally, a way to easily update your Redis database,
and we've seen sort of a variety of interesting things
around data modernization, taking data out of older systems and then sort of accelerating
it to build applications and get value from it. But besides overall data modernization, you can also use RDI to
just modernize your cache, that the cache-aside architecture can be a little bit brittle. Dealing with cache and
validation can be annoying. And with RDI, you can
basically sync updates into a source database
directly into your cache to serve fast reads without dealing with sort of the cache-aside architecture. So it's a way to very much simplify, for many use cases, your
caching architecture using RDI. And a great example is this. So we worked with Access Bank. This is sort of top of mind for me today, talking with some customers. Access Bank, they're building
a mobile banking application, and their core banking
system store data in Oracle. Oracle has higher latency
during peak times. You couldn't really sort
of max out the throughput. You couldn't really scale it very well. And using RDI, Access was able
to pull data out of Oracle in real time, transform
it, put it into Redis, and build their entire
mobile banking application on top of that Redis database
and keep it up to date. That resulted in a much,
much lower latency, thousands, huge scalability increase, and sort of a modern way
to build an application without needing to sunset Oracle, right? It's a way to get more value out of data that's locked in other data systems. Okay, so moving from RDI,
wanted to have a quick note on what Redis is doing in
the generative AI space. Obviously, that is what
everyone is talking about for the last couple
years and current, right? This conference is no exception. And people build with Redis,
Gen AI apps on Redis daily. And it makes sense, right? In the same way that
Redis is sort of the thing that you use when you scale
out your mobile application, your web application, Gen AI applications have a lot of the same needs,
and it's sort of logical that you'd use Redis for a
lot of those same things. Redis is fast. For Redis' semantic
search-like applications, it has high accuracy. And Redis is integrated, right? We've got over 30 plus of the
top AI building frameworks plus a variety of other tools that you use when building apps as well, and Redis is integrated
with all of those things. And customers ranging from OpenAI, RelevanceAI, Superlinked, Raymond James, they're all using these Redis technology to make their generative AI apps fast and performance and low-cost. And this slide sort of shows, really, the versatility of Redis
in the Gen AI stack. There's a ton of icons here, but I will call out a few things. And actually, you can use
Redis for all of these layers, things like Redis Flex
for long-term storage, RDI as the data pipeline, or a variety of other
things that Redis integrates ranging from Snowflake or Databricks, a variety of database services
in all the hyperscalers, using a variety of data
pipeline tools to get data in. But the key is the working memory layer, that fast data layer for agents, that's Redis, right? And Redis Vector Search, which is a way to obviously
use semantic search at scale with very high performance, and the Redis Engine in general can back a variety of
these different Gen AI apps you might build. And then there's
integrations with Tools LLMs. Redis VL is very, very popular, semantic caching with lane cache, a variety of other Redis tools
to really integrate Redis with the way you build for Gen AI, alongside integrations with
a variety of other tools as well, right? And this is all sort of
there and rapidly developed and hugely important for our team to serve the Gen AI world in the same way that we're serving the
web app, mobile app world. I wanna call out one specific
thing we're working on, Redis Lane Cache, which is
our semantic caching product, uses Redis under the hood, but has a variety of services
that make it very, very easy to sort of build semantic caching. There's a bunch of things
besides the actual cache and Vector Search to really build a great semantic caching solution. If you're not familiar
with semantic caching, it's basically some of the similar idea of what caching is with a database. Instead of hitting an LLM for everything, let's say you have a chat bot and you're hitting the LLM
for all of the responses, oftentimes you're gonna
have many customers asking the same thing, and if you could cache that response back from an LLM, it would be cheaper, you wouldn't have to go hit
the LLM again, and faster. For anyone who's built with LLMs, they know that the latency is not as fast as a lot of other data or AI products. And so with Lane Cache,
we've seen customers get up to 15 times faster
performance in calling an LLM, and up to 90% lower cost, depending on how you structure the cache, because you're not
hitting the LLM as often. So once again, this is
something that you think about when productionizing your Gen AI systems is at some point, you're
gonna need to think about performance and lower cost. And here's an example, right? It's not just sort of an abstract idea. Performance does matter. We worked with Asurion, who has a customer service application. They built their Symantec
Cache and optimized it so that a high percentage of asks were served out of the cache. This improved their
response times by over 50%, resulting in a four
times higher engagement on their websites, right? Performance, when
thinking about this stuff, makes a huge difference, and we're seeing Symantec Caching, now that a lot of these generative AI apps are moving towards production, becoming just a critical
part of the Gen AI stack. So before I hand it over to Lina, one more point I wanted to make, which was, we're at an AWS conference. We all love the cloud, we all love AWS, but many of you, I'm sure, have either your team or
teams in your organization running deployments in a
variety of areas, right? In other hyperscaler clouds, maybe on Kubernetes in
the cloud or on-prem, or software and VMs, either in the cloud or on-premises, right? Enterprises today usually
don't just run in one place, and with Redis, you can really run Redis and enterprise-grade
supported Redis anywhere. In any major cloud, we support, Kubernetes for a variety
of major cloud service, Kubernetes providers, or
Kubernetes in general, wherever, OpenShift, we support it, and software as well, we support. And one thing that I found
when talking to customers, especially enterprise customers, is they care about
consolidating their engines, so there's sort of one
standard way to deploy, and they appreciate the fact that they can sort of deploy the best-in-class, fastest engine with all these different capabilities across Gen-AI, caching, NoSQL, wherever they want with the same group, and so we can offer that. But with that, I'll hand it over to Lina, who will get more into
how all this technology is used at Sky to reinvent their streaming platform and their future with generative AI. ♪ Yeah, I wanna go with you ♪ - [Narrator] The NBA is
streaming on Peacock. 140 games, Peacock NBA Monday, Coast to Coast Tuesday, and one epic 2026. ♪ I'mma elevate the next
time they see this ♪ - [Narrator] Plus all new ways
to see more than the score. From the court, to the culture, the NBA is on Peacock. ♪ Go baby ♪ ♪ Yeah I wanna go baby ♪ - Thank you, Jon. I hope you enjoyed that short video showcasing our partnership
with NBA on Peacock. So let me give you a bit of an overview about global streaming and who we are. So we have over 41 million customers here in the US alone for Peacock, and we consider ourselves as leaders in the live sports streaming. To give you a bit of a scale, in 2024, we had a streaming record with the NFL wild card game, and we encountered over 30%
of the internet of the US, which was, at the time, a record. So global streaming technology is truly a global department. We have engineers here in the US, in London, Czech Republic,
Portugal, and India. So let me give you an
overview about bookmarking, which is one of the use
case we used Redis Cloud, and it was our first application to integrate Redis Enterprise. So what's bookmarking? I guess all of you here have been using it on a day-to-day during
your streaming experience. So basically, you'll be watching such an episode on Love
Island, for example, and you will want to pause
to grab a cup of coffee or, let's say, go back to work. So that's basically bookmarking. So that's available, as you know, on all platforms such as Peacock, Netflix, or, God forbid, Amazon Prime. So as you can imagine, we get millions of people
watching every day, and in the number of
bookmarking we're saving, it's also a million, and that's the scale we
are handling every day. So bookmarking is feeding, as well, on another important feature, which is continue watching. It's also continue watching the rail that you can see on the right. It shows you all the
content you've started but haven't completed it. So it appears in multiple contexts. So on the left, you will see
the Yellowstone series page where you would have
saved all your bookmarks, and you would continue
watching where you left it off. But on the right, you will see that the continue
watching section homepage will have all your series, such as Yellowstone, Love Island, and How to Train Your Dragon, which you didn't continue or finish. And it will also show you any
returning series or episodes. Now that sounds like
quite a simple feature, but actually, the complexity
lies into the scale. So the technical challenge here is to maintain the state, in the consistent state
of saving the bookmarks, the low latency, and the
cadence of saving a bookmark. So every minute, you
have millions of writes, and every page load, you will have potentially millions of
reads for the bookmarks. So what can you do when
your largest database is too costly to run and manage? So we were using Cassandra
to store our bookmarks, but we hit several limitations, due to the data size, loads,
the volume of bookmarks. Our infrastructure was under strain, and it was becoming very cost-intensive. So we were unable to meet one of the most important
product requirements, such as expanding the
retention of our bookmarks, and that was a problem
due to the Cassandra not able to support it. Outside of this project, we've been working on a broader migration from the self-managed Cassandra
to a managed AWS Keyspaces, and all of these
limitations were the same, not being able, for this reason, to migrate to AWS Keyspaces. So this is our previous
bookmarking service architecture. As you can see, in the middle, we were heavily dependent on the database, so every reads and writes operation went directly to Cassandra, with no caching layer, so there was no place to absorb traffic or buffer for writes. So the system used a single
uniform persistent layer for all the data. There was no distinction
between the short-term and the long-term data. So everything lived in the same place, and as you can imagine, it was creating a constant
high cadence and pressure on the database. So every bookmark update executed at full, rate-generated sustained load, and no natural relief
point on this architecture. So as you can see, Cassandra
struggled to scale, especially when we had
big events, effectively. So the challenge was not
simply to add capacity, even if we scaled horizontally, this was not solving the problem. Compounding this issue with, as I said, the product requirements,
we were not able to meet, so it was clear to us that
this architecture we had was clearly, could not evolve with any of these product requirements, or could not sustain. So here comes Redis. We reached out to Redis, so that we look at potential options to solve those problems together. So initially, we looked
at Redis Open Source. It seems like everyone
knows Redis Open Source. It offers a lot of core capabilities, however, with Open Source,
everything is self-managed. So that would have been difficult,
especially at our scale, for maintaining, scaling,
and all this operation, and it will have created a
lot of operational overhead for us, and required a dedicated expertise to manage effectively. So we then evaluated Redis Cloud, that Jon mentioned previously. So it's a managed service
that offers all of those, and eliminates our
operational buffer and burden. So the team identified that
this area of Redis Cloud provides the most value for us. So auto-scaling is, for us,
the biggest differentiator. So Redis Cloud will handle
scaling effectively, and it will allow us to
focus on the development, rather than the infrastructure. And that was the biggest
game-changer for us. In addition to that, they support the cross-region replication,
with a very low latency. So for us, as we said, we are global, and that will obviously work for us, for global deployments. And we also have, as a feature
provided by Redis Cloud, a two-second flash to this capability, that ensure data durability. And obviously, if we had
to use self-managed Redis, it would have been very
difficult to maintain. Another aspect of the Redis Cloud is the number of modern data
structures they support. So we explored hash,
JSON, string, sorted set. We end up choosing a
string and sorted set, but all of those models they offer worked very well for our business, and allow us to save massive costs. In addition to those ones, we also have a TTL-based eviction policy, which is time-to-leave
based eviction policy, which will clean up your clusters, and effectively manage,
simplify, manage your cache. So in the end, as you can see, we have the hybrid search, which is used for vector search. We do not need this for bookmarking, but it was also, while we
were exploring Redis Cloud, we were thinking that
it could be a use case, a very good one for Genepi, which we will be talking about. She's our Gen AI platform. So we've built a new
architecture using Redis to make bookmarks faster
and more reliable. So as you can see, when you
create or update a bookmark, so our system are writing
to two Redis Cloud clusters. The first one is a string, and the second one is a sorted set, which I will be explaining
further in the next slides. So that separates service,
as you can see below, which we call BMS, the bookmarking service
cache right behind, will save the bookmarks
to long-term data storage, which will be AWS Keyspaces
we are currently migrating, once they are enough mature. And also, when you need a bookmark, in terms of bookmarking reading, our system will check both Redis and our long storage in parallel, and will fetch the most recent bookmark. So bookmarks now stay in
Redis for at least 10 minutes before they go to the long-term storage, and instead of writing
to Cassandra constantly, the separation of hot data, so basically what you need the most, and the cold data, which
is the historic bookmarks, improves the performance and
reduce massively the cost. So Redis acts as a cache in the middle of our infrastructure, as a design to cache data
for the bookmarking reader, while also finding a way to persist data for long-term storage. So we architected Redis with
two different data structure. The first one is a string cluster, and the sorted set data structure. So the string data structure
supports heavy writes, so the writes happening
at the same cadence of the current, as soon as
we receive the bookmark. For every single bookmarks
we have in Kafka, it will end up in our string cluster. So the aim of the string cluster is to deduplicate the data, if we have a new bookmark
for the same user, for the same content, we simply update the string position of that bookmark. So this is essentially a cache
accumulating all the data. So the string operation
are very, very fast, and quite performant, they
have a time complexity of O1, and obviously this was
where we had a lot of data. We needed something else
to process the data, and that's why we took a second cluster, which is a sorted set. So the sorted set has, as the name said, it's basically ordering the bookmarks, and it's like a
leaderboard, which will keep the key of the bookmark, and a score that will keep moving and compare the previous entries we had. With a sorted set, you get a view of the string cluster in an ordered way. So this gives us a nice
way to process the data separately from the string cluster, which is used to fetch the bookmarks, and without impacting the customer. So we started our journey with Redis by proof of concept last year, where we conducted
functional testing, NFT, scale on the load and latency. They really helped us to
explore with the architects both different data model
and what could work for us. We then did an accumulation rate test to see how much we will
be saving of writes in the long persistent database, which was at that time Cassandra, and it happened that we
were saving 20 to 40 times. So that was massive, and
it was very clear to us that Redis Cloud will be a good choice. We then did a latency benchmarking test through one of their
library they provided, which is Memtier. We observed some latency there. Redis helped us to find that
it was mainly on our stack, but also, they also tried to provide even better performance
that came out in Redis 8.2, especially on how they recharged when we are scaling on the load. We then started our development by integrating Redis
open source initially, and the reason why was that we needed, as NBCU, Sky, AWS private link to not be exposed over the
public internet, to avoid that, and Redis really stood out. They road mapped it, they worked with AWS, and it was available last summer, just a summer, a few months ago. So that allowed us to start
our production readiness. We did some chaos testing, scaling, and we launched a few weeks ago, hand-in-hand with Redis, and we have had zero incidents so far. So that unlocked for us the
migration to AWS Keyspaces with the cost reduction
and the number of writes that have reduced by at least 20 times. So as I said, the result of
this Redis cloud implementation has been transformational for us. We have a 20 times reduction
in the write pressure. This means our database can
focus on complex queries and long-term storage rather than handling millions of millions of bookmarks updates. And with this performance
bottleneck removed now, our product teams can
now build more feature they've been waiting for. So we are seeing some really
faster feature development in our side, and more
ambitious road map items that are becoming feasible. Also, the Redis performance
gives us ability to handle traffic spikes
without degradation. We are preparing the NFL,
big NFL exclusive event for end of December, and
we are quite confident now that we have Redis in place
that we will be able to scale. And also by keeping, obviously this, only the frequently accessed bookmarks into the long-term database, it's obviously a massive
cost reduction for us. So we are migrating our Cassandra database to AWS Keyspaces, and I want to highlight the key benefits that made
this the right choice for us. So by combining better Redis caching, and we were able to reduce the writes and basically unlock this migration that was awaited for so long. So AWS Keyspaces are managed as a service, they handle for us the infrastructure, the backups, and the maintenance, so we don't have to worry
about operational overhead. The service scales to handle millions of operations per second
without any downtime. It has, like Redis, five
nines of high availability, with data replicated across
multiple availability zones. So one of the key reasons
we chose Keyspaces, it was compatible with
our Apache Cassandra, and we can use our existing APIs, tools without any code
changes, to migrate. And also AWS partnership
has really facilitated for big database,
especially our bookmarking, which is in terabytes, to migrate, and they've increased the throughput on the gouge on their side. So beyond our existing bookmarking, we are actively exploring and working on several additional Redis
use cases across NBCU Sky. So the first two, concurrency
management and GNAP, are the areas I will
be talking you through. And then you have continue
watching and personalization, which we are exploring. Continue watching will be pretty much the same solution we have
been using for bookmarking. And we are also exploring
and evaluating feature form, which will be replacing our feature store for personalization features, for personalization features
and for that service. So concurrency manager,
or what we call ConMan, is a service that manage concurrent access to content across our platform. It basically controls how
many simultaneous streams a user can have, active at the same time. So for example, you are watching
NFL or NBA in one device, and ConMan tracks this
stream and enforce you to not have multiple
streams on other devices. And that depends, obviously,
of your subscription. So in the current architecture, ConMan is deployed across multiple region. So here you can see
region one and region two. And each of them are
connected to a separate DB. So the change we are gonna do very soon is to integrate Redis
Cloud with PrivateLink, similarly to what we did with bookmarking. And this will obviously make
it definitely more secure, but also, Redis Cloud provides
cross-region replication, so it would work for us perfectly. We are also evaluating Redis Flex, which obviously is an
optimized storage tier, since ConMan has a very small
time to live, retention, so that would work probably
better in terms of cost. So I will talk about the Genepi, which is our multipurpose GenAI platform that supports development
and production workloads. So it's an in-house solution that is vendor agnostic and
cloud provider agnostic. That means that we are not tied up to any AI vendor or cloud provider. And it seeks to eventually
facilitate to our team, to all our team, to create
their own AI solution and development. It provides guardrails and
governance, as well as security. So as you can see on the left side, you have our tenants, which are basically our team's application that use Genepi, that go through Genepi
before accessing AI models. And that obviously provides
for us standardization, security, but also cost tracking. So let me take you through
Genepi and how it works and how Redis and AWS come
into the architecture. So on the left, you have all our tenants, which are three types. The workflows, which are consecutive AI requests, and you have the chains, which are connected sequence of AI, where the output of one will
feed the input of the other. And you have the agents. So they go all through
Genepi, which is, as I said, the in-house product that we have done. It has an AI gateway that
facilitate the authorization and the authentication. And then the orchestrator,
which is basically the brain that connect to all the other component and the LLM adapter. So above Genepi, you can
see we have semantic cache and we have chosen to
take Redis line cache, which is basically a
semantic cache as a service. And it's quite performance and one of the fastest, to be honest. Then once, if basically
the tenants send a request, Genepi will go to the line cache. If there is a miss within that line cache, we are going to the RAG. We are currently using
AWS Kendra for the search and the AWS Knowledge Base,
which is a RAG as a service. And those will go to the vector database. We are also using AWS
OpenSearch and Redis. If you ask me why we are
basically using both and not one, it all depends of our
tenant and what they need. So the tenant control the RAG. They also feed it with their request, the embedding models, their documents. So depending on what they want, we will choose either OpenSearch or Redis. So Redis is very fast
compared to OpenSearch. We're speaking about milliseconds. OpenSearch is 10 to 100 millisecond. Redis is between three to 10. So you can imagine that
it simplify for you a lot. It's also depending of the tenant, so we will be either
taking one or the other. And for the MCP, so to
connect to other tools such as Jira, Confluence, et cetera, we are currently evaluating
AWS Asian Core Gateway. So all of these requests go there before to reach the LLM provider. And if they are not found, we
go through the AWS guardrail that basically make sure
that we are compliant in the output and the inputs. So we have been building better together. I've started with the Redis community because this is where we started as a POC and maybe many of you know it. So this is especially
for Redis open source where you can find information. We use the Memtier, as I said, for the latency benchmarking. And then once we reach out to Redis, we had their great support
in terms of architects and all the guidance from them to choose which data model we wanted. But also, when we had found
that we needed private link, they were hand-in-hand with us. When we saw that there
was some latency happening when scaling on the load,
they were working with us depending of the framework we were using and advising us what to do. And especially when we
had a date to release, they were sitting next to us in the office making sure that everything went well. And I also have AWS support,
which linked basically to the Redis-AWS private
link that happened there. So Redis really worked with
AWS to provide this for us as soon as possible. And finally, the AWS marketplace that we have been able to access and procure Redis Cloud through them. And it simplified us, obviously
the billing, et cetera, and made that purchase very fast. - Okay, well hey, thanks all for coming. Have a great rest of the conference and I appreciate you taking the time to come and come to our session. Thank you. - Thank you for having me.
(audience applauds)
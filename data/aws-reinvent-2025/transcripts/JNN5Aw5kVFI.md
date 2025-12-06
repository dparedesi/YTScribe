---
video_id: JNN5Aw5kVFI
video_url: https://www.youtube.com/watch?v=JNN5Aw5kVFI
title: AWS re:Invent 2025 - Amazon S3 performance: Architecture, design, and optimization (STG335)
author: AWS Events
published_date: 2025-12-03
length_minutes: 40.47
views: 517
description: "Go behind the scenes of Amazon S3 performance architecture while learning practical optimization strategies. We'll explore how S3's internal systems manage massive throughput, handle concurrent requests, and balance loads across its distributed infrastructure. Dive deep into the technical foundations - from request routing and partitioning strategies to caching mechanisms - that enable S3 to power demanding workloads like real-time analytics and ML training. You'll learn how to leverage this arc..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
---

- We're gonna talk a little bit about S3's architecture and design and how you can leverage that to drive massive throughput and get high performance out of S3. My name is Ian McGarry, I'm a director of software
development for Amazon S3, and I'm joined by my colleague Dev Kumar, who is a principal product manager for S3. So let's go through our agenda quickly. In this talk, we'll dive
deep into how S3 works, its scale, and how you can leverage that to drive massive throughput
and get low latency out of S3. And we'll also cover
Amazon S3 Express One Zone, which is our high-performance
storage class. My colleague, Dev, will be covering that, when to use it, and what
the key benefits of it are. Okay, so the question
is why would you want to drive high throughput and
get low latency out of S3? It's an object store. Well, many of our customers look at S3. They see the durability, they see the availability,
they see the cost. But most importantly for
these types of workloads, they see the elasticity. It can scale up and down to
high throughput as needed. A lot of customers are running data lakes, analytics workloads, or machine learning training on S3 and are scaling to hundreds of gigabytes per second of sustained throughput. Similarly, they're running
interactive querying on logs and machine model loading on Express. So we'll talk a little
bit about those use cases and how to get the most
of out of S3 for them. Okay, so let's dive right in. Optimizing for high throughput. If you take anything away
from this talk at all, it's that you should use Amazon S3's scale to your advantage. There is a lot of infrastructure, disks, servers, and networking that goes into making Amazon
S3 work for everybody. And that's actually the key to unlocking your throughput as well. Go broad and go wide across
the the various fleets we have across the world. And speaking of scale, I
just wanted to take you through some cool numbers that
I thought would be helpful to give you a sense of
the scale we operate at. Amazon S3 currently stores
over 500 trillion objects, which equates to hundreds
of exabytes of storage. We also serve over 200
million requests per second, and customers are running over
a million data lakes on AWS. So scale is definitely the goal. Because we support such
scale such as this, we have, as I mentioned,
a lot of infrastructure, and that'll be the key to unlocking the high throughput today. Okay, so S3's architecture. At a very high level, we think of S3 in three simple components, and this is in the context of serving GetObject and PutObject, so retrieving data from S3
or persisting data into S3. There's our front end,
which is the set of services that route your request to S3, and also includes the services that orchestrate the
processing of your requests. What do I mean by
orchestration and processing? I mean by running authorization,
running authentication, generating events, generating
logs for your requests, all the things that go into
actually serving the request. It's also responsible for orchestrating generating metadata about your object in your request, looking that up in our index, which I'll talk about in a second, and then also persisting and retrieving that data from our discs. The next is our index component, and that is basically a very, very large
distributed key-value store. And it's very simply there
to map object metadata to the object bytes. Simple example is take
the key name of the object and store location of
the bytes on the discs so that we know where
to go to get the data. It also stores things like
creation date and so on. And then finally, our storage subsystem. This is responsible for managing
all of those disks at scale and then also figuring
out where to place data. So these three components work together to fulfill a GetObject
and a PutObject request. And that's how we think of them. We organize around those internally. And so for example, for myself, I lead the front end teams who
work on all the APIs for S3. Okay, so that's the architecture. How does that map to what you do? Well, let's take a very,
very simple example. I have a 500-megabyte object, could be a video, could be a
document, could be anything, and I want to upload that to S3. I establish a connection
between my client and S3 and I start uploading via the request. One key piece of information. When you establish a connection to S3, you can only have one active request on that connection at one time. It'll become important in a little bit. So, 500-megabyte object, establish my connection
and begin my request. There's no actual limit on the amount of data you can upload
on a single connection from the S3 perspective, but generally given
network-client configuration and different constraints, we find most customers can achieve about 100 megabytes per second
on any single connection. So if you take my 500-megabyte object, you take my
100-megabyte-per-second connection, that means I can upload that
object in about five seconds. But how do I get that down to one second? I wanna go faster. The way I do that is parallelize, and that's what I mean
about use S3's breadth. Parallelize many connections across S3 so you can achieve higher throughput. For the persisting of data, we'll talk about multi-part uploads, and for the retrieval of data, parallelizing the retrieval of data, we'll talk about range GETs. So we're gonna talk about
spreading data across, or sorry, connections across many, many different IP addresses. And we'll talk a little
bit about the tools for doing this in a second. So let's go back to our example. Now I have my single object,
which, again, can be a video, but I carve that up into five parts and have a single connection to upload those parts in parallel. And now you can see that with each connection getting
100 megabytes per second, I've carved it up into 500
megabyte chunks or parts. I can upload those all within a second. But there's more benefits to this. Taking multi-part upload which is the API to achieve the PutObject in parallel, there's a few key benefits to this. The first one I mentioned,
it improves throughput. But it also improves our recovery time. If any individual connection fails, which could be due to your client failing, could be due to network trouble, it could be due to the
server on the S3 side, which is physical infrastructure failing, then I only need to re-upload
that individual part. So you can imagine in
my initial connection, I get 250 or 400
megabytes the way through, my connection times
out for whatever reason because I go through a bad
router or a bad switch, I now have to go back and re-upload all that data again, not with multi-part upload. Now, if I upload four out of those five, I only need to re-upload
the one that failed. These can be uploaded
in any order as well. And so the beauty of
this multi-part upload is that you can even start an upload to S3 before you have all the data in memory. You can imagine for a streaming use case where you have data coming in, you don't know what its size is yet, it's streaming video or it's
coming from a stream of data, you can start uploading in parts and only when you have
all those parts uploaded then you can complete
that multi-part upload and persist your data. So a lot of benefits to that. You can also pause and resume
object load uploads as well. You can go in individual parts, pause for a period, resume,
and then complete at the end. It's the same on reads,
except we're not using multi-part upload this time. We're using range to GETs. So again, if I uploaded
my 500-megabyte object, now I want to download it
again 'cause I plan to use it, I can now do range GETs which are five individual GET requests across five individual connections to pull all that data down at the same time and then
reconstitute on the client. So again, here, instead
of taking five seconds to download the whole 500-megabyte object, I can now download across
five individual connections and get it down to one second. How do I do range GETs? Range GETs are a little bit different because now I've actually
stored all my parts up there. So I need to use the ListParts API, which lists out all the
individual parts of your object and maps them to ranges. And then I can use the range GET API to download those in parallel. Again, the same benefits apply here. If any individual part fails to download due to network trouble,
trouble with my client, I only need to download
that individual part. So this is kind of the key recipe or ingredients to going
massively parallel. I've talked about one
object, five connections, this can scale very, very broad, and we have customers who are doing hundreds of thousands of
connections today in this way. Okay, take you a little
bit under the hood. What I mentioned earlier was I have five individual connections. The ideal state is that is
five individual connections to five different IP addresses of S3. S3 has many, many IP addresses that all get stored in our DNS zones and they get returned to customers. And ideally, you want to
parallelize across many, because if we have a
problem with one server, we want you to quickly be able to recover and try different servers. And similarly, if you're
doing a multi-part upload or a ranged GET and one
of those servers fails, we want you to be able to quickly retry. So rather than having all your connections to one single IP address, 'cause if that fails then
all your connections fail, we want you to spread across. And how do we do that? A couple of years ago, the teams that I lead launched
multivalue answer DNS. So you can see on the right-hand side, I've got a dig command, I've
just digged for Ian's bucket at our S3 endpoint in us-east-one. And if you look at the answer section, which is the response to
the DNS query that I made, we've got eight IP addresses there. So on any DNS lookup, we will return up to eight
IP addresses to the client. Many, many clients can
take advantage of this and actually take all those eight answers rather than just taking one off the top, cache them, and use them to parallelize but also use them to retry against. For example, if they fail
a connection to one IP, they can just pick another one without having to re-resolve DNS. So this actually takes
latency down on connections and also allows you to go in parallel, and many SDKs and many
clients actually resolve DNS and then build a bigger and
bigger cache list of all the IPs that they can use. AWS, SDK versions, Java 2.x and C++ and Python Boto3 all take advantage of this and have so for the last couple of years. So a lot of this is actually baked in under the hood you're getting it, but if you want, you can
go dig the endpoint today and see for yourself. Okay, so I've talked a lot about connection management in theory. A couple of years ago, a few of us got together in S3 and realized, "Hey, we have
all these best practices. We're talking on a case by
case basis with customers about actually using them, baking them into their client, about how do they architect
their HTTP clients." And we thought, how can we actually go and just give this to everybody for free and get them to stay up to date so they don't have to think
about this very often? It's good to know about it, but you don't wanna be tinkering around with clients every single day. And with that, we launched
the AWS Common Runtime, or CRT as we call it for short. It has all of our best
practices baked in in code, and it has a ton of value, so it has things like it
handles asynchronous I/O, it has a HDB client
that's optimized baked in, and it does authentication
and authorization for you, and it does things like
automatically parallelize for uploads and downloads. So all those range GETs and multi-part uploads I spoke about, it handles that for you, and it will actually also try and scale to your performance needs, and I'll talk about that in a second. And the other thing, it
has built-in retry logic. So when I spoke about failures, it already has optimal
retry logic baked in. So if you fail a request, it
will retry using a cached IP as opposed to resolving DNS. So you get performance benefit from that. There's a lot within the CRT, but I just wanted to talk
about one single configuration that I really like because of its simplicity,
and that is target throughput. I've put up the SDK config
and the CLI config example, but the target throughput is
basically you telling the CRT, "Hey, I want to get this much
throughput out of my client." Now, just one call out, this throughput is in gigabits
per second, not gigabytes, which we were talking
about megabytes earlier. This is bits, so it's a little bit of a different scaling factor. The reason it's in bits is
most of our EC2 instances, their network interface
cards are rated in bits. So it's nice for you to
be able to think, "Hey, I want to get 20 gigabits per second out of this S3 client on this instance which has a 50 gig NIC," for example. So the default is usually set
at 10 gigabits per second, which is pretty high. But you can go and configure this, and what it will tell the CRT to do is to looking at the objects you're wanting to upload or download and taking your target throughput, it will automatically figure out how many connections we should open to try and maximize to that throughput. And I've tested myself,
it gets pretty close to around the 20, if you set it at 20 and you've got the right workload. So something to look at, it's a really nice configuration to set. I want to achieve this throughput, get this performance,
instantiate the client, configure it, and away you go. Okay, CRT, how do you actually use it? Well, the CRT is embedded
in multiple clients, as I mentioned. It's also the foundation of our open-source file connector client, which is Mountpoint for Amazon S3. And it is also available by default on Boto3 and the AWS CLI on Trn1, P4d, and P5 EC2 instances. And the reason is those
have very large CPUs and large network interfaces, so they benefit the most from these performance design patterns. For other instance types, you can go and enable it and configure it yourself. Okay, I'm putting a QR code here for getting started with the AWS CRT Now you know about, it's
definitely the first place to go when you're trying to
think about how to drive higher and higher throughput to S3. Okay, so we talked a lot
about parallelization of connections and going broad, and a reasonable question
you might ask yourself is, "Well, can I just take that and just continue to scale indefinitely?" And the answer is generally yes, but it also depends on
your prefix structure. I'll talk about what
that means in a second. So we talked about those three components. We had our front end, we had our index, and we had our storage. Our index is a subsystem
that's responsible for mapping metadata to storage locations. So you can imagine when a
request comes in for a GetObject, we are looking up that index saying, "Hey, where are those bytes
so I can get them back to the customer or to the client?" And that's where we're
looking up our index. Our index works around, or sorry, our index works
around prefix structure, and we'll talk about what
that means in a second. But just to take you
back to the architecture. Okay, so what is an S3 prefix? It is any string of characters
after the bucket name. So you create your bucket
name, Ian's bucket for example, and then any of the keys after that, or any of the text after that,
is your prefix structure, and that's used to map into
the object data itself. Let's make this concrete. Here, for example, I've got my organization
and I have two divisions or two departments
within that organization. I've got engineering and I've got finance. My engineering organization
likes to store their data between prod and test. In prod, they have their
production software artifacts that they use to deploy, and in test, they have their
test software artifacts that they use to deploy. My finance team likes to think about their
fiscal artifacts in years because they have deadlines
towards the end of the year that they need to prepare for. So they go based on year. So that's what your prefix structure might look like in a bucket. Prefixes within S3, because it's an object
store, are not directories, but it's a very easy and
natural or organic way to think about them. It's like directories
going down to my data. But it's very important you don't just think
about them as directories, 'cause it can lead to some
suboptimal structures in prefix. So let's see how we put this in practice. Or first, sorry, why does this matter? As I mentioned, it matters because there's limitations per prefix. When you create your bucket
for the very first time, when I create Ian's bucket, I can achieve 3,500 PUTs or
5,500 GETs against that bucket. I can do more if I want to, but I need to think about my
prefix strategy underneath. If I create 10 prefixes in my bucket, I can now 10x that that request per second or PUTs per second or GETs per second. So now, I can achieve
35,000 PUTs per second or 55,000 GETs per second. We automatically scale based
on your prefix structure as you are driving more and more requests. So as you drive requests that exceed the 3,500 PUTs or the 5,500 GETs, we'll automatically partition
out your prefix structure so you can drive more and more TPS. So let's walk through an example. I've got my reinvent-bucket. Today, I can do 5,500 GETs per second and 3,500 PUTs per second. So let's talk about what the
first split might look like for my prefixes. I've got prefix1 and I've got prefix2. You might think of this as sales
and engineering from before or finance and engineering from before. On my first prefix, I
can now drive 5,500 GETs, and in my second prefix, I
can drive 5,500 GETs as well. When I'm driving a combined
11,000 requests per second, S3 will automatically
split out these prefixes seeing that there is what
we call prefix heat on both and then splitting out those prefixes. But we can take this a step further. Very simply to keep things
simple on the screen, I've now got A and B
under prefix1 and prefix2, and now I can drive a combined 22,000 TPS. Again as I drive more requests to it, S3 automatically partitions
out these prefixes. So really important to think about how your prefixing your data before. You want natural splits in your prefixes between different workloads. This can, again, lead to sharp
edges if we're not careful, and we'll talk a little
bit about that next. So here, I've now switched
over to a different format. I've got day within my prefix, and this is a very common
pitfall for users of S3. Having time-based data or day based data, it's very alluring or it's very easy to
stick the day up front because you're changing
your data over time and you might have analytics workloads that want to run on a day-by-day basis, so it's easy to stick day
at the start of your prefix to help you think about your data. But that does lead to suboptimal outcomes. So let's talk about it. We'll take our exact same sample before where we have our prefix1 and prefix2 and we have A and B,
but day1 is to the left and day2 and day3 and day4
will all be to the left. The problem with this is that once I've generated enough requests to my prefixes which has resulted in the
partitioning to achieve my 22,000, when I move on to the next
day, that's all wasted. It's all gone, because I have
day at the start of my prefix instead of later on. So you want to make sure that day2 or any dates are further down or right in your prefix structure so that when you are partitioning
your prefixes to the left, you're able to reuse those requests later. So I've called it out here, but the partitions from
day1 are now unused and we need to do the
same splitting on day2 while we see sustained load. Now, while we are actually partitioning or breaking out these prefixes
to drive more requests, you might see HTTP 503s from us. We're telling you to slow down
while we're doing the work to break these out. But once we've done the work, then you will sustain
those requests per second without seeing any HTTP 503s or slowdowns. And so it's really important that rather than putting
the date to the left, you're pushing it down
so that the work we do to partition out your prefixes gets reused as the days go on. And so in this example, I've now pushed day1
and day2 to the right. So any work we've done
on prefix1 and prefix2 to split them and then A and B to split those gets carried over as the days move on. So a really, really common pitfall and something to definitely
take away from this. But whenever you're
starting with an S3 bucket just to test or mess around, it's very easy to just
create any prefix structure that maps to what you have. But when you know you're
going to do high throughput and high scale, take a second step back, write down, and make sure you're thinking about how your prefix
structure will look like and that you're having
natural divides to ensure that you can drive the TPS you need to. Here I've got another QR code, it's a best practices
reference for optimizing high request rate workloads, talks a lot about prefixes, gives you some other examples. I think it's a great
secondary dive into this. I've given you the kind of high level of how this works at a very simple case, but if you want go deeper
on that, use the QR code. Okay, now, I will hand
over to my colleague, Dev, to talk about Express One Zone. - Thanks, Ian. Hello, everyone. My name is Devabrat Kumar, and I'm a product manager
on Amazon S3 team. I lead S3 Express One Zone, and I'm gonna talk about its
performance characteristics, some of its unique capabilities, pop use cases customers are using it for, and some key architectural considerations when building with S3 Express One Zone. So let's dive right in. S3 Express One Zone is
the fastest object storage delivering single-digit
millisecond access times. That's really fast. It also offers up to 2
million requests per second per directory bucket. I'll talk about it a bit
later in more detail, but one of the key things to note here and kind of extension of what Ian was talking about is you get the TPS capacity right when you create the bucket. You can scale it up to 2 million, but you get 200k right out of the box, and we'll look into why that's important and why it's super relevant for some of the bursty access use cases. Then you also have some pretty cool differentiated capabilities specifically in this storage class. So for example, you can add
data to an existing object while it is in the object storage. Basically I mean to say you
can append data to an object while it is in a Express One Zone, something pretty cool
for an object storage, which before this capability
had been immutable, you could not actually mutate
an object in object storage. Also, you have order of one
rename operation now available, which basically means that
regardless of the size of the object, you can
rename it in constant time, a brand new API we launched
a few months back this year. With these capabilities, customers achieve up to
10x faster access times on S3 Express One Zone
compared to S3 standard. So why does all of this matter? It matters because there are
a whole bunch of use cases that need high performance. Kind of intuitive I guess. At this point, actually, lemme
do a quick show of hands. How many of you in this room have at least one of these problems? Like, at least one use case
here that you work with? Okay, that's a good number. Hopefully all of you use Express already and benefit from this talk. Let's start with the
first one, ML training. With the past few years,
a lot of customers are using S3 Express One Zone to drive very high levels of throughput, very high levels of data transfer speed. As we know for ML trading, customers deploy very large
number of high-performance GPUs, and they want to keep
these GPUs busy, right? So your data is in your object storage, you want to get it as soon as possible, so you want to have the
fastest data transfer speed that you can attain. When you try to do that, you run very high levels of TPS, and, you know, your transfer speeds could be up to terabytes per second. And because S3 Express One Zone is built for high performance, you benefit from its capability
to scale to these levels and you can keep your GPUs busy and continue doing meaningful work. So super popular for
ML training these days, and we see a lot of customers adopting it, some event training foundational models with S3 Express One Zone. The next one is interactive querying, and, you know, this is a use case that has existed for as
long as I can think of. Customers have data, they
want to make use of this data, they want to run high-performance queries. A lot of these queries
are also interactive where you have an end user waiting for the answer to come back. So for example, think of
observability analytics use case. So you have a whole bunch
of log files sitting in S3 and you want to get insights
out of those log files. When an end user is running a query, he might burst to tens to
hundreds of thousands of TPS because he may need to
scan a lot of that data and obviously he requires
low-latency access because he doesn't want to wait too long. So this is exactly when you would want to use S3 Express One Zone to benefit from its
high-TPS, low-latency access for these interactive querying scenarios. Next one is, again, like,
log comes again here, but this is a different use
case, log and media streaming. So what happens with
log and media streaming is that you constantly get new data. So let's say, you know,
you have applications and internal services creating logs, so new data is coming, or let's say you are a broadcast company and you have continuous feed coming in, you typically write to an existing file, and before we had the append capability, customers used to provision
and manage their own storage on top of S3, and then that's where
they created these files. And then when you have these files, you have consumer applications. If you're a broadcast company, then you probably want to
send it to your end users. If you are an observability
company, you want your end users to be able to run
analytics on these files. So you want to perform reads as well. So with three Express One Zone, because now it has the append capability, you can essentially create these files in the object storage itself. So you don't need to maintain an additional layer on top of it. You can build your files, you
can use the append capability, and you can run high-TPS,
low-latency queries on top and have, like, the full workflow running right from object storage itself. So that simplifies
architectures, lowers cost, and obviously improves performance because of the unique
performance characteristics that S3 Express One Zone offers. Last but not the least on
this slide is model loading. So over the last I would
say year or two years, a lot of enterprise companies are now building inference pipelines. In an inference pipeline, let's say if you're a e-commerce company and you have a recommendation engine, you may need to update your models because let's say your
inventory has changed or your customer uses pattern has changed and whenever a model gets updated, customers want their inference notes to pick up the updates
as soon as possible. And in a typical inference pipeline, you would have tens of thousands of node. We have also seen, like, 100,000-plus nodes trying to read, you know, a model and and
weights which is just a few files pretty much at the same time. So it's a very bursty access problem. With S3 general purpose
buckets, as Ian was explaining, the TPS capacity is scaled gradually. You can scale to very high levels, but the scale up is gradual. If you suddenly have, like, a burst of 100k GETs coming
in, let's say on a new bucket, then you may get slow-down error messages. You can retry but that that
may slow down the workflow and that is something that
customers are very sensitive to, specifically for these real-world inference pipeline use cases. So this is, again, where S3
Express One Zone's high TPS out of the box really comes
in handy for customers and we have customers building
a bunch of model loading and inference pipelines
on S3 express today. Before go we go on to the next slide, I think by this point we understand that, you know, S3 Express One Zone is the fastest object storage, offers 10x faster access
times compared to S3 Standard, so it's actually a really good option to build your cache on, right? So you can keep your data in
the general purpose bucket in your regional storage classes, you get multi-AZ resilience, and have a caching layer that runs out of S3 Express One Zone, and that's exactly why we have
a number of customers today using S3 Express One
effectively as a cache on top of general purpose bucket and regional storage classes. One of these customers we are
super excited about is Tavily. Tavily is an AI platform company. They basically serve
as the web access layer for agentic workloads and
large language models. And previously, they managed
and built their own cache, they provisioned storage and used that to deliver
low-latency access to these agentic workflows. But it's harder to scale, as you would imagine,
their management overheads. So they started looking
into S3 Express One Zone, and today, they're running on production and their caching layer is
basically S3 Express One Zone. It scales elastically, delivers single-digit
millisecond access times, and the total cost of ownership of Tavily has gone down by up to six times. Just an example of how elastic scaling and high performance out of
the box can help customers save costs in addition
to improving performance. All right. So now, at this point, we appreciate, I hope, the performance, the differentiated performance
of S3 Express One Zone, the popular use cases
customers are are using it for. Now, let's go into some of the
architectural considerations that you may want to keep in mind when building with Express One Zone for one of these use cases or any other use case you
may find it useful for. There are basically three considerations. The first is its single
availability zone nature, single, it's a zonal storage class. The second one is the directory buckets, which is a new construct we announced alongside S3 Express One Zone. And the third one is its
unique auth mechanism that we will talk about, which is optimized for low-latency access. So let's review each of
these in greater detail. S3 Express One Zone is a single-availability zone storage class, which basically means that
when you create objects, it is stored in a directory bucket in a single availability zone. This allows faster access, but that doesn't mean that
you cannot do cross-AZ access. Once you create your directory bucket, you add your object there, you can access it from a
different availability zone. And one of the remarkable characteristics of Express One Zone is that the access remains the same. So regardless of whether you're accessing your directory bucket from
the same availability zone where it is located or you're accessing it from compute, from a different availability zone, there is no additional network cost. Something to be aware of in
case your fleet is really large and distributed across
different availability zones, which is pretty common for use cases like machine learning training and large analytics workloads loads. Now, let's talk about the second
architecture consideration that I would say, like, a design concept. So S3's directory bucket is a relatively new type of bucket that we launched two years ago. It exists alongside our
general purpose bucket and has a pretty different
scaling model as far as TPS goes. So with general purpose
buckets, as Ian was explaining, it scales TPS capacity based on load. So if your TPS load
increases on the bucket, then it automatically scales
to higher TPS capacity. On the other hand, with directory buckets, as soon as you create a directory bucket, it is already scaled up to 200k or 200,000 GET requests per second and 100,000 PUT requests per second. So if you have bursty access use cases where it's hard to predict, let's say you have a whole
bunch of end customers sending observability queries and you don't know which query is going to be, like, super bursty or you have, like, model loading pipeline that I was talking about earlier, then you want your bucket
to be already scaled up, and that's exactly what
directory buckets are. They're already scaled up to 200k GETs per second by default, 100k PUTs per second by default, and you can also request
for further scaling to up to 2 million GET
requests per second. So different scaling models of TPS relevant for different use cases, depending on the nature
of your application. Moving on, as the name suggests, directory buckets store their data in directories. No surprises there. And the namespace is
basically hierarchical. The implication of this is that if you try to run a list operation against your directory bucket and you're trying to
list the entire bucket, then your list results are not going to be
lexicographically sorted. This is in contrast to
general purpose buckets where your list results are
lexicographically sorted. Why does it matter? We always want to make
it easy for our customers to reuse existing
applications, existing code. So if you are reusing your code that works against a
general purpose bucket, this is a consideration
you want to be aware of. If your application, for example, doesn't make any exemptions
of the list order sorting, then it's totally fine. But it does, then this is something that
you may want to be aware of. Next, let's talk about auth. When we launched S3 Express One Zone, we also launched a new auth mechanism, the session-based auth. What happens with session-based auth is that you have an API, the CreateSession API, that you use to create a session, again, no surprises there, and get temporary credentials that you can then use in subsequent requests for authentication. What this does is it
amortizes or distributes the cost of your auth
across multiple requests, which basically means
that each of your requests actually finishes faster. Again, the reason why we did this is to improve latency performance for every single request that you make. If you architect against
REST APIs directly, you would need to use this API
manage sessions and tokens. However, if you use one of our SDKs, then this is done for you. So basically, the session
management and token management is taken care of by SDK, and you don't have to worry about it. Again, something to be aware of, and we strongly recommend using our SDK and CRT and other stuff
that I'll touch upon again and Ian already talked about. Okay, so to summarize what
we have talked so far, if you want to use S3 Express One Zone, if you have one of the use
cases I talked about earlier, you create a directory bucket first, scaled out to 200k GET TPS by default, you want to have your compute
in the same availability zone to optimize for latency. You can keep it in different
availability zones as well if your fleet is spread out. But to get the best latency performance, you want to co-locate
your compute with storage. You want to use the session-based auth to access your objects. And if you're using your SDK, then session management, token management is taken care of for you. With this architecture, you achieve high-TPS, low-latency access right out of the box. You increase the speed
of data access by 10x and benefit from S Express
One Zone's performance for request-sensitive or
request-intensive applications like machine learning training and latency sensitive
applications like query. To put it all together, what Ian talked about, like, what I talked about
and taking a step back, when you are thinking about
optimizing performance for your use case, you want to
think about the requirements, you want to think about
what's the latency requirement of your end user or the application, you want to think about
what is the access pattern, whether the requests are bursty, whether the the request rates
gradually increase over time, and you wanna think about
the kind of throughput that your application and
your workload would drive. If your access pattern is bursty, if you have end users waiting and your application is latency sensitive, then we recommend using
S3's Express One Zone. On the other hand, if your TPS load increases gradually over time or you have predictable access patterns that you can partition your
prefixes as Ian was describing, then you want to use
general purpose buckets and you can use any of our
regional storage classes, like S3 Standard or S3
Intelligent-Tiering. Regardless, we strongly
recommend using CRT-based client or Amazon Common Runtime
library-based client because it implements a lot of performance best practices, like use of multipart uploads
and range GETs, for you. And you can benefit from
CRT if you're using our SDKs and opt into it, or if you're using
Mountpoint for Amazon S3, which is our file client
for object storage. Here is a best practices reference, essentially a blog which contextualizes everything that we talked
about in the context of a really popular use case these days, which is checkpoint storage. If you're in the ML space,
strongly recommend reading it, and even if you're not,
recommend reading it so that, you know, you get a sense of everything that we talked about in the context of a real-world problem. On that note, we really
appreciate you joining us today, and hopefully you found
the content useful. We request you to share
feedback on the app, and enjoy rest of the re:Invent. Thank you. (audience applauds)
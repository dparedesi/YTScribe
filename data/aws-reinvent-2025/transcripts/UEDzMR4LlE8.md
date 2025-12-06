---
video_id: UEDzMR4LlE8
video_url: https://www.youtube.com/watch?v=UEDzMR4LlE8
is_generated: False
is_translatable: True
---

- Everybody good? You all know you could
be at lunch right now, but you're here with
me, and I appreciate it. Obviously, this is a sold out session, and since the camera's on me, no one will know if I'm telling the truth. My name is Dutch Meyer. I'm a principal software engineer with Amazon Web Services,
Elastic Block Store, GBS. I'm joined here by our
principal product manager, Sapna Gupta, and we're
gonna talk to you today about how to get the most
out of your GP3 volumes. If you don't already
know, the GP3 volume type, as an operator of the service every day, the volume type I see the most of is GP3, and that's because it's designed to be really the default
choice or the best choice for the widest range of workloads. It's called general purpose for a reason. So, I'm gonna talk a little bit about how we think about running that service, how we think about building it, and what you can do to
get the most out of it. Here's our plan. I'm gonna start the session. I'm gonna talk mostly
about reads and writes down the I/O path. I'm gonna stick to storage fundamentals. I'm gonna talk about this problem of coupled versus decoupled storage, and I'll go into that in much more depth, but what I'm talking about there is the way that your capacity of storage and your performance of storage
is coupled together or not. I'm gonna talk about how to
monitor that performance, make sure you're getting what
you're supposed to be getting, and what to do when you start to get out into the extremes of performance. And then Sapna's gonna take over. Do you wanna introduce yourself? - Good afternoon, everyone. This is Sapna, Principal
Product Manager at AWS. I'm super excited to be here today. Thank you for joining us. No, it's lunchtime, but hope
you all enjoy this session. After that, you can go for the lunch. I'll cover the last two
topics of this session today. How do you evolve your volume to optimize for price and performance? I'll cover that not just for
your primary environment, but I will also talk about
how do you do the same thing for your secondary environment? So with that, I'll hand it over to Dutch, and then I'll be back. - Thank you so much.
- Thank you. - Okay, so I care a lot about storage. I'm really passionate about being a storage optimizer, a builder, but as a confessional, in my private life, I am extremely wasteful in storage. So I have by my computer
at my house, a rack, not in the server sense, but just like a bookshelf
full of hard drives. It's basically all the
hard drives I've ever had. A couple of them are disassembled
because I was curious, but I'll be an egregious
waster of space there in my personal life,
and if you're like me, and I know I am, a lot of
you are doing the same thing. You've got a whole bunch
of volumes lying around. You're not really using them, whether they're physical
disks or EBS volumes, or you're taking a system
and you're benchmarking it full speed against something else, and the point I wanna make here, it's really important for GP3, is that an optimized
system is not a system running as hard as possible. It's a system that's in balance, where your IOPS and your
throughput and your capacity, your latency certainly, and in some cases, even your durability is correct and aligned to the workload you have. So that's what I mean by optimized today. Storage is about making those hard choices between those different trade-offs, and what I'm gonna talk about is how we can build this system, GP3, which is meant to serve the vast majority of customer workloads, and all of them are valid points in that space. So looking at the range of possible performance characteristics
and sizes of GP3, it's quite large. We go from a one gig volume all the way up to 64 terabytes today. And that's important not
because it's so fast, it is fast, but there are
faster volumes you can get. What's important about this for GP3 is that anywhere in that space is a valid GP3 volume with GP3 behavior, GP3 durability, and it's
even more complex than that because if you step back, you
can move in either direction. You can move in the capacity direction, make a large volume that's cold. That's a valid GP3 volume. You can make a smaller volume that's fast. It's a valid GP3 volume. If those numbers look a little bigger than you're used to, it's
because we bumped them in the last month or so. I was actually involved in this. We took the capacity up four X, the IOPS up five X. Again, all valid GP3 volumes. So I wanna talk about how we do that. It's important to understand, how does EBS work as a service? And then I'm gonna talk about what it means to do that scaling, to make a bigger GP3, and how you can take advantage
of it for your workloads. Your volume comes to us as provisioned with some kind of entitlement. It's got a set number of IOPS. It's got a size. You let us know what that is. What we do internally
is we take that volume and we shard it. And lots of systems shard. It's a core technique of storage. The thing I wanna point
out about this sharding is that it lets us take that large span of different GP3 characteristics and reduce it to a smaller
set of shard characteristics. So your entitlement from
a performance perspective is carried through to the shard that makes up your volume. But because we can vary
the number of shards, we can reduce the span, make it actually less dynamic. So smaller variance in our fleet of the performance that
those shards bring. What you get with that GP3 volume is the ability to purchase a decoupled performance capacity volume. And I am deeply envious of that ability because on the EBS side,
I actually can't do that. When I go and I buy raw commodity storage, you can imagine me
buying it off Amazon.com, I can't get exactly the right volume that Sapna's gonna need
for her desktop tomorrow. It's absolutely not what I do. If you look at our fleet, it's
actually fairly homogeneous. Now we vary by vendor. We vary by size and
performance a little bit and we do roll our hardware
revisions regularly, but our fleet is actually
fairly homogeneous from a disk drive perspective. So what we're doing somehow is we're taking a very
coupled storage fleet, we're turning it into decoupled storage. And when you, the
customer, buy that fleet, and let's say you're off in
the extreme of performance, you've got high IOPS, we have the freedom on our
side to use our fleet size to put that in the fleet
at the right place, the right place for
that is probably nearby some other customer who has
a capacity-heavy cold volume. It's kind of the core magic of EBS is that we can turn our
hardware, our physical fleet, a very coupled performance
and capacity storage into a dynamic offering that
gets a mixed performance and then we recombine them to utilize that hardware
as much as possible. So two immediate lessons
on your side of the stack. One is by specifying the
IOPS and the throughput that you need to be exactly what you need, you actually enable me to do a better job placing in my fleet to take
advantage of my hardware and it lowers costs for all of us. We actually just pass that
on to you for the most part. And then when we wanna
increase the performance as we did about a month ago, for GP3, the naive approach would be, oh, you can add more shards, right? You just like scale that out. You get twice as many
shards, it goes twice as fast 'cause your IOPS are spread twice like. That is actually not what we do. Because when you do that,
it has ramifications to the lived experience of GP3. It actually makes your GP3 volume, the performance impacts are
not what we want for GP3. It makes those, it means that anywhere that there is a hardware event, something unfortunate
happens in our fleet, you're more likely to feel
that the more shards you have. So what we actually do when we're looking at increasing the range of GP3 is we're making those
shards more performant all the way down the stack. Okay, I'm gonna talk about
performance in a minute. I wanna circle back on this coupled versus uncoupled performance because we do have a GP2 volume type. People use it, it's fine. But GP2 is giving you
that coupled performance. When you buy a GP2 volume, you're getting capacity and
performance tied together. It's a fine replica of
buying a physical disk. But it doesn't actually
have the characteristics that I want you to have as a customer. I want you to be able to independently scale those two axes. GP3 in comparison gives you
that decoupled performance. If you want more IOPS,
you can buy more IOPS, mostly independent of
the underlying capacity. And what you get there is a cost savings. So what this enables you to do is to build a strategy for your volumes depending on your workload. And this is the core trick that lets us create this volume type that is the most broadly applicable. Go ahead, take the picture. So for more transactional processing, you want more IOPS, right? More IOPS returning with
more latency quickly. Those tend to be smaller operations. For larger throughput, you're gonna have larger block sizes. The IOPS and throughput are connected to the block size that way. And in that entire range, you're getting GP3
latency and performance. So let's talk a little
bit about performance as measured by latency, because of course, performance is more than
IOPS and throughput. Controlling latency is really important. So I monitor latency extensively. It's the thing in EBS
that is kept constant. So your experience from a
latency perspective is the same, no matter where you are in
that range of GP3 volumes. GP3 experience we talk about as a single digit millisecond experience with 99% compliance. In comparison, there are IO2 volumes. Those are great if that's what you need. That is a very different experience. That's sub millisecond. And the biggest difference
I think of with IO2 really is the conformity
to that experience. I won't put the full GP2, this isn't a GP2 talk, so I won't give you the full
performance curve there. But I can say that the
incidence of IO operations that take more than 800 microseconds is 10x lower on IO2 than GP3. So if someone needs
that really fast latency and they need that really
strict compliance to latency, that's the IO2 experience. It's just different from the GP experience regardless of how many IOPS or how much throughput you have. Okay, so we've talked about coupled versus uncoupled storage. Talked just a little bit about latency and what the product is. I wanna give you one of my best tools. I use this every single day. This is not about EBS. This is just storage fundamentals. But there's a relationship
between your latency and your IOPS. It's connected by queue depth. This is just basic queuing theory, okay? Your latency is your queue
depth divided by your IOPS. It's physics. And there's a linear
relationship between the two. So let's say, for example,
you've got a GP3 volume. You've got some workloads running on it. And at noon, you figure
everyone's gonna be at lunch. So you set your cron jobs
or your scheduled tasks to all fire at noon. They all fire up. They launch a bunch of
IOPS against the system. What happens? All those operations
increase the queue depth. You get more queue of
operations coming in. The result is you get more performance. Your IOPS goes up. Your latency's gonna hold constant. Your IOPS is gonna increase right up until you hit your IOPS entitlement. And when you have enough
scheduled jobs firing all at the same time to hit that cap, then your latency's gonna
come up in response. Anytime I'm looking at a system
and trying to figure out, well, what is this system doing from a storage perspective? I've got that equation
in the back of my head. It will make you seem really
smart in front of your peers 'cause you can just throw it out there. By the way, if you jitter your cron jobs to not start on the hour, then I won't see a huge spike
in IOPS every single hour. That's my problem, just saying. But you could be a friend. Okay, this slide is the same thing. I'm just gonna reiterate
the same thing again. The queue depth, the IOPS, the latency are all connected together. You can bring your performance up by increasing your queues
up to your IOPS entitlement, and then you're gonna
start to feel latency. But what this means is that
you actually have control of your latency. Even though the latency of the GP3 product is the thing that I hold constant, you actually have a lot of
control in both directions. If you drive it too hard from
a queue depth perspective, you will see the latency come up. Your instance will start throttling. We actually have, it was October, late October release, there
are CloudWatch metrics now that will tell you when this is happening. So you can diagnose this yourself. There's also new CloudWatch metrics to manage throughput and latency. So we have that monitoring built in. You can look at it directly. The actual performance of the queue depth versus the IOPS and the latency is gonna depend on your
workload and your block size. As a general rule, you should expect when you're in the 16K
range for block size, one QD per 1,000 IOPS. And if you reverse the math on that, it comes to one millisecond latency. It's all connected
exactly by that equation. So that is the theory. That is the basic theory of storage. It is absolutely true. But I think we know in practice, the average doesn't tell the whole story. In practice, we have to monitor across the range of
performance characteristics. So again, how do we monitor? We've got CloudWatch metrics. We've got NVMe CLI. There's some new commands here
I'll talk about in a second. The best tool that I have
to monitor performance is actually a latency histogram. And again, this is not EBS specific. This is just fundamental storage. So I'm gonna show you what a
latency histogram looks like if you haven't seen it. I'll talk you through the slide. This is an actual latency histogram. It is not internal EBS. It is something I pulled from
my personal cloud desktop on one weekend day. Let's look at what my system is doing for the purposes of this deck. You'll see sort of a pulse wave. On the x-axis, that is your
latency in microseconds. So 1,024 microseconds,
that's about a millisecond. That's where you get the peak. On the y-axis, that's the
number of I/O operations that fall into that latency bucket. This is nine times out of 10 the best way to look at your latency of your system. So when I am dealing
with a latency histogram, the first thing I look at
is, well, where's my peak? That's sort of the typical performance. In this case, it just happens. It's around a millisecond. It's about what I expect
from a GP3 volume. I kinda was hoping I
would get something weird in my graph, but I didn't. It's a normal behaving system. I also look at how that pulse is skewed. If it's totally normal, I'm
getting an even distribution of I/Os that are slower and faster. In this case, I'm skewed
left a little bit. So the system is generally
under a millisecond. Again, it's pretty good
performance for a GP3 volume, especially one that's not
under a lot of stress. Queue depth isn't that deep. I think about how wide this curve is. That's the variability in performance. So here, there's some
variance in performance. I'm getting four milliseconds. I'm getting one millisecond. I'm getting things that are completing in a quarter of a millisecond. It's pretty fast. If this were GP, sorry, if
this were an I/O two volume instead of a GP3 volume,
you can sort of predict what you'd see. You'd see that whole
pulse skewed to the left because it's faster, and you
would see the width narrow because it's a more compliant system. That's just a different lived experience. Now, when you have a graph like this, it's great to track it over time. You know about what your system's doing. You can track how that's
changing over time. When you start to have
a performance problem, what that will show up as is a new mode, a new bump, usually towards the side that we care about there, that right, that I guess would be
left side for you, right? In the high latency band,
when you see a bump there, that's a bunch of I/Os that
are delayed by something. So I wanna talk a little bit about what causes those latency
outliers that we see and how we handle them. Before I do that, I do
wanna point out this. So this is actually EBS NVMe output. The tool that you can
use to grab it is there. That's the tool I use to grab this. We also have CloudWatch metrics with this histogram now
built in on Nitro instances, but you can also use
basically any tool to monitor. We use IOstat extensively. Any tool that monitors performance you can use to build
this kind of histogram. So let's talk about what
causes these outliers. I have to go in to how SSDs are built. I'm gonna do it on a very shallow level. I can talk for an hour about this. If you wanna learn more about SSDs and programmer race cycles, I would love to chat with
you outside this session. But essentially your SSD, whether it's your phone or
your laptop or EBS storage, it's a physical device. It's a real disk. It's made up of blocks and
those blocks have cells. Inside the cells, there
are little MOSFET gates that physically trap electrons. They're super cool. But because they're a physical device, they're subject to the cruel
whims of the physical world, which means things break. Those little gates can break. And when they break, there's a bunch of failure
modes for a physical disk. But one of them is that it can find that it's unable to
reprogram one of those gates. And when it does, when it finds that, it'll retry a few times, but then it'll declare,
"Oh, I've got a dead cell." And what the disk has
to do with a dead cell is it's gonna have to move
information out of that block, mark the block as dead, and go onto a new block. Now, if I pick a random
server in our fleet, the odds are it doesn't have
any of these dead blocks. But if I picked a couple
servers, I would see a few. It's normal, it's healthy, it's fine. But when that happens, when the disk has to
take on the extra work of moving the data from one block that's been damaged to another, we will see latency events on the order of 10 to 100 microseconds. They can last a little while as the disk works through that workload. It's unavoidable. This is just a fact of
living with storage. You have those outliers. And if I had one or two of those, those could be consistent
with a GP3 experience. But as a general rule, I don't wanna just pass
those upward to the customer because GP3 as a product
has its own experience. You would be very unsatisfied with me if I said, "Well, I just failed, so." My job is to present you
GP3, not physical disks. So what we do is we monitor via those same latency histograms, those same throughput metrics. We monitor this very actively. And we have thresholds that tell us when I've got a drive that is behaving outside of the normal operating envelope. What I do is basically
the same as the disk or an analogous behavior to the disk. When I see this misbehavior, I route your data off to another server. I take that server in for repair, or sometimes it just needs
a rest like all of us. Effectively, by using that same technique that the disk uses, I can
build a higher performance, more stable performance product out of less performant
underlying hardware. And that's a tool that works
all the way up the stack, even on services built on top of EBS. Now, to get it, that's a
little high level, I admit. To get into the details, we have to face another one of those really hard choices around storage. There are no, there's no one answer here. It's as varied as there
are different workloads. So let's just thought experiment. You get a request that
goes to some EBS server. The EBS server writes it down. Let's say it's a write request. And then EBS is replicated,
that shouldn't be a surprise, for reliability, durability purposes. We reach out to the peer, we say we'd like you to write this data. And I don't hear back. I don't hear back for 500 microseconds, which isn't that much time,
it's like really short. But for a computer system,
it's actually a long time. So what do you do? And most of your day one
EBS engineers will say, well, you could retry, you could time out, and you could try again. And that's not necessarily
the wrong answer. At EBS, it's the wrong answer. Because we are a very
latency sensitive product. We wanna hold that latency
bar as tightly as we can. Retry is usually the wrong answer. Usually when a host is
telling you that it's slow, it's because it's gonna be slow. And the right answer is
to move past that host. Find a new friend, write the data there. Think about read requests too. One of the tools, so retry is valid. It's valid, I shy away from it, from a performance perspective, 'cause I care a lot about latency. I would rather use the
throughput of my system to move the data away
from a misbehaving peer. One technique we use a lot
of is read and write hedging. So imagine a different scenario where the customer issues a read request. They want their data. I send that read down to disk. The disk is slow. Takes a few hundred
microseconds to come back. It's longer than I expect. I can proactively issue
another read in parallel to the peer that has the data. Say, I don't know if
my disk is coming back. It seems slightly delayed, but I'm just gonna go grab
the data somewhere else. And I'll take whichever
answer comes back first. So read and write hedging
are highly valuable. I can't tell you what the right
answer for your system is, except to say that these latency outliers are a fact of life in all
storage systems at any level. Now, we could build, I could build you the system
where this doesn't happen. It's essentially I/O 2. It's more expensive, right? But a well-optimized system
that suits most workloads, which is GP3, is gonna
have these outliers. What you can do, there's a system called AWS
Fault Injection Service. And this year, we added EBS
Latency Event Injection. So you can fire up Fault Injection Service on your own system. Actually, Sapna's gonna talk about how to get a test environment
out of a production system where this is a great use case for firing up some fault injection to see how your system behaves
to those latency outliers. Most systems will just tolerate them, especially in the write path. You issue a write. The write comes back later. A little bit of latency is fine. Sometimes when you're in a more transactional database mode, that write is the commit block with a bunch of I/O behind it, and you get what's called
head-of-line blocking. That's a big performance issue. So understanding how your system behaves to those kind of latency outliers is really critical in determining how sensitive you are to
latency and what you do if you issue some kind of request hedging or giving up on a peer when that happens on your storage system. So let me wrap all this up. We talked about coupled
versus uncoupled scaling, building your system to
move in multiple dimensions and optimize each of them, so optimizing in the dimension
of IOPS or throughput, optimizing in the dimension of capacity. We talked about using queue
depth to control latency and manipulate that performance, either bringing the performance up if the system is underfed
with a small queue or bringing it down. Shorter queues give you
a faster response time. We talked about monitoring
latency using a histogram, some of the new CloudWatch
metrics we have, and NVMe CLI, which is another
tool on the Nitro instances. And we talked about using
the latency response, the response of your system
to high latency, rather, choosing that really carefully and testing it with
fault injection service. How your system responds to
those different behaviors is what defines the lived experience. I keep saying lived experience, right? It's that lived experience that gets you the GP3 volume type or
the IO2 volume type. That's how we build that product separate from the underlying medium. And that's also how, when
we're dealing with these, we have big surges in our workloads, too. We had Prime Day just
recently hit new peaks for EBS and through it all, we
can maintain our SLAs of EBS performance. So this has all been workloads
in a very static sense, fixed workloads. We're gonna talk next about
how workloads change over time. I'm gonna hand off to Sapna. - Thank you, Doug.
- Thanks. - I love his passion for block storage and the way he explains
some of the fundamentals of block storage is pretty exciting. All right, let's dive deep into how do you evolve your volume? I'm gonna take a step back first. Some of you already know
what is the right performance for you for your specific use case, but some of you may actually not know or may not be sure about what is the right performance place for you. And that is where there are two options. One, you can start with
higher performing volume and then you can scale it down as you learn more about
your volume and the use case and the performance that you need or you can start with
a tighter performance. For example, GP3 baseline performance, you can start there
and you can scale it up as your volume demand grows. Dutch talked about how can
you measure the performance, went into some of the details of latency. So all of those data points
can help you learn more about what is the right IOPS throughput that you need for your specific use case. GP3 is pretty impressive, especially with our recent
launch of higher limits. It gives you a pretty broad spectrum. For example, data size,
you can start pretty small, one TB and then you can
go up to 64 terabyte. On-demand power, now you
can go up to 80,000 IOPS and if you need that only
for a short amount of time, for example, just for a
few days or a few months, you can leave it till then and then you can scale back
down when you don't need it. That way you're not
paying for the performance that you're not utilizing. Striping is a technique that
some of our customers use to get the right data size
and also the performance. But with GP3 larger and higher limits, you don't have to worry
about the complexity behind striping. You can reduce and minimize that overhead by just increasing independently
your IOPS and throughput. So let's get into what is the mechanism for you to evolve or modify your volume. EV is the way to go. It basically allows you to
dynamically increase your size, your IOPS and throughput independently. There are three actions
that you can change, that you can take. First one, change volume. What if you just want to
migrate from GP2 to GP3 or GP3 to IO2? You can do that using EV. You can also tune your performance
within the GP3 spectrum. You can move from 16,000
IOPS to 80,000 for example. Size, I want you to be a
little cautious about it because size you can only scale up, you cannot come back down. So if you really need
higher size of your volume, please keep that in mind that
you cannot come back down. So what are the best practices? What are the different
steps that you need to take to actually request for a
modification of your volume? One snapshot, for some of
you who may not be aware of what snapshot means, is a point in time copy of your volume. And you can restore your volume from that specific snapshot. Once you take the snapshot, there are different ways of requesting the modification of your volume and you can ask for GP2 to GP3 or within GP3 you can
ask for different limits. After that, you can monitor the progress of your modification. I'll show how in the next slide. Number four, I want you
to be cautious about, sometimes EC2 instances don't recognize, especially the size change, don't recognize your size change. And for example, if you are
using 100 gigabyte of volume and then you increase the size to 200, if EC2 does not know about that, you're paying for 200, but actually only utilizing 100 gigabyte. So extending file system helps to sync the physical disk space
with the EC2 instance. Here are a few methods using which you can request for modification. One is AWS CLI, PowerShell script. You can just go to your console and also monitor your status. You can see the volume state, your current volume state, and then the modification state. Optimizing basically
means we are transitioning to your new limits that
you have requested. Okay, so let's dive deep
into what is happening behind the scene when you're
requesting for a modification. Raise your hand if you're curious about what happens behind the scene when you're requesting, for example, higher IOPS or throughput. Okay, yeah, it's pretty
exciting to understand. And Dutch explained some of this already. I'm just gonna pick a specific scenario. We are running at a massive scale. We get hundreds of thousands of requests to modify the volume, and that is where we have to
check every single request to make sure where your
volume was initially placed, let's say server A, in this case, we do have the right capacity
to bump up your performance. And if not, then in that case, we replace your volume to the server, in this case, server B, so that you get the
performance that you need, you're able to get the size that you need. And this is pretty seamless, by the way, from customer point of view. I'm just sharing so that you understand what happens behind the scene. Okay, so let's talk about what
are the different boundaries and challenges associated with EV. Although we give you a wide range of GP3, in terms of size, in terms
of IOPS and throughput, there are certain limitations. I mentioned some of them already. One-way sizing. When you're requesting
to go from 100 gigabyte to 200 gigabyte, for example, you cannot come back to 100 gigabyte. There might be some workarounds, but directly, you cannot do so. So just be cognizant of that. The six-hour timer. Between two requests that you're making to modify your volume,
there's a six-hour wait time. And this is to make sure
your volume integrity consistent in performance,
all of that is intact. So we have kept this boundary
to make sure of that. The last one is more along the
lines of what I said before. Some of the older EC2
instances may not recognize, for example, the size that
you have requested for, and that is where you might need to reboot or run OS command to make
sure your EC2 instance is also recognizing the change
that you have requested. I love sharing customer success stories. We've talked about how can
you evolve your volume, what is the mechanism to do so, and now let's see one of the example where one of our customer,
VMware Carbon Black, they were actually able to
optimize their cost performance, leveraging GP3. Before I get into some of
the details of the scenario, just wanted to quickly
call out what they do, what's their scale, so
that you can connect with this success story and
may apply a similar principle and strategy to optimize the cost. VMware Carbon Black is a leading
industry in cybersecurity. They're focusing on endpoint detection, next-generation antivirus, they're handling millions
of requests every second. And to make sure their
customer reputation, they're giving the best
application experience to their customer,
latency is super important for this specific use case. They need high-speed volume, and that is where they are using EBS. Here is a pretty high-level architecture. They're using multiple services of AWS. I'm not going to get into the detail of every single service. My focus and this session focus is EBS. They're using EBS for high-speed volume. They're processing millions
of requests and records and sorting and compressing
within the volume using EKS cluster. And for this to work out,
they need to read and write the data pretty often,
and that is where IOPS and their performance is super important. So what was the challenge,
and how did they optimize and mitigate that challenge? Initially, they were using GP2, and like Dutch mentioned, GP2 performance and size is coupled. They just wanted 3,000 IOPS, and for them to get to 3,000 IOPS, they were stuck with two options. One is either they pay for
extra 960 gigabyte of storage and get the 3,000 IOPS, or they could use bursting performance, but that wouldn't guarantee
the consistent performance that they needed all the time. They went for the second option, and that is where they were struggling, getting throttled, and
because of throttling, they were also seeing that
their cluster scaled up unnecessary EC2 nodes. So let's see how did they
resolve this problem. I'm assuming it's pretty obvious by now. We've talked about GP3 quite a lot. They moved to GP3, and
they were able to get guaranteed 3,000 IOPS without
paying for unused storage. And with that migration,
they were directly able to save 20% cost in the storage. They were able to reduce
the number of EC2 instances by 50 count. Altogether, at least they were
able to save 25K per month, and now that number is pretty large. Here's the anecdote
directly from our customer. They also shared this graph. As you can see, the number of EC2 instance decreased by 50 count
after they migrated to GP3, and got the consistent
performance of 3,000 IOPS. This anecdote summarizes
that the migration really helped them, and
they were able to save several thousands of dollar per month. So this is one story
where one of our customer moved from GP2 to GP3,
and they were able to optimize price and performance. You can also do that within GP3 spectrum with the higher limits
that we offer today. Okay, so far, what we have talked about is in the context of primary environment. How do you improve, or how do you optimize the price and performance using GP3 for your primary environment? But what about secondary environment that you might be using for dev testing? How do you think about
optimizing price and performance for those use cases? I'll share one scenario. Previously, when we did not
offer higher limits of GP3, our customers were stuck with IO2 when they needed higher
IOPS, 16,000 for example. And in case of secondary environment, unless latency and
durability is super critical, you can actually now move from IO2 to GP3 and pay much less for your dev testing. And that way, you're able to optimize cost and not paying premium for IO2 when you're just experimenting
with your use cases. This is one scenario. Within, again, within
GP3 spectrum as well, you can do a lot more,
strategize how you want to optimize your dev environment. Now, similar to primary environment, I wanted to touch base on, how do you even make
a copy of your volume? How do you create a secondary environment without interrupting your primary production live environment? There are two methods to do so. One is snapshot. Snapshot, again, it's a point
in time copy of your volume. You take a snapshot and
then you can hydrate or restore your snapshot, your volume from the
snapshot that you have taken. Since we are talking about the cost and the price and performance, I wanted to educate you
on how EBS snapshot works and how behind the scene
we are trying to optimize that price and performance for you by avoiding duplicated data. State one, for example, you
have 10 gigabyte of data, 10 gigabyte of volume. If there is no snapshot existing, we will first take the full snapshot. And state two, let's say you made a
change of four gigabyte. In that state, we are not going
to take the full snapshot. Again, we are only going
to take the snapshot of four gigabyte and
refer to the snapshot A for six gigabyte of data
that you have not touched. That way, we are not duplicating, you are not paying multiple
times for the full snapshot. State three, let's say now you have added two gigabyte of data to your volume. Now in state three, we
are only going to take the snapshot of two gigabyte, refer to snapshot B for four, and then refer to snapshot A for six. So you're only paying for
the incremental backup here. And that is what I wanted you to take away to make sure that we are
optimizing the cost for you here. This works even if you have hydrated, even if you have restored
your volume from the snapshot. In this scenario, for example, if you have a 10 gigabyte of volume and you have taken the
snapshot and you have hydrated, you have restored your
volume, let's say volume two, and then you have made some
changes of four gigabyte. In that scenario, we are only taking the snapshot for four gigabyte, and we are maintaining your lineage and referring to snapshot
A for the 10 gigabyte of data that you have not touched. All right, so some of
you might be thinking, okay, snapshot, we take a snapshot and then hydrate or restore. There are two steps involved here. What if you want to
optimize the performance of restoring, of hydrating your volume? Sometimes you may want immediately because you have critical use cases. So we offer three options here. Depending on your use case, how critical your application
is, you can pick and choose. For you, if you care more about cost, you can go with the standard restore. It's a free tier, you
don't have to pay extra. But if you need predictable performance, how soon you can recover the volume, or if you need to see
your volume immediately, then we have two option, provisioned rate. You can pick the speed at which your volume is provisioning. And then also FSR, you get
instant access to your volume. Those two options you have to pay, and that is where you have to think about the strategy of optimizing
cost and performance. All right, especially
for the dev test use case where you just need to
create a copy of your volume, there are certain limitations, especially if you need an
instant copy of your volume. Like I mentioned before,
snapshot have at least two steps. You need to first create the snapshot, and then you need to restore your volume from that specific snapshot. Your copy may not be instantly available depending on which option you're picking. Restore is definitely required. So this is where we have
recently launched clones. If you're looking to instantly
just copy your volume and want to just start with the testing, one click of a button, you can do so. One API, instant point-in-time
copy, no restore required. So how does this clone works? We have EC2 Instant. There's also a volume attached to it. Let's say in this scenario, IO2. And if you want to,
like I mentioned before, if you want to optimize the cost here, you can actually choose GP3 when you're copying your volume. And that way you're not paying
for the premium IO2 volume. Instead, you're just paying for the GP3, which is much cheaper. On the console, there's one option. You can click off a button. You can just create copy. (audience applauds) All right, we have reached
towards the end of our session. I'm just gonna quickly summarize the last two topics that we talked about. GP3 gives you a pretty large range of size, IOPS, and throughput. With that and the EV, you
can evolve your volume. You can migrate seamlessly
from GP2 to GP3. You can fine-tune, right-size your volume depending on your use case
and what you've learned about your data by monitoring performance. You can modernize your architecture. Now we offer up to 64 terabyte
of size limit with GP3. And the great thing about EV and GP3 is we are doing this in place. You don't have to worry
about stopping your instance. You don't have to worry
about detaching your volume. All of that is happening behind the scene. For you, the live and
production data volume is not interrupted. We have about 11 sessions
at this re:Invent lined up. We're done with four of them, so I would highly encourage
you to look at other sessions if you want to learn more
about EBS and EBS snapshots. Snapshots in particular,
if you want to learn more, we have STG325. We have got STG326. I'm co-presenting STG406 on Wednesday if you're interested in
having a hands-on experience and learn more about EBS snapshots, you can come join us there. With that, thanks a lot
for staying back in here. We would love to hear your feedback. This is how we evolve our content and make sure it's relevant. So please take the survey and let us know how you like the session and enjoy the rest of your re:Invent. Thank you.
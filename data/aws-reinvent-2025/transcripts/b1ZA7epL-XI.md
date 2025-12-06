---
video_id: b1ZA7epL-XI
video_url: https://www.youtube.com/watch?v=b1ZA7epL-XI
is_generated: False
is_translatable: True
---

- Welcome to Vegas.
Welcome to re:Invent 2025. You are in ANT 307, operating and scaling managed
Apache Kafka and Flink. My name is Ashish Palekar. I take care of our Kafka, Flink, and Firehose services here at AWS, which means that I spend
time talking to customers, but also building the service, but also operating the service. With me is... - I'm Sai Maddali, I
lead the product teams for our Amazon managed streaming for Apache Kafka, managed
service for Apache Flink and Amazon Data Firehose. - Very cool. So today we are going to cover a bunch of what we are doing with
our Kafka and Flink services. We're gonna walk you through our learnings and compare and contrast, give you a sense of what we've learned and hopefully we can cover a
lot of details in the session. So let's get started. As we go through it, a lot of customers often
start with why streaming data and why now? It really boils down to four things that we hear from customers. It's about unlocking
real value from your data in real time as it flows, helps you make decisions in real time and shorten the time to
actually get to insights. You can get continuous
intelligence from that data. And last, but not the least, as we are continually seeing
now with AI workloads, you need more contextualized data. You need more fresh data. And streaming technologies
help you get that. Here at AWS, we love Kafka and Flink. We have had Kafka and Flink services for well over five years at this point. And in fact have been operating
workloads for customers. We have customers who also
use self-managed Kafka and Flink in addition to ours. And there's certainly other
partner solutions as well. But really, we see a large and wide variety of
workloads across the board. So one of the things I
get asked by customers is what are the outcomes
that customers look for when running at scale? What do customers really care about? It really boils down to price performance, boils down to reliability,
boils down to security and boils down to performance. These seem like basics, but at the same time, at
scale, these are magnified. And every one of you
that is operating a Kafka or Flink service knows that. Just by show of hands, how many of you operate a Kafka service? Vast majority of you. Awesome. So that this helps Sai later on, how many of you use Flink? Few of you. We'll talk about that too. Thank you for being our customers. These are some other customers. Customers make our world go round and this is absolutely super
helpful for us to understand what customers are doing. So let's talk about
running Kafka at scale. Always love to start
with a customer example. Nexthink, Nexthink is a customer
based out of Switzerland and really focus on how to go
build developer experience. Their core problem was how to help scale their
Kafka business, switch to MSK. They were running on premises, switch to MSK on AWS, and
they can process now trillions of events a day, reaching
five gigabytes per second of aggregated throughput. Really has been compelling
to watch their journey in scaling from 200 megabytes to five gigabytes per second. And that has taught them, as well as us a whole bunch of lessons and as we observe workloads
across our customers. So when we think about
the spectrum of Kafka, and I'll speak to sort
of the services we offer, we think of it across a
two-pronged spectrum, right? Like, on the left-hand side,
you have more Kafka control and on the right-hand side,
you have more Kafka automation. In the more Kafka control
case, we offer standard brokers for Amazon MSK. This is the case when you're migrating from an existing Kafka setup. You need fine grained control for Kafka and have deep know-how
about how Kafka works. And that becomes important. On the other end of the spectrum
is Amazon MSK Serverless where you can quickly
deploy and scale up Kafka. You don't need Kafka
management and you don't need or care about the nuances
of managing Kafka. And in between, this is
something we launched last year, last November, is Express brokers for MSK where you value performance and elasticity where you want or need
lower control over Kafka. And typically what we see is
this is a set of customers that is managing Kafka at scale. And this is something
I provide as guidance to customers when I talk to them. Unless you know differently, always recommend you start from Express. It's a good place to
start for your workloads and then decide where to go. So across this family of products, we see a diversity of Kafka workloads and it gives us really,
really interesting insights. We see customers operating
at small scale, large scale. We see customers operating
with a high partition count, low partition count, combinations of both. And that entails different things. One of the first areas
that I'll talk about today is about storage management. And this starts to get tricky, especially at scale. Specifically, storage scaling takes time and as we started looking at it, you can go from four terabytes to eight terabytes to 12 terabytes. All of this is possible. One of the things we
consistently see is customers who are not monitoring
their storage utilization. In fact, your storage
utilization can spike. You can start to start to see that grow as workloads change. If you haven't already, there
is something MSK offers, you should subscribe to disk full alerts. You get alerts at 60% full, at 80% full and then when it's actually full. But that will alert you to make sure that your capacity is
actually taken care of. One thing we noticed is it
is easy to scale up capacity, but you don't have a capacity scale-down. And that is something
that trips up customers. And so customers often
delay making a decision about scaling up and
something that is a tension that you need to wrestle
with as customers. Recognizing that, one of the things we did is when we built Express brokers, we eliminated storage management. What we operated with is really started with not having any storage configuration. Just tell us your attention period and we are off to the races. You get virtually unlimited
storage capacity per broker, which means you really don't
have this conceptual notion of what a disk full looks like. Your storage is provisioned
per cluster versus per broker and that obviously has cost savings, but equally importantly makes it easier to sort of imagine what your
overall workload size is and then you pay for what you use versus needing provisioned capacities. And last but not the
least, you get hands free and instant scaling on the storage side, and that is also super useful. So if you really look at
sort of the core tenets of how we worked on storage management, if you think about it
in the Express context, our focus was we wanted to
eliminate storage management for you and that entailed
doing all these five things. The other area that that we see where customers are challenged with is around failure handling. And so you say, "Well,
what does that mean?" Well, here what we have
is a three-broker cluster. You have producers, you have consumers, you have consumers in the consumer group. The producer is producing
to two brokers here. So what does the basic traffic look like? You have producer traffic,
you have consumer traffic, you have replication traffic, and depending on your workload, you have partition compute needs, right? Very rarely we do encounter workloads or I guess not so rarely,
we do encounter workloads that are partition bound. And so you have to
account for that as well. And this is the basic configuration that as customers you need to account for, which is what's my producer traffic? What's my consumer traffic? What's my replication traffic and what are my partition compute needs? And then failures happen. Let's say a broker dies. What happens in that case? You need buffers for
handling broker failures. How does that look like? Your producer swaps, your replications switches,
your leadership changes, and then the broker comes back, which means your first broker
has to actually account for the throughput of
two producers, right? Now your broker comes back and now there's different workloads that you need to account for. What is your catchup replication? What does that look like, right? And eventually, then as
the broker rebalances and producer reswitches,
you also need to account for what happens when there's
a consumer rebalancing. And there is some
interesting new innovation that is happening in the
Kafka space around us. But all of these are things
that you have to build in when planning your workloads. Too often we encounter customers who have workloads that work fine when things are going fine, but when failures happen, that's when they encounter problems. And these are some things
that we ask customers to sort of think through. What does your failure
handling actually look like? But failure recovery is also time taking. So it's not just about having the space and buffers to actually
account for these failures. It's also accounting for time. And specifically in this case, what happens is in the
standard Kafka case, you're scaling compute
and storage together, and especially after a
node recovers from failure, it has to catch up. This process is time consuming, but it's also non-deterministic. What does that mean? It's dependent on what is
your storage throughput? What is your storage capacity? What is your compute to local
storage network throughput? So you have all these
different factors that are sort of competing for attention
in that infrastructure, which means your recovery time is going to be dependent on that. Interestingly, Kafka is a
remarkably stable system until failures happen. And at the point that failures happen, then the thing that
you can do as customers is to wait for recovery. And that often is where a lot of our customer conversations happen is around how have you
thought about failure recovery and failure recovery in these modes? On the Express side, looking at that, what we ended up doing
is really rethinking how failure recovery happens. Because we separated our resources, what that means is your recovery is up to 90% faster, right? And that fundamentally means that you're getting high resilience because your mean time to recovery is low. And that is a phenomenally important thing when you're designing
resilient distributor systems is how do you keep your recovery time low so that you can build
resilience for your systems. And I'll walk you through some examples of what that looks like. But that is how Express
brokers is different. What does that mean
for horizontal scaling? Everyone has a plan until they have to rebalance partitions, right? And that is what Kafka
horizontal scaling looks like. You add three brokers, you're going to go move partitions across. You have to reserve enough
bandwidth for rebalancing. You have to carefully
orchestrate the movement so that it does not impact
your existing workloads. And last but not the least, you're continuously
monitoring your infrastructure so that if there's a need
to change the plan, you can. And that's what happens. Rebalancing can take hours
and again is variable. And that is how the system behaves. On Express brokers, because we
have separation of resources, what that fundamentally
means is you can get up to 20x more elasticity
compared to standard brokers. I often get this question from customers, which is what does elasticity mean? So let's look at an example. How fast can I rebalance my partitions after adding brokers while
traffic is still climbing? Here's an experiment that we ran. We had three brokers, one
topic, 2,000 partitions, four terabytes of data per broker. What we did is we had three brokers and we added three brokers,
rebalanced 1,000 partitions, all this while producing
90 megabytes per second . Pretty typical for what we see. And what we did is compare
standard to Express and I'm just gonna show you a
couple of CloudWatch graphs. So here's what standard looks like. You have three brokers
that are at the top. On the left red line is
where we issued the command to add three brokers. You can instantly see
the throughput drops. And the throughput drops
and continues dropping and eventually the new three
brokers start to pick up. And you can see the throughput sort of gets throttled further and eventually the throughput stabilizes and behaves as if it's six brokers, right? So you get producer degradation until the throughput recovers and that entire process takes
about 175 minutes, right? And so you are going through
this partition rebalancing and adding three brokers until you get productive six
brokers for about 175 minutes. Here's what this looks
like for Express brokers. The left is where we
added the three brokers. Yep, the brokers went
to the new throughput and within 10 minutes, the remaining three brokers were added and they joined the cluster
and produced the traffic. Again, from a customer standpoint, and for you as users of this, what that means is
you're spending less time doing partition rebalancing, which is giving you a
more resilient system, which also means you can scale
up and scale down faster. You can run this experiment and see what your results look like. But wait, there's more. What we announced a few weeks ago for Express brokers is
intelligent rebalancing. What we've now done is you
get always-on rebalancing, you get auto partition placement, you can do fully automated
horizontal scaling with zero click automated heat management and that gives you
improved price performance from a cluster standpoint. And here's what intelligent
rebalancing looks like. You get up to 180x faster rebalancing, which means shorter recovery
windows and higher resilience, and that is as compared
to standard brokers. One of the interesting
things the team did, which really is sort
of well thought through is you get built-in operational awareness. In other words, we detect
when there's healing going on, when there's patching going on and we prevent unsafe overlap. And last but not the least, we apply all our best
practices for scale-in and scale-out intelligence before resizing our clusters, right? And so that becomes enormously helpful in terms of giving you a signal of what workloads your brokers can accept. So super happy that this
is in customer hands, it's available for Express brokers and it's starting I think two weeks ago. So one of the other thing
was we had to rethink what resilience looks like. And part of this is to
help you understand sort of how we think about resilience and all the work that we had to do to sort of build in resilience. Here's what standard
Kafka behavior looks like. You have a broker, I sort of modeled it as you have a broker with
partitions, you have memory, you have compute, you have
network, you have storage. Kafka classically is an
allocate when asked system. You sort of can request capacity, it'll give you capacity, you can create a partition,
it'll create a partition. And what happens is the
onus is on Kafka clients and the users to not overload the system. And the challenge with that is you only find out you've
overloaded the system by monitoring it well,
by having heuristics, by having experience of
managing your workloads. But when that overloading
happens, it causes broker failures and so you are in the mode
of recovery at the point that you've overloaded the brokers. So one of the things
that we did in Express is you have the same model for a broker, but for each of those, we
have added safe throttles safe dynamic throttles on
compute, memory and networking. And what that means is we
can start to minimize sort of the impact on the broker and protect the broker from failures. In fact, the team has
also had to think through what does it mean to
survive storage failures? Now, you can't survive storage failures for an infinite amount of time, but still it builds in resilience and gives you the capacity,
at least for a while, to survive without storage being there. And last but not the least, especially as we throttle,
your client can then react to the throttling behavior it sees instead of just seeing the failure and then reacting to the failure. So what that means is
from a design standpoint, you actually have the ability
to design your system, to take cognizance of like
the system being overloaded and actually accounting
for it differently. And that is something that
is fundamentally different about what we had to do in order to re-architect for resilience. So it goes further, deeper. One of the other things
that we did with Express is we made it such that you did not need a
maintenance window for patching. We also built in partition-level fairness and what does that mean
is you get protection from noisy workloads. So you can't have a single partition taking up all the
throughput of your broker and you get better protection on that. Last but not the least, one of the things that the team has also
had to think through is what does it mean to stop
potential cascading faults and how do you isolate them by design? Nothing's perfect, but
there's a lot of thinking that had to go in in
terms of building systems that can survive. And so part of like
walking you through this is to help you understand what does it mean to actually operate and run these systems at scale? Now, there are some customers who'll come and tell us we want even lower management. And so all of this infrastructure and all of that knowledge
we built into MSK Serverless and there you're just operating
at the level of scaling up, scaling down, you're doing
zero Kafka management and normally we recommend
it for new to Kafka or new to streaming customers. I debated putting this slide up and I debated very, very deeply about like, it seems remedial and yet it's one of the more
common failures that we see with customers is monitoring Kafka. What I'll show you on the
next slide will seem obvious, but it's remarkable how
customers, like a lot of customers are not set up for
actually monitoring these. So these are the things
we recommend you monitor in your Kafka setup. So I'll start with the per
broker, per cluster things. It's partitions per broker,
total partitions per cluster, it's connections per broker,
monitor these, right? It's super important to make sure that these are within the bounds and in fact set alerting so
that you can react to this. And then on the usage side, think about your broker CPU usage, your disk usage, your memory usage, your throughput usage. It is amazing how these simple metrics will give you a view on what
it means for the service and the system to operate. Super important that you balance not just the operational
side of running the system, but also the monitoring and making sure that you're
doing the right thing. That is what it means
to run Kafka at scale. Up next, Sai will tell
you about what it means to run Flink at scale. - Well, thank you so much, Ashish. So now that you've got
all the data streamed in Apache Kafka, you need to process it and that is where running
Apache Flink at scale comes to fruition. So how many of you have
some of these use cases, anomaly detection where
you're transforming data before you're loading
that into an OLAP system? How many of you're supporting building event-driven applications? If you're using any of those use cases, or all those three use cases, then you should be using Apache Flink. There are four reasons
why. First, it's real time. Second, it's great at
handling dynamic datasets. Number three, it's stateful and
finally, it is programmable. Let's dive deeper into each
one of these using an example. Imagine you are building
a fleet monitoring system and your goal is to detect anomalies as quickly as you find them so that way you can improve
the customer experience. So I start with a few nodes and within no time, my fleet
grows and now I have tens and hundreds of nodes and
in no time, I have thousands of nodes to monitor and detect. What is equally important to remember is as your customers are
creating new resources, you have new nodes to monitor and when they're deleting resources, you no longer have to monitor those nodes. So this set of data that you're
monitoring changes rapidly. Somewhere along the line
you realize that, "Look, my anomaly detection can be better if I also include storage
monitoring into the mix." And then eventually
software versions, regions. So very quickly what you see is a big increase in
complexity of your data. This is where Flink's
continuous processing is a lot better than using
batch-based processing. A batch is like capturing a photo. A photo captures what's
true in the moment. You cannot track what happened before or potentially what has happened after. Comparatively a video captures
every frame, every detail. It gives you all the rich
context available for you. You can go pause that, go
back to a point in time, compare different things and get to the insight in
a more accurate fashion. We also talked about one of Flink's strength being it's stateful. So in our example, you're able
to capture the state per key, per server, per software type. And as new events come in, that state is incrementally
updated by Flink. And what it does, it waits
for patterns to emerge and either decides, "Well, this is noise, I'm gonna suppress it
or it's a valid signal, let me act on it." So in our example, it could
be a breach in threshold where you say, "Well, I wanna monitor if I
have more than five faults in any given minute and if
it breaches that threshold, I want to trigger an automated action, which is replacing that faulty
node before the customer is actually seeing impact." So being stateful gives you
that rich memory for you to make more context-aware decisions. The last piece is it's programmable. So in our example of fleet monitoring, you can start with a
simple if-then-else logic. If this happens, I'm gonna do this. But over time you realize, well, I wanna also monitor my storage so it can evolve your logic to now also include other metrics. You can also map the data to
a table in a database table so that you can actually
enrich that context. And finally, you can
start with simple actions. In my fleet monitoring
example, that customer started with creating an alarm
so that a human can react to that alarm and replace that node, but over time they grew confidence
in operating that system and started taking automated
action using that workflow. So this gives you that ability to constantly evolve your application. The combination of
real-time, statefulness, being able to handle dynamic datasets and programmability is also the reason why customers are turning to Flink to build agentic AI applications. So what does it take to do more data processing
workloads real time? When we talk to a wide
variety of customers, three particular patterns emerge. First, it requires a change
in your operating model. Second, you need resilient
Flink infrastructure and finally, build programming
logic that is robust. It sounds obvious but it's very important. Let's start with what do we mean by changing the operating model? And a good way to understand
that is to compare that with batch-based processing, something that has been
popular over the years. In the batch world, your
data is largely fixed. So you're processing data
that is either days old or a few hours old and the analyst is now running
different set of queries to find that insight. And then essentially
also leaning on a human to generally take an action. Compare that in a streaming system. Data is getting continuously generated. And then on this set of
continuous generating data, you're applying a set of
generally static rules to understand insights and
almost automate the action. So in our fleet example,
the automation there is replacing that faulty
node or storage device. Time is explicit in the dashboard. When you take a photo,
the snapshot tells you that this was taken at
this particular time. But when it comes to video, you have to specify that time explicitly. I wanna go to this particular timeframe and then compare things. So time is explicit in streaming systems. So that is what we mean by
changing operating model. You're moving away from
dynamic queries on static data to static queries largely on dynamic data. That also means that as developers, there are some new
concepts for you to learn. First is event time, which actually tells you when
the actual event has happened, not when it's processed. Sometimes as an example of
fleet monitoring system, you could get events related to storage before you get events related to server. If you end up using processing time, you would miss processing
events related to your server and that means your action
would not be accurate. So leaning on event time
becomes very important. The second key concept is Windows. Because you have this
continuous flow of data, Windows allows you to group this events into small buckets for analysis. The next important
concept is partitioning. That essentially is
how data is distributed so that you can parallelize
your processing. Now, because Flink is
trying to process data at really high throughput and low latency, partitioning becomes very important. Lastly, one of Flink's strong calling card is its support for
exactly once processing, which means that as a
developer, I get the confidence that I'm not worried about duplicates when it comes to processing. So I'm processing each event exactly once. So how does Apache Flink
support high throughput data at low latency with
remarkable consistency? The answer lies in its architecture. The job manager is like a
brain for the Flink system. It is planning, scheduling,
coordinating the work. And then you have task manager where the actual processing is happening and the task manager is further
broken down into task slots, which aids for parallel processing. So here's how it works. So you deploy, you build your logic, you deploy it as a JAR, and then job manager takes the code, first translate that into
a logical unit of work and then breaks that into
physical units of work and places those work in task slots. Why? Because it wants to
guarantee parallelism. Flink also captures the state, we've talked about how important that is, and periodically
checkpoints its processing into a durable store within S3. And the reason it's doing that
is to give you the guarantee of exactly one's processing, but also be resilience
when failures happens. So when a job fails, when
infrastructure fails, it needs to know where to start and how to start those
operators processing data again. So this combination of
orchestration with job manager, parallelism driven by task manager, as well as checkpoints give
you the right set of perimeters for you to run at scale. But as an administrator, what are all the activities
I'm responsible for to run these systems at scale? They largely fall into three categories. First is deployment, second is monitoring, and the last is scaling and evolution. So your developer comes to you, they wanna build an application. So starting point is you pick
an infrastructure provider, Kubernetes-based system. Then you have a choice to make, whether you wanna run
that in application mode where you have a dedicated
set of infrastructure for that job or you
wanna run in session mode where you can run multiple jobs on that same set of infrastructure. And for most at-scale applications, you choose the application mode. Then we're off to monitoring once you've deployed the infrastructure. And we'll dive deeper into this subject, but the core goal there is to make sure that you're always processing data. And finally, scaling the
system is super important. And we've talked about how programmability and evolution are so key
perimeters for Flink. And so your goal there is to
monitor when you need to scale, do the scaling event, also
support deploying new code. So that's what it looks
like as a life cycle of a Flink job and the
activities around it. Now, for developers running applications, this is a fairly involved process. So at AWS, we offer managed
service for Apache Flink that provides the
easiest way for customers to build resilient Flink applications. So the developer experience with our managed services
is far simpler compared to the deployment example
that I gave you before. So in here, there's no
infrastructure set up. You get built in multi-AZ resiliency and there is no configuration tuning. And here is how it works. You go to your favorite
IDE, build the application, get a JAR file out of it, create an application
within the managed service, and then you're off to the
races to start processing data. There's no computer managed, there's no configurations
for you to set up. Now you've got this thing up and running, now you have to operate it. And what I'm gonna do
next is kind of walk you through our learnings operating
Flink applications at scale and how you can potentially
benefit from it. And I'm gonna focus on
two specific learnings. The first one that we've
learned is in Flink, a significant change can lead to processing being interrupted. So what is a significant change? Could be you're trying
to scale the system. Could be you are trying
to handle a node failure or it could be you're doing patching and software upgrades. In each of this case, what
happens is Flink says, "Okay, well, I detect
a change in the system, let me pause everything,
let me reassign things, and then resume processing." So our first goal in operating
the system is making sure that we are minimizing
these processing delays. How do we do that? The key to do that is to
separate the time it takes to spin up EC2 instances and other prerequisites from
the overall job downtime. So you separate those things out, and we do that with two
specific techniques, which is one is blue-green deployments, the other is having a warm pool. With blue-green deployments, we do not stop the job until we set up and verify the prerequisites. Here is how it works. First, we spin up the
necessary EC2 instances. Next, we verify your job configuration, we'll make sure all the
prerequisites are met. And at that point is when
we are switching over from the old infrastructure
to the new infrastructure and resuming processing
from the exactly same point at which you stopped
processing previously. The next key concept is warm pools. So instead of waiting for
EC2 instances to spin up and the amount of time it takes, we maintain a warm pool of infrastructure, thereby we get an instance
that is ready to go. So the combination of
blue-green deployments and warm pools is how we reduce the time and how we reduce a job downtime when there's a change in the system. Another key aspect that we've talked about is how Flink allows you to
change and evolve your logic. So our fundamental goal is to how do we make
this whole process simple for our developers or for our developers? We wanna be repeatable, fail proof and quick so that they can
consistently make changes. So how does this work? Well, a developer decides that
you wanna go make changes, build a new JAR file with their code changes and they submit to the managed service. And what we detect that
there's a new deployment that is happening and we do
not stop the job right away. We take a snapshot of
the current running job, durably store that in S3 and then the managed
service sets up this new job with the configuration, sets up the new infrastructure,
including EC2 instances, make sure they're spinned
up and they're running. Sets up the job configuration,
validates the things and then restores the state from what it has stored within S3. So now your operators are
running with the preserved state and that is when you switch
over to the new infrastructure and you resume processing. We also pair this with smart guardrails. The goal there is to detect
any known code issues and thereby doesn't impact job processing. So the way this guardrails
work is as an example, imagine you upload a new code and it has some null pointer exceptions. It detects that this
code is having issues, it automatically reverses back
to the last known good state of this application and starts
to resume the processing. So a combination of automation and the orchestration of how we deploy new code,
blue-green deployments and smart guardrails is how we give developers the confidence to constantly evolve their applications in a highly resilient way. The second learning, the first learning that we talked about
is any change in Flink means there is a job downtime and how do we minimize it, right? The second key learning
we've had is a lot of times, developers and administrators in Flink are working with different abstractions. Developers are thinking
about core logical operators and then admins are
thinking about resources, its utilization, and they have
no visibility into the core. And same way, developers
have no visibility into the actual infrastructure. So we recognize there is a need for them to have a common mental model
and how to reason about Flink. And there are two key shared mental models that we recommend customers. First is fixed unit. The second is how do we
think about job availability and not just infrastructure availability? Let's talk about fixed units. Typically it's very hard or very unpredictable
to map the Flink code to the actual resources like
task managers and task slots. It's very unpredictable, hard, complex. And the reason is that is
different task managers can have different
performance characteristics and depending on how you've created slots, that can have different
performance characteristics. So you have a pretty unpredictable system. And the goal with fixed units is to bring predictability
into the system. So in our managed
service, the smallest unit of provisioning is a KPU,
which gives you a one vCPU, four gigabytes of memory
and 50 gigabytes of storage. So what it does is now you get deterministic
performance per parallelism. Each lane is also isolated. So the trouble with noisy
neighbors is no longer an issue. It also makes debugging easier. So when you have hot slots or issues, it's very easy to detect where exactly it is
happening as an administrator and resolve that very quickly. Lastly, it simplifies scaling. So if you want to add more capacity, you simply add more parallelism units. And then you also get
predictable state slices. So things like checkpointing and backpressure management
becomes a lot more consistent for application admins. So what does fixed units do? For developers, what it means
is your workflows are simple. Now you can design your
code so that they fit in a fixed budget. And then once you figure out what that deployment profile looks like, then you can scale that by
simply adding more KPUs. And for administrators, by
enforcing these guardrails, you are being more proactive
rather than being reactive when it comes to handling issues. So that is a role of the fixed units. The second common way that you want people to reason about Flink is to think about job availability rather than infrastructure availability. Now, job availability tracking
in Flink is very hard. Flink states whether the job is running, doesn't always mean that
data is getting processed. Why is that the case? There are three reasons
why that may happen. First is the boundaries between user code. Flink runtime and external
systems are not always clear. So debugging is very complex. Second is restarts and
recovery means a lot of times the underlying
root cause is masked. The second run, which starts
producing different errors, will mask the errors that were actually caused
by the original problem. That makes troubleshooting very hard. Finally, issues can happen that are external to the Flink runtime. Think about node failures,
storage failures. So it's important to track
them and address them. So what we recognize is we need
a smarter detection system, a system that can detect that
there's an issue, classify it and be very surgical about the
action it's trying to take. So what we built is a system that consistently monitors a Flink job, looks to classify whether
an issue is something that is related to user code
or is a system-driven one. A user-driven issue could look
like issues with your code, like a null pointer exception, things that have resource exhaustion that is created from the code base. A good example of that is you've opened too many connections, you've not closed them or it could be incorrect configurations that you picked for your job. All of these are in the category that are related to user code. And then you have system-related issues. And these could look like
node failures, Flink bugs or generally issues with connectors. The automatic healer
identifies error causes, classifies them, and then
the reason the classification is important is it can be very surgical about the fix it wants to do. As an example, if it detects that there are incorrect configurations, dynamically, it can change
those configurations and thereby restart becomes much faster. And the whole purpose of the system is to reduce the mean time
to recover from the failure. Let's dive deeper using a few examples. The first one is performance degradation. Imagine you have built an application for the fault system that
I talked about previously. It works great for 100 records per second, 100,000 records per second, but now suddenly you wanna scale that to 500,000 records per second. And those specific static configurations that you picked no longer
work for this increased scale and Flink gives you 400 plus
configurations to choose from and that makes the whole process harder. So what the detection
system does is it detects that there's an issue with
the incorrect configuration, fixes that dynamically and thereby recovers a job very quickly from the performance degradation. The second example is something that we see very typically
is with connectors. A good scenario for
this is Flink is looking to restart the job to
recover from another failure. And then what it realizes is that there is this process
related to this connector that is not responsive. So what the detector does is it detects that there's an issue with
this connector process, kills that process externally, thereby the job can restart very quickly. Here's an example once
again where the goal is to recover faster from an issue. Finally, failures can happen
outside the Flink job, which we've talked about. A good example is node failures. Failures do happen,
infrastructure does fail. And when it fails, we detect
that there's an issue. Pick a node from the warm pool
that I mentioned previously and then accelerate the recovery process very
quickly for customers. So again, three examples where having a detection
system, classifying it, being very surgical
with what we are fixing reduces the mean time to
recover from failures. Now, what we've also
recognized is availability is also the function of your code. Issues such as high CPU, out of memory, this throttling can also come in terms of how the code is structured. Let's understand this using an example. Imagine a customer says,
a developer says, "Look, I have this high CPU issue." And you start dive deeping
into that job graph. And what you realize is
that job has morphed itself into a wide variety of
subtasks, 1,600 plus subtasks, and they're trying to
fit that into 10 KPUs. Now, one way to solve the problem is to horizontally scale, add more KPUs. And you're almost like
throwing money at the problem. The other way to do that is to look at is the
code structured properly? A couple of ways to
think about that is one, is there excessive branching
happening in this code? Now, back to our fleet monitoring example, one way to branch is by alarm type. It's almost like I'm
executing the same logic and I want to execute
that for each alarm type. So I have 20 alarm types,
I have 20 branches. Another way to do it is
hey, is there something that is common across these 20 branches? And potentially you can
organize that by window sizes. You could have one-minute
windows, five-minute windows, and maybe three minute windows. So you can go from having 20
branches to three branches. So instead of throwing
infrastructure the problem, you are reorganizing the core so that way you have lesser subtasks and there you can fit into the 10 KPU that we've talked about. Another example is parallelism. Sometimes what you see is not
all task managers are busy. There are some that are
running extremely hot and there are some that are idle. And that means that you've
picked an operator parallelism that doesn't work well consistently across the entire pipeline. And that is a case where you
could work with a developer to make sure they care very specific about the operator
parallelism they're picking across different parts of the job. So these are a couple of examples where how your layout core can have an interesting side
effect on the infrastructure. So what it comes down to is you need another layer of defense to make sure you're detecting
these issues very quickly. Now, Flink gives you a raft of metrics and I'm not gonna spend time
walking through every metric, but what I wanted to share with you, a mental model around
what our customers use when they operate Flink at high scale. The first category is application health. And the goal here is not
just the actual uptime, but also more importantly
is the job making progress? Because at the end of the day, it's all about processing data. The second category is checkpoints. Checkpoints are Flink's safety
net to recover from failure. So you wanna have a robust
monitoring mechanism for these checkpointing data. So you're looking at
things like is the duration of checkpointing long? Are the sizes pretty high? So you wanna make sure
that system is very robust. The third important
monitoring area is latency. At the end of the day,
Flink is a real-time system and you wanna make sure you're always processing
the freshest data. And so one way to do that is
to compare your watermarks and see if they are slow or fast. A slow watermark means there
is lag getting built up, which means that eventually
you have stalled task managers. So the goal there is to
compare, as an example, your watermarks with your processing time to see how behind you are with the latest data
that is being processed. The fourth dimension is throughput, not just the aggregate throughput, that is easier to monitor, but also to monitor throughput to make sure there's
not enough backpressure being built into the system 'cause say as an example,
there's one part of the workflow that is getting backed up. Then what it means is that spreads across the entire pipeline. So goal of that is to monitor throughput at the operator level,
at the sub-task level, thereby you have the insights on where exactly within the pipeline you're having those
backpressure challenges. So those are the four different categories on how you can build a
robust monitoring mechanism for your Flink applications. You also wanna understand what are some of the best practices that we can share with the development needs? One of the successful patterns we've seen with customers is where
they've democratized this on how to build Flink applications
into their enterprise. So what is a good core and
behaviors and when it doesn't and what does the anti-patterns
look like on infrastructure? The first area is timers and watermarks. Now, we've talked about how
event time is super critical and so when you don't use event time, you end up using processing time. The typical complaint you see is, "Well, my aggregations are off." Well, that tells you that
somewhere in the code people are using processing
time versus event time. Another scenario with timers
is your watermarks are slow. So if your watermarks are slow, this means there's too much lag. What if they're too fast? Well, if they're too fast,
you're not waiting long enough for data that is trickling in slowly. So you need to find the right balance between fast and being too slow. The second area is state hygiene. And again, state is such
a crucial aspect of Flink, but you don't wanna keep
everything in that state for all the time. What you want is to enforce TTLs, thereby your evicting state,
as and when it's necessary. So getting your state management is super critical in your code. The third big area is avoiding data skew. One of the calling cards
of Flink is how you're able to partition the data, process each of that chunk independently. And you do that by using keyBy operators. Now, what type of operators, what type of data patterns you wanna use? You certainly wanna avoid
low cardinality analytic keys because what happens with
low cardinality cases, you have some task managers
that are running hot and some task managers that
are running inefficiently. So you wanna pick a high
cardinality each time. Also, you wanna reduce the
number of shuffles you do. Shuffles are critical because
you wanna shuffle data because you wanna get data based on one particular key,
process that data differently. So you would end up using shuffles, but using too many means data
is getting shuffled too much. That also impacts how much serialized time is spent on serialization. And that leads to CPU being busy, garbage collection being slow
and things of that nature. Lastly, serialization and
schemas play a very pivotal role. Not all use cases would benefit from the default serialization. And when you end up using
the default serialization, especially for CPU-intense workloads by doing transformations and complex transformations, that ends up again being
an infrastructure issue. Schemas also play a very important role. Instead of getting all the data, then validating it for the quality, schemas allow you to enforce
that on the producer side so that the Flink consuming
code is confident that the data that it's getting is
actually qualitative enough. In summary, writing the optimal Flink code will make sure the applicants are fast, resilient and reliable. So that brings us to how and what it takes for us
to run Kafka at scale. Now, if you want all these capabilities without the overhead, we
offer our managed services. So I wanna bring Ashish. Ashish.
- Yep. - We've talked about what
it takes to run Kafka and Flink at scale. What are some of the top
key takeaways from this? - Yeah, I think it's a
really pertinent point. One of our motivations
in doing this session was actually sharing our experience. And a lot of the discussions, I know Sai does as well and I do, are about customers who know Kafka but at the same time,
the effects of scale, when they encounter running at scale or when they encounter failures
at scale are different. And one of our learnings
from that was oftentimes, the only place that you
actually learn about failures and how you handle them
is when failures happen. And that's probably the worst time to actually learn those failures. And so what we've tried
to do is explain some of our thinking in terms
of our best practices, but also explain how we are
building the system ground up to make sure that these
things are accounted for. You saw this on the Kafka end as we transition from standard
to serverless to Express, and you're seeing this on the Flink end on how we are applying that. Part of why we are sharing this is as you are making your choices about running your infrastructure, are able to make a decision on which of these to apply, how you'll apply it and how you'll run it. The last sort of big takeaway from me and definitely looking
for learning from you on the Flink side as well, is too often, customers are running infrastructure but actually not monitoring the things that can cause the failures. And so what happens is
oftentimes when failures happen or the SOPs are not functional, then what happens is you discover that your system is not running
as stably as you thought. And a part of this is that there is a shared
responsibility boundary in terms of managing the infrastructure, which we will do and we will own. And equally importantly,
managing the operational side of Kafka or Flink, which
then you and us as customers have to have to
participate and partner on. And that, Sai, is my key takeaway. Partly what I'm hoping here
is that we can help customers as they're thinking about their
choices, run better systems. Anything on the Flink side
that you'd like to add? - It's very similar to
what we've spoken on Kafka. I think the three things are like knowing your shared boundaries. Now, with Flink, the
shared boundary also means you're running code, arbitrary code. So that has a interesting
effects that we talked about. Second is picking the
right offering, right? And sometimes you can learn
from our best practice, our learnings that we
built into our products and build infrastructure on your own or use some of our services. So I think it's very similar to our learnings on Kafka side as well. Awesome. Well, that brings to
the end of the presentation. Now you can try it for yourself, both MSK Express brokers, as well as deploy your Flink applications or managed service for Apache Flink because at the end of the day, seeing and trying is believing. - [Ashish] With that, thank you so much.
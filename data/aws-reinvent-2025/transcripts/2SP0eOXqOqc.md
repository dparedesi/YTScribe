---
video_id: 2SP0eOXqOqc
video_url: https://www.youtube.com/watch?v=2SP0eOXqOqc
is_generated: False
is_translatable: True
---

- My name is Amit Kinha. I'm the field CTO at DoiT, where we specialize in
helping cloud ops and FinOps with many of our customers getting the true value of the cloud out. Previously joining DoiT, I was a director of
cloud FinOps at Citibank, where for a number of years, I led our practice around cloud FinOps. And when you think about FinOps, oftentimes if you ask, say,
four people in the room today, you might get eight
different answers, right? You might get answers around, well, we help with optimization, we help with things like the savings plans at the end of the day, we might also be doing
some sort of ETL things, and we might be building
a lot of reports, right? And a lot of dashboards. And while all of that was true, the thing that I found I
was doing the most often which moved the needle was really around building confidence in the cloud. When a managing director would see a bill they didn't really understand, and they're panicking about it, sitting down with them and
helping them understand that, yeah, the bill went up $500,000 for their product in the last month, but that's not really a negative thing because look at the revenue
that they got out of it. Or cloud is elastic, and
so budgets are really hard, but that's not a negative thing either because that means we're really paying for the things we're using. And what I found was
oftentimes this confidence I'm describing is what
FinOps was really about. It was not about the ETL
pipelines that I'd be fixing or looking at our payer accounts and trying to organize
tags forever and ever. We're really around how do we get people to get confidence that the stuff that they're actually doing
in the cloud is A, efficient, B, that the value they're
getting back is really immediate, and finally, getting the
data to the right people at the right time. Oftentimes reports that we would generate would either go static or oftentimes it felt
like a very ad hoc thing. Someone would come to my team to ask about what can we do about FinOps? I see my bill is creeping up every month, and I'm not really sure whether it's a good or bad thing there. So what I coined the
term here is FinOps 3.0, where we get to a place where we're no longer just
looking at dashboards, we're no longer just looking at tagging or anomalies without context, but we're in a place where
it's a cohesive whole. So talk about 3.0, I guess
we should take a step back and well, what the hell is
3.0 in the first place, right? And I think about it this way, 1.0 was all about visibility. And this is where we
started thinking about, we have many different accounts on AWS. We might have some other cloud vendors. And what we really wanna be
able to understand is the what. What is the money going towards, right? You come from an on-premise background where everything is pretty
much taken care of, right? You have a CapEx spent for five years. Engineers will request some amount of CPU and memory for their
Kubernetes nodes, their VMs. And that was all there was to it. And 1.0 was about, well, how
can we now aggregate this data across four different
accounts for one team? Or how do we now look at
something that happened without the bill at the
end of the month, right? So we had a lot of dashboards,
we had a lot of reports. And 2.0 to me was, the next
question would be asked is like, okay, I can see my bill, but now what do we do about it? Can we optimize? Can we now get alerts faster? Can we have budgets that
are actually reasonable and not go out of style
or out of date every month when we launch a new product? And 2.0 had a lot of really
good, interesting things there around optimization, especially. We started thinking about
things like Kubernetes. Can we optimize at the workload level? Can we think about networks? Can we think about intelligent
tiering on S3, for example? But oftentimes in 2.0, what I
found was that even at Citi, we would see a list of recommendations that were say, 17 pages long. And oftentimes I'd go to the
engineering team and say, well, you should do these three things. And they would either reply with, well, we can't prioritize this, we're trying to build a business. Or this thing actually
doesn't apply to us. Around anomaly detection, we
would get an alert that says, hey, you spent $1,000 more than yesterday. An engineer would just
right-click in Outlook, make a new folder they would
never look at afterward because they realize, well,
this is not a negative thing, we just launched a production. So oftentimes we're
lacking a lot of context. And the lack of context
really makes it that we're looking at one part of the whole, which is the cloud cost, and
not necessarily architecture, the business outcomes we care about, or anything that actually
moves the needle there. So 3.0 for me is all about confidence. We go away from this place where, you talk to FinOps, to any CXO, and they think about the invoice
that they get every month and the bill that keeps
creeping up and up and up. And the engineers think about, well, I guess I'm supposed to care
not only about security, resiliency, availability,
but now my manager really wants me to care about cost, great. And we get into a place where the tools that they're getting and the data they're getting
is not only full of context, but it's actually meaningful, right? Especially when it comes
towards optimizations, when it comes towards guardrails, when it comes towards data
that's relevant there. So within 3.0, there's three key pillars
that I think about. There's data, there's efficiency, and then there's governance. And data is probably
the place where we have done the most amount of work, right? We now have reports, we got, like I said, a lot of dashboards. Some people are doing
economics really well, some are still struggling with that. And we have efficiency, we have some level of
optimization insights. And governance, we have
a little bit, right? We get anomaly alerts once in a while. But to be able to
transform in the age of AI where even if you
thought cloud was before, was a little bit chaotic
compared to on-prem, with AI, especially
energetic AI on the rise and any sort of chatbots or any gen AI workloads you're doing it becomes critical to
move forward in FinOps where instead of being in a place where it's very reactionary, right? The milk is spilt,
let's take a look at it. Let's try to solve it
and all the engineers are focused on optimization
for say a week or a month. And then eventually it
starts creeping back up again until someone freaks out about it. Instead of fixing it that way, I think we have to move forward in a place where the context is loaded in the heart of all three of these pillars. So what I'll do now is double
click into each of these and explain what I mean. So on the data side, I think we have the most amount of work done
already in FinOps, right? From 1.0 to 2.0, we've got, we already have level of economics, we already have some sort of anomalies, we already have reports we can get. But the problem still is there where if someone wants data, right? Say your CEO wants to now
negotiate the new PPA deal. They will still go to the CTO
who goes to the IT director who goes to the FinOps head and who eventually goes
to the FinOps engineer who will extract some
data, put into Excel, put into a PowerPoint,
goes back up the stack, and the CEO may ask, "Well,
what about this gen AI thing? "Can we load that in?" This whole game of telephone repeats itself again and again. The other thing that
we have today is that, sure, you can see the cost in
very granular fashion, right? Even at Kubernetes level, we solved it because now we can say, "Well,
we can allocate the cost "by namespace, for example, as a proxy." We have tagging strategies that
are pretty well thought out and we can bifurcate
costs that's, you know, say egress or data transfer by doing things like cost follow cost. What we're still missing
to me is this key concept which is contextualizing the data, right? Instead of just thinking about data from a perspective of the cost itself, what we're still missing is the context around the business outcome
we really cared about. It might be that when you launch a new product to production of course the cost is
going to go up, right? But without having the
context and knowing up front, you're still gonna get an anomaly that is irrelevant to you. Or it might be that, you know, we're getting a lot of
different data reports. However, what are we
actually doing with them is still happening outside, right? A product person may get a data set that says the unit price for, you know, daily active users is this much, but they still have to then think about, "Well, how do I now use this
data in my decision tree "to think about, well, how
do I price my B2B app better? "How do I think about margin production?" And if you're on the, you
know, in an FSI, for example, you're thinking about revenue
for the quant libraries that you're running every
day for risk analysis, but not knowing what are you actually getting back in return, either
the number of calculations or whether this upgrade that we did that was, you know, benign and a refactor is actually causing our
things to spike a lot more. If you don't do these things properly, it still becomes one of
those things that, you know, cost data is still seen as a number that we always have to tamp down, rather than thinking about
it from a perspective of, "Well, the cost is going up, "but look at how much more
we're getting back in return." So for me, there's really
three keys of focus here. The first one is around what matters most for performance and value, or rather, for connecting the cloud spend
towards business outcomes. And we had started this in FinOps 2.0 when we started thinking
about, say, uneconomics, right? But we still are very short
of where we need to be, which is, what are we getting
back in return, right? Instead of thinking about
Gen AI, for example, you open up a chatbot internally, and it just connects
to, say, some MCP server that does, you know, vacation days. And what you don't realize
upfront is that every engineer or everyone in your company
is going to love this chatbot. And whatever you had thought about before of daily active users
or the number of tokens you'd be using, it kind
of goes out the window when it's so variable there. Rather than relying on only on, say, a cloud cost being this absolute number that should go up and down every month, we really have to start thinking about, well, what are we getting
back in return there, right? Maybe the cost has to go up because this new product
that we're launching is very expensive, but the ROI on it might not even be revenue. It might be that our daily active users is increasing tenfold, and
then we can serve them ads. The second place I
think cloud cost, right, visibility needs to improve, would be around the
way we explain the why. So today we do a really good
job of explaining the what. We can take a million dollars
a month cloud cost from AWS, we can bifurcate it
between every product team, we can even go between
environments to say, sandbox costs this much,
non-prod is that much, and production is blah. But we still can't answer the why did the cost go up, right? At the end of the day,
the cloud cost to me is just another point
in your decision tree when you're making better decisions. It might be that you wanna
do optimizations today because you realize that every time we're doing a PR on Terraform, the cloud unit price for
our million API calls is increasing tenfold. There has to be something
else we can do there. 'Cause if you don't do that,
especially with Gen AI, and if you don't do it now, it's gonna get very difficult
where all of a sudden, every time you use a different model, or you have a context
that's being changed, or the embeddings itself is
not being utilized properly, this variable cloud
cost that we have today is only gonna increase in variability, and it's just gonna cause
a lot of heartburn, right? Every single person will just think, this number, it will never go down until someone freaks out about it, and then we have to have this whole two, three week cycle where
we put all our heads down, figure out the unattached EBS volumes, or hey, this bucket
that's just holding logs should not even be in standards,
should be in whatever. But instead, we get into
this continuous cycle where we're getting the data when we need. And the last part for me would be around delivering the right
data to the right person at the right time. So oftentimes I feel like,
as a former engineer, still engineer a little bit, I find this trope in FinOps that engineers don't
care about cloud cost. And to me, it's always been really funny. It's not that we don't care about it, it's more that if you think
about every single other metric that we quote unquote care about, be it throughput, performance,
reliability, availability, we have the tools to help us get there, and it's quantifiable. You can tell when you have
100 transactions a second, you can tell when you can support 100 active daily users, or a million, and you can tell when security itself is, it's embedded in the
lifecycle of development. But with cloud cost, we still
look at it as something that we're supposed to care about, and yet we don't really
offer the proper tooling. We don't tell engineers that, hey, this simple web server that you're running could run on Lambda, it
could run on ECS, EKS, Fargate, whatever, and
yet here's a trade-off between all three of them. It's one of those things that,
if you don't do it properly, it just becomes a thing that
you always do afterward, and by then, sometimes
it's either too late, or it just causes burnout,
where an engineer says, yeah, I'd love to care
about cloud cost, too, but can you give me the right tooling that isn't just a report that says I'm spending too much money? If you don't go beyond that,
it's gonna get very difficult to kind of give the
engineers the right tooling in the lifecycle that
they actually have to say, well, what is the scenario
that you're describing of this Gen AI product that you wanna launch, which everyone is super excited about? If you use this model
based on the test data, it's gonna cost this much every
single time person hits it, and based on historical evidence, in our production environment, this is the number of
users we're expecting. If you use this other
model, it might be cheaper, or it might be more expensive, but this is the value you
get back in return there. And so being able to do these
three things really well, being able to connect to an actual outcome from the business and not necessarily on just a raw number that you're trying to raise or lower, being able to explain the why, and not necessarily just the what, and then finally being able
to deliver the right insights, I think can really be powered
by Gen AI now as well. Imagine a world where, in my CEO example, instead of him or her
going towards the CTO, to the director, to the
FinOps, to the FinOps engineer, they can just ask in English, where is most of my spend going? When I renew my PPA, what are the SKUs I should try to actually get a discount on? Or for an engineer, a
what-if analysis that, sure, we wanna launch and
migrate from VMs to containers, what is the cost going to be if I just did a lift and shift? What if I actually just use Fargate? Or what if I wanted to do EKS itself? And what would that look like there? The second pillar for
me is around efficiency. And I think this is where
we've spent a lot of time in the last five or six years in FinOps. It's all about optimization. And traditionally, the
FinOps optimization story goes something along what
I call the FinOops moment, where the bill is running
and all of a sudden, you see a giant spike that's unexplained and everyone freaks out about it. And we start looking and we start, it's almost like a duck hunt, where you find a million dollars here, we find $20,000 there. And a lot of these
tools that are out there will help you with this. They'll be able to analyze your cost and be able to tell you, "Hey, you should consolidate
your VPC endpoints. "You should look at lowering
the utilization on your VM, "or rather, fixing the VM size "so you can match the utilization." But what I find often, though, is a lot of these optimization
recommendations fall short because they don't
understand your architecture. It might be that the VPC
endpoint consolidation, when you go to the team
that's doing networking, might say, "Well, the way
we deployed our network "in every single account,
it'll take nine months to do, "to save 1%." We don't really fully understand the cost of actually doing some of these actions in a way that actually gives
confidence to the teams that are supposed to
be taking these actions in a way that they'll actually apply them. It might be that the recommendation says, "Switch to ARM processors,
it's way cheaper," but your quant libraries only run on x86. So you can look at it,
you can feel bad about it, you can ignore it, but oftentimes, as soon as you start
ignoring these things, you start losing value and realizing, "Well, the analysis is not really done. "The report card that I get from FinOps "says I have a C-minus on my team, "and my product head is
really upset about it, "but I can't really do any
of these things anyway." So being able to focus
on the what matters most for performance and value, and understanding the context
of what's actually happening in your architecture
becomes really important. It might be that when you start
looking at models in GenAI, and you say, "Well, why
are we using SONET 4.5? "We don't need to use this. "We should be using a quantized version "because that's what this
recommendation says." And you realize, "Well, the thing "that we're actually using
it for requires this model." Or if every engineer starts loading their full context window
because it's two million, it's amazing, and the
answers you're getting back are now running up the bill, instead of looking at that and saying, "Well, shorten the context window," if you don't understand, well, you don't have an embeddings model in the middle of it, and 85% of your stuff is the
most generic MCP answers, it's really difficult
to now have engineers start to think about these things in a way that moves the needle. Being able to prioritize these decisions in a way that isn't left to someone to look at these 17 pages of
optimizations and figure out, yeah, I guess I will do this one, it'll go in the backlog of a team until someone freaks out about it, and instead, being able to
now meet them where they are. When someone is doing
an actual architecture and they're doing performance
testing and non-prod, being able to have the cost
data right there that says, yes, you got your performance
that you really cared about, but at what cost? And there's two different alternatives that you could actually
do for similar performance for a fraction of the cost. Or conversely, when you
see an optimization, instead of thinking about
only the actual thing that you have to do, be it Terraform, CloudFormation, whatever, but really understanding
your full architecture that the way you've set up your accounts, the way you have set up your organization, it's gonna be very difficult
to do this in a timely manner, and you'll have to do a lot more testing in order to actually do this. That's what's missing today. And finally, I think on
the optimization side, I know Joe's here from FinOps. We always talk about shift left, right? Everything should be shifting left. All the engineers should be the ones who think about these things, and product teams should
think about cloud cost as a first and foremost, but I think sometimes there's
a lot of different examples where shift left doesn't really apply, and we should be able to
automate these things. An example of that is
in Kubernetes, right? Each workload, you went from a VM that was, say, 20 gigs with four vCPUs, and you go to containers, and your engineers will say, "Well, I need 20 gigs and four vCPUs too. "That made sense before." And you get this
utilization number that says you're using 10% of
your node in Kubernetes. And all of a sudden, you now have engineers
trying to figure out, "Well, I guess I need 10 gigs. "I think I need 3.2 CPUs." And you do this entire performance test to figure out, and you isolate the cost. But then as soon as you
pull out another PR, or you start making more
calls to the database, or there's a refactor that was benign, the number might go way down or way up. And so oftentimes, I feel like, especially in Kubernetes, it doesn't make sense to have engineers always be shifting left and
worrying about these things. We should be able to automate them. We shouldn't necessarily have to have every single engineer
care about these things to the level where they feel obligated to now not only do security, not only do observability, reliability, on and on and on, and then also think, "Well, what are these dials
should be set to exactly "to get performance at the cost as well?" We should be able to automate these things when they happen. On the governance side, I think this is where GenAI
will be really helpful and will be really needed. Governance up till now has been around, specifically cost governance, it's really been around
anomaly detections. When the cost exceeds a number or a budget is breached by a certain
amount, alert somebody. That's pretty much what we do today. And I find that really challenging because oftentimes when you
look at that in isolation, you get the alert, it fires off, it might go to PagerDuty,
it might go to the SRE team, maybe the engineers, maybe
it opens a backlog ticket in your Jira board that says, "Fix this." And when you go to take a look at it, there's a lot of legwork to be done. You have to understand, "Well, why did this actually happen? "Was this a good thing?" Maybe you spend 24 hours
looking at an anomaly and realize, "Well, we were
in the front of a tech crunch, "and this is not a bad thing at all. "The cost should be going up "because we're scaling automatically." Maybe you had a great
quarter and all of a sudden you're doing a lot of quant calculations because you're making a lot of revenue. Well, of course the cost is gonna go up, but without that context
of why it's happening is really difficult, and
oftentimes what I've found is that engineers will get this alert, might be product or might be whoever, and as soon as they see,
"Well, this was a false alarm," even if the limits are set
to say reasonable numbers, like only if the cost goes
up $100,000, alert me. If it was a good thing
and not a bad thing, you're gonna start ignoring it. And oftentimes when you
start ignoring these things is when the real problems arise because you kinda ignore the
actual issue when it happens because every single
time you've taken a look, it just feels like it's
another thing to ignore. So being able to fix these things, to me, comes down to this. It's very similar to security in a way. You wanna prevent the
bad things from happening first and foremost. In FinOps, it might be
that you wanna prevent in your ephemeral environments anything but spot instances. It might be that the Gen
AI team is the only one that should use the P5
clusters in Kubernetes 'cause it's $95 an hour or whatever, and you don't want anyone
else to touch them. Or it might be on and on,
all these different rules that you wanna set in place that are, at the same time, not too restrictive where you're blocking
innovation in your teams, but also not so brittle
that every single time you set a policy in place,
an engineer comes to you and everything's an
exception all the time. Eventually, if you start doing that, the teams will basically
just raise an exception for everything they wanna do, and this entire prevention
system that we've built kinda goes out the window. The second step is, if
you find you can prevent a lot of these things from happening, they'll still happen. There'll still be rules that were slipped or someone went in console
in your non-prod environment, did one small thing
that now raised the bar, or raised the price, rather. And when those things happen, you wanna detect them as soon as possible. And you wanna detect them not at the level of just only cost, which we're used to, but you wanna detect the
underlying reason for it. It might be that the thing
that someone was trying, they forgot to quote-unquote
shut off the lights. It was a experiment they
were running on inference or training a model, and afterward, they forgot to right-size
the cluster right after. It might be they're
doing performance testing and 24 hours later, the
performance test is done, but six months later, as you discover, this cluster's still running there. Or as a personal example,
once I had a call from AWS partners where they said, "This account that runs only $400 a month "is up to $180,000 in 24 hours." And we started looking, and we're like, "Oh God, what happened?" The oops moment. And it turns out someone was trying to do exponential back-off on queues, and they were using serverless, Lambdas, and so it should be really cheap, except they didn't really implement the exponential part properly. So we're retrying the same failed message 600 times a second for 24 hours. And all of a sudden, you realize, "Well, why did we not know
about this immediately? "Why did we have to wait
until either getting a call "or an anomaly seven or eight hours later? "And oftentimes, when
you get this anomaly, "why was it not told me immediately "what was the cause of it?" And today, we get the cause
in terms of this service is the one that's spending a lot of money, but what we don't get is a context of this PR that was raised that was being done by this team, and this is what the
code snippet was doing. This change is causing
this to happen, right? So being able to fully embed the context of what we're describing here, I think we'll do two things. One, we'll get away
from this idea of wolf, the boy who cried wolf all the time, of random anomaly alerts that you ignore, budgets that are out of date. So you say, "No, it's fine. "We had a meeting last month
that we updated the budget, "but we forgot to tell
the FinOps team about it." But instead, you get into a place where, especially with AI agents, where you can actually look at an anomaly, and by the time it hits your desk, you're getting the full
context of why it happened, what's happening, and then
finally, how to remediate it. And today, remediation
is one of those things that we don't really offer, right? We say, "Hey, there's an issue. "Go take a look at it, figure it out." And oftentimes, there's
a lot of time spent trying to figure this out, right? Either be it, is it a code change? Was it that we had a lot more volume, and it was a good thing,
like I said earlier? Was it something else
causing this entirely? Could it have been that
the savings plan ran out, and so now the cost is spiking, and that is a reason for it, and not that EC2 is all
of a sudden 40% higher than it was last month, right? So being able to now
remediate it in a way that, in fact, why even stop there? Instead of just showing you what it is that you should fix, oftentimes,
I feel like in security, we would be able to patch
something immediately. We give access to a lot
of our security tools that if they detect a
vulnerability, fix it on the spot. And now, in my mind, FinOps
is one of those things that doesn't have to be all the way there, but it can be a lot closer to it. For example, in remediation, when you have a issue that happens, and it was caused by a
code change in Terraform or in application logic, why can't we just raise
the PR automatically? And we still rely on the engineer to actually approve the PR,
test it, and then merge it in, but at least get them all the way there, or at least give them the logging from CloudWatch and CloudTrail,
VPC flow logs, maybe, of this is the cause,
this is what we think, and we did research for you already. And maybe in some environments, like, say, your non-prod or
experimental environment, why don't we fix these
things automatically? The example I used earlier
of shutting down the lights. Experiment is over, the model looks great, we're gonna go to production with it. We don't need to rely on every engineer to remember to now spin down that instance or in the performance environment. We should be able to do it automatically within rules that actually make sense. And the way we make these rules, right, of the prevention, the
detection, and the remediation should follow a security model as well. Instead of having very brittle policies that always are out of date,
which are full of exceptions, which aren't catching
the new things anyway, we should be in a place where they're all continuously learning as well. We should be in a place where an engine or a centralized FinOps team can put very basic
rules in place initially for some environments, and
the higher environments really lock them down to prevent these things from occurring. And then when there's an exception, automatically apply it in a way that isn't an exception anymore, but now becomes a standard there. Now, assuming that what
I just described to you of between the data side,
between the governance side and efficiency side, let's
take an example here. So assume that you run a B2B SaaS company, you come to re:Invent, and it takes off. Everyone comes to your
booth, they love it, and they start using it properly. Everyone's signing up
for it, it's amazing. Tomorrow morning, you'll get a bill that says your bill is up 1,000%. Now, in FinOps 2.0 and
1.0, what would happen is someone would get this
bill in your company, absolutely freak out about it, and now start going down the rabbit hole of what's causing this. They would see some
things that are spiking, there's some resiliency
issues that are happening, some things are scaling horizontally in a way they didn't
intend, on and on and on, and eventually, maybe the
product team would chime in and say, oh no, that's expected. We look at the amount
of daily users we have. Eventually, the CTO or CFO
would also get involved because the bill is so much
higher than they expected. The procurement team
might freak out about it because the PPA was for a lot less than what they had intended. They could have gotten a bigger discount. In FinOps 3.0, the response would be an agent that's running sees the spike, understands that re:Invent's happening, sees all these traffic coming
in from new user signups, and people are actually
trying the application out immediately, and then understand, well, the unit price per daily active user is actually going down. We're actually scaling
really, really efficiently, and this baseline cost that we had, this is a really good thing. So there should not be an alert fired. In fact, maybe there's
a report that's sent out that says, hey, this is
something that has now occurred, but this is the context of it. The CEO gets it, the product team gets it. Maybe the engineering team gets a report that shows them, at
scale, these two services are the ones you should try to optimize, and here's a PR that actually
helps you optimize them. So when you start scaling horizontally, it isn't this giant spike going forward. Maybe there's an architectural review that you can do on the
fly to change things. Try it out in non-prod with the volume that you're looking at, and then apply it within a couple of hours. And the outcome really would be here that instead of always
thinking about the what and this feeling of the
number is always going up, the cloud cost is too high. We're freaking out about it. You should be in a place where cloud cost is in context of all these
other things you care about. So regardless of whether
it goes up or down, you understand the context of it, which gives a lot of
confidence in being able to not only save money,
but also spend more money. The confidence to actually
get out of this POC for all these good ideas you have of using Gen AI workloads,
actually start moving them to production, 'cause
you're no longer worried about the fact that,
well, last time we did a Gen AI project, we launched it. It was a million dollars
more than we intended. So let's slow down on it. Instead, you have
confidence that the build that you're expecting and the
data that you're looking at is full of context of what
you're getting back in return. You have the anomaly set up in a way that you're only getting the
things that are actual issues, like my serverless Lambda moment. And you'll also be able
to build policies in place that are not so brittle that
the team is spending time just doing this nonstop. Instead, they're self-healing in a way. And to do everything I'm describing, it's only really possible
today in my mind with Gen AI. Being able to connect the
cost data, your business data, performance data all
together in this Venn diagram where you fully understand
what is actually happening, before it would take a lot of effort. It'd probably be in Excel. You'd probably be trying to combine different data sets together
and be very time in place. You might do this once
a quarter, once a year, or whenever the CEO
freaks out about the cost. And instead, you should be
able to do this continuously. You should be able to look at your data in the fully loaded context I'm describing in near real time. You should be able to
understand that the cost data that's spiking is a
good thing, like I said. The other side is automating
the analysis, right? So on the optimization side, instead of just only
looking at in isolation, we should do this, which
will result in lower cost, we should be able to understand, well, the cost of doing that
would require a full rewrite and a replatforming of
our entire application. That's gonna take 10 months. We don't have to wait that long. Can we do something today? Sure, that thing may
save 9% year over year, but at what cost? Will the engineering teams
drop everything they're doing to focus on this one
thing versus something that could be a very minor change today that can start saving
you money immediately? And finally, being able
to learn from this context in a way that you can
actually guide the prevention, the detection, the
remediation automatically to help shift not so much left anymore, but back to the center where
it actually makes sense. Instead of having
engineers being overloaded to say now also worry about
the myriad of different things that you have to do in cloud, we can actually help them
and give them the right data so they can make better decisions. We should be able to have
our CEOs ask the question, not in an email chain that
goes nine messages deep before it hits a person
who's doing the work, but maybe they can just ask in English and your AI agent can
run in the background, getting the relevant data,
doing the what-if analysis, and giving the answer
that they actually need in the right moment there. So yeah, in summary, I think
this continuous learning that we're describing of
FinOps going from the static once-in-a-time thing that we try to do, we get the flywheel effect going instead. We start thinking about cloud costs as a key point in a decision tree when we're making architectural decisions, business decisions, and product decisions rather than something to look at that has to always be
lowered or freak out about because the number's too high. We should be able to have
this done autonomously in a way that we're not
asking our engineers to spend so much time analyzing this data that we have to build a
FinOps team to be 10 analysts who are just continuously serving us almost like an internal
consultancy of sorts. Engineers come to your team, the bill is too high,
help me figure it out, and we do this process again and again. Instead, we meet them where they are. We connect with them, maybe
in their CI/CD pipeline. Maybe we give them the right tooling for the centralized team
to build these guardrails and policies in place
that don't require you to have a mathematics degree
to build out policies. Maybe we are finally moving from a place where we have these anomalies
that are lacking context and go into the dustbin, so to speak, but instead are full of information and actually help you because
the only time they're raised is when there's an actual issue there. And then finally, going
from this cost data in isolation towards this connected data and being able to use that
to make better decisions is finally where we
can get to with Gen AI. So for me, going back to my city example, it was never about cutting cost. It was always about giving the confidence to spend more money because I feel like the true value of cloud
is that you're getting just the right amount of
compute, storage, databases, whatever, when you actually need it and not this thing that where every time you deploy something and
you take a look at it, you're finding all these random issues because every time you find these issues of either unattached
EBS volumes or whatever, you start to lose a
little bit of confidence. You start to get into a place where there's a little bit of hesitation before we open up the floodgates for this beautiful Gen
AI thing that you built and yet you don't understand why someone's not signing off on it. You get into a place
where you have confidence that not only are we gonna launch this, we have confidence that if
there's something that happens, we'll be able to find
out about it immediately and we might be able to
fix it within an hour, within two hours or something. With that, I'll open up the
floor for any questions. Thank you.
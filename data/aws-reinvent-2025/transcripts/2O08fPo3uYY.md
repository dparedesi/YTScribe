---
video_id: 2O08fPo3uYY
video_url: https://www.youtube.com/watch?v=2O08fPo3uYY
is_generated: False
is_translatable: True
---

- All right, welcome everybody. So today we're going to talk a little bit about troubleshooting database performance and issues at scale. But before we do this,
kind of picture this, tell me if this sounds familiar,
I'll ask for some hands. You know, sometimes when you're managing
a large fleet of databases, it could be very hard
to identify, you know, where the issue is or if
it's even the database. You know, do teams ever
reach out to you saying like, "Hey, our retail service is slow. We think it might be due to this, or our ordering service is slow. We've looked at the front end,
we think it's the database, you know, you need to look at it." Or "We're not sure what the issue is." Does anyone ever run
into things like that? I mean, I know I have for like the past 20
something years, right? And so today, me, Joe Alioto, I am a senior solutions architect that focuses on cloud operations, things like observability and monitoring, governance compliance,
centralized operations management from like compute to database. I deal with a lot of stuff. So what we're going to talk about today is we're going to go into
some customer challenges, like some common things we see kind of related to what
I talked about today. We'll look at some fleet
wide observability, look at how we can do some
end-to-end transaction analysis with application performance
monitoring baked in, and then just a common
troubleshooting workflow. Additionally, this will
be online on YouTube in the next 48 hours as well, so this is recorded so you will
be able to view this again. Alright, so but before we do, let me introduce you to Alex. Alex is an SRE lead at Ocktank and he's experienced with supporting, let's say like everything. He just supports operations,
what it needs, right? He's the superhero that
actually fixes things. That's a little unsung in
the organization, right? Alex is going to be our champion today. So what Alex commonly runs into is like managing a wide
variety of databases. Alex works with customers that have, or like his customers in the office, have different databases
from like Postgres to MySQL to MS SQL, like Microsoft SQL and around. They have multiple different
databases from different teams, and you know, he has
to manage that as well. Having a lack of application context has been a problem previously, right? So they say, "Hey, we think
there's something wrong with the retail application." Like we looked at the
application, it's fine. There's nothing wrong. I know
it has to be the database. Being able to solve that
and not spend the hours of back and forth trying to
figure out what's going on has been a problem forever, and we're going to see how
we can simplify that, right? Also, having an ever-growing set of tools, like we have different tools
for Postgres, for MySQL, for Microsoft SQL, we use different things to look at the databases there
or the applications, right? And then also understanding
how all of those work. They all have very
specific characteristics that are for the specific database engines that makes it complex. So first off, here's Alex. "Help me, Alex. Sales team's reaching out. "Our retail service is
slow! What's happening?" I don't know, but let
me take a look, right? Alex is going to dive in. So what Alex is able to
do is he's able to use the fleet wide monitoring
that gives unified access across accounts and regions. Kind of key thing is
it's across three regions at a time currently due
to some limitations, but he's able to see the different alarms, the different average
load for the databases, the max load for those databases. You can see them in those honeycombs, and if it's high, it's red. If it's really low, it's white, kind of going down that scale. He can save those fleets
to different views like that retail prod application view. He can see those top 10 instances be like, "Oh this one has a lot of load. Maybe I need to focus my attention there." Additionally, he can look
at the different events, seeing restarts, failures, you know, different levels of severity
that we've kind of opinionated built into there to
understand what's going on as well as application integration where that prod retail service
had 45% failures, right? Maybe that's an issue. Additionally, there's some
top 10 metrics you can define by like CPU, memory disc, network I/O, things that are important to you, and a table view at the bottom where you can kind of see that
honeycomb in a table format. This is a great way to
start to look at your fleet across your entire global fleet, identify where the problem's happening, and then dive deeper, right, into the instance view
once you've found it. So once you've found that instance, you can start to look at it
and get the time span data at the top, right, where you
can see each individual second during the time span. And then at the bottom, you have the holistic time span, right? So you can see over the duration
we're looking at right now one hour, that we can see most of the
queries were actually due or most of the load was due
to a specific query, right? You can view this in different ways, whether you want a line or a bar graph, you can kind of see the max CPU, going above that max CPU is a general like load characteristic for it for the size of your database. If you're having sessions above that, that's generally a
performance issue, right? And you can start to carve it out. But what's really interesting here is like who's running the select + from orders and it's consistently running, right? Who's doing that? We want to start to carve that out, right? So what we can do is we can
go, okay, select that query. Looking at that query, who's running this? It's the dba_intern. Why is he running and why
is it continuously running? Where is he doing that from, right? I could see he's doing
it from these two hosts. So I know it's the dba_intern, I know he's running it from two locations. What application is he using, right? And so from there you can see, I can see he's using
the db-operations tools that they have from that
application to kind of identify the who, what, when these
things happen, right? And the where of when it's happened. We haven't answered the why, but this kind of gives you the information that now you can reach
out to that team, say, "Hey, what's going on?" You know, did they make a mistake? Is this something they need to clean up? Additionally, you can start
to carve it out by the other, the other like areas, right? You want to see which
hosts have the most load, which users, which
applications are generating the most load on the database. You could do it very easily, right? And so you kind of choose how
you want to carve that up. Next, let's move on. "Alex, help me." Sales team, "We can't run our reports. we don't know what's going
on, can you help us fix it?" Alright, so he was able
to find the instance, we already looked at the fleet view, but he found the reports, and what he's seeing is there's a lot of
locking going on, right? And he's able to use database
insights for this instance to start looking at the
lock analysis or lock table that we have, or this lock tree, I mean, and we can start to investigate deeper. We can view the specific details
that are important to us, but we can identify things like, you know, popular record, locking scenarios, and all the other common ones. There's so many different
locking scenarios you can run into, but we can start to get
an ID of what's running and then we can start to carve it out or slice out the views to
get a better understanding of what's actually going on. Right now at the top, we're looking at the weights view, right? And we can see what are
causing the different weights, we can see specifically
what that is, where it is. We can start looking
at the blocked objects. So if there was a specific
single object that's blocking it, you would be able to see
that and see it going across. See what the value of that is, and you can just kind of key
in on the various aspects here. Blocking session. If you had a single session holding up like a specific locking
scenario that's holding that, you would be able to view that here, see it across the specific time span, and then be able to identify
how you need to clear that up, which could potentially
be an application issue, but we'll look at that later as well. So from here as what we
can also do is we can kind of choose the segment
we want to key in on, that lock tree is focused
in that one area, right? So for this area what
we do is we can select that like minute timeframe and then break it down
by 15 second increments where we have this specific lock tree. So depending on the
specific locking scenario, you're able to dive
really deep to understand what's going on without
having to leave the console. You don't have to connect to the database, it's just all kind of here for you. Alright, so next. "Help me, Alex," right? Sales team again, sales
team needs a lot of help. "Our order processing was
having issues looking up orders, what happened? It happened sometime earlier today. We're not sure when, it was
just having some problems." And so what you could do is
you can go and look and see, okay, well, when we're
taking a look at this, this specific query that they were using that we know is part of that, right? We could see during this
timeframe, there were some issues, but you know, I can't tell much yet. I can see there's two
execution plans that were run. Okay, so I know that something happened, but I only really see one right now. But if I change the pan to a plan view to slice it by that, I
can see there's two plans. I can't even see the other one. Where even is that, right? I can see there's about
8.5 average active sessions and when I switch it to the other one, that's way more efficient. It went way down to like
less than like a 10th of an average active session, right? It was being very performant. So now we can go down at the bottom and it might be a little small, but you can see where we were
doing like a full table scan, right, on that order tables, and actually it's
September 19th partition, and we could see we're doing
the index only scan, right? For that yellow, the ones
that were being efficient. And what you'll notice is that is on a different partition, right? Still on the orders table, but we can kind of see
what the differences are and we can also start to
like look a little bit deeper into what the cause is for the sequel and start to understand
when and why that happened. We know it was happening
on a different table, but we can see what the
specific executions plan were when they happened and dive
a bit deeper from there. Next. "Help me, Alex." Application devs, the good old app team. "Our dev databases have
been running slow recently. What's the problem?" I don't know but I'll find out, right? That's what Alex is going to do, right? He has these automatic dashboards that are built in with metrics. He's done some of the
other analysis already, but what he can do is he can
go into his database telemetry. He has 18 different metrics
that are already built into this dashboard per database engine, per Postgres SQL, per MySQL, per whatever engine you're using. You update it once, it's going to be across the entire fleet having that same view. But we also have like
hundreds of other metrics, just search by keywords. Let's look for latency, I want some latency information, right? So I want to get my
average reads and writes, I'm going to create a new widget that's specifically for that that I can view across my entire database engine type, right? And so this is going
to make it really easy to have those customized
metric dashboards you want no matter what instance you look at, you do it once and that's it, right? And so we can see that, we can
see there's more reads there. Let's move on. "Help me, Alex." This is the inventory
manager this time, right? "Sometimes it takes a long
time to view our inventory. We're not sure what's going on but we want to know more." So what you can do is we also have some slow query analysis, right? When's it happening, why is
it happening and where, right? So we can go in and take a
view in our database telemetry. If you've noticed this is all in the same pane of glass so far. We've gone to different tabs, but we haven't changed
to a different section. We're now looking at the slow queries. We can see query patterns, and then if we select a
specific query pattern, we can see the patterns related to that. We can see how many times that's run. We can see like the
average duration, you know, what the 50% mark is, what the 95% of, you know, use cases are. And then the max, the ones
that are running long. So this can help you
identify a long running query that maybe you didn't know
exactly was running long, and also find out when
it was running long, so you can start to
analyze what was going on. Next. So "Help me, Alex." Application devs. "Our retail service is having issues. It has to be the database,
I know it's the database, I've looked at everything else. There's no way it's not
the database." Right? And so what we have is
we've built in integration with application signals. We call it calling services. These are the services that
database manages, right? So you have to have application signals configured on your applications, but we can see the fault rate
of 47% on that retail service. But now we can see why. So what we're going to do is we're going to go
into application signals. This is no longer database insight that jumps us to
application signal service, specifically that retail
service we need to investigate, right? And from here what you're going to see is it has a dashboard, it gives you an idea of like different service level operations like availability or latency that are within
thresholds you define can give you some
operational audit information out of the box. Didn't do anything, it's just there. Can show you some high periods of latency. That's just there by default
by kind of looking at it and understanding like, "Hey, this looks out of the normal." Right? From there you could take a
look at the service operations. This is generally going to be like where the compute's happening. This is happening in Lambda for me. I've built my application
to run in Lambda, and I can start to see, you
know, what's happening here. I don't see any specific errors there yet, but let me look at the dependencies that run within that Lambda function. Okay, so I have the
select operation, right? I have some other uninstrumented areas that need to be fixed, but
I can see the fault rate's high on that select operation, so what's going on with
that select operation? So what I can do is I
can select the faults, I can start to view the spans. So spans give us an
idea of what's occurring within that entire transaction. I see there's failures,
I see how long they run. I can pop this up, I'm
going to get a trace map in this trace details end to end, customer comes in, goes
through API gateway. Something's happening with API gateway, red's got to be bad, right? I can see the lambda function, the service that's running
within the Lambda function, and when it's connecting
to the database, right? Additionally, on the right, I can go down and view the actual timeline of the entire trace, right? I can view each individual span, I could see where I'm
making that Postgres query. I can go directly back to the
database from there if I want. And I can also view the
specific query for that trace that's occurring during
that specific span. And so this, if you're looking at this, you can see the duration
it took to run that call. If that's within normal behavior of what you expect for that application, you know it's not
related to your database. In this instance, I was
able to find an error earlier up in the stack in the Lambda and I can see specifically
in the Lambda function on line 96 in the code
of the Lambda function, that's where the stack
trace error's being thrown. So I know it was in within the
threshold of what we wanted, but the actual application
code threw the error in the stack trace and
pointed to the exact line that it's at, right? So as long as I know that that duration is within normal operating, like you know, expectations, then it kind of helps you point out what could potentially
be wrong pretty easily. Alright, thanks Alex. Like I
said, Alex is our superhero. He manages a lot of different things, but he was very easily be able, through from mostly a single pane of glass for his global fleet, be able to see how to fix
those different problems, whether it was related to database load, execution plans that may have
flipped or had bad plans. There's a lot of other things you can do for looking at the logs directly as well without having to change a single pane and search through those. And Alex saved the day. So with what we just went through and all the problems Alex solved, let's talk about like a pretty generic troubleshooting workflow, right? So first, identify the database instances and database load from
the fleet view, right? Look at your fleet if you
don't know the exact instance you need to go to, you know, take a look where it is
potentially supposed to be. Try to identify where there's high load. From there, dive a little bit deeper. Look at the queries that are being run once you get to that instance view. Understand where the load
is if it's related to locks or execution plans changing or what is potentially causing that. Or if there is initial
like more upstream load that's occurring and you
have to address that, right? And then from there, also review key metrics to help you kind of understand what's going on, right? So if you're looking like at, you know, blocks per second per hit, understanding how many
pages are occurring, how those are piling up, you know, average active executions, there's so many metrics,
hundreds of metrics, okay? But things that can help
you correlate as you know to understand what that load is and how it's changed over time. And then lastly, if you
have application performance monitoring enabled for the applications in front of the database, you can very easily see how the end-to-end transaction's running, you can see where the
latency is for the queries if that's within normal thresholds, and honestly not just
be able to track down when it is performing poorly, but you can actually set up
some other alarms around it not behaving as you expected
for those dependencies as well, which can make it a little
easier to be notified before you actually, you
know, have an issue happen and you're not sure what's going on. So with that, I have a few resources here. So these are just some
real scenarios, right? Go ahead and take a screenshot of this. You can go to that QR code and you can review some
very specific scenarios. There's also some database
insights, documentation. So on the documentation,
there's like a detailed section for execution plan analysis, lock analysis, and some other like functionality
that's in there as well. And you got to love the cat, super cat. This is more observability as a whole, not just database insights. But if you go to this one QR code, it has a bunch of best
practices on that page. It's going to take you to a GitHub page where we have our
observability best practices. It has a lot of really
good links in there. And then the next thing, it's early in re:Invent,
the expo hasn't opened, but when it does in AWS village, we have cloud ops kiosks, we have everything from
cloud ops, management, observability, governance compliance, resilience, AI ops, multi-cloud and more. Yeah, just come to the expo. No, I will be at the expo on Wednesday between like 12:00 and 4:00
doing the AI ops booth, which I'm doing that, as well as the observability booth where if you want to talk
more about database insights or other observability
for your applications, I will be there happy to talk to you. And with that, you know, thank you all so much for attending today. Please remember to do the
session survey for COP 331. That's how they rate me. Let me know if they want me to come back or if you want me to come back, how we can make this better for you. And yeah, I hope you all have a
wonderful time at re:Invent. Ride the Datadog slide. It's amazing, it's fun. It's one of my favorite things
to do. I do it every year. And check out the expo,
check out all the partners, the other sessions,
everything that interests you. I'll be right over there if anyone wants to chat right after this. But with that, thank you
all so much for being here, and you know, hopefully I get a chance to talk to you all in just a minute. Thanks.
(audience applauds)
---
video_id: 4HSY9Cc3U1w
video_url: https://www.youtube.com/watch?v=4HSY9Cc3U1w
is_generated: False
is_translatable: True
---

- All right, hi everyone. Thank you so much for joining us today on this first morning of re:Invent 2025. Just if you wish, a show
of hands for any of you who this is not your
first session for today. Nice, I got some early
starters, I like it. All right, so my name is Christine Megit, and I am a Microsoft Licensing
Specialist here at AWS, and I'm joined today by my colleagues, GianPaolo and Valerie. And today, we're gonna speak to you about enterprise software
licensing and optimization on AWS. There is gonna be a focus
on Microsoft licensing just because we do have some new features that we wanna highlight today, so we're excited to share that with you. And before I begin, I'm just gonna start with a bit of a quote. Most presentations like to start with an impactful or motivational quote. I'm not sure that's what we have here, but this is something that
we do here from customers on a regular basis at least once a week. So Microsoft licensing especially
can be really difficult, and we're here today to kind of break down some of that complexity for you. Microsoft licensing is complex, there's different agreement
types, different license models, is the product eligible for
License Mobility benefits? Show of hands if anyone knows about License Mobility benefits. Good, all right, nice. So today, we're gonna speak
to you about the optimization and licensing assessment,
Val's gonna kick that off. That's a fully funded program that we have for Enterprise workloads,
not just Microsoft licensing. I'm gonna take over again and I'm gonna talk to you about
bringing your own license, as well as some of our
License Included offerings. And then I'll go into some
licensing optimization best practices, including
highlighting some new features that we are going to announce that will help you save some costs. Then I'll hand it over to GianPaolo, and he's going to speak to you about Optimize CPU for License Included, which is one of the new
features we wanna highlight, and also provide a live demo for AWS Compute Optimizer
and Optimize CPU. Then we'll kick it back over
to Valerie who's gonna discuss how to get started, how to
start realizing these savings and these new features, especially
through our OLA program. All right, I'm gonna hand
it over to you Valerie, so. - Thanks Christy, awesome. All right, so a question for the audience, how many of you have ever
googled Microsoft licensing and immediately regretted it? Yes, all right, I see a lot
of hands, that was surprising. Great audience engagement. All right, so how do you
make informed decisions about migrating to the cloud
without becoming an expert in optimization strategies or getting that PhD in Microsoft licensing that Christine mentioned? Well, the good news is that
we have a program built at AWS for this. So the Optimization and
Licensing Assessment program or OLA program that Christine
mentioned is purposely built to help you optimize both your compute and your licensing costs
when you're considering a migration to AWS. My name's Valerie Rosenfield,
I'm a part of the OLA program. I've been on this team
for about five years, serving our customers as a
Migration Assessment Specialist. So I help customers when they
are considering migrating all workloads, but specifically for today, Microsoft workloads to the cloud, review what they have
in their environment, understand what their key
business priorities are, any open questions that they have, and then recommend an assessment process that will get them answers
in the most efficient manner. There we go, there's the OLA slide. Awesome, all right, so OLA
is all about simplifying your migration and your licensing journey. What are the benefits for customers? Actually I'll ask another question. How many of you are customers who are already running on AWS today? Oh, nice, awesome, you will
love this presentation then. How many customers are
considering migrating to the cloud in one to two years, but don't run any workloads
yet on AWS, anybody? Awesome, okay, any
partners in the audience? Awesome, awesome. Okay, that's great context for talking about how OLA helps simplify
the migration journey. It's good to know who we
have here in the audience. First off, OLA is a data-driven
assessment that is built to answer three key
questions when customers are considering migration
or post migration, which it sounds like is most relevant to the audience here today. The first is collecting an inventory. So we need to know what
is in your environment and how is it being used. That visibility is crucial because cloud optimization
is all about running as lean as possible, as
many of you will know, and we can't optimize what we can't see, so the OLA starts with
that baseline inventory of understanding what you
have in the environment. Next, we assess the
business case for the cloud or we assess how you can
optimize your existing footprint that is already running in AWS. So we will review your
environment to understand if rehosting, replatforming,
or refactoring is the right approach,
show you costing options for each of those, and along the way, we'll show you how you can optimize both your compute and your licensing. All right, so for customers
who are considering a new migration to the cloud, the OLA data also serves
as the building blocks for helping you plan the journey. So a lot of times we are... You're working with a
partner on the assessment, sometimes you're working
with the AWS account team, and this data just helps them
dive deeper to understand what your priorities are, what your timelines are around migration, and importantly, this program
also helps qualify you for different AWS programs and incentives. All right, what is the
impact of OLA in numbers? So first off, as Christine mentioned, the OLA comes at no cost to customers. This is an investment that AWS
makes in setting customers up for success as they
migrate and post migration for those of you who are
already running in AWS. Next, we see that customers that perform one of these exercises and
take the recommendations that are surfaced in the OLA
achieve a 36% cost reduction. Finally, migrations are about 34% faster when you're executing the
migration based on real data instead of guesswork. All right, so we will zoom in a little bit on the Microsoft side of the assessment. So what will you get from the
Microsoft licensing analysis that is a part of an OLA, you know, that's why most of you are here today. When customers are considering a migration of their Microsoft workloads to AWS, they come to us with five
key questions normally, and OLA has the answers for those. The first is, what does my Windows and SQL Server footprint look like? So that goes back to collecting that baseline inventory as the first step. And we'll talk about
process-wise a little bit, what that looks like
on the following slide. Next is, how can I reduce my SQL cores? So we see that the
majority of our customers spend on Microsoft products
is typically on SQL Server, especially in terms of what
gets migrated to the cloud. So that is top of mind product when customers are thinking
about cost optimization. Next, can I bring my own
licenses to AWS or BYOL? Most of you will be familiar
with that terminology. The good news is the
answer is typically yes, there are, of course,
nuances and that's exactly what the OLA will help you navigate. Even if you can bring
your Microsoft licenses to AWS, should you? And today, we're gonna be
talking about an exciting feature that is released for
License Included workloads that can help reduce
that spend versus BYOL. So in the future, we actually do think that License Included options will become more cost competitive for customers, so stay tuned for that. And finally, how do I optimize
my Enterprise Agreement, my EA renewal with Microsoft as I migrate? So if you can execute one
of these assessments shortly before your EA renewal,
that's really the prime time to do it because then you can
actually realize the savings that will surface to you in the OLA. As many of you will know, this
is usually a three-year term, so if you can do this exercise
in preparation for that, you'll avoid that lock-in or be able to choose more flexible options when you do renew with Microsoft. All right, so tying it back
to that first question, how do we collect an
inventory of your Windows and SQL Server footprint? OLA can support you in two ways for this. If you have a tool on
premise that already has an inventory of your
environment, has limited gaps, it has your SQL inventory,
you can supply that to us instead of installing a tool, which sometimes takes some time, and we'll clean it, consolidate it, and analyze it for you, turn
it into an AWS business case. If you don't have a tool on
premise with high coverage or you just wanna get a fresh dataset, AWS, this is part of the
investment that we make in the OLA program, we'll
fund a discovery tool for you to collect the information. So there are a few tools
that we use for this process. You may be familiar with
some of these names. This isn't the full tool set, but it's what we use on the
majority of engagements. We have our first-party AWS
Migration Evaluator tool and two third-parties named
Cloudamize and modelizeIT. In terms of the information that we get from Microsoft workloads, you're
going to get the additions and the versions of your Windows
and SQL Server deployments. We'll get information on
how those are utilized. So the CPU memory storage utilization, and then the instances and
databases that are running. And the purpose of this is
just to inform the Windows and SQL Server optimization
analysis that we'll walk you through on the following slide. All right, let's get to the good stuff. This is a sample OLA output from a recent customer engagement, and this was an existing customer in AWS, I think it will resonate with the audience that we have here today. This customer was a
large healthcare customer with $16.5 million of EC2 spend. So the first optimization
that we are going to surface in an OLA is right-sizing your workloads. So this is the basic level
one version of optimization where you are just running the
most cost effective instance that meets your performance needs. AWS has a variety of
different instance families, and so a lot of times, you're running one that doesn't perfectly
suit whether that workload is compute memory or storage intensive, and just switching the
family can reduce your costs. In this case, right-sizing
just their Linux EC2 workloads save them about 12%. This is savings opportunity, so perhaps they execute on 50% of those, but still pretty meaningful
savings at $1 million. The next optimizations are
specific to Windows EC2 and SQL EC2 workloads, and this is what we're gonna dive deeper into with Christine and GP
later in the presentation, so I won't harp on it too much. But an exciting new feature
that allows you to tailor the number of vCPUs that you have on your Windows and SQL
License Included instances, as many of you will know, those licensing models are core based, so anytime you're
reducing the core counts, you're gonna reduce your licensing costs, and this actually comes
directly off of your AWS bill. So if you're purchasing Windows
or SQL licensing from AWS, which most of you will be, this will reflect a
reduction on your AWS spend. In this case, it was a
13% additional savings, so another $2 million that... Before this launch wasn't even possible. This is an incremental strategy
that is really gonna make some important savings
changes for our customers. And finally, the template. The standard output that
you're gonna get for SQL, the additional optimization strategy is identifying SQL workloads that look like they're non-prod. Microsoft has a free edition of SQL Server called Developer edition,
and so during the OLA, we'll flag instances that
look like they are non-prod based on their naming convention. So dev, test, QA, et cetera. We'll summarize the cores
that are running on those, show you what you're likely spending on your Microsoft contracts
for those non-prod cores, so you can make an informed decision about whether you should
downgrade to that Free edition of Microsoft SQL Server
called Developer edition. In this case, it was an
incremental 2% savings, so a little bit lighter
than the other savings, but sometimes this is the easiest one for customers to execute, so
it's still pretty helpful. Awesome, so cumulatively this was a $5 million savings
opportunity for the customer and they were very
pleased because for them, even if they only achieved
25% of these savings, it would still be over $1
million, which meant... Was a meaningful cost reduction and a reinvestment opportunity for them. All right, wrapping up this section. So the final question
that we usually address in an OLA is how do I optimize my Microsoft Enterprise Agreement renewal? Again, we highly encourage
doing one of these exercises six months to one year in
advance of your EA renewal, so you can go into that conversation with the insights from the OLA, especially if you're seriously
considering a cloud migration within the next year as well. Is anybody coming up on
their Microsoft EA renewal in the next year? Anyone know? We don't know. Not procurement people it sounds like. All right, well, there
are some standard insights that will surface as
a part of this process and then we have experts
who can dive deeper, look at your unique contracts
if you are interested in that type of tailored analysis. But the first one is, for Windows Server, most customers are gonna
migrate to shared tenancy in AWS and that comes with the
Windows License Included. So our standard recommendation
is to avoid double payment, you should discontinue
the payments that you make to Microsoft annually for
Windows Software Assurance to reduce your net costs. For SQL Server, we encourage
customers to switch from perpetual licensing to subscription in certain scenarios, this is
not right for every customer. But if you know that
you will be optimizing your cores further after migration, but you don't have time to
do it before your EA renewal, a good option can be to switch
to subscription licensing so you have the flexibility
to true-down sooner. EA is a three-year lock in unless you do that subscription licensing, which would give you more flexibility to true-down after a year. So it's something to consider if you know you're gonna optimize, but you can't do it immediately. Next, and again, this is gonna tie to GP's and Christine's presentation on Optimize CPU for
License Included workloads, but evaluating whether License
Included is a better option for you than Bring-Your-Own-License. Outside of it becoming
more cost competitive with this new feature, a lot of customers just prefer not to manage
licensing with Microsoft. Makes sense, rightfully so. So you can outsource that to AWS and we manage the licensing
payments to Microsoft when you go License Included. And finally, this is not specific, we talked a little bit about
addition downgrades before. This is more associated with
your production workloads. So if you have production workloads that are running Enterprise
edition software, a lot of times, you're not
using the Enterprise features and it's actually less expensive to buy new perpetual standard licenses than just to renew the
annual maintenance payments on Enterprise Edition. Enterprise is about four times more as expensive as Standard. So that's another thing
that you can consider. Assess whether you're
actually using the features and if not, it might be a good opportunity just to make the change, bite the bullet, and downgrade to a Standard edition. Awesome, so these are the
standard recommendations that you will get in an OLA output. But behind every OLA, we have
a team of licensing experts like myself, like GP, like Christine, who you can tap into
if you have more custom or specific asks, and they can also answer follow-up questions on
the licensing insights that we present. Christine is the expert
in Microsoft licensing, she's our go-to, so
I'll pass it over to her to give more detailed
insights on how to optimize and manage in the cloud. - Thank you so much, Valerie. All right, so now, I'm gonna go over a bit of licensing information for you. I'll start with Bring-Your-Own-License and how that works on AWS. So I mentioned earlier,
it looks like a lot of you maybe are already familiar
with License Mobility benefits, but if you're not familiar, this is a Software Assurance benefit that allows you to bring
your eligible products to a shared tenancy
environment such as EC2 on AWS. To qualify, the product
itself must be eligible for License Mobility benefits. So it's not necessarily enough that there's Software Assurance, the product also must be eligible, and again, the Software Assurance and eligible subscriptions are required, and this can be deployed on
shared or dedicated tenancy, it doesn't have to be shared. And there is a License Mobility
verification form as well that you are to fill out up
to 10 days after deployment. For some products that are eligible for License Mobility benefits, we have Azure DevOps, Exchange
Server, Project Server, SharePoint Server, SQL Server, of course, System Center Server,
and there's some others in there as well. So just to dive in a bit
more into SQL Server BYOL, 'cause it is a very popular
product for customers to bring. If we're looking at the core model, one core license is gonna cover one vCPU on shared tenant EC2. There is a four core licensing
minimum set by Microsoft. So you could potentially
deploy on an instance smaller than four vCPUs, but you would still need to assign four cores of licensing as a minimum. Again, Software Assurance is required, and if we look here at this chart of... The r7a instance family, you'll see the r7a.large
does have two vCPUs, but again, you would assign four cores just because of that four
core licensing minimum. If you were to deploy on
the r7a.24xlarge instance, you'd bring 96 cores of SQL. Now, for the server CAL model, we don't come across this as often, but it is definitely something that some customers do still have, for specific use cases. Here you're just gonna
have one server license per EC2 instance or per VM, plus you'll have the
additional user or Device CALs for all users or devices that have access, and that's direct or indirect access. You'll also need the Software Assurance or eligible subscriptions
on the server licenses and also the the CALs. Again, just a reminder that License Mobility
verification form is required. A bit more on BYOL for SQL Server, there is a passive failover
benefit available for customers that are bringing their licenses with their Software Assurance. Again, this is a Software
Assurance benefit and it is one-to-one, so
it does work differently than maybe what you can do on-premises. So that is a key note to consider. So one SQL Server EC2
instance, for example, allows you to deploy a secondary
passive SQL Server instance of the same size or
smaller in terms of vCPUs. This is not eligible for
active-active configurations. If we look at this example
here, two R5 instances, eight vCPUs each, the
passive instance doesn't need to be licensed for SQL, but the active instance
would be licensed for SQL. So overall, eight cores of
SQL Server licensing required for this configuration. Now, for non-production,
Val touched on this already, but SQL Server Developer
edition is free for you to bring for non-production workloads,
so it is a BYOL scenario. And with the release of SQL
Server 2025 just the other day, not sure if you saw that, but there is now two Developer editions
available for that version. One for Enterprise edition,
one for Standard edition, which is great for those of you that are only looking to deploy. In Standard edition, once
you move to production, you can use that Standard
edition, Developer edition. For anyone deploying SQL Server
2022 or earlier versions, you'd still use the Standard... Developer edition that covers all features up to Enterprise edition. And as a reminder to use
this Developer edition, you cannot be connected
to a production database or it can't be used for DR as well. And it does include all the same features as Enterprise edition except, of course, where you're using the new 2025 version that does have a Standard edition. And as with any BYOL on AWS, you are required to bring
your own media or install for the products that you're bringing. Now, I'm gonna shift
gears to bringing products that do not have License
Mobility benefits. There was some changes that were made effective October 1st 2019. These were changes
specifically impacted products that are not eligible for
License Mobility benefits. So this does not impact anything I've just
spoken about previously. To bring a product that is not eligible for License Mobility benefits,
such as Windows Server, the version you're deploying
first must be a version that was released before October 1st 2019. For Windows Server, that's
version 2019 or earlier only. You must also have perpetual
licenses, not subscription. And the licenses must have
been originally purchased before October 1st 2019 or originally purchased within an EA term that started before October 1st 2019. So again, this impacted
products only not eligible for License Mobility benefits,
that would be Windows Server, Visual Studio, and Office applications. SQL Server without Software
Assurance would also not have License Mobility benefits, so
that would also be impacted if you did not have Software
Assurance on your SQL. Just to dive a bit more
into Windows Server BYOL, as it does come up quite often. If you have those eligible licenses and you're deploying
version 2019 or earlier, you would use dedicated
hosts and you would license the total number of
physical cores of the hosts. So if you're looking at
an R5 EC2 dedicated host, for example, that has 48 physical cores, you'd license 48 cores
Windows Server Datacenter, and you'd be covered for
any number of R5 instances that you can fit on that host. This also is true for our
recently launched service, Amazon EVS or Elastic VMware Service. It is running on dedicated,
so it does allow you to bring your Windows
Server licenses as well. Again, Software Assurance is not required for bringing Windows Server because it doesn't have
License Mobility benefits. So whether you're using BYOL or you're moving to a
License Included model, as Valerie mentioned, that's a great way to reduce costs at your next renewal, is to lower that Software Assurance as you won't be needing it. Now, for License Included and some of the offerings we have there. For Windows Server License Included, this is most commonly used by customers because it does allow customers
to deploy on shared EC2. It covers any addition. We don't always list an addition, but our licensing agreement
with Microsoft is very specific, very customized, and
it covers any addition. It also includes unlimited
Windows Server CALs, as well as two remote
desktop services connections for each EC2 instance that
using License Included. And again, this is a
required licensing option on shared EC2. It's also required for
versions 2022 and 2025 of Windows Server, and
that's because those versions were released after the
October 1st 2019 changes. These Windows Server License Included is billed per vCPU per second
for on-demand instances. It is an option that can
be used for external use. So for example, if you are
an ISV or a SaaS provider that was impacted by the SPLA BYOL changes where Microsoft no longer
allows SPLA BYOL on AWS, License Included is a compatible
option for those workloads. And if you need additional remote desktop services connections, we do offer those as License Included. But you can also BYOL or
bring your own RDS User CALs with Software Assurance through
License Mobility benefits. Now, for License Included SQL Server. We offer this in the core model only, so there's no CALs required. We offer this in Standard,
Enterprise, and Web edition. Again, with the release of SQL 2025, there is no new Web edition available. So 2022 Web edition is
the last edition available and it is a very specific use case. So Web edition can only be used for publicly accessible websites. If you're not familiar with that edition, that probably means you can't use it, but it is something that
we do offer for up to 2022. All right, so this is also
billed per vCPU per second for on-demand instances, and it can also be used for external use. So again, if you're an
ISV or a SaaS provider, this option also replaces the
SPLA BYOL that was removed. All right, so now, onto some licensing
optimization recommendations and best practices. So we do have a free tool
called AWS License Manager. This is a great tool to use to input your licenses
that you're bringing. It can also be used to take a look at your License Included instances. This is a great way to keep
track of what you're using. You can use it also to integrate with dedicated hosts and other services. So I highly recommend checking this out, if you haven't already. It can be used with a variety
of different software. It doesn't have to be Microsoft, there's a lot of different
vendors that it supports, and you can use it even for on-premises, or workloads, and other clouds as well. This is just a view of what it looks like when you're inputting some licenses. and you can choose whether you want to enforce a license limit or don't have it in
force where you just get a warning message if you
go over your licensing. If you are interested in
learning more about this tool, I'm also speaking at a
second session on Thursday called MAM321: Licensing
management and optimization where we are gonna speak about
some new licensing features through License Manager. That's on Thursday, December
4th at the MGM Grand. This QR code will take
you to the catalogs, you can see where that's located. All right, instance right-sizing. As Valerie mentioned,
this is a core component of our OLA offerings. This can benefit License Included. Our products are licensed per vCPU for Windows Server and SQL Server, so the more you're right-sized
on the instance size, the more your licensing costs
will be right-sized as well. For BYOL, this is also beneficial because SQL licensing for
BYOL is licensed per vCPU if you're bringing core licenses, and again, right-sizing is
gonna optimize your licensing that you're bringing over as well. On the Windows Server side,
this can help in both ways. BYOL, if you're right-sizing, you can end up with fewer hosts, which means lower infrastructure costs and lower licensing costs as well. And again, OLA, so that's
gonna help you figure all of this stuff out. Now, for a new feature that
we just recently launched, Amazon EC2 High
Availability for SQL Server. This is a new feature available for License Included SQL
Server that now allows you to not license the
passive or secondary node. Previously, this was required,
you'd have to license both if you were using License Included. Now, if you're using License Included, you will be exempt from the
SQL License Included costs on that secondary passive node. So this supports two EC2 instances per SQL Server High Availability cluster. It supports always on availability groups, as well as failover cluster instances. You only pay for the Windows
Server License Included costs on the passive nodes, as well as the compute costs, of course. The passive SQL Server instance
needs to be the same size or smaller than the active
SQL Server instance. And this is available for
new and existing instances. So you can go into the console
to update your instances if you have these already or you can use this for new deployments. It does require AWS Systems
Manager Agent to be installed and running on the
instances for this to work. If you wanna learn more, we do have this QR code here as well. We have lots of documentation for you including a blog that's
been released as well, so check that out. And for another new feature
that has been recently launched, and this is gonna be spoken
about a lot in our session, GP's gonna take over for me shortly, but this is Optimize CPU
for License Included. So previously to this
launch, customers could use Optimize CPU to lower their
number of vCPUs on an instance, which would let them bring
fewer SQL Core licenses. This now is available for
License Included as well. And it not only impacts SQL
Server License Included, but it also impacts Windows
Server License Included. So this is gonna be a
great way for customers who for the most part have to use Windows Server License
Included on shared EC2 if there's room for optimization there, and to either disable hyper-threading or use a specific number of vCPUs, this will immediately lower
your License Included costs for Windows Server, as well as SQL Server. Using this feature, you
will see a separate billing for licensing, so it will be broken out of your EC2 instance costs, which is new. Typically, without using this feature, your License Included costs will be within your compute costs. This feature will separate those. And again, this is available
for new and existing instances. So great news here, here's just an example of the x1e family type. You can see the max vCPUs
is the default vCPUs, the instance size comes with. You can turn these down all the way to the examples shown here. But just a reminder, SQL Server licensing is a four core minimum
even for License Included, so we wouldn't necessarily recommend going all the way down anyways, but
if you were to go below four, you'd still see license
costs for four cores. All right, so that's it for me, I'm gonna hand it over to GP. - Thank you. So my name is GianPaolo Albanese, I'm a Solutions Architect Specialist. Been at AWS for eight years. The one thing that I got
from the session so far is that I have really
trouble sleeping at night. So if you wanna fall asleep very quickly, you can read about the licensing
that Microsoft provides. I will appreciate actually
Polly, Amazon Polly, to actually read it to me
very slowly and softly, and you fall asleep right
away, or you can go to a bar. But this is probably works best. So let's move in and
talk about a little bit about Optimize CPU and SQL Server. So why is this important? So SQL Server licensing
is based on active CPUs that are visible to the operating systems. And so what we are seeing more and more is that customers need to
deploy larger EC2 instance sizes because they have specific requirement, either IOPS requirements
or memory requirements. And so therefore, if you
want a 512 gigs of RAM allocated to your instance,
you have to deploy maybe an r6idn.16xlarge. It's a lot of money, right? And again, there is gold, right? There's gold coins in there. So every time you basically
spin one of these machines up just to accommodate one of your workloads, again, it's a huge cost
that happens on licensing. And so again, what we're
trying to do is we're trying to kind of minimize the cost. So what can we do? As already Valerie and
Christine mentioned, we do have a new feature,
it's Optimize CPU. And what Optimize CPU would
allow us to do is it allows you to actually modify the
instance type after launch. So what you can do is
after you start analyzing your workload and trying
to figure out exactly what really works or what
is the perfect balance between CPU memory and storage, then at that point you can
actually stop the instance and start making some
modification to the instance. In fact, some of the
things that you can do or how this feature works is that after you accept
the default instance that you have deployed, you can go back and you can
start working on disabling the hyper-threading on the CPU. So you allow now to modify that
after you stop the instance. And what we notice that most of the times, when you're dealing with high
performance compute workloads or maybe someday it's dealing with the scientific calculations, disabling hyper-threading
actually helps a lot, right? You see an improvement because
there is no context switching with the operating systems. And so at this point, what you can do is you can also now go even further. After you disable the hyper-threading, you start analyzing your workload, now, you can go back and say, "Maybe I can actually
also trim down the CPUs. I don't have to dedicate four
CPUs for my Windows Server, maybe I can go for two," if
you're not running SQL Server. Remember, SQL Server requires four CPUs, there is no way around that. So that's another way that
you can kind of reduce cost. So what are some of the key benefits that some of our customers seeing? First of all, you start seeing a reduction on your SQL Server cost, especially with you
Bring-Your-Own-License into AWS, and there is a new feature coming up where this will available also for License Included on SQL Server. But what I also know, there's
a lot of commercial software, they have specific
requirements that are many CPUs you need to run to be compliant. Especially if you have
like a third-party support and you need to open up a case, you wanna make sure that
you follow the guidelines from the third-party vendor or the the CALs application requirements. Something else that you
can see is we seen... Some customers seeing some
really performance improvements when they disable the hyper-threading on some of the workloads. Again, you need to test that out, and we do have CloudWatch and CloudMetrix that you can kind of collect or if you have your own collection agents, you can kind of start
collecting this information and analyze it often. And again, we have another
exciting tool that we can use to actually help you go
through and figure out exactly what is working for your
particular workload. And so we this, see some
customers now improving and having performance improvement just by disabling hyper-threading. And also what they (indistinct) is another is a lower infrastructure
cost, and that's key, because, again, AWS is
a little differentiator with other cloud providers you might see. We always try to help
customers save costs, right? We provide you the tools
to analyze your workload and then you can work with any one of us, a solutions architect or specialist, to kind of help you kind of figure out where can we kind of trim things or kind of lower the trial a little bit so that you can save some money. So what are some of the best practices, specifically when you're dealing
with SQL CPU optimization? Well, there's some things
that you really need to be careful and be watching out for. So first things that we noticed is that once you disable
the hyper-threading on SQL Server specifically,
we don't see any major impact on performance on the machine. In fact, that's a quick win,
right, for saving money. And the beauty of this is that we... Especially if you're dealing with online transactional processing, actually benefits the operating system and the server actually runs
much better and by performing. The next steps, so with the first steps you see almost 35% on cost. But if you go to the next
steps and now start looking and monitoring your environment even more, you start realizing maybe
you can kind of throttle down even the core count. And if you do this, you
can actually achieve a 47% cost savings without
impacting your workload. Now, I wanna be extremely careful there. You have to continuously
test the environment and collect metrics to make sure that you're actually
achieving those goals. Because sometimes what's
happening is you might have certain processes or certain systems that at the end of the month
are very transactional, they're running some
big batch jobs, right? And you wanna minimize any
impact on your performance. And the other thing I wanna mention is, actually you need to monitor, you know, the IOPS and CPU ratio. So we found like a sweet spot,
7,000 to 8,000 IOPS per CPU is the sweet spot where you can get actually good performance, and also there is a
cost savings associated. If you start deviating from
this IOPS requirement per CPU, if you go to high, you
have system contention. 'Cause what happens is
now the IOPS are very high and what's happening in the subsystem is actually working very, very hard. So now, the storage IOPS system
is actually being impacted. If you go the other way around where you travel down the IOPS, now, you're seeing that
you CPU is actually idling and it's not doing anything, it's waiting for the
system to provide data. So again, testing is key
and you want to kind of don't want to go... You wanna kind of stay or monitor the IOPS for your environment. And lastly, test, test, test. You have to test your workload, test with load, with no load, test over the weekend nights, you know, Black Friday, just test it. We have a lot of tools
that we can provide you. We have CloudWatch metrics
that can basically help you monitor all these things. You can also set alerts as well or you can create an SNS
topic and send the information to your email or to a dashboard. So now, it's part of the demo. So how do you do this? So let me just switch over to my screen, and if everything works
well, there you go. So you have your Console here, right? Don't look at my bill. This thing is bothering me. There we go. So a bunch of instances
running on my system, right? And right now, I'm just gonna second guess and see what's happening, right? I have no metrics, but let's
say that I have this SQL Server that I'm running on m5.xlarge, right? And right now, if you look
at the instance, right, if you don't know anything about m5.large, you can actually see how many CPUs are allocated to the system. (GP hums) Oh, sorry, that's the guy. There we go. All right, once you look at the details, you go on the bottom,
and you can actually see some information about the server itself. So right now, if you
can tell on the screen, eight CPUs are actually allocated to this virtual machine, it's by default. So I deployed the SQL Server, I've deployed Enterprise on it, I automatically enabled eight CPUs on it. But let's say that you wanna actually now start streaming down or start playing around
with the hyper-threading. Well, your first thing you
have to do is you actually have to stop the instance, right? Now, once the instance is stopped, it will take a couple
minutes, a minute or so. We can actually go in there
and not stop playing around with the hyper-threading first, right? And you'll see that after you do that, you can actually start
the instance up again and it will actually now allocate only the number of CPUs that I've... Or vCPUS that I have allocated
to a particular system. So let's refresh this real quick. Okay. All right, that's the guy. So you go to Actions, you
go to Instance Settings, and now, you have a new option
here that says Change CPUs. Here it actually allows you and it gives you a little snippet there. It tells you that you
can lower your Windows with SQL Server Standard
vCPU licenses, right? By just playing around with these numbers. The one thing that I'm gonna do is I'm just gonna disable hyper-threading. Right now, we have two
threads allocated per CPU across my server. Notice what happens. First of all, you get this message that if you are used to
looking at the billing and the way the EC2 is actually charged, usually if you do a License Included, you only see one cost, right? Once you actually start playing
it out with the threading or a CPU course that you
enable and disabling, it actually is gonna split the cost. So you're gonna see two prices there. One for the instance and one for actually the number
of CPUs actually allocated. So I'm just gonna change it. The only thing you have to do after this is just start the instance. You give it a minute, right? And now, you can see that the
number of vCPUs now it's four. So going forward, if you
have a License Included with SQL Server running on it, you're gonna only pay for
the four licenses now, instead of eight. You can do this on every
single server across your fleet and you're already gonna start
seeing some cost savings. But obviously, you're gonna ask yourself, "Am I gonna go through 5,000 servers and start clicking on things, and trying to figure out what
works, what doesn't work?" Obviously you don't wanna
do that, right? (coughs) So another tool that we have, and I'm gonna switch
back to PowerPoint, yeah. Is the AWS Compute Optimizer. This is a great tool, and the reason why is because it takes the
thought process figuring out what work and what doesn't
work in your environment to the next level. So what is it? It's actually powered by Machine Learning. You're gonna hear about
AI across the board. Well, this is actually a tool
that I really love to use because it actually saves me a lot of time when I start analyzing my environment, and you will see why, right? So it is powered by Machine Learning. It actually analyzes historical data that is being collected from your systems, from CPU, memory, IOPS
consumption, and it starts just tracking all these
data, right, internally. It starts identify some patterns
and maybe you have missed. So you run this in your
environment, you turn it, literally, it's a flag that you enable, and it starts analyzing your
environment for you, right? And then what it starts doing,
it starts making predictions. It starts telling you,
"Okay, you know what? I see a cost savings of X
thousands of dollars a month if you make these modifications." In the past we had similar
tools, I kind of did this. However, you only provide
you like, you know, you could use Cost Explorer, right? You can use AWS Budget, you
can use all these other tools. I kind of combine 'em
together to give you that data and then you have to figure out what you wanna do with this data. So what happens? Well, as it goes through, it starts looking at your EC2 instances, it starts looking at
your auto scaling groups, the EBS volume, the storage,
the Lambda function. Now, we have also Aurora and RDS databases that actually are being monitored as well, and also we have ECS on
Fargate, and we are gonna have more and more services being
monitored by Compute Optimizer. Now, what happens, because it's using AI to actually do all this, right? It's all automated. Think about this. You have a guy working 24/7,
monitoring your environment, collecting data constantly,
then using the data, running some algorithm against it, and then trying to figure out
what will work best for you. So again, it's a predictive
cost optimizations. So you really don't have to do anything, you just have to turn on a flag. It actually looks like your performance on the subsystem as well. So if you remember before,
we had to find a sweet spot, 7,000 AI, 8,000 IOPS per CPU, we don't have to do that now, right? The system will do that for you, and it also it's gonna make some data driven recommendations,
which is very cool. So I just have a quick dashboard
and then we're gonna... I'm gonna jump into my laptop again, I'll show you my environment 'cause I had to collect some data first. But for example, it gives you
eh, $185 a month cost savings. Ah, not big deal, right? You click on the EC2 instance,
but you can see there on the left side all these other services that it's actually
monitoring for you, right? And again, like I mentioned before, more and more service are gonna be added. And then what it'll do is it actually make a recommendation for you. Look at all your environment, it is actually looking at your workload, and then it's gonna actually say, "Wait a minute, some of these systems are actually optimized, some
of them are over-provisioned." And then it actually tells you
what is over provision, why. In this case, CPU over provision,
EBS, IOPS over provision, and so on and so forth, because I haven't done
anything with these machines. Basically the sitting IOP,
right, running something. But if you look on the right pane, it actually gives you a
estimated monthly cost of what the cost savings are. So if we go back to my screen, yep. And we do AWS Cost Optimizer,
Compute Optimizer, right? So let's look how my account looks like. Definitely over provisioned. There we go. So I have cost saving. This is just my personal account, right? I can actually save $1,000 a month. I mean AWS saves $1,000 'cause
I'm not paying for this. But look at this, some of the
numbers, 15% cost savings. And what I really like about this, I can click on my EC2 instances, and now, I have the
data that I need, right? It tells me that my SQL Server
Optimize CPU is optimized, but there is a bunch of other instances that are not optimized. Now, the cool thing about this is that it's actually gonna start making some recommendations of what
the current instance type is and what is the recommended
instance size to go to. Now, the other thing that you can also do is start using this data to instead of maybe changing instance sizes, because now, we have the Optimize
CPU that we can leverage. Go back and stop playing
around with the hyper-threading and, you know, and turning
off the CPUs on your system. So you don't necessarily, but
you can use this as a guide to kind of help you through it. Very cool stuff. So the question that you might have now is how to get started
with all of this, right? So I'm gonna give it back
to Valerie to continue. Thank you, Valerie.
- Awesome, thank you GP. All right, so we've just seen
the power of Optimize CPU for License Included in real life. We saw some good usage of the
AWS Compute Optimizer tool to right-size your
workloads in other ways. You may be wondering how
you can start assessing the savings that are
possible in your environment. So as GP mentioned, we do
have these self-service tools in the AWS Console. Compute Optimizer is
a great starting point if you like to get in the
data and do it yourself. But the OLA program is
here to support as well, wherever that would be useful for you. So Compute Optimizer does have the resource utilization data. You'll see your CPU memory
IOPS throughput usage there. It doesn't quite yet since
this feature of Optimize CPU for License Included
was just released have the recommendations on
whether you should disable hyper-threading, whether you
should just reduce the vCPUs instead of changing the instance type. So that's where OLA can
step in, in the interim, while they're rolling out those features to AWS Compute Optimizer. For existing AWS workloads, this program is programmatically available for any customers that are
carrying AWS Enterprise Support. This criteria is really
just tied to the fact that when customers
have Enterprise Support, we have permissions to the necessary data to do the OLA savings analysis. So this is actually a very
quick exercise for us. For you who are already running in AWS and carrying Enterprise Support, we can turn around the OLA insights in less than a week usually, and it requires almost no lift from you. The only thing that would require lift is really you tagging your SQL, Bring-Your-Own-License workloads if you are using any of those. So in order to launch this assessment, most of our sellers will be
familiar with the OLA program. AWS is a big company, so
your specific account manager might not know about the program. So ask your AWS account manager, ask your services
partner, if you're working through a partner about launching an OLA, or you can use the QR code that is here. This will just pop up an email that asks some questions
about your environment and sends those responses
directly to our team, so we can get you started on your OLA for your existing EC2 environment. For your non-AWS workloads, the program is also
available for all customers. We do see, since these savings
that we've reviewed today are so Microsoft focused, that
it makes the biggest impact when you have around 100 Windows
Servers or 10 SQL Servers, licensable SQL Servers
in your environment. But we have the offering
for all customers. Again, reach out to your
AWS account manager, say you learned about OLA at re:Invent and they should know how to launch one. If not, you can contact us through this direct QR code as well. Awesome, all right. So here we've talked a lot about Optimize CPU for
License Included today. The census feature was
so recently released. We've just started to analyze
customer environments. I have some savings from the
last month of assessments that we've done that I'll show you. But in the meantime, we
have these blog posts, we have the user guide, we encourage you to check out that documentation,
it's very thorough, and there's a lot of self-service tools that can help you get started immediately. Give you a minute in case
anybody wants the QR code. Awesome, all right. So these are just a
handful of results, again, these savings are pretty preliminary since we just released the feature. But I tried to provide a
range of customer sizes and sample savings. We have a customer with $2
million about EC2 spend. They had projected savings
of 15% on their EC2 compute just from the Optimize CPU
for License Included features. So again, this is
incremental to right-sizing, this is incremental to other
SQL reduction opportunities we discussed like
non-prod, Dev downgrades. So 15% of savings that
weren't achievable before are now possible. And even more impressive savings
for a medium-sized customer that probably wasn't very
optimized, 30% savings for them, 10% savings for another customer, 24% savings for an extra large customer. On average, what we're seeing right now is around 20% savings. Again, it's not a huge dataset, but that's about where we
expect the savings to land on average, 20% on your
overall EC2 compute just from this one strategy. All right, so we've talked
a lot about OLA today. Today, OLA is a guided program. We have self-service tools
like the one GP mentioned, like AWS Compute Optimizer. Today, the OLA program is guided. So you engage AWS we... I either work with you directly or sometimes you'll work
with a certified OLA partner. We'll help you run the data collection, we'll do the analysis, we'll
read out the insights to you. But in an ideal world,
this would all be automated and that is what we're moving towards with our tool called AWS Transform. So this is available to
you in the AWS Console. And over time, the OLA insights
that we've reviewed today are gonna roll into AWS Transform. It's not quite at parody yet, but we encourage you
to be an early adopter. Check out the tool, see
what types of migration, recommendations, and licensing insights you can already get from it today. And provide us feedback, let
us know what you think about it so we can continue enhancing it. All right, today's session
was heavily focused on Microsoft workloads. That was on purpose, but
we do wanna do a quick plug that for all major workload types, we have an assessment offering
under the OLA program. So we have modules for EUC for storage, end user computing for storage,
for VMware, for Oracle. So let us know what your
mix of workloads are, or your account manager,
or your services partner, and we'll make sure we
customize the assessment to what you have. And again, we just have the QR code if you would like to reach
out directly to the OLA team. All right, we are just
about ready to wrap up. I have the various QR codes
on the next two slides that we reviewed throughout the deck. So our Optimize CPU for
License Included blog, requesting an OLA, and learning more about AWS Transform assessments. Give you a minute for those. On the next slide, we have a link to our Skill Builder AWS platform. And this is a training platform with trainings on every AWS
topic that you could imagine. There's over 1,000 deep dives. So whatever topic you are interested in, we encourage you to check out
our Skill Builder platform to continue your Amazon
AWS learning journey. So this will link you directly to the Microsoft workload section of that Skill Builder page, but again, lots of trainings
available to you there. Awesome, so I'll wrap us up
with a couple key takeaways. We've talked about three main
things in this presentation. First, Microsoft licensing is complex, but we have the OLA
program available to you to provide clarity on
the best way to migrate your Microsoft workloads to the cloud. Second, is that we have our
very new exciting Optimize CPU for License Included features. We're really excited to see how this can make License
Included offerings more cost advantageous for customers, and really reduce that
license compliance management that they have when they
contract directly with Microsoft. And finally, AWS Transform is the future. We wanna make this as accessible as possible for our customers. So we will continue to iterate and bring these optimization
insights into AWS Transform, and we encourage you to check that out. Thank you very much for joining us, for spending the whole hour with us. We look forward to partnering with you on your migration journey or optimizing your
existing AWS environments. We'll be around if you have any questions. Thank you very much. If you don't mind filling out
the survey in the mobile app, we would really appreciate
it, enjoy re:Invent.
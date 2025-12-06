---
video_id: JsuEPLg50fc
video_url: https://www.youtube.com/watch?v=JsuEPLg50fc
is_generated: False
is_translatable: True
---

- So hope all of y'all
had like safe travel and are excited for the re:Invent
for the rest of the week. And before we get engrossed
with the great sessions that we have planned for
you for the entire week, let's think through a scenario over here. You get up, you wanna
grab a cup of coffee, you go to your favorite coffee shop and you order your usual coffee. The barista says, "Sorry sir,
I can't do that right now. I don't have all the ingredients available at one place right now. The creamer that you like
is in the side cooler. The special milk that you
like is in the back warehouse and the beans across the town altogether." Sounds absurd, right? But isn't that how organizations
running our data today? That like our data sits
in different systems, customer data somewhere
else, our sales data, different places, our
service analytics data, completely different places. And then you have all your usual questions that our executives come up with. "Hey, can I know what was
the sales last month?" Or you know what this new
product that we launched, how is it doing based on the
opportunities that we had? And it takes us weeks to get
the data in the right place so that we can just run basic analysis on it. So this is why we are here. I'm sure Shruti Worklikar senior manager, analytics specialist SA and with me, Shrey Malpani senior product manager for AWS analytics. And we have talked to
hundreds of customers and what they have told us is
they wish there was an easy way to integrate data from
all these different locations into a singular place. In today's session, universal
data connectivity with ETL and SQL queries will show you how you can transform your
data and make it actionable. How you can simplify the data pipelines with AWS capabilities such
as AWS Glue, zero ETL, and Federated query so that you can get actionable
insights from it faster. We'll show you how we help
the customers eliminate ETL bottlenecks, accelerate data ingestion and maximize return on
their data investments. So you are up for a ride. Quick show of hands, how
many of you are using variety of operational databases and
enterprise applications today and are having to stitch it together? Correct, all of us have to do that. So why is this important? This is because there is a
fundamental challenge when we have to tackle all of this. In today's organization, everybody says they
have to be data driven. Now this is not just a buzzword anymore. This is important because we need to get to
actionable data faster. We need to understand what
are the market changes and how do we understand
our customer deeply. These all are critical for growing our organization needs. Here is a fundamental
challenge that we have. All of our data lives in different silos. The data that we have is
stored in different systems, all in different locations all together. Sometimes even in
different cloud providers or on premises data centers. In addition to that, we
have different personas who are using this data. Now, a new trend that's
accelerating right now that we are hearing from
our customers is convergence of analytics and AI ML workloads
on the same kind of data. So your data scientists
need access to the same data that your data analysts
have, which they are using to build dashboards. The AI ML models are
built on the same data that feeds into your real
time analytic systems, which makes it additionally more complex. So you might be wondering what does this complexity
look like in a real life enterprise environment? Let's take a look at that. As you can see over here
at the bottom we have bunch of data sources, finance,
telematics, customer experience, manufacturing, sales, product quality. Each of these systems are
generating mission critical data for our organization. In the middle we have our data lake, which host the raw data sets. Then all of your structured
data is sitting on your data warehouses. You are using AWS Blue catalog to do the metadata management. You have transformation
engines such as AWS Glue, AWS EMR, and then your query
engines such as Redshift, Amazon Athena. And then last but not
the least, you wanna run AI ML on top of it. So you are using AWS SageMaker or Bedrock. Now this makes it complex. The additional piece of complexity where it comes into picture
is all the different personas who are accessing the systems. Your data scientists are
creating the ML models. Your data engineers are
building the pipelines. Your data analysts are
creating the dashboards. Your data stewards are
managing the governance and your data owners are managing access. Now this is just one piece of the puzzle. We are not even scratching
the surface about third party data integration or even marketplace integrations. All of this makes the data
mumbo jumbo more complex and more critical to navigate. We do have a solution in mind and which we call the universal
data connectivity approach. At AWS, we are taking a
look at it very differently. We believe there is no one size fits all. Different scenarios require
different tools, different level of controls and different trade offs between flexibility and simplicity. What we have built is a unified
data connectivity strategy. What that means is purpose-built tools and solutions so that your user
personas can utilize it for what they need at that
given point of time. To make this concrete, I'll introduce to a user persona over here. One of our customers,
Alex, he's a data engineer. He works for a large enterprise. He is familiar, he knows his
way around ETL pipelines. He has deep, deep, deep spark expertise. He can work with multiple data sources at any given point of time, but he's always struggling
with similar questions. How can he drive value
for his organization? How can he connect to all of
these data sources seamlessly? We are talking of dozens if
not hundreds of data sources and what tools can help him
simplify this data pipeline so that he doesn't have
to build deep expertise for every new tool, every new technology that he's gonna use? So let's look at what Alex's
environment looks like. Alex today is using Snowflake
for historical data analysis for one of his use cases. The company's CRM data sits on Salesforce. The other operation data sits on SAP and service IT data sits on ServiceNow. All of these are different
disparate third party systems. In addition to that, he has all the AWS systems that he's using. Amazon Redshift serves his central data warehousing platform. Amazon S3 is his data lake, which is hosting raw
logs or structured data that he has created transactional
data that he has created. And in addition to that we
have Amazon RDS, Amazon Aurora, which connects the operational
database, which are fielding or running the actual
enterprise application on top. These are all different systems
that the data flows through, but it needs to flow through seamlessly so that we can build in the right insights that we are looking for. So what does Alex need
to accomplish with all of these different systems? Alex has three tasks
that he has to achieve. First, creating ETL pipeline to ingest data from multiple sources. Now all of y'all are
familiar with this is bread and butter of data engineering, extracting data from multiple
sources, polishing it, transforming it into usable format, and then loading it into
source destination systems. It's foundational work, but it is time consuming and complex. Second, reducing the operational load of managing the data ingestion pipelines. We talked about, right? How can it drive value faster
every time he is building in net new applications or net new pipelines, he has
to manage it, he has to fix it if something goes wrong,
that is frustrating. You know, schema changes,
add new pipeline in, et cetera, et cetera, et cetera. And last but not the
least, ad hoc request. We have all been in these shoes, right? Our VP comes in and we are looking for
combining data across multiple different sources that he needs
answers to like yesterday. We have to quickly put something together. The data analyst comes in and they are asking for access to run like a single query
at one given point of time wherein the infrastructure
may not be even used at any given point of time. So these are all the tasks that Alex is struggling with today. AWS provides three distinct patterns to address each of these needs. Let me show you our
comprehensive approach. AWS what we call is universal
connectivity options, right? So there are three options. Self-manage ingestion
using AWS Glue connectors manage data ingestion
using AWS's zero ETL, and inplace data access
using federated queries. Each of them have their unique benefits for unique use cases. First, for teams who want control over their pipelines and want customization, AWS Glue connectors is their go-to shop. We have built over a
hundred pre-built connectors for y'all to AWS and
third party applications. Manage data ingestion. If you wanna pipeline, but you don't want to manage
the operational overhead with respect to this
pipeline with zero ETL, you select the source, you
select the destination, and AWS takes care of the
managing of that entire pipeline. You don't have to worry
about maintaining it or anything of that sort. And last but not the least,
you have data where you need to query it on ad hoc basis or there is data that shouldn't be duplicated
across multiple systems because of security reasons. Or last but not the least, you are actually combining
data across multiple systems. For this, we have in-place data access using federated query. Now each of these are available for you. Now let's dive deep into
each scenario one at a time. For the first one, we utilize AWS Glue. AWS Glue is our serverless
data integration service that thousands, tens of thousands of customers are utilizing today. What makes Glue interesting? Glue is an all-in one
data integration service. You wanna manage the data quality, know what are the anomalies
associated with it. You wanna have the data catalog so that you can query the data, you know where the data sets are available and they're searchable. All of that is available with Glue. It's cost effective
because it is serverless. No need to deploy infrastructure. You will only pay for the infrastructure that you use based on the
jobs that are running. This allows you to scale
from gigabytes to petabytes and only paying for what you utilize. It's tailored to support
all of the data users. Your data analyst who are not
used to like coding languages. They're used to more UI
based infrastructure, they can use the visual infrastructure to build pipeline without utilizing code. You have data engineers who
are familiar with Python Scala and wanna do in-depth customization. Great, they can use AWS Glue. Or you have data administrators who are actually more comfortable with SQL for you doing transformations, et cetera. Perfect. They can use AWS Glue too. So it gives you tailored tools for each of these different user personas. And then last but not the least, it supports all workloads in one place. Think about traditional ETL, modern ELT streaming data ingestion
or batch analytics. All of that is possible with AWS Glue. So one stop shop for y'all. What makes this more
interesting is the diversity or the depth of the platform
that's made available for you and how have we done that? We have done that with
hundred plus data sources that are available for you. These are prebuilt connectors
that are available, which not just showcase, you
know, it's not just a number. This is years of engineering
effort that's made it possible to virtually connect any
source, any destination in AWS or in third party applications available to you at your fingertips. Then have three types of
connectors, native connectors. These are the ones which
are managed by AWS. They are prebuilt, they are
maintained, they are updated. Everything is taken care by AWS for you. We have custom connectors. If you have unique requirements, if there are unique transformations that you wanna do on the
platform, on the pipeline, you can build your own
connectors utilizing AWS's SDKs and it's available for you. And then last but not the
least, marketplace connectors. These are connectors that
our 3P partners have built so that you can utilize them and connect to multiple 3P sources that are available out there. Managed catalogs, these are fascinating because utilizing managed
catalog you can use, you can manage catalog utilizing Amazon S3 or Redshift Managed Storage to create Apache iceberg tables directly. What that allows you is the modern open for table format accessibility
directly on your platform, asset transaction, time travel. All of these need features available to you at your fingertips. And last but not the
least, reliable and secure. Encryption at rest, encryption at transit. (indistinct) based access controls so that your authentication and
authorization happens seamlessly and all the data sits in
your VPC control so that the data doesn't leave
your private network. So this is what AWS Glue
connectors have to do. Now let's see how Alex
can utilize everything that we talked about to actually solve his first
use case that we said. Alex wants to enrich and
unify his customer profiles. Now he's using two key systems. In SAP, he has his
operational data, which has purchase history, payment
terms, credit limits, et cetera. In Salesforce, he has
his customer profile. So all the sales data,
all the sales transaction, the tickets that were
opened by the customer, et cetera, et cetera. What we are able to do over
here, what Alex is able to do over here is utilizing
AWS's Glue connector connect Salesforce to AWS Glue and the connector takes care of all the Salesforce API integration. He doesn't have to worry about pagination or anything of that sort. The Glue connector takes care of the entire overhead associated with it. Same thing for SAP. Just plug in this SAP connector and plug it in into Glue
and that's about it. All the API level transaction
that needs to happen, that's gonna be taken
care by the connector. You don't need to learn a net new API for these 3P solutions on your own. So that's that. Now the best part about
it is utilizing AWS Glue, Alex can look for anomalies. Is this the right email address format? Are these the right ages?
Does it look fake or not? Are these the right amount? Do I have any negative sales
amount associated with it? Why is this important? This is important because you
can catch anomalies in your pipeline before they even reach your analytics platform, right? So fewer surprises down
the road making the life of all the other user
personas that are going to use this data much, much easier. Finally, Alex will use the aggregate. Alex can use AWS Glue to aggregate and join all of these data together to create a unified portfolio. And then that data is
available on Amazon S3 as iceberg tables so
that it could be queried by any analytics platform or it's available for
any AI ML application. This entire pipeline is
serverless, scalable, pay-as-you-go model. And we are constantly making this better. Let me show you how. Right now we have 60 plus connectors just to 3P solutions, right? So we are talking about Salesforce,
Xandex, SAP, ServiceNow, Google Ads, and on and on and on wherein we take care of all the connectivity platform for you. We are making it better. Just in the last quarter we
added 20 new connections. Just to call out few over here, Datadog. Think about it. You can use your
application monitoring data and see how does that apply
to my business utilization? You have Okta integration.
How is my user interaction? How long are my users
interacting with my application? And does that influence the sales that I'm doing within my platform? Adobe Analytics, all the top of the funnel marketing
activities that we are doing, how are they influencing our sales? And last but not the least, Asana, how is it that my organization operates? How do we project manage, which
projects are actually moving the needle for my organization? All of this available to
you at your fingertips. All of these new connectors are run with standard industry authentication
methods such as O2.0 so that you don't have to
worry about storing credentials in files or anything of that sort. Everything is automated in
the system accessible for you. It just works securely and reliably. With this connectors, customers
can test the connection, validate the connection, and then browse the metadata as needed. And so to close off this journey, let me tell you about a customer use case. Vyaire Medical, they are
a respiratory care company headquartered in suburban Chicago. They deliver respiratory
care products to hospitals and healthcare providers worldwide. It's like any other healthcare company. They had the same challenge. All of their operational
data sitting in silos in multiple places. They have data sitting in SAP, JD Edwards, ServiceNow, Salesforce,
et cetera, et cetera. They need to be able to get all of these disparate data
sources together so that they can understand
their customers better. They can do inventory management better, they can do their sales management better. How are they able to do that? What they did was they utilize AWS Glue and AWS's Glue connectors to pull in all of these disparate data sources together and point them to AWS's
Lakehouse architecture. Over the period of eight months they were able to transform hundreds of jobs, ETL jobs from
their legacy ETL tool into AWS Glue. And they had huge, huge benefits. We are talking about 50%
cost savings compared to their previous solution. Now that's not something easy, that's a fundamental
difference with respect to their cost structure. Imagine the savings over there. But the key thing was
actually allowing the, improving the developer productivity for their data engineering team. These data engineers
who used to take weeks to create net new pipelines
are able to create in days. Previously to get net new
analysis, which used to take days, it takes add the best
hours for them, right? This is the kind of
fundamental operational and productivity change that
AWS Glue was able to deliver for our customers and
which we can do for you. So we have discussed
Alex's first challenge, building ETL pipeline,
but don't forget about it, he has two other challenges
that we discussed, right? So for that, I'm gonna call
my colleague Shrey Malpani who's gonna come here and talk to us about
how Alex can solve that. Shrey. - Thanks Shruti. So using the AWS Glue connectors, Alex was now able to
simplify his ETL pipelines. Now his next goal is to keep his analytical data in sync with operational databases
without adding much of an operational overhead on his head. His current ETL pipelines
run on an hourly basis, so any data that he gets access to in his analytical systems
are at least an hour old. He's also responsible to
maintain the pipelines and ensure the reliability of them. Now, just like all of us, he hates getting pinned paged
at 2:00 AM in the morning because something broke
in his data pipeline. So he's thinking to
himself, I need a solution that can keep my analytics
data current without having to implement complex change data systems, which bring in the additional overhead. And this is where AWS
zero ETL can help Alex. Before we dive into what AWS zero ETL is, let's look at the typical
requirements that will be needed if you are running your
own data application and ingestion shops. You might have data
stored in multiple sources and may need to apply certain business
logics which are specific to each of those sources. You might also need to implement
some complex retry logics to ensure that the pipeline does not break because of some transient errors. You would also be responsible
to maintain the infrastructure and monitor the pipeline to ensure everything is running smoothly. Plus, you'll also need some
specialized ETL skill sets to make sure that the
pipelines are running in the most optimal manner. At AWS, we understand that all of these requirements can make the task of replicating data from
multiple sources for the simplest of use cases, very complex. And hence, we are investing
in a zero ETL future. AWS zero ETL is a set of
AWS managed integrations that allow you to ingest data
from multiple data sources without having to build an ETL pipeline. You can ingest data from multiple
transactional, operational and enterprise SaaS application sources. With zero ETL, you can
get access to fresher data for your analytics, AI ML applications or reporting use cases. Now, you may be thinking that AWS already offers
multiple ways in which you can operate your data pipelines and ingest data in your
analytics data warehouses and data lakes. Like we discussed earlier, you could use Glue ETL to build and maintain your own ETL pipeline. You could use visual ETL to get a no-code low-code interface, or we offer other services as well where you can operate your ETL pipelines. So what is so special about zero ETL? Well, zero ETL is a purpose
built AWS managed capability that helps you operate and ingest data from
multiple sources in a simple and secure way. Where you just have to
create the integration once and then we take care of the rest. It's also highly performant and delivers data from multiple sources to your target systems
within near real time lag. So say you have zero ETL
integrations from Amazon Aurora or Amazon RDS to Amazon Redshift, any changes on the
source will be replicated to the target within a few seconds. And for other sources, these changes can be
captured within minutes. What this means is it
reduces your time to insight. Zero ETL is also very efficient and it runs with minimum
disruptions at source. And finally it has the
right mechanisms in place so that you can trust zero ETL
to replicate data accurately to the target systems. You could leverage encryption mechanisms. You could operate the
zero ETL integrations in your VPC systems and ensure
the security of your data. Now many of you and other AWS customers
have shared feedback with us that you want your end
users of the data warehouses and data lakes to be able to ingest data from multiple sources and use them in the analytics
engine of your choice. These end users may not
always be data engineers. They could be data analysts who lack the specialized skill
sets that are needed to build and operate data pipelines. With zero ETL our goal is
to enable these end users with a no code and
managed capability so that ingesting data from
multiple sources becomes a transformational experience for them. Now let's take a look under the hood and see how zero ETL works. We look at an example where say you have to ingest data from an
Amazon Aurora database to an Amazon Redshift database. You might want to capture
the initial snapshot of data from Aurora into
the Redshift database and then periodically capture any changes that are made into Aurora and have them reflected
in the Redshift database. In this case, Aurora becomes your source and Redshift is your target. Once you set up a zero ETL
integrations between Aurora and Redshift, it starts
with an initial load of the full snapshot of the data. So it creates the table on the
destination Redshift database and creates the corresponding data types to match the source without you having to write a single line of code. After the initial load is done, it starts capturing any inserts, updates or deletes in near real time and reflects them in the target database, Amazon Redshift in this case. So if a new record is
added to your Aurora table, zero ETL will add the same record in the Redshift database as well. In case you drop the column, the same will be reflected
on the target database in near real time. That is the simplicity with
which you can operate zero ETL. You just create the zero
ETL integration once and then we take care of the rest. Let's look at a demo, which
will show you how simple it is to create zero ETL integrations. In this case, we will create
a zero ETL integration from Salesforce to Redshift. A prerequisite for setting
up this integration would be for you to create an AWS Glue
connection to Salesforce, just like Shruti mentioned earlier. So you could navigate
to the AWS Glue console, click on zero ETL tab, create
a zero ETL integration, select Salesforce as source, click next, select the right connection,
provide the IM role that has access to the Salesforce data, and then you can start filtering
on the multiple Salesforce objects that are available. This is very helpful when you
don't want to replicate all of the data from Salesforce, but want to limit it
to the specific objects that are relevant for your use cases. Once you have made all the selections, you have the capability to
review the data as well. This gives you an opportunity
to check everything looks as it should, before it's
too late in the system. Now that the source is configured, you provide the target details. In this case that would be the Amazon Redshift data warehouse. Now that the source and
target are set, click next and you can now configure the integration. You could provide the encryption keys or modify the replication
intervals for change data capture. You could also add the integration name, let's say we call it Salesforce
integration in this case. And click next, review all the details. And finally, if everything looks good, click on create. It'll take a minute or
so to set everything up and notice how in this case
it prompts us that we have not yet created the Redshift database where the replication should happen. So just with a click
here without navigating to a different console, you
can create that database. Let's say we call that
database as Salesforce db. Click on, okay, and it's all set. If you go to the Redshift
console, you can see that the zero ETL
integration is now active. The new database that we
created is also active, and you can quickly start querying that data in the Redshift Query Editor. So if you look at the databases
that you have access to, you would notice that it shows
the Salesforce DB database that we just created, and it
has four different tables, each one corresponding to
one object that you selected while configuring the source, start writing your queries
and get the results. You could also dive into
the integration metrics and look at the data
that has been transferred because of this integration. You could also check the status of each of the tables individually and figure out if any step is needed to debug any errors
that might have come up. Such is the simplicity
of setting up zero ETL and just within a few clicks,
without writing a single line of code, you can start ingesting
data from multiple sources into the analytical
systems of your choice. So now that we understand how to create zero ETL integrations, let's look at what are
the different sources that you can ingest data
from using zero ETL. This year, we have had its
support for 11 new sources for zero ETL integrations, and now zero ETL supports
23 distinct data sources. These can be classified
into three broad categories. The first one is AWS databases. You can create point to
point integrations from different Amazon databases
like Amazon DynamoDB, RDS for MySQL and Amazon Aurora. In addition, earlier this
year we added support for RDS for Oracle, RDS for PostgreSQL and Oracle database at AWS
for zero ETL integrations. The next category is third
party enterprise applications. You can create managed data
ingestion using zero ETL from eight different SaaS
applications including Salesforce, SAP, ServiceNow, and Zendesk. And finally, last week we
launched a whole new category of zero ETL integrations
from self-managed databases. So you can create zero
ETL integrations from MySQL databases, PostgreSQL, SQL Server, and Oracle databases, which
are either hosted on premises or on EC2 instances. So that's eight additional sources. If you are creating zero ETL integrations to Amazon Redshift, you
can ingest data from all of these 23 different sources. Alternatively, if you want to ingest data in your
data lakes in Amazon S3, you can do so from 12 of these 23 sources. You can create integrations
from Amazon DynamoDB. And earlier this year we
also launched support for RDS for MySQL and Amazon Aurora databases to create zero ETL
integrations into Amazon S3. In addition, you can also ingest data from the SaaS applications that
we discussed about earlier. Now, another thing in addition
to the different sources that we launched this
year is a whole new target Amazon S3 tables. For those of you who don't know, Amazon S3 tables provide
S3 storage that is optimized for analytics workloads. It has features that are designed to continuously improve
performance on tabular data, and it is ideal for storing tabular data, which may include
transactional information, your sensor data that are
being stored in tabular format or other forms of tabular data. You could ingest data into
Amazon S3 tables using zero ETL from Amazon DynamoDB or the
eight enterprise applications. So now that we understand
the scope of zero ETL, let's go back to our friend
Alex and evaluate his situation. The sales team in his organization
is trying to understand what is the revenue coming from some of the top opportunities
that were identified earlier. Now the revenue or sales data is stored in Amazon Aurora, and the opportunity information
is available in Salesforce. The sales and marketing teams want to build a customer lifecycle
model using data from both these sources and also create reports on some of their top accounts. So the task for Alex is to integrate data from these sources so that the marketing team is able to achieve both these outcomes. Now, Alex thinks that he can build an ETL
pipeline to achieve this outcome. He could take a streaming
approach just like the one shown at the top of the screen and
start ingesting that data. Or he could build a pipeline that looks like the
one shown at the bottom and have a batch integration approach. But his existing pipelines
are already taking up most of his time, so he does not
want to add an additional burden of managing these new pipelines. He turns to zero ETL instead. He sets up a zero ETL integration
from Aurora to Redshift and then another one from
Salesforce to Redshift with just a few clicks
like we discussed earlier, and just like that in a matter of minutes, the data from these two
sources automatically starts flowing into Amazon Redshift, and this is available in
near real time for any of the analytics needs
for the marketing teams. For Alex, zero ETL means
eliminating an entire category of pipeline maintenance work. AWS takes care of the replication
of any schema translation and error handling, and
Alex can now invest more of his time into business critical tasks. So Alex was able to achieve
two of his outcomes now. Before he move to his third task, let's look at what are the
other new things apart from the sources and targets that
we discussed about that we have launched in zero ETL. The first category is features that provide you more
control when creating zero ETL integrations. We've added support for on
demand ingestion using zero ETL for cases where you want
to ingest full snapshot of data immediately. We have also added
support for history mode for zero ETL integrations
into Amazon Redshift, which preserves the history of any changes made at your source within the Amazon Redshift databases. This allows you to track and analyze any changes in
Redshift itself rather than having to go to the source
to track those changes. Second, we added features
for more flexibility when you are creating
zero ETL integrations. You can now customize the refresh interval when creating zero ETL
integrations from SaaS sources between 15 minutes to six days. You can also create up to five integrations from
an Amazon Aurora cluster to your Amazon Redshift data warehouse, and this could be to the same
or different data warehouse. You can also now ingest
data from Amazon Aurora PostgreSQL tables that have declarative partitions. And finally, we improved observability for zero ETL integrations and started logging the client errors into Amazon CloudWatch logs. This will help improve the debug ability of zero ETL integrations. As we wrap up zero ETL, let's
take a look at a case study of one of our customers, Pionex. Pionex is a crypto exchange and wants to use the latest
market data to deliver insights to their end users. It is critical to deliver these
insights on the latest data so that their users can
make decisions based on the latest data available. Earlier, Pionex used to
operate an ETL pipeline managed by themselves, which led
to a lag of 30 minutes. This meant that any
insights that were delivered to their users was on 30
minute old market data, and this was a key blocker for them to deliver the best experience
for their end users. They shifted to zero ETL and since that shift, they have seen 98% reduction in latencies, 80% reduction in maintenance costs, and 66% reduction in overall
operational overhead costs. Such is the impact that zero ETL can have on your workloads as well. In the words of senior director
of data analytics of Pionex, "Zero ETL has helped them
achieve real time access to their operational data, something that was not possible before." So now that we understand the benefits that zero ETL can deliver
for our use cases, let's go back to Alex's tasks. He has simplified his data
pipelines using connectors. He has eliminated a lot of his operational
overhead using zero ETL, and just as he gets his
pipelines running smoothly, he realizes there is a whole
different category of requests that he received that he
has not addressed yet. These are typically ad hoc requests that come from his leadership, and more often than not, they're required in a matter of hours. Now, Alex wonders in those scenarios that there's just no time to
build a new data pipeline. How can he deliver those analysis and insights in the timeline
that has been requested? This is where federated queries
can come to Alex's rescue. Federated queries provide on demand access to data from multiple different
data sources into a single query without having to
move a single bite of data. With federated queries
there is no need to build an ETL pipeline at all. You can analyze data
directly where it lives and write a single SQL query which accesses data
across multiple sources. We offer federated queries
in both Amazon Redshift and Amazon Athena giving you flexibility to choose the right querying
engine based on your use case. You can query and analyze data stored in relational, non-relational object or any custom data sources
and write a single query to get near real time insights
from the different data sources where a data might be located. This approach works perfectly
for ad hoc analysis, for data exploration, for cases where you might have sensitive data, which cannot be replicated
at multiple locations or scenarios where you are trying to optimize your storage
footprint without having to store multiple copies of the same data. Let's see what all can you
achieve using federated queries. Today we support 30 plus
federated connectors and you can connect to
transactional databases, say MySQL or PostgreSQL databases and AWS databases like Aurora and RDS. You could connect to other storage systems and data warehouses and
data lakes like Amazon S3, Redshift and Snowflake. You could also connect
to multi-cloud systems, like Google Cloud Platform
or Microsoft Azure. You could choose to connect to enterprise applications like SAP or any big data platforms like Cloudera. Let's take a look at how
it works under the hood. Say you want to use Amazon Athena as your centralized querying engine, and your data is stored
at some of those places that we discussed in the last slide. You can use Lambda based
connectors available in Athena, which will use Lambda functions to access data across these
different data sources. So you could either query or process the data
from these data sources. You could read the schema or
get the records themselves and modify them to achieve the desired analysis that you want. Once the analysis is received
from the federated query, you could decide to
generate an ad hoc report, create a visualization, or store the output
persistently in your data lakes. And that way you are not
copying the whole of your data, but only the analysis that has been generated from the query. Let's take a look at
setting up Amazon Athena federated queries using
SageMaker Unified Studio. If you go to SageMaker Unified
Studio, go to the data tab and in your lakehouse click
add to add a new data source. You can select, okay, sorry for that. You can select the data
sources and provide the name and provide the credentials
that will be required to access the data in the query. You can also do the same for other sources and evaluate the data or preview the data from a single source. You could also go you the
SageMaker Unified Studio Query editor and join data across
multiple data sources that are available in your lakehouse. This will result into the
analytical outcomes that you want to achieve within a
minute without really have to replicating the data into
your analytical systems. Now, now that we have
set up federated queries, let's see Alex's situation. Alex has recently received an
email from his VP of sales, and the ask is that they want to understand the customer
tickets that are raised by their top customers. To do that, Alex needs to join
data from Amazon Redshift, which has the customer size
information, Amazon RDS, which has all the customer orders and SAP where all the customer
service tickets are located. Alex writes a single query to integrate data across
these three different sources using Amazon Athena Federated Query and gets the output within minutes. He can then store the output in Amazon S3 or visualize it using Amazon Quick Suite. And just like that, he has
the output that the VP wanted. So in this manner, he was able to achieve the ability to say yes to any ad hoc requests rather than having to explain why it'll take days or weeks to build a new ETL
pipeline and replicate the data. Now let's take a look at what is new with Federated Queries this year. Earlier this year, we launched support for
OAuth authentication mode for Snowflake connections. This mode uses authorization tokens and refreshes the tokens automatically, which makes it perfect for
long running federated queries. With federated queries, you
can also leverage the multiple performance enhancements
that we have introduced to our query engines. This includes enhancing the querying speed for common file formats, generating outputs quickly
when the query results are more than a hundred mbs and expanded DDL support for
iceberg tables and S3 tables. And finally, we also launched
managed Query result storage, which allows you to store the outputs from
your federated queries in an AWS managed storage
for up to 24 hours free cost. So given that we have looked
at all the three approaches that we started off with,
let's quickly wrap up and understand how these
approaches can deliver value. Let's take a look at
Alex's situation again. By leveraging these
connectivity approaches offered by AWS strategically, Alex was able to transform his data architecture. Complex custom pipelines
have now been replaced with AWS Glue data pipelines that leverage AWS Glue connectors, and that provides him control as well as pre-built functionality. Critical operational data
now flows automatically using zero ETL integrations and minimize Alex's operational overhead and maintenance work, and any
ad hoc requests are handled through federated queries,
minimizing the need to build new data pipelines. For Alex, this means that he now spends much less time dealing with data connectivity issues and focuses his attention on
business critical insights. Just like Alex, you don't have
to choose just one approach. The most effective data
strategies combine all these three approaches together. When you need complete control
over your data pipeline, you can use AWS Glue connectors for self-managed data ingestion. When you want to focus on insights and not infrastructure, you can leverage AWS zero ETL integrations for a managed data ingestion experience. And when speed and flexibility are key, you can leverage federated queries for in-place data analytics. I encourage you all to
pick just one use case and apply these strategies. You could start with creating a Glue ETL job using connectors. You could start with creating your first zero ETL integration or writing your first federated query. If you want to learn more
about any of these topics that we approached today, you
can refer to these resources. The first QR code will
direct you to a blog that will help you get started with creating zero ETL integrations. And the second one here
will take you to a demo to set up federated
queries in Amazon Athena. In addition, you can refer
to the AWS Developers Guide to learn more about any of the features that we discussed today. You could also visit AWS Skill Builder to leverage the Abundant Learning
Resources available there and even practice with hands-on exercises. With that, I would like to thank you for being such a great audience. Please take time to share
your feedback on the session using your mobile apps. Shruti and I will be available
right outside this area to answer any questions that you may have, and given some of the other
sessions are still ongoing and their silent sessions,
I request you to be mindful of them while moving out. I wish you have a great
reinvent ahead. Thank you. (crowd clapping)
---
video_id: kWPrlsHErUM
video_url: https://www.youtube.com/watch?v=kWPrlsHErUM
is_generated: False
is_translatable: True
---

- All right. Good morning everyone. Welcome to re:Invent. How's your morning? - [Audience Member] Great. - Awesome. All right. Today we're standing at a
turning point, an infaction point that AI drive, and then changing
the whole analytics world. So in today's session,
we're exactly talking about how we are building a
robust data architecture to adapt to that world, to
power your enterprise AI, and then BI workload. My name is Emily Zhu. I'm a senior product manager
from Amazon Quick Suite. Together with me on the stage will be my colleague Thomas Schlosser, a solution architecture manager from AWS, and our guest speaker,
Kevin Kamau from Basware, as the director of Product Manager. Let's get started. All right, this is where we
are headed for our agenda. We will first talk about the big shift of how we are building a data
foundation in the AI world, and then I will introduce our new platform of AI workloads called Amazon Quick Suite. Then we'll dive into the structured data, which is still the core
of our AI workload. My colleague, Thomas, will
talk about how we expand it to integrate unstructured data and the applications as the data sources. At last, Kevin will talk
about exciting use cases of how Basware build that
foundations in practice. All right, let's get dive in. Since the invention of the
dashboards from 20 years ago, BI always has been in the
center of analytics world. People using BI to build insights and then making informed decisions. However, the rise of AI technology changes the whole architecture. Now we want to see how we adapt to that. In the BI-driven architecture, people always start with
predefined dashboards and then questions. The metrics logics are
always defined by human, and the result of those
BI dashboards are used by human as well. They interpret it, making decisions, and all those computing
are defined to power that, but that computing is
powered to enable human use. So it's fine to be batched. However, the AI technology
makes all those transition for the technology. AI need to use an open-ended multimodal and then dynamic reasoning. AI need to understand the
semantics of your data context, not just the data itself, but
the meaning of your business. The agent will need to
generating and executing the analysis instead of people
interpreting the results. So the computing to power all of those capabilities really need to be high-scale,
low-latency, and in real time. So with that context in mind, let's see what we can carry over from the current BI
foundation architecture. We probably will still relying
on the existing data storage and the schemas, enterprise
entities, identities, access controls are still super critical. We still need to rely on
the data pipelines, catalog, lineages to enable trust
and then governance. Curated business definition and the metrics are super important still because it evolves as
companies define them. Last but not least,
dashboard will not disappear, because that is still for
what human to communicate, and then to share their
insights and then decisions. As we are stepping into the AI world, there a lot of portion of our
architecture need to evolve. First one is your data
should not be siloed. You will need to connect
all your enterprises data so AI can inform across all
the business and systems. Similarly, your knowledge
should not be localized. You need to define some centralized
semantic knowledge graph so that AI can generate consistent context across business and systems. Workflow, as we said, doesn't
work if they're batched. We need to build continuous
event-driven data pipelines. Governance should be really scalable. Instead of manual defining
user access controls, we need some automated
policy-driven controls. Last but not least, analysis are not just
for human to trigger. We need to build some workflows
that really automate it, and then using the AI agents
to help driving the workflows. With that context in mind, I would like to introduce
Amazon Quick Suite. I would like to do a quick
survey of our audience. How many of you have heard,
or used, Amazon Quick Suite? All right, this is awesome.
This is a great start. So we launched in October the
9th of Amazon Quick Suite. What is it? It is a set of agentic teammates that will access all your enterprise data, quickly answer your questions at work, and help you turn these
answers into actions. Let's see what Quick Suite can do. It provide a series of AI workloads and capabilities targeting
on different use cases. First one, we have a
native chat bot experience to provide you conversational experience that you can ask questions
against your enterprise data. And then you can also
customize your agent, build on top of it, to
share with your teammates. We have researchers that will allow you to do very deep-dive analysis
and then be able to generate and export a report to
share with other people. We have QuickSight as
the core BI capability that we enhance with AI technologies, help you to build even
more beautiful dashboards and analytics. Now, given the first three, we have two capabilities
that will help you to build your workload,
workflow more automatically. The first one is called Flow. It is targeting on the
non-technical business user to be able to automate your
flow for your repetitive works, and then predefine some steps to replace the time-consuming manual work. The next one is called Automate. That one is targeted on
more complex problems and enable organizations to transform the entire business process
into an automatic workflow. So those are the AI capabilities that we offer from Quick Suite. Behind the scene, this is the data foundation
that unlock those. Click into the data foundation.
There are major two layers. The bottom layer are the data
layer that will allow you to access the world knowledge, also access your structured data, unstructured data, your uploaded files, and then your actions across
your third-party applications. On top of the data layer is
the governance piece of it. We provide access control,
guardrails, responsible AIs to govern, and then
secure your usage of data. Now with that, let's dive into how structured data unlock your workload. It still is the core
fuel for AI workloads. And then that is mostly
focusing on the tabular form of your data in uploaded
files or data sets, and then how we access control,
the usage of those data. So let's first take a look at how the data flow look like when
user start their journey with the structured data sources. You bring your data sources. Your data sources can
come from your database, data warehouses, data lakes, it can come from your applications, it can from your local or S3 file imports. When you want to use them
in Amazon Quick Suite, you connect through a governed connector, create the data sources. After that, you can define
the schema of your data, and then create the so-called data set. That is the queryable object
in Amazon Quick Suite. You can create a data set that be able to directly run query in your SQL sources, or you can give data to SPICE, which is the proprietary data
engine of Amazon Quick Suite that provides you high
performance, low cost, and auto- scale capability. After you define the data sets, you'll be able to author them
into a dashboard or a topic. In this step, you'll add more semantics, and then business context to them to get it prepared for your AI workload. After that, when user coming in and enjoy the applications
of Amazon Quick Suite, your data is behind
all those applications, including scenarios,
stories, chat agent flows, and then researches. So having that in mind,
let's take a look at what are the deliverables
that we delivered this year to enhance these foundations
and then make it even powerful? First, let's start with the
core of our analytics stack, the SPICE engine. We have done a whole re-architecture with the open source Apache
Iceberg and Apache Spark this year to (speaking
faintly) powerful SPICE Engine. Given that capability, we are providing a much
larger data set size, double the data size from one TB, 1 billion row previously,
to 2D TB, 2 billion rows. Now you can enjoy a much
larger data set ingested into SPICE. At the same time, we're
improving the performance of SPICE Engine by increasing
as much as 2.5 times of the ingestion speed
and then query speed. Now getting data into QuickSight makes Quick Suite is much easier. We launched the reimagined
data preparation experience this year, allow you to be able
to see a whole step-by-step data preparation of your
data transformations. You don't need any code for SQL, you don't need to write Python or SQL. Instead, you can see a map of step-by-step by just click, and drag and drop, to manage your data transformation. We also allow APPEND,
Aggregation, PIVOT, UNPIVOT, and then LIST AGG the new
transformation capabilities. The collaborations is more easier because now we are allowing 10 levels of using already created
dataset as your data source to (faintly speaking) of your data. Instead of only working
on the capabilities within Quick Suite, we also
do a lot of integrations with the whole AWS Eco-system. The biggest one that we
launched this year was the integration between Amazon Quick Suite and Amazon SageMaker Unified Studio. Now if you are landing in Amazon Quick, Amazon SageMaker Unified Studio, and then manage your data, you'll be able to transfer
into Amazon Quick Suite by just one click of creating a data set from SageMaker Unified Studio. For instance between the two system having corresponding concept
so you can easily switch back and forth between the two system if you want to manage your data. Last but not least, the data governance layer
is being more comprehensive. Previously you'll be
able to share your asset through the folders, through
the restricted folders. You'll be able to log
in using your IAM roles, and then creating data sources
of Redshift and Athena. You'll be able to create
role-level security, column-level security
in Amazon Quick Suite. And then this year we allow
this whole integration of Lake Formation and enable
trusted identity propagation through that capability. When user log in Amazon Quick Suite, their identity will be propagated. And then the rules, the
fine-grain access control rules that you define in Lake Formation will be automatically inherited
when you are using Quick in a very governed and
then access-controlled way. All right, by looking
at those capabilities with a strong foundation
for structured data now I would like to invite Thomas on the stage for the next section. - Thank you Emily. Thanks. So as Emily was just
saying, and as we've seen, now that how we can build
a scalable data foundation on top of your structured data, I would like to ask each of you to just think about the last time you had to make a big decision,
a really big decision, and now take a few seconds
to think about what type of information you needed
to make that decision. And I would kindly ask
you to raise your hand in case you needed additional information. For example, information
from other sources like your company document
repository or applications that you use in your day-to-day life. Can you just? I see plenty of hands
raised and I think that just shows how important it is
to go beyond structured data and to build a data
foundation that integrates all of the relevant data sources
across your entire business. So next we are going to look
at how Quick Suite allows you to establish a holistic view across your entire information ecosystem. Also integrating the document
and content repositories as well as the enterprise applications and services you're already using. As a very first one,
we look at the document and content repositories
such as the Confluences, SharePoints, and Google
drives that you already use within your organizations. Quick Suite allows you to integrate those through a concept called knowledge base. And knowledge base is
a searchable repository of information coming
from external sources. So what does it mean and what
is a knowledge base doing? A knowledge base is an
organized index collection of documents coming from
those external sources, that is optimized for
generative AI-powered information retrieval
and question answering. It provides the large language models with the rich contextual
intelligence to be able to provide trustworthy and
accurate AI experiences. And once they have been created, the configurable automatic
synchronization mechanism keeps them up-to-date. And the built-in access control
mechanisms of Quick Suite allow you to also configure
which user has access to information from which knowledge base. To tap into your
organization's knowledge coming from OneDrive, Confluence, S3 and more, the very first step you
have to do is to create and set up a data access integration, where you would configure the
integration-specific details, such as the connection or
account information as well as the authentication
required to access the system. On top of that, you can build one or
multiple knowledge bases to make that content, or specific content, also available for AI analysis. So in this step you would
choose which content to include from the external source. You can additionally also
influence the indexing behavior, define the refresh schedule,
and manage access permissions. Once that's done, Quick Suite
will process the content and adds it to the quick index. Quick Suite capabilities
such as chat agents, flows, and research will then be able to access the content once
indexing is completed. And as users intact with the agents, the agents will be able to
run semantic search on top of the knowledge bases as required, and combine it with the information coming from other sources such as
the structured data, web, or uploaded files to provide
the most relevant answers. Let's see it now also in action. So in this demo we are an
employee who would like to understand how many
vacation days we have per year. When we ask now the chat
agent, without pointing it to company-specific knowledge,
it will use web search and general world knowledge
from the large language model and will just tell us where this information
can typically be found in. So not very useful, right? So let's go ahead and
now add an integration to our policy documents
coming from Google Drive. So we go to the integration section and add a new data access
integration for Google Drive, where we first pick the
account that we want to use, and provide Quick Suite the permissions to access the files in Google Drive. Which kind of concludes the creation of the data access integration. Let's go ahead and create
our first knowledge base on top of that where
we pick now the folder, the policies folder and give it a name. Let's call it "Policy documents." And as we create that
knowledge base, Quick Suite, goes now ahead and starts the indexing. And once indexing is completed,
we can open chat again, and repeat the question from earlier. Now this time we will see that the chat agent is running
a semantic search on top of the leave policy document coming and originating from Google Drive, and it will tell us that we are entitled to 20 vacation days per calendar year. So as just seen, creating
knowledge bases within Quick Suite is a great mechanism to
improve the relevance and the accuracy of an agent's answers. However, some of you might
have already built indexes in other places. Quick Suite allows you also
to connect to external indexes such as the Amazon Q Index through a concept called
"Bring your own index." With Bring your own index, you don't have to recreate your index or upload the same data again, but instead you point to
the existing index to bring that one in and leverage
this within Quick Suite. And the knowledge bases
that you built on top of that can be used and
shared exactly in the same way as the knowledge base that
live within the Quick Index, all while maintaining
still the same security and access control from
the external index. So in case of the Amazon Q Index, Quick Suite users will only
be able to access the content from the data source of the Q Index that the users would
have permission to access in that data source, if
you configure it that way. But what if we need
real-time access to data or applications for our external systems? This is where actions come into picture. Action connectors within
Quick Suite allow users and agent to invoke real-time calls to perform actions in external systems. So by leveraging those actions, agents will be able to pull information to answer users' natural
language chat request, automate workflows, send notifications, or trigger processes in
connected applications. Action connectors basically
support two type of actions, on-demand actions and actions
in automated workflows. The on-demand actions execute immediately as users triggers them. So typically use cases would
be to create a Jira ticket or sending a notification on Slack, or updating Salesforce records. Actions in automated workflows
on the other hand side, execute as when they are scheduled, or in response to specific triggers. When it comes to the authentication method for those actions, they
also slightly differ. So for the on-demand actions, it requires user-level
authentication methods, such as managed 3-legged OAuth, or custom-user-based authentication, for scenarios that require
organizational control or custom configuration. The automated workflow and actions there, they require service-level authentication. So you can use methods such as API keys, or 2-legged authentication. Similarly, the permission
model also differs in the similar way. So with on-demand actions it leverages personal access permissions which are tied to the user's
identity in the target system. For automated workflows actions follow a service-level permissions. What both have in common is that again, you can in Quick Suite, leverage the access control
mechanisms to define which user or group has access to
execute specific actions. Quick Suite supports a wide range of popular enterprise applications such as Asana for project
management, Outlook for email, and many more. Also, if you have custom
applications, you can connect to those using custom
connectors that leverage either REST APIs, OpenAPI specification, or the model context protocol or MCP, which is a standardized
way to connect AI systems to external tools or data sources. The first party action connectors that allow you to connect to services such as Amazon Bedrock Agent,
Comprehend and S3, allow agents to execute actions
on top of AWS resources. For all of them to be able
to make them available to users or agents in Quick
Suite, the first step, what you have to do is, to
create an action connector. Depending on the action
type, you will provide the integration specific connection, VPC, and authentication details. And then on-demand actions that can be used in chat agents, flows, or on top of dashboard visuals, are those interaction or
interactive operations that users trigger and hence require at the first use, user sign-in. The system level and background operations such as automate runs
and threshold alerts, on the other hand side
don't require that step because those would be leveraging the system authentication
as discussed earlier. Coming back to our previous demo, let's now also integrate our HR system that the employees use to
manage their time-off requests. As our HR system offers
an API that provides an OpenAPI specification, we first start by navigating
in the integration section to the Action step. To then add a new OpenAPI
specification integration where we select the schema
to make the structure of the API visible to Quick Suite. Then we give it a name. Let's call it "HR System Integration," as well as a description. And then we can choose between the two different authentication methods. We choose User authentication because we want to use it in Church. Then we provide the integration, the authentication details here, get an overview of all the actions that we make now available
to the agent can share it with other users and groups. And once the action is
created, the action connector, we can open chat again, and now we can also ask questions such as, "How many vacation days
do I have left this year?" And once we ask the question, we will see how chat agent now identifies this stage HR system integration
that it wants to leverage. So it asks us at the
first use now to sign in. Given that we didn't sign in beforehand, it asks us now to provide
username and password. Once that's completed, we will see how the agent now uses the
GetTimeOff balance, API, to then tell us that we have
seven vacation days remaining for this year. So let's go ahead and ask
it to book now next Monday, the Monday after re:Invent off. So it will use web search to figure out when re:Invent takes place, and then it's using the create API, and ask us first to review
and validate that it's the 8th of December that
we want to take off. So once we submit this
form, the agent goes ahead, and is booking the time off on our behalf. And then we get a quick summary
of what it executed for us. When you build your data foundations, you also always should have in mind how it enables collaboration at scale. Emily mentioned earlier
that we have folders, which is a hierarchical
organization that allows you to share analytics assets at scale. In addition, Spaces serve
as a collaborative workspace that allow users to create
dedicated collections of data assets, files, and
actions to reduce data silos. As such, Spaces function
as custom knowledge hub for specific domains and teams. And as they're being shared with users, each person will be able to
access and collaborate within the space based on the access
permissions that they have. The spaces when being applied on, or used in agents, provide a
data boundary for those agents, to make sure that they
have the right context and operate within that defined context to provide the most relevant
answers and interactions. Let's now also go ahead and create a space for our HR domain. So we navigate on the
left side to the Spaces and click to create a new space. We first give it a name,
let's call it "HR Space," and then we could now upload files, or add existing resources. So let's go ahead and add our
policy document knowledge base as well as the HR system integration that we created earlier. Additionally, we also add
now the structured data. Let's add a topic about employee data, which includes the new hire start dates, as well as a dashboard
about our staff schedules and holidays. Once that's done, we can open chat again and by default it will now
automatically open in the context of that HR space. And we can ask more complicated tasks like "Book five days of vacation in December when no new hire starts so that we got the longest uninterrupted break." What the agent is now doing, it's using the resources
from this particular space, looks for the new hire start
dates from the employee data, the time off balance we
have from the HR system, and makes us a suggestion. So based on the new hire start dates, which are on 1st, 9th,
and 22nd of December, it asks us if it should book on our behalf the 15th to 19th of December off, because that would give us nine
days of uninterrupted break. If we confirm with yes, we will similarly, as we've seen it beforehand,
have to quickly validate that this is what we want to do. Once we submit it, it goes ahead, and books those five days of
vacation for us in December. So now that we've seen how
you can bring structured data, unstructured data and
applications together, and put it to work in your day-to-day life in the new agentic AI
world, let's hear directly from one of our customers. Let me invite Kevin Kamau
from Basware on stage who's going to walk us
through their journey of building a scalable data product on top of Amazon Quick Suite. - All right, super. Thanks Thomas. Hey everyone, my name is Kevin. I lead our data AI products at Basware. So to get us started,
and actually it's a story that I'll be telling, so
it's really a customer story. What, who is Basware, right? So Basware essentially is the world's leading invoice
lifecycle management provider. We help enterprises automate
their financial supply chain, and at the center of this
is something called AP, or accounts payable. So what accounts payable is this is a team that receives, validates,
routes, and pays invoices. So essentially ensuring that
businesses keep on operating. With this, every supplier,
every purchase order, every workflow will essentially cross AP. And what that means, it is very,
very operationally critical and at the same time produces
one of the richest data troves that you will see in
the finance enterprise. As Basware, we actually
are very, very honored and privileged to have a
really, really rich data set from our customer base. So we connect over 20 million
suppliers with our customers. We've processed over 10 trillion
in spend through our system and that essentially is
just to give you an idea of how much data we have had in place. Now Basware itself has
actually been around for a very long time, over 40 years. Interestingly, or as a note here, we actually invented the
invoice automation space. So we were the first ones to bring to the market something
called invoice automation. And we've been in this space for well over four decades,
right, so since 1985. More recently are moving to the cloud, and in the 2020s then getting
owned by a private equity. Now, I mentioned this a few
times that through this journey and through, you know,
the business that we do, there comes an enormous data footprint, billions of invoices, trillions of spend, and thousands of global customers, millions of suppliers globally. For us, the opportunity
here was rather obvious. If we could unlock this data, it would essentially
give our finance teams or enterprises globally superpowers. So let's take one step back. Our journey with embedded
actually started in 2016, and when we started, the
product was really, really well recognized in the market. So our embedded analytics product
was really well recognized in the market, very, very highly praised. And I joined Basware in 2017. However, and I'll take a pause here. When I joined Basware in
2017, this was August 7th, and I remember on August 9th I was put in front of a customer. It was a three hour call,
a three hour meeting, and after the meeting I went straight home and I locked myself, I didn't cry, but I did not want to go back to work. And why was that? This was the reason. This is all I heard the
customer say that day. And it was really an
awakening moment for me, because you put yourself in my shoes, you have started right in another company, and you are expecting things
to be all good and dandy, and this is what you hear. Not happy day scenario, right? Now, I met a lot of other
customers over the next few years and there seemed to be
a recurring theme here. The recurring theme was, the AP teams, and when I say AP here,
it's not action points, it's accounts payable, so
let's just to clarify that. So AP teams here were really struggling to get the data that they needed, to get insights that were
actually driving their business. There was limited
visibility from the product that they were getting. They couldn't clearly see where time was being spent by their teams. They could not identify
process bottlenecks. The main issue was they had
data and they had a lot of it, but there was no intelligence. They did not know what to do with it. So decision making was slow and improvements were
essentially just guess work. Now with all of this, I
went back to the team, and I asked the team, "Let's take a stop and really, really, you know, reevaluate this whole scenario. What is really going on?" And it came down to
these four issues here. The first one, our analytic
stack, old analytic stack, simply wasn't built for what
we were trying to achieve. So we had built our
embedded product on top of our production database. That's limiting a lot of data
that we were able to access, but also limiting
innovation quite massively. The product itself had become
somewhat too complex, right? There are a lot of people here I can see, I would guess, data people. We have a common nuance, which
is data people build products as though they're gonna
be used by data people. And that quite often
leads to a misalignment, because our users are not
necessarily data people, they're business people. And these are folks who are used to the world's greatest BI tool, Excel. I didn't say that out loud, but
you know what I mean, right? So there was a disconnect here, right? We had built a very bespoke product, that wasn't really
working for our customers. And all of this led us to a point where what we needed was not
just better dashboards, we really needed to hit a reset. We really needed to ask ourselves, "How are we gonna, what do
we need to do that we enable our customers achieve
their business outcomes?" And the shift was not a small one, right? We realized it's not a cosmetic update, and we had to reframe the whole problem. The market was demanding
speed, consistency, and embedded intelligence,
as well as AI readiness. At the same time, our
strategy based on these two, so we have the customer sentiment, and we know how the market is evolving. Our strategy became quite simple. What we needed to do was three things. Build a governed, scalable,
multi-tenant data platform, essentially reshift
our whole architecture, crystallize the value proposition, so who are we building
for and for what purpose? I should have mentioned
this in the previous slide, but one of the things that we saw is that we had built a product
that was not being used for what we had built it for, right? So we built very, very bespoke dashboards. But at the end of when
you show a customer that, the next thing they ask you is, "Can I download that data to Excel?" I'm sure you've heard that before, right? So really understanding
what the use case was and building for that, so crystallizing the value proposition. And last but not least, designing a future-proof
architecture that allowed us to actually innovate and scale. Innovation was super,
super paramount for us, especially considering, as I
said, we had a lot of data, and where the market was shifting, especially in our domain as such. Now this is where the
partnership with AWS came in, and it was really, I
wouldn't say a no-brainer, but it was a myriad of things
that we actually considered, and I would just highlight
a few here, right? So serverless architecture,
that was a huge one for us. It gave us the possibility to scale, without costing, where we
needed to process hundreds, or hundreds of terabytes on a daily basis. Governance, finance data,
and that goes without saying, demands strict tenancy separation, strict user user authentication
as well as auditability, and embedding still. QuickSight gave us,
QuickSight which is a part of the Quick Suite now, gave
us a way to push intelligence into the Basware experience
without actually having to reinvent the platform itself. Now this was a no-brainer, right? That we're going ahead with AWS. So what did we actually build? This is what we built, okay?
Yes, this is what we built. We built three things. First of all, a unified, enriched, analytics-grade data foundation
across, give or take, about 1,000 tenants, so 1,000 customers, with consistent KPI models, big team. We have a dedicated governance layer that enforces tenant
isolation, role-level security, KPI consistency as well as compliance. Secondly, we built a fully
automated multi-tenant pipeline, round about 6,800-7,000
as of last week, datasets, being refreshed daily,
about 26 terabytes processed on each cycle with the
largest dataset being about half a terabyte. And thirdly, we built a
deployment engine using Lambda and QuickSight APIs where we publish, and deploy round about
30,000 dashboards globally, and that list, keeps on increasing. All of this takes about 17
seconds to publish 19 dashboards, so per tenant as such. On top of all of this sits QuickSight, which powers the intelligence, right? So we have dashboards that are embedded directly
in the AP workflows, SPICE that is powering
sub-second performance from the datasets. And then within Q, within QuickSight we have Q that enables
natural language analysis, machine-learning-based
insights and et cetera. Now, the biggest unlock from this exercise wasn't the dashboards. It wasn't building new
pretty dashboards, no. It was really how we transformed that raw accounts payable data, AP data, into analytics-grade intelligence. We essentially unified the
entire invoice lifecycle data, and reached it and created
consistent KPM models, and enabled segmentation
across our customers, different industries,
suppliers, et cetera. Now this became a very
powerful foundation, something that we'll take a look after we see exactly what we built. (upbeat dynamic music) - [Narrator] Basware Insights, unlock the power of your AP data. Basware helps organizations
transform AP data into actionable insights,
enabling smarter, faster decisions that drive better business outcomes. With Basware Insights, data is accessible to everyone vested in
AP, CFO, AP managers, shared services center leader,
as well as AP team members. This solution evolves
with your needs addressing these four key questions. How can I track and
enhance business outcomes using my AP KPIs? Basware Insights connects the dots between your KPIs and business outcomes, ensuring your AP processes
are efficient and aligned with your broader strategic goals. How do I quickly get the answers I need? With robust ad-hoc reporting capabilities and Gen-AI powered insights, you can simply ask a business question and get real-time data-driven answers, no technical expertise required. How can I securely access my AP data? Our data access API ensures
secure, seamless access to your critical AP data so you can trust that your information is always protected. What's happening in my AP
processes in real time? Operational AP Insights
provide real-time visibility into daily operations, helping
you stay on top of activities and react swiftly when needed. Gen AI that transforms how your organization works with data. Simply ask a question and
get real-time insights. (dynamic upbeat music continues) And you have a recipe for
best-in-class finance operations. With Basware Insights, realize the full value
of your AP solution. (dynamic upbeat music continues) Now it all just happens. (dynamic upbeat music continues) - All right, this is my favorite part. It's actually not what we built as such, well, I like that too, but
this is my favorite part. It's actually what this
has enabled for customers. And I have two numbers
here, numbers that I like to talk about a lot. You know, these numbers are (coughing), it's essentially what we've been able to achieve with QuickSight. Our development cycle has
essentially reduced about 90%. We are able to ship
enhancements and features to our customers within a matter of weeks, when previously it took
six to nine months. At the same time, the time
it takes for a customer to get insight has significantly reduced, and this is why it really
matters most, right? The customer experience. So there's no more waiting, no exporting, no manual reconciliation,
for our customers and because everything is embedded, AP teams will get, or
accounts payable teams, get the insights directly
within their workflow. Now, I did talk about when
I started Basware in 2017, and the sentiment I got. Now 2024, last year,
round about the same time, we actually launched our
product to the market. And during the launch there was a bunch of customers seated there, and one of the customers
raised their hands and they asked me this. This is what they said. They said, "In 30 years of
building some really cool cars, we have never seen a product
as Basware as that product." This was a profound moment for us because what we had
essentially done is transformed completely how our customers
used to consume data, and they consume data moving forward. Now, as we knew, that's when
we built something special and the foundation was
set, then what is next? We are on a journey and what
we have done so far is laid the foundation with embedded intelligence. We are looking at expanding
that with predictive workflows, simulations, forecasting, et cetera. Now ultimately our goal here is to deliver personalized,
proactive accounts payable, where AI doesn't just
describe what happened, it recommends what to do
next and in certain cases, within certain guardrails,
actually takes an action. Why accounts payable? A recent study done with
"Financial Times" reveals that 75% of CFOs actually want to
increase their investments within accounts payable, in AI. And 85% of CFOs also
see a really huge return on investment within accounts payable. Accounts payable is the ideal
place for AI to play, right? It's a linear process with very, a lot of manual, repetitive tasks
and really, really good data that we can leverage. How we are looking at
essentially providing this is by embedding AI within
our platform, right? So we call this InvoiceAI, where we don't build AI
externally outside of our system, but it's built within the workflow, essentially augmenting and
enhancing how accounts payable, essentially execute the process. With that said, what does
it mean then? Quick Suite. So far with our users, for our
users, we have been able to, and you did see a bit of
this with the Q capabilities, we have been able to ask
or, to enable our customers, to ask two fundamental questions. What happened? When did it happen? So what were the invoices
sent by supplier X, Y, Z? What was the value of those invoices? Now that's good. That's information. But fundamentally where
we want to take this, and we are really looking forward to, is answering these particular questions. "Why did it happen? What
should I do to fix it? What if I change something? How would that impact our
processes or business?" And ultimately baking this in together with the actions, right? So really having AI execute certain flows, within certain guardrails, for end users. It's a really exciting time
for us as we move ahead. To wrap this up, what we set out to do, was to essentially reimagine
what analytics could do for finance and especially
accounts payable. What we built was more than a platform. It is really a foundation,
a data foundation, and a solid foundation, that
will drive transformation. And for me it's super, super exciting because the journey doesn't end here, it's just the beginning. Thank you. I'll hand over back to Thomas
to take us to the next step. (audience applauding) - Thanks Kevin. Thanks for
sharing this insightful story. And I'm as excited as you to
see how the new AI capabilities will empower you and your
customers going forward. Having focused in today's session mostly on the data foundation and
integration side of Quick Suite, you've likely realized that there's so much more to explore and learn. In the coming days, you
will have the opportunity to join plenty of sessions
and workshops across the next re:Invent days to
learn more about different set of use cases and all the
different capabilities that Quick Suite can offer. Additionally, I would highly
encourage you to also stop by at one of our booth in the
AWS Village, in the Expo area, where you can see additional demos of some of the other capabilities as
well as discuss your questions and use cases with one of our experts. I can also highly recommend you to check out the Quick Suite community that provides you access to hundreds of learning resources,
events, and much more. With that, I would kindly, sorry. I would like to thank you first of all, for your attention today, and kindly ask you to fill
out the session survey in the mobile app. In case you have questions, we
will be sticking around here. Wishing you a great rest of the week. Enjoy re:Invent, and thanks again. (audience applauding)
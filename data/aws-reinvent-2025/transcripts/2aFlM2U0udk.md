---
video_id: 2aFlM2U0udk
video_url: https://www.youtube.com/watch?v=2aFlM2U0udk
is_generated: False
is_translatable: True
---

- Thank you, thank you for
coming to this session. It's so early on a Monday
and it's almost like all of us here are kicking
off this re:Invent 2025. So, you know, kudos to all of us. My name is Raghu, I'm a technical product manager at, a product marketing manager at AWS. I've been with the company
almost 10 years in a few weeks. So, welcome to today's session, which is Enabling AI Innovation with Amazon SageMaker
Unified Studio, okay? I'll kick things off, and I have two other speakers here today. Terri Sutherland. She is the general
manager for data platforms at Commonwealth Bank of Australia. So for short, you know,
we'll call it CommBank. So she's gonna come on, and then we have our star
solution architect, Praveen, who is also from Australia. So very thankful to Terri
and Praveen for coming here all the way from Australia
to do this session with us. So, oh, I should have done this first. So this is today's agenda. So like I said, I'm gonna kick
things off, set the stage, and then I'm going to
hand this off to Terri. Terri is going to walk us
through CommBank's journey using SageMaker Unified Studio and some of the other
capabilities within SageMaker. Problem statement, outcomes, impact that they have had in the bank. And then Praveen is going to come on and he is going to walk us
through the architecture that they built within
CommBank and also do a demo. So this is going to get very technical once Praveen comes on,
and I'm sure, you know, those bits are going to be
some of the more exciting parts of today's presentation. So. Okay. so we're gonna start off with
some data, some research. So this is a research analysis done by Harvard Business Review this year. And basically what they are telling us is 89% of CDOs have an initiative to build applications
using AI and generative AI. So majority of them are
building applications with AI and gen AI, but an
overwhelming 52% of those CDOs don't think they are ready
to embark on the AI journey. And the reason for that is
they don't have enough trust in their own data. They don't have enough
faith in their own data because they don't know their data. So as much as we all want
to do exciting things with AI and generative AI,
agentic this and agentic that, I hate to break it to you. We kind of have to go back to the basics and get our house in order with our data. So what does that mean? It means building a sound data foundation within the organization, okay? And at AWS, we look at this as
two very broad things, okay? Well, how do you build a data foundation? We're gonna talk about that a little bit. And then we look at this
as two very broad things. One is improving data literacy
within the organization, which is, do you know about your data? Do you know what's good? Do you know what good looks like? These are not easy
questions to answer, okay? So improve the data literacy
within the organization, and the second is build
a data culture, okay? And we will look at these
two parts, you know, a brief overview of what this means, and then, you know, we'll go
to CBA story or CommBank story. Okay. So I may have spent majority of my time here at AWS doing this with our customers. And I believe that most folks who are here can relate to many projects that you may be currently working
on that does this exact thing. So there are seven data actions as part of improving data
literacy within the organization. This is not an exhaustive list, you know, this is some of the main
items that most customers do to improve the data literacy
within their organization. Let's just kind of go
through this one by one, you know, 20, 30 seconds each. Build a data inventory. What does that mean? It can mean different things, but broadly this is what it is. It is a directory, a
list of all your data, and that includes tables,
that includes S3 buckets, you know, with structured
data, S3 buckets with images. It also includes
applications like dashboards, models, all of it, okay? You should build a list of all that data. We call them data assets, okay? This in itself can be a
pretty elaborate topic, but I'm gonna just do this really quickly. You can build this a few different ways. One is you can start at
the bottom with the data and build an inventory
off that, which is tables, S3 buckets, and so on. Some customers like to do it from the top, which is from the application side. They like to build an inventory
off their BI dashboards and models and then work their way down. Some customers just start
with a line of business, figure it out, and get a process going in terms of building that inventory and then rinse and repeat that from line of business to line of business. And CommBank is going to talk
a little bit more about that. So that's what building
a data inventory means at a high level. Second is data annotation. And this is probably the most boring part of the whole journey, but
there is generative AI to help all of us, but
what does that mean? When you build a data
inventory, what does it contain? It just contains metadata, you know? Just cryptic table names and column names, and no one can really make sense out of it whether humans or agents can make sense out of technical data. And in most cases, we
will all get it wrong. So data annotation means putting, describing, describing technical data and giving it business context. This is customer table for product X, this is a regional
customer table, et cetera. Someone or something will have
to go and annotate this data. And like I said, not very
exciting, but very important. From there, detection of PII data. If you're going to be
doing modeling, training, you're retraining a foundational model. You do not want PII data
as part of that project. So detection of PII data, super important. Once you detect PII data,
what do you do next? You categorize it. Most sensitive, least
sensitive, et cetera, that fits your company's security SLAs. From there, data quality. How good is this data? We all talk about bad data. How bad is it? So data quality is part of
building the data literacy within the organization. Then lineage, most people
here probably know what it is. Data origin, data transformation. Where did this data come from? You know, that's being tracked. And then finally,
publishing new data assets. So this is one of the areas where I have seen customers struggle with. You do all of it, but your
data inventory is not static. Your data inventory is ever changing. So you have to build the practice where when you do all of this, this is a significant investment. New assets are created every day. You gotta put it back in the inventory. So it's a practice, it's a habit. Many customers do it really well. A lot of customers are still
trying to figure it out. Okay. Like I said, been doing
this for a long time. And I just want to just
leave you with this, you know, and a couple more slides. Choose your own journey with this in improving the data literacy
within the organization. What I have on the screen,
it's just a recommendation, it's a suggestion, but
choose your own adventure in improving the data literacy
within your companies. Most companies start with PII because they want to de-risk, okay? Then they go to data
quality and then inventory. So, so on, right? So pick your journey and then stick to it. So this is, if you take a
step back and look at it, and even if you did, four
or five of these things, you will be significantly improving the data literacy footprint
within the organization. Okay. So that's data literacy. Second, building a data culture. The best way to explain this, we all have learned to be
very social digitally, right? You know, with Facebooks and
in LinkedIns of the world. We all have built a pretty
good social culture. The same thing applies to data culture. I'm just gonna draw some parallels here. When you want to make a social platform, okay, either it is for videos
or whether it's for data, you really have three things. You have producers, content creators, you have consumers who consume
what the producers create, and they like, comment, use. And then there is a third party,
which is the central team. The central team provides
you with the platform. They provide you with guardrails,
policies, best practices, do's and don'ts, so the whole activity of being social is sustainable. CommBank built this and
they will walk you through their story, how they started, and how they built once
they kind of got it right, and how they kind of
expanded their expertise and built the data culture
within the organization. So this is extremely important. And again, when you build a data culture, it really needs to be in
the organization's DNA. It needs to sustain executive churns. So like I said, these things take time. You have to build it over time and you gotta make that a habit
within the entire company. Okay, so we talked about data foundations, we talked about data literacy, we talked about how you
build a data culture, and none of these things
had anything to do with AWS services. These are just in a good data practices. So how can we help you? If this is important to you, if PII detection,
building a data inventory, building the data culture
is important to you, well, how do you get started? Well, last re:Invent, re:Invent 2024, we released, we rereleased, relaunched, I should say,
Amazon SageMaker, okay? It is our data and AI platform. It's got lots of features and functions and we broadly look at Amazon SageMaker like a three-layer cake, okay? We'll go from bottom up. At the bottom, we have the
lakehouse architecture, all Iceberg-based data architectures, Iceberg REST Catalog functionality, lot of managed capabilities
built into our lakehouse. So we got sessions on lakehouse, so definitely check those out. And on top of it is the
data in AI governance. Most of what I just talked
about in the last 10, 12 minutes fits into this data and
AI governance capabilities built in Amazon SageMaker, okay? And at the top, we have
unified data experience. Well, what does that mean? So you got a lakehouse, you have good data
governance capabilities, which means you can search data, you can find data, get access to data. Then what do you do with it? Well, that's where the
UnifiedUI comes into picture. SQL capabilities, data processing,
building data pipelines, generative AI app development are all part of our Unified user experience. But obviously we are not stopping there. We are, you know,
building more capabilities like streaming and BI
and even search analytics and some of these capabilities
will come in 2026. So this is just zooming into the Unified Studio
experience within SageMaker. As you can imagine, this
is meant for data workers, whether you are doing SQL, whether you're doing modeling,
training, building pipelines, we have notebooks as you can imagine. We have notebook experiences
built into the studio. We have query editors
built into the studio. We have, this is my favorite, visual low-code, no-code experience built into the studio as well, which means you can build data pipelines, you can build, you know, ETL
jobs with absolutely no code. And then we also have
generative AI chatbot building experiences as well. And then it's my last slide before I, you know,
get Terri on the stage. So this is the second
layer of Amazon SageMaker, and this is, like I said,
most of what I discussed, which is data literacy and
building the data culture within the organization
are all part of the data and AI governance
functionality within SageMaker. You can do PII detection, you
can do data quality checks. We have an awesome business data catalog, awesomely priced, almost free. So it's got great capabilities, you know, definitely check those out. And then, you know,
hopefully you start building your amazing data practice
on Amazon SageMaker. Before I get Terri on, I
do wanna mention one thing. You saw the three layers. I should have said this
a couple of slides ago. You saw the three layers. You don't have to use all
of it all at the same time. You can start your journey anywhere, okay? If data governance is the
most burning problem for you, then you can start with data governance. If lakehouse, then start with lakehouse. And then you don't have to use everything. We truly believe if you use all of it, you will get the best experience, but you don't have to. You can start somewhere and
then expand your overall usage of Amazon SageMaker as the needs come. Terri. Thanks, folks. (audience applauds) - Oh, thank you. Thanks very much. Hi everyone. Thank you, Raghu. Really pleased to be here. My name's Terri Sutherland. I'm the general manager of
the cloud data platforms at the Commonwealth Bank of Australia and I'm super excited to be here today to talk to you about our
ambitious strategy and AI roadmap and transformation journey. But first let me tell you a little bit about the bank itself. Though many of you have
probably never heard of the Commonwealth Bank of
Australia or CBA as we call it, we are Australia's largest bank. Australia's population
is 27 million people. And CBA services 17.5 million customers. That means one in three Australians and one in three businesses bank with us. Overall, 50% of
transactions go through CBA, and on the global stage we
are the 13th largest bank by value, by market value. And I'm excited to say
that we've just been named top four bank globally for AI maturity. Oops, sorry. Didn't realize you hadn't moved the slide. Given the importance of CBA
to the Australian economy, our data and AI strategy is one of the bank's most valuable assets. It underpins everything we do. From protecting our customers
against frauds and scam to delivering seamless
personalized experiences. Whether you're accessing cash at an ATM, paying for groceries, or
applying for a home loan. Data and AI powers the services that our customers rely on every day. At the heart of this strategy
are three core pillars. Firstly, and always most
importantly, our people. Like many organizations, we
realized central engineering and AI teams just couldn't scale. So our first step of our
strategy was to decentralize and embed our data engineers
and data scientists across the lines of business in the bank. By doing this, we brought the data and AI closer to the people who use it and closer to the people
we serve, our customers. Our second pillar is safeguards. We're a bank, we manage
sensitive customer information. So we've designed governance and controls to be inherent in every single stage of the data and AI life cycle,
ensuring safety by design. And finally, our third pillar, technology. This is where our partnership
with AWS comes in. We needed to take decades of rich data spread across hundreds of source systems and put it into the hands of our federated data and AI teams. To achieve this, we established
a data mesh ecosystem that empowers our federated
teams to operate independently. It moves data seamlessly, ensures access for people and machine, all the while enforcing strict governance. We call this ecosystem CommBank.data. Today it provides our 40 lines
of business across the bank, the freedom to produce and use data all within a trusted,
traceable, controlled framework. By decentralizing, we adopted a clear producer-consumer model. Each business unit now owns managers and manages this data as a product with defined roles and responsibilities. We also introduce
self-service data sharing through a unified data marketplace, a single pane of glass where
users can discover, request, and consume data across
the entire AWS ecosystem. But here's the reality, data has gravity. Where the data lives is where
every single data engineer and data scientist in the bank will work. Historically, CBA had decades of rich data held in on-premise platforms. Platforms that lacked interoperability or could not scale for AI. And so we made a bold move. We migrated 61,000
on-premise data pipelines to our AWS mesh ecosystem
that's equivalent of 10 petabytes of data. The migration took us nine months with 100% of data pipelines
tested at least three times. That's 229,000 tests. And in so doing, we moved
our entire data engineering and AI workforce to AWS cloud. To make all of this real, we had to run two major programs in parallel,
migration and marketplace. We migrated over 10 petabytes of data from on-premise to AWS cloud and built the data marketplace aligned to our federated,
decentralized operating model. We started with migration. Earlier last year, we kicked
off a series of workshops with AWS to test our
most complex data flows and AI use cases to see if the migration to AWS native technologies was possible. We call this approach steel threads. Like an MVP or a proof of concept, steel threads proves the technology fit, but also productionalizes the outcome. We built AI and generative
AI that transformed code, check for errors, and tested output, reconciling every single table to our on-premise platform 100%. Every single row, column, and number had to be accounted for. But this was more than a
tech builder migration. It was also a major
change management effort. We onboarded federated data teams through 200 tailored sessions and trained over 1,000 engineers, embedding change, building capability, and driving sustained adoption. And throughout, we also worked closely with local and international regulators to ensure compliance and continuity. Now let's talk about the
second major stream of work, building the data marketplace. This was a fundamental shift in how we think about data ownership and access across the bank. Each line of business
was becoming a producer, a consumer, and many cases, both. We started by building
our technical foundations, a federated data mesh
platform designed for scale, governance, and decentralized ownership. As we transitioned from a monolithic to a composable platform,
we faced the challenge how to seamlessly connect hundreds of line of business owned AWS accounts while keeping the user
experience frictionless. So we implemented a abstraction layer, one that could unify access to data, offer flexibility in
compute and UI choices, and uphold our rigorous
governance standards. Praveen will bring that experience to life in a demo shortly. Once that was all in place, we implemented AWS DataZone
to enable discovery, access, and sharing
across the organization, bringing on early adopters. And with the launch of
SageMaker Unified Studio, earlier this year, we added in a single pane of glass
experience so everyone from analysts to executives
could see and use the data they needed. In completing this, we
aligned our engineers, onboarded producers and
consumers, to a shared framework, one that creates self-service
while maintaining governance and interoperability across the mesh. And now with the right
data in the right place, we're ready to scale with governed AI. Let's look at the benefits
of what this transformation is allowing us to do today. When we spoke to our
engineers and data scientists, they told us CommBank.data marketplace has transformed the way they work. Now they connect directly from their local VS code environment, no longer restricted to
SageMaker or remote platforms. This access streamlines workflows and speeds up experimentation. On the standout features is a single pane of glass experience. Instead of switching between
tools and interfaces, teams have a unified dashboard for data discovery,
analytics, and monitoring. The Spark UI is easily accessible, allowing real-time tracking
of query performance and quick identification of bottlenecks. Dedicated compute resources also means workflows run reliably and troubleshooting is far more simple if problems arise. The integration with
SageMaker was a game changer. Data labs outputs are now available directly within the platform, removing manual steps and making it easier to run advanced analytics and
machine learning workloads. These improvements have
created a unified environment that empowers our teams to experiment, deploy, and scale AI with ease. It helps us build a
culture of AI innovation where our people are closer to the data and scaling AI with confidence. So we've achieved a lot
in the past 18 months. We built a strategic mesh
ecosystem in AWS cloud. We migrated decades of investment
to that cloud ecosystem and onboarded data and engineers, data engineers and data scientists to AWS and innovative tooling. But what did we learn along the way? We could not scale with data and AI with centralized operating
model and monolithic platforms. We needed to train our people to understand the new
federated operating model and allow time for engineers and data scientists to become
certified in the new tooling. MVPs, steel threads, and iteration
are our path to discovery and in fact the fastest way to true value outcomes for our customers. And importantly, we needed to recognize that transformation is
always a learning curve, which means being
comfortable with the unknown. Looking ahead, we'll continue onboarding our lines of business and maturing with them,
expanding generative AI, Unified Studio including
Amazon Q and agentic AI and deepening lineage
explainability and observability. Next, Praveen will show you
this unified experience works and end-to-end SageMaker Unified Studio for the CommBank.data marketplace so you can see the
architecture come to life. (audience applauds) - Thank you, Terri. It's been a pleasure to collaborate and work alongside CommBank data team on this very exciting data
transformation program. I strongly believe that the
team has built a highly scalable and a future fit modern data platform that is going to help
accelerate time to insights, is going to increase
organizational agility, and at the same time meet
all of the strict governance and regulatory obligations. My name is Praveen Kumar. I'm a principal AI
solutions architect at AWS. And the next 20 minutes or so, I'm going to take you through
CommBank data platform, how we'll design, platform architecture, and I'll also have a
short demo to show you an end-to-end user experience in a multi-account environment. And that's how CommBank
data platform is set up. But before that, I would
like to acknowledge CommBank data team and
particularly Olatunde Baruwa who's a chief engineer at CommBank. They have been instrumental
in the implementation and the execution of this data platform. As Terri shared, the data
transformation program included two major streams of work. The first one was about migrating our on-premise Hadoop-based
data lake platform with over 10 petabytes of data to AWS. And the second program involved setting up an internal data marketplace that aligned with targeted
state federated operating model where each line of business,
there are 40 of them, will act as data producer
or data consumer or both. And the central team will
provide lightweight governance while facilitating the
marketplace ecosystem. So let's look at the
migration program first. What you see here is the high level design and the key components of
the on-premise platform before and after migration. On the left is the setup
before the migration. The on-premise platform was made up of two large scale Hadoop clusters. One of the cluster was used
to run 61,000 pipelines and then data and metadata was copied to the other Hadoop cluster to serve interactive workload. When this platform was moved to cloud, it was mainly done through
a lift and shift approach. So data was migrated to Amazon S3 and compute is now powered by Amazon EMR. However, one of the key
benefit when migrating Hadoop-based data lake platform to cloud is that there is separation
of a storage and compute. Because all of the data is in Amazon S3, the team is able to
enable access of this data to variety of cloud native
analytics and ML engines to support diverse set of use cases. Next is federation. Previously, the team built,
managed, and supported on-premise data lake
platform that was monolithic. However, in the federated
setup, each line of business, there are 40 of them, have their
own dedicated AWS accounts. They use Amazon S3 to store their data in Apache Iceberg format. They built pipelines using
either EMR Serverless or Redshift or other third party engines. They use Glue to store technical metadata, lake formation for
policy stored, and so on. But more importantly,
LOBs are now responsible for building and managing
their own data assets, their own data pipelines,
their orchestration. They're responsible for the
data quality of these assets, SLAs, observability, and more. So as the platform evolved
from a monolithic unit to a distributed and composable construct, we needed to build an abstraction layer that would bring all
of these LOBs together. So there are two key requirements. The first one was to build an enterprise-wide business data catalog where data producers
can publish data assets and data products, and
data consumers can search, discover these assets, and
request access to these assets. The second key requirement was to provide an integrated builder
experience for all data users. Users such as data engineers,
data analysts, data scientists to use user interface of their choice. This could be notebooks,
query editors, visual ETL. And then we also be able to leverage a variety of compute engines that's optimized for their use case. And so to support these
two key requirements, the team onboarded Amazon
SageMaker Unified Studio. SageMaker Unified Studio
provides an integrated developer experience for all data users to build data and AI-driven applications. It has got governance built
in with SageMaker catalog. The teams were also able to leverage many of the construct within
SageMaker Unified Studio for broader governance. For example, they use domain units to replicate organizational hierarchy and implement governance policies. They used projects to isolate workloads and map to hundreds of AWS accounts, and they use the pops up model within SageMaker Unified Studio to integrate with third party engines. Now, earlier this year, we migrated the on-premise Hadoop based
data lake platform to AWS. This has almost all of CBA data. We are talking about tens
of thousands of tables. However, this is monolithic in nature. In parallel, we started onboarding
various lines of business to the internal data marketplace, and this platform is federated
and distributed in nature. So the next challenge was how
do we bring them together. So we did that in two steps. The first was to identify
the line of business owner for each table that has
been migrated to AWS now within the data marketplace. And so the idea was to provide
the necessary governance. For example, a business
owner is now responsible for approving the usage and access of that table or data asset. The second step was to enable
the technical integration. And this is going back
to my earlier point. Because all of the migrated
data is in Amazon S3, we built a lightweight ETL
job that replicates metadata from RDS Hive Metastore
to Glue Data Catalog. So you have all of the tables now appearing in Glue Data Catalog. And then we mapped each of those tables to the respective SageMaker
project under their LOB. Now since all of the data is available in the centralized SageMaker data catalog, data consumers can come
to a central place, which is the studio. They can browse, discover, request access. And once the access is approved, they can build their applications through a query in place architecture across hundreds of AWS accounts. So there is no data movement. Data can be living in many
of these AWS accounts, but we're able to use compute
from any of these accounts with the right governance. All right, so now it's time
to see all of this in action. The demo is partly inspired by how common data platform is set up. So you'll be using a
multi-account environment. The demo use case is building
a fraud detection model for a financial services organization. We'll have two user personas in this demo. We have got Samantha or Sam. She's a data engineer. She's part of retail banking team, so that's a LOB line of business. She's going to create a new table called customer_profile table by combining data from two existing table that her team owns. She's then able to, she's then going to enrich the metadata. So she's going to add a README, she's going to add data quality, lineage. And once the metadata is enriched, she's going to publish it to the catalog for others to discover and request access. She's also responsible
for approving access to the subscription
requests on LOB's behalf. The second user persona is Javier. He's a data scientist and
part of financial crime team. He's going to build the
fraud detection model. And to do that, he needs
access to the various datasets. So he'll go to the catalog where he can centrally
discover all of the assets and request access to this new
table that Sam has created. Once the access is approved, Javier is going to do
some interactive analysis and then build a ML model
using SageMaker AI API. Here is the setup. So this is the multi-account
environment setup. At the top in this demo, I
have used three AWS accounts. At the top is the shared services account. So this account is owned
by the central team and this is where
SageMaker domain is set up. And then SageMaker domain is
hooked to two AWS accounts. One is the data producer
account on the left and the other is data
consumer account on the right. So anything that Sam is using in terms of storage and compute, that's going to sit in
the producer account. When she's building a pipeline using Spark or when storing data in
S3, that's all going to be in that leftmost account,
which is the producer account. Anything that Javier is going to do, so essentially, you know,
you're running Athena query to do exploratory analysis or using SageMaker AI
API to train the model, that sits in the consumer
account on the right. This pattern is scalable to
hundreds of AWS accounts, and this provides you the best practices in terms of setting up
multi-account strategy. You get workload isolation, you can allocate costs to respective LOBs, and at the same time, you can implement the distinct governance boundary. All right. I'll hit play. So I'm in SageMaker Unified
Studio and I'm logged in as Sam. So this is the homepage of
SageMaker Unified Studio. And you can see at the top section you have things like discover catalog, you can play with the foundation model through generative AI playground. So let's, you know, as
one of the first action, let's browse catalog. So this is the catalog
view where you can discover all of the organizational asset. So at the top section,
you can type in a keyword, it does semantic search, and then it will return
the results, right? So for example, I have a search for a table called transaction, it showed up. At the bottom half of the page, what you see here is the
domain unit hierarchy. So this maps to your LOB hierarchy. In this case there are only two LOBs, RetailBanking and FinCrime. And then at the top is the project. So project is a concept
where you map a project to a use case which allows you to group compute and data that
a team has access to. So in this case I've got two projects, RetailBanking data team
project that is aligned to the retail banking team. And this is where Sam is going to work. And I've also got another project FinCrime which Javier has access to, and this is where, you
know, he's going to use that project to train ML model. So Sam is going to click on that project. This is the project overview homepage. We'll go through the menu
options on the left one by one, but at the top on this page, you can see the various project files. This could be your notebook
files, query files and so on. But important point to note
is this project role ARN on the right side, so,
which I have highlighted. And I can see that there
is an account number here. This is the data producer account, right? And this project role helps map
what compute and data access that the team has as a
part of this project. So in case of, you know, JVR, this will be a different
role and a different account. All right, so that's the
project overview homepage. Next we will go and click on
the data on the left hand side. And so this is all of the dataset that the team has access to. So, you know, any Glue
tables will show up. In this case there are three Glue tables that the team has already created. If you have access to Redshift data, that will show up here as
well as any S3 buckets. Then there is the Compute tab, which is where all of
the compute will show up. So in this case the team has
access to Redshift Compute as well as Glue Spark. And you have access to
other compute like Hyperport or MLflow Tracking Server,
all of that will appear here. And this Members is, you
know, all of your team members who are part of this project. So essentially part of
retail banking team, that will show up here. On the bottom half of the left hand side is the project catalog. So this is where you build your catalog. So you bring your table
from Glue Data Catalog to SageMaker catalog inventory space and this is where you enrich the metadata. So you can add glossary,
metadata forms, data quality, and I'll show you this in a while. But for example, this team
has already got access to three tables that they have enriched. And this is showing up as customer, customer account, and transactions. All right, so the next step from here is, let's say Sam wants to
build a new table, right? They already have access to two tables, customer and customer activity. Now she's wanting to build a new table called customer_profile. So she comes to the Jupyter Notebook. She sets some Glue Spark
config, like number of workers. Run some selected statement, you know, customer account and customers. And at the bottom, there's a
cell called create table as where essentially she combines data from customer and customer account table and creates a new customer_profile table. So once that cell runs, you'll
see on the left-hand side that we'll have fourth table appear called customer_profile. So that seller has executed and now I can see the fourth table. So I've created a new table
by combining information from other tables that my team owns. So the next step is I want to enrich the metadata of this table. So I come to the data source. So I'm already creating an data source that points to Glue Data Catalog and I'll bring the metadata
to the inventory space. So I have now run that data source, I can see the new table is appearing here. Now this is where you can
add things like README, you can look at, you
know, the schema details. So all of the columns will appear here. Data quality is blank, we'll
populate it in a while. And then it also shows you the lineage. And this lineage is, you know, as we're building the pipeline, Glue Spark is already integrated
with SageMaker catalog. So it's pulling all of
the lineage information when we are ingesting the
metadata of that table. So it shows you column level lineage and this is open lineage compatible. So from here, let's say
I want to add a README, which is essentially looking
at the schema details of this table and looking at
few records of this table, I want to generate a summary. Now you could do this
in a couple of phase, you could have your steward
manually doing this task or you can take advantage of agentic AI. So when you go to the Jupyter Lab, we have this agentic AI capability, which is Q CLI integrated. So I'm giving it a prompt, I'm saying that I have a
table named customer_profile in my Glue Data Catalog. Can you generate a concise summary of this dataset using schema details and also looking at 10
records within the table? And I then provide a helper
function which has details like using the permission
scoped to the project, which is the project role, as
well as the Athena work group assigned to that project. So I give that instruction. Now this is where the agent is
planning out the set of steps and then it's going to execute. It fires up, you know,
Glue APIs to understand if there's a table
which is similar looking and it's able to detect that table. And then it's going to
use Athena as an engine to run a select star statement. So this takes about a few seconds, but once it completes, it
will save the description, concise description into a
local file within the space. If you want to look at the details, what query it has generated, you can, you know, just
expand one of the dropdown and you can look at the query
that that agent has generated. So just in few seconds, you'll see that it has now created a directory. Now it's creating a file
and it's going to save. All right, so it has
already created the file and saved the concise
description based on the schema and the tender codes. Next I want the agent
to use this information that I just generated and I
want it to update the data asset within the SageMaker catalog
with this information. So update the README. So I'm just saying that read
the dataset description file generated above as part of
analysis of the specified table. Format the content and
update the README section of the data asset. And I provide helper
function with an example API. So then it's able to, you know, compile the necessities and structure, it self-correct itself in
case it's not able to post. And again, within few seconds, it's able to create an asset revision within SageMaker catalog for this asset. So it has completed that activity now. If I go here and refresh, I will see the README
section is populated. Now this README section is fairly accurate in terms of what that dataset is about. Next, so we have got, we have enriched the dataset with lineage, README. Next if you want to, let's
say, run data quality checks, that's another prompt you can run. I'm saying that I have a dataset and I want to run a data
quality for this table. I would like you to create
two data quality rules, check null values for each
column and email validation and use Glue Spark engine to do that. So again, it goes and plans, it uses the Glue interactive session in the context of the project. It changes the Spark SQL. And right now the data quality is null. But once this finishes running
the data quality checks, you'll see that data
quality will get populated. And this is where it's save, like, it has finished running
the data quality checks and it's saving the results into a file in the local directory. And so one last prompt time entering is, now take this information
that I just generated in terms of data quality results and populate the data quality section within the SageMaker catalog. And this is all running
in context of the project. So the scope boundary is that project role that I showed you. So this has completed updating
the data quality rules. And you can see here again
within minute or two, you have got all of the
data quality results appearing in the SageMaker catalog. So now Sam is happy with
all of the enrichment. So she has updated README,
lineage, and data quality. So she's going to publish this asset, which makes it discoverable
to anyone in the organization who has access to the
SageMaker Unified Studio. And this is that single
pane that we talked about. So this customer_profile
table is appearing now. I'm logged in as Javier
in a different browser. So you can see it's a different user. And this is the project overview homepage and the project selected here is FinCrime. So it's a different project. You'll see here the project
role is a different role and the account number is
that data consumer account that I talked about earlier. Javier and his team has access
to a different set of table. So in this case, he has got access to a table called transactions. And he needs more dataset to
be able to build his ML model. So he goes and types for any information related to customer_profile. He can see that there is a
table that has been created and that exists in the catalog. So he can analyze all of the
metadata, like column details, data quality, lineage. And if he's happy with
all of the information, so he can also looks at who created this, which team owns it. But if he's happy with
all of the information, he requests access to this table. So it creates a subscription request. And this request goes to Sam
who is the owner of the table. So Sam can see there is
a subscription request and she goes and reviews
the subscription request where she can see details
like who has created it, which team is it coming from, and if she's happy with, you
know, all of the details, she goes ahead and approves. At this point, SageMaker
takes care of the fulfillment. So even though the data is
located in a different account and compute is in a different account, it goes and execute the lake
formation API to, you know, do the necessary policy
so that, now Javier, once he goes and refreshes
his technical data catalog, he will see that the
new table will appear. So now he has access to
customer_profile table, he'll run a quick select star. So this query which he's using Athena is running in the data consumer account. So he's happy with all of the results. And so one final step is
to build the ML model. So I pre-created a notebook. So Javier goes to the Jupyter lab. I pre-created a notebook
and I've also taken the help of agentic AI to kind
of generate this notebook. But he goes and, you
know, runs Athena Query for feature engineering. He pre-process the data,
he prepares the data, he uploads the data to S3, and then eventually he trains the model using SageMaker AI API. This takes about few minutes to run, so we won't probably
wait till this finishes, but this is kind of the last
step in the process, right? So that's the end of the demo. Let's head back to the presentation now. All right. Now before I wrap up,
I'd like to emphasize on a few key points that we
covered in our session today. First, building data and
AI culture takes time. So it's crucial that
you have executed buy-in and that you stay invested. Second, as you embark on your
data transformation journey, it's important to start
with steel thread use cases because not only it provides
immediate business value, but it also helps with faster
iteration and feedback loop. Third, your data is your
unique differentiator. And so it's very important that you have a strong
data foundation first in order to get the maximum value from your analytics and AI initiatives. And finally, as you saw
in case of CommBank, you can leverage Amazon SageMaker for your data transformation journey. And we at AWS are here to help. With that, I'd like to
wrap up our session today. I'd like to thank Terri and
Raghu again for co-presenting and each one of you for
attending our session today. I really appreciate if you could
fill up the feedback survey that should be on the mobile app, and thank you and have a
great rest of the re:Invent. (audience applauds)
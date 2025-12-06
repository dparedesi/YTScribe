---
video_id: 95ko3gR34oI
video_url: https://www.youtube.com/watch?v=95ko3gR34oI
is_generated: False
is_translatable: True
summary: Business-driven AI innovation requires eliminating the fundamental gap between business teams' creative potential and their practical ability to access and understand enterprise data, which MUFG addresses through a strategic three-layer approach built on Starburst's data federation platform that empowers business users to independently drive AI initiatives while maintaining appropriate governance, guardrails, and guidance throughout their experimentation journey. The foundational layer leverages data federation to access information wherever it resides across cloud and on-premises environments without requiring costly and time-consuming data migration, whether data lives in data lakes, relational databases, SaaS platforms like Salesforce, or embedded systems distributed across the enterprise, providing immediate connectivity to dozens or hundreds of disparate data sources without the operational overhead of moving data into consolidated repositories. The transformative second layer implements a business-facing semantic layer that organizes raw technical data into logical data products business teams can recognize and understand, similar to walking into a family gathering where you immediately recognize your relatives, creating an intuitive experience where business users encounter their data structured according to their mental models rather than technical schemas, with MUFG implementing a two-tiered semantic layer architecture consisting of core data products aggregating data from potentially hundreds of sources into fundamental business concepts like customer, channel, and banking products, while functional data products serve as derivatives combining elements from multiple core products to address specific departmental needs such as commercial loan operations monitoring data quality during loan booking processes. This approach pivots from traditional physical data consolidation strategies toward logical organization, aligning data products directly with business products so lending teams work with term loan data products that mirror their actual business offerings, enabled by creating specialized business data producer personas embedded within business units rather than IT, ensuring data organization reflects business language and operational realities while maintaining data elites within business context who understand both domain requirements and data relationships. The trigger for MUFG's strategic transformation centered on time to market considerations, specifically empowering revenue-generating business teams to prepare data independently rather than queuing requests through IT or CDO organizations, recognizing that business success depends on enabling self-sufficient analytical capabilities where power users can access data from fifty different systems without technical intermediaries, though the journey involves mixed adoption requiring complementary data literacy programs since approximately half the user base consists of power users capable of independent operation while others need guided support to reach that confidence level. The critical enabler throughout this architecture involves enriching data products with comprehensive business metadata at column, table, and role levels rather than relying solely on technical metadata, because when business descriptions accompany data structures exposed to large language models, the result delivers dramatically more accurate and performant analytics, allowing business teams to receive curated lending data products and independently evolve capabilities by asking exploratory questions like whether agents can perform specific tasks or incorporate additional skills, creating an environment where experimentation feels safe because data products expose only governed subsets rather than entire systems, fundamentally decreasing both time and cost to experiment while targeting the goal of launching ten AI projects in ten weeks rather than one project over eighteen months, accepting that not all experiments succeed but maintaining velocity through rapid iteration cycles where three successes justify moving forward despite seven failures. MUFG's AI landscape strategy operates along two dimensions: first, utilizing AI to enhance data management capabilities including profiling, lineage tracking, cataloging, and tagging, all centralized through Starburst rather than distributed across fifty different systems; second, enabling business users to chat with data through conversational interfaces asking questions like "give me all middle-market banking customers" while ensuring authentication mechanisms prevent unauthorized access, integrating Amazon Bedrock and other Agentic features into a unified real data marketplace where users access everything in one location. The bidirectional relationship between data and AI manifests as "data for AI" where structured data from systems and unstructured content from deal files feed LLM models to generate organizational insights, and "AI for data" where artificial intelligence automates tagging, creates lineage documentation, and performs profiling to generate metadata insights, with Starburst enabling improved data quality indexes by centralizing curation before feeding information into AI modeling processes, ensuring richer input quality for machine learning applications. The strategic architecture delivers agility on two fronts: first, the semantic layer's logical organization remains agnostic to underlying data locations, supporting connection without migration; second, the front-end flexibility allows business teams to experiment with diverse AI and Agentic solutions emerging across the marketplace without locking into specific platforms or requiring custom data modeling for each tool, as long as governance, guardrails, and guidance ensure appropriate data delivery to any agent, and source connectivity maintains proper access patterns, ultimately enabling CEOs to evaluate multiple innovative solutions simultaneously while data teams guarantee appropriate information reaches each experimental initiative. This trust-building journey positions business as pivotal partners enhancing data capabilities organization-wide, where centralized data access enables progressive curation and quality improvement, with business teams feeling increasingly empowered to organize data according to their functional requirements, recognizing their datasets immediately upon entry, and gaining confidence to work with AI without fear of breaking production systems, collectively transforming enterprise data strategy from IT-centric technical consolidation toward business-driven logical organization where domain experts drive innovation while data teams provide enabling infrastructure, governance frameworks, and technical connectivity ensuring experimental velocity without sacrificing security, quality, or compliance requirements.
keywords: business-driven AI, semantic layer, data federation, self-service analytics, data products
---

- So, a little bit about myself before we kinda jump into it. Adrian Estala, as you
guys can read up here. I'm the CDO at Starburst. I was a CDO before I joined Starburst, so oftentimes when I look at
these types of discussions, it's not from a Starburst perspective, it's from an ecosystem perspective, and so I hope to kind of bring
to you a broader conversation of strategy that includes Starburst. So very nice to meet everybody.
Roger, why don't you tell us about yourself?
- Yep. I am Raja Palaniswamy. I work at MUFG, manage the enterprise data and then do the data strategy
for the team right now. - Fantastic, fantastic. I had an opportunity
before we got started. I always love to do this. So,
I walked the room a little bit just to kinda get a
pulse for who's in here and what the interest is, and we have a, I won't point names, but I've got some chief
product officers over here, people that are in charge of product. I've got teams on this
side that we talked to that were really interested
in driving adopting on the business side, really
pushing business self-service, and those are two great topics. Poor Raja's gonna have to work around me. What we wanna do today here, kind of in the conversation is really bring to light the importance of letting your business
teams really feel empowered when they're driving the AI solutions. And AI is very generic, and I'm talking more on the GenAI side. I'm talking more on the Agentic side. I'm talking more about the
kind of conversational AI. Maybe it's a bit more simpler. I'm not talking machine learning. I'm not gonna let my business
teams kind of drive ML ops, but I do think when we get
business teams more involved on actually being creative,
owning the art of the possible with our AI capabilities, magic happens, and a lot of the customers
and business teams that I work with, I'm working
directly with business teams, getting them excited,
building solutions together. If you sat in on any of the
cloud sessions this morning, it's amazing, right? It feels so easy. The ability to create,
the ability to build, the ability to understand
how skills come together to solve a solution. These are all things
that our business teams should be able to own
and drive on their own, but there's a gap, right? There's a gap that maybe it's
where some companies struggle to drive that empowerment, and that gap really comes down
to understanding your data and being able to access your data, right? And so, I kinda draw this
up in three simple blocks, and Raja is down kind of
the journey over at MUFG, and so what I wanna do
here is I wanna kinda set the foundation for the talk track in three simple layers, and then I wanna dig
into Raja's experience and what they're doing at MUFG and the work they're doing to drive business-driven AI innovation, right? But let's start with the foundation first. The first part of any foundation,
as I said a second ago, the challenge is getting the data. What we do is we allow our teams to get data where it sits, right? So I don't care if it's in the cloud, I don't care if it's prem. I prefer it to be in the lake.
It isn't always in a lake. But Federation for a long
time is always what kinda made Starburst famous, right? That's what we've been
good at for a long time, and that's great, but if I can get to my data where it sits without having to migrate
it, whether it's in the cloud or on-prem, this next block is
what's most exciting, right? And now you're hearing
a lot of excitement. You're hearing a lot of buzz
around the semantic layer. It's this business-facing semantic layer that's the real game changer. If I can access my data where
it sits without migrating it, and I can start to organize that data into logical data products that my business teams can understand, I told Raja this once before,
I said, "We wanna create an experience when the business
teams walks in the room, they recognize their data." It's like walking in a family. You know your cousins,
you know your family. - Yep.
- You recognize your data. It's easy for you to understand. When you can create these
logical data products, now, I don't care where the
data sits, I can organize it into packages that my
business can understand, it's a real game changer. It's a true semantic layer where you're abstracting
the legacy complexity and you're giving the business
team something they can use. And when you've done that, now, business teams feel
a little bit more comfort. Now, business teams feel
a lot more confidence when they enter the room
and they say, "Look, I wanna test out a new agent in Amazon.
I wanna test out a new agent in any system. I just
need to get the data." If they can ideate very quickly because they can say, "I
need a little bit of this, a little bit of this,
a little bit of this. I wanna bring these governed, curated, secure data products into my agent and I wanna use them to
do an analytical exercise, I can do that because
the data is already there and I have the access in terms of security and availability that
I need to get there." Those are the three layers. If you wanna think about what's the bridge to get to business enablement for AI, it's getting access to the
data through Federation. It's creating a
business-facing semantic layer that they understand. In many cases, I build these
with the business teams. Raja'll tell you, we've been building this with his business teams, and the third layer is in just adopting these data products, right? Using 'em directly in BI or AI solutions. That's kind of the framework
that I like to talk about. You don't wanna hear it from me, you wanna hear it from Raja. (Raja chuckles)
So, I apologize for the long intro, Raja,
but I've set the stage. - Yep.
- Before I kinda jump into some questions, is there anything you would correct or anything you would add
to what I just talked about in that foundation? - I would say data needs
AI and AI needs data. You know what I mean?
- Love it. - It's a cycle. So, I think I would say,
we started the journey, like the traditional data strategy where we'll consolidate everything into physical consolidation,
move the data, curate the data, profile the data, and then
do things accordingly. We pivoted that and then
said, "Okay, can we create data products in a logical way?" And then those data products, or what Adrian talked about, I will add is the semantic layer is nothing but from a business product
lens in a corporate world, if you're from corporate
banking, you have lending, like we have term loans, several
of those business products, we aligned our business products and data products to be identical, so when a business user comes in, there are business data producers who create these curated data sets from the semantic layer
so that they can create, if, let's say we have
commercial loan operations, that team wants to see the data
quality of the loan booking. They are able to really curate the data from the core products, and then create a functional data model or a data product that
is specific for them. So, we gave the business users,
we created three personas to Adrian's point,
business data producers. We call them specifically
business data producers, not IT or a CDO, am I right? The data elites are in with the business, so they know and speak the same language that they can understand the data, so I would add that for
us, it was more towards how do we enable business
for self-sufficiency. They should not be coming to IT or data elites to understand
what data is there, how it is related to the product, how do I get access to that data? So, this Starburst
provided us that capability to pull data from multiple data sources, whether it is distributed
environment, whether it is SaaS, whether it is PaaS, whether
it is embedded systems like Salesforce or any of those, so we pulled that data in to create the curated data products. That enabled business for
them to be self-service. - Perfect. Was there a trigger, Raja, that kinda, I don't wanna say forced, but really kinda got you guys to rethink your data strategy? At what point did you guys say, "Look, we've gotta do something different. We have to maybe move
closer to the business. We have to drive more self-service. We have to find a way to
get our business teams to trust more data." I don't
wanna give you the answers, but (chuckles)-
- Yeah. - What was the trigger at MUFG to kind of force you to
rethink your old data strategy? - I think time to market was the key. How do we enable... Because businesses making money as of now, how do we in increase our
revenue generators' capability, who are sitting within the
business, time to market? Like how soon can we get the data for them to prepare
the data for themselves rather than they coming
to IT, I'm from IT, coming to IT or CDO. How do we enable the
business to prepare the data to be self-sufficient? That was the pivotal point that triggered us to be in this journey. - Love it. Let's give the audience an idea of what a semantic layer might look like, without giving away too
many of your secrets, and so I'm gonna stay high level here. When I talk about a semantic layer that business teams can understand, and then, forgive me, you
stop me if I go too far. Within MUFG, we've got this
notion of core data products and functional data products. You can think about the
functional data products as derivatives of the core. Core data products are well curated. I got data from maybe a hundred sources and I've organized them into a small set of core data products. I've got one for customer,
I've got one for channel, I've got one banking, I've
got one for like kind of all my different big things, and then functional, you can imagine having
a lending team saying, "I need a little bit of that
one, a little bit of that one, a little bit of that one,
to make this data product, and that a little..." And so they're building
their own derivatives in their function to kinda
answer their specific functional questions or analytical needs, so to speak, right? So, that's a model that
we're building at MUFG. Now, tell me about your consumer, your business teams on the function side. Do they feel empowered? Are they all jumping in,
or how is that working? I didn't mean to do that. My
kids would go crazy, but... (Raja laughs) (Adrian laughs)
- It's a journey. - Yeah.
- We have mixed business users. Some are very excited to see the data. Some are like, "Okay,
get me halfway through. I need to understand the data." So we mixed up that with
data literacy programs so that we can educate what data is there, how they can access. So it's mixed, like 50 50. I would say some of the
users who are power users, they are like, "Okay, I have my data where I need from 50
different systems. I'm happy." And then they can sail on their own. They are self-sufficient. - We're empowering business teams to organize data in the
way that they need to. Now, let's go back to the
third box, the AI box, right? 'cause that's kinda what we
really wanna talk about here. If I can build a data
product that's curated, the secret is business metadata. It'd be one thing if
I'm just building data from technical metadata. - Yep.
- If I build a data product with business metadata
at the column level, at the table level, at the role level, I've got real business
descriptions of that data product. When you put that in front of an LLM, you get very accurate analytics, you get very performant analytics, and so we can sit down
with a business team, a lending team for example, and say, "Here's your lending
data product. Go for it." And it's not that you're
just giving them a solution that they're gonna own forever. You're giving them a capability that they're going to evolve. You want your business teams to be able to look at the capability and say, "Wait a minute, can it do this? Can it do this? What if I add this skill? What if I add that skill?" The magic happens when the business teams understand the data, and
they get the confidence to work with AI. They're not afraid to break something, because in a data product,
you're only exposing this data. That's it. Nothing else. In a locked-in system,
there's really clear, I love your three Gs.
What are your three Gs? - Guidance, guardrails, and governance. - You're giving 'em the
guardrails and the governance and the guidance to experiment, and so at the end of the day, you're decreasing the time to experiment and you're lowering
the cost to experiment. So, I always say, I wanna do
10 AI projects in 10 weeks versus one AI project in 18 months, right? And they're all going to succeed, but you can succeed on the three and keep going forward
and fail on the seven. If that's the, that's probably
not the right failure, right, we all want, but that's the reality when you're experimenting. Not everything works. On the AI side, Raja, I know
that we're just kinda starting to build that foundation
for those data products. How are you looking at the
Agentic front end to this in the future?
- I think we are looking at the AI landscape in two forms. One is to make use of
all the data management, enable the data management capabilities, whether it is profiling,
whether it is lineage or any of those. Second part is we want our business users to start chatting with the data. We want our business users to say, "Okay, can you give me
all the middle-market banking customers." We wanted to provide them that capability, and then we provide them that list. We also make sure that we integrate that with our authentication mechanism. We don't want middle-market
banking customers to be exposed to who is
not authorized to do it, so it's a mix of getting the chat, using AI to enable data products, get the lineage, get the
profiling, get the cataloging, tagging, those kind of things. That's part one, because
by having Starburst, what's happening is it's enabling us to go into one location, rather
than 50 different systems that we have to go and do that across. The other part of is people can, as soon as they come to
Starburst, they can click on it. We want to invoke the
chatting with that data, using the Agentic
features that is available to us, using Amazon
Bedrock and other features, where everything is in one box so that they can come to something called real data marketplace. So, that's kind of the objective of that. - There's a point that I
wanted to underscore there, 'cause it's agility on the two sides. If I have a semantic layer that I built with my business teams, and
the semantic layer, logical, doesn't care where the data comes from. You can leave it there.
You can connect to it. It's also the agility on the
front of that semantic layer, saying, "I can build an agent." I mean, if you look around
here, there's so many cool AI or Agentic-type solutions, right? If I'm a CEO, I wanna try them all, but if every one of them is attached to some core platform, it's expensive. If every one of them requires me to go model data a certain
way, it's expensive. If I can deliver data
products to any agent, and I can tell my business
teams, "I've got the guardrails," I'm gonna steal this from you, "Got the governance and the guidance. I will deliver the data to you." Maybe you can build, you
can try any agent you want on the front end, I don't care. Build any agent. I'm gonna make
sure you get the right data. Use any source, I'm gonna
make sure I connect to it in the right way. It's just incredible flexibility
and incredible agility and ultimately offers you at longer term, the opportunities to make better choices. - Yep. Yeah. What I would add is in this journey, business plays a pivotal role. Business is in partnership with us for us to enhance the data
capabilities across the board, and that comes by, I would say it's a trust-building scenario where we allow them to prepare data, and also, it's a centralized location where you have all the data
that you can really curate, get things to the next level. In fact, we improve our
data quality indexes by pulling data through Starburst so that when it's fed into any AI for modeling, it has much more rich data quality. - I like what you said earlier,
we were talking, you said, "I use AI for data and I use data for AI."
- Yeah. Yeah. - Can you explain that a little bit? - Yeah, so, when I say I use data for AI, is to learn through the LLM models, the entire content that is rich content that we have in the organization. Whether it is structured data
sitting in our deal file, whether it is, sorry, unstructured data that is sitting in our deal file, or structured data that is in our systems, so that data, we can feed it into AI for learning more about the insights. The other side is where
we need AI for data, we wanted to use AI for tagging purposes. We want to use for AI
for lineage creation. We want to use AI for profiling. So, those are the insights
that we can create. So data for AI and AI for data. - Love it. I love it.
- Yeah. - Fantastic. Fantastic. I'm gonna pause to see if
I've got any questions. (crowd drones) Awesome. Thank you very
much for your time. Really appreciate your interest. - Thank you.
- We have a booth, just down the hall here at 550. Happy to talk some more. - Yeah, thank you. Thank you guys. (crowd applauds)
Thank you.
---
video_id: kTT3vnC3qyg
video_url: https://www.youtube.com/watch?v=kTT3vnC3qyg
is_generated: False
is_translatable: True
---

- Thank you. - Thank you very much. So I'm Ryan McMahon from
Cambridge Mobile Telematics. We're a technology company
that measures driving behavior, and our mission is to
make the world's roads and drivers safer. And we do that today, or historically we've done that, by identifying and understanding the risks that create crashes, and understanding what
risks go into that crash. And then being able to help, and identify how to prevent that, is really our core mission. And we do that by understanding and identifying a vast array of sensors, and processing that
information on AWS today. And for the most part,
over the company's history, it's been used on an
individual one-to-one basis, meaning that the individual
driver is measured and we process that information and provide that information back to them. We also detect crashes, respond to them, but over time what's happened is that data size has
gotten even more complex, because we're gathering sensors, as those sensors have come online over the company's history. We started with the initial version of feature phones, have
gone to smartphones. We use proprietary tags that
we manufacture ourselves, and we're also expanding
into other sensor platforms. All that information
today is processed on AWS, but it's been processed and
used for individual drivers. And the reason that we
do this is to identify and understand those basic
risks, so that we don't get to the top of the pyramid, the top of the pyramid
being roadway fatalities. And if you're not familiar, unfortunately, over 40,000 people die on the roads here in the US every year. But even more than that,
we're talking about over a million people globally, and we're a global company. So over 15 years, our focus
has been on individual drivers. So this session is about geospatial, and you may be asking yourself, "How does the two things
connect back to them?" Well, what happened was we started to do research in the topic, and identify more than just
the individual driver risk. We started to identify a
host of features that go beyond the individual driver, because when it comes to crash risk, it's not just the
individual driver that leads to that negative outcome, that leads to those
injuries and fatalities. In fact, the vehicle
has a large role to play and the road does as well. And we've expanded significantly onto that last phase into
understanding road risk. So the goal is to predict and identify where crashes
are going to happen, because a crash in itself, if
we could just simply identify where those serious injury crashes happen and address the issues that were there, then we can remove those
fatal crashes from the past. But the reality is, that
it's not predictive. As sad as each individual crash
is that leads to an injury or fatality, in and of itself it's not predictive to identify where that next fatal crash or injury
crash is going to happen. So you have to identify the
features that are below that. What leads to the risk to
get to the point to identify where a crash is going to happen? And that's where AWS, and AWS came into play
in a huge way for us, because we're processing this, an enormous amount of data every day, over a trillion data points are coming in. And we had a problem when we
wanted to move to road risk, because for an individual driver the processing that goes
into play is important, but it's not in the same factor from a geospatial perspective. So we had to take two steps
further to get to the point to be able to identify those issues. And this is what we built. So from this now, and this is an example,
this is a road in Arkansas, just spoke recently at the
Arkansas Safety Summit, and their director of
the DOT, Jared Wiley, invited me to come and
present, and this is one of the data points that I showed. And this is an aggregation
of hard breaking events that occur over a month period of time, over a three months period of time. And when you look at the
aggregation of those events, it becomes clear when you actually start to get under the ground. But we didn't identify
this issue from an image, we identified this issue
from human behavior. But if you look at the
image, it becomes very clear, the stop sign's occluded. So if that stop sign's occluded, you know, there's many branches and trees that are blocking
stop signs all over the world. But how many can you get
to the point to identify where the human behavior is concentrated and aggregated to get to the
point to identify that risk? So the challenge is, that
if you get to this point, that you have all this information
to identify the behaviors that lead to crash risk, and you can aggregate it together, how do you display it in a
map that's useful to the DOTs, to the highway safety offices,
to the people, the EMS, to get to that point, to be able to reduce those risks as they occur? And really the question came down, should we use road segments? So we take all this information and load it into pre-existing
mapping coordinates. And really what happened was we said, "We're going to use H3 hexes." But the problem was, at that point, AWS didn't support taking that data and moving into H3 hexes. So this is really what
AWS has been able to do, is to take all of that information today, and give us the information that we need to identify at a massive level. And what we're doing now is
loading over 5 billion records every single day into
a system that opens up and can do something like this. So this is a stop sign in Washington D.C. I went there in person,
I took this picture, same issue, same exact issue. You can see that there's a stop sign that's secluded by a tree. And what's happening? Well, people are getting
a near miss crashes. And today, the way that
these problems are solved, if you're a DOT or
highway safety office is, we wait for the bad thing to happen, because the currency of risk today is unfortunately the crash itself. So we're moving two steps beyond that. And AWS, if AWS didn't
have those capabilities, we wouldn't be able to take
this massive amount of research that we'd already done
in identifying risk, and be able to bring it to the solution to make it easy to use. And effectively, what I try to term it as is Zillow for road safety, is looking at, from a mapping perspective, how do you identify and
understand those risks and make it translatable across the globe? And this is a huge scale of undertaking to identify those behaviors,
to ultimately get to the point where we can move
further down the pyramid. And from a technical
perspective, the partnership that we had with AWS, 18 months ago, we couldn't have done this. And it was that partnership
that led to this development. So frankly, I'm so impressed. And to talk more about, really that work of getting
further down the pyramid, and how technically we got to that, I'm gonna hand it over to Ravi from AWS. - Thanks, Ryan. So as you heard... Thank you. Redshift went down the path of building spatial capabilities into a cloud data warehouse. We went down this path
some seven years ago, eight years ago, and we're
pretty far along now. And the key to what CMT, Cambridge Mobile
Telematics, has built into their StreetVision platform is using the spatial data together with the spatial query
functionality with Redshift. So you don't need to learn anything new, it's all done in SQL, right? So you have all the spatial capabilities, and I will talk about some of the newer capabilities we've built, which is specifically the H3 functions, the hierarchical hexagonal indexing, which is an open source initiative. It started at Uber, I believe, but it is a huge leap in terms of spatial performance, right? So the question on top of all of your minds is: Why Redshift Spatial? All of you have probably
heard of Amazon Redshift, one of the first
cloud-native data warehouses to be released, almost 14 years ago. The reason is very simple. Redshift has the right architecture to do massively power processing, MPP architecture from day one, right? So the first cloud data warehouse to be built on MPP architecture, it can handle petabyte scale data and it operates on columnar data. So you get all the
benefits of columnar data, your vectorized scans, for really, really
efficient query processing on read queries. And that lends very, very well into petabytes of spatial data. The volume of data that CMT has to deal with is massive, right? It's in the petabyte scale. So couple that with the highly precise, numerically accurate, robustness of our spatial implementations,
whether it's WGS84, the SRS standard for implementing spatial projections on
an ellipsoid earth model, and leveraging all the functions that we're continuously adding to our spatial portfolio functions. The most recent of which
is the H3 functions, right? And those who are familiar with PostGIS libraries are
probably already familiar with some of the spatial capabilities in Postgres like databases. So we follow the same
syntax, the same sort of functional equivalence. So when we first embarked on this, we launched GEOMETRY data type as the first class data type in Redshift. And very soon, a couple years later, we added GEOGRAPHY as well. So geometries are more
for 2D, two dimensional, and non, you know, non geoid based, so non lat, long, latitude,
longitude based coordinates for short dimensions where
you don't need the projections and accuracy, numerical accuracy
of geography data types. So together with GEOGRAPHY and GEOMETRY as native first
class data types in Redshift, you have the building blocks to handle all spatial data in Redshift. And then we are now up to
over a hundred plus functions, spatial functions, implemented
natively within Redshift, and most recent of which is the H3. And I'll talk about H3 in a bit. So here's what it looks like when you run a sample
query in Redshift, right? So it's pretty simple, you create, just like any
other cloud data warehouse, you create a table, you
load some spatial data, and you use SQL to query it, right? And you use all the
built-in spatial functions, all those a hundred and plus
functions that I talked about. And voila, you have your
spatial analytics capabilities, you can mix and match spatial data type, non-spatial data types like anything else. So this is pretty much standard now, many cloud data warehouses support it, but Redshift with its architecture for very high performance, really excels in processing spatial data. And what's special about the functions, the spatial functions, is that, for example, you can do
these kind of visualizations. So what you're seeing here
is, let's say this is a map of Berlin, and let's say
you basically want a, let's say you have a table
called "Accommodations", with all the coordinates
of hotels in that polygon. Those little clouds that you see are the
parameters of the polygons. And the query here is
basically showing you, "Find me all the hotels
in that polygon", right? So that's, you submit
a shape, a shape file, and you extract the latitude, longitude, and you simply use a regular SQL query. And that's it, you get
all the list of hotels. So this is a very, very simple query, but think of it as the building block for processing at scale
millions and millions per minute or per second in some cases, right? So that's the scale
with which it operates. And some of the spatial formats, we obviously see the shape files there, but we also support
WKT is well-known text, WKB, well-known binary, and the extended versions of those, WKT and WKB, and geojson,
and many other types. So we have a lot of
flexibility in terms of reading and writing spatial data formats. And this is, I don't want to,
you can look up the docs here, but this is some of the sample of the hundred plus
functions that we have, and it's continuously growing. What you see on the yellow or orange there is what
we've recently added. We started with the five
functions that are most needed by their StreetVision application. There are several more H3 functions, and we plan to introduce them, but this is where we started, right? So the question is, what is H3, right? So H3, as I said at the start, is a hexagonal hierarchical indexing system. The big problem as you saw
in a couple of slides ago, is the old way of querying things. You have a polygon, right? You define a parameter, and you want to find
points within that polygon or some other variations of it. So what it boils down to for the SQL engine is a
Cartesian join basically, which is complex, expensive, and exponentially huge, right, so it can get bogged down. With H3 indexing, you
have pre-computed indexes for your locations, right? So each index, each cell's index is the location itself, and you can choose the resolution
that's of interest to you. There's 16 levels from zero to 15, and you can choose the
resolution that you want. So a lookup is lightning fast. To see how fast it is, here's a comparison that you'll see. You can save 98% of compute, the old way of doing lookups versus the new way of
doing lookups, right? And this shows you some of the other's resources about memory, CPU time, et cetera, et cetera, and query response times. So H3 is a game changer for spatial lookups at scale, right? So you can save like up to
85% on your Amazon, you know, charges if you want,
your Redshift charges, but just by using H3. Okay, so some of you may
be wondering, you know, we talked about, you know, spatial Ryan talked about the
StreetVision platform and CMT. So how does it fit into some of the NLP capabilities. He talked about, you know, they're using Bedrock and some of the models that Amazon has, the way it all fits in
is through Query Editor, Amazon Redshift has the Query Editor, which is our SQL ID, or SQL interface if you will. It's been growing in features. We now support Jupyter-style
notebooks for SQL. And it has full integration
with Amazon Q SQL, which has integration with all the models that Amazon has access to, both Amazon developed
and third-party models. So what this gives you is the ability for non SQL experts to be able to use a SQL data warehouse
like Amazon Redshift using plain English, natural
language processing, right? And the big advantage, you might say is, why should I use this engine versus, you know, many other query engines that are also NLP capable. The biggest advantage is that Amazon Query Editor
v2 is fully integrated with the Amazon Redshift
cloud data warehouse. So you have full query
history, full metadata, and you have full context of the schema. It does the schema
crawling, it understands what you're trying to query,
what tables and columns, and it understands from your query history exactly what you're looking for, right? So that is a huge difference. And some of the other query
tools within the AWS portfolio, like QuickSight are also building this integration with Redshift. And finally, generative SQL. So translating NLP, your NLP in plain English, the intent of your query is where the generative
part comes in, right? It looks at your history, like I said, but it also divines
your, your intent, right? And this is where is, you know, it really is a game changer, because it can sort of
do predictive queries, and you can of course have the ability to edit it in your notebooks, right? It generates the query,
you can execute it as is, or you can edit it and submit it, right? So that is one of the biggest advantages of generative SQL integration. And finally, as I said, I think
I've already mentioned some of these things, but the biggest
advantage is it understands the context of your schema, the tables and the layout, and the history. Taking those two together is
really the big difference. If you use a third-party BI tool, you will be missing some of that context, because they don't have the
level of integration that we do to our own metadata, Redshift metadata. So that is the real differentiator. So with that, I'd like to thank you folks for taking the time to attend today. And we have a few minutes left here, and I will open it up for questions, if any of you have it,
we will take questions, for Adrian from Cambridge
Mobile Telematics, Ryan, or myself, I'm from
Amazon Analytics team, so more than happy to take questions. Thank you again for attending today. (audience clapping)
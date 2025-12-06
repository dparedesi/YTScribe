---
video_id: pNOn9DHlArQ
video_url: https://www.youtube.com/watch?v=pNOn9DHlArQ
is_generated: False
is_translatable: True
---

- Welcome, everybody, to DAT447, using graphs over your data lake to power generative AI applications. Quick shout-out to the tech team here who worked through a couple of last-minute presentation issues. I'm Brad Bebee, I am a director
with AWS for Amazon Neptune and I'll also be joined today by my colleague Dr. Umit Catalyurek, who's an Amazon scholar and
is also with the Neptune team. Before we get started,
could I see a show of hands of folks who are using graph
processing on your data lake, either graph algorithms
or graph query pieces? Okay, a few. How about people who are using different techniques, including graphs, to improve the accuracy of
generative AI applications? Okay, cool. Well, it should be a good talk. Graphs are awesome, and the reason that they're awesome is because they allow you
to use the relationships in your data to be able to solve
problems and ask questions. In a graph data model,
relationships themselves are first-class entities. You can query them, you can traverse them, you can write algorithms and programs that iterate
and loop over them. And this enables all kinds of super interesting and
valuable graph applications, from finance and fraud detection to knowledge graphs and engineering models to Customer 360 and profile pieces. One of the things that I've seen, and I joined AWS almost 10 years ago to start what's now the Neptune service, is that the most successful businesses and companies and applications, they find a way to use a graph to do something remarkable for their customers, to provide some sort of unique
and interesting function. A great recent example of this is Wiz. Wiz is a large cloud security
posture management company. They started with a vision of the world as a graph and context as king, and they used that to reimagine cloud security
posture management. And we had the benefit of being able to watch them along the
way over a few years. And one of the things that
struck me about what Wiz has done that many other people have
tried in different ways is the way that they use graphs not just to connect data, but also to help explain findings and give you a way that
you can ask questions and understand quickly, why is this the most important thing or why is this the right answer? We often quote that there
are many, many problems in the world that can be solved by graphs, but as practitioners, as people who are building applications, we need to keep in mind that graphs themselves are
not an intrinsic benefit. You're not actually, if your end state is in,
"Now I have a graph," you haven't really accomplished anything in your application. And over the last year, 18 months, we've seen a huge increase
in the number of customers who want to improve the accuracy of generative AI applications, who want to use data on their data lakes and try and get more insights. And so today, what we're gonna go through is a couple of different strategies about how you can do that, how you can do useful
things with your graphs, where your data lives. And so I'm gonna introduce Umit to take you to the next part. - Good afternoon, everyone. So I'm gonna walk through two of the strategies we have been using and you can use in your
applications as well. So the first one we are gonna look at, taking your data from your data lake and using it in a graph. These cases, you know
that there is a graph, either you created the graph or you want to create the graph, and we'll see how we can do this today. So Neptune Analytics built on top of a unified graph data model. So it's called one graph model, and it's a logical model that unifies both property graphs and RDF so that you can actually
load both RDF data and the property graph
into Neptune Analytics. So you could import your data, start your graph with that way, but after you start the graph, you can also use tabular data that sits in your data lake using your favorite graph
processing language, openCypher. So you can query the data sitting in your
data lake with openCypher and you can import and export
to your data lake as well. What are the use cases to do those? Let's say that I have an airline dataset. I have the metadata
information about airports and their connections, but I don't have most recent
airline flight informations. Let's say that that sits on my data lake. We can actually read
that and process that. We can read that and
federate with our datasets. Let's look at how we do those. The first one is reading
from your data lake. So we developed Neptune read algorithm. What it does, if you have a dataset, either a Parquet format or CSV format, you can load your dataset. All you have to do is tell the format, this is the format, Parquet format, and it sits in this S3 URI. Then what it does, it
returns every single row of that data to you, and you have the direct access to columns and you can use those columns. You can do the same thing
with CSV files as well. Okay, so let's look at an
example how to use this. Let's say that the scenario
I've just described, we have the S3 data table, S3 file, and it's a Parquet file and it consists of multiple columns, like carrier, flight number,
and origin and destination. And you wanna read that. You simply tell, this is the URI, this is the Parquet file, and it returns this row by row. It's an openCypher. You can use those columns as you wish. You can take carrier information as it is, you can concatenate origin and destination with an arrow between, and you can produce the output like this. This is just reading your graph. You're reading data in
your graph language, okay? Of course, we can do more. We can federate the data. Let's say that you already have the airport metadata
information about the airports and what you wanna do, you wanna get the most
up-to-date recent flight numbers by each carrier, okay? You can start your openCypher query with a MATCH clause asking for airport one and airport two and specifying their code to be JFK and Las Vegas. So you're trying to
find all of the flights between those two locations. And we call neptune.read,
giving the same Parquet file. So it's returning each
of them but row by row. So what we wanna do, we wanna filter that so that the airport one and the origin and airport two and destination match. If they match, you wanna collect the carrier information and all of the flight numbers, but you wanna combine all
of those flight numbers as a set, basically, and you can use a collect
intrinsic for that and you can return the results and you'll get an output
of something like this. Okay, so we federated
what we have in our graph and what we are reading
from data lake, right? So we can also augment
our graph with the data. Let's say that we wanna create an edge between airports. We wanna create a new edge, we already have the
route edge between them. We wanna create a new edge
flight for every carrier that's flying between those two airport. Okay? So for example, the first row shows that between JFK and Las Vegas, B6 carrier is flying. So what we can do, we'll have a very similar cipher query. We'll again specify the first node and this second node as JFK and Las Vegas. We will have the same filtering. This time what we want, we just want the distinct
carrier information, because the same carrier
may have multiple flights. We just want one of them. We ask with the distinct, and we can actually create a
new edge with this information and augment our existing data. All right? So that was strategy one, when you have just data and you either have a graph
or you don't have a graph, you either get the data and process like a graph
or augment, et cetera. So these are simple cipher queries. What if I wanna do something more? What if I wanna do some
graph algorithms on that? Okay, so what's the graph
algorithms useful for? There are many graph algorithms and they serve many different purposes. In one scenario, let's
say that I have a graph that contains technical
research information, okay? And I want to understand the importance of a research or researcher. Okay? So I may have a graph of airports, I may wanna understand
the importance of airport in terms of the closest
airport to the other airports, or I may have a customer graph, I may want to investigate the most influential
campaigns I can run, okay? Or I may have financial transactional data and I might be interested
in identifying frauds. In these cases, we use graph algorithms. Graph algorithms will run on whole graph, not just giving a single agent to pairs. And let's look at one
graph algorithm, okay? So one of the most
commonly known algorithm is Google's famous PageRank algorithm. Many of you might already familiar. My apologies, for the repetition, but how do we define the importance of a vertex? So to find out that, we need to look at, what are other vertices
pointing to that vertex, right? Who is following you, right? So that's the first step. The next step is for those, of course, we need to
repeat the exact same step. We need to figure out who
are following those people. As you can imagine, this goes recursively for
the whole graph, right? So the PageRank algorithm basically operates like this. For every single vertex, the importance of a vertex is the average of the importance of the
vertex connects to that vertex. That's one way of describing, and that's the formula
that I'm showing here. So the second term is basically getting all the importance of the vertices that are pointing towards me. The first term is some randomization so that you can do random jump and smooth basically the process. Of course, this algorithm can be implemented in many other ways. So this is the one looking from
the destination perspective. You can think of this
looking from the source, you may distributing your
importance to your neighbors or another way of looking
at, for every single edge, you take a ratio of the
source's importance, and it's giving that to the destination. So there are different ways
to implement these algorithms and how your data is laid out will define which one of
them is performing well. Okay? So, but you don't need to worry
about all of these things, how these are implemented, because we implement this algorithms as efficient as possible
in our data structures. Okay? All you need to know is how
to run these algorithms. Okay? So this is the cipher
call to run PageRank. We have two versions of the PageRank. This one called mutate. What it's doing, it's calling a PageRank
on the existing graph. It's asking the result of the PageRank should be written to the
property called score. Basically a PageRank score. Okay? So PageRank algorithm, I guess I skipped a little bit too fast, is not a one-pass algorithm. You need to go over the
graph multiple times, you need to do that
iteration multiple times, and you either user decides
how many times they want to do, maybe you run this algorithm
multiple times in your graph and you know that some
numbers is sufficient. Generally, PageRank algorithm, 10, 20 iterations more
than sufficient, okay? And you tell which
vertices you wanna run this and which edge labels you want to use. And you run the algorithm. Of course, after you run the algorithm, you have the score in your graph. If you want to integrate this score with other processing systems you have, you want to transfer
this to your data lake, you can do this by
using an export comment. You can basically specify, "Hey, for each every airport I choose I want you to write the score I computed. And this will give you a table in basically a table format with each of the PageRank scores. Okay? So that's one of the algorithms. So another algorithm commonly used are centrality algorithms. Centrality algorithms are useful to identify the important vertices. In this toy graph, you may identify the
source of the problem, the guy, the culprits, the Arthur, the guy hiding himself, sits in the middle of
all of the connections. So obviously, Arthur is very vital for passing the information
between those two sites and also sits in the middle of the graphs and close to everyone, right? So there are different centrality metrics. Closeness centrality is one of them, and closeness centrality, what measures, it measures how far each of the vertices from you, okay? And it normalizes. The challenge, obviously, to run this algorithm
in the whole graph fast, so let me give you the
just simple formulation and algorithm to explain how this algorithm in general works. So given a graph, what you do for every single vertex, you go over in the distance
to all other vertices and you sum them up. So you compute how far this
vertex from everyone else, and closeness centrality is the reciprocal of all the vertices, all other vertices, and minus one divided by how far you are. This is one of the
formulation of the centrality, which just basically normalizes so the number is between zero and one, and easy to interpret, okay? If you run the closeness
centrality on this toy graph, you'll see that Arthur's
closeness centrality is very high. So you can identify that. How do we do this? So the algorithm starts with, for every single vortex, you need to compute its
closeness centrality. For every single vertex, what you need to do is you need to run either a shortest path if your graph is weighted or simple BFS if you're
running an unweighted graph, and then you write the
output by normalizing. Okay? So I just wanna highlight, this BFS is obviously your
standard BFS algorithm, or single source shortest path. The best you can do is you need to go over all of the edges
at some point in time. Then an outer loop over all the vertices is gonna take quite a bit time. So this is a very expensive algorithm. So obviously, no one is running such algorithm in large scale. What you do, you usually sample a random set of vertices, okay? And in Neptune Analytics, we do much more than this. We do other HPC optimizations like vectorization and and
parallelization, obviously, to make this algorithm
run much, much faster. But again, for you, what's important is how to use this algorithm, right? So all you have to do is tell, "Hey, I wanna run this
algorithm on airports." And when you call, you can either specify how many source vertices you wanna give. If you give a maximum number, you're gonna run an old, old graph. And you specify which
routes you want to run, then it will return the score, and we will here printing just the description of the airport, which will give you a human-readable form and showing that Charles de Gaulle is the airport that has the closest central route. Okay? So, we have a suite of algorithms implemented in Neptune
Analytics that you can use. I just showed you just two of them. We have different class of the algorithms, like
pathfinding algorithms, simple breadth for search, looking the connectivity
between a single vertex and how others are reachable. Shortest path, again, starting from a single vertex, using the weights and how
far other vertices are, or if you're interested with
just going two, three hops and just getting a limited set, you can either use topK hop-limited BFS or Ego network if you're
only interested one vertex in its neighborhood. Centrality algorithms, I
already mentioned two of them, and degree is obviously the third one, just computing the degree of the vertex. Then clustering, if you
wanna find related vertices, this will be a great
algorithm for fraud direction. So you can run any of those algorithms
depending on your graph. So starting from the simplest one, which looks at weakly
connected components, how the works are connected, going to the label
propagation and Louvain. And we have a set of algorithms to look the similarity of the vertices. And most interestingly, which
Brad will talk about more, we have about vector
algorithms that you can use to search the vertices that are similar and use those vector distances. So the vectors come from
LLM, GNN, many other sources, whatever you have the vectors,
we can use the vectors as the vertex properties. So maybe if you wanna play it yourself, if you wanna see how you
can use the algorithms, this will be one use case
you can track yourself. If you use the QR code, you
will get to one of the notebook that we set up with the example case. So in this case, the case
study is about using PaySim, which is mobile payment transactions. And we are trying to find the fraud. So the data is in S3
tables in this case, okay? What you can do, following the notebook, you can load the data
from S3 tables to a graph, then you can run Louvain
algorithm on that graph, right, to identify the communities. And you can obviously export
it back, those communities, to be used by other upstream
processing you may have, or you can even use the visualization enabled with the graph explorer. Okay? So I described the cases where you know that there's a graph and you wanna run some algorithms. So now, Brad will take over you to vectors and when you don't even need
to know that there's a graph. - So now that we know
about graph algorithms, let's look at a different strategy where we combine vector search and different kinds of graph traversals. So if you think about
searching in vector space, when you find things that are similar, you're taking a distance measure from a basically a
high-dimensional matrix. And it's a super powerful technique. It lets you find images that are similar. It lets you understand that a zucchini and a courgette are most
likely the same thing. But if you're trying to build
an accurate application, you're trying to explain
the results to someone, vector similarity search is
really kind of a black box. You can't tell why some
things are related. Contrast that with a graph
traversal or a graph search, and if you ask something like, "Why are Wong Xiulan
and John Doe related?" you can answer it with a very explicit traversal and say they're related because they acted
together in these movies. And it may not be as flexible
necessarily as vector search, but it's certainly very
easy for you to explain. And so, one of the things that we've seen customers
do is look at combining these different types of search. And so this is one
example of hybrid search where a user asks a question and you use a combination
of different techniques, maybe a conventional inverted text index, a vector similarity
search, a knowledge graph, and you combine those results to be able to give the
user a better answer. Building on what Umit showed you, it's very straightforward to create a graph with vector embeddings. You simply add this additional
parameter at the bottom here, that's the vector search configuration, and you specify the
dimensionality of the vectors that you wanna store, and then you can load the
vectors into your graph through a fairly basic serialization. We'll also take a look
at a Parquet example in just a second. So if we go back to the airport routes, and suppose that we have in S3 vectors or we've made some LLM calls and we've created vectors
for our different airports and we have those in a Parquet file, we can use the same kind of
technique that we used before. In this case we're using
the neptune.read function, we're calling it to read the Parquet file, but rather than federate the results or use them in a query, we're actually then matching
on the airport codes and storing that embedding
as a property in the graph. And then we can go on and do other kinds of vector
search type operations. Now, another way that you can combine vectors and graph traversals is not necessarily starting
with a vector search. This is an example that's
a little bit abbreviated, but it's taken from one of the fraud teams at the amazon.com. And as you can imagine,
on a site like amazon.com, it's quite a challenge to keep up with various different kinds
of bad actor type behaviors. One of the things that
this group is looking at is who are trying to sell
books that were generated by generative AI. And the way the technique that they used was they started off by
doing a graph reversal to match something that
they had in their graph, so in this case, in their product graph, and in this example we'll look at, I wanna look at books
about travel to Las Vegas. They took that graph search result and then they combined
it with a vector search. So, show me books that are similar within some topK of the travel books that
I specified in my graph. And then they combine
this with information that they had in their graph already related to various different
scoring that they use for sellers, listers, or buyers that have been flagged as suspicious. And so they can start with
something they're interested in, expand out and from the vector
search to find other things that are similar to it, and then combine that
with the relationships about who is known to be selling, listing, or otherwise producing
this kind of content. So a very interesting way
to combine the vector search with the structured graph piece. If you wanna do more or learn
more on this particular case, you can use this as
also a Jupyter Notebook that you can use to try and combine vector
search with graph search. What else can you do
with vectors and graphs? Well, one of the techniques
that many people have used and tried is to use retrieval
augmented generation to improve the accuracy of responses by bringing in specific
data that might be relevant to your organization or to your business and using that to try
and provide grounding. Well, with GraphRAG,
you can take that sort of retrieval augmented
generation architectural pattern and bring in some of
the explicit information that you have from a graph. And we'll show you briefly an example where we're creating the
graph automatically for you. But if you think about in this diagram, some of the different kinds of algorithms that Umit talked about, there's lots of different
ways that you can envision to combine these things. So you can do various different kinds of ranking or other pieces. So, you know, there's a lot
of different opportunity to use different
combinations of techniques. With Amazon Bedrock Knowledge Bases, you can do this automatically if you create a Bedrock Knowledge Base and you choose GraphRAG as the option. What will happen is in the
generation of the chunks from your RAG application will automatically build a graph. The graph is what we call lexical graph. It conceptually looks something like this. So typically, a RAG application takes the documents and chunks the documents in some way, embeds storage vectors
along with those chunks. And in this case, when you use Bedrock
Knowledge Base as GraphRAG, we also use an LLM to extract entities and facts that are occurring
within those chunks. And so we automatically create a lexical graph behind the scenes. You don't need to have any graph expertise to be able to do that. But when you ask questions in a particular multi-hop,
multi-stage questions where you need to assimilate information from multiple different sources to be able to achieve a result, you're able to get the
benefit of the relationships and the connections in the graph in what's called the re-ranking phase. So typically, in a RAG application, you'll do a vector search. That vector search will have
a topK and the topK results. There's often a re-ranking
where you might take other kinds of metadata, or in this case where
you're using the graph, and effectively we're boosting the results that we're presenting back to the user based on explicit
connections in the graph. And so as a quick example, if this document through this
chunk was the topK result or was it one of the results
returned in the vector search, these other documents
may not have shown up. But because we have this lexical graph with these connections where
we can see that there's a fact that's connected to these three entities, the re-ranking phase of
this GraphRAG integration will effectively boost the results. And so that allows you to
get more accurate results. So how well does it work? This is a case study from Trend Micro, obviously a computer security company, and they built a user-facing
security chatbot, and they've built it and
deployed it over time, combining various different
techniques to build graphs, use GraphRAG, use Bedrock, use Neptune. And what they found over time, and you can see that this is looking at about two months of data, the full case study is
available with the QR code, that over time they were able to increase the accuracy of their
chat bot from 70% to 90%. So higher is better here. And they were able to increase
the user satisfaction, this thumbs down rate is
getting lower, over time. So they were able to produce
more accurate answers, which also improved
their user satisfaction. So that brings me to the last strategy. One of the things that obviously is very popular these days is looking at different ways
to build agentic applications. And so if you look at a simple sort of agent dialogue, you might ask a question. Maybe I ask a question about
something about my phone and I gave it the model number, and I come back a couple days later and I ask another question
that's related to my phone, and the agent asked me something that I think it should have known. So this sort of lack of context or loss of context means that agents aren't as personalized and they're not able to
respond as accurately to user interactions. And people often talk about
this sort of the goldfish effect where an agent without memory, every interaction is
like a brand new thing, experiencing it for the first time. So a way to solve this problem is to add memory to your agents. So this allows you to save and store the context of different interactions such that it can be reused
at a future point in time. And there's lots of different
potential applications for this beyond the sort of
user experience app model. You could, for example, think about if you had
multi-agent workflows and they were doing plans, what plans generated what outcomes, and storing those kinds
of things as memory. So there's lots of
different potential here. There are different types of memory. So as a quick example, if you were to ask an agent to plan a trip to Tokyo with certain length and price parameters and say, you know, "I'm interested in cultural sites and experiences," conceptually, you might
break out the memories into these different types. And so you might have a working memory, which is things that were just asked in this current session. You might have had some kind
of short-term memory concept where these are things
that other conversations or other working memories that this individual or user has had. And then you might have
something that was more of an organized, long-term
concept that you might know that they have travel
certain seating preferences, that they have global entry. And so if you're able to store and manage this context, you can use it within
your agentic workflows and agentic interactions for both accuracy and
latency improvements. There's lots of different
ways to add agent memory. Fortunately, most folks are building inside of different kinds of frameworks. Obviously, the Bedrock AgentCore is one that we're using quite a lot. And so you can have different techniques to enable those in those frameworks. So you can use MCP servers to help you construct knowledge graphs based on memories or organization that agents
have interacted with. Mem0 is an open source library that helps you do
personalized knowledge graphs as part of your memory. Cognee is really more
conversationally focused, and Zep/Graphiti is really
focused on temporal graphs, and there's lots of
other different options. This is another opportunity for you if you want to go a
little bit deeper here. This blog post was published last week, and it has code examples about
how to use the Strands SDK, which is an agent framework
that we have it here at AWS, to be able to add and store persistent memory of different types. And again, you can use that QR code. And so just to kind of give
you a quick walkthrough of this example, so this is a Strands agent example. This is really, if you go to the blog post, you'll see there's really,
like, three lines of code here to create this very simple agent. It's asking a question
about the Mem0 project, and it gets a result. You can enable graph memory, which is, again, adding a
couple of lines of code, of Python code, to the Strands agent. You can ask a question
where the top contributors to the Mem0 project receive the answer, and then when you ask another question, "Who works on the Mem0 project?" you'll get both a faster result and a result where you have
to retrieve fewer tokens. And so in addition to providing a benefit from an accuracy and user perspective, there's also a cost dimension. So again, how well does this work? These are some numbers that were presented by Zep and Graphiti, and you can see that using memories, they're able to get some
improvements in accuracy. And very significantly, they were able to see almost 10x improvements in latency and the average number
of context tokens used. So you're able to improve the latency in the user experience
and also reduce the cost. So, just to kind of do a quick wrap-up, when you think about graphs, think about graphs as a tool to get more of out of your data, and ways that you can use graphs to process your data where it is, and where you can use graphs in ways to improve the accuracy
of different applications. Combine vector search and graph traversal to get the power of
vector similarity search with the benefits and explicit information that you can get from a graph. And lastly, look at how you can store and organize agentic memories, particularly using graph structures with Strands and Bedrock AgentCore. Thank you very much for
spending your afternoon or at least an hour of
your afternoon with us. We greatly appreciate it. Umit and I'll be around afterwards if anyone has other
questions, wants to talk. And enjoy the rest of the conference. Thank you.
(audience applauds)
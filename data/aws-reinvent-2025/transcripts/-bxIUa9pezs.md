---
video_id: -bxIUa9pezs
video_url: https://www.youtube.com/watch?v=-bxIUa9pezs
is_generated: False
is_translatable: True
---

- Good evening. I hope you can hear me. I'm Shreeni, and I lead
the business for innovation and emerging technologies. We at Tech Mahindra, one of the largest SI
IT companies from India, partner with AWS in multiple areas, and we work with them in AI, in metaverse, and quantum computing. In today's session, we would like to cover
how Tech Mahindra and AWS have helped companies reduce their TCO by doing joint offerings
in the generative AI space. I'll just, yeah. So I'll give you some important stats. Lots of IT companies
have actually been doing a lot of POCs in the generative AI space, and everybody talks about the work they do in agents and all. But do we know how many of these POCs actually get converted to production? It's a measly 5%. Let me give you three more statistics. In any given company that we work, we spend a quarter of our
time typically to find out data that we require for our daily work, or we try to find out
who's the right person who can give the data. That happens in all the organizations. Similarly, each company
is now spending money to see how it can make their
associates more productive by giving them co-pilots and other things. So that is coming to up to 7%. But the most surprising thing that we have is that a lot of
investment in technologies are actually not getting used. One third of the investment that we do, typically in areas like
GPUs, technologies, softwares, are not getting used. So, where do we go from here? So TechM and AWS have said that, let us define some parameters on how do we actually make POCs which are production-grade. And these are some of the
principles that we follow. So what typically happens is, when we try to do a POC, we will look at it only
as a proof of concept. But can we look at POC
as a full-term project? As the deliverables that we want to give? As the data that we need to look at? As the latency that we need to look at? Is that making a difference? The second point is, the most important thing that
people talk in the AI space is how do we provide security? How do we do governance? And are we inculcating that
in the first stage itself when we are doing POCs? The third thing is, AI is something that
will improve over time, so when we are thinking of production, are we thinking of
staggering our production with learnings from each phase? The fourth thing, and a
big misnomer that we have, is that agentic AI will
not need human beings. It's a big misnomer. Agents are there to augment what we do, and we need to plan in such a way that agents do bulk of the work. And as we go ahead, can they ensure that the presence of human
beings required is very less? But plan it in such a way. And the last and most important thing for anything that we do is, are we evaluating what we are doing? Are we evaluating? Are we benchmarking the
POC that we are doing? Are we looking at what results
we want to get out of it? So these are key things
that we need to look at when we try to create a POC. So in TechM, we actually found a strategy
on how do we deliver AI. So any company that
comes to us asking for AI is looking at four key things. Either they're trying to do productivity, or they're trying to do transformation, or they're trying to do
innovation, or governance. So we came with a strategy saying, can we ensure that we
deliver AI delivered right in the first instance? And to do that, TechM has come up with a product called TechM Orion. Now, what is TechM Orion? So TechM, along with NVIDIA
as an infrastructure player, has come up with a platform which will give you access
to models for fine-tuning, which will help you to
create RAG repositories, and also help you to launch agents to automate your tasks. So what will that give us? Speed, interoperability, and
security, and governance. Now, this is the entire
architecture of Orion. I will not go into detail, but I would request all of
you to come to our booth, which is 1284, which is
where we are talking about what is Orion, what are the key use cases that we have developed on Orion, how do we launch agents
at breakneck speed, what are the repositories that we create, how is AWS a part of the entire Orion. So when you come to our
booth, we'll talk about them, but this is the general
architecture of Orion. So what are we doing with AWS typically? We are partnered with them in Orion. Orion is actually hosted on AWS. Second is, in their agent core, we are developing agents
for some of our customers, typically in BFSI and manufacturing side. And Tech Mahindra has a large repository of certified people who have
different belts from AWS, and we are actually doing
joint research with them in some of the core areas. So, between Tech Mahindra and AWS, there are multiple case studies that we have done with customers, but I'll highlight two use
cases or two case studies. The first one is a US-based company. This is into developing
engineering services. Has been in presence since 1950. For the last 50, 60
years, it's been there. And it had one typical problem
that they approached us, is they have 75 human agents who work on the customer support. And these customer support
agents who were there were getting bogged with multiple calls that they were getting, which resulted in long queues for people trying to access
their customer center, which affected the productivity. So, what did TechM do? So TechM and AWS gave out a joint solution where we said that we'll
create you a chatbot, a generative AI-based chatbot, which will help you
solve all these queries. How did we do that? So the first thing we did was that we powered this by Amazon Lex. Now, what is Amazon Lex? Amazon Lex is a tool that uses natural language understanding. So whenever a customer puts in a query, it tries to understand what is
the intent behind that query, and then it passes this
information to AWS Lambda, which actually orchestrates the entire information which is there. It could be a repository or the inventory of the
things that represent, it'll be pricing. It fetches it and gives
it to Claude Sonnet. Now, what happens typically in AWS is, AWS Bedrock has multiple models which are from AWS and Anthropic. So Claude Sonnet is one of
the models from Anthropic, and this is used for typically
solving complex use cases. So this use case will take
the information from Lambda and pass it on to Lex in the
way that human beings can read, and that information goes to the end user. By doing this, we actually automated 50% of the calls they were getting, and we could bring in
productivity to the customer. Now, what has happened is
using the same 75 agents, they've been able to spend more time in terms of actually selling more and generating $50,000 of revenue. So this is the first use case that we did for an engineering company. Now, the second use case that we did was for a company in Philippines. This was a BFSI company, primarily into mobile, and doing remittances. Now, this company has been doing well for the past few years, and by 2024, they had 94 million consumers and a market capitalization of $5 billion. Now, if you look at
Philippines as a country, there's a lot of focus on remittances. And you see that remittances as an area is growing at 13.3% every year, till 2030. But this customer hit a roadblock. What typically happens
is, in the finance world, there's something called
as account takeover, where people will impersonate your details and take over your account, and then start doing
malicious things around that. Now, the moment I get to know that something wrong has
happened with my account, I immediately write to
the customer support. Now, the same thing used to
happen with this customer, but the customer support
team used to typically take seven days to solve it. Now, if you are in finance business and you are taking seven days, you're actually talking
of credibility loss. You're talking of credibility
loss for the company. So the company approached us, and we actually created a platform for them called FraudSentinel. Now, what did we do that? There are two things
that we basically did. One is we automated the
entire fraud detection process using Step, which is an AWS product. So, typically, what used to
happen as a manual thing, now happens to a process flow, and fraud detection happens much simpler. The second thing is we also created a generative AI-based chatbot, which could be used by the fraud analysts to actually talk to the
chatbot or to the experts using normal business language. Now, doing this, what we could do is bring down the resolution of the ATO cases that were happening from about seven days
to less than 24 hours. Now, not only did we bring
the time to resolve slow, but we also brought the SLA to one day. Now, for a company that has
been losing credibility, doing this has actually
helped it increase its CSI or what we call as customer
satisfaction index by 10%. And now they're back into the business, they're still leading
that area in Philippines, and they're expanding. So, these are two use cases
that I wanted to talk about, but primarily the objective is that, when we focus on business, what is that we are looking at? So more what generally happens is when we technologists
go and meet customers, we are happy to discuss technology, or to tell them what the
latest technology will help. But the focus here should be, what is the business
outcome they are looking and how can we solve it? Can a normal automation
solution help the customer do the job rather than
giving them an idea of using a large language model
and a RAG repository? So are we focusing on
what business outcomes is the customer looking from us, or is he looking at us on technology? So that's the first thing. The second thing that we are doing is, are we focusing on cost? And when I say cost is right from the time we
are looking at the solution, are we looking at cost economics? Do we need these things? A lot of times, what happens is, we tend to use, say,
ChatGPT or any other models where the tokens are costly. Is that taken into consideration? I'm not saying they're good or bad, but I'm saying are we taking
that into consideration when we are doing the economics? The third one is, are we
planning the POCs properly into a production-grade
that I was talking about? So these are some of the
things that we are doing. And the last and most important
thing that we need to do is, measure all the work that we are doing. Measure the POCs that we are trying to do, measure the projects
that we are trying to do. How can we build... And what is the output that
we want to get out of that? Is the most important thing
that we are trying to focus on. So, if you look at typically the way we have been orchestrating things is that in the discussion
with the customer, we've been trying to understand
what has been the problem, and how does the problem
actually impact the customer. So like the first case, where we said this company was typically losing business because the customer service executives, who were supposed to sell or cross-sell, were busy handling the queries, and they were taking
more time to handle that. In the second case, we
found out that customer, while gaining business, was
actually losing credibility, which in the long-term could affect in a growing market for remittances. So the focus was on how do
we look at business outcomes, and then we come back to
the drawing board and say, am I going to use AI? Am I going to use generative AI? Am I going to use a RAG repository for it? What is the solution
that we want to derive? So, I think, overall, the focus has been on how do we derive business
outcomes in terms of it. So, the last point I wanted to talk was, like we said that we
thought agents are a panacea for all the problems that we have, the large language models
are also not the panacea. So if Tech Mahindra has created a model, which is 1.2 billion called Indus, and we benchmarked with GPT and others, and independent bodies found out that our ratio of tokenization was much better than them, it means that it also tells us the fact that we are not looking
at large language models just based on parameters, but based on how they have been fine-tuned and how they have been built. So, coming back to the same premises, we look at cost, we look
at business outcomes, and we try to do our POCs
as a production-grade. I think this is what we learned when we did the journey
with both the customers. The next point I wanted to say was that we would like to extend this discussion when you come to our booth at 1284 to see what are the problems
that you have in your areas. In the AI space, what are the problems that
your customers are facing, and how we can work it together? How we can involve AWS whenever required? The third point was we as a
company also look beyond AI, and I have my metaverse expert here, where we are trying to see how we can use immersive experiences combined with AI to simulate a lot of business processes. It could be digital twins
for a mining company. It could be digital twin on
how fiber has to be laid out for a telecom company. Or digital twin on how a
financial process gets solved. These are things that we are trying to do, but this is a culmination of both AI and immersive experience,
or metaverse as we call it. And the last area that we are focusing on, again, working with AWS is, how do we bring quantum
computing into practice? How do we look at quantum computing to solve cases like fraud detection? How do we bring route
optimization using quantum? And this is something that
we are working on Braket, which is an AWS product. But I think that is where
I'd like to end my session. If there are any questions,
I'd like to take it. (audience clapping)
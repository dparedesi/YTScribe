---
video_id: tgnyLTV5h1s
video_url: https://www.youtube.com/watch?v=tgnyLTV5h1s
is_generated: False
is_translatable: True
---

- Today, we're going to
understand from Suhrud what RiskSpan does, what is
the Private Credit market, what are some of the decisions that they made in their
generative AI journey on AWS. And finally, what are some considerations to take into account when you want to take this application into production in a customer-facing capacity. Suhrud, thank you for making the time. Incredibly privileged to
have you here on stage with me presenting the story. I wanna start us off by telling our audience a
little bit about RiskSpan, and maybe even defining what
Private Credit is for us. Thank you, Subhash, and thank you, AWS, for this amazing opportunity. So, RiskSpan is a technology company that provides analysis for some of the most complex
investment asset classes. We are needed to AWS, we built our entire platform on AWS. We are, you know, as a
result, we are a 100% Cloud, and we run very large workloads
on very complex assets. We run trillions of dollars
of assets on a daily basis. We run very granular loan-level analysis, like 45 million loans across, you know, 70-plus asset classes. And again, to reiterate,
we've been on it with AWS for 15 years now, and that's the kind of, we wouldn't exist without AWS. Private credit. So, private credit, when
most of us go get a loan, which is a credit by
definition, we go to a bank. But when a non-bank entity
provides a loan to individuals or to companies, because those loans are non-standard, that's where private credit comes in. It's a huge market. You know, there's 14
trillion of assets out there. There are 9 trillion of
untapped assets out there. Why is that the case? Because, definitionally,
every investment is custom. Every investment looks different which, and all the information about
the investment is buried in documents, emails, a lot of
unstructured data to be able to model, and analyze, and
price this investments. Today, analysts build Excel
spreadsheets, which, again, as we all know, doesn't scale. And what it does is that it
creates this opaque market with very little (poor audio quality) on a regular time basis, and portfolio managers are now
managing trillions of dollars of these assets and
react to changing market and investment opportunities quickly. - Looks like a pretty massive opportunity. It's 14T with a trillion, and with a lot of data. So, what are the challenges? Can you walk us through this because you talked about
investors of all kinds, large net worth or institutional, or anyone that's accessing private credit? What's the complexity in
providing what they need? - Yeah, it's kind of, you
know, it's hard to imagine that there's so much assets that is being, you know, invested in, and at risk where the
information is buried in these documents. And in more majority of the cases, there isn't one single 200-page document as this slide says. There are 17 to 20 amendments that occur, which makes it very difficult to extract all the information
in a structured format that somebody can act on. And as a result, to even get to a point where you are comfortable and you know what is the investment that you're getting into. It, today, takes about three to four weeks to have read through documents, extract the data, put in an Excel, and create an Excel model
that you are comfortable with. But (poor audio quality) see here, right, the growth today is like
1.7 trillion-plus is what's happening on a
kind of over the last two or three years. Hence, investors want
to (poor audio quality) in this investment, need
to react very quickly. Sometimes they have less
than 10 minutes, at most, half an hour to go and decide if they want
to pursue this investment. Otherwise, they'll commit to
spending three, four weeks and still not be competitive. And what's happened is that
there has been a lot of risk. There are two very major incidents that occurred in the private credit space, where there were billions
of dollars of losses because investors didn't
have access to the data and couldn't monitor the
investment on a regular basis. - Looks like a complex problem to solve when you have a lot of
data, mostly unstructured, typically takes a long time to process, it's a fairly manual process. However, your investors are looking to make decisions fast,
and that's the challenge. So, how do we take this complex problem and solve it in a way that investors can actually
make the right decisions based on all that information in those deals? So, tell us a little bit
about where did you start, because it seems like a
fairly complex problem. Talk a little bit about
your journey with AWS. - So, you know, we are all
technologists at heart. We want to solve cool problems, build cool technology. But working with Subhash's team
over the last several years, we've learned a lot of cool techniques to help us build something
that was relevant and relevant to the market, and something that addressed the problem. Using the AWS PR/FAQ Process where we wrote a press release with our cross-functional
team, sales, marketing, executive leadership, technology, and even some third-party
external clients to tell clients what are they going to
get, what are we building? And then, combine that with a frequently-asked-questions list an FAQ, which answered hard questions, also that we could focus on that $9-trillion uncapped opportunity, instead of reinventing the wheel and building yet another system that didn't solve the problem. And most importantly, we
didn't write a single line of code 'til we had our vision defined, and had a customer-centric solution. And Subhash can talk
more about the PR/FAQ. - Yeah, that's pretty impressive. How many of you here are familiar with the AWS PR/FAQ mechanism? I see a few hands, mostly Amazonians. So PR/FAQ stands for a Press Release and Frequently Asked Questions. It's a mechanism we have, where, before we start to invest any
development time or dollars or resources, we actually
write a press release about how the product is going to show up when it's released. Think of it like a one-pager,
an actual press release, where we're talking about the customer. Who is the customer? What is the pain point? And how does the solution
address that pain point? The FAQ is the detailed section where you're putting
yourselves in the shoes of multiple stakeholders,
sometimes technical, sometimes business, financial, sometimes the customer themselves, and answering questions
from their perspective on how the solution would
impact them and their teams. It's a comprehensive
process for, as a customer, this is something that we offer for free. So you can work with your
Amazon, you know, account teams to kind of go through this process. The beauty about this is
it's an incredible tool to drive clarity, and a consistent vision
across multiple functions, multiple teams within your companies. And it's something that helps us center our
strategy around the end customer. Because the PR/FAQ focuses
a lot on identifying who is the customer, the pain point, and how you're effectively
addressing that pain point. Thanks for that, Suhrud. So, the PR/FAQ process,
once you go through it, establishes the vision, and now the next part is
to move to an architecture. So, Suhrud, talk to us a
little bit about what were the considerations while
establishing an architecture, and how does the architecture look today? - So, in some ways, this is
a very standard architecture. You have data ingestion, you have a model, and then we are making the
results accessible to end users. Kind of a standard analytic
calculation calculators, that what was complex here was that the data was highly
coming in a variety of format and also that the problem was custom. So every deal was gonna be custom. So we needed intelligence
to not only come up with a final solution for
project forecasting, cash flows and value for these investments
that we also needed, (poor audio quality) Handled unstructured
data in a large scale. So, you know, we use
storage (poor audio quality) Oh, okay, sorry. Yeah, we use secure storage because confidentiality
was key to our clients. We use tools to extract data
from scanned PDF images, unstructured emails, you know,
handwritten notes, et cetera. We ran, and then that was a lot of data. So there was no way that LLM Claude, which is LLM in this case, was gonna be able to process that. So we needed embeddings,
we needed a rack solution, which again, we were able to leverage all of that through Bedrock. And then, having the information
flow through in a form that our legacy APIs
could take those forecasts and give clients a seamless experience across all their investments
was the last layer of the API layer, which already existed. And the impact of that
has been quite incredible. We use serverless technology
for running the final code that was being generated by Claude. So, Claude, in this case, is generating the dynamically generating code to model the investment,
waterfall investment logic, and we were able to hand-scale endlessly the cost through automation was amazing. The AWS services we used
were very cost-effective, and the cost, you know,
was like less than $50, including the human in
the loop being involved. - So, pretty impressive
impact talking about, you know, 10x scalability, but also more importantly,
the 90x reduction in cost. For those of you that have worked with Generative AI
applications, typically, the perception is that it's
going to drive up cost. But in this use case, we're
seeing a tremendous amount of efficiency automation
that's being, you know, put into the architecture, which
is what is helping us drive that cost advantage. Now, Suhrud, one of Gartner's
recent observations is that about 90-plus percentage of Generative AI projects die a slow death in the pilot phase, and not really make it to production. You are one of those customers that have had tremendous
success taking this architecture to production and monetizing it. Talk to us a little bit,
you know, about that journey to product, putting this
application in production. What are some things that you
had to really, really focus on to get it right at scale,
in a customer-facing, you know, application? - Yeah, and I'll start by saying that, of course, we made a lot of mistakes. We had, you know, we walked
into it thinking that, you know, we had the magic bullet with
LLM, we'll feed all the data, and out we'll get the code, because that's what you
get when you sit in front of either ChatGPT or
the Cloud Web UI, right, which is clearly not the case. And you know, one of the learnings was that the LLMs are trained
on vast amount of data, but they're not specifically
trained on our domain, or, you know, anybody's
domain at the granular level that we understand the domain to be and the expertise we have. So, like taking, training the LLM, and by providing the
appropriate context for, and the domain knowledge for
the various prob various deals and structures that we are
modeling was one key learning that we had, this was done
also to avoid, you know, hallucination create deterministic output to the extent possible. Similar to that was
breaking down the problems by creating those semantic
chunks from the document and all the way to
solving individual aspects of a transaction. Like, okay, this is the
context to calculate fees. This is the context to
calculate interest income. This is the context of how
you deal with delinquencies, defaults, et cetera. Like breaking that down into chunks was a key learning we had early on. And then, finally, something
that we as software developers, we've known this but was initially lost, but we kind of got back
to it pretty quickly, was providing structure. LLMs do much better if you're giving data in a preset-structured format. So, extracting, especially for
the code generation aspect. So we created this
well-defined structure JSON, which the LLMs would consume, and then also the output was provided in a very structured format, that the last bit probably
helped us the most in terms of, you know, accuracy, reliability, and robustness of the solution. - Wow, thank you for sharing that. I think, just to summarize it, one, everyone has access to the model. It's not the model that's
going to differentiate you, it's your data, the context, the business context you
provide that is going to be differentiating. Second, I think to expect the
LLM to solve a large problem by itself, even with the best of prompts, I think is unrealistic. You wanna break it down
into smaller problems, think microservices,
think specific solutions, and start to improve on
accuracy and latency, and cost, and other considerations. Last but not the least, the more structured both your
data is or your inferences, the better the LLMs perform. And so, of course, putting in
the work to do that, you know, data wrangling up front and getting it to an LLM in a
structured format does help. So, now you have this
application in production, you're monetizing it, however, you do understand that the technology is changing incredibly fast underneath you. So, what does the future look for, and what is the vision for
RiskSpan going forward? - Yeah, I'll start by saying that by no means have we solved
the problem completely. There is a lot of work to be done because this space, the Private Credit space,
is constantly evolving. The need for custom structures
come about all the time. The need for real-time risk is pretty key. And we had kind of, we laid out a vision of what we wanted to do to be able to make the ability to create a
model to be more robust, more deterministic, and
also help our clients solve more forecasting-related issues. We wanted to help have our
clients create structures more dynamically based
on market conditions. Instead of taking a legal document and then modeling the deal,
we wanted them to come and say, "Well, in this market, what type of structure would we need?" So kind of, so the few
things that are listed here that we were focused on, and you know, I can kind
of get to the punchline, and the punchline is AgentCore. AgentCore kind of solves
almost every one of the things that we had planned to build. So now we are gonna try and figure out what, where to
kind of spend our time next, but it's just like having
these, you know, multiple agents that solve very specific problem. We were doing that by having,
using prompts and such, but here, creating agents and then having the agent orchestration is
helping us tremendously. We are seeing benefits of that already. And then, pairing up, like
getting our SMEs to help, you know, again, provide
prompts for those agents, giving them the ability
to even kind of, you know, create those agents more dynamically has helped tremendously. We walled our rag approach a
lot more as well, to be able to again, manage these,
you know, these documents in a more semantic way,
in a more reliable way, and finally, continuous
learning, which is, again, like the dynamic prompt and the agent orchestration
is helped a lot through the continuous learning aspect. And a couple of screenshots
we attach here to show that this is actually
real, which is kind of, we couldn't have a PowerPoint
without any screenshots. So, thanks, Subhash,
letting us slide a few in. - Yeah, yeah, no, absolutely
love that you're starting to transition the
architecture to much more of an agent-based where, you know, we talked about breaking
the bigger problem into smaller chunks, where
you have the set of agents that are individually focused
on a task, driving, you know, much better accuracy, but then having a platform like AgentCore that can orchestrate all
these agents to work together, continue to maintain that security and compliance piece as they work. So, again, I think, you know, getting to an end state
where your investors are able to upload a portfolio and
quickly evaluate it in real time and make an investment decision, I think it's the grand vision, and certainly, I think you're on the right track. You've driven tremendous
impact in your business. It's fair to say that some of the outcomes that you've achieved are
fairly transformational, right? Talking about, you know,
87% faster are, you know, onboarding for customers. I mean, taking the processing time for a deal structure evaluation
from three to four weeks to about three to five days,
that's pretty impressive, and that's pretty significant. While you're also
increasing your capacity, you're also lowering your costs. So, love the fact that you're on path to unlocking this $9-trillion market. And I wanna say thank you for giving your valuable time, sharing your perspective on
your Generative AI journey, and thank you again for partnering with us and giving us a part, you
know, to play in your journey. So, Suhrud, thank you again for the time. Thank you, everyone.
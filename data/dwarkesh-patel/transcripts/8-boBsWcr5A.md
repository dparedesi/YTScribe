---
video_id: 8-boBsWcr5A
video_url: https://www.youtube.com/watch?v=8-boBsWcr5A
title: Satya Nadella – How Microsoft thinks about AGI
author: Dwarkesh Patel
published_date: 2025-11-12
length_minutes: 88.68
views: 264118
description: "As part of this interview, Satya Nadella gave me and Dylan Patel (founder of SemiAnalysis) an exclusive first-look at their brand-new Fairwater 2 datacenter.  Microsoft is building multiple Fairwaters, each of which has hundreds of thousands of GB200s & GB300s. Between all these interconnected buildings, they’ll have over 2 GW of total capacity. Just to give a frame of reference, even a single one of these Fairwater buildings is more powerful than any other AI datacenter that currently exists.  ..."
is_generated: False
is_translatable: True
---

Today we are interviewing Satya Nadella.   "We" being me and Dylan Patel, who is 
founder of SemiAnalysis. Satya, welcome.  Thank you. It's great. Thanks 
for coming over to Atlanta.  Thank you for giving us the 
tour of the new facility.  It's been really cool to see.
Absolutely.  Satya and Scott Guthrie, Microsoft's 
EVP of Cloud and AI, give us a tour of   their brand new Fairwater 2 data center, 
the current most powerful in the world.  We've tried to 10x the training 
capacity every 18 to 24 months.  So this would effectively be a 10x 
increase from what GPT-5 was trained with.  So to put it in perspective in the number of 
optics, the network optics in this building   is almost as much as all of Azure across all 
our data centers two and a half years ago.  It's got like five million network connections.
You've got all this bandwidth between different   sites in a region and between the two regions.
So is this like a big bet on scaling in the   future, that you anticipate in the future that 
there's going to be some huge model that will   require two whole different regions to train?
The goal is to be able to aggregate these   flops for a large training job and then 
put these things together across sites.  The reality is you'll use it for training and 
then you'll use it for data gen, you'll use it   for inference in all sorts of ways.
It's not like it's going to be used   only for one workload forever.
Fairwater 4, which you're going   to see under construction nearby, will also be on 
that one petabit network so that we can actually   link the two at a very high rate.
Then we do the AI WAN connecting to   Milwaukee where we have multiple 
other Fairwaters being built.  Literally you can see the model 
parallelism and the data parallelism.  It's kind of built for, essentially, the 
training jobs, the super pods across this campus.  And then with the WAN, you can 
go to the Wisconsin data center.  You literally run a training job 
with all of them getting aggregated.  What we're seeing right here is a cell 
with no servers in it yet, no racks.  How many racks are in a cell?
We don't necessarily share that per se, but…  That’s the reason I ask.
You'll see upstairs.  I'll start counting.
You can start counting.   We'll let you start counting.
How many cells are there in this building?  That part also I can't tell you.
Well, division is easy, right?  My God, it's kind of loud.
Are you looking at this like,   "Now I see where my money is going."
It's like, "I run a software company.   Welcome to the software company."
How big is the design space once   you've decided to use the GB200s and the NVLink?
How many other decisions are there to be made?  There is coupling from the model architecture 
to what is the physical plan that's optimized.  And it's also scary in that sense, which is, 
there's going to be a new chip that'll come   out. Take Vera Rubin Ultra. That's going to have 
power density that's going to be so different,   with cooling requirements that 
are going to be so different.  So you kind of don't want to 
just build all to one spec.  That goes back a little bit 
to the dialogue we'll have,   which is that you want to be scaling in time as 
opposed to scale once and then be stuck with it.  When you look at all the past technological 
transitions—whether it be railroads or the   Internet or replaceable parts, industrialization, 
the cloud, all of these things—each revolution   has gotten much faster in the time it 
goes from technology discovered to ramp   and pervasiveness through the economy.
Many folks who have been on Dwarkesh's   podcast believe this is the final 
technological revolution or transition,   and that this time is very, very different.
At least so far in the markets, in three years   we've already skyrocketed to hyperscalers 
doing $500 billion of capex next year,   which is a scale that's unmatched to 
prior revolutions in terms of speed.  The end state seems to be quite different.
Your framing of this seems quite   different from what I would call the 
"AI bro" who's like, "AGI is coming."  I'd like to understand that more.
I start with the excitement that I   also feel for the idea that maybe after 
the Industrial Revolution this is the   biggest thing. I start with that premise. But 
at the same time, I'm a little grounded in the   fact that this is still early innings.
We've built some very useful things,   we're seeing some great properties, 
these scaling laws seem to be working.  I'm optimistic that they'll continue to work.
Some of it does require real science   breakthroughs, but it's also a lot 
of engineering and what have you.  That said, I also sort of take the view 
that even what has been happening in the   last 70 years of computing has also 
been a march that has helped us move.  I like one of the things that Raj 
Reddy has as a metaphor for what AI is.  He's a Turing Award winner at CMU. He had 
this, even pre-AGI. He had this metaphor   for AI, it should either be a guardian angel 
or a cognitive amplifier. I love that. It's a   simple way to think about what this is.
Ultimately, what is its human utility?  It is going to be a cognitive 
amplifier and a guardian angel.  If I view it that way, I view it as a tool.
But then you can also go very mystical about   it and say this is more than a tool.
It does all these things, which only   humans did before so far.
But that has been the case   with many technologies in the past.
Only humans did a lot of things,   and then we had tools that did them.
We don't have to get wrapped up in the definition   here, but one way to think about it is, maybe 
it takes five years, ten years, twenty years.  At some point, eventually a machine is producing 
Satya tokens, and the Microsoft board thinks that   Satya tokens are worth a lot.
How much are you wasting of   this economic value by interviewing Satya?
I could not afford the API costs of Satya tokens.  Whatever you want to call it, are the 
Satya tokens a tool or an agent, whatever.  Right now, if you have models that cost on the 
order of dollars or cents per million tokens,   there's just an enormous room 
for margin expansion there,   where a million tokens of Satya are worth a lot.
Where does that margin go and what level of that   margin is Microsoft involved 
in is the question I have.  In some sense this goes back again to, 
essentially, what's the economic growth   picture going to really look like?
What's the firm going to look like?  What's productivity going to look like?
That to me is where, again, if the Industrial   Revolution created… After 70 years of diffusion 
is when you started seeing the economic growth.  That's the other thing to remember.
Even if the tech is diffusing fast this   time around, for true economic growth to appear 
it has to diffuse to a point where the work,   the work artifact, and the workflow has to change.
So that's one place where I think the change   management required for a corporation to truly 
change is something we shouldn't discount.  Going forward, do humans and the tokens they 
produce get higher leverage, whether it's the   Dwarkesh or the Dylan tokens of the future?
Think about the amount of technology.  Would you be able to run SemiAnalysis 
or this podcast without technology?  No chance, at the scale that you have 
been able to achieve, there’s no chance.  So the question is, what's that scale?
Is it going to be 10x'ed with something   that comes through? Absolutely. Therefore, 
whether you're ramped to some revenue number   or you're ramped to some audience number or what 
have you, that I think is what's going to happen.  The point is, what took 70 years, maybe 
150 years for the Industrial Revolution,   may happen in 20 years, 25 years.
I would love to compress what happened   in 200 years of the Industrial Revolution 
into a 20-year period, if we're lucky.  Microsoft historically has been 
perhaps the greatest software company,   the largest software-as-a-service company.
You've gone through a transition in the past   where you used to sell Windows licenses 
and disks of Windows or Microsoft,   and now you sell subscriptions to 365.
As we go from that transition to where   your business is today, there's also 
a transition going on after that.  Software-as-a-service has incredibly 
low incremental cost per user.  There's a lot of R&D, there's a 
lot of customer acquisition costs.  This is sort of why, not Microsoft, but 
the SaaS companies have underperformed   massively in the markets, because the COGS of 
AI is just so high, and that just completely   breaks how these business models work.
How do you, as perhaps the greatest   software-as-a-service company, transition 
Microsoft to this new age where COGS matters a lot   and the incremental cost per user is different?
Because right now you're charging like, "Hey,   it's 20 bucks for Copilot."
It's a great question because in some   sense with the business models themselves, 
the levers are going to remain similar.  If you look at the menu of models starting from 
consumer all the way, there will be some ad unit,   there will be some transaction, 
there will be some device gross   margin for somebody who builds an AI device.
There will be subscriptions, consumer and   enterprise, and then there'll be consumption.
So I still think those are all the meters.  To your point, what is a subscription?
Up to now, people like subscriptions   because they can budget for them.
They are essentially entitlements to   some consumption rights that come 
encapsulated in a subscription.  So I think that in some sense 
becomes a pricing decision.  How much consumption you are entitled to is, 
if you look at all the coding subscriptions,   kind of what they are, right?
Then you have the pro tier,   the standard tier, and what have you.
So I think that's how the pricing   and the margin structures will get tiered.
The interesting thing is that at Microsoft,   the good news for us is we are in 
that business across all those meters.  At a portfolio level, we pretty much 
have consumption, subscriptions,   to all of the other consumer levers as well.
I think time will tell which of these   models make sense in what categories.
One thing on the SaaS side, since you   brought it up, which I think a lot about.
Take Office 365 or Microsoft 365.  Having a low ARPU is great, because 
here's an interesting thing.  During the transition from server to cloud, one 
of the questions we used to ask ourselves is,   "Oh my God, if all we did was just basically 
move the same users who were using our Office   licenses and our Office servers at the 
time to the cloud, and we had COGS,   this is going to not only shrink our margins but 
we'll be fundamentally a less profitable company."  Except what happened was the move to the 
cloud expanded the market like crazy.  We sold a few servers in 
India, we didn't sell much.  Whereas in the cloud suddenly 
everybody in India also could   afford fractionally buying servers, the IT cost.
In fact, the biggest thing I had not realized,   for example, was the amount of money people were 
spending buying storage underneath SharePoint.  In fact, EMC's biggest segment may have 
been storage servers for SharePoint.  All that sort of dropped in the 
cloud because nobody had to go buy.  In fact, it was working capital, 
meaning basically, it was cash flow out.  So it expanded the market massively.
So this AI thing will be that.  If you take coding, what we built with 
GitHub and VS Code over decades, suddenly   the coding assistant is that big in one year.
That I think is what's going to happen as well,   which is the market expands massively.
There’s a question of, the market will   expand, but will the parts of the revenue that 
touch Microsoft expand? Copilot is an example.   If you look earlier this year, according 
to Dylan's numbers, GitHub Copilot revenue   was like $500 million or something like 
that and there were no close competitors.  Whereas now you have Claude 
Code, Cursor, and Copilot   with around similar revenue, around a billion.
Codex is catching up around $700–800 million.  So the question is, across all the surfaces that 
Microsoft has access to, what is the advantage   that Microsoft's equivalents of Copilot have?
By the way, I love this chart.  I love this chart for so many reasons.
One is we're still on the top.  Second is all these companies that are listed 
here are all companies that have been born in   the last four or five years.
That to me is the best sign.  You have new competitors, 
new existential problems.  When you say, who's it now?
Claude's going to kill you,   Cursor is going to kill you, it's not Borland. 
Thank God. That means we are in the right   direction. This is it. The fact that we went from 
nothing to this scale is the market expansion.  This is like the cloud-like stuff.
Fundamentally, this category of   coding and AI is probably going to 
be one of the biggest categories.  It is the software factory category.
In fact, it may be bigger than knowledge work.  I want to keep myself open-minded about it.
We're going to have tough competition.  That's your point, which is a great one.
But I'm glad we have parlayed   what we had into this and now we have to compete.
On the competing side, even in the last quarter we   just finished, we did our quarterly announcement 
and I think we grew from 20 to 26 million subs.  I feel good about our sub growth and 
where the direction of travel on that is.  But the more interesting thing that has happened 
is, guess where all the repos of all these other   guys who are generating lots and lots of code go? 
They go to GitHub. GitHub is at an all-time high   in terms of repo creation, PRs, everything.
In some sense we want to keep that open,   by the way.
That means we want to have that.  We don't want to conflate 
that with our own growth.  Interestingly enough, we are getting 
one developer joining GitHub a second   or something, that is the stat, I think.
And 80% of them just fall into some GitHub   Copilot workflow, just because there are.
By the way, many of these things will even   use some of our coding code review agents, which 
are by default on, just because you can use it.  We'll have many, many structural shots at this.
The thing that we're also going   to do is what we did with Git.
The primitives of GitHub, starting with Git,   to issues, to actions, these are powerful, lovely 
things because they kind of are all built around   your repo. We want to extend that. Last week 
at GitHub Universe, that's kind of what we did.  We said Agent HQ was the conceptual thing 
that we said we're going to build out.  This is where, for example, you 
have a thing called Mission Control.  You go to Mission Control, and now I can fire off.
Sometimes I describe it as the cable TV of all   these AI agents because I'll have, essentially 
packaged into one subscription, Codex, Claude,   Cognition stuff, anyone's agents, 
Grok, all of them will be there.  So I get one package and then I can literally 
go issue a task and steer them so they'll all   be working in their independent branches. I can 
monitor them. I think that's going to be one of   the biggest places of innovation, because right 
now I want to be able to use multiple agents.  I want to be able to then digest 
the output of the multiple agents.  I want to be able to then 
keep a handle on my repo.  If there's some kind of a heads-up display 
that needs to be built and then for me to   quickly steer and triage what the coding agents 
have generated, that to me, between VS Code,   GitHub, and all of these new primitives we'll 
build as Mission Control with a control plane.  Observability… Just think about everyone 
who is going to deploy all this.  It will require a whole host of observability 
of what agent did what at what time to what   code base. I feel that's the opportunity. At 
the end of the day your point is well taken,   which is we better be competitive and innovate.
If we don't, we will get toppled.  But I like the chart, at least as long as 
we're on the top, even with competition.  The key point here is sort of 
that GitHub will keep growing   regardless of whose coding agent wins.
But that market only grows at say 10,   15, 20%, which is way above GDP. It's a great 
compounder. But these AI coding agents have   grown from say $500 million run rate at the end 
of last year—which was just GitHub Copilot—to   now where the current run rate across GitHub 
Copilot, Claude Code, Cursor, Cognition, Windsurf,   Replit, OpenAI Codex… That’s run rating at 
$5–6 billion now for the Q4 of this year.   That's 10x. When you look at the TAM of software 
agents, is it the $2 trillion of wages you pay   people, or is it something beyond that?
Because every company in the world will   now be able to develop software more?
No question Microsoft takes a slice of that.  But you've gone from near 100%, 
or certainly way above 50%,   to sub-25% market share in just one year.
What is the confidence that people can get   that Microsoft will keep winning?
It goes back a little bit, Dylan,   to that there's no birthright here, 
that we should have any confidence   other than to say we should go innovate.
Knowing the lucky break we have, in some sense,   is that this category is going to be a lot 
bigger than anything we had high share in.  Let me say it that way.
You could say we had high   share in VS Code, we had high share in the 
repos with GitHub, and that was a good market.  But the point is that even having a decent 
share in what is a much more expansive market…  You could say we had a high share 
in client-server server computing.  We have much lower share than that in hyperscale.
But is it a much bigger business? By orders of   magnitude. So at least it's existence proof that 
Microsoft has been okay even if our share position   has not been as strong as it was, as long as 
the markets we are competing in are creating   more value. And there are multiple winners. That's 
the stuff. But I take your point that ultimately   it all means you have to get competitive. I 
watch that every quarter. That’s why I'm very   optimistic about what we're going to do with 
Agent HQ, turning GitHub into a place where   all these agents come.
As I said, we'll have   multiple shots on goal on there.
It need not be… Some of these guys   can succeed along with us, so it doesn't need 
to be just one winner and one subscription.  I guess the reason to focus on this 
question is that it's not just about GitHub,   but fundamentally about Office and all 
the other software that Microsoft offers.  One vision you could have about how AI 
proceeds is that the models are going   to keep being hobbled and you'll need this 
direct visible observability all the time.  Another vision is that over time these models 
which are now doing tasks that take two minutes,   in the future, they'll be doing 
tasks that take 10, 30 minutes.  In the future, maybe they're doing 
days worth of work autonomously.  Then the model companies are charging thousands 
of dollars maybe for access to, really,   a coworker which could use any UI to communicate 
with their human and migrate between platforms.  If we’re getting closer to that, why 
aren't the model companies that are   just getting more and more profitable, 
the ones that are taking all the margin?  Why is the place where the scaffolding happens, 
which becomes less and less relevant as the AI   becomes more capable, going to be that important?
That goes to Office as it exists now versus   coworkers that are just doing knowledge work.
That's a great point. Does all the value   migrate just to the model?
Or does it get split between   the scaffolding and the model?
I think that time will tell.  But my fundamental point also is that 
the incentive structure gets clear.  Let’s take information work, or take even coding.
Already in fact, one of my favorite settings   in GitHub Copilot is called 
auto, which will just optimize.  In fact I buy a subscription and the auto 
one will start picking and optimizing   for what I am asking it to do.
It could even be fully autonomous.  It could arbitrage the tokens available 
across multiple models to go get a task done.  If you take that argument, the 
commodity there will be models.  Especially with open source models, you 
can pick a checkpoint and you can take a   bunch of your data and you're seeing it.
I think all of us will start, whether   it's from Cursor or from Microsoft, 
seeing some in-house models even.  And then you'll offload most of your tasks to it.
So one argument is if you win the   scaffolding—which today is dealing 
with all the hobbling problems or the   jaggedness of these intelligence problems, 
which you kind of have to—if you win that,   then you will vertically integrate yourself 
into the model just because you will have   the liquidity of the data and what have you.
There are enough and more checkpoints that   are going to be available. That's the other 
thing. Structurally, I think there will always   be an open source model that will be fairly 
capable in the world that you could then use,   as long as you have something that you can use 
that with, which is data and a scaffolding.  I can make the argument that if you're a 
model company, you may have a winner's curse.  You may have done all the hard work, 
done unbelievable innovation, except   it's one copy away from that being commoditized.
Then the person who has the data for grounding and   context engineering, and the liquidity of data 
can then go take that checkpoint and train it.  So I think the argument can be made both ways.
Unpacking what you said,   there's two views of the world.
One is that there are so many different   models out there. Open source exists. There 
will be differences between the models that   will drive some level of who wins and who doesn't.
But the scaffolding is what enables you to win.  The other view is that, 
actually, models are the key IP.  And everyone's in a tight race and there's 
some, "Hey, I can use Anthropic or OpenAI."  You can see this in the revenue charts.
OpenAI's revenue started skyrocketing once they   finally had a code model with similar capabilities 
to Anthropic, although in different ways.  There's the view that the model companies 
are the ones that garner all the margin.  Because if you look across this 
year, at least at Anthropic,   their gross margins on inference went from well 
below 40% to north of 60% by the end of the year.  The margins are expanding there despite 
more Chinese open source models than ever.  OpenAI is competitive, Google is 
competitive, X/Grok is now competitive.  All these companies are now competitive, and 
yet despite this, the margins have expanded at   the model layer significantly.
How do you think about that?  It's a great question. Perhaps a few years ago 
people were saying, "Oh, I could just wrap a   model and build a successful company."
That has probably gotten debunked just   because of the model capabilities, 
and the tools used, in particular.  But the interesting thing is, when I look at 
Office 365, let's take even this little thing we   built called Excel Agent. It's interesting. 
Excel Agent is not a UI-level wrapper.  It's actually a model that is in the middle tier.
In this case, because we have all the IP from   the GPT family, we are taking that and 
putting it into the core middle tier of   the Office system to teach it what it means to 
natively understand Excel, everything in it.  It's not just, "Hey, I just have 
a pixel-level understanding."  I have a full understanding of 
all the native artifacts of Excel.  Because if you think about it, if I'm 
going to give it some reasoning task,   I need to even fix the reasoning mistakes I make.
That means I need to not just see the pixels,   I need to be able to see, "Oh, I got that 
formula wrong," and I need to understand that.  To some degree, that's all being done not 
at the UI wrapper level with some prompt,   but it's being done in the middle tier 
by teaching it all the tools of Excel.  I'm giving it essentially a markdown to 
teach it the skills of what it means to   be a sophisticated Excel user.
It's a weird thing that it goes   back a little bit to the AI brain.
You're building not just Excel,   business logic in its traditional sense.
You're taking the Excel business logic   in the traditional sense and wrapping 
essentially a cognitive layer to it,   using this model which knows how to use the tool.
In some sense, Excel will come with an analyst   bundled in and with all the tools used.
That's the type of stuff that will get   built by everybody.
So even for the   model companies, they’ll have to compete.
If they price stuff high, guess what, if I'm a   builder of a tool like this, I'll substitute you.
I may use you for a while.  So as long as there's competition… 
There's always a winner-take-all thing.  If there's going to be one model that 
is better than everybody else with   massive distance, yes, that's a winner-take-all.
But as long as there's competition where there are   multiple models, just like hyperscale competition, 
and there's an open source check, there is enough   room here to go build value on top of models.
At Microsoft, the way I look at it is   that we are going to be in the hyperscale 
business, which will support multiple models.  We will have access to OpenAI models for seven 
more years, which we will innovate on top of.  Essentially, I think of ourselves as 
having a frontier-class model that we can   use and innovate on with full flexibility.
And we'll build our own models with MAI.  So we will always have a model level.
And then we'll build—whether it's in security,   whether it's in knowledge work, whether it's 
in coding, or in science—our own application   scaffolding, which will be model-forward.  It won't be a wrapper on a model, but the 
model will be wrapped into the application.  I have so many questions about 
the other things you mentioned.  But before we move onto those topics, 
I still wonder whether this is not   forward-looking on AI capabilities, where 
you're imagining models like they exist today.  It takes a screenshot of your screen, but it can't 
look inside each cell and what the formula is.  I think the better mental model here is 
just imagining that these models will be   able to use a computer as well as a human.
A human knowledge worker who is using Excel   can look into the formulas, can use alternative 
software, can migrate data between Office 365   and another piece of software if the 
migration is necessary, et cetera.  That's kind of what I'm saying.
But if that's the case, then the   integration with Excel doesn't matter that much.
No, no, don't worry about the Excel integration.  After all, Excel was built as a tool for 
analysts. Great. So whoever is this AI that   is an analyst should have tools that they can use.
They have the computer. Just the way a human can   use a computer. That's their tool.
The tool is the computer. So all   I’m saying is that I'm building an 
analyst as essentially an AI agent,   which happens to come with an a priori knowledge 
of how to use all of these analytical tools.  Just to make sure we're talking 
about the same thing, is it a thing   that a human like me using Excel…
No, it's completely autonomous. So   we should now maybe lay out what I 
think the future of the company is.  The future of the company would be the tools 
business in which I have a computer, I use Excel.  In fact, in the future I'll even have a 
Copilot, and that Copilot will also have agents.  But it's still me steering everything, and 
everything is coming back. That's one world.   The second world is the company just literally 
provisions a computing resource for an AI agent,   and that is working fully autonomously.
That fully autonomous agent will have   essentially an embodied set of those 
same tools that are available to it.  So this AI tool that comes in 
also has not just a raw computer,   because it's going to be more token-efficient 
to use tools to get stuff done.  In fact, I kind of look at 
it and say that our business,   which today is an end-user tools business, 
will become essentially an infrastructure   business in support of agents doing work.
It's another way to think about it.  In fact, all the stuff we built underneath 
M365 still is going to be very relevant.  You need some place to store it, some place 
to do archival, some place to do discovery,   some place to manage all of these activities, even 
if you're an AI agent. It's a new infrastructure.  To make sure I understand, you're 
saying theoretically a future AI that   has actual computer use—which all these model 
companies are working on right now—could use,   even if it's not partnered with Microsoft 
or under our umbrella, Microsoft software.  But you're saying, if you're working 
with our infrastructure, we're going   to give them lower-level access that makes it 
more efficient for you to do the same things   you could have otherwise done anyways?
100%. What happened is we had servers,   then there was virtualization, 
and then we had many more servers.  That's another way to think about this.
Don't think of the tool as the end thing.  What is the entire substrate 
underneath that tool that humans use?  That entire substrate is the 
bootstrap for the AI agent as well,   because the AI agent needs a computer.
In fact, one of the fascinating   things where we're seeing a significant amount 
of growth is all these guys who are doing these   Office artifacts and what have you, as autonomous 
agents and so on want to provision Windows 365.  They really want to be able to provision 
a computer for these agents. Absolutely.   That's why we're going to have essentially an 
end-user computing infrastructure business,   which is going to just keep growing because it's 
going to grow faster than the number of users.  That's one of the other questions people ask me, 
"Hey, what happens to the per-user business?"  At least the early signs maybe, the way 
to think about the per-user business   is not just per user, it's per agent.
And if you say it's per user and per agent,   the key is what's the stuff 
to provision for every agent?  A computer, a set of security things 
around it, an identity around it.  All those things, observability and 
so on, are the management layers.  That's all going to get baked into that.
The way to frame it—at least the way I currently   think about it and I’d like to hear your view—is 
that these model companies are all building   environments to train their models to use Excel or 
Amazon shopping or whatever it is, book flights.  But at the same time, they're also 
training these models to do migration.  Because that is probably the most immediately 
valuable thing: converting mainframe-based   systems to standard cloud systems, converting 
Excel databases into real databases with SQL,   or converting what is done in Word and Excel 
to something that is more programmatic and   more efficient in a classical sense 
that can be done by humans as well.  It's just not cost-effective for 
the software developer to do that.  That seems to be what everyone is going 
to do with AI, for the next few years at   least, to massively drive value.
How does Microsoft fit into that   if the models can utilize the tools 
themselves to migrate to something?  Yes, Microsoft has a leadership position 
in databases and in storage and in all   these other categories, but the use 
of an Office ecosystem is going to   be significantly less just like the use of a 
mainframe ecosystem could be potentially less.  Now mainframes have grown for the last two decades 
actually, even though no one talks about them   anymore. They've still grown.
100%, I agree with that.  How does that flow?
At the end of the day, there   is going to be a significant amount of time where 
there's going to be a hybrid world, because people   are going to be using the tools that are going 
to be working with agents that have to use tools,   and they have to communicate with each other.
What's the artifact I generate that   then a human needs to see?
All of these things will be real   considerations in any place, the outputs, inputs.
I don't think it'll just be about,   "Oh, I migrated off."
The bottom line is that I   have to live in this hybrid world.
But that doesn't fully answer your   question because there can be a real new 
efficient frontier where it's just agents   working with agents and completely optimized.
Even when agents are working with agents,   what are the primitives that are needed?
Do you need a storage system?  Does that storage system need to have e-discovery?
Do you need to have observability?  Do you need to have an identity system 
that is going to use multiple models   with all having one identity system?
These are all the core underlying rails   we have today for what are the 
Office systems or what have you.  And that's what we will have in the future as 
well. You've talked about databases. I mean man,   I would love all of Excel 
to have a database backend.  I would love for all that to happen immediately.
And that database is a good database.  Databases in fact will be 
a big thing that will grow.  If I think about all of the Office artifacts 
being structured better, the ability to do the   joins between structured and unstructured better 
because of the agentic world, that will grow the   underlying infrastructure business.
It happens that the consumption   of that is all being driven by agents.
You could say all that is just-in-time generated   software by a model company. That could also be 
true. We will be one such model company too. We   will build in... The competition could be that we 
will build a model plus all the infrastructure and   provision it, and then there will be competition 
between a bunch of those folks who can do that.  Speaking of model companies, you say not 
only will you have the infrastructure,   you'll have the model itself.
Right now, Microsoft AI's most   recent model that was released two 
months ago is 36 in Chatbot Arena.  You obviously have the IP rights to OpenAI.
To the extent you agree with that,   it seems to be behind.
Why is that the case, especially given   the fact that you theoretically have the right to 
fork OpenAI's monorepo or distill their models,   especially if it's a big part of your strategy 
that you need to have a leading model company?  First of all, we are absolutely 
going to use the OpenAI models   to the maximum across all of our products.
That's the core thing that we're going to continue   to do all the way for the next seven years, 
and not just use it but then add value to it.  That's where the analyst and this Excel 
agent, these are all things that we will   do where we'll do RL fine-tuning.
We'll do some mid-training runs   on top of a GPT family where we have 
unique data assets and build capability.  With the MAI model, the way that I think 
we’re going to think about it is that the   good news here with the new agreement is 
we can be very, very clear that we're going   to build a world-class superintelligence 
team and go after it with a high ambition.  But at the same time, we're also 
going to use this time to be smart   about how to use both these things.
That means we will, on one end,   be very product-focused, and on the 
other end, be very research-focused.  Because we have access to the GPT family, the last 
thing I want to do is use my flops in a way that   is just duplicative and doesn't add much value.
I want to be able to take the flops that we use   to generate a GPT family and maximize its value, 
while my MAI flops are being used for… Let's take   the image model that we launched, which I 
think is at number nine in the image arena.  We're using it both for cost 
optimization, it's on Copilot,   it's in Bing, and we're going to use that.
We have an audio model in Copilot.  It's got personality and what have you.
We optimized it for our product. So we will   do those. Even on the LMArena, we started 
on the text one and it debuted at like 13.  By the way, it was done 
only on around 15,000 H100s.  It was a very small model.
So it was, again, to prove out   the core capability, the instruction 
following, and everything else.  We wanted to make sure we could 
match what was state of the art.  That shows us, given scaling laws, what we are 
capable of doing if we gave more flops to it.  The next thing we will do is an omni-model where 
we will take the work we have done in audio,   what we have done in image, 
and what we have done in text.  That will be the next pit stop on the MAI side.
So when I think about the MAI roadmap, we are   going to build a first-class 
superintelligence team.  We are going to continue to drop, and 
do it in the open, some of these models.  They will either be used in our products, 
because they're going to be latency-friendly,   cost-friendly, or what have you, or 
they'll have some special capability.  And we will do real research in order to 
be ready for the next five, six, seven,   eight breakthroughs that are all needed on 
this march towards superintelligence—while   exploiting the advantage we have of having the 
GPT family that we can work on top of as well.  Say we roll forward seven years, you 
no longer have access to OpenAI models.  What does Microsoft do to make sure they 
are leading, or have a leading AI lab?  Today, OpenAI has developed many of the 
breakthroughs, whether it be scaling or reasoning.  Or Google's developed all the 
breakthroughs like transformers.  But it is also a big talent game.
You've seen Meta spend north   of $20 billion on talent.
You've seen Anthropic poach the entire   Blueshift reasoning team from Google last year.
You've seen Meta poach a large reasoning and   post-training team from Google more recently.
These sorts of talent wars are   very capital intensive.
Arguably, if you're spending   $100 billion on infrastructure, you should 
also spend X amount of money on the people   using the infrastructure so that they're more 
efficiently making these new breakthroughs.  What confidence can one get that Microsoft 
will have a team that's world-class that   can make these breakthroughs?
Once you decide to turn on   the money faucet—you're being a bit capital 
efficient right now, which is smart it seems,   to not waste money doing duplicative work—but once 
you decide you need to, how can one say, "Oh yeah,   now you can shoot up to the top five model?"
At the end of the day, we're going to build   a world-class team and we already have a 
world-class team that's beginning to be assembled.  We have Mustafa coming in, we have Karen.
We have Amar Subramanya who did a lot of the   post-training at Gemini 2.5 who's at Microsoft.
Nando, who did a lot of the multimedia   work at DeepMind, is there.
We're going to build a world-class team.  In fact, later this week even, Mustafa 
will publish something with a little   more clarity on what our lab is going to go do.
The thing that I want the world to know, perhaps,   is that we are going to build the infrastructure 
that will support multiple models.  Because from a hyperscale perspective, we want 
to build the most scaled infrastructure fleet   that's capable of supporting all the models the 
world needs, whether it's from open source or   obviously from OpenAI and others. That's one 
job. Secondly, in our own model capability,   we will absolutely use the OpenAI model in our 
products and we'll start building our own model.  And we may—like in GitHub Copilot where Anthropic 
is used—even have other frontier models that are   going to be wrapped into our products, as well.
I think that’s how each time… At the end of the   day, the eval of the product as it meets a 
particular task or a job is what matters.  We'll start back from there into the vertical 
integration needed, knowing that as long as   you're serving the market well with the 
product, you can always cost-optimize.  There's a question going forward. 
Right now, we have models that have   this distinction between training and inference.
One could argue that there's a smaller and smaller   difference between the different models.
Going forward, if you're really   expecting something like human-level 
intelligence, humans learn on the job.  If you think about your last 30 years, 
what makes Satya tokens so valuable?  It's the last 30 years of wisdom and 
experience you've gained in Microsoft.  We will eventually have models, if they 
get to human level, which will have   this ability to continuously learn on the job.
That will drive so much value to the model company   that is ahead, at least in my view, because you 
have copies of one model broadly deployed through   the economy learning how to do every single job.
And unlike humans, they can amalgamate   their learnings to that model.
So there's this sort of continuous   learning exponential feedback loop, which almost 
looks like a sort of intelligence explosion.  If that happens and Microsoft isn't 
the leading model company by that time…   You're saying that well, we substitute one model 
for another, et cetera. Doesn’t that then matter   less? Because it's like this one model 
knows how to do every single job in   the economy, the others in the long tail don't.
Your point, if there's one model that is the only   model that's most broadly deployed in the world 
and it sees all the data and it does continuous   learning, that's game set match and you stop shop.
The reality that at least I see is that in the   world today, for all the dominance of 
any one model, that is not the case.  Take coding, there are multiple models.
In fact, everyday it's less the case.  There is not one model that 
is getting deployed broadly.  There are multiple models that are getting 
deployed. It's like databases. It's always   the thing, "Can one database be the one that 
is just used everywhere?" Except it's not.   There are multiple types of databases that 
are getting deployed for different use cases.  I think that there are going to be some 
network effects of continual learning—I   call it data liquidity—that any one model has.
Is it going to happen in all domains? I don't   think so. Is it going to happen in all geos? 
I don't think so. Is it going to happen in all   segments? I don't think so. It'll happen in all 
categories at the same time? I don't think so.   So therefore I feel like the design space is 
so large that there's plenty of opportunity.  But your fundamental point is having a capability 
which is at the infrastructure layer, model layer,   and at the scaffolding layer, and then 
being able to compose these things not   just as a vertical stack, but to be able to 
compose each thing for what its purpose is.  You can't build an infrastructure 
that's optimized for one model.  If you do that, what if you fall behind?
In fact, all the infrastructure   you built will be a waste.
You kind of need to build an   infrastructure that's capable of supporting 
multiple families and lineages of models.  Otherwise the capital you put in, which is 
optimized for one model architecture, means   you're one tweak away, some MoE-like breakthrough 
that happens, and your entire network topology   goes out of the window. That's a scary thing. 
Therefore you kind of want the infrastructure   to support whatever may come in your own model 
family and other model families. You've got to   be open. If you're serious about the hyperscale 
business, you've got to be serious about that.  If you're serious about being a model 
company, you have to basically say,   "What are the ways people can do things on top of 
the model so that I can have an ISV ecosystem?"  Unless I'm thinking I'll own every 
category, that just can't be that.  Then you won't have an API business and that, by 
definition, will mean you'll never be a platform   company that's successfully deployed everywhere.
Therefore the industry structure is such that   it will really force people to specialize.
In that specialization, a company like Microsoft   should compete in each layer by its merits, but 
not think that this is all about the road to game   set match, where I just compose vertically 
all these layers. That just doesn't happen.  So last year Microsoft was on path to be 
the largest infrastructure provider by far.  You were the earliest in 2023, so you went 
out there, you acquired all the resources   in terms of leasing data centers, starting 
construction, securing power, everything.  You guys were on pace to 
beat Amazon in 2026 or 2027.  Certainly by 2028 you were going to beat them.
Since then, let’s call it, in the second half   of last year, Microsoft did this big pause, where 
they let go of a bunch of leasing sites that they   were going to take, which then Google, Meta, 
Amazon in some cases, Oracle, took these sites.  We're sitting in one of the largest data centers 
in the world, so obviously it's not everything,   you guys are expanding like crazy.
But there are sites that you just stopped   working on. Why did you do this?
This goes back a little bit to,   what is the hyperscale business all about?
One of the key decisions we made was that   if we're going to build out Azure to 
be fantastic for all stages of AI—from   training to mid-training to data gen to 
inference—we just need fungibility of the fleet.  So that entire thing caused us basically 
not to go build a whole lot of capacity   with a particular set of generations.
Because the other thing you have to   realize is that having up to now 10x'ed 
every 18 months enough training capacity   for the various OpenAI models, we realized 
that the key is to stay on that path.  But the more important thing is to have a balance, 
to not just train, but to be able to serve these   models all around the world.
Because at the end of the day,   the rate of monetization is what 
will then allow us to keep funding.  And then the infrastructure was going 
to need us to support multiple models.  So once we said that that's the case, we 
just course-corrected to the path we're on.  If I look at the path we're on, we 
are doing a lot more starts now.  We are also buying up as much managed 
capacity as we can, whether it's to build,   whether it's to lease, or even GPUs as a service.
But we're building it for where we see the demand   and the serving needs and our training needs.
We didn't want to just be a hoster for one company   and have just a massive book 
of business with one customer.  That's not a business, you should be 
vertically integrated with that company.  Given that OpenAI was going to be 
a successful independent company,   which is fantastic. It makes sense. And even 
Meta may use third-party capacity, but ultimately   they're all going to be first-party.
For anyone who has large scale,   they'll be a hyperscaler on their own.
To me, it was to build out a hyperscale   fleet and our own research compute. That's what 
the adjustment was. So I feel very, very good.  By the way, the other thing is that I didn't want 
to get stuck with massive scale of one generation.  We just saw the GB200s, the GB300s are coming.
By the time I get to Vera Rubin, Vera Rubin Ultra,   the data center is going to look very different 
because the power per rack, power per row,   is going to be so different.
The cooling requirements are   going to be so different.
That means I don't want to   just go build out a whole number of gigawatts 
that are only for a one-generation, one family.  So I think the pacing matters, the 
fungibility and the location matters,   the workload diversity matters, customer diversity 
matters and that's what we’re building towards.  The other thing that we've learned 
a lot is that every AI workload does   require not only the AI accelerator, but 
it requires a whole lot of other things.  In fact, a lot of the margin structure 
for us will be in those other things.  Therefore, we want to build out Azure as being 
fantastic for the long tail of the workloads,   because that's the hyperscale business, while 
knowing that we've got to be super competitive   starting with the bare-metal 
for the highest end training.  But that can't crowd out the rest of the 
business, because we're not in the business   of just doing five contracts with five customers 
being their bare-metal service. That's not a   Microsoft business. That may be a business 
for someone else, and that's a good thing.  What we have said is that we're in the 
hyperscale business, which is at the end   of the day a long tail business for AI workloads.
And in order to do that, we will have some leading   bare-metal-as-a-service capabilities 
for a set of models, including our own.  And that, I think, is the balance you see.
Another question that comes around   this whole fungibility topic.
Okay, it's not where you want it, you would   rather have it in a good population center, like 
Atlanta. We're here. There's also the question of,   how much does that matter as the horizon of AI 
tasks grows? 30 seconds for a reasoning prompt,   or 30 minutes for a deep research, or it's going 
to be hours for software agents at some point   and days and so on and so forth, 
the time to human interaction.  Why does it matter if it's location A, B, or C?
It’s a great question. That's exactly it. In fact,   that's one of the other reasons why we want to 
think about what an Azure region looks like and   what is the networking between Azure regions.
This is where I think as the model capabilities   evolve and the usage of these tokens evolves, 
whether it's synchronously or asynchronously,   you don't want to be out of position.
Then on top of that, by the way,   what are the data residency laws?
There’s the entire EU thing, where   we literally had to create an EU Data Boundary.
That basically meant that you can't just roundtrip   a call to wherever, even if it's asynchronous.
Therefore you need to have maybe regional   things that are high density, and 
then the power costs and so on.  But you're 100% right in bringing up that the 
topology as we build out will have to evolve.  One, for tokens per dollar per watt. What 
are the economics? Overlay that with,   what is the usage pattern?
Usage pattern in terms   of synchronous, asynchronous.
But also what is the compute storage?  Because the latencies may matter for certain 
things. The storage better be there. If I have   a Cosmos DB close to this for session data or even 
for an autonomous thing, then that also has to be   somewhere close to it, and so on.
All of those considerations are   what will shape the hyperscale business.
Prior to the pause, what we had forecasted for   you, by 2028 you were going to be 12–13 gigawatts.
Now we're at nine and a half or so.  But something that's even more relevant—and 
I just want you to more concretely state that   this is the business you don't want to be 
in—is that Oracle's going from 1/5th your   size to bigger than you by the end of 2027.
While it's not a Microsoft-level quality of   return on invested capital, they're 
still making 35% gross margins.  So the question is, maybe it's not Microsoft's 
business to do this, but you've created a   hyperscaler now by refusing this business, by 
giving away the right of first refusal, et cetera.  First of all, I don't want to take away 
anything from the success Oracle has had in   building their business and I wish them well.
The thing that I think I've answered for you   is that it didn't make sense for us to 
go be a hoster for one model company   with limited time horizon RPO.
Let's just put it that way.  The thing that you have to think through 
is not what you do in the next five years,   but what you do for the next 50.
We made our set of decisions.  I feel very good about our OpenAI 
partnership and what we're doing.  We have a decent book of business.
We wish them a lot of success.  In fact, we are buyers of Oracle capacity. 
We wish them success. But at this point,   I think the industrial logic for what we are 
trying to do is pretty clear, which is that it's   not about chasing… First of all, I track, by 
the way, your things whether it's AWS or Google   and ours, which I think is super useful.
But it doesn't mean I have to chase those.  I have to chase them for not just the gross margin 
that they may represent in a period of time.  What is this book of business that 
Microsoft uniquely can go clear, which   makes sense for us to clear? That's what we'll do.
I have a question even stepping back from this,   I take your point that it's a better business 
to be in, all else equal, to have a long tail   of customers you can have higher margin from 
rather than serving bare metal to a few labs.  But then there's a question of, 
which way is the industry evolving?  If we believe we're on the path to smarter 
and smarter AIs, then why isn't the shape of   the industry that the OpenAIs and Anthropics and 
DeepMinds are the platform on which the long tail   of enterprises are actually doing business?
They need bare metal, but they are the platform.  What is the long tail that 
is directly using Azure?  Because you want to use 
the general cognitive core.  But those models are all going to be available 
on Azure, so any workload that says, "Hey,   I want to use some open source model and an 
OpenAI model," if you go to Azure Foundry today,   you have all these models that you can 
provision, buy PTUs, get a Cosmos DB,   get a SQL DB, get some storage, get some compute.
That's what a real workload looks like.  A real workload is not just 
an API call to a model.  A real workload needs all of these things to 
go build an app or instantiate an application.  In fact, the model companies 
need that to build anything.  It's not just like, "I have a token factory."
I have to have all of these things. That's   the hyperscale business. And it's not on 
any one model, but all of these models.  So if you want Grok plus, say, OpenAI plus 
an open source model, come to Azure Foundry,   provision them, build your application. Here is 
a database. That's kind of what the business is.  There is a separate business called just selling 
raw bare-metal services to model companies.  And that's the argument about 
how much of that business you   want to be in and not be in and what that is.
It's a very different segment of the business,   which we are in, and we also have limits to how 
much of it is going to crowd out the rest of it.  But that's kind of at least the way I look at it.  There are sort of two questions here.
One is, why couldn't you just do both?  The other one is, given our estimates 
on what your capacity is in 2028,   it's three and a half gigawatts lower.
Sure, you could have dedicated that to   OpenAI training and inference capacity, 
but you could have also dedicated that   to actually just running Azure, running 
Microsoft 365, running GitHub Copilot.  I could have just built it 
and not given it to OpenAI.  Or I may want to build it in a different location.
I may want to build it in the UAE,   I may want to build it in India, 
I may want to build it in Europe.  One of the things is, as I said, where we have 
real capacity constraints right now, given   the regulatory needs and the data sovereignty 
needs, we've got to build all over the world.  First of all, stateside capacity is super 
important, and we want to build everything.  But when I look out to 2030, I have a 
global view of what is Microsoft's shape   of business by first-party and third-party.
Third-party segmented by the frontier labs   and how much they want versus the inference 
capacity we want to build for multiple models,   and our own research compute needs.
That's all going into my calculus.  You're rightfully pointing out the pause, 
but the pause was not done because we said,   "Oh my God, we don't want to build that."
We realized that we want to build what we want   to build slightly differently by both workload 
type as well as geo-type and timing as well.  We'll keep ramping up our gigawatts, and the 
question is at what pace and in what location.  And how do I ride Moore's law on it, which is, 
do I really want to overbuild three and a half   in 2027 or do I want to spread that in 2027-28 
knowing even… One of the biggest learnings we had   even with Nvidia is that their pace increased 
in terms of their migrations. That was a big   factor. I didn't want to go get stuck for four 
or five years of depreciation on one generation.  In fact, Jensen's advice to me was two things.
One is, get on the speed-of-light execution.  That's why the execution in 
this Atlanta data center....  I mean, it's like 90 days between when we 
get it and to hand off to a real workload.  That's real speed-of-light 
execution on that front.  I wanted to get good on that.
And then that way I'm building   each generation in scaling.
And then every five years,   you have something much more balanced.
So it becomes literally like a flow   for a large-scale industrial operation like 
this where you're suddenly not lopsided,   where you've built up a lot in one time and then 
you take a massive hiatus because you're stuck   with all this, to your point, in one location 
which may be great for training, or it may not   be great for inference because I can't serve, 
even if it's all asynchronous, because Europe   won't let me round-trip to Texas.
So that's all of the things.  How do I rationalize this statement with 
what you've done over the last few weeks?  You've announced deals with Iris 
Energy, with Nebius, and Lambda Labs,   and there's a few more coming as well.
You're going out there and securing capacity   that you're renting from the neoclouds 
rather than having built it yourself.  It's fine for us because now when you have line 
of sight to demand, which can be served where   people are building, it's great.
In fact we will take leases,   we will take build-to-suit, we'll even take 
GPUs-as-a-service where we don't have capacity   but we need capacity and someone else has that.
And by the way, I would even sort of welcome every   neocloud to just be part of our marketplace. 
Because guess what? If they go bring their   capacity into our marketplace, that customer who 
comes through Azure will use the neocloud, which   is a great win for them, and will use compute, 
storage, databases, all the rest from Azure.  So I'm not at all thinking of this as, "Hey, I 
should just go gobble up all of that myself."  You mentioned how this depreciating asset, in five 
or six years, is 75% of the TCO of a data center.  And Jensen is taking a 75% margin on that.
So what all the hyperscalers are trying to   do is develop their own accelerator so that 
they can reduce this overwhelming cost for   equipment, to increase their margins.
And when you look at where they are,   Google's way ahead of everyone else.
They've been doing it for the longest.  They're going to make something like five 
to seven million chips of their own TPUs.  You look at Amazon and they're trying to make 
three to five million [Lifetime shipment units].  But when we look at what Microsoft is ordering 
of their own chips, it's way below that number.  You've had a program for just as long.
What's going on with your internal chips?  It’s a good question. A couple of things. 
One is that the thing that is the biggest   competitor for any new accelerator is kind 
of even the previous generation of Nvidia.  In a fleet, what I'm going to 
look at is the overall TCO.  The bar I have, even for our own… By the 
way, I was just looking at the data for   Maia 200 which looks great, except that one 
of the things that we learned even on the   compute side… We had a lot of Intel, then 
we introduced AMD, and then we introduced   Cobalt. That's how we scaled it. We have good 
existence proof of, at least in core compute,   how to build your own silicon and then manage a 
fleet where all three are at play in some balance.  Because by the way, even Google's 
buying Nvidia, and so is Amazon.  It makes sense because Nvidia is innovating 
and it's the general-purpose thing.  All models run on it and customer demand is there.
Because if you build your own vertical thing,   you better have your own model, which is either 
going to use it for training or inference,   and you have to generate your own demand 
for it or subsidize the demand for it.  So therefore you want to make 
sure you scale it appropriately.  The way we are going to do it is to have a close 
loop between our own MAI models and our silicon,   because I feel like that's what gives you 
the birthright to do your own silicon,   where you literally have designed the 
microarchitecture with what you're doing,   and then you keep pace with your own models.
In our case, the good news here is that OpenAI   has a program which we have access to.
So therefore to think that Microsoft   is not going to have something that's—
What level of access do you have to that?  All of it.
You just get the IP for all of that?  So the only IP you don't 
have is consumer hardware?  That's it.
Oh, okay. Interesting.  By the way, we gave them a bunch 
of IP as well to bootstrap them.  This is one of the reasons why they… Because 
we built all these supercomputers together.  We built it for them and they 
benefited from it, rightfully so.  And now as they innovate, even at the 
system level, we get access to all of it.  And we first want to instantiate what they 
build, for them, but then we'll extend it.  So if anything, the way I think about your 
question is, Microsoft wants to be a fantastic,   I'll call it, speed-of-light 
execution partner for Nvidia.  Because quite frankly that fleet is life itself.
Obviously Jensen's doing super well with his   margins, but the TCO has many dimensions 
to it and I want to be great at that TCO.  On top of that, I want to be able to 
really work with the OpenAI lineage   and the MAI lineage and the system design, 
knowing that we have the IP rights on both ends.  Speaking of rights, you had an interview a 
couple days ago where you said that in the   new agreement you made with OpenAI you have 
rights, the exclusivity, to the stateless   API calls that OpenAI makes.
We were sort of confused about   if there's any state whatsoever.
You were just mentioning a second   ago that all these complicated workloads that 
are coming up are going to require memory and   databases and storage and so forth.
Is that now not stateless if   ChatGPT is storing stuff on sessions?
That's the reason why. The strategic decision we   made, and also accommodating for the flexibility 
OpenAI needed in order to be able to procure   compute for… Essentially think of OpenAI having 
a PaaS business and a SaaS business. The SaaS   business is ChatGPT. Their PaaS business is 
their API. That API is Azure-exclusive. The   SaaS business, they can run it anywhere.
And they can partner with anyone they   want to to build SaaS products?
If they want a partner and that   partner wants to use a stateless API, then Azure 
is the place where they can get the stateless API.  It seems like there's a way for them to build 
the product together and it's a stateful thing…  No, for even that they'll have to come to Azure.
Again, this is done in the spirit of "what is it   that we value as part of our partnership."
And we made sure that, at the same time,   we were good partners to OpenAI given 
all the flexibility they needed.  So for example, Salesforce wants to integrate 
OpenAI. It's not through an API. They actually   work together, train a model together 
and deploy it on, let's say, Amazon now.  Is that allowed or do they have to use your…
For any custom agreement like that, they will have   to come run it… There are some few exceptions, 
the US government and so on, that we made,   but other than that, they'd have to come to Azure.
Stepping back, when we were walking back and forth   through the factory, one of the things 
you were talking about is that Microsoft,   you can think of it as a software business, but 
now it's really becoming an industrial business.  There's all this capex, 
there's all this construction.  If you just look over the last two 
years, your capex has sort of tripled.  Maybe you extrapolate that forward, it actually 
just becomes this huge industrial explosion.  Other hyperscalers are taking loans. Meta 
has done a $20 billion loan at Louisiana.   They've done a corporate loan. It seems clear 
everyone's free cash flow is going to zero,   which I'm sure Amy is going to beat you up if 
you even try to do that, but what's happening?  I think the structural change is what 
you're referencing, which is massive.  I describe it as we are now a capital-intensive 
business and a knowledge-intensive business.  In fact, we have to use our knowledge to 
increase the ROIC on the capital spend.  The hardware guys have done a 
great job of marketing Moore's Law,   which I think is unbelievable and it's great.  But if you even look at some of the stats I even 
did in my earnings call, for a given GPT family,   the software improvements of really throughput 
in terms of tokens-per-dollar-per-watt that we're   able to get quarter-over-quarter, 
year-over-year, it’s massive.  It's 5x, 10x, maybe 40x in some of these 
cases, just because of how you can optimize.  That's knowledge intensity coming 
to bring out capital efficiency.  That, at some level, is what we have to master.
Some people ask me, what is the difference between   a classic old-time hoster and a hyperscaler? 
Software. Yes, it is capital intensive,   but as long as you have systems know-how, software 
capability to optimize by workload, by fleet...  That's why when we say fungibility, 
there's so much software in it.  It's not just about the fleet.
It's the ability to evict a   workload and then schedule another workload.
Can I manage that algorithm of scheduling around?  That is the type of stuff that 
we have to be world-class at.  So yes, I think we'll still remain a software 
company, but yes, this is a different business   and we're going to manage.
At the end of the day,   the cash flow that Microsoft has allows 
us to have both these arms firing well.  It seems like in the short 
term you have more credence   on things taking a while, being more jagged.
But maybe in the long term you think the people   who talk about AGI and ASI are correct. Sam 
will be right, eventually. I have a broader   question about what makes sense for a hyperscaler 
to do, given that you have to invest massively in   this thing which depreciates over five years.
So if you have 2040 timelines to the kind of   thing that somebody like Sam anticipates 
in three years, what is a reasonable   thing for you to do in that world?
There needs to be an allocation to,   I'll call it, research compute.
That needs to be done like you did R&D.  That's the best way to even 
account for it, quite frankly.  We should think of it as just R&D expense and 
you should say, "What's the research compute   and how do you want to scale it?"
Let's even say it's an order of   magnitude scale in some period.
Pick your thing, is it two years?   Is it 16 months? What have you. That's sort of one 
piece, which is table stakes, that's R&D expenses.  The rest is all demand driven.
Ultimately, you're allowed to build   ahead of demand, but you better have a demand 
plan that doesn't go completely off kilter.  Do you buy… These labs are now projecting 
revenues of $100 billion in 2027–28   and they're projecting revenue to keep 
growing at this rate of 3x, 2x a year…  In the marketplace there's all kinds of 
incentives right now, and rightfully so.  What do you expect an independent lab that 
is sort of trying to raise money to do?  They have to put some numbers out there 
such that they can actually go raise   money so that they can pay their bills 
for compute and what have you. And it's   a good thing. Someone's going to take some risk 
and put it in there, and they've shown traction.  It's not like it's all risk without seeing 
the fact that they've been performing,   whether it's OpenAI, or whether it's Anthropic.
So I feel great about what they've done,   and we have a massive book of business with these 
chaps. So therefore that's all good. But overall   ultimately, there's two simple things.
One is you have to allocate for R&D.   You brought up talent. The talent for 
AI is at a premium. You have to spend   there. You've got to spend on compute.
So in some sense researcher-to-GPU   ratios have to be high.
That is sort of what it takes   to be a leading R&D company in this world.
And that's something that needs to scale,   and you have to have a balance sheet that allows 
you to scale that long before it's conventional   wisdom and so on. That's kind of one thing. But 
the other is all about knowing how to forecast.  As we look across the world, America 
has dominated many tech stacks.  The US owns Windows through Microsoft, 
which is deployed even in China,   that's the main operating system.
Of course, there's Linux,   which is open source, but Windows is deployed 
everywhere in China on personal computers.  You look at Word, it's deployed everywhere.
You look at all these various technologies,   it's deployed everywhere.
And Microsoft and other   companies have grown elsewhere.
They're building data centers   in Europe and in India and in all these other 
places, in Southeast Asia and LatAm and Africa.  In all of these different places, you're building 
capacity. But this seems quite different. Today,   the political aspect of technology, 
of compute… The US administration   didn't care about the dot-com bubble.
It seems like the US administration,   as well as every other administration 
around the world, cares a lot about AI.  The question is, we're sort of in a bipolar world, 
at least with the US and China, but Europe and   India and all these other countries are saying, 
"No, we're going to have sovereign AI as well."  How does Microsoft navigate the difference to the 
90s—where there's one country in the world that   matters, it's America, and our companies 
sell everywhere and therefore Microsoft   benefits massively—to a world where it is bipolar?
Where Microsoft can't just necessarily have the   right to win all of Europe or India or Singapore.
There are actually sovereign AI efforts.  What is your thought process here 
and how do you think about this?  It's a super critical piece. I think that 
the key, key priority for the US tech sector   and the US government is to ensure that 
we not only do leading innovative work,   but that we also collectively build 
trust around the world on our tech stack.  Because I always say the United States is just 
an unbelievable place. It's just unique in   history. It's 4% of the world's population, 
25% of the GDP, and 50% of the market cap.  I think you should think about 
those ratios and reflect on it.  That 50% happens because quite frankly the 
trust the world has in the United States,   whether it's its capital markets 
or whether it's its technology and   its stewardship of what matters at any 
given time in terms of leading sector.  If that is broken, then that's not 
a good day for the United States.  We start with that, which I think President 
Trump gets, the White House, David Sacks,   everyone really, I think, gets it.
So therefore I applaud anything   that the United States government and the 
tech sector jointly does to, for example,   put our own capital at risk, collectively 
as an industry, in every part of the world.  I would like the USG to take credit 
for foreign direct investment by   American companies all over the world.
It's the least talked about, but the best   marketing that the United States should be doing 
is that it's not just about all the foreign direct   investment coming into the United States, but the 
most leading sector, which is these AI factories,   are all being created all over the world. By 
whom? By America and American companies. And   so you start there, and then you even build 
other agreements around it, which are around   their continuity, their legitimate sovereignty 
concerns, around whether it's data residency,   for them to have real agency and 
guarantees on privacy, and so on.  In fact, our European 
commitments are worth reading.  We made a series of commitments to Europe on how 
we will govern our hyperscale investment there   such that the European Union and the 
European countries have sovereignty.  We're also building sovereign 
clouds in France and in Germany.  We have something called Sovereign Services on 
Azure, which literally gives people key management   services along with confidential computing, 
including confidential computing in GPUs, which   we've done great innovative work with Nvidia.
So I feel very, very good about being able to   build, both technically and through policy, 
this trust in the American tech stack.  How do you see this shaking out as you have 
this network effect with continual learning   and things on the model level?
Maybe you have equivalent   things at the hyperscaler level as well.
Do you expect that the countries will say,   "Look, it's clear one model or a couple models 
are the best, and so we're going to use them,   but we're going to have some laws around the 
weights having to be hosted in our country"?  Or do you expect that there will be this push so 
that it has to be a model trained in our country?  Maybe an analogy here is that semiconductors 
are very important to the economy,   and people would like to have their sovereign 
semiconductors, but TSMC is just better.  And semiconductors are so important to 
the economy that you will just go to   Taiwan and buy the semiconductors. You 
have to. Will it be like that with AI?  Ultimately, what matters is the use of AI 
in their economy to create economic value.  That's the diffusion theory, which 
ultimately, it's not the leading sector,   but it's the ability to use the leading technology 
to create your own comparative advantage.  So I think that will 
fundamentally be the core driver.  But that said, they will want continuity of that.
So in some sense, that's one of the reasons why,   I believe, there's always going to be a 
check to "Hey, can this one model have all   the runaway deployment?"
That's why open source   is always going to be there.
There will be, by definition, multiple   models. That'll be one way. That's one way for 
people to sort of demand continuity and not have   concentration risk, that’s another way to say it.
And so you say, "Hey, I want multiple models,   and then I want an open source."
I feel that as long as that's there,   every country will feel like, "Okay, I don't 
have to worry about deploying the best model   and broadly diffusing because I can always take 
what is my data and my liquidity and move it   to another model, whether it's open source 
or from another country or what have you."  Concentration risk and sovereignty, which is 
really agency, those are the two things that   will drive the market structure.
The thing about this is that   this doesn't exist for semiconductors.
All refrigerators, cars have chips made in Taiwan.  It didn't exist until now.
Even then, if Taiwan is cut off,   there are no more cars or no more refrigerators.
TSMC Arizona is not replacing any   real fraction of the production.
The sovereignty is a bit of a scam, if you will.  It's worthwhile having it, it's 
important to have it, but it's not   real sovereignty. We're a global economy.
I think it’s kind of like saying, "Hey,   at this point, we've not learned anything about 
what resilience means and what one needs to do."  Any nation state, including the United 
States, at this point will do what it   takes to be more self-sufficient on 
some of these critical supply chains.  So I, as a multinational company, have to 
think about that as a first-class requirement.  If I don't, then I'm not respecting what is in 
the policy interests of that country long-term.  I'm not saying they won't make 
practical decisions in the short term.  Absolutely, globalization can't just be rewound.
All these capital investments cannot be made   in a way, at the pace at which… But at the same 
time, think about it, if somebody showed up in   Washington and said, "Hey, we're not going to 
build any semiconductor plants," they're going   to be kicked out of the United States.
The same thing is going to be   true in every other country, too.
So therefore we have to, as companies,   respect what the lessons learned are, whether 
it's that the pandemic woke us up or whatever.  But nevertheless people are saying, 
"Look, globalization was fantastic.  It helped supply chains be 
globalized and be super efficient.  But there's such a thing called 
resilience, and we want resilience."  So therefore that feature will get built.
At what pace, I think,   is the point you are making.
You can't snap your fingers   and say all the TSMC plants now are all in 
Arizona with all their capability. They're   not going to be. But is there a plan? There 
will be a plan. And should we respect that?   Absolutely. So I feel that that’s the world.
I want to meet the world where it is and on what   it wants to do going forward, as opposed 
to saying, "Hey, we have a point of view   that doesn't respect your view."
Just to make sure I understand,   the idea here is that each country will want 
some kind of data residency, privacy, et cetera.  And Microsoft is especially privileged here 
because you have relationships with these   countries, you have expertise in setting 
up these kinds of sovereign data centers.  Therefore Microsoft is uniquely fit for a 
world with more sovereignty requirements.  I don't want to sort of describe it 
as somehow we're uniquely privileged.  I would just say I think of that as a business 
requirement that we have been doing all the hard   work all these decades, and we plan to.
So my answer to Dylan's previous question   was that I take—whether it's in the United 
States, or when the White House and the USG says,   "We want you to allocate more of your wafer 
starts to fabs in the US"—we take that seriously.  Or whether it is data centers and the 
EU boundary, we take that seriously.  So to me, respecting what are legitimate 
reasons why countries care about sovereignty,   building for it as a software and 
a physical plant, is what we'll do.  As we go to the bipolar world—US, 
China—it's not just you versus Amazon,   or you versus Anthropic, or you versus Google.
There is a whole host of competition.  How does America rebuild the trust?
What do you do to rebuild the trust?  To say, "Actually, no, American companies 
will be the main provider for you."  And how do you think about competition with 
up and coming Chinese companies, whether it   be ByteDance and Alibaba or Deepseek and Moonshot?
To add to that question, one concern is how we're   talking about how AI is becoming this industrial 
capex race where you're rapidly having to build   quickly across all loads of supply chain.
When you hear that, at least up until now,   you just think about China. This is their 
comparative advantage. And especially if we're not   going to moonshot to ASI next year, but it's going 
to be decades of buildouts and infrastructure,   how do you deal with Chinese competition?
Are they privileged in that world?  It’s a great question. In fact, you just 
made the point of why trust in American   tech is probably the most important feature.
It's not even the model capability, maybe.  It is, "can I trust you, the company, 
can I trust you, your country, and its   institutions to be a long-term supplier?"
That may be the thing that wins the world.  That's a good note to end on.
Satya, thank you for doing this.  Thank you so much. Thank you.
Thank you.  It's awesome. You two guys are quite the team.
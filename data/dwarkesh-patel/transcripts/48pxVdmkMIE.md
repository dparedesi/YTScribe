---
video_id: 48pxVdmkMIE
video_url: https://www.youtube.com/watch?v=48pxVdmkMIE
title: Fully autonomous robots are much closer than you think – Sergey Levine
author: Dwarkesh Patel
published_date: 2025-09-12
length_minutes: 88.47
views: 183997
description: "Sergey Levine is one of the world’s top robotics researchers and co-founder of Physical Intelligence. He thinks we’re on the cusp of a “self-improvement flywheel” for general-purpose robots. His median estimate for when robots will be able to run households entirely autonomously? 2030.  If Sergey’s right, the world 5 years from now will be an *insanely* different place than it is today. This conversation focuses on understanding how we get there: we dive into foundation models for robotics, and ..."
is_generated: False
is_translatable: True
---

Today I'm chatting with Sergey Levine, who 
is a co-founder of Physical Intelligence,   which is a robotics foundation model company, 
and also a professor at UC Berkeley and just   generally one of the world's leading 
researchers in robotics, RL, and AI.  Sergey, thank you for coming on the podcast.
Thank you, and thank you for   the kind introduction.
Let's talk about robotics. Before   I pepper you with questions, I'm wondering if you 
can give the audience a summary of where Physical   Intelligence is at right now.
You guys started a year ago.  What does the progress look like?
What are you guys working on?  Physical Intelligence aims to 
build robotic foundation models.  That basically means general-purpose 
models that could in principle   control any robot to perform any task.
We care about this because we see this as a   very fundamental aspect of the AI problem.
The robot is essentially   encompassing all AI technology.
If you can get a robot that's truly   general, then you can do, hopefully, 
a large chunk of what people can do.  Where we're at right now is that we've 
kind of gotten to the point where we've   built out a lot of the basics.
Those basics actually are pretty   cool. They work pretty well. We can get a robot 
that will fold laundry and that will go into   a new home and try to clean up the kitchen.
But in my mind, what we're doing at Physical   Intelligence right now is really 
the very, very early beginning.  It's just putting in place the basic 
building blocks, on top of which we can   then tackle all these really tough problems.
What's a year-by-year vision? One year in,   I got a chance to watch some of the robots, 
they can do pretty dexterous tasks like folding   a box using grippers.
It's pretty hard to   fold the box even with my hands.
If you had to go year by year until   we get to the full robotics explosion, 
what is happening every single year?  What is the thing that needs 
to be unlocked, et cetera?  There are a few things that we need to get right.
Dexterity obviously is one of them.  In the beginning we really want to make sure 
that we understand whether the methods that   we're developing have the ability to tackle 
the kind of intricate tasks that people can do.  As you mentioned, folding a box, folding different 
articles of laundry, cleaning up a table,   making a coffee, that sort of thing. That's 
good, that works. The results we've been   able to show are pretty cool, but the end 
goal of this is not to fold a nice T-shirt.  The end goal is to just confirm our initial 
hypothesis that the basics are solid.  From there, there are a number 
of really major challenges.  Sometimes when results get abstracted to the level 
of a three-minute video, someone can look at this   video and it's like, "Oh, that's cool. That's what 
they're doing." But it's not. It's a very simple   and basic version of what I think is to come.
What you really want from a robot is not to   tell it like, "Hey, please fold my T-shirt."
What you want from a robot is to tell it like,   "Hey, robot, you're now doing 
all sorts of home tasks for me.  I like to have dinner made at 6:00 p.m.
I wake up and go to work at 7:00 a.m.  I like to do my laundry on Saturday, so make 
sure that it's ready. This and this and this.   By the way, check in with me every Monday to 
see what I want you to pick up when you do the   shopping." That's the prompt. Then the robot 
should go and do this for six months, a year.  That's the duration of the task.
Ultimately if this stuff is   successful, it should be a lot bigger.
It should have that ability to learn continuously.  It should have the understanding of the physical 
world, the common sense, the ability to go in and   pull in more information if it needs it.
Let’s say I ask it, "Hey, tonight,   can you make me this type of salad?"
It should figure out what that entails,   look it up, go and buy the ingredients.
There's a lot that goes into this. It   requires common sense. It requires understanding 
that there are certain edge cases that you need   to handle intelligently, cases 
where you need to think harder.  It requires the ability to improve continuously.
It requires understanding safety, being reliable   at the right time, being able to fix your 
mistakes when you do make those mistakes.  There's a lot more that goes into this.
But the principles there are:   you need to leverage prior knowledge and 
you need to have the right representations.  This grand vision, what year? If you had 
to give an estimate. 25 percentile, 50, 75?  I think it's something where it's not going to 
be a case where we develop everything in the   laboratory and then it's done and then come 
2030-something, you get a robot in a box.  Again, it'll be the same as what 
we've seen with AI assistants.  Once we reach some basic level of competence 
where the robot is delivering something useful,   it'll go out there in the world.
The cool thing is that once it's out   there in the world, they can collect experience 
and leverage that experience to get better.  To me, what I tend to think about in terms of 
timelines is not the date when it will be done,   but the date when the flywheel starts basically.
When does the flywheel start?  That could be very soon. There's 
some decisions to be made.  The trade-off there is that the more 
narrowly you scope the thing, the   earlier you can get it out into the real world.
But this is something we're already exploring.  We're already trying to figure out what 
are the real things this thing can do that   could allow us to start spinning the flywheel.
But in terms of stuff that you would actually   care about, that you would want to see… I don't 
know but single-digit years is very realistic.  I'm really hoping it'll be more like one or 
two before something is actually out there,   but it's hard to say.
Something being out   there means what? What is out there?
It means that there is a robot that does a thing   that you actually care about, that you want done.
It does so competently enough to actually do it   for real, for real people that want it done.
We already have LLMs which are broadly deployed.  That hasn't resulted in some sort of flywheel, 
at least not some obvious flywheel for the model   companies where now Claude is learning how to do 
every single job in the economy or GPT's learning   how to do every single job in the economy.
So, why doesn’t that flywheel work for LLMs?  Well, I think it's actually very close 
to working and I am 100% certain that   many organizations are working on exactly this.
In fact, arguably there is already a flywheel.  It’s not an automated flywheel 
but a human-in-the-loop flywheel.  Everybody who's deploying an LLM is of course 
going to look at what it's doing and it's going   to use that to then modify its behavior.
It's complex because it comes back to this   question of representations and figuring out the 
right way to derive supervision signals and ground   those supervision signals in the behavior of 
the system so that it improves on what you want.  I don't think that's a 
profoundly impossible problem.  It's just something where the details get 
pretty gnarly and challenges with algorithms   and stability become pretty complex.
It's something that's taken a while for   the community collectively to get their hands on.
Do you think it'll be easier for robotics?  Or do you think that with these kinds of 
techniques to label data that you collect out   in the world and use it as a reward, the whole 
wave will rise and robotics will rise as well?  Or is there some reason robotics 
will benefit more from this?  I don't think there's a profound 
reason why robotics is that different.  There are a few small differences that 
make things a little bit more manageable.  Especially if you have a robot that's doing 
something in cooperation with people, whether   it's a person that's supervising it or directing 
it, there are very natural sources of supervision.  There's a big incentive for the person to provide 
the assistance that will make things succeed.  There are a lot of dynamics where you can 
make mistakes and recover from those mistakes   and then reflect back on what happened 
and avoid that mistake in the future.  When you're doing physical 
things in the real world,   that stuff just happens more often than it does 
if you're an AI assistant answering a question.  If you answer a question and just answer it wrong,   it's not like you can just go 
back and tweak a few things.  The person you told the answer to 
might not even know that it's wrong.  Whereas if you're folding the T-shirt and you 
messed up a little bit, it's pretty obvious.  You can reflect on that, figure out what 
happened, and do it better next time.  Okay, in one year we have robots 
which are doing some useful things.  Maybe if you have some relatively simple 
loopy process, they can do it for you,   like keep folding thousands of boxes or something.
But then there's some flywheel… and there's some   machine which will just run my house for 
me as well as a human housekeeper would.  What is the gap between this thing which 
will be deployed in a year that starts   the flywheel and this thing which is 
like a fully autonomous housekeeper?  It's actually not that different from what we've 
seen with LLMs in some ways. It's a matter of   scope. Think about coding assistants. 
Initially the best tools for coding,   they could do a little bit of completion.
You give them a function signature and   they'll try their best to type out the whole 
function and they'll maybe get half of it right.  As that stuff progresses, then you're willing 
to give these things a lot more agency.  The very best coding assistance now—if you're 
doing something relatively formulaic, maybe it can   put together most of a PR for you for something 
fairly accessible. It'll be the same thing. We'll   see an increase in the scope that we're willing to 
give to the robots as they get better and better.  Initially the scope might be 
a particular thing you do.  You're making the coffee or something.
As they get more capable, as their ability to have   common sense and a broader repertoire of tasks 
increases, then we'll give them greater scope.  Now you're running the whole coffee shop.
I get that there's a spectrum.  I get that there won't be a specific 
moment that feels like we've achieved it   but if you had to give a year for your 
median estimate of when that happens?  My sense there too is that this 
is probably a single-digit thing   rather than a double-digit thing.
The reason it's hard to really pin   down is because, as with all research, it does 
depend on figuring out a few question marks.  My answer in terms of the nature of those question 
marks is that I don't think these are things that   require profoundly, deeply different ideas 
but it does require the right synthesis   of the kinds of things that we already know.
Sometimes synthesis, to be clear, is just as   difficult as coming up with profoundly new stuff.
It's intellectually a very   deep and profound problem.
Figuring that out is going to be very exciting.  But I think we kind of know roughly the puzzle 
pieces and it's something that we need to work on.  If we work on it and we're a bit lucky 
and everything kind of goes as planned,   single-digit is reasonable.
I'm just going to do   binary search until I get a year.
It's less than 10 years, so more than five years,   your median estimate? I know there's a range.
I think five is a good median.  Okay, five years. If you can fully 
autonomously run a house, then you   can fully autonomously do most blue-collar work.
Your estimate is that in five years it should be   able to do most blue-collar work in the economy.
There's a nuance here. It becomes more obvious if   we consider the analogy to coding assistants.
It's not like the nature of coding assistants   today is that there's a switch that 
flips and instead of writing software,   suddenly all software engineers get fired 
and everyone's using LLMs for everything.  It actually makes a lot of sense that the 
biggest gain in productivity comes from experts,   which is software engineers, whose productivity 
is now augmented by these really powerful tools.  Separate from the question of whether people 
will get fired or not, a different question is,   what will the economic impact be in five years?
The reason I'm curious about this is because with   LLMs, the relationship between the 
revenues for these models to their seeming   capability has been sort of mysterious.
You have something which feels like AGI.  You can have a conversation where 
it really passes the Turing test.  It really feels like it can 
do all this knowledge work.  It's obviously doing a bunch of coding, et cetera.
But the revenues from these AI companies   are cumulatively on the order of $20-30 
billion per year and that's much less than   all knowledge work, which is $30-40 trillion.
In five years are we in a similar situation to   what LLMs are in now, or is it more like we have 
robots deployed everywhere and they're actually   doing a whole bunch of real work, et cetera?
It's a very subtle question. What it probably   will come down to is this question of scope.
The reason that LLMs aren't doing all software   engineering is because they're good within 
a certain scope, but there's limits to that.  Those limits are increasing, 
to be clear, every year.  I think that there's no reason that we wouldn't 
see the same kind of thing with robots.  The scope will have to start out small 
because there will be certain things that   these systems can do very well and certain 
other things where more human oversight is   really important. The scope will grow. What that 
will translate into is increased productivity.  Some of that productivity will come from 
the robots themselves being valuable.  Some of it will come from the people using the 
robots are now more productive in their work.  But there's so many things 
which increase productivity.  Like wearing gloves increases 
productivity or I don't know.  You want to understand something which 
increases productivity a hundredfold   versus something which has a small increase.
Robots already increase productivity for workers.  Where LLMs are right now in terms of the share 
of knowledge work they can do, is I guess like   1/1000th of the knowledge work that happens 
in the economy, at least in terms of revenue.  Are you saying that fraction will be possible 
for robots, but for physical work, in five years?  That's a very hard question to answer.
I'm probably not prepared to tell you   what percentage of all labor work can be done 
by robots, because I don't think right now,   off the cuff, I have a sufficient understanding 
of what's involved in that big of a cross-section   of all physical labor.
What I can tell you is this.  It's much easier to get effective systems rolled 
out gradually in a human-in-the-loop setup.  Again, this is exactly what 
we've seen with coding systems.  I think we'll see the same thing with automation, 
where basically robot plus human is much better   than just human or just robot. That just makes 
total sense. It also makes it much easier   to get all the technology bootstrapped.
Because when it's robot plus human now,   there's a lot more potential for the robot to 
actually learn on the job, acquire new skills.  Because a human can label what's happening?
Also because the human can help,   the human can give hints.
Let me tell you this story.  When we were working on the π0.5 project, 
the paper that we released last April,   we initially controlled our robots with 
teleoperation in a variety of different settings.  At some point we actually realized that 
we can actually make significant headway,   once the model was good enough, by supervising 
it not just with low-level actions but actually   literally instructing it through language.
Now you need a certain level of competence   before you can do that, but once you have that 
level of competence, just standing there and   telling the robot, "Okay, now pick up the cup, 
put the cup in the sink, put the dish in the   sink," just with words already, actually gives the 
robot information that it can use to get better.  Now imagine what this implies 
for the human plus robot dynamic.  Now basically, learning for these systems 
is not just learning from raw actions,   it's also learning from words.
Eventually it’ll be learning   from observing what people do from the kind of 
natural feedback that you receive when you're   doing a job together with somebody else.
This is also the kind of stuff where the   prior knowledge that comes from these big 
models is tremendously valuable, because that   lets you understand that interaction dynamic.
There's a lot of potential for these kinds of   human plus robot deployments 
to make the model better.  In terms of robotics progress, 
why won't it be like self-driving cars, where it's been more than
10 years since Google   launched its… Wasn't it in 2009 that they 
launched the self-driving car initiative?  I remember when I was a teenager, watching demos 
where we would go buy a Taco Bell and drive back.  Only now do we have them actually deployed.
Even then they may make mistakes, etc.  Maybe it'll be many more years before 
most of the cars are self-driving.  You're saying five years 
to this quite robust thing,   but actually will it just feel like 20 years?
Once we get the cool demo in five years,   then it'll be another 10 years before we 
have the Waymo and the Tesla FSD working.  That's a really good question. One of the big 
things that is different now than it was in 2009   has to do with the technology for machine learning 
systems that understand the world around them.  Principally for autonomous 
driving, this is perception.  For robots, it can mean a 
few other things as well.  Perception certainly was 
not in a good place in 2009.  The trouble with perception is that it's one 
of those things where you can nail a really   good demo with a somewhat engineered system, but 
hit a brick wall when you try to generalize it.  Now at this point in 2025, we have much 
better technology for generalizable and   robust perception systems and, more 
generally, generalizable and robust   systems for understanding the world around us.
When you say that the system is scalable,   in machine learning scalable 
really means generalizable.  That gives us a much better starting point today.
That's not an argument about robotics being easier   than autonomous driving.
It's just an argument for   2025 being a better year than 2009.
But there's also other things about   robotics that are a bit different than driving.
In some ways, robotic manipulation is a much,   much harder problem.
But in other ways, it's   a problem space where it's easier to get rolling, 
to start that flywheel with a more limited scope.  To give you an example, if you're learning 
how to drive, you would probably be pretty   crazy to learn how to drive on your 
own without somebody helping you.  You would not trust your teenage child 
to learn to drive just on their own,   just drop them in the car and say, "Go for it."
That's also a 16-year-old who's had a significant   amount of time to learn about the world.
You would never even dream of putting a   five-year-old in a car and 
telling him to get started.  But if you want somebody to clean 
the dishes, dishes can break too.  But you would probably be okay with a child trying 
to do the dishes without somebody constantly   sitting next to them with a brake, so to speak.
For a lot of tasks that we want to do with   robotic manipulation, there's potential to 
make mistakes and correct those mistakes.  When you make a mistake and correct it, well first 
you've achieved the task because you've corrected,   but you've also gained knowledge that allows 
you to avoid that mistake in the future.  With driving, because of the dynamics of how it's 
set up, it's very hard to make a mistake, correct   it and then learn from it because the mistakes 
themselves have significant ramifications.  Not all manipulation tasks are that.
There are truly some very safety-critical stuff.  This is where the next thing 
comes in, which is common sense.  Common sense, meaning the ability to 
make inferences about what might happen   that are reasonable guesses, but that do not 
require you to experience that mistake and   learn from it in advance. That's tremendously 
important. That's something that we basically   had no idea how to do about five years ago.
But now we can use LLMs and VLMs and ask them   questions and they will make reasonable guesses.
They will not give you expert behavior,   but you can say, "Hey, there's 
a sign that says slippery floor.  What's going to happen when I walk 
up over that?" It's pretty obvious,   right? No autonomous car in 2009 would 
have been able to answer that question.  Common sense plus the ability to make 
mistakes and correct those mistakes,   that's sounding an awful lot what a person 
does when they're trying to learn something.  All of that doesn't make robotic manipulation easy 
necessarily, but it allows us to get started with   a smaller scope and then grow from there.
So for years, I mean not since 2009,   but we've had lots of video data, language 
data, and transformers for 5-8 years.  Lots of companies have tried to build 
transformer-based robots with lots of training   data, including Google, Meta, et cetera.
What is the reason that they've been   hitting roadblocks? What has changed now?
That's a really good question. I'll start out with   a slight modification to your comment.
They've made a lot of progress.  In some ways, a lot of the work that we're 
doing now at Physical Intelligence is built   on the backs of lots of other great work 
that was done, for example, at Google.  Many of us were at Google before.
We were involved in some of that work.  Some of it is work that we're 
drawing on that others did.  There's definitely been a lot of progress there.
But to make robotic foundation models really work,   it's not just a laboratory science experiment.
It also requires industrial scale building effort.  It's more like the Apollo program 
than it is a science experiment.  The excellent research that was done 
in the past industrial research labs,   and I was involved in much of that, was very much 
framed as a fundamental research effort. That's   good. The fundamental research is really 
important, but it's not enough by itself.  You need the fundamental research and you 
also need the impetus to make it real.  Making it real means actually putting the robots 
out there, getting data that is representative,   the tasks that they need to do in the real 
world, getting that data at scale, building   out the systems, and getting all that stuff right.
That requires a degree of focus, a singular focus   on really nailing the robotic foundation model 
for its own sake, not just as a way to do more   science, not just as a way to publish a paper, 
and not just as a way to have a research lab.  What is preventing you now from 
scaling that data even more?  If data is a big bottleneck, why can't you 
just increase the size of your office 100x,   have 100x more operators operating 
these robots and collecting more data.  Why not ramp it up immediately 100x more?
That's a really good question. The challenge   here is understanding which axes of scale 
contribute to which axes of capability.  If we want to expand capability 
horizontally—meaning the robot knows how to   do 10 things now and I'd like it to do 100 things 
later—that can be addressed by just directly   horizontally scaling what we already have.
But we want to get robots to a level of   capability where they can do practically 
useful things in the real world.  That requires expanding along other axes too.
It requires, for example,   getting to very high robustness.
It requires getting them to perform   tasks very efficiently, quickly.
It requires them to recognize   edge cases and respond intelligently.
Those things can also be addressed with scaling.  But we have to identify the right axes for that, 
which means figuring out what data to collect,   what settings to collect it in, what methods 
consume that data, and how those methods work.  Answering those questions more thoroughly 
will give us greater clarity on the axes,   on those dependent variables, on 
the things that we need to scale.  We don't fully know right 
now what that will look like.  I think we'll figure it out pretty soon.
It's something we're working on actively.  We want to really get that right 
so that when we do scale it up,   it'll directly translate into capabilities 
that are very relevant to practical use.  Just to give an order of magnitude, how 
does the amount of data you have collected   compare to internet-scale pre-training data?
I know it's hard to do a token-by-token count,   because how does video information compare 
to internet information, et cetera.  But using your reasonable 
estimates, what fraction?  It's very hard to do because robotic 
experience consists of time steps   that are very correlated with each other.
The raw byte representation is enormous,   but probably the information 
density is comparatively low.  Maybe a better comparison is to the datasets 
that are used for multimodal training.  And there, I believe last time we did that count, 
it was between one and two orders of magnitude.  The vision you have of robotics, 
will it not be possible until you   collect what, 100x, 1000x more data?
That's the thing, we don't know that.  It's certainly very reasonable to 
infer that robotics is a tough problem.  Probably it requires as much 
experience as the language stuff.  But because we don't know the answer to that, 
to me a much more useful way to think about   it is not how much data do we need to get 
before we're fully done, but how much data   do we need to get before we can get started.
That means before we can get a data flywheel   that represents a self-sustaining and 
ever-growing data-collection recipe.  When you say self-sustaining, is it just learning 
on the job or do you have something else in mind?  Learning on the job or acquiring data in a way 
such that the process of acquisition of that data   itself is useful and valuable.
I see. Some kind of RL.  Doing something actually real. 
Ideally I would like it to be RL,   because with RL you can get away with the 
robot acting autonomously which is easier.  But it's not out of the question 
that you can have mixed autonomy.  As I mentioned before, robots can 
learn from all sorts of other signals.  I described how we can have a robot 
that learns from a person talking to it.  There's a lot of middle ground in between fully 
teleoperated robots and fully autonomous robots.  How does the π0 model work?
The current model that we   have basically is a vision-language model 
that has been adapted for motor control.  To give you a little bit of a fanciful brain 
analogy, a VLM, a vision-language model,   is basically an LLM that has had a little pseudo 
visual cortex grafted to it, a vision encoder.  Our models, they have a vision encoder, 
but they also have an action expert,   an action decoder essentially.
It has a little visual cortex   and notionally a little motor cortex.
The way that the model makes decisions   is it reads in the sensory information from the 
robot. It does some internal processing. That   could involve outputting intermediate steps.
You might tell it, "Clean up the kitchen."  It might think to itself, 
"Hey, to clean up the kitchen,   I need to pick up the dish and I need to pick 
up the sponge and I need to put this and this."  Eventually it works its way through that 
chain-of-thought generation down to the   action expert, which produces continuous actions.
That has to be a different module because the   actions are continuous, they're high frequency.
They have a different data format than   text tokens.
But structurally   it's still an end-to-end transformer.
Roughly speaking, technically, it   corresponds to a mixture-of-experts architecture.
And what is actually happening is that it's   predicting "I should do X thing."
Then there's an image token,   then some action tokens –what it actually 
ends up doing– and then more image,   more text description, more action tokens.
Basically I'm looking at what stream is going on.  That's right, with the exception that the 
actions are not represented as discrete tokens.  It actually uses flow matching and diffusion 
because they're continuous and you need to be very   precise with your actions for dexterous control.
I find it super interesting that you're   using the open-source Gemma model, which is 
Google's LLM that they released open source,   and then adding this action expert on top.
I find it super interesting that the progress   in different areas of AI is based on not only the 
same techniques, but literally the same model.  You can just use an open-source LLM 
and add this action expert on top.  You naively might think that, "Oh, there's a 
separate area of research which is robotics,   and there's a separate area of research called 
LLMs and natural language processing." No,   it's literally the same. The considerations 
are the same, the architectures are the same,   even the weights are the same.
I know you do more training on   top of these open-source models, 
but I find that super interesting.  One theme here that is important to keep in mind 
is that the reason that those building blocks   are so valuable is because the AI community has 
gotten a lot better at leveraging prior knowledge.  A lot of what we're getting from the pre-trained 
LLMs and VLMs is prior knowledge about the world.  It's a little bit abstracted knowledge.
You can identify objects, you can figure   out roughly where things are 
in image, that sort of thing.  But if I had to summarize in one 
sentence, the big benefit that   recent innovations in AI give to robotics 
is the ability to leverage prior knowledge.  The fact that the model is the same model, 
that's always been the case in deep learning.  But it's that ability to 
pull in that prior knowledge,   that abstract knowledge that can come from 
many different sources that's really powerful.  I was talking to this researcher, Sander at 
GDM, and he works on video and audio models.  He made the point that the reason, in his 
view, we aren't seeing that much transfer   learning between different modalities.
That is to say, training a language model   on video and images doesn't seem to necessarily 
make it that much better at textual questions and   tasks because images are represented at 
a different semantic level than text.  His argument is that text has this high-level 
semantic representation within the model, whereas   images and videos are just compressed pixels.
When they're embedded, they don't represent   some high-level semantic information. 
They're just compressed pixels. Therefore   there's no transfer learning at the level 
at which they're going through the model.  Obviously this is super relevant 
to the work you're doing.  Your hope is that by training the model 
on the visual data that the robot sees,   visual data generally maybe even from YouTube or 
whatever eventually, plus language information,   plus action information from the robot itself, all 
of this together will make it generally robust.  You had a really interesting blog post about why 
video models aren't as robust as language models.  Sorry, this is not a super well-formed question.
I just wanted to get a reaction.  Yeah, what’s up with that? I have 
maybe two things I can say there.  I have some bad news and some good news.
The bad news is what you're saying is   really getting at the core of a long-running 
challenge with video and image generation models.  In some ways, the idea of getting 
intelligent systems by predicting   video is even older than the idea of getting 
intelligent systems by predicting text.  The text stuff turned into practically useful 
things earlier than the video stuff did.  I mean, the video stuff is great. You 
can generate cool videos. The work   that's been done there recently is amazing.
But it's not like just generating videos and   images has already resulted in systems that 
have this deep understanding of the world   where you can ask them to do stuff beyond 
just generating more images and videos.  Whereas with language, clearly it has.
This point about representations   is really key to it.
One way we can think about it is this.  Imagine pointing a camera outside this building, 
there's the sky, the clouds are moving around,   the water, cars driving around, people.
If you want to predict everything that'll   happen in the future, you can 
do so in many different ways.  You can say, "Okay, there's people around.
Let me get really good at understanding the   psychology of how people behave in 
crowds and predict the pedestrians."  But you could also say, "Well, 
there's clouds moving around.  Let me understand everything about water 
molecules and ice particles in the air."  You could go super deep on that.
If you want to fully understand   down to the subatomic level everything that's 
going on, as a person you could spend decades   just thinking about that and you'll never 
even get to the pedestrians or the water.  If you want to really predict everything 
that's going on in that scene, there's   just so much stuff that even if you're 
doing a really great job and capturing   100% of something, by the time you get to 
everything else, ages will have passed.  Whereas with text, it's already been abstracted 
into those bits that we as humans care about.   The representations are already there. 
They're not just good representations,   they focus on what really matters. That's the 
bad news. Here's the good news. The good news   is that we don't have to just get everything 
out of pointing a camera outside this building.  When you have a robot, that 
robot is trying to do a job.  It has a purpose, and its perception is 
in service to fulfilling that purpose.  That is a really great focusing factor.
We know that for people, this really matters.  Literally what you see is affected 
by what you're trying to do.  There's been no shortage of psychology experiments 
showing that people have almost a shocking degree   of tunnel vision where they will literally 
not see things right in front of their eyes   if it's not relevant to what they're trying to 
achieve. That is tremendously powerful. There   must be a reason why people do that.
Certainly if you're out in the jungle,   seeing more is better than seeing less.
If you have that powerful focusing mechanism,   it must be darn important for 
getting you to achieve your goal.  Robots will have that focusing mechanism 
because they're trying to achieve a goal.  The fact that video models aren't as 
robust, is that bearish for robotics?  So much of the data you will have to use… I 
guess you're saying a lot of it will be labeled.  Ideally, you just want to be able to throw 
everything on YouTube, every video we've   ever recorded, and have it learn how the 
physical world works and how to move about.  Just see humans performing 
tasks and learn from that.  I guess you're saying it's hard to learn just from 
that and it needs to practice the task itself.  Let me put it this way.
Let's say that I gave you lots of videotapes   or lots of recordings of different sporting 
events and gave you a year to just watch sports.  After that year, I told you, "Okay, now your 
job, you're going to be playing tennis." Okay,   that's pretty dumb right? Whereas if I told 
you first you're going to be playing tennis   and then I let you study up, now you 
really know what you're looking for.  There's a very real challenge here.
I don't want to understate the challenge.  But there's also a lot of potential for foundation 
models that are embodied, that learn from   interaction, from controlling robotic systems, 
to be better at absorbing the other data sources   because they know what they're trying to do.
I don't think that by itself is a silver bullet.  I don't think it solves 
everything, but it does help a lot.  We've already seen the beginnings of that where 
we can see that including web data in training for   robots really does help with generalization.
I have the suspicion that in the long run,   it'll make it easier to use those sources of 
data that have been tricky to use up until now.  Famously, LLMs have all these emergent 
capabilities that were never engineered in,   because somewhere in internet text is the data 
to train and to be able to give it the knowledge   to do a certain kind of thing.
With robots, it seems like you   are collecting all the data manually.
So there won't be this mysterious new   capability that is somewhere in the dataset 
that you haven't purposefully collected.  Which seems like it should make it 
even harder to then have robust,   out-of-distribution capabilities.
I wonder if the trek over the next   5-10 years will be like this: Each subtask, 
you have to give it thousands of episodes.  Then it's very hard to actually automate 
much work just by doing subtasks.  If you think about what a 
barista does, what a waiter does,   what a chef does, very little of it involves 
just sitting at one station and doing stuff.  You got to move around, you got to 
restock, you got to fix the machine, et   cetera, go between the counter and 
the cashier and the machine, etc.  Will there just be this long tail of 
things and skills that you have to   keep adding episodes for manually and 
labeling and seeing how well they did?  Or is there some reason to think that it 
will progress more generally than that?  There's a subtlety here. Emergent 
capabilities don't just come from the   fact that internet data has a lot of stuff in it.
They also come from the fact that generalization,   once it reaches a certain 
level, becomes compositional.  There was a cute example that one of my students 
really liked to use in some of his presentations.  You know what the International 
Phonetic Alphabet (IPA) is?  No.
If you look in a dictionary, they'll   have the pronunciation of a word written in funny 
letters. That's basically International Phonetic   Alphabet. It's an alphabet that is pretty much 
exclusively used for writing down pronunciations   of individual words and dictionaries.
You can ask an LLM to write you a recipe   for making some meal in International Phonetic 
Alphabet, and it will do it. That's like,   holy crap. That is definitely not something that 
it has ever seen because IPA is only ever used   for writing down pronunciations of individual 
words. That's compositional generalization. It's   putting together things you've seen in new ways.
Arguably there's nothing profoundly new here   because yes, you've seen different words written 
that way, but you've figured out that now you   can compose the words in this other language the 
same way that you've composed words in English.  That's actually where the 
emergent capabilities come from.  Because of this, in principle, if we 
have a sufficient diversity of behaviors,   the model should figure out that those 
behaviors can be composed in new ways   as the situation calls for it.
We've actually seen things   even with our current models.
In the grand scheme of things,   looking back five years from now, we'll 
probably think that these are tiny in scale.  But we've already seen what I 
would call emerging capabilities.  When we were playing around with 
some of our laundry folding policies,   we actually discovered this by accident.
The robot accidentally picked up two T-shirts   out of the bin instead of one.
It starts folding the first one,   the other one gets in the way, picks up 
the other one, throws it back in the bin.  We didn't know it would do that. Holy crap. 
Then we tried to play around with it, and yep,   it does that every time. It's doing its work. 
Drop something else on the table, it just picks   it up and puts it back. Okay, that's cool. 
It starts putting things in a shopping bag.  The shopping bag tips over, it picks 
it back up, and stands it upright.  We didn't tell anybody to collect data for that.
I'm sure somebody accidentally at some point,   or maybe intentionally picked up the shopping bag.
You just have this kind of compositionality that   emerges when you do learning at scale.
That's really where all these   remarkable capabilities come from.
Now you put that together with language.  You put that together with all 
sorts of chain-of-thought reasoning,   and there's a lot of potential for the 
model to compose things in new ways.  Right. I had an example like this when 
I got a tour of the robots at your   office. It was folding shorts. I don't know 
if there was an episode like this in the   training set, but just for fun I took one 
of the shorts and turned it inside out.  Then it was able to understand that 
it first needed to get… First of all,   the grippers are just like this, two 
opposable finger and thumb-like things.  It's actually shocking how 
much you can do with just that.  But it understood that it first needed to fold 
it inside out before folding it correctly.  What's especially surprising 
about that is it seems like   this model only has one second of context.
Language models can often see the entire codebase.  They're observing hundreds of thousands of 
tokens and thinking about them before outputting.  They're observing their own chain of thought 
for thousands of tokens before making a plan   about how to code something up.
Your model is seeing one image,   what happened in the last second, and it 
vaguely knows it's supposed to fold this short.  It's seeing the image of what happened in 
the last second. I guess it works. It's   crazy that it will just see the last thing that 
happened and then keep executing on the plan.  Fold it inside out, then fold it correctly.
But it's shocking that a second of context   is enough to execute on a minute-long task. 
Yeah. I'm curious why you made that choice in   the first place and why it's possible to 
actually do tasks… If a human only had a   second of memory and had to do physical work, 
I feel like that would just be impossible.  It's not that there's something good 
about having less memory, to be clear.  Adding memory, adding longer context, all 
that stuff, adding higher resolution images,   those things will make the model better.
But the reason why it's not the most   important thing for the kind of skills 
that you saw when you visited us,   at some level, comes back to Moravec's paradox.
Moravec's paradox basically, if you want to   know one thing about robotics, that's the thing.
Moravec's paradox says that in AI the easy things   are hard and the hard things are easy.
Meaning the things that we take for   granted—like picking up objects, seeing, 
perceiving the world, all that stuff—those   are all the hard problems in AI.
The things that we find challenging,   like playing chess and doing calculus, 
actually are often the easier problems.  I think this memory stuff is actually 
Moravec’s paradox in disguise.  We think that the cognitively demanding tasks that 
we do that we find hard, that cause us to think,   "Oh man, I'm sweating. I'm working hard." Those 
are the ones that require us to keep lots of   stuff in memory, lots of stuff in our minds.
If you're solving some big math problem, if   you're having a complicated technical conversation 
on a podcast, those are things where you have to   keep all those puzzle pieces in your head.
If you're doing a well-rehearsed task—if you   are an Olympic swimmer and you're swimming 
with perfect form—and you're right there   in the zone, people even say it's "in 
the moment." It's in the moment. It's   like you've practiced it so much you've baked 
it into your neural network in your brain.  You don't have to think carefully 
about keeping all that context.  It really is just Moravec's 
paradox manifesting itself.  That doesn't mean that we don't need the memory.
It just means that if we want to match the level   of dexterity and physical proficiency that 
people have, there's other things we should   get right first and then gradually go up that 
stack into the more cognitively demanding areas,   into reasoning, into context, into 
planning, all that kind of stuff.  That stuff will be important too.
You have this trilemma. You have three different   things which all take more compute during 
inference that you want to increase at the same   time. You have the inference speed. Humans are 
processing 24 frames a second or whatever it is.  We can react to things extremely fast.
Then you have the context length.  For the kind of robot which is just cleaning 
up your house, I think it has to be aware of   things that happened minutes ago or hours 
ago and how that influences its plan   about the next task it's doing.
Then you have the model size.  At least with LLMs, we've seen that there's 
gains from increasing the amount of parameters.  I think currently you have 100 
millisecond inference speeds.  You have a second-long context and then 
the model is a couple billion parameters?  Each of these, at least two of them, 
are many orders of magnitude smaller   than what seems to be the human equivalent.
A human brain has trillions of parameters   and this has like 2 billion parameters.
Humans are processing at least as fast   as this model, actually a decent bit 
faster, and we have hours of context.  It depends on how you define human context, 
but hours of context, minutes of context.  Sometimes decades of context.
Exactly. You have to have many order-of-magnitude   improvements across all of these three 
things which seem to oppose each other.  Increasing one reduces the amount of compute you 
can dedicate towards the other one in inference.  How are we going to solve this?
That's a very big question. Let's   try to unpack this a little bit.
There's a lot going on in there.  One thing is a really 
interesting technical problem.  It's something where we'll 
see perhaps a lot of really   interesting innovation over the next few years.
It’s the question of representation for context.  You gave some of the examples, like 
if you have a home robot that's doing   something then it needs to keep track.
As a person, there are certainly some   things where you keep track of them very 
symbolically, almost in language. I have   my checklist. I'm going shopping. At least for me, 
I can literally visualize in my mind my checklist.  Pick up the yogurt, pick up 
the milk, pick up whatever.  I'm not picturing the milk shelf with the 
milk sitting there. I'm just thinking,   "milk." But then there's other things 
that are much more spatial, almost visual.  When I was trying to get to your 
studio, I was thinking, "Okay,   here's what the street looks like.
Here's what that street looks like.  Here's what I expect the doorway to look like."
Representing your context in the right form,   that captures what you really need 
to achieve your goal—and otherwise   discards all the unnecessary stuff—I 
think that's a really important thing.  We're seeing the beginnings of 
that with multimodal models.  But I think that multimodality has much 
more to it than just image plus text.  That's a place where there's a lot of 
room for really exciting innovation.  Do you mean in terms of how we represent?
How we represent both context,   both what happened in the past, and also plans or 
reasoning, as you call it in the LLM world, which   is what we would like to happen in the future or 
intermediate processing stages in solving a task.  Doing that in a variety of modalities, including 
potentially learned modalities that are suitable   for the job, is something that has enormous 
potential to overcome some of these challenges.  Interesting. Another question I have as we're 
discussing these tough trade-offs in terms of   inference is comparing it to the human brain.
The human brain is able to have hours, decades   of context while being able to act on the order 
of 10 milliseconds, while having 100 trillion   parameters or however you want to count it.
I wonder if the best way to understand what's   happening here is that human brain hardware 
is just way more advanced than the hardware   we have with GPUs, or that the algorithms for 
encoding video information are way more efficient.  Maybe it's some crazy mixture of experts 
where the active parameters are also on the   order of billions, low billions.
Or it’s some mixture of the two.  If you had to think about why we have these 
models that are, across many dimensions,   orders of magnitude less efficient compared 
to the brain, is it hardware or algorithms?  That's a really good question. I 
definitely don't know the answer to this.  I am not by any means well-versed in neuroscience.
If I had to guess and also provide an answer that   leans more on things I know, it's something 
like this. The brain is extremely parallel.   It has to be just because of the biophysics, 
but it's even more parallel than your GPU.  If you think about how a modern 
multimodal language model processes   the input, if you give it some images and 
some text, first it reads in the images,   then it reads in the text, and then proceeds 
one token at a time to generate the output.  It makes a lot more sense to me for an 
embodied system to have parallel processes.  Now mathematically you can make close 
equivalences between parallel and sequential   stuff. Transformers aren't fundamentally 
sequential. You make them sequential by   putting in position embeddings.
Transformers are fundamentally   very parallelizable things.
That's what makes them so great.  I don't think that mathematically this highly 
parallel thing—where you're doing perception   and proprioception and planning all at the 
same time—necessarily needs to look that   different from a transformer, although its 
practical implementation will be different.  You could imagine that the system will in parallel 
think about, "Okay, here's my long-term memory,   here's what I've seen a decade ago, 
here's my short-term spatial stuff,   here's my semantic stuff, here's what I'm 
seeing now, here's what I'm planning."  All of that can be implemented in a way that 
there's some very familiar attentional mechanism,   but in practice all running in parallel, 
maybe at different rates, maybe with the   more complex things running slower, the 
faster reactive stuff running faster.  If in five years we have a system 
which is as robust as a human in   terms of interacting with the world, then 
what has happened that makes it physically   possible to be able to run those models?
To have video information that is streaming   at real time, or hours of prior video 
information is somehow being encoded and   considered while decoding in a millisecond 
scale, and with many more parameters.  Is it just that Nvidia has shipped much 
better GPUs or that you guys have come up   with much better encoders and stuff?
What's happened in the five years?  There are a lot of things to this question.
Certainly there's a really   fascinating systems problem.
I'm by no means a systems expert.  I would imagine that the right architecture 
in practice, especially if you want an   affordable low-cost system, would be to 
externalize at least part of the thinking.  You could imagine in the future you'll have a 
robot where, if your Internet connection is not   very good, the robot is in a dumber reactive mode.
But if you have a good Internet connection then it   can be a little smarter. It's pretty cool. There 
is also research and algorithms stuff that can   help here, figuring out the right representations, 
concisely representing both your past observations   but also changes in observation.
Your sensory stream is extremely   temporally correlated.
The marginal information   gained from each additional observation is not 
the same as the entirety of that observation.  The image that I'm seeing now is very 
correlated to the image I saw before.  In principle, I want to represent it concisely.
I could get away with a much more   compressed representation than if I 
represent the images independently.  There's a lot that can be done on the 
algorithm side to get this right. That's   really interesting algorithms work. There's 
also a really fascinating systems problem.  To be truthful, I haven't gotten to 
the systems problem because you want   to implement the system once you know the 
shape of the machine learning solution.  But there's a lot of cool stuff to do there.
Maybe you guys just need to hire the people   who run the YouTube data centers because 
they know how to encode video information.   This raises an interesting question. 
With LLMs, theoretically you could   run your own model on this laptop or whatever.
Realistically what happens is that the largest,   most effective models are being run 
in batches of thousands and millions   of users at the same time, not locally.
Will the same thing happen in robotics   because of the inherent efficiencies of batching, 
plus the fact that we have to do this incredibly   compute-intensive inference task?
You don't want to be carrying around   $50,000 GPUs per robot or something.
You just want that to happen somewhere else.  In this robotics world, should we 
just be anticipating something where   you need connectivity everywhere?
You need robots that are super fast.  You're streaming video information back and 
forth, or at least video information one way.  Does that have interesting implications about how 
this deployment of robots will be instantiated?  I don't know. But if I were to guess, 
I would guess that we'll see both.  That we'll see low-cost systems with 
off-board inference and more reliable systems.  For example, in settings where you have 
an outdoor robot or something where you   can't rely on connectivity, those will 
be costlier and have onboard inference.  I'll say a few things from a technical standpoint 
that might contribute to understanding this.  While a real-time system obviously needs to be 
controlled in real time, often at high frequency,   the amount of thinking you need to do for 
every time step might be surprisingly low.  Again, we see this in humans and animals.
When we plan out movements, there is definitely   a real planning process that happens in the brain.
If you record from a monkey brain, you will find   neural correlates of planning.
There is something that happens   in advance of a movement.
When that movement takes place,   the shape of the movement correlates with what 
happened before the movement. That's planning.   That means that you put something in place and 
set the initial conditions of some process and   then unroll that process, and that's the movement.
That means that during that movement, you're doing   less processing and you batch it up in advance.
But you're not entirely an open loop.  It's not that you're playing back a tape recorder.
You are reacting as you go.  You're just reacting at a different level of 
abstraction, a more basic level of abstraction.  Again, this comes back to representations.
Figure out which representations are   sufficient for planning in advance and 
then unrolling, and which representations   require a tight feedback loop.
For that tight feedback loop,   what are you doing feedback on?
If I'm driving a vehicle,   maybe I'm doing feedback on the position 
of the lane marker so that I stay straight.  At a lower frequency, I sort 
of gauge where I am in traffic.  You have a couple of lectures from a few years 
back where you say that even for robotics, RL is   in many cases better than imitation learning.
But so far the models are exclusively   doing imitation learning.
I'm curious how your thinking on   this has changed. Maybe it hasn’t changed. 
But then you need to do this for the RL.  Why can't you do RL yet?
The key here is prior knowledge.  In order to effectively learn from your own 
experience, it turns out that it's really,   really important to already know 
something about what you're doing.  Otherwise it takes far too long, just like 
it takes a person, when they're a child,   a very long time to learn very basic things, to 
learn to write for the first time, for example.  Once you already have some knowledge, then 
you can learn new things very quickly.  The purpose of training the models with supervised 
learning now is to build out that foundation that   provides the prior knowledge so they can 
figure things out much more quickly later.  Again, this is not a new idea.
This is exactly what we've seen with LLMs.  LLMs start off being trained 
purely with next token prediction.  That provided an excellent starting 
point, first for all sorts of synthetic   data generation and then for RL.
It makes total sense that we would   expect basically any foundation model 
effort to follow that same trajectory.  We first build out the foundation 
essentially in a somewhat brute-force way.  The stronger that foundation gets, the 
easier it is to then make it even better   with much more accessible training.
In 10 years, will the best model for   knowledge work also be a robotics model 
or have an action expert attached to it?  The reason I ask is, so far we've seen advantages 
from using more general models for things.  Will robotics fall into this bucket?
Will we just have the model which does everything,   including physical work and knowledge work, or 
do you think they'll continue to stay separate?  I really hope that they will actually be the same. 
Obviously I'm extremely biased. I love robotics,   I think it's very fundamental to AI.
But optimistically, I hope it's actually   the other way around, that the robotics element of 
the equation will make all the other stuff better.  There are two reasons for this 
that I can tell you about.  One has to do with representations and focus.
What I said before, with video prediction   models if you just want to 
predict everything that happens,   it's very hard to figure out what's relevant.
If you have the focus that comes from trying to   do a task now that acts to structure 
how you see the world in a way that   allows you to more fruitfully utilize the other 
signals. That could be extremely powerful. The   second one is that understanding the physical 
world at a very deep, fundamental level, at a   level that goes beyond just what we can articulate 
with language, can help you solve other problems.  We experience this all the time.
When we talk about abstract concepts,   we say, "This company has a lot of momentum."
We'll use social metaphors to describe   inanimate objects. "My computer hates me."
We experience the world in a particular way   and our subjective experience shapes how 
we think about it in very profound ways.  Then we use that as a hammer to basically 
hit all sorts of other nails that are far   too abstract to handle any other way.
There might be other considerations   that are relevant to physical robots in 
terms of inference speed and model size,   et cetera, which might be different from 
the considerations for knowledge work.  Maybe it's still the same model, but 
then you can serve it in different ways.  The advantages of co-training are high enough.
I'm wondering, in five years if I'm using a   model to code for me, does it also 
know how to do robotics stuff?  Maybe the advantages of code writing on 
robotics are high enough that it's worth it.  The coding is probably the pinnacle of 
abstract knowledge work in the sense   that just by the mathematical nature of computer 
programming, it's an extremely abstract activity,   which is why people struggle with it so much.
I'm a bit confused about why simulation   doesn't work better for robots.
If I look at humans, smart humans   do a good job of, if they're intentionally 
trying to learn, noticing what about the   simulation is similar to real life and paying 
attention to that and learning from that.  If you have pilots who are learning in simulation 
or F1 drivers who are learning in simulation,   should we expect it to be the case that as robots 
get smarter they will also be able to learn more   things through simulation?
Or is this cursed and we   need real-world data forever?
This is a very subtle question.  Your example with the airplane pilot 
using simulation is really interesting.  But something to remember is that when a pilot 
is using a simulator to learn to fly an airplane,   they're extremely goal-directed.
Their goal in life is not to learn   to use a simulator.
Their goal in life   is to learn to fly the airplane.
They know there will be a test afterwards.  They know that eventually they'll be in 
charge of a few hundred passengers and   they really need to not crash that thing.
When we train models on data from multiple   different domains, the models don't know that 
they're supposed to solve a particular task.  They just see, "Hey, here's 
one thing I need to master.  Here's another thing I need to master."
Maybe a better analogy there is if you're   playing a video game where you can fly an 
airplane and then eventually someone puts   you in the cockpit of a real one.
It's not that the video game is   useless, but it's not the same thing.
If you're trying to play that video game and your   goal is to really master the video game, you're 
not going to go about it in quite the same way.  Can you do some kind of meta-RL on this?
There's this really interesting   paper you wrote in 2017.
Maybe the loss function is not how well it does at   a particular video game or particular simulation. 
I'll let you explain it. But it was about how   well being trained at different video games 
makes it better at some other downstream task.  I did a terrible job at 
explaining but can you do a better   job and try to explain what I was trying to say?
What you're trying to say is that maybe if we have   a really smart model that's doing meta-learning, 
perhaps it can figure out that its performance   on a downstream problem, a real-world problem, 
is increased by doing something in a simulator.  And then specifically make 
that the loss function, right?  That's right. But here's the thing with this.
There's a set of these ideas that are all going   to be something like, "Train to make it better 
on the real thing by leveraging something else."  The key linchpin for all of that is the ability 
to train it to be better on the real thing.  I suspect in reality we might not even 
need to do something quite so explicit.  Meta learning is emergent, 
as you pointed out before.  LLMs essentially do a kind of meta 
learning via in-context learning.  We can debate how much that's learning or not, but 
the point is that large powerful models trained   on the right objective and on real data, get 
much better at leveraging all the other stuff.  I think that's actually the key.
Coming back to your airplane pilot, the airplane   pilot is trained on a real world objective.
Their objective is to be a good airplane pilot,   to be successful, to have a good career.
All of that kind of propagates back into   the actions they take and leveraging 
all these other data sources.  So what I think is actually the 
key here to leveraging auxiliary   data sources including simulation, is to 
build the right foundation model that is   really good and has those emergent abilities.
To your point, to get really good like that,   it has to have the right objective.
Now we know how to get the right objective   out of real world data, maybe we can get it out 
of other things, but that's harder right now.  Again, we can look to the examples 
of what happened in other fields.  These days if someone trains an 
LLM for solving complex problems,   they're using lots of synthetic data.
The reason they're able to leverage that   synthetic data effectively is because they 
have this starting point that is trained on   lots of real data that gets it.
Once it gets it, then it's more   able to leverage all this other stuff.
Perhaps ironically, the key to leveraging   other data sources including simulation, 
is to get really good at using real data,   understand what's up with the world, and 
then you can fruitfully utilize that.  Once we have, in 2035 or 2030, basically this 
sci-fi world, are you optimistic about the   ability of true AGIs to build simulations in 
which they are rehearsing skills that no human   or AI has ever had a chance to practice before?
They need to practice to be astronauts because   we're building the Dyson sphere and 
they can just do that in simulation.  Or will the issue with simulation continue to 
be one regardless of how smart the models get?  Here’s what I would say. Deep 
down at a very fundamental level,   the synthetic experience that you create yourself 
doesn't allow you to learn more about the world.  It allows you to rehearse things, it 
allows you to consider counterfactuals.  But somehow information about the world 
needs to get injected into the system.  The way you pose this question 
elucidates this very nicely.  In robotics classically, 
people have often thought about   simulation as a way to inject human knowledge.
A person knows how to write down differential   equations, they can code it up and that gives 
the robot more knowledge than it had before.  But increasingly what we're learning 
from experiences in other fields,   from how the video generation stuff 
goes from synthetic data for LLMs,   is that probably the most powerful way to create 
synthetic experience is from a really good model.  The model probably knows more than a person 
does about those fine-grained details.  But then of course, where does that model get 
the knowledge? From experiencing the world. In a   sense, what you said is quite right in that a very 
powerful AI system can simulate a lot of stuff.  But also at that point it almost doesn't 
matter because, viewed as a black box,   what's going on with that system is that 
information comes in and capability comes out.  Whether the way to process that information is 
by imagining some stuff and simulating or by   some model-free method is kind of irrelevant 
in our understanding of its capabilities.  Do you have a sense of what 
the equivalent is in humans?  Whatever we're doing when 
we're daydreaming or sleeping.  I don't know if you have some sense of 
what this auxiliary thing we're doing is,   but if you had to make an ML analogy, what is it?
Certainly when you sleep your brain does stuff   that looks an awful lot like 
what it does when it's awake.  It looks an awful lot like playing 
back experience or perhaps generating   new statistically similar experience.
It's very reasonable to guess that perhaps   simulation through a learned model is part of how 
your brain figures out counterfactuals, basically.  Something that's even more fundamental than 
that is that optimal decision making at its   core, regardless of how you do it, 
requires considering counterfactuals.  You basically have to ask yourself, "If I did 
this instead of that, would it be better?"  You have to answer that question somehow.
Whether you answer that question by using a   learned simulator, or whether you answer 
that question by using a value function   or something, by using a reward 
model, in the end it's all the same.  As long as you have some mechanism for 
considering counterfactuals and figuring out   which counterfactual is better, you've got it.
I like to think about it this way   because it simplifies things.
It tells us that the key is not   necessarily to do really good simulations.
The key is to figure out how to answer   counterfactuals.
Yeah, Interesting.   Stepping into the big picture again.
The reason I'm interested in getting a concrete   understanding of when this robot economy 
will be deployed is because it's relevant   to understanding how fast AGI will proceed in the 
sense that it's obviously about the data flywheel.  But also, if you just extrapolate out the capex 
for AI by 2030, people have different estimates,   but many people have estimates in the hundreds 
of gigawatts – 100, 200, 300 gigawatts.  You can just crunch numbers on having 
100-200 gigawatts deployed by 2030.  The marginal capex per year is 
in the trillions of dollars.  It's $2-4 trillion dollars a year.
That corresponds to actual data centers you have   to build, actual chip foundries you have to build, 
actual solar panel factories you have to build.  I am very curious about whether by 2030, the big 
bottleneck is just the people to lay out the solar   panels next to the data center or assemble the 
data center, or will the robot economy be mature   enough to help significantly in that process.
That's cool. You're basically saying, how   much concrete should I buy now to build the data 
center so that by 2030 I can power all the robots.  That is a more ambitious way of thinking about it 
than has occurred to me, but it's a cool question.  The good thing, of course, is that the 
robots can help you build that stuff.  But will they be able to by that time?
There's the non-robotic stuff,   which will also mandate a lot of capex.
Then there's robot stuff where you have   to build robot factories, etc.
There will be this industrial   explosion across the whole stack.
How much will robotics be able to   speed that up or make it possible?
In principle, quite a lot. We have a   tendency sometimes to think about robots as 
mechanical people, but that's not the case.  People are people and robots are robots.
The better analogy for the robot,   it's like your car or a bulldozer.
It has much lower maintenance requirements.  You can put them into all sorts of weird places 
and they don't have to look like people at all.  You can make a robot that's 100 feet tall.
You can make a robot that's tiny.  If you have the intelligence to power 
very heterogeneous robotic systems,   you can probably do a lot better than 
just having mechanical people, in effect.  It can be a big productivity boost for real 
people and it can allow you to solve problems   that are very difficult to solve.
For example, I'm not an expert on   data centers by any means, but you could 
build your data centers in a very remote   location because the robots don't have to worry 
about whether there's a shopping center nearby.  There's the question of where the software 
will be, and then there's the question of   how many physical robots we will have.
How many of the robots you're training   in Physical Intelligence, these tabletop 
arms, are there physically in the world?  How many will there be by 2030?
These are tough questions, how many will   be needed for the intelligence explosion.
These are very tough questions. Also,   economies of scale in robotics so far 
have not functioned the same way that they   probably would in the long term.
Just to give you an example,   when I started working in robotics in 
2014, I used a very nice research robot   called a PR2 that cost $400,000 to purchase.
When I started my research lab at UC Berkeley,   I bought robot arms that were $30,000.
The robots that we are using now at Physical   Intelligence, each arm costs about $3,000.
We think they can be made   for a small fraction of that.
What is the cause of that learning rate?  There are a few things. One, of course, 
has to do with economies of scale.  Custom-built, high-end research hardware, 
of course, is going to be much more   expensive than more productionized hardware.
Then of course, there's a technological element.  As we get better at building actuated 
machines, they become cheaper. There's also   a software element. The smarter your AI 
system gets, the less you need the hardware   to satisfy certain requirements.
Traditional robots in factories   need to make motions that are highly repeatable.
Therefore it requires a degree of precision and   robustness that you don't need if 
you can use cheap visual feedback.  AI also makes robots more affordable and 
lowers the requirements on the hardware.  Interesting. Do you think the 
learning rate will continue?  Do you think it will cost hundreds of dollars 
by the end of the decade to buy mobile arms?  That is a great question for my co-founder, Adnan 
Esmail, who is probably the best person arguably   in the world to ask that question.
Certainly the drop in cost that   I've seen has surprised me year after year.
How many arms are there probably in the world?  Is it more than a million? Less than a million?
I don't know the answer to that question,   but it's also a tricky question to answer 
because not all arms are made equal.  Arguably, the robots that are assembling 
cars in a factory are just not the   right kind to think about.
The kind you want to train on.  Very few because they are not currently 
commercially deployed as factory robots.  Less than 100,000?
I don't know, but probably.  Okay. And we want billions of 
robots, at least millions of robots.  If you're just thinking about the 
industrial explosion that you need to get   this explosive AI growth, not only do you need the 
arms, but you need something that can move around.  Basically, I'm just trying to think whether 
that will be possible by the time that you   need a lot more labor to power this AI boom?
Well, economies are very good at filling   demand when there's a lot of demand.
How many iPhones were in the world in   2001? There's definitely a challenge there. 
It's something that is worth thinking about.  A particularly important question 
for researchers like myself is how   can AI affect how we think about hardware?
There are some things that are going to be   really, really important.
You probably want your   thing to not break all the time.
There are some things that are firmly   in that category of question marks.
How many fingers do we need?  You said yourself before that you were surprised 
that a robot with two fingers can do a lot.  Maybe you still want more than that, but still 
finding the bare minimum that still lets you have   good functionality, that's important.
That's in the question mark box.  There are some things that we probably don't need.
We probably don't need the robot to be super   duper precise, because we know that 
feedback can compensate for that.  My job, as I see it right now, is to figure out 
what's the minimal package we can get away with.  I really think about robots in terms 
of minimal package because I don't   think that we will have the one ultimate 
robot, the mechanical person basically.  What we will have is a bunch of things that 
good, effective robots need to satisfy.  Just like good smartphones 
need to have a touchscreen.  That's something that we all agreed on.
Then they’ll need a bunch of other stuff   that's optional, depending on the need, 
depending on the cost point, et cetera.  There will be a lot of innovation where 
once we have very capable AI systems that   can be plugged into any robot to endow it with 
some basic level of intelligence, then lots of   different people can innovate on how to get the 
robot hardware to be optimal for each niche.  In terms of manufacturers, is 
there some Nvidia of robotics?  Not right now. Maybe there will be 
someday. Maybe I'm being idealistic,   but I would really like to see a world where 
there's a lot of heterogeneity in robots.  What is the biggest bottleneck in the 
hardware today as somebody who's designing   the algorithms that run on it?
It's a tough question to answer,   mainly because things are changing so fast.
To me, the things that I spend a significant   amount of time thinking about on the hardware 
side is really more reliability and cost.  It's not that I'm that worried about cost.
It's just that cost translates to the number of   robots, which translates to the amount of data.
Being an ML person, I really like   having lots of data.
I really want to have   robots that are low cost, because then I can 
have more of them and therefore more data.  Reliability is important, more 
or less for the same reason.  It's something that we'll get more 
clarity on as things progress.  Basically, the AI systems of today are 
not pushing the hardware to the limit.  As the AI systems get better and better, 
the hardware will get pushed to the limit,   and then we'll hopefully have a 
much better answer to your question.  This is a question I've had for a lot of guests.
If you go through any layer of this AI explosion,   you find that a bunch of the actual source 
supply chain is being manufactured in China,   other than chips obviously.
You talk about data centers   and you're like, "Oh, all the wafers for solar 
panels and a bunch of the cells and modules,   et cetera, are manufactured in China."
You just go through the supply chain.  Obviously robot arms are 
being manufactured in China.  You’ll live in this world where it’s 
just incredibly valuable to ramp up   manufacturing of the hardware, because 
each robot can produce some fraction   of the value that a human worker can produce.
Not only is that true, but the value of human   workers or any worker has tremendously skyrocketed 
because we need tons of bodies to lay out the tens   of thousands of acres of solar farms and 
data centers and foundries and everything.  In this boom world, the big bottleneck there's 
just how many robots can you physically deploy?   How many can you manufacture? Because you 
guys are going to come up with the algorithms   now. We just need the hardware. This 
is a question I've asked many guests.  If you look at the part of the chain that 
you are observing, what is the reason that   China just doesn't win by default?
If they're producing all the robots   and you come up with the algorithms 
that make those robots super valuable,   why don't they just win by default?
This is a very complex question.  I'll start with the broader themes and then 
try to drill a little bit into the details.  One broader theme here is that if you want to 
have an economy where you get ahead by having   a highly educated workforce—by having people 
that have high productivity, meaning that   for each person's hour of work, lots of stuff 
gets done—automation is really, really good.  Automation is what multiplies the amount 
of productivity that each person has.  Again, it’s the same as LLM coding tools.
LLM coding tools amplify the   productivity of a software engineer.
Robots will amplify the productivity of   basically everybody that is doing work.
Now that's a final state, a desirable final state.  There's a lot of complexity in how you 
get to that state, how you make that   an appealing journey to society, how you 
navigate the geopolitical dimension of that.  All of that stuff is pretty complicated.
It requires making a number   of really good decisions.
Good decisions about investing in   a balanced robotics ecosystem, supporting both 
software innovation and hardware innovation.  I don't think any of those 
are insurmountable problems.  It just requires a degree of long-term 
vision and the right balance of investment.  What makes me really optimistic 
about this is the final state.  We can all agree that in the United States we 
would like to have a society where people are   highly productive, where we have highly 
educated people doing high-value work.  Because that end state seems to me very 
compatible with automation, with robotics,   at some level there should be a lot 
of incentive to get to that state.  Then from there we have to solve for 
all the details that will help us get   there. That's not easy. There's a lot 
of complicated decisions that need to   be made in terms of private industry, in terms of 
investment, in terms of the political dimension.  But I'm very optimistic about it because 
it seems to me that the light at the end   of the tunnel is in the right direction.
I guess there's a different question.  If the value is bottlenecked by hardware 
and you just need to produce more hardware,   what is the path by which hundreds of 
millions of robots or billions of robots   are being manufactured in the US or with allies?
I don't know how to approach that question, but   it seems like a different question than, "Well, 
what is the impact on human wages or something?"  For the specifics of how we make that happen, 
that's a very long conversation that I'm probably   not the most qualified to speak to.
But in terms of the ingredients,   the ingredient here that is important is that 
robots help with physical things, physical work.  If producing robots is itself physical 
work, then getting really good at   robotics should help with that.
It's a little circular, of course,   and as with all circular things, you have to 
bootstrap it and try to get that engine going.  But it seems like it is an easier 
problem to address than, for example,   the problem of digital devices.
Work goes into creating computers,   phones, et cetera.
But the computers and   phones don't themselves help with the work.
Right. I guess feedback loops go both ways.  They can help you or they can help 
others and it's a positive sum world.  It's not necessarily bad that they help others.
But to the extent that a lot of the things   which would go into this feedback loop—the 
sub-component, manufacturing and supply chain,   already exist in China—it seems like the 
stronger feedback loop would exist in China.   Then there's a separate discussion. 
Maybe that's fine, maybe that's good,   and maybe they'll continue exporting this to us.
But I just find it notable that whenever I talk   to guests about different things, it's 
just like, "Yeah, within a few years the   key bottleneck to every single part of 
the supply chain here will be something   that China is the 80% world supplier of."
This is why I said before that something   really important to get right here 
is a balanced robotics ecosystem.  AI is tremendously exciting, but we should 
also recognize that getting AI right is   not the only thing that we need to do.
We need to think about how to balance our   priorities, our investment, the kind 
of things that we spend our time on.  Just as an example, at Physical Intelligence 
we do take hardware very seriously.  We build a lot of our own things and we want to 
have a hardware roadmap alongside our AI roadmap.   But that's just us. For the United States, 
arguably for human civilization as a whole,   we need to think about these 
problems very holistically.  It is easy to get distracted sometimes 
when there's a lot of excitement,   a lot of progress in one area like AI.
We are tempted to lose track of other things,   including things you've said. There's a hardware 
component. There's an infrastructure component   with compute and things like that.
In general it's good to have a more   holistic view of these things.
I wish we had more holistic   conversations about that sometimes.
From the perspective of society as a whole,   how should they be thinking about the 
advances in robotics and knowledge work?  Basically society should be 
planning for full automation.  There will be a period in which people's work 
is way more valuable because there's this huge   boom in the economy where we’re building 
all these data centers and factories.  Eventually humans can do things with their 
body and we can do things with our mind.  There's not some secret third thing.
What should society be planning for?  It should be full automation of humans.
Society will also be much wealthier.  Presumably there are ways to do this such that 
everybody is much better off than they are today.  But the end state, the light at the end of the 
tunnel, is the full automation but plus super   wealthy society with some redistribution 
or whatever way to figure that out.  I don't know if you disagree 
with that characterization.  At some level that's a very 
reasonable way to look at things.  But if there's one thing that I've learned 
about technology, it's that it rarely   evolves quite the way that people expect.
Sometimes the journey is just as important   as the destination.
It's very difficult   to plan ahead for an end state.
Directionally, what you said makes a lot of sense.  I do think that it's very important for us 
collectively to think about how to structure   the world around us in a way that is amenable to 
greater and greater automation across all sectors.  But we should really think about the journey 
just as much as the destination, because   things evolve in all sorts of unpredictable ways.
We'll find automation showing up in all sorts of   places, probably not the places we expect first.
The constant here that is really important   is that education is really, really valuable.
Education is the best buffer somebody has   against the negative effects of change.
If there is one single lever that we can pull   collectively as a society, it's more education.
Is that true? Moravec's paradox is that the   things which are most beneficial from education 
for humans might be the easiest to automate   because it's really easy to educate AIs.
You can throw the textbooks that would take   you eight years of grad school 
to do at them in an afternoon.  What education gives you is flexibility.
It's less about the particular facts you   know, as it is about your ability to 
acquire skills, acquire understanding.  It has to be a good education.
Yeah. Okay, Sergey, thank you so much   for coming on the podcast. Super fascinating.
Yeah, this was intense. Tough questions.
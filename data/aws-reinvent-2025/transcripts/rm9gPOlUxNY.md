---
video_id: rm9gPOlUxNY
video_url: https://www.youtube.com/watch?v=rm9gPOlUxNY
is_generated: False
is_translatable: True
---

- This is Continuous integration and continuous delivery on AWS. Session is DVT202. If that's what you're expecting,
you're in the right place. My name is Steve Rice. I'm general manager for AWS AppConfig as well as Parameter Store. I'll be joined later by Mihai Balaci who's going to talk
about the state of CI/CD. But first I'm gonna ask you all, how many people is this
their first re:Invent? Would you mind raising your hand? This is awesome. I love seeing so many new people. How many people have
gone to two re:Invents? Three? Four? Five? I can't, oh, okay. Six? Dang, seven? Seven back there, all right, sold. Okay, anybody above seven? Okay, I can't see if there's anybody. These lights are a little bright, but thank you all for coming. re:Invent is one of my
favorite times of the year. I apologize that it's right
after US Thanksgiving. If you're American, it's
a little bit challenging to come here right after
you left your family. I actually had a flight that
arrived here late last night. I was here three in the morning my time, so I'm fully caffeinated now, but didn't sleep much last night. But hopefully now that you're here, you're fully engaged and
you're here to learn. That's one of the key
things about re:Invent is that you're going to learn a lot. You're gonna be overwhelmed probably. I hope you're taking some notes. The good news is a lot of
these sessions are recorded and you'll be able to watch
some of them later on YouTube or some of the streaming
things that are out there. The other thing that we
really want you to do at re:Invent is meet each other and want you to be aggressively friendly to those that are around
you so that you can network. And again, it's really cool. I work at AWS, obviously. It's really cool when we see our customers all talking to each other
and not sitting there talking to an AWS employee. So I hope that happens over the next week. Okay, now back to this. We are gonna be talking about CI/CD. I'm gonna go way back in time. You can see I have gray hair and I've been doing software for 25 years. And I remember back in the day when I first was building software, I worked for a company called AOL and we would release a piece
of software once a year on a CD and I was the engineering
lead for AOL 7.0. So what that meant was that I had to go and talk to about 200 different engineers and coordinate to make
sure that we were ready to do our build once every two weeks. And I went and I would reach
out on Instant Messenger and say, "Are you ready yet?" "Oh, I'm all ready, yep." And then on build day,
which was on Wednesday, I would merge all the
code and I'd do a build and it would never work. So then I'd figure out
where the failures are. I'd go talk to probably
50 of those 200 engineers and I'd have to go back
and ask them to make a fix. And we use Visual Source
Safe, if you remember that. Again, I can see some
gray-haired people out there. And it was a very strenuous process. We were supposed to build on Wednesdays. Usually we'd end up building on Friday or the following Monday because there's so many build failures. Then we moved to a build system
that actually used branches and that was a huge innovation,
a huge innovation in CI/CD. Actually, CI/CD didn't exist
yet, but in source management. And we would be able to
develop on our own branch and then we'd merge in. And the auto-merges were amazing. That was something that really
moved us forward faster. Looking back, those were
sort of the dinosaur days. We were not making as much
progress as we do today, but that branching was a big innovation. Then we moved to CI/CD. And again, I had left AOL a while ago, but we moved to CI/CD where
all this was automated. So I'd commit some code and
then it would be out there through a process out to
production after some testing. And that was a revolutionary thing. Today, we're gonna talk
about looking forward and some new innovations in CI/CD. I think that AI will be a big thing that you hear a lot at re:Invent, but I think that there's
areas where we've seen tremendous success and
tremendous opportunity for development with AI. And one is code writing, obviously. It's pretty amazing what AI agents can do. The other is in the CI/CD space. That's gonna be transformed over the next three to five years and the way we do things today
is gonna be very different than the way we're gonna do things by the end of the next year and the year after that, et cetera. So I'm gonna dive into a couple of things. Our agenda today, talked a little bit about the state of where
things are with CI/CD. And Mihai's gonna talk to you about how to deploy to AWS using agents. And then sort of a workflow of that. Previewing your app, going
live, troubleshooting. I'm gonna come back later and talk about something called continuous configuration and feature flagging, and then we'll wrap up with key takeaways. We're not gonna do questions in the room. We are going to do
questions outside the room. So we're gonna try to end
with about 10 minutes left so that you all can ask us questions and/or get to your next session. This slide shows how
AWS releases software. If you didn't know, all of our
tools that we have externally are either the exact same or very similar to the tools we use internally. And I just want you to know, sir, this is our mindset of how
we release things at Amazon. I always say we develop very quickly and release very slowly. There's sort of three pillars to every release mechanism that we use. One is we release gradually. And you can see here
we have several waves. If you look in kind of
the right-hand side, wave one, wave two, wave N. We release things very
slowly and gradually. That helps us limit the
blast radius of changes. The second thing that we do is we always have automatic
rollback configured. A lot of tools will have
an automatic rollback, but if an alarm goes off
during the deployment of new code or new configuration, we're gonna have auto-rollback. It's sort of like having
auto-braking in a car. Today, almost all cars have some sort of crash
collision detection. I personally wouldn't drive a car if it didn't have that now. It's really nice. It just automatically rolls back if something strange is detected. And then the third thing we do is always sort of
validation along the way. You see that we do things
like integration tests. Sometimes with configuration data, we might validate that there's no typos because, unfortunately,
we've seen a lot of outages caused by typos in configuration,
including at Amazon. Those three pillars are
sort of reflected here. Again, going from left to
right, source, build, package. Then we have a gamma thing. It sits there, it bakes, and then we put in the
first wave, second wave. For Amazon, as you probably
know, we have over 30 regions, and we use those partitions as waves. So the first wave is
a small region for us. The second wave might be two regions. The third might be a bigger region. And most of the time, whatever
we change in a small region, if it works okay, it's gonna
work in the other regions. But there are times when
we will discover something only at scale, only at US
East 1, the problem occurs, and it was fine in the other regions. But again, for you all, I
would recommend thinking about how can you partition
your releases in a way that allows you to release gradually and be able to test it,
let it bake a little bit. That is some culture
changing you need to do with your marketing teams. Marketing would love it if you could just release it everywhere all at once. But again, it makes a
much better experience if you're releasing something, and to 1% of your customers, 10%, then maybe if something goes wrong, only 10% see that problem
and it gets rolled back. So you gotta work with
marketing and other teams about doing gradual releases. Okay, so at AWS, we have
a full set of tools. We also know that a lot of companies have been around for a while and been using other tools
as they're moving to AWS. So we built these tools in a way so that they can be mixed and matched. You don't have to use all the tools. We have a lot of customers
using Jenkins, for example, and that fits into this
suite of tools as well. We expect that to be there. You can see on the left-hand side, Kiro, that's a relatively new offering. It's using AI. I'm gonna ask, has anybody
used Kiro in the room yet? Okay, great. It's sort of a spec-driven
development thing. I've been super impressed with it, and I promise it's not
just 'cause I work at AWS. It's a really impressive tool for sort of getting off the
ground, starting a new project. It's really engaging. And then we're gonna be
moving across the way here and talk about some, Mihai's gonna talk about
some of these other tools. We're not gonna talk about,
on the right-hand side, a lot of the monitoring tools. That is an important
part of your CI/CD plan. And I told you, the second to the right, AWS Africa, I'm gonna talk a little bit about that at the end. Okay, I am going to hand it over to Mihai. To talk about some of
the very exciting changes that are happening, both
in the industry and at AWS. - Thank you, Steve. Good morning, everybody. I hope you're doing good so far. You know what I like
about this slide the most is the fact that we have so many tools and we have so many stages that
we developed over the years. And this makes it very, very interesting because if we look at how many
stages we have these days, maturing your software
development life cycle is a challenging journey by now. Having sustainable CI/CD maturity both requires and reinforces
the SDLC maturity. Do we have vibe coders in the
room today, in the audience? We have one, good. Let's imagine you have
that brilliant idea, the billion dollar idea, and you're about to start right now. Your SDLC maturity would
be very low at this point. Your focus will be entirely
on speed of implementation and you will have probably
no test, not enough security, and not so many platform knowledge. But the more you're evolving
into a growing startup, your maturity, your SDLC maturity level gets to a medium stage. But your focus also changes
from speed to collaboration. The more you go and grow into a scale-up, your focus changes again, and your SDLC maturity
becomes even higher than that. You start having all the
steps covered properly in the SDLC pipeline, but
your focus changes as well and moves towards scaling the technology. On the last stage of
your growing business, you will end up becoming an enterprise and you will have all the
stages pretty well-defined and fully covered, but
your focus changes again. You will start looking more into security, auditing, and how to scale the governance. Organizations encounter
various pain points across their maturity
journey of their SCICD. In the last five, 10
years, if we think about how fast those tools have been evolving, this evolution makes it almost impossible for teams and organizations
to stay current. So teams struggle to balance
between adopting new practices versus maintaining stability. They also struggle when
standardization is pushed over, not one single team, but multiple teams. This is always super time-consuming. Security vulnerabilities
can be also introduced at any point at the pipeline stage, and by now you need to have
continuous security scanning and compliance checks in place, and you need to do all
this by not slowing down the delivery process. Pipeline performance,
we also learn over time that pipeline performance will degrade with increased code base
and the number of teams that are using that pipeline. A pipeline that once
used to be very efficient can over time become a bottleneck, lead to slow delivery times,
and become even more expensive. Pipeline failures can be
introduced at any stage, but they can also be very
difficult to diagnose and even reproduce. Complex integration points create multiple failure possibilities. And as we also learn over time, the infrastructure cost
for CI/CD grows with scale. In software development, the need for seamless collaboration, continuous integration, and
delivery is paramount today. Having multiple complex possibilities to orchestrate your CI/CD
pipelines is extremely valuable, but what we have observed over time is that orchestrating a deployment on AWS can become very complex. At Amazon, we believe
that in this new world of vibe coding and AI-driven innovation, all this complexity should be triggered by simple interactions. Let's just imagine what if a deployment was as simple as describing what you want. What I'm gonna show you today is how to orchestrate a deployment on AWS using AI and the AWS MCP server. We will use best practices, like infrastructure as code through CDK, to keep our environment consistency, and I'm gonna show you how
to bring your brilliant idea to production in a matter of minutes. There are so many innovations
happening right now in the AI space, and MCP is one of them. Does anyone know about
MCP in the audience? One, two, three, all right. MCP stands for Model Context Protocol, and is a way to enhance
the model's knowledge and capabilities, and I like to think that deploy using the AWS MCP should be your first DevOps hire, especially if you are
in the first quadrant, the zero to one quadrant
that I showed you before. Do we have any Joe in the audience? Congratulations, Joe,
looks like you're about to release a new company. Joe is a vibe coder, he just
created his first project on a vibe coding platform,
and he wants to share a link of that application to his family, friends, and stakeholders. Joe heard about AWS
releasing the MCP server, and he just wants to try it out. Let's look at his journey
as he creates this link where his application can be accessed. First, Joe will use his ID of choice, in our case, we will show you
Kiro, it's our ID of choice. He will install and
configure the AWS MCP server, and Joe will simply start
his flow, his preview flow, by asking Kiro what he wants. To deploy this, we will use agent SOPs. These are standard operating
procedures for agents, and their SOPs are usable workflows written in markdown for agents to follow. These SOPs are all part
of the AWS MCP server. At the end of this flow, when
these checks are completed, Joe will end up having his
link, a CloudFront link, where his application will be running. And let me show you how this works. All right, Joe goes to
his GitHub repository where his lovable application was saved. Joe is using a standard
lovable app this time. I'm gonna demo you a standard lovable app. This has a React front-end,
has authentication mechanism, a super-based database, and
a Lambda serverless function. The first thing that Joe will do is to test his application locally. As we can see here, localhost 8080, the application is loading. Let's see also if the functionality is what we expect it to be. Joe is placing a new order. Okay, it works. The checks are in place. Now, Kiro has native support for MCP. The next step in this
flow would be for Joe to configure and set
up the AWS MCP server. This seems to work as well. Now, Joe is checking his AWS credentials. All works well. And now, Joe will ask
Kiro to deploy his app. I'm gonna pause right now. Oh, he's not pausing, no. All right, so Kiro will load an agent SOP which will follow a series
of steps to deploy this app. Once Kiro scans the application code, we'll understand the type of application and we'll generate the type of components that will be further on
deployed using CDK to AWS. As you can see in the interaction, Joe constantly receives
the output from AWS into a readable format in the chat. So those actions can be performed once by asking Kiro to do it, copy pasting the commands in the CLI or going to the AWS console, logging in the AWS console
by using those links and perform the actions. Now, we have the application live. We have a CloudFront link. And let's see if the order that we previously created is still there and check again the
functionality of the application. Joe is placing another order. Looks like we have a technical issue here. As you can see in the AWS console, we have two resources created. We have a CloudFormation stack for the API and another stack for
the front-end component. In the IDE as well,
the model has generated the infrastructure's code
files and the lambda function. There are two new markdown
files that Kiro will create guided by the SOP. One is the agents.md. This is the file that will allow the model to work more effectively
with Joe's application after scanning that code. And the second one is the skills. We will see that now we
have four identified skills mapping the application components that have been discovered by the model when scanning on the third stage. Now for this flow, on AWS, we
are using CloudFront AWS S3, an API gateway, and we are translating the serverless function from
lovable into a lambda function. Things have progressed. Joe is very happy and he's very confident that he wants to go live on
production with his application. He wants to take full
advantage of best practices without putting too much effort
into setting them himself. And he's proceeding. In order to deploy to production,
Joe will go back to Kiro and tell his AI chatbot
that he wants to deploy the application to production. The model will get the relevant details like getting the GitHub token, identify the missing
components in this case, and it will call the right
tools under the AWS MCP server and will start creating the
deploy for the pipeline. Joe is having a great time. The application is live on production. It works, customers and
friends are using it, but he's also receiving a
lot of new feature requests. He's finishing working
on a feature request. He's pushing a commit and it fails. Before having the AWS
MCP and before having Vibe coding in IDE, Joe
was supposed to go back to the AWS console, log
in, identify the pipeline, inspect the logs, inspect his code base, and then troubleshoot the pipeline errors. This time, with all
these new tools in place, his troubleshooting
flow would be as simple as asking Kiro to fix the problem. Joe continues his chat with Kiro, and he will ask the model very soon to deploy the application. The model is now identifying
the type of components that the CI/CD pipeline will require, and because we're using best practices, the model is also going to suggest two stages for this pipeline. And as you can see, there is one component that has been identified and generated. In order to connect
CodePipeline with the customer, in this case, Joe's
repository, GitHub repository, we need a CodeConnection
instance to be created. The model now is generating
the pipeline stack, and this pipeline stack, once created, will be deployed using CDK. Joe is asked to authorize this deployment. The model is performing a CDK bootstrap, which will start building
the components on AWS. By now, Joe should have a pipeline created with multiple stages. Every time a component is created, the model will retrieve the link to access it in the AWS console. There is no one action that
Joe needs to do right now, is to activate the AWS
CodeConnections instance to connect CodePipeline with GitHub. And by following this link,
he will authorize GitHub now. We identify the connection, and the connection will be enabled. Next, Joe will need to fill in the secrets for both dev and prod environment. The pipeline is now created,
and is running all the tests. We can also see that in CodeBuild, we have multiple projects created according to the number of
stages we have in the pipeline. The pipeline is running now all the tests, builds the backend and
the frontend components, and then first deploys
the dev environment, then the production environment. And when all this is completed, the IDE, Kiro will present Joe the links to access all these components. And let's see if the
application works now. This has been successful in the IDE. Joe has both links to dev and prod. And as I said before, Joe is
taking in new feature request, and he's working on delivering new capabilities
for his application. But unfortunately, the
pipeline gets an error in the build stage for the frontend. The troubleshooting session in this case would be as simple as going back to Kiro, going back to the IDE, and
ask the agent to troubleshoot. And the agent will do two things. Will read the agents.md file,
and the deployment.md file, to understand, one, how this application has been deployed before, and second, to get all
the relevant information about the code base after
the scanning session, to understand what type of
application he's dealing with. Then, third, we'll call the
MCP, which we'll call AWS APIs. In this case, we will
call the CodePipeline APIs to understand the status of the pipeline. And because Kiro has access
to the entire code base, it will easily be to identify
where the problem is, what files are affected by
the change, and fix them. And as previously instructed, Kiro is allowed to do
git push and git commit. The moment a git commit is done, then the pipeline being
a self-mutating pipeline would automatically restart
and rebuild the changes. And I think we have a
successful deployment by now. For this stage, for the production stage, on AWS, in terms of CI/CD components, we're using CodePipeline, we're using CodeBuild and CloudFormation. As well, we are creating
a code connection instance that can connect your
repository of choice. In this case, it's GitHub, but you can use it with
GitLab or Bitbucket as well with CodePipeline. As you can see, with the power of AI, we can optimize time-consuming tasks like setting up a pipeline or perform a multi-stage deployment. What tasks that once required
hours or days of configuration you can do now in a couple of minutes. By using the AWS MCP server, you get out-of-the-box
infrastructural code with best practices. You run all the necessary
testing steps and code scanning and pipeline notifications. A few ideas for the future, we are thinking of supporting
more complex applications like full-stack applications. We will propose ways to
speed up slow pipelines and we will use smart scaling based on historical deployment patterns. We are also looking into agents constantly and continuously monitoring your system that can detect anomalies and
propose corrective actions and those actions will not
require a manual intervention. We're also looking at
AI-generated pipeline templates based on the type of application that will include the best practices for the type of application you will have. Deploy with AWS MCP has revolutionized our deployment process. With just a few prompts, we have a fully functional,
secure, and scalable CI/CD pipeline that
deploys directly on AWS. And why I'm so excited about it is because every minute we
spend on configuring CI/CD is a minute we don't spend on innovation. We are giving developers this time back. I'm gonna ask Steve to come on stage and continue with some more
time-consuming actions. - Great.
- And examples. Thank you. Hopefully you saw some new things there that you haven't seen before. Again, we'll be happy to talk to you after about how you may apply that when you go back to your jobs next week. I'm gonna switch gears a little bit and talk about something
called continuous configuration and using feature flags. How many people in the room
are using feature flags today? Okay, good amount, great. Feature flagging is sort of
the secret weapon, I think, about moving fast and getting
some of that time back that Mihai was talking about. And I'm gonna talk just at a high level about how we use it at AWS. We did not invent feature
flagging, but we use it at scale. And some of the benefits for those that might wanna fine-tune
how they're using it or maybe introduce it into
their set of tools for CI/CD. So again, you should think
about what happens after CI/CD. So you go ahead and you've
developed your software, you've run it through your pipeline, and it goes to production. Depending on how complex things are, that might take 15 minutes,
it might take a couple hours, it might take a couple days. I told you at AWS, it's
actually weeks of time that we roll out our changes
across all of our regions. I'm gonna zoom in on this side here that's in the box, the release part. So if you have a change
that you want to make and you don't wanna go
through all of CI/CD, you can use something like AWS AppConfig or there are other feature
flagging solutions out there that are great to tweak the behavior of software on production so you're not having to go
through that 15 minutes. I'll give you an example. Let's say you have something where you have a bad actor on your system and you wanna block that bad actor. If you have your
configuration of allow lists or block lists embedded with your code and you wanna make a change and you're not using feature flags, what's gonna happen, you're
gonna update your list of your block list to
prevent that bad actor from doing things. You're gonna send it through CI/CD and that could take,
as I said, 15 minutes, couple hours or even days and you wanna be able to react
much more quickly than that. So what you're gonna have
is an application out there that is dynamically fetching and reading configuration
data on production and it's tweaking the
behavior of that software while it's on production without going and changing any code. So this concept of
continuous configuration, it allows you to do a
few different things. When people hear feature flags, they often think of I'm
releasing a new feature. That is a very common use case and we call that a release flag. So the way you do that
is you have your code. Remember earlier I was talking about these long-lived branches. You don't have long-lived
branches anymore. You have your code on the trunk but the access to that
code or that feature is controlled by a small
configuration Boolean. If feature enabled, let
people use the new code. If feature not enabled, don't
let them use the new code and kinda hide the code. This allows your software engineers to develop something and
push it to production even if it's not all the way done, nobody can access it
'cause the feature flag is off in that state. They can continue to develop
it over weeks or months, however long it takes
to develop that feature and then you can turn on that feature and you turn it on for
a small set of users. It might just be for a
couple developers at first. Then it might be for all internals and then it might be for
10% of users, 20%, et cetera and you release it slowly over time. So feature flags and
continuous configuration allows you to turn on features slowly. It also allows you to turn off features. This is a really powerful thing. It's a kill switch. Let's say something at
20% you're realizing this thing is killing our
CPU, we gotta turn it off. You don't wanna have to go
back and change all your code and then redeploy out. Instead, you can just
turn off that feature. Of course, you can roll
back code more quickly but what's really cool about
continuous configuration and feature flags, let's
say you have a push, a big push and there's 10 features in it and it's going through and
you're releasing it slowly and there's a problem with
one of those 10 things. Instead of rolling everything back and rolling back all 10 features, you can have a feature flag
just turn off the one feature that's not working so well and then you can fix it
and move forward that way. Another use case of feature flagging are what we call operational flags. I'm gonna do a demo a little bit later of an example of an operational flag. The allow list or the block list might be something like that. You also might wanna do things like limit the number of background processes. We used to do that at a
company I worked at before. During peak times, we actually turned off non-essential things so that CPU would stay at a manageable rate and then once things sort
of settled back down, we would turn on those features again. And then again, this idea of just limiting the impact of a change. I think you all know
most outages are caused by a software change of some sort and so you wanna always make
sure you're releasing things in a way that limits the
blast radius of those things. And again, with feature
flags, you're doing all this without changing any of your code. You're just changing
the configuration data. You make that change,
you push that change out of the configuration data
and your application's dynamically reading that change and within seconds, it'll update itself. So, some benefits here. No long-lived branches. Again, when I was getting
back, at least in my career, branch merges can slow you down. We've had customers that say
that they can only release once every month because
they have a very long process to resolve merge conflicts. So with feature flags, you're developing what's called trunk-based development. It's part of the
well-architected framework if you wanna look that up. And you are just deploying that capability behind a feature flag. You're really separating the
idea of a feature release from a code deployment. That's tremendously powerful. You have control about
when the code goes out. You're not waiting and
trying to time a release with something that's happening on stage. For AppConfig, which is the
feature flagging solution that almost every AWS service uses, this is a really big week for us. As we're launching all of
these new features on AWS for customers this week,
these features have actually been out there for a couple weeks. The code has been out there,
but they've been all hidden by feature flags, and
they've been turned on just for a couple users. And this week, a lot of feature
flags are getting turned on. And I already talked a little
bit about this fast rollback. Speed really matters, and so
the idea of I want to be able to roll back the change,
and just that one change, very quickly, feature
flags allow you to do that. This will result in, allow
you to respond to problems on production much faster. Your MTTRs will really
decrease, which is fantastic. You'll also be able to
validate in production. If you have a QA group, and
they have QA environments, and this always happens,
well, it didn't fail in QA, but it failed in production. What you're doing with the feature flag is you're allowing access
to test that new capability just to maybe QA accounts,
or internal accounts, on production, so you can really validate with whatever the data texture is on production that you have. Some people will use feature
flags for A/B testing. I always say this is a
way to sort of get rid of the loudest voice in the room, or the most senior voice in the room. People say, "I really
think that blue button "is gonna perform much better
than that green button, "so we're gonna have a blue button." Well, with a feature flag, you can actually split your traffic, and have 10% have blue,
and another 10% have green, and really look at the real world data over the course of a couple weeks, and see what does perform better rather than somebody's opinion. And again, you'll see some increases in your software release frequency, which is critical in moving fast. I think you all have heard
many quotes from Werner. I know he's doing a keynote later. The famous one he always says is, "Everything fails all the time," and design with this in mind. This is another quote
from a blog post he did around continuous configuration, and I'm not gonna read it exactly, but having this capability
is a secret weapon to be able to tune your
software on production. And I like this second paragraph here. "In the future, we'll be
able to respond to events "before they've even happened." This is a promise of AI agents
that are gonna go out there, they're going to be able
to test on production, or theorize this is not right, and it can actually address the thing with just a very small
configuration change. So I'm gonna do a quick demo here. The demo is going to show you
the use of a feature flag. The use case is an operational flag. It's going to toggle the
verbosity of your logging. So when there's something
critical going on in production, you actually might wanna
toggle from info to debug. You don't wanna do that
kind of thing in your code. You don't wanna have to, as I said before, I don't wanna make that
change in the code, push it through my CACD pipelines. I wanna be able to respond more quickly. There's some suspicious activity
happening on production. I wanna do that very quickly. A feature flag's a good use for that. What I'm showing you here is
the console for AWS AppConfig. Again, this is a capability that some other feature
flagging services have as well. An AppConfig has a couple
different types of configuration. We have something called a feature flag. We also have open-ended,
free-form configuration. Here I'm setting up what's
called a configuration profile. It's just a collection of flags. There are times when you wanna actually group multiple flags together and deploy them as a
single deployable unit, so AppConfig allows you
to group these things. I'm gonna create a flag that is logging verbosity essentially and I'm gonna have a friendly name. I'm going to have how I
reference it in the code, which is listed there. One problem with feature flags that we hear a lot from customers or that we see internally too is this idea of feature flag clutter. You might have flags littered
all throughout your code that nobody even knows
what they do anymore. They were used two years ago and you're afraid to remove 'em. So AppConfig actually has something where you can designate a
flag to be sort of short-term. Here I'm turning on the
flag to be on so it's active and then I'm gonna set up a
value of the logging verbosity. So here I'm gonna again create the key. I'm going to set a value as,
I think I said info to debug, so I'm setting up it's
gonna be a type string and then I'm gonna make
sure that it is info. That's sort of the normal state. Okay. I'm gonna go ahead and save this and then what I'll do here
is actually set up the flag and I'm going to, first you save it and
then we think of flags and configuration data just like code. You actually deploy the flag. So again, some solutions out
there might have something where you just update
a record in a database that's there immediately for everybody. That way you're not getting the benefit of a slow deployment and auto-rollback. So here I'm doing a deployment. I'm gonna deploy that
configuration change out to production and then again
my application is reading it. It's actively saying,
oh, logging verbosity should be info, should be info. All right, I'm gonna jump
ahead very quickly here and set up, I think in the
demo there's a CloudWatch alarm and again you could do
this with other solutions like Datadog, New Relic, et cetera and I'm gonna be monitoring
for suspicious activity. An example of that
might be something like, somebody's, we call the
API to list IAM roles. That is a normal cycle
that goes through the week but if something happens
where that spikes up, that sounds suspicious,
something weird is going on and that's a use case where you might want to turn on the verbosity to debug so you get a lot more information about when that's going on. So this is just a sample alarm. It goes through the normal
patterns here throughout the day and I set a threshold. It's really doing anomaly detection that says this is fine the number of times that this API is called. I've pre-configured here with an action. So again, CloudWatch allows you to do this and other APM solutions will
allow you to set an action when alarm goes off besides just an alarm. You can actually set up an action. In this case, I've just
decided to create a lambda that's gonna go ahead and
toggle that verbosity flag inside of AppConfig. So that's the action that gets triggered when the alarm goes off. And then again, I have the
ability to sort of notify because I certainly wanna
know when this is going on and in this case, there's other solutions that you can use, SMS, SQS, et cetera, for those kind of
notifications or event bridge. I'm gonna jump ahead here. I had something already pre-configured where the alarms did go off. If you see those two or
three peaks that said, hey, this is an anomaly,
something strange is here and that went ahead and
you see on the green and red bar on the bottom that says something strange happened here. I'm gonna flip the feature
flag from info to debug without anybody having to do anything. Again, part of this idea is automate some of your operations here. So if you go back into AppConfig here, you can take a look and
the value of the flag is now set to debug because the
alarm triggered that action. Okay, again, to recap
what I just showed you, you can set up a feature flag, an operations flag in this case. Pretty easy to do inside of AppConfig. It's very flexible. You can set it to be strings
or numbers or whatever and then use that configuration
in your application and you can even automate the
flipping of the feature flag. Okay, bring it home now. A couple key takeaways
from what you saw today. So really, I said at the
beginning of the talk that things are changing very quickly and I hope you're here
to learn some new things, not just to see what happened last year, but instead what's gonna be
happening this year and beyond. Mihai is developing some
very cool capabilities to simplify the CI/CD process. MCP really does allow teams to move faster and again, probably the most
important resource you have in your company is time. People is important too,
but time is critical. So any tools or any
technology that allows you to move faster is gonna be critical and then at the end, I
would highly recommend looking at feature flags
and continuous configuration to allow you to respond to
issues on production faster and allow your teams to release
software more frequently. So I think that's my last slide. So a couple thank yous here. One, thank you for sitting through this. Hopefully you learned some takeaways and you're gonna go and action some things starting next week, but
thank you all very much and enjoy the rest of your re:Invent. - Thank you, everybody. (audience applauding)
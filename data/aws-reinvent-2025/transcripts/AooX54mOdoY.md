---
video_id: AooX54mOdoY
video_url: https://www.youtube.com/watch?v=AooX54mOdoY
title: AWS re:Invent 2025 - Build AI Agents with Island: Customer Story Featuring Amazon (AIM125)
author: AWS Events
published_date: 2025-12-02
length_minutes: 14.08
views: 3459
description: "Discover how Amazon is building production-ready AI agents with Island and Amazon Bedrock—solving the security, governance, and deployment challenges that generally stop enterprises from going live. Join this lightning talk with Adam Hoyos-Marré, Sr. PMT at Amazon, and Island to see real use cases, real results. This presentation is brought to you by Island, an AWS Partner.  Learn more: AWS re:Invent: https://go.aws/reinforce. More AWS events: https://go.aws/3kss9CP   Subscribe: More AWS videos:..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
---

- Hey, everybody. Thanks
for joining today. This is a presentation
from a company I'm with called Island, and I
can't wait to show you. This is a very game changing technology. We're doing some really great stuff with something called
the Enterprise Browser. And if you've never heard of what that is, you're gonna learn a bit about it. You're also gonna understand kind of how we helped
Amazon on the .com side, do some really revolutionary
things, specifically with AI. And unfortunately, my co-presenter, Adam, could not make it today. So it's just gonna be me
as we go through this. And we will have some
time for some questions if anybody would like to have, you know, understand a little bit
more about what this is. Obviously, our booth is back there, but we're gonna have a roaming
mic as well for questions, and there will be time
for questions as well. So, what is the big deal? What is the challenge here today? Well, the challenge is that
we have these AI agents that can do a lot of stuff, but we need to make sure
it's governed in a good way. And so today, you know,
we are thinking about the data governance that
goes along with that. It's nothing, you know. You can do basically whatever you want. The data, the sensitive
data goes right in. There's really not a lot
of governance to that. Data comes back out. And then we start talking
about agentic AI, right? So when it's doing things. And it's really nice when it does things for you from a personal
consumer type way, right? Maybe you give it your, I don't
know, your OpenTable login and it does a reservation, that's cute. But then when we bring
that into the business, we need different controls. We need different governance around it. So, what we're gonna talk about today is that control in that security and making sure it's reliable and some use cases that Amazon found that really helped them
drive some true value and some cost savings
within their enterprise. So, first, if you haven't heard
about what this category is, it's probably the most exciting
thing I've seen in tech for a long time. I've been in tech for a long time. This is super exciting. I've been with the company for five years. We started about five years ago. But in order to bring in data and think about when your data gets, you know, brought to you. It's brought in usually
through a web browser, some sort of an interface. And this is where it gets decrypted. And today it happens in a consumer browser that you use, right? So, Chrome and Edge and others, and that's where that
thing called SSL kicks in and it does the big
two prime numbers thing and magically brings you your data. And so, you know, five years ago, or about four years ago, rather, we launched the Enterprise Browser and now we have controls over that. So, this brought us data
protection controls. It brought us delivery controls. It brought us things we could
never do before, you know, without trying to break open
SSL and inspect the wire and see what the data
was doing inside there. That's getting harder
to do as you guys know. So, when we brought this
to market, you know, we put all the controls that are needed to also gain network access. So, you think about this as
really not just a browser, but really an enterprise workspace that gets you access to the
data that you need to get to and governs and controls the data as it goes in and out of the organization. So, that's kind of the
basis of what we've done. And since we have brought
this to market, you know, we have some of the world's
largest banks, you know. I think we have most all
of them at this point, at least in the top 10. We have some of the largest
travel companies in the world, a lot of adoption in
healthcare and BPOs, right? Because that's where the data leaks out. This is, unfortunately, this is where data, the
operators can, you know, potentially accidentally leak data or intentionally, deliberately leak data. And so we have, you know,
some fantastic customers that have proven that this
technology, you know, is real. They've invested with us and obviously they're big
companies that we have working with all around the world. So, now, we have AI, and
this is kind of where we are. You guys are probably gonna be flooded with all kinds of stuff
around AI today and tomorrow and for the rest of the week. And it was cool. It's
super cool technology. And we started with the
chat bots, you know, then we got into, thanks
to ChatGPT and others, and then Anthropic created the protocol. So, we can do our modeling protocols. We had connections we brought
in those AI agents, right? We're starting to also see
consumer-based, you know, AI browsers hit the market as well. So, those are really
focused on the consumer. So, the challenge though is what do we do with trusting the data? We need to make sure it's useful so that builders and developers
can access backend data. But they need to have
governed access to the apps. They need to have governed
access to the data. And it all needs to be audited
in a secure and safe way. And what I mean, audited,
I mean, we need to see, you know, what do they did? What did they do? What did they click on? What data did they go to?
Where did they move the data? Did they move it from this
system to a different system? And unfortunately, in
the world of AI agents, when that access is granted, it doesn't know much about
the role of the user. And so, you know, you might
have somebody that has access to, you know, the HR system
and they could query that. They could say, "Hey, what's the CEO's social security number?" And of course it's got
access to that data. It could deliver that data, but the context of the
role was missing, right? And so that's when it
starts to get complicated. And the one thing between
you and those roles is today an Enterprise Browser. It's today something that
governs that activity and governs your access
to what they can get to. Passwords. A good example
of this are passwords. So, yes, like I mentioned before, I don't mind giving, you know, somebody my OpenTable account. That's a password. Maybe I
don't give them my bank account. I certainly don't give them the keys to the corporate accounts, right? But that's where we are today. We need those credentials in
order for AI agents to work. So, how do we do this without giving those credentials to AI? And the answer is the Enterprise Browser. That's the way to do it because that's where it can be injected. That's where data can make sure
it's never exposed visually. It's never exposed on the wire.
It could be sent securely. That's a big leg up for
everything we need this to do. This is the future. When we start talking
about these agentic AI and you start seeing demonstrations and, you know, future plans for this, this is where the rubber meets the road. It has to be done in the browser. And we've already built this
to create that technology and enable that in a way
that's safe and secure. So of course, you know, we
need to have collaboration and this is a lot different
than the consumer AI agents. Again, as I mentioned
before, these are useful. These are great. These are great for the
individual, not for the role within the corporation, right? So when we think about the
enterprise grade requirements that we have, this is where
we need to step it up. We need to say, "What role
is that user responsible for? What do they do within the company?" You know, "Can they have
access to that data?" So, that's where those
Enterprise AI agents really come into play. And so, today, you know, we are talking about the Island AI agents as something that we have introduced. This lets teams create, share, run secure, reliable agents in the browser. And that's the place where
you need them, right? So, this is where we can
control the data protection. This is where we can automate
work across the businesses. We can keep the data protected. So, this is agentic AI
in an Enterprise Browser. Today we're calling it AI agents. And just to show you kind
of how we've built this. You know, there is a trust layer and some of these are
components within Island. So, the Island components
of private access, getting you to those network
resources already built in, you know, the components
of data protection, you know, those layers
are already built in. So, when you create a model, it's very easy to create that
model with a set of skills that are repeatable. And in order to do this, it's real easy. You just do it, guess
what, inside of a browser. You hit the record button. You go through a series of steps. And some of those steps
might be manual intervention. You might have somebody
that needs to do something, approve something, you know. After all, they've got access to the keys, to the kingdom, and everything else. So we need to make sure
we have that audit trail. We have that visibility. And having those actions
in that human oversight, it has to be done where humans work. And again, that's inside of that browser. And so we've built this
with control policy into that hardened Enterprise Browser. It can access storage, secure storage. What's secure storage?
Could be your cloud storage. Well, can I get there
with Chrome and Edge? No, you used to, but now you have the Enterprise Browser. That's your only way to get there. That's also the agents' only
way to get there, right? So we've created that closed loop system for that agentic AI to take over and be able to do the functions that are needed for the company, and of course, that full audit trail. This includes screenshots,
you know, mouse clicks. Where did they type? What did they put in? What came back out? What
did the screen look like? You know, full audit,
full capability for that. And so, when we have this
governance and control, you have to think about,
well, who's gonna use it? Well, we got the mode set up
so that a builder can build what they need to build for an AI, for an agentic AI within the browser. Again, do the recorded replay. You know, we have the
access to the applications. Those are running in a
browser, whether they're PWAs or, you know, just basic web
apps or maybe WebAssembly apps. And then of course,
what they can do, right? What they can do, which
button can they click on? Which button can they never click on? That's kind of an important thing. If you don't want an agentic AI to accidentally click the
big red button that deletes, you know, 20 instances, you
know, of your EC2, right? That's gonna be a challenge.
That happens in a browser. That can be an agentic AI configuration. So, that configuration
is important, you know, can they just read the data
or can they delete it, right? And so, now we have that
ability to give that oversight and deploy with confidence. And so, we can deploy
this in a number of ways. Obviously, you know, the Island browser, it can be run in a remote browser, isolated browser environment. This is a locally running browser as well. So, most of the activity that you do is gonna run on the endpoint. It's gonna run, you know,
locally with your system on your network, with your
data, with your credentials. That's the productivity that
we really wanted to see. And that's what, you
know, we can integrate with Bedrock for that as well. So, full integration with AWS Bedrock so that you can keep your data. It could be, you know, stored
within the Bedrock system and it obviously built
for scale for there. So, what did amazon.com do? So, again, I mentioned that we have kind of a
customer testimonial, and I was hoping Adam could
be here to talk about it, but what they were able to do is they found a way to use our
agentic AI or Island's AI agents to build some real productivity within some of their key systems. And they did this in a few ways, but the whole point of
this was that it was easy and they put the hands in the folks that actually knew what they were doing. Folks that know that it's
a repetitive task, right? If they're doing the same
thing over and over again, they know that they could save time. So let's put the power of that automation into the hands of the
folks that could use it and let's make sure it's governed and let's make sure it's safe. And so, you know, this
is kind of how it's done. Pretty simple as you can
think about a recorded replay. If anybody, you know, has
been in IT as long as I have, you probably heard of Mercury Interactive. We used to record and replay
scripts like Selenium scripts, and COM, and CORBA, and DCOM, and all these different protocols. It's kinda like that, but super easy 'cause it's built into the browser. So, all we do is you prompt the user with what workflow to build and include a set of skills along the way. And those skills could be
click on this, search for this, do this button, take this PO number and copy it and paste it over here. And that's productivity that you can quickly
do across applications. And again, this all happens within that governance of the browser. You validate it. You edit
the flows if you need to. You add human interaction
steps for those needed. And then of course you share
that with your department and increase productivity. These are the three use cases. And I do wanna have questions
here in just a minute, but these are the three use cases that they actually put to work. So, amazon.com and their
marketing teams and a few others, they're doing some really
cool automations already as Island customers. And so what that means
is their purchase orders. They're automating the updating of the, a lot of these manual
tasks that are happening as well as the social media
team and the marketing team doing things across different platforms and moving data, adding
tags to certain areas so that they can be quickly
monitored a little bit better with those tags. But again, all things that they would just be
naturally doing in the browser, we can automate that and make sure that they're
now governed and safe. And again, that's that tag
creation there at the bottom. So, in particular, I like this solution that he really wanted to
showcase this himself, but the challenge here on
this purchase order one that top use case was
that they were spending, and I think it was 30 minutes
per day for 1,000 users. So 30 minutes per day for 1,000 users today at Amazon right now are being saved because they've implemented
this agentic AI solution with the Island browser. And basically what it is,
it's updating permissions. It's copying and pasting PO numbers. And before it actually gets executed, before they actually pay that
bill, they get a little prompt that says, "Okay, we did all this work. Is this the bill you want to pay?" And they hit yes in the browser and then it executes that transaction and actually pays the bill. So anyway, 80, I think it's
80 cumulative hours per week, which is an amazing
impact over 1,000 users. That's a big deal. So, that's
what I wanted to show today. Obviously you can see the power when you think about agentic AI. If you're not thinking about what it can do within a browser context, you're not considering
it, you know, thoroughly because this is where the data is. This is where you have access to the data. And now with the Enterprise
Browser of Island, you've got the governance,
the control, the audit, and you have that capability
just naturally built in to a single, you know, ecosystem for that app delivery mechanism. And we'd love for you
guys to come see a demo. This is something that
I could talk about for, you know, for three days. You still wouldn't get it. If you come see it, I guarantee
you it's not just a browser. It's a true enterprise delivery workspace. We'd love to give you a demo
and walk you through it. We've got just a few minutes for questions if anybody has any. We've got a roaming mic coming through.
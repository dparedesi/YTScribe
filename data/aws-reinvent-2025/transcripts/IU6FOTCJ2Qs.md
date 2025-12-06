---
video_id: IU6FOTCJ2Qs
video_url: https://www.youtube.com/watch?v=IU6FOTCJ2Qs
is_generated: False
is_translatable: True
---

- Welcome to Dev 336 Kiro in action. Let's talk about the problem that we're trying to solve today. That's the visibility gap. When you're doing a red team engagement or a pen testing assessment
for a large organization with hundreds of AWS accounts,
you're gonna have hundreds of thousands of resources and you're gonna need to find the vulnerabilities within those. We're gonna show you how
to build a tool using Kiro to do that. Let's introduce ourselves. I'm Nick Gilbert, the
red team manager at FICO. I'm an AWS community
builder on the security and identity team. I'm also part of the AWS
Subject Matter Experts program for the security specialty
exam and a Gen AI enthusiast. - And what's going on
y'all, my name's Damien. I am a senior cloud security
engineer at FICO during the day and at night I'm the founder
of the Devsec Blueprint, which is basically to help people get into
DevSecOps Cloud security. I'm an AWS community builder, just like my buddy Nick over here. I also produce a lot of content as well as create courses on LinkedIn. And then for fun, when I have the time, whenever I have the time, I love anime, I like cars, I play video games. And those are just a
sumation of my hobbies. But let's just quickly
discuss how we intend to close that visibility gap. And I'm gonna turn it back to Nick so he can cover the IAM scanner and the high level requirements. - So we're gonna build a IAM
scan that does the following. So first it's gonna identify
your high value attack fast. It's gonna enumerate cross account access. So you'll often start out in a dev account and then wanna work your way
to those crown jewel assets in the prod accounts. It's gonna be able to
prioritize roles by impact. It's gonna spot common
mistakes like wild cards and trust policies, missing external IDs. It'll give you specific
actionable escalation pass. It'll provide repeatable results, so once you report your findings, the team will tell you
they fixed the issue and then you can simply
run the scanner again to confirm everything's fixed. And then finally, we're gonna use Python with multi-threading to
be able to scan hundreds of accounts all at once. - So the question that we
need to ask ourselves is how can we solve our solution
quickly as security engineers? So with the introduction of
AI into the industry, we know for a fact that there are
two kinds of strategies that we can use to be,
to make this happen. So there's vibe coding and
there's also spec based design or spec driven development. And the question is, which one do we use? So let's talk through vibe
coding, right, at a high level. So Vibe coding essentially
is basically you and the AI just vibe, right? You open a chat, chatGPT,
(indistinct) code, AI, whatever have you. You throw some ideas at it,
you brainstorm, you refine it, and you copy and paste the
code, you keep tweaking it and you just keep doing
the same thing over and over again until it actually works. And it's great for proof of concepts, but it is not what we need
for scalability, right? It doesn't scale. There's no way to understand, there's no shared
understanding, no guarantees. And there's definitely no
long-term maintainability for all of that, right? And for us in our approach,
that's not how we want to basically build a
production scale security tool or even guardrails for that matter or any type of security automation, right? But with spec based design and or spec driven development,
it's quite different. And when you look at it like this, you're basically the
architect of your solution. Before you even ask the AI to
write code, you basically have to think about everything
from the beginning all the way to the end, from the requirements, have everything mapped out and how you actually want
it to be implemented, right? Which in a sense, is gonna help us build that scalable maintainable
solution that updated by changes to the spec itself. And that's pretty much where Kiro comes into the picture, right? So Kiro is basically that AI powered IDE, that basically is used to
enhance the software development by using AI agents on the backend. And one of the key features
of Kiro is that it supports that spec based or spec driven development and spec based design
that we talked about. Not only that, but it's very
user friendly and easy to use. If you're a developer and you
use VS code, it's very easy because it's basically a clone of VS code. And it also supports various different programming languages. So with Python being our
number one programming language of choice and what it is
that we use to what we use to build the IAM scanner. So now I'm gonna turn it back
to Nick so he can talk about how to create a spec using
the prompt framework. - So to create your spec
files, good way to do that is using the prompt framework. So PROMPT is an acronym. So the P stands for purpose. So this is a brief description of what you're trying to build. Then you wanna give the requirements, so a high level overview of your program. Think of this like a job description. Next is the output, list how you wanna
receive the deliverables. Do you want it in one single file or do you want it
modular in several files? Next up is the method. This is gonna be the largest
section of the prompt. So you wanna enumerate the very specific details of your prompt. And then a pro tip, this
is something I always like to do when using Kiro is
at the end of the prompt, I tell it to ask me clarifying
questions before it begins. There's usually always something
important that I forgot. And then finally testability. So one great thing about
kiro is it can create unit tests for you. So anytime you make a change
to the software, simply run the unit test to confirm
everything's working okay. - All right, so when it comes
down to the IAM scanner, the thing that we use and that kiro expects
is three markdown files. So we have the requirements,
which is basically what we are wanting, right? The design, which is what is needed, and then also the task, which
is how we actually want this to work, right? So the step by step execution. But the beautiful thing
about this is that as someone who may not necessarily have
a lot of software development or engineering experience, you can essentially
create your own products by just essentially creating
markdown files with a bunch of texts, right? And I think that's the
key thing with kiro is that it puts you in a different part or in a different spot of
the SDLC by allowing you to be able to write the the specifications in English instead of in code. And next slide. - So let's talk about how
the I Am scanner works. So the first thing it's
gonna do is cache the AWS managed policies. There's over a thousand of 'em. So when you're doing hundreds
of accounts, you don't want to download 'em each time. So it's gonna use a
caching system from that. Next up is gonna collect the IAM data. So this is your users, groups, roles and customer managed policies. Then it's gonna analyze all
those managed policies using a policy engine, find out
which ones have high level permissions. Next is gonna check all the principles. So both the managed policies
as well as the inline policies and determine which
principles are dangerous. Then it's gonna look at
the role trust policy. So this is important for lateral
movement bulk (indistinct) in the current account, as
well as cross account access. Then it's gonna look at unused roles. So a lot of times when
doing red team assessments, the roles we end up using are unused ones that were created a long time ago with high privileges and never deleted. And then it's gonna analyze
privilege escalation paths. So this will go through every role, determine if it has a
path to admin access, and then tell you how you
get from where you're at to admin access. For example, it may say,
assume a certain role, then use that role to create an EC2 instance with the high privileged role. We'll give you the code
for this at the end. - All right, so now that you understand how the IAM scanner works from
an architectural standpoint, let's talk about the estimated
time it would take if we attempted to do this without using AI versus with using Kiro. So if you take a look at
the table, you can see that from planning and design to development, you got touchpoint meetings, testing, and also the rework rate. You're looking at between 200 to 350 hours for building out a tool
as sophisticated as that with all those various different steps. But with Kiro, you can see that there's at least a 70%
reduction across the board simply because we're
essentially passing in all the parameters for it to be able to build out everything with AI. That includes unit test cases. And the key thing is also that rework rate because it's generating the
code and it's also going through and testing the code as well
while it's generating it. So you're thinking about maybe
25, 35 hours, if not a week, for us to be able to build this tool. So just so y'all know that
I'm not telling y'all no lie. Let's talk about some of the results so you can see everything
that actually happens, right? So when you take a look
at this, this is step five of the IAM scanner where it's
basically iterating through and performing a role
analysis in my account. So yes, this is my account
ID please do not steal it or take it or do anything bad because I'm going to
terminate the account anyway. But ultimately you can see
that there are 40 unused roles, and 21 of them are considered
to be dangerous, right? And the beautiful thing about this is that it generates two files. It generates the JSON file,
which can be used for, you know, some automation that you're writing, and it also generates that
markdown report with all of that information in those analysis points. But the thing about this
is that with that report that's being generated, if you need to convince your leadership
to throw some extra money so that you can have the additional
support to secure some of those resources in the
cloud, you can export this as a PDF and send it all on your way. And basically, that'll
allow you to be able to convince people otherwise by basically giving
you an executive summary of what's going on in
your account and why. And all this, again, is maintained
by those markdown files. So if we need to make a change to this, we essentially update the
spec and have kiro go through and update the code for us, right? So some key takeaways. Use spec driven design or
kiro to rapidly develop and scale your security solutions. Why? Because you can essentially
pass in those requirements via text to be able to make that happen. Also, use spec files to translate those product
requirements into a working code and software without writing code. Hence what I just said in
the first key takeaway. And the last thing, if you
are a security engineer, whether it's red team,
blue team, purple team, whatever color you're on
the map, you wanna make sure that you create automated tool and to be able to find those
unlike entry points into your cloud environment and any of
those hidden vulnerabilities and risks so that you can
pretty much mitigate all of those in an automated fashion. So next steps, as we
approach the end, if you want to check out the code, please make sure you scan
the QR code at the very top for the IAM scanners and
GitHub it is available for use. And then also connect
with us on social media, myself and also Nick. Those are our QR codes
to our LinkedIn profiles. Thank you guys so much for listening.
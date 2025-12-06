---
video_id: yh51_W3tR5o
video_url: https://www.youtube.com/watch?v=yh51_W3tR5o
is_generated: False
is_translatable: True
---

- Hi everyone. Can you hear me? Good. Okay, perfect. So I think it's time and we
should start this presentation. So, first of all, thank you
so much for joining me today. I really hope you're having a great start to this conference. I know it's the first day, and today actually I'm
very excited to share something that brings together two of my favorite things. First is gaming. So I am from gaming domain, and I've worked in gaming
domain for the last seven years. And the second is applied generative AI. This is one domain where most of us are quite curious nowadays. So the title of my session is "GenAI game coach: Real-time
gameplay feedback." And the big idea behind it
is actually very simple. So, in this talk, we'll
explore an imagination where you have your gameplay clips, and we are imagining
if your gameplay clips could talk back to you and tell you exactly how to improve, if you like gaming, if
you're into video games. But the other aspect of this talk is we are not going to talk about SDKs. We are not going to talk about
some game engine plugins. We are actually going to
take a raw gameplay video, and we'll use AWS-powered offerings to see how we can build
an intelligent agent that will guide us and act like a coach looking over our shoulders when we are playing a game online. So before I get into this talk, I'll give a brief
introduction about myself. My name is Gaganjot, and everyone calls me Gagan. So I go by Gagan. I am currently working for
Sony Interactive Entertainment, which is basically the
gaming division of Sony, known for PlayStation. I have been with PlayStation
for almost seven years now, and I work as a staff software engineer. My focus is backend engineering and I've worked in different domains, started from personalization, and then jumped into cloud streaming, and my most recent is AI enablement space. So I'm actually very
passionate about experimenting with GenAI for gameplay,
for developer tools, for interactive intelligence. And this talk is one of those experiments which turned into a super fun prototype. So, we have a limited time, but I'll try to go over a couple of things in this next couple of minutes. So, on a high level, we'll talk about what is the skill improvement
demand in the gaming industry. Why are players struggling? Then we'll look into how
generative AI can help players make sense of fast or chaotic combat. And then finally, I'll show
you an AWS-powered architecture where we are going to look
into different offerings, but mainly focusing on
Amazon Bedrock and AgentCore, which basically orchestrates
the entire coaching workflow. And I'll also show you a de
demo video of what I built, what it looks like, what is the coach built using AWS say about a sample clip
that I'll show to you. And finally I'll wrap it up. But if you're interested to
continue this discussion, if you have more ideas,
definitely let's catch up. Once this talk is done,
please meet me afterwards and I would be very happy
to take your questions and your further ideas in this area. So let's get started. I think the very first thing is I would basically like to talk about a scenario where you're imagining that you're playing "Spider-Man." "Spider-Man" is one of my favorite games. And you're swim swinging
through Manhattan, chasing a group of thugs, and one brute suddenly charges at you. A sniper laser lines up from a rooftop, and you get hit. In that moment, what you think is, "I reacted on time and I
did all the right things, but I still got hit." But if you think about a game which is a "Spider-Man" style combat, it's a very fast and chaotic combat. Human reaction time is
usually 250 milliseconds, but these telegraphed attacks resolve in 100 to 150 milliseconds seconds. So this mismatch of timing means most of the players cannot
even see their own mistakes. So the scope of improvement is very less because you don't even
know what you did wrong, what was the move which
caused you this kind of hit. And this is not just "Spider-Man." This can be actually imagined about most of the games in the gaming world. So, looking at some studies, I've seen most of the
players actually misdiagnose their own mistakes in a video game. And that's where we have some challenges, we have some opportunities, and we have a potential solution. So talking about the challenge, like I said, gameplay is chaotic. Players don't know what went wrong, and a mistimed dodge
happens in 150 milliseconds. A wrong rotation decision
happens in half a second. So there is a complete mismatch of time between the player's response versus how the game is responding. And raw gameplay is actually very noisy. Most skill mistakes happen
far too fast for players to even break down on their own. So that's where we have the opportunity. We have millions of players
who want to get better. They don't have coaches and they don't want to invest their money into these expensive tools
or expensive softwares, which could be also complex to understand. Even studios don't want
to in huge GPU clusters to build some scalable analysis. So that's where we are going
to imagine about a solution because this is where GenAI can shine. So what if your gameplay could talk back? And what if you had a personal AI coach that understands timing,
movement, and decisions just from a short clip? So that's where we are headed. But before we get into the
actual stuff that I built, I wanted to show you a sample game clip. It's a long clip so I'm not
going to show the entire clip, but it's relevant because this is the clip which I used for actually
performing my demo or actually building the
website and analyzing this clip. This is a game clip
which is 578 MB in size and the duration is roughly five minutes, but there is like a lot of action, a lot of movement happening in this clip, and a lot of things happening. So I'm going to play it for a few minutes to show you what this clip is all about. And afterwards, in the demo, you'll see what the coach that I built using AWS had to say about this clip and what could be improved by this player. Anyways, I'll go on to the next slide because I just wanted to give
you a glimpse of this video that I used for my analysis. So now comes the AI-powered
architectural solution. So before we jump into the demo, I just wanted to show
you a high level flow of what my architecture looks like. So let's just start at the very beginning. We have a user interface. User interface is basically where the user will input a clip. So you need an interface
where you capture the clip, maybe five minutes, 10
minutes, whatever long clip, and you want to upload it. So this is an interface. It's a simple react based
single page application which is delivered globally
using Amazon CloudFront, so that's the CDN layer, which will ensure low-latency
access for players anywhere. And not only you will upload the clip, you can also actually see the
analysis report on this UI. Also, it has another functionality where you can trigger an
actual conversational agent which can talk to you and give you suggestions on the areas that
you need suggestions for. So from the next layer, we go onto the API layer. So this clip actually
goes into S3 storage. So when you click upload button, it will, basically, behind the scenes... We have two kinds of gateways. We have API gateway or Lambda URL function which will perform different functions. So API gateway actually provides
you different endpoints, like there is an endpoint to get the upload URL of your S3 bucket where this clip is getting uploaded. There is an URL analyze endpoint which can basically
trigger the analysis by AI. And there is also a chat endpoint which will trigger your chat when when you want to
chat with the AI agent. On the other hand, I also
have Lambda URL function. The purpose of this is actually
for bigger size videos. I was actually hitting
timeouts on API gateway, so the default timeout is 30 seconds. But for Lambda, you can
actually increase this timeout. So for bigger videos, it's
better to actually use Lambda instead of using API
gateway to upload a video, get the URL, and send it for the analysis. So this is what the API layer
looks like on a high level. Next comes the compute layer. So, compute layer is basically
the different Lambdas which this application is using. On a high level, there are three
different types of lambdas. So there is analysis
Lambda which basically is used for generating
the S3 pre-signed URLs for video upload, and then it will process
your video from S3. Next is the chat handler Lambda which basically receives the chat messages from the front end. It invokes Bedrock
agent behind the scenes, and then it gives you the
results on the front end. And last is the agent action Lambda which basically is used for executing Bedrock agent action group functions. And this use case that I built, I've used it for just for myself. But even if you want to have multiple users hitting your website, the Lambda is scalable. There will be multiple
instances of Lambda coming up if you have multiple users trying to upload video on this website. The storage is S3, and the final is the AI/ML layer. So there are a bunch of
things here in this layer. We see there is Amazon Bedrock. So there are two kinds of ways in which I was basically using Bedrock. So first is I just give my direct video to one of the models that
I selected on Bedrock. Bedrock gives you access to a variety of different LLM models. So I used Amazon Nova Pro which
can directly take a video, and it can analyze your video and understand what is
happening in this video. The other area which I
built in this application is using AgentCore, which gives you a facility to build a production
grade agentic platform. So it takes care of the memory. It takes care of any kind of networking that you wanna build, but essentially I used it to build an interactive coaching chat. So there will be a two-way communication. You can ask questions, and your chat is also getting stored. So it also retains the
history of what you talked. The other parallel analysis
that happens behind the scenes is using Amazon recognition, which is for computer vision. So this analysis helps us to identify what are the different
objects in a given clip, what the scene could be
about, what is the text. If your video has speech like you are saying certain things
while playing the game and you capture that video,
you can actually have a speech to text transcription
using Amazon Transcribe, which is another parallel
analysis that gets triggered. And the last one is Amazon Comprehend which basically does
the sentiment analysis of the entire clip. So this is what, on high level, what the different components look like. I also wanted to quickly show you the prompts which I used for this. So prompts are very important. Behind the scenes, you can
have different personas for your agent. This agent is a coach. What kind of coach you want? Do you want a supportive coach? You want a coach that is motivating and saying friendly things or you want to coach,
which is very competitive and really giving or grilling a player. That will very highly
depend on the prompt. So the kind of language generated in terms of the
suggestions from your coach would actually be dependent on
the kind of prompts you give. So, as an example, I've given... You're an expert gaming coach
with years of experience helping players improve their skills. You have access to the player's
gameplay, blah, blah, blah. But I've also told it be conversational, friendly, and motivating. You are here to help
them level up their game. So this is like the detailed prompts I gave for different personas. Moving on. I wanted to actually show you
a quick video if it plays. But yeah, this is a demo of the video which basically takes this same video that I showed you earlier. And as soon as I click
the start AI analysis, it basically runs behind the scenes. It's uploading your video to S3. The Lambda will trigger all kinds of AI analysis on your video, and it will basically
generate you the report of what are the suggestions provided. So, what I noticed, one of the challenges
I noticed was it takes a very long time to upload it to S3, and that's where it's kind
of taking most of the time, but I wanted to actually
forward it and show you the actual prompts or the actual results which
came from this analysis. So you can see there is
computer vision analysis, which comes from recognition, which shows there's a person, there's a road, there's
weapon, there's gun. This is the AI gameplay analysis, which comes from the Nova Pro model. There's a lot of analysis but
it basically recognizes... This video shows a player navigating various environments in "Destiny 2," engaging in combat with enemies. And then if you see player performance, that's where it tells there are moments where the player could improve in terms
of situational awareness and enemy engagement. But at the same time, if you see the tone, it's very friendly and
it's very motivating. The player's gameplay is commendable, especially in terms of
aiming and cover usage. So this is a high level AI analysis. And then there is overall assessment, there is sentiment analysis, and also wanted to quickly
show you the coach. So, in the end, there is also a button where you can actually trigger this coach. So there are also some custom
prompts for this coach. So you can select one of those prompts or you can actually
frame your own question. But if you select one of those prompts, it will basically generate
the question on its own. So for example, if you select
Analyze My Performance, it will basically create the question that, hey, can you give
me a detailed breakdown of how my performance was? So this is the screenshot of the demos that I actually wanted
to show in the video, but it's not forwarding. So I just showed you in the screenshots. So I think, the next, I just wanted to quickly
touch on the cost side. For my use case, I used all
these different offerings and the total cost for this one video, which is five minutes long, was $0.9. Of course, once you build
something at a production level, you have to take into consideration how many concurrent users
are in your environment, how frequently you want
to do this analysis, and how big would be the video size that you're dealing with. So yeah, for a casual gamer, if I have five videos per
month, it will be $50 per year, or for 20 videos per month, it
would $235 per year roughly. Latency analysis. The latency, like I said, it did take a lot of time to upload. It almost takes eight minutes to upload. So this is one area where I would like to improve it further. The AI analysis is still pretty good. It takes almost two minutes to finish the entire parallel analysis. So the total time is roughly 10 minutes for this five-minute long
video for this entire analysis with the report that you get. I think, lessons learned,
I kind of already touched on few of those things, hitting the limits of
the size of the video, and then figuring out what
is the other way for me to pass on these videos to models like Nova. So, for Nova, the limit
that you get is one GB. And if you're uploading it on S3, you can actually upload
a video as big as one GB. And the other thing I
wanted to point out was I did not have to do any
kind of frame extraction. Nova recognition, as long as
you've uploaded them on S3, they're taking care of
extracting the frames on its own. As far as I understand,
Nova is basically doing intelligence sampling behind the scenes. So that was all taken care of. What's next? So, basically, like I said, I would like to work
on the latency aspect, would like to reduce it from 10 minutes to at least make it near real time. I would also like to
explore video compression and caching technologies to improve the overall latency and cost. The other area where this
would be very useful is for the live streaming platforms because there is a lot of players who actually stream their videos on platforms like Twitch or YouTube. Can we analyze it and can we build this conversational thing as and when the players are playing? So those are the areas where I want to explore these things in future, but with that, I would like
to share some of the links. So there is a GitHub repo where
I have put this entire code with instructions on how to run it. You can connect with me on LinkedIn if you want to continue this discussion even after this conference. But yeah, that is all from my side, and thank you so much for
coming to the session, And I see that I'm right on time. But if you have any questions,
please meet me afterwards, and I'm more than happy
to chat with you all. And with that, thank you so much. Have a great rest of your day.
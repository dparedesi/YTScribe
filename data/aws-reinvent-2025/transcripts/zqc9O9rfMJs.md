---
video_id: zqc9O9rfMJs
video_url: https://www.youtube.com/watch?v=zqc9O9rfMJs
is_generated: False
is_translatable: True
---

- Good morning, everyone. Thank you so much for
joining us this morning. A full three hours into re:Invent, so I assume the donut sugar high is kicking in any second now. My name's David Provan, I'm Vice President of Digital Architecture with the PGA TOUR. I'm here with Murali who's our Solutions Architect
on account from AWS, and we're here today to talk to you about the work we have
done at the PGA TOUR on using agentic AI to write content for distribution on our digital platforms. So, I'm gonna stand up because
it's awkward to sit down. I just feel weird about it. So, let's start by describing
what the PGA TOUR is because some people don't
know and that's okay. The PGA TOUR is responsible
for operating golf tournaments throughout the globe at this
point for other players. So, unlike other sports leagues, we're actually player-owned. Many other sports leagues
are like owner, down. Our players actually own the PGA TOUR. So, our job is to deliver golf tournaments for the players to have
playing opportunities and improve their game and
prize money, essentially. And we do that pretty much
every week of the year, then we get like three weekends off. Other than that, there's
golf every weekend and we also do four different tours. So, you may have all
heard of the PGA TOUR. We have the Korn Ferry Tour,
which is our qualifying event, PGA TOUR Champions, and PGA TOUR Americas. And these are all, again, opportunities for our players to be seen, to be engaged with and to play
the sport they want to play to progress up to the PGA TOUR. We're a bit unlike other sports. Other sports, you play
inside, like, white lines or you play in a stadium or a fixed area. We don't do that. We play in these amazing venues
which are 150 acres plus. Everything you see is playable area. There is not inside this
white line, stay there. We've had players purposely
hit balls on top of clubhouses to get relief. We will have John Deere tractors in the middle of the golf course when it's a John Deere Classic. So, we have natural objects that players are working
around to play golf and all of that is part
of our playable area. So, to data collecting that
is a real challenge for us. We have 156 players, 31,000 shots in a standard
golf tournament in stroke play. We then decided that wasn't hard enough, so why don't we do
different scoring formats? So, some weeks you'll
watch a team stroke play, match play, stable foot scoring. So, we have a whole
variety of, like, variables that go into what we do, and our biggest challenge inside all that is how to engage you
guys on what we're doing. Golf is hard. Golf is sometimes particularly
hard to watch live, but sometimes it's hard to
know what the hell is going on and why should I care. So, we're building agentic systems to help us kind of solve those things. We're gonna cover those today. So, if you look at our digital strategy, like, at the core of what
we do, some of you guys... I remember the guy who
once used an analogy of, like, the wedding cake, which is, like, our
website is the base layer. It's got everything
you could possibly want to the nth level. If you want a golf nerd out, it's probably on pgatour.com somewhere. You'll find it and live your best life. Our mobile apps? Highly engaged platforms, and so we see like a 7X
consumption compared to web, but it's highly focused,
like, short-term use. In, leaderboard, out. In, leaderboard, watch videos, out. But they'll come back
seven or eight times. They'll use the platform a lot. More recently we played with
Vision Pro and other platforms and we have this kind of content strategy where we will build out from that. And then, we've actually been successful working with other golf
organizations more recently and bringing some of
this PGA TOUR technology whether it's Shotlink or our
digital products like TOURCast and delivering them for
USGA, PGA of America to kind of create that experience that fans have come dependent on. So, like I said, with data first, the biggest problem we have is gathering data off a golf course and making it relevant to our players, to our sponsors, and to our fans. That's the challenge we face every week and I do mean every week on the PGA TOUR. So, we are gathering petabytes of data. If you come to a PGA TOUR event, which you should all come,
please, you're welcome, you'll see these cameras that are like world's best
security camera system, 140 4K cameras dotted
around the golf course. They are scanning, each
one at five on a hole and they're analyzing the
ball data as it comes in. And we also have two radars
on every single hole. One on the tee, one on the green. They are military-grade radar used for tracking tiny white objects and in our case, our tiny
white objects are golf balls. We've also got on there... The cameras all plug in together and we're starting to
look at player movement, where are the players. And we thought we built this really great golf
ball tracking system and our security team are like, "That's also a really great closed circuit camera
system for out of hours. Can you leave them turned on please?" Aside from all of that other data, we have walking scorers
capturing when ball is hit, ball in motion, and if you watch a
Shotlink event underway, the determination of the Shotlink team to capture every single shot, it's a militant
determination to be perfect. It's incredible to see those guys determined that we will
not miss a single shot. We deliver those to gaming providers, we deliver to digital platforms, but we capture a very large and significant amount of data on site. We also build (indistinct) stuff. If you come to a PGA TOUR
event and you see the cameras, at the bottom of the camera, you're going to see a black skirt. If you get really close to it, which you can 'cause the playable area's also the area you get to walk in, you'll see solar panels have
been stitched into the skirt. So, we can run our cameras
through solar panels. We get two or three days of light, which we do on golf courses typically. We can run that and we're
not shipping power and stuff. So, at our core, we're
really an operational team that runs and deploys and
runs golf tournaments. Like I said, 150 acres. (mumbles) 14 balls, and we've covered the stuff. So, where do we store that? The first project we undertook
with AWS was this data lake. Where do we put the data? And we built this massive collection of scoring data, ball data, content, all the stuff that we could possibly need, and it's highly structured. We know every single shot back to, I think, 2012 is our shot data collection. Might be before then. We have scoring and
leaderboard data back to 1864 if you'd like it. So, we have tons and tons of data. So, our real challenge is how
do we storytell that data? How do we pick what's
relevant at the right point, at the right time and the right mechanism to make you engage with our platform? On top of that, we've
also built a media lake. So, on a given standard PGA TOUR event, we're running seven live video streams. Four with ESPN, some with Golf Channel, some with NBC, some with CBS. Those are all stored in the media lake. We have... I can't, I'm going to get the number wrong so I'm not gonna say
it, but let's just say, thousands of hours of golf coverage, which we've essentially
built a shopping cart. You can come and say, "I want
all Scottie Scheffler putts that are less than 10
feet at this golf course," and we'll create a playlist that we can give to our
broadcaster and say, "There's your supporting reel
you can use in broadcast." So, this data lake and video
lake is super important and kind of the core foundation of what we're building at the TOUR. So, we've talked data. Now, we're going to talk about the AI side and our challenges that the TOUR has in terms of what we deliver. We started looking at AI
about two to three years ago. And I think most like all of us went, "What do we do with it? Sounds cool. Not sure
what to do with this. Not sure how to derive value out of it. Not sure if it's going to... How do we use it properly?" So, actually we have a
really strong product team in our digital team. We took a product-first
approach in what we did. So, we build any feature for
PGA TOUR digital platforms. What's the value for the fan? What are the values of the stakeholders? And what are the value to the brand? Those three things are the top of what our product
team do week in, week out. We just applied that to AI. What can we do that will help
our fans consume content, provide more coverage, and being the PGA TOUR voice, and respect that kind of brand. So like I said, fans, business, and brand. And sometimes, we do things
that match all three of these. Sometimes we do things
that match one of them. Sometimes we do something
because it's cool. It's not fan engagement, but a sports thing you want to look good. And sometimes, we do
things that no one sees but it cuts my AWS bill by 20%. It's important to the business, right? As we build those features, we then have this, like,
production-first thinking in what we're doing. So, I have worked in technical sports for about 16 years. We live in the edge case. We are really good at edge cases. What happens if someone
holes-in-one and damages the hole and we got to re-pin
the middle of a round? What happens if Jordan Spieth puts the golf ball on top of a
clubhouse to get free relief? All these things are
areas that seem ridiculous but is what we call Thursday. We have these 31,000 shots. They are not uniform,
they're not consistent. Golf is hard for those you who play it. So, we live in things that can go wrong. So, we have to bring that
kind of edge case thinking to the forefront of what we do. So, the first thing we talk about is how do we score and validate. We work in sport, we can't be second. If we're second, we're last. We have to be first. So, how do we automatically approve things as quickly as possible using
scoring and validation? So, our features essentially
will go through an analysis and work out, have you passed
the validation techniques? Some of it's simple regex, some of it's LLM as a judge, some of it's take the original data and check it's in the output. There are different
techniques we use there. Sometimes, we'll throw to a human when we're building a new feature, as Murali will come onto. We'll have a few running
draft, we'll verify it, when we're happy with the quality, we then flip the auto button on. And then, more importantly, we plan for that production
at the beginning. All the features that Murali
will take you through here, we have not changed our support footprint. We've kept the same support team. We've extended, like,
AWS CloudWatch dashboards and integrations operationally to allow us to monitor those systems and prove that they're
operating at the level we expect and in fact, demand. So, we don't want to be in the business of watching a golf tournament. I've always said my
favorite idea of success, if we sit there and twiddle our thumbs for four days of a golf tournament, giant check mark. We succeeded. The best analogy I have
is the golf tournament, it looks like a swan above the river but the legs are going like crazy, and hopefully none of you see that. If none of you see it,
we've done a good job. So, this journey we took into AI was a really interesting one because we kind of pivoted along the way. And like I said, at the start of 2023, we worked PGA TOUR. Everyone wanted a chat bot. Full confession, David
doesn't like chat bots. I think chat bots are a great way to make your brand be exposed. Just, you have to really
confine what they can do. Played with chat bots. Then, we kind of learn from
that and start to pivot. What are the things that
can make a difference? So, through 2024 we kind of prototyped and worked on this idea
of shot commentary. So, for those of you that follow sport, if you watch NFL on a
Sunday, or Bundesliga, or... I watched a Premier League
on the plane here yesterday. The commentator is quite important. The color commentator is really the kind of
the icing on the cake that sets the context for you. So, not just the play by play, but why does that play matter? So, at PLAYERS 2025, we launched
our shot commentary system. That shot commentary system
works in two aspects. It generates a fact. "Scottie Scheffler has
hit the ball 164 yards, he is five feet from the pin." It then adds context. "He has a 96% chance of making this putt. If he birdies it, he's gonna move to position
one on the leaderboard and take overall lead of the FedEx Cup." Oh, that is actually useful. We were really strong that
we didn't wanna do narration, we wanted to do commentary. And we held ourselves accountable
to a really high standard where it can be repetitive, it's gotta be varied,
it's gotta be engaging, it's gotta matter, which also means sometimes
we don't do the context. Sometimes, it's just his
first drive on the first hole and there is no context. So, we'll say, "Scottish
Scheffler opens his round on a hole one with a 255-yard drive." That's all you need to know, and sometimes it's okay to say nothing. Sometimes, it's okay just
to report what happened. Shot commentary went live
at the beginning of 2025. In parallel to that, we're building the agentic system which drives our content engagement. So, we're going to come on and start talking about those things now. So, shot commentary on the top right here. If you go to the TOURCAST, it's our 3D data model
for every golf course. You see every shot, you see the radar curve for
exactly where that ball went. You'll see the direction the
putts went, the distance. And then, on the right, you'll see our betting profiles which are generated
through our agentic system, and we built a system
using Bedrock to do this, that we're going to have
Murali dive into detail with you guys. But betting profiles, for us, are content that drives
engagement on non-tournament days. So Thursday, Friday, Saturday, Sunday, traffic up here. Monday, Tuesday, Wednesday, no one cares. There's, what am I gonna read about? Unless there's something
newsworthy comes out about golf, we're not a busy website on those days. Betting profiles allow us to kind of push the lever on those days because we know that
fantasy and gambling users get hyper engaged in content
(indistinct) to make decisions. So, we have 156 players. There is no way I could
tell a content guy, "Your job is to write 156
very similar articles today. Does that sound rewarding?" No is the answer to that. So, using kind of a recipe, an agentic system to build those out, we can generate them on Monday
morning at nine o'clock, they're complete by 9:30, they're on the website and we're in the SEO
index very, very quickly. And these things on non-TOUR days are our highest engaged content. It's not even close because the fans that care about it are looking on those days and we become the single
source the truth for it. One of the things we're
really proud of on the TOUR is we lead SEO for our
sport, which is unusual. Like, people come to the
PGA TOUR first for scoring over other platforms, which is something we work really hard on in content like this to
drive those kind of results. So, what's next for us on our AI journey aside from the content generation that you kind of dive into more detail? I don't wanna ruin Murali's bit, guys. He'll be furious.
(Murali laughing) For us, it's the operational side. So, we spent a lot of
work in the last year working on fan engagement
ideas, betting profiles. We actually produced about 180
different types of article, 180 articles of about
eight different types, which are highly engaged
things but super easy to write. Like, at the end of a tournament, we do a purse breakdown,
who won how much money? Literal vertical line for search on that. At the end of a tournament,
it is the most searched thing. How much did people make? Everyone wants to know how much did Scottie
Scheffler win this week? What did Rory McIlroy make this week? We do a possible points breakdown. Given the position finishes, well, how is that going
to affect something? These are all essentially
mathematical scripted things. Super easy to run through LMs and create but also highly engaging for us. Where we're changing our approach or evolving our approach, I guess, in that back end of '25 into
'26 is we no longer can... We try really hard to not do AI projects. We do projects that utilize
AI when it makes sense. And that's been a real mind shift I've pushed very heavily for in the TOUR because I think it's really
easy to get excited about. "Oh my god, it's AI. It must be amazing. I must have more AI. Give me more of the AI
and let's call it agents so it sounds even cooler." And the truth of it is, like, where it makes value and sense to us, we absolutely want to do it. And these things do make
value and improvement to it, but it doesn't mean it's
the be all and end all. Where we are looking at now, the value being derived is
in our development processes, in our operational support processes, in our content management
and planning phases. Where can we use AI tools to drive value and drive operation improvements? So, tools like Kiro, which
you'll hear a lot about, I'm sure, this week. Your Claude Code, Cursor,
those kind of platforms, we're in the infancy of trying to work out which of these make a different, but turns out, to the
untrained eye, they look great. To the trained eye, is like, "That's almost good, but you did just put the
secret in plain text." So, the real challenge for us
as we implement these tools, it's also making me
evaluate how do we hire. Like, my standard development approach was you hire some junior developers, you find some mid-tier
developers to run that team, and away you go. And what we are seeing is the AI tools work really, really well when driven by more senior talent. If I give an AI coding tool
to someone at a code camp, it'll generate what to
them looks like great code. It looks fantastic, it's spelt well, it's camel case, it's perfect. AI agents like to succeed,
they like to make you happy. They're like puppies. They want you to be happy with the result of what they produced. You give it to a senior
developer and like, "That's great, but I'd
probably change this pattern." That also influences how
we prompt those tools. We put those tools in the
hand of a senior developer and they change their prompt. They give much more direct
guidance in terms of how it works and we see the quality that comes out. So, this next drive for us is really the operational improvement to my development teams, to the operational teams, to the Shotlink teams, to every component of what
we touch in the PGA TOUR. Now, does that mean
we'll use it everywhere? No, that would be a terrific
lie if I told you that. What we're getting really rigorous about is using it in the right place where we see differences being made, and also not being afraid to go, "Stop. It doesn't work." There's a real tendency to go, "Just keep going. It's five more minutes. Five
more minutes, it'll be fine." But the bravery to walk away is something we've got
better at in terms of, "This idea didn't work. It was a good idea,
let's move back for it." The big one for us there, 'cause someone's gonna ask me, image generation is a
complete nightmare for us. We have player rights, player images, all sorts of AI IP things. We are not having great success presently with image generation. It'd be fantastic if we could, but the IP stuff makes it hard. But if we look at the operational
stuff inside the building, whether it's coding or
AWS account analysis or spending anomalies, that type of stuff, yeah, we are seeing
value with those things. So, I'm going to hand over to Murali who's going to dive you
deeper into the technology behind the agentic AI content generation. - Thank you, David. My name is Murali Bakhta,
I'm AWS Solutions Architect and I've been covering PGA
TOUR for the last five years. David explained the use case, like content generation and how the content
generation helps PGA TOUR and brings business value kind of stuff. We are going to dive a little bit deeper and figure out how they
implemented this thing and what are the things
that they considered before they implemented
this solution kind of stuff. So, generating content at scale is hard. PGA TOUR generates close
to 800 articles per week on different kinds of articles. We'll look into those
different types of articles. They generate around 800 articles a week and generating this
content using AI is hard. There are like several challenges when you generate articles with AI. The first one is, as you can see, like, the number of articles that needs to be generated is large, and the second one is generating
articles when you have, for live sports events is hard because LLMs typically do not have the data that is needed to
generate articles, right? Because the LLM's data
is usually the old data. And so, you need to feed data to the LLM to be able to generate these articles because you're generating these articles based on the live sports real-time data of how the player played today or how the player played
just few minutes ago and things like that. And so, you need to feed
this data to the LLM to be able to generate
the content for you, because the LLM by itself
does not have this data. And the next thing is
when you generate content, like, PGA TOUR being, like, a world-class sports organization, they wanted to make sure that the brand value
is not damaged, right? When you generate content, you want to make sure
the content is validated, it has a correct factual information in the content that has been generated, and it also make sure that it complies with all the brand guidelines and the style guidelines
that PGA TOUR has, so that their brand value is maintained kind of stuff, right? And in addition, like, the other challenges with PGA TOUR is they generate a large
number of articles. Like, I know David mentioned that about the betting profile articles that people who bet on different players, they have typically in a tournament, they have 156 players. And so, they generate 156 articles on each and every one of those players, and they also have betting
profile summary articles. And then, tournament preview
before the tournament starts, they write an article
about the tournament, and then tournament recap
after the tournament ends, how the tournament happened kind of stuff. Tournament recap articles. And then, they write
articles about player recap, how the player played in that tournament for each one of those 156 players. And also, they write articles on round recap. If you think of golf, golf is played, round
one is played on Thursday and round two is played
on Friday, like that, and round four is plays on Sunday. So, after each round, like, how did the player do kind of stuff because there are fans for like, even for the players who are
the bottom of the leaderboard, there are fans globally, they would like to read
about their own players that they are interested in. And so, you need to write these articles to be able to engage the fans who are, like, globally
present and they're, like, even though they're
not in the leaderboard, you would like to get them engaged in the fan engagement perspective. So, not only they write these
different kinds of articles on different kinds of
players, they also write... The articles can be long form, like, for website and mobile
app, it can be long articles. And if they want to post to social media, it may need be to a paragraph
that they need to generate, right, for the social media stuff. And also, a lot of the
fans have their apps and if you want to just
send a notification about how, like, Scottie
Scheffler did a hole in one or whatever you want to send
a notification to their fans, that's a short-form content
that needs to be generated to be sent to their fans. So, there are different kinds of content that needs to be generated and also different lengths and
different formats of content that needs to be generated, and that's what makes the
problem challenging, right? So, we need to take
care of all these things when you're generating content and your architecture needs to
accommodate all these things. So, I know this is too
small on the screen. The thing is, like, we'll go, like, step
by step in this thing. So, typically what happens is
a content request comes in, like, to generate a
particular type of content like a betting profile
content or whatever, right? And then, the request comes in and once the request comes in, the first thing that you want to do is you want to do some research, right? Like, you want to do research on, like, both get statistical information from the PGA TOUR's database, like, so there's a structured data available through TOUR APIs. You go and get the structured data about how the player performed
last week or the last year and you get the statistical
information about the player, which is already in the TOUR APIs. And also, the research request sends a request to the data agent, and the data agent also looks
through their media guides. The media guides, like, if you look, it's a big PDF
document about the player, where the player grew up and where he went to school and how many tournaments he has won. All kinds of information is
there in the PDF document. So, the data agent goes and looks at the unstructured data which is available in the PDF document and gets that information that is needed to write the content. So, the research request, the research request goes in, goes in and gets the data both from the structured data as well as the unstructured data and all that information is
sent and creates a work order. So the work order is, like, okay, you need to write an
article, betting profile article, and this is the data that
we have done research, like the statistical information from the TOUR structured data as well as unstructured data that is coming from their
media guides and other areas, and all this information is passed on and a work order is created for the editor to make the request. Next, the first job from the work order is taken over by the editor and the editor asks the writer to write an article with
this specific format for this specific target audience and for this specific thing, it's sent to the writer. And the writer agent writes the content based on the information that has been provided
to the writer agent. And then, based on the
article that was generated, when you write these articles, if you look at, if you go
to the PGA TOUR website, when you see these articles, like, you can see the articles
that are generated by AI, it'll say at the bottom, "These articles are generated by AI." They also post an image with the article, so that image needs to be selected from their Getty repository and the image needs to make sense, the image needs to make sense for the specific type of article
that they are generating, and it also needs to make sense
to show the specific player or PGA TOUR in a positive sense, a positive angle, right? You don't want to show, put an image there where the player is
angry or whatever, right? So, you want to like
take the right picture and add that picture with the content. And then, this image with the returned article by the writer is sent back to the editor agent. So, it's sent back to the editor agent and the editor agent, if it finds the article is well written, it just sends the request
back for validation. If the article is not well written, it doesn't conform to PGA
TOUR's style guidelines and PGA TOUR's brand guidelines, the request goes back to the writer and the writer fixes those issues. And then, the editor agent, once the editor agent feels comfortable with all the content
that has been generated, the content is sent back
for a validation request. Because the content is generated, but we want to make sure the content has the right facts in it. You want to make sure,
like, if, let's say, if Scottie Scheffler scored
a birdie in the 18th hole, you want to make sure
that content is correct. And so, that's what you
need to do validation. So, you need to extract
the facts from the content and then use the data. The data agent can give you the data from the TOUR API, like, that Scottie Scheffler scored
a birdie in the 18th hole and that information is
taken from the data agent and is compared with the
data that is available, that extracted from the content. And so, if they match, that means the verification is correct, and then the verification passes and then it goes for publication. If it doesn't match, the request is sent
back to the editor agent asking the editor agent to fix the issues that was identified by the validation agent. Once the validation is complete, the request is sent back for publication to different channels of publication. This is the overall high-level workflow of how the agent performs. To look at the technical
architecture, how this works. To look at the technical
architecture, how this works, this is implemented using agent, they use AgentCore for this thing to run most of their agents
inside AgentCore runtime. So, a request comes in on the... If you look at the black
box on the bottom right, the request comes in through that and then once a request comes in, the request is returned
to a DynamoDB table that a specific workload has
been launched kind of stuff. And then, that request
goes into a job transformer which transforms the request that came in and puts it in an SQS queue. Because as I mentioned earlier, they write, like, hundreds of articles and generating all these
articles at one time. They may hit some limits on, like, the usage of tokens
and stuff like that so they put all these requests in a queue. And then, from there, they pick one of the
requests from the SQS queue and then, the lambda, like, AgentCore Lambda
invoker takes that message and makes a invocation on the AgentCore runtime. And the AgentCore runtime takes a job, and then as we talked about earlier, it needs to make requests to the TOUR APIs to get data from the TOUR API. It needs to make a request to
get Getty APIs to get images. It needs to make a call to an LLM for Bedrock to generate the content. Like, PGA TOUR is able
to save a lot of costs by running these things in AgentCore because every time you make a request and you're waiting for a response, you don't pay for those computer sources with AgentCore runtime. Because AgentCore runtime, when you are making a request and you're waiting for a response back, you don't pay for the compute costs and they save on those costs by running on AgentCore runtime. And so, once the AgentCore runtime, they also monitor the AgentCore runtime, like, latencies and how long it takes and all those kind of stuff using AgentCore
observability kind of stuff. And then, once the content is generated, the content is written back to S3 buckets. And then, that triggers a
Lambda which takes the content and pushes back into the
content ingest workflow kind of stuff. So, that's the overall
architecture that they, a high-level architecture
that they have implemented for this content generation
kind of stuff, right? So, once you have this architecture, as I said, like, the reason behind the
cost savings, if you see, they generate these articles
used for 25 cents an article. So, if you see on the right-hand side, each article is generated
using generative AI for 25 cents per article. That resulted in 95% cost reduction. So, they previously, whatever they spent to
write these articles, now they have reduced the cost by 95%. They're only spending 5% of that cost to write these articles. So, this is a brand new stuff. Currently they're writing around 140 to 180 articles per week. Soon, by the end of this year, they're going to write close
to 800 articles per week using agentic AI. And these gen-AI-generated articles are viewed billions of page views. It has billions of page views per year. So, these gen-AI-generated articles have billions of page views per year and they... For the image, like, to check if the image is appropriate image to add to the article,
they use Nova model. Because they're using Nova, they reduce the cost by 75%
because Nova models are, for price performance wise, much cheaper. And so, they were able to use Nova and reduce the cost further
for the image selection, image review piece kind of stuff. And then, as you can see from the graph, these articles have like the highest views when the, like, every week, you can see there's a peak when the tournament happens and then it dies down when
the tournament gets over. So, because they're using AI to generate these articles
instead of humans, right, they can generate these articles within five to 10 minutes
after the tournament ends. Let's say the game, the
game ends on around... One ends at 5:00 PM. They can generate these
articles within 5:05 or 5:10. So, they are the fastest to
the market with these articles over the other sports
outlets and stuff like that. So, that means they get
the highest number of hits because when you do a Google search, they are the only one
who has that information about these articles. And so, they get the
highest number of fits and that is not only their saving on cost and they are also getting
the highest number of hits with these agentic-AI-generated
articles kind of stuff. So with that, I would like to, like, say, like, agentic AI can not only, like,
overall reduce your cost, it can also, like, help you increase, like, the fan engagement also, like, be able to help you with improving the performance. In this PGA TOUR case, they were able to get the
highest number of hits kind of stuff. With that, thank you. And if you have any questions, like, we have a lot of
time, we have 20 minutes. So, if you have, like, any more questions, there are two mics at the back. Feel free to ask either me
or David before this end. Thank you. (audience clapping)
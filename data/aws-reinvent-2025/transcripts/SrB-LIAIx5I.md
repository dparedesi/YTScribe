---
video_id: SrB-LIAIx5I
video_url: https://www.youtube.com/watch?v=SrB-LIAIx5I
is_generated: False
is_translatable: True
---

- Awesome. My name is Anushri Mainthia. I am a principal product manager at AWS. - My name is Tyler Strand. I'm the Co-founder and CTO
of a startup called Air. - Morning. I am Nini. I am a senior product manager at Amazon Bedrock and
with my colleague Anushri. - And we're gonna talk to you about how to work with multimodal content and what type of multimodal
solutions that AWS has. Nini and Tyler will be helping
kind of share that story, but we're really excited
to have you all here today. So before we get started, I just, I wanna get a quick show of hands. How many of y'all deal with
some sort of multimodal content, images, video, documents,
just show of hands as part of your function? Awesome. What we're gonna do is
those, how many people with documents? Okay. Video and images, media content? Audio call centers, that kind
of thing, conversations? Okay. And how about all of them? And you have to figure out how to manage and deal with all of them. Got it. Awesome. It's a challenging problem. So what we're gonna do today, there's gonna be about
four things we're gonna do. First, we're gonna talk about what that multimodal content challenge is, and y'all are very familiar with it, given almost everyone in the audience is dealing with some sort of content. Then we're gonna talk
about what Amazon Bedrock data automation is and how it aims to solve and
resolve those challenges. Then Tyler from Air is gonna
tell us about their journey through how they manage
multimodal content. And finally, Nini will share a
few of the launches we've had and kind of what's new
and what's going on. So let's hop into the
multimodal content challenge. These numbers you're
probably familiar with, if you're reading the screen, you're probably experiencing deep pain when you think about these things. But one of the biggest problems is 80% of content is unstructured data. It's unstructured, multimodal content, whether it's in images
or documents or videos or audio files that you have. And for any process that you're
trying to build a solution for, say intelligent document
processing, you're gonna have to figure out how to get those
insights into a usable format to power your downstream applications. And unfortunately, only 20% of organizations right now are able to take advantage of that scale. Why is it particularly hard?
There's a couple of reasons. So one, there's an
incredibly large diversity of different types of multimodal content both across modalities. So for insurance claims,
you're dealing with documents, you're dealing with forms
that have been filled in. You're dealing with videos,
you're dealing with pictures of a car crash, for example. You're managing all those
different types of formats and files across modalities and even within modality. Within documents, a single
organization could be managing 300 different types of documents, all which require different schemas. Then you have the additional challenge of how are you gonna get the
accuracy you need at scale? And that's the biggest
challenge is you're not dealing with one document here or a video there. You're dealing with hundreds
of thousands, millions of these types of content that you need to process at scale efficiently. And so how do you get that
accuracy? It's a challenge. And how do you get that auditability so that way you can go
back and figure out exactly what is being used to generate insights, especially if they're gen AI derived. There's a lack of standardized
tooling, which means you have to learn multiple services,
multiple interfaces. And finally, and this is kind
of one of the most painful, I think the unsung heroes, is you have to put it all together. You have to do the transformations, you have to mesh all that data together. You guys know this in terms of it is, it is incredibly challenging to do that and it's time consuming and it's tedious. So what have we done to
try and help solve that and make it just a little bit easier? Well, hopefully a lot of you guys know what Bedrock Data Automation is. If you don't, I'll introduce it to you. So Bedrock Data Automation
is our way that we wanna help with multimodal content. Imagine a single API that
allows you to process images, documents, video and audio. And basically what you do is
you tell BDA what you want and we'll walk through how that works. And BDA does it for you. You don't have to figure
out the orchestration, you don't have to figure out
which FM you're gonna use. You don't have to figure out how to route things from
one place to the other. All you have is a single API. You can send any modality through it, specify the output you want,
and BDA generates it for you. In terms of what this means, it's simpler from an implementation
perspective, especially as you move towards more and
more multimodal use cases. In a previous era, you know,
you'd have documents run through one pipeline and videos
run through one pipeline. You can have them run
through a same pipeline now if the output is driving
the same business process. So that becomes much simpler 'cause you're interacting and you're creating that
integration with one service. BDA also allows you to tailor your output and allows that customization. So you're able to define your own schema. If you have a downstream
system, some sort of database that you have, these seven
columns, you can define those, you can specify your
normalizations transformations, all of that through BDA, and again, BDA just does it for you. And finally, BDA provides
things like confidence scores, grounding in the actual assets, whether it's exactly on the page and the page number where
in the conversation. So that way if you have something that's an inferred
insight, you know exactly what was used to derive that insight. If there are three inputs
used to calculate one thing, it'll show you exactly what that is. That allows you to have easier
humans in the loop reviews auditability to be able to more efficiently
create your applications. So what use cases can you use BDA for? 'cause an API is great but it's gonna power something, right? So there are five use cases that we see customers
typically using with BDA. The first is one that you would expect. Intelligent document processing and intelligent document search. These are things like insurance
claims, loan processing, anything where there's lots of documents and you need to process them quickly to generate extractions and insights. I'll hop to intelligent search analytics. Think call center analytics. It's not just the transcript, but what was the tone of this call? At what point was the customer unhappy? At what point did the agent convert this to a good customer call? Those types of things. If you can get those at
scale as opposed to having to post-process and
analyze that transcript, it becomes much easier. Media analysis and kind
of content discovery, that's another one. You have videos, say you're an ad agency and you have hundreds of videos and you're looking for
that one ad from 1984, that Christmas ad or that holiday ad, because you wanna create a series of all the most amazing holiday ads and you remember it had a penguin in it. How are you gonna get that? Well, imagine if you could
process all your content, get generalized output and also specific output so
that way you can search right for those assets. And we'll hear a little
bit more about that with Tyler's journey and Air. And finally, agentic workflows. You know, agents are things
that everyone is thinking about how they can use, how they can make their processes more efficient. If you think about BDA, think about BDA as the tool in agent calls. And now what you have is
you have a single tool that handles all multimodal content regardless of the modality. And you can set up your agentic workflows to use BDA as that tool. There's an MTP server available, you can use it today in this capacity. There's a few builder
workshops happening later, where you can kind of practice
and see how that happens. Okay, one API is great, but
how does that actually work? So essentially with
BDA, it's quite simple. As part of the API call,
you provide the asset. Along with that API call,
you provide two things. You basically provide a project, which is where you specify exactly what you want. In it you can include a schema, you can bring your own schema or you can choose from options and standard output
that we provide, right? For every modality, it'll
be slightly different because we've optimized it per modality. So for example, for documents,
you'll have the choice of do I want my output in
plain text, HTML, marked down because we know systems interpret and can perform differently. If you have a RAG system,
some perform better with HTML, some perform better with
markdown, you can choose that output, not just get plain text. For videos and audio
files, you can choose, do you want chapter summaries? What type of summarization do you want? Do you want to understand if there's content that should be moderated? You can kind of pick and toggle those. So there'll be a set of standard options where literally you just have to click. We've already have a default
project set up if you don't wanna make a choice, or you can provide your custom blueprint. And imagine your blueprint
is the schema you bring. You'll provide exactly what you want, what format you want it
in, and we'll do that. You send it to BDA, BDA figures it out. It says, "I wonder what asset this is. Let me figure that out." It's an image file, but it is actually a driver's
license, which is a document. So I'm gonna process it like a document. I see that they included a
blueprint for driver's licenses, so I'm gonna return all
the information they want. I'm also gonna give them
the linearized output of that driver's license so
that way they can ingest it and they always have
auditability back and that's it. And so that's how BDA works. I think it might be
helpful to see an example. Nini, do you have one handy
that you might be able to share? A little cheesy, but... - I think I just got the thing. It'll be good. And let's
do a little bit of a demo. So how familiar have
you guys watched TikToks and Instagrams recently? Like reels or anything like that? So you'll know that
there are actually a lot of sponsored content right? There are advertisements that's embedded in directly in the content of the video in short form. So I'm just gonna show you that video and just think about, you
know, if you are managing a lot of different media assets, a
lot of different short form content, long form content, et cetera, and you need to search for it, right? So that'll be the use case. I'm gonna pause there and
just show you the video. And the key here is just try to understand the context of the video. What are some ads maybe that
you kind of sort of spot and then I'll show you
how BDA works with it. - Had a break then to having
the baby while the baby naps. I'm gonna tidy up the house a little bit. It gets back, everything is clean. You feel at peace when she comes home. Yes, I come with my own supply. (wrapper rustling) I never really heard the words. I love you growing up and
I feel like it's a pretty synonymous experience among Asian culture. An adult, I've realized that sometimes I love use
isn't said it's served, which is why I'm making meals and cleaning as a host, as a guest has always been part of my DNA. I think it's a balancing act because sometimes I feel like
we lean too heavy on our words and forget to actually show up. (spray hissing) So I'm learning to say those
words out loud accompanying with my acts of service so
that my love could be heard and also felt. For me again, because culturally
it's just not practiced often, but the saying is what's hard, but I'm slowly getting there. Trying to break those generational habits, choosing both the full
plates, the affirmation, the clean house, the soft and hard to use, the acts of service, the language of presence. I just want people to know
my love in every form, what they see, what they
hear, what they feel. (dishes banging) And sometimes the loudest I
love use isn't just served. It's spoken. (dishes banging) (baby crying) No I don't want. Good news. Good news is mommy's bath. - You're toes look great. (baby crying) It's okay. - Proud you took some time
today, you deserved it. - All righty. So it was a video about
helping a mother take care of their kids, right
while the mother goes out to get her nails done. And I'm gonna bring you to the Bedrock Data Automation console and you can actually
get started super easy. You can go to try demo and
which we'll do in a second. We have some blueprints, there
are things called projects. And we also have a
sandbox where you can play with your RAG indexing, intelligent document processing,
media analysis, audio. You can literally just go and try it out. But let's start with the demo. And then what I'm gonna do
is upload that same video that you guys just saw from my computer and you just click choose file and then select the video and then go generate the results. And the key here is that
it will take some time, but I'm gonna show you
standard output first. And what is standard output? It's just a standard set of things that you can directly get out the box when you upload your video. And so sometimes your video
can be a little bit long, it can be even two hours, right? So what we have here is we
take the first five minutes and process that so that you know exactly what you're about to extract, right? And then you can extract longer because this can all
be done through an API. So I fast forward it a little bit. You'll see in standard output, these are some of the knobs. You got your summaries,
you can look at the text, you can look at IAB
taxonomies, content moderation. Here, I just chose the summaries, right? To just show like what are some of the rich summaries that you get? And remember we're talking
about a mother and her friend and her friend is taking care of the kid, while the mother is out. And so you'll see that
in the video summary. And this is, you know, a lot of things that we talk about like
postpartum, like how to, how to express love, right? Is all in that summary. You can see. Then you have what we call chapters. There's four chapters in this video and we just detected that outta the box. And these chapters,
think of them as scenes. These scenes, I'll
actually show you, right? So how do we even cut
up? Like what is a scene? So in the first 20 seconds
of the video is an intro. So I'll show you again when we've scrubbed to the first 20 seconds. Wait, so the woman here
introduces the context, right? And then it shifts to the bathroom. So from 20 second to one
minute and ten second mark, she's in the location
of the bathroom, right? And talking about the product and then it shifts over to a laundry room. And in each, in the bathroom and in the laundry room, she's
using the Blueland product, which is the embedded sponsored ad. And then the last one is
when the mother comes back. So this, we detect all these
key moments in short form right outta the box. Now one thing that I've kind
of noticed is, you know, where is all the logos, right? So what you can do is you can
just detect text in the video. As we see here, we have a
bounding box on a confidence score and it'll just detect that outta the box. And remember all of this you can still do with just the API as well. We have one unified API. Now I also wanna get the
text transcript, right, the audio transcript right out. And then I also want to get IAB taxonomy. So how do I do that?
Just click a few buttons. I'm gonna create a new project, which is where you store
these output configurations. In this case a standard
output configuration. And then I'm just gonna
call it my first project v1. And I'm gonna speed this
processing up a little bit. Usually it takes about a minute. And then, right, we're getting
the full audio transcript and then IAB taxonomies, right? So I'm gonna scroll down
a little bit, right? We talked about parenting, family, talked about a few other things, right? That you detect for your advertisers. And then here's a full audio transcript. We also have speaker detection. So in this case there was one speaker, but you can detect multiple speakers and then map that to the
person that you want. So that's pretty much standard output. You can play it with it
yourselves at some point and that gets you outta the box. But I actually want to go more specific. I actually don't like some of
the how verbose it was, right? I want to get more
concise, I want smart tags, I want better summaries, right? So what I can do is
create something called custom output, go to a blueprint. And I got started as simply
as just clicking add field. And for the first one, I
want my chapter summaries to be a lot more concise. I want the exact details, right? So I can say like, hey, let's do it for at least I think in this example, 30 words for example. But no more than a hundred words, right? And then I just specify
that with natural language. And then I want to get some chapter titles 'cause previously it was
chapter one, chapter two, chapter three, right? Very generic, I want
chapter titles, right? So I wanna specify how that looks like. And I say the granularity
is at the chapter level. And then I want to create
some smart tags, right? Like here are tags that are
easily searchable if I am, if I have a large media
content library, right? So I say like, these tags
have to be very precise. They contain some marketing terms, right? That allows me to search more easily. Then I want this at the video level. I don't want this at the scene level. I can do that too, but I
want this at the video level. And then finally, why don't
we just wrap it up with a, just a summary field, right? I want my summaries to be
a little bit more concise. I want them to be more,
not a lot of repetition. I want it right. And you can shape that
basically as a prompt. So these natural language
instructions for every field is how you would go about it. Great, so I've added everything and just, right, this
is called a blueprint and custom output and let's just call it the blueland_demo_v1. I'm gonna click get results, and then I'll fast forward
a little bit, right? It takes some time to process. But you'll see some of the results, right? This exactly is the schema that you just custom
built basically, right? And then some of the smart tags that we see here are
starting to just come out. You even have #blueland in the smart tags. And this is all, again, I did nothing special here other
than saying like gimme some smart tags and some natural
language instructions. With each of the chapters, you'll also notice that the
timing was exactly the same as in standard output. So it is deterministic. We won't give you like different
chapters all of a sudden. And then the other part is in
the chapter titles right now, they're more specific to the actual chapters
that we were talking about. And then we can look at the
different chapter summaries. Great, so I just walked
you through standard and custom output on blueprint
on Bedrock Data Automation. And so what did you have to do before to make this happen? So when I talked to
customers, they've said that, "Hey, like previously I had
to build my own MLP task specific models to, you know,
maybe detect these certain objects or and stitch multiple
models together, right, to make this work." So this is something you now no longer need to do with BDA. There's also, you know,
you have your videos, it contains both audio,
text and visual signals. There's a lot of things
that happen, right? When we were talking about, hey, like there was a scene in the bathroom and then in the laundry room, right? So before you could do
that with the visual model, but on the audio side you
might miss the context. So what BDA does is we actually synthesize that together outta the box. There's also just summarizing the content, I know that is becoming
easier and easier with LLMs, but you would have to just bolt that on and try to optimize that
price performance, right? And then there's also all
your different entities. There's detecting logos,
detecting objects, detecting people, detecting scene mood. So there's a lot of things
that you might want to detect as an entity in the actual video. And now this is something that you can do straight
outta the box as well. And then finally, even if
you've got this, you know, beautiful like stitch together
machine together, right? You gotta orchestrate everything,
you gotta maintain it, you gotta right there, there's gonna be different
models are gonna come up with new features. So you're gonna have to keep up with the API documentation
on how that works. And you're gonna have to keep balancing that price performance over time. Customers always want, right, they're gonna want better
costs, better accuracy, better performance, better latency. That is all something that you'll need to continuously balance. But with BDA, we manage
that for you out of the box. And so just, just a quick summary, right? The development times
of putting this together can take long, it can
take a couple of months, and there's also a lot of
maintenance that is required to keep this in shape. And then finally, there's
just a lot of knowledge and context that you
gotta keep up with, right? The world is moving so fast
these days that you'll have to, for every single new model or every single new feature that you're bolting on, you
have to keep up with that. So what I just showed
you in media also works for intelligent documents,
document processing. So here I have an application
package in my container bank statement W2s. So we take that and split that out and then we analyze each of those pieces. And as you saw you define
your, the type of output that you want, standard or custom. If you want some custom, same thing. You define your own schema and then process it through BDA. So just to kind of summarize
some of the key features. So number one, we have an intuitive system that allows you to just
define your output, right? What is the type of output you want? If you really want to keep
it simple, go to standard and keep it set up knobs
that you can select or you can bring and bring
your own schema, right? Bring your own and define it, right? And that can be done with natural language for each of those fields. The second part is the orchestration. So under the hood, we have
our own task specific models that we pre optimized. We have FMs under the
hood that are running and that we're constantly updating. So these are things that we
are managing on your behalf now and making sure that it has the best price performance balance. Then we have all the great stuff of AWS kind of baked in already. So KMS keys, private cloud,
and also responsible AI. We wanna make sure that
a lot of the content that's being outputted
actually has some confidence and grounding that you have. So we have confidence scores in what you saw with the bounding box. We actually ground it in the image, and we also have toxic content detection right outta the box as well. We're also integrated into
the set of AWS services in bedrock as well. So for example, with your knowledge base, if you're gonna put in a lot of your documents into your
knowledge base, you can use BDA for example, as a parser
to parse that content when you want it to build it
for your RAG applications. And then finally it is a single API, like all of this I just
showed you was on the console, just so you can visualize, right? Like media is a very visual modality, so you can kind of see what's happening. But all of this at the
end of the day can be done and should be done
actually through the API. Now there are other AI services in AWS that serves very specific
use cases in IDP, in image analysis, in
conversational analytics. And so for example, if
you want in documents, if you want to extract, you know, just extract the linearized
text, get the full blob of text out, then that's,
that's going, you know, Textract is kind of your way to go. If you're looking for
image analysis, right, you have a lot of different things. We can detect live if people
are live in the image or not. So that's something that's
best done with recognition. And then if you just want
a great price performance audio to speech model, an ASR
model, then use Transcribe. And actually to really help with this, I'd actually like to play a game. And the game is this. I'm
gonna define the use cases. I'm gonna give you some
of the customer needs and then you can just
tell me which AWS service would best solve this need. So you can just shout out the answer, but of course I will tell you the answer. So for the first one, right, if you want video
understanding multimodal, you want latency maybe in minutes and you want a high
degree of customization, and you have to take
multiple, like audio, text, visual inputs, what is a service that would best work for this use case? I hear BDA, okay, this is BDA, exactly. That should be the easy
one to kick off with. Suppose you want to just
stream transcription, you want really low latent
transcription from audio to text. You want a high accuracy, not too much customization going on. And at the end of the
day it's audio based, which service would you like to use? Anybody? Okay, alright. It's Transcribe, that
would be the best one to use for that particular use case. Now, if you have, if
you are detecting faces, if this is a live face, right, and you're trying to analyze
that image, this has to be pretty accurate at millisecond latency, and then it is complete image based, what would be the service to use? Okay, recognition, that's good. Insurance claims processing you want, you're okay with some minutes. There are a lot of contextual details in the claims processing, you
want to customize it a lot and generally you want some high accuracy, which service would you use? So actually this one is
BDA, this is, you can use, you can do all that now with BDA. And if you just want
in a piece of document to just get the blob of text out, right? You wanna extract everything
out, you want just basic OCR and you want it very quickly at low latency, right? Which service would you use? Textract. All right, nice. So I love to welcome Tyler onto stage here to talk a little bit
more about his journey with AWS and Air. - Thank you Nini. Good morning. First of all, thank you all for kicking off your re:Invent
journey with us bright and early at 8:30 AM on Monday morning. I appreciate the full house here. My name is Tyler, I am the co-founder and CTO of a company called Air, which I'll tell you all
about in a second here. And we've been building on top of BDA for the last six months or so, and it's really changed
the way we think about multimodal intelligence
and information extraction. To give you a little bit of
background on what we do at Air, we are what we call a
creative operations platform. That essentially means we
help businesses manage all of their creative files and the work around them,
images, videos, documents, whatever it is that they're working with. We manage about eight petabytes of data across all of our customers today. Hundreds of millions of individual assets. We work with about 100,000
creative professionals, day-to-day spread across
2,500 plus businesses. These are businesses like Sweet
Green and NBCU and JP Morgan and Graza, the olive oil company
you might be familiar with. And so really wide set
of use cases, a wide set of content types and file types. And we're really interested
in providing rich experiences on top of that data set. We think about our
product in two core ways. Asset management is the first. This is stuff you're used to
getting from a cloud storage provider, it's storage, it's
organization, it's search, all of which is made much more efficient with multimodal intelligent extraction. And we also think a lot
about the creative work that happens on top of
that content library. Things like giving feedback, making edits, and sharing content externally
when it's ready to go. To make this a little more real, I'm gonna give you a
quick customer case study. How many of you're familiar
with The Infatuation? Maybe you use them to look
up a restaurant out here in Las Vegas this week. They started in New York City, but today they operate in
cities around the globe, and they manage about 25 terabytes of creative content with Air. We've been working with them since 2019 and a lot of the technologies that we use and the services that we provide have advanced over those years. But we've powered creative
operations for The Infatuation for five plus years. They have about 150 teammates
spread across the globe. Photographers, editors,
designers, creative directors, and by their estimates, Air is saving them about
four hours a week for folks who are embedded in that creative work because of the functionality
that we provide on top of their content library. We are an AWS shop through and through. We've been building with
AWS since the beginning of our business in 2017. We use S3 to store and secure the original
files that get uploaded to our system and we use
a slew of AWS services to process that media. We transcode every file into
a lightweight, you know, web friendly copy for day-to-day
use downsizing images, transcribing videos, converting documents to PDFs for rendering. And we also for a long time
have extracted information out of those files in order to provide end user experiences on top,
like search, like tagging, like organization, reducing manual effort on behalf of our customers. But this has always been
one of the big challenges of our business. Extracting, you know,
AI powered information from a large data set can be really hard, especially when we were first getting started as a company. Each file type has its specific nuances. There are different services or tools or ways that you think about extracting information from
an image versus a video versus a document versus something else. The metadata that we get back
from those services can often be fragmented or inconsistent, and you have to maintain a
fairly complex orchestration system around each of
those specific modalities. So you can see on the
image on the right here for each content type that gets uploaded, we were processing the
file with, you know, AWS compute resources and then sending it to, you know, specific enrichment
providers, either on AWS or external third party vendors. So, you know, at the beginning
of this year, we set out to rethink the way that we'd
architected this solution and we wanted a solution that was simple, simpler to maintain, easier
to scale, really secure. This is obviously, you know, of the utmost importance to our customers. They want to know that the
content that they upload to Air is safe. It's not being, you know, shared
with folks unintentionally or sold to third party data providers. And we needed it to be cost effective. You know, eight petabytes of media, hundreds of millions of files. We wanna be able to do this type of AI enrichment at scale
without breaking the bank. So we went out and ran a search to try to find the right solution
to solve this problem. And we wound up landing on
Bedrock Data Automation BDA. It checked all the boxes
that we were looking for. And then some, and I'll
tell you a little bit about how it fit our use case
specifically as we go here. But first of all, the simplicity I think
was the big winner for us. Rather than maintaining those
individual fragmented media pipelines for each type of
content we were working with, we had a unified API for all modalities, it was also one shot. So if we had a file and we wanted to get, you know, 10 different pieces of information back about
it, we could ask all of that in one go and wait for
an asynchronous notification to come back saying that
the media had been processed and all the metadata
that we needed was there. And as Nini mentioned, it also abstracted away
model selection from us, which was really massive as you all know, this stuff is changing really quickly. It feels like every week
there's a new advancement or change in the right
model for the right job. And for us, we wanted to stay sort of one degree removed from that and focus on building end user
experiences for our customers and not chasing the best model of the day. By being an AWS product, it was intrinsically more secure for us. We were able to manage all
of this data in the transfer between services all within
our VPC, hosted on AWS so we could be confident that
the data would never leave our infrastructure and
it was cost effective. You know, as we ramped
up the amount of media that we were processing
with BDA, the economies of scale made sense for us and we were able to provide
this to just about all of our customers without increasing cost. Keeping data transfer between
AWS products also meant that that line item remained
free as opposed to sending it to an external vendor and
paying data transfer fees. A few of the other benefits, you know, that we weren't necessarily looking for when we kicked off our search, but really stood out. There's tremendous range
of file support with BDA, so we didn't have to do a lot
of pre-processing to convert input files into, you
know, an output format that BDA could accept. The custom blueprints,
which I'll show in a demo in a sec here were massive for us to be able to maintain a
consistency of user experience. You know, we wanted the metadata to come back in a certain shape or a certain way that was
consistent with our product and a few other, you know, benefits that really made BDA the
standout solution for us. So I'm gonna play a little demo video here to give you a sense of what
this looks like in our product. So to start, we just drop in a file. This is the Air UI, the file uploads to S3 in the matter of seconds and that now kicks off a series of asynchronous jobs in the background. The first thing we do
is process the media. We produce little previews, the scrubbable preview you just saw and then we transcode
the video for playback. You'll see on the right side there, we're now processing some
of the smart metadata. We use BDA to generate smart
summaries of every asset as well as smart tags. And these are customized and controlled to subscribe to a format that we want in our product. We use chapterization to
pull out chapter titles and summaries and
transcription of the audio in the file as well. So three or four different
types of extraction happening here and all of that powers a really simple search experience. You're able to type in
a natural language query and find the file and
even the moment within that file that you're looking for. So all powered by BDA under the hood and the output formats that
we see here are customized to meet the experience
that we're looking for. To give you a little
peek under the hood of what implementation looked like for us when we were putting this together, it really is as simple as
a single API call to BDA to create a new job. We passed it a reference to the
S3 object that we're looking to process and then a reference to the custom blueprints we want to use for this job. So those are the things that
are defined in the BDA console that Nini demoed earlier
where you can specify the format or the schema or the structure of
information that you want back. We kick off that job and then we wait, we subscribe to an
EventBridge notification. When the job is finished processing, we receive a notification and then write the metadata
wherever we need to write it. So super simple to kick off a job and then receive metadata back. And I know this is
getting even simpler now as the BDA team moves
to synchronous API calls for certain modalities as well. We've now deployed this offering across all of our customers. So you know, about 2,500
paid customers are now using these services as well as many
of our free customers too. And it's been a massive win
for both our engineering team who no longer has to manage the
complexity of the, you know, fragmented pipelines across each modality. But it's also been a
win for our customers. The graph on the right side
here shows the number of jobs that are waiting to be picked up and processed in order to be enriched or to have metadata extracted and then appear in search results and see those summaries,
those chapters in the UI, the number of waiting jobs
has dropped to next to nothing because BDA is able to
support the scale of uploads that we see at Air. We regularly see hundreds of thousands of new files uploaded in a day, sometimes millions when
we're onboarding a large new customer and we're able to
churn through processing that media very, very quickly. Since launching with BDA
a couple of months ago, we've processed about 15
and a half million jobs and at any given moment
we typically see about 160 approaching 200 running at a time. Most of them finish very
fast, obviously, you know, dependent on the type of
file that you're processing or the size of the file, but you know, for our use
cases this has been completely adequate to provide the
type of customer experience that we're looking for. I do also want to call
out that this has been a big team effort between
my engineering team at Air and the folks on the
BDA team at AWS as well. Gaurav is our account manager, and he highlighted the sort
of degree of collaboration that we saw with this effort, which was pretty special. Every day you know, we were
in Slack together, you know, incorporating their service
into our product, finding bugs and reporting them, having
them fix them, you know, within hours or a day, and, you know, just the
near real time collaboration here was an absolute win. And I think personally something that surprised me when working
with a company as large as AWS to see their
ability to remain nimble and work with, you know, an early growing startup like Air was really, really impressive. I think this is hopefully
just the beginning of our partnership with BDA and our multimodal journey as well to give you some insight
into some of the stuff that we're thinking about next. The first we've actually already launched, which is we're now taking all the metadata that we get back from BDA and creating vector embeddings of it to power a semantic search experience. You saw this briefly in
the demo video we played, but you can just talk
to Air search, you know, in plain text or plain language
like you would a coworker. We create an embedding for that query and compare it to the
embedding of the metadata that we get back from BDA for each of the files in your workspace. And that has been super
easy to stand up on top of this multimodal infrastructure that we've just talked about. We're excited to switch over
to synchronous data processing for some of our modalities
like images as well, which will speed up processing time and reduce complexity even further. We are still in the
process of consolidating some of our use cases over to BDA as well. So video transcription, which
we saw in the product demo is moving over to BDA shortly here too. One that I'm particularly
excited about is exposing those custom blueprints to our end customers. You know, we've gone ahead
and set up requirements and said, "Hey, we'd
like to keep summaries, you know, less than 50 words or we want, you know, 10 to 15 smart tags when you process an image." But you could imagine giving those keys to the customer themselves and saying, how would you
like to understand the content that you're uploading to our product? And this is something
that we're considering as a potential enterprise
offering on top of our AI infrastructure,
continuing to scale this out to multiple regions to improve latency and reduce complexity. And I'm sure continuing to
collaborate really tightly with the BDA team as
we do all of the above. So hopefully this provides a
little bit of insight for all of you as you think about
how you might approach some of these challenges at your companies or your use cases. But yeah, looking back
over the last six months, I think we've been really
pleased with how easy it was to get all this functionality stood up and deployed across a really
massive set of files across, you know, thousands of customers and excited for what's to come next. So thank you so much. (audience applauding) Got a few more? - Thank you Tyler. And it has really been
a great collaboration. I know we've been working
so closely together and it's funny, yesterday
night we were trying to get one of these demo videos up, and I'm like, "Tyler,
like I need this video." So it's actually been a very,
very close collaboration. I wanna talk about what's
new and what's coming up. So it's funny Tyler, that you mention
synchronous image processing 'cause that's actually something
just launched last week, and so I'll go over each
of the different modalities and some of the new stuff
that were coming up. So for documents, we've
expanded across five different languages now and that's
gonna be coming up as well for the other modalities. We've also added new file
format support on documents. On video and images, on media in general. We've increased the image
processing speed by about a half and then the synchronous
API processing allows you to take your assets, right, put it in and then you immediately
get a result at return. And that also helps you,
especially with a lot of more responsive use
cases maybe for mobile, sync API will allow you
to do that bit better. Also added a bunch more different formats, AVI, MVK, et cetera, so that you can actually go
across the spectrum of your different assets and
file formats and codecs and just natively process
without having to reconvert or take up any jobs to do it like that. On the speech side, so on the audio side we
have channel identification and that allows you to also, you know, detect those multiple speakers. I think earlier in the
demo we showed one speaker, but you'll be able to detect multiple and then that speaker diarization is along the same idea, right? That for turns of the
conversation, you want to be able to tag those different
speakers that are talking. And then we're gonna expand it to all the major languages and more. There are also a few other
things I just want to kind of preview with you guys. So number one for documents. We understand that accuracy
is actually a very big, big thing to unlock production, right? You want to get something
past like 90% accuracy. So we are gonna launch
something that allows you to take your documents,
label them with ground truth, and then optimize your blueprint, so that you can achieve greater
accuracy during runtime. There's also something
that we're gonna launch in terms of entities. So we understand that hey,
if you talk about different pronunciations right of words, sometimes they may show up differently in the transcript. So we're gonna launch something
that allows you to define what are the correct
pronunciations so that we'll detect that in your transcript in audio. And then finally, I talked
about entities before and we will allow you to
actually detect the entities that you wanna detect,
any recognized people that you know would be
pretty much impossible in public domain knowledge. And that is something that
you can bring in terms of your own images of people
that you wanna recognize and then supply that to BDA, so that we'll detect
it out the box for you. And then just one final thing, we are gonna expand the number of AWS regions we're gonna cover. So we're gonna be able to double that to 15 plus regions by
the end of this year. So stay tuned, we got a
lot of exciting updates that are gonna be coming up soon. Thank you so much. I'm also gonna suggest if you
want to, you know, take any of these resources, go
ahead and one final tidbit. We actually have a builder
session today at the Win. It's at the Promenade
Lafayette 9 at 1:00 PM. Lafayette 9 at 1:00 PM. Feel free to join us there and we have a few more
minutes so we'll be off stage. Feel free to talk to us and happy to share some
additional thoughts. Thank you so much. (audience applauding)
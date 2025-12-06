---
video_id: 168mGOX6LnE
video_url: https://www.youtube.com/watch?v=168mGOX6LnE
is_generated: False
is_translatable: True
---

- [Gunnar] Good morning everyone. Welcome to DEV309. My name is Gunnar Grosch, I'm
a developer advocate at AWS. Excited to see so many of
you already Monday morning. - [Shridhar] Hello everyone.
I'm Shridhar Pandey. I'm a principal product manager and I lead developer
experience for serverless. Happy Monday morning
and happy re:Inventing. - [Gunnar] All right,
so this is a code talk where we are gonna look
at how we can make use of AI coding assistance, specifically when we are working with serverless applications. And kinda what we're expecting is that perhaps you haven't
used AI assistance that much for that use, but maybe many of you at least know things about serverless. Maybe, we'll see. So in this next hour, we're gonna walk through how
we can use these types of tools to build serverless applications. And we're gonna build both front and back end with the
help of an AI assistant. And then since this is a
code talk, it is interactive, so if you have questions, we'll
try to answer those as well. But we do have some things we wanna make sure to get through. So we'll try to power through as well. - [Shridhar] All right, before
we dive into the details and the session, let's level set on what developer experience
means for serverless. You can think of it as two distinct, but interconnected loops, the inner loop and the outer loop. The inner loop is where you'd likely spend most of your time on your
local development environment. It's all about rapid iterations. You know, write code, test
locally, debug and repeat. The goal here is fast feedback cycles. On the other hand, the outer
loop begins when you push code from your device to production or staging or integration testing environment. It includes CICD pipelines,
staging, deployment, testing, production monitoring and so on. The cycles are less frequent
but much more high stakes. The outer loop involves team
collaboration and coordination. And this is where works on
my machine meets reality. - [Gunnar] Alright, so the
AI assistant we're gonna use for this is Kiro CLI, the artist formerly known as
Amazon Queue developer CLI rebranded a couple of weeks ago. So Kiro CLI is a CLI, a tool that we can use within our terminal and that then have access
to large language models. It has access to adding
capabilities through MCP servers. It allows you to do a lot of the things many of us as developers
do through the CLI, but with the help of an AI assistant. So that is the tool we'll be using. And we will be using it within an ID, but you can also run it
just in any terminal window as you want as well. So with that, I think we've
set the baseline pretty much. So let's look at what we're
gonna build in this session. Alright. - [Shridhar] Alright, so we'll build a simple
image generator application. At the core of this
application, the back end, is an API that calls Lambda function, which is written in Node.js. The Lambda function then
calls a Bedrock model to generate the image. In this case we will use the
Titan Image Generator v2 model and we will use S3 for persistence. We'll also add a front end to this app, which will be built on React with Vite and deployed with Amplify Hosting. And lastly, we'll set up
observability for this application with CloudWatch application signals X-ray and use Power Tools for structured logging and to gather additional insights. And we'll also use CloudWatch Live Tail for real time debugging
if the need arises. - [Gunnar] I think we'll
skip over it, right. Alright, so time to get building and I'll be doing the
building from down here. And this what we see right
now on screen is the Kiro ID. Kiro is an ID that has AI capabilities, but like I said, we're
gonna use the Kiro CLI, this is just my preferred ID. You could use the visual studio code, you could use whatever ID
you want with the Kiro CLI. So the first thing I want to show is kind of what we can do
with the help of Kiro CLI. What we have so far in
our project is basically just empty folders, but what I have done just to save some time, is
to create our front end, just a clean install of Vite with React. So it kind of just
looks like this for now. We all know that installing everything through MPM takes a while,
so just saving us some time. Alright, so right now we have my terminal. We can open up Kiro CLI. That is then gonna load and let's see what we have here. So what you can see
straight away is that I have a number of MCP servers that
I've added to my configuration. All of these are now
in the disabled state. The CLI or the MCP servers that we have, I'm using a bunch of
different ones from AWS. You can obviously add
any type of MCP server that helps with your workflow. I wanna show just kind of how this differs when we start adding these MCP servers. So you can see kind of
how that enables you to be more powerful I'd say
with the help of these tools. So what I wanna do just to begin with is to tell my Kiro to just create a
serverless application now. I'm gonna copy paste prompts. You don't have to see
me writing everything, but right now I've opened it. I can start chatting with Kiro. It's using different
models behind the scenes. As you can see here with
Kiro you have access to Claude Sonnet 4.5, Claude Sonnet 4, Claude Haiku 4.5. And you can choose which
model you want to use. And as always with these
large language models, they're good at different things. So depending on what you are doing, you can either pick a specific one or stay in that auto mode. I'm gonna stay in auto for now, meaning that it will select
itself which model to use. But now I can then start
asking it just like any LLM. But what Kiro CLI is able
to do is that it has access to my file system so it can actually start doing things for me. So the first thing I wanna do now, with MCP servers disabled, I wanna tell it to
create a new SAM project, SAM, service application model, the way we can with
infrastructure as code, easily build serverless applications. I wanna have Node.js 22, an HTTP API and two Lambda functions. So this is basically the architecture that we looked at before. Let me just add, create
it in the back end folder. So what's gonna happen now is that Kiro is gonna
use the knowledge it has in that large language model and it's then gonna start doing things. And it now suggests that
it's gonna run this. It's gonna do a bunch of commands, create a file or a folder. It's gonna go into that folder, it's gonna run the sam init, meaning that it's using the sam CLI to create this application. But basically it's rounding a
bunch of CLI commands for me so I can press yes and
allow it to do this. So that's cool. It means that based on that model, it has a lot of knowledge that it can use basically from the documentation probably that it's trained on. But what these MCP servers allows us to do is add additional capabilities through different types of tools. And the first one that
we wanna make use of, so I'm not gonna run this command now because I don't want
it to actually do this, so I'm gonna cancel. There we go. And then I'm gonna enable
my MCP servers instead. So first one is AWS serverless. Maybe you can explain
a bit what that one is. - [Shridhar] Yeah, so the
AWS serverless MCP server, which we launched earlier in the year, it's an open source MCP server. And the idea was to combine the power of AI-assisted coding with the serverless expertise to help you throughout
the entire life cycle of your serverless application
development journey. So talk about best practices deployment as Gunnar will just show us
how it picks the right tools and guides us through the right
deployment model and so on. And it goes all the way
through to operations such as monitoring, looking at metrics and suggesting what could be going wrong with the application or what
could be improved and so on. Then we went ahead, went a step further and last month we added
specialized MCP ESM, event source mapping
tools to the MCP server to guide you through selecting
the right configuration for your event sources and troubleshooting if
something were to go wrong. - [Gunnar] So these additional
tools means that instead of just relying on the model's knowledge that it's been trained on, it can actually do very specific things. So now I've enabled those. I also enabled one specific
for AWS documentation, meaning that it has knowledge from all of the AWS documentation. There's also ones with AWS knowledge, MCP server contains additional information and tools that it can use. I also have one for front end
that we'll make use of later. All of these, the information
and how to find them will be shared in the
resources at the end as well. So you'll be able to get that there. So what we can do now is we can check. Slash MCP. Let's see. Oh now it... Ah. There we go. Let me restart it. Kiro CLI. So now it has access to those MCP and we're gonna basically try
again and see what it says. List the available serverless tools. So let's see what it says. So now we can see that
well these are the type of tools that it can do. So for instance, we saw before that it wanted to run
sam init as a command. Well now I can see that
it has access to sam init as a tool instead to be able to do this, and a bunch of other ones as well. So now with that, well we can then try to create this project again. So let me paste a prompt. Once again, create a new SAM project, create in the back end folder. I want it to create that project. Both of the Lambda
functions should now return just hard code adjacent to begin with, since we're not connecting it to Bedrock just yet. I wanted to run sam build as well, which is another tool to
actually build the project. We wanna run sam validate to make sure that everything works as expected. I also tell it to create a change log. And this is something that
I use with AI assistance. So for everything I do to keep track, I always keep a change log. So everything it does basically
ends up in a markdown file for me to be able to review afterwards. So let's try this again
and see what happens. So now it says they will do this and you can see the difference here. So instead of saying
just a long CLI command, it now says that it's gonna
run the sam init tool for us. It's gonna create an image generator with Node.js 22 and so on. So now I can say that I want to run this. Let's say that we're
gonna trust it to run. There we go. So now Kiro is gonna run the tool for us. 65,000 attendees running
Kiro at the same time. So I have to give it a few minutes. Okay, so now it's running.
Oh it failed to validate. Let's see. There we go. And what what I think
is pretty cool with Kiro is if something fails, well then it looks at that error message and tries to adjust itself
so I don't have to try to find what error it was, what happened. It's instead gonna do that itself. So here we go. So now it's generating this. So it generated our initial back end as we can see basically a hello world example using sam init, and now it's gonna start adjusting it based on what we needed, our tool endpoints for instance and so on. So once again, I'm gonna trust
it to make these changes. It's now updating the template. And trust it once again. The first few times
we're rounding commands. It's always gonna ask
you if you want to trust for this session or if you want to just say yes or no every time. Alright, so it's creating
my initial Lambda handlers with just static JSON to begin with. It's creating a package
JSON for what we need. So now through that simple prompt with the help of those tools from MCP, it's able to start creating
everything I wanted it to do. There we go. You can see that it's still
using the serverless MCP server, now it's a sam build command and now it's doing sam validate with lint. It's now gonna create a
change log for me as well. Here we go. So keeping that change log, I think that's usually for me a
great way to keep track of what's happening within my projects. Since these AI tools, they're
able to do a lot of things. So keeping track of exactly
what it's doing can be hard through just the CLI. It's also doing some
initializing a Git repo for me and here we go. Alright, so now it's done all of that through that simple prompt. Created a new project, created an HTTP API,
implemented two endpoints with Lambda functions
and it's run sam build and sam validate. So now it's basically ready for us to be able to deploy this. - [Shridhar] And if you did
not want to do even that, the MCP server has access
to a well curated library of patterns through Serverless Land. So you could have just started with that. "Hey get me Serverless Land
that has an API gateway connected to a Lambda function." And it would've gotten you that as well. So you have options here. - [Gunnar] Yep. Alright, so now we have that done, we can basically go ahead and deploy this first
version of our application and then fingers crossed it might work. So I'm gonna open a new terminal. I could tell Kiro to
actually do the deployment but I'm gonna do it manually in this case. So let's go into the back end and let's run a sam deploy and guide it. So this is gonna be my
first deployment. Oops. Oh sorry. There we go. Something's outdated. Let's call it image generate December 1st today, right? US West 2 sounds good. Confirm changes, no. Create roles, disable rollback. We don't have any
authentication to begin with, which is fine in this case. Here we go. So now it's gonna start
deploying this for us. And as soon as this deployment
is done, it's gonna take a couple of minutes usually
through cloud formation, then we can basically try it out. And the normal way to do this is, I'm sure most of us would,
we look at the output, we get the API endpoint,
we test it through postman or through curl or something. But this is another way where
I usually use the AI assistant to help me with this. And you can do it in multiple ways. It can help you find
the resources for you. So instead of me having to
find the correct API endpoint, I can tell the CLI to do that for me. I can also then tell it to actually test and make sure that the output is correct. So here we go. So it's now deployed and we can see we have the API endpoint. So yes I could use curl. I never remember the exact curl commands. Honestly I've been doing
development for 25 years now I have to Google it every time. - You're not alone.
- No. So this helps me so much. Alright so now let's try it out then. So I have my test prompt. Get the API endpoint from
the cloud formation stack. This is why I shouldn't
change it. The stack name. Alright. Rookie mistake. Imagegen-API. That's not at all what I called it. What did I call it? Let's see if you can find it
without even mentioning it. Here we go. So I'm telling it to get the API endpoint. Now it wants to deploy. It's already deployed. There we go. So now it's gonna try to get that. Nope, that's not the correct name. So now it needs to find-
- Had a December 1 in it. - [Gunnar] I know. So let's see if it can. So now it's gonna list,
let's see if we can find it. This was on purpose. There we go. That is not correct. Oh! That is not correct. It has a different name. Let's see, what was the name? December 1st?
- Yep. - [Gunnar] Okay, I trust
Kiro. There we go, yay. Okay, so now it's gonna get that for me. Now it has the API endpoint. Now it's gonna test it and as you can see it's
basically using curl. But yeah it knows the
command that I don't. Both endpoints are working,
these are the results. So that's very cool. We're able to then
start testing the things we deploy straight away
just by prompting it again. So at that point I think we can go on to the next part of the architecture. And what I didn't say before is that what I tend to do
when I build these types of applications, specifically
with AI assistant, but I kind of do it otherwise as well, is to break down the architecture
and do it step-by-step. So that's what we did now, we created the API and the
initial Lambda functions, then we start adding the next parts of it and the next part in this case could be the S3 bucket for instance. So let's do that. Let's do the prompt. Add an S3 bucket to the SAM template, update POST generate to
create a placeholder object and then update GET/ images to list the 25 most recent objects
and return pre-signed URLs. And that's gonna be
important in our architecture because we wanted to generate images and then we want to be able
to actually view the images without making this entire bucket public because that's a big no-no. Least-privilege IAM for
S3. Rebuild and redeploy. So let's see if it's then able
to actually do those commands as well and update the change log. So here we go. Add S3 bucket, update Lambda functions. And the thing is that
I'm not gonna prompt it to use tools or not use tools. That's gonna be up to Kiro in this case. So the way those tools are built, they basically have capabilities and when it's kind of matching something that I tell it to do, it's
gonna pick to use a tool. Other times it's just
gonna use the knowledge that it has in the training data from the large language model. Alright, so now it's
doing a bunch of stuff. We can see in the code it's creating pre-signed URLs for instance, it's updating our package. There we go. And now it's gonna do
the sam build tool again, it's running it hopefully. So we can see these are
our Lambda functions and the code for it. We haven't written a single line of code but I think it's so far looking like it's generating exactly what we need. I'm gonna allow it to run sam deploy. So that's a tool we didn't use before since I did it manually. But now it's deciding that
it's gonna use that tool. I trust it. So from here on out it's gonna be able to do these deployments by itself. Alright, so Kiro is hard at work. And the next thing then, well same thing. We're gonna test this out to
see that it actually works. Sure it's running. What do you think? Is it doing something? - [Shridhar] Yeah, it looks like it. - [Gunnar] Yes. - [Shridhar] Sometimes you've
gotta let it do its thing and not let your instinct
take over and like start. - [Gunnar] I know. All right. But hopefully it's deploying. I guess we can check that
in cloud formation, right? See if something is happening. Yeah, updating progress. It's just not showing
the output at the moment. - [Shridhar] Is the S3 object and stuff already showing there? I can't see very well from here so. - [Gunnar] Oh yeah. Let's see. Resources, the functions. Yeah, it's created a bucket for us now.
- Nice. - [Gunnar] Yeah and update complete now. So let's see. Now it's updating the
change log for us as well so we can see that these
are the things it's done. Alright, so now that's done. So we can test this out as well. So let me just make sure that I'm not gonna trick it
with the wrong stack name again. Where is my stack name? There we go. Okay, so let's try this out and then when we've tested that, I'm gonna show something
else that's super useful when using these tools. So now it's hopefully
gonna test that as well to generate an image. So far we're only
generating a test text file and now it's testing the
output to get the images and as we can see it's
getting the ID of the file and it's getting a pre-assigned
URL that it's able to fetch. So yeah, that works as well. - Nice.
- We've gotten that far. I want to show something
that I try to use quite a lot that's helpful when using these tools. With Kiro you can create
what's called steering files. So I'm doing this now in the Kiro ID. What's pretty cool is that Kiro ID and Kiro CLI, they're
sharing certain things. For instance, the MCV server configuration is shared between those two. The steering files is the same thing. And steering files is basically a way to control the behavior of these AI tools. So I have a global steering
file that I use for Kiro that basically tells it what it should do. If you are an AI assistant, you must follow these rules
just to make it very clear. But then I have kind of my workflow, what it's supposed to do. Always make sure to update read me or design documents when it make changes. Do not create additional
markdown files in repository unless you're instructed
explicitly to do that. Something that keeps
happening with these tools is that it wants to always
create markdown files to explain everything. So by adding that little
line, I'm able to stop it too. I've also told it that it should
use commit when it needs to and kind of my rules for
when I think it should. I also tell it how to do commit messages. Bit about unit tests. I don't want it to have big unit tests, it should be very small
pieces of functionality. And then I have some things
around code style for instance, how it should name functionality, how it should do documentation. I want to follow JSDoc for instance. Testing standards, security essentials. This one is good, never commit secrets, and so on and so on. So this is basically
how I can control Kiro. And these are, like I said,
these are my global steering. So it uses this all the time. What I can do as well is to
create additional steering files and once again I'm doing it in the ID now, but these are just files
in the file system. So if I don't use Kiro ID, it's just files that I store there. So I can create an additional one, either a global one like we had, or I can create specific
ones for this workspace and they're just stored
in the .kiro folder for my workspace in that case. - [Shridhar] What happens if
so, which one takes precedence? So if it has a global steering file and then it has a workspace one, it's gonna use the workspace steering. So for instance, if I have
a global steering file that says "Always use Java" and then I have in my specific
workspace steering document that I want to use Node.js, well then it's gonna go with Node.js because that's for
specifically that project. So we can create a new one. Project steering, there we go. And then just start
adding my rules into that. I just had, let's see. - [Shridhar] So it basically serves a bunch of purposes, right? You can use it as
guardrails, you can use it as sort of augmentation
of the tool itself. - [Gunnar] Yep, exactly. So let me just add, probably should have done
this earlier, but it's fine. We control it through our prompt instead. But for instance, for my project, well I wanted to use US west 2 and that could be
specifically for that project. How I want the structure to be, back end front end directories, that it should use the template YAML, that I want to use Node.js. The full timer should be 30 seconds. So then by adding these, I
don't have to prompt everything. It's gonna look at the project
steering for it as well. So I can save this and now it's always gonna
have that as context with everything that I prompt it to do. So I think that's a very
useful thing to have when working with this and
especially then if you want to control the output of what
you're actually building. Alright, so let's get back to
what we're actually building. So now we've created the API,
the two Lambda functions. We're just doing a text files for now and then we're storing
those in an S3 bucket and we're able to return
with a pre-signed URL to be able to fetch the images. So, so far so good. I guess the next step then is
to add Bedrock into the mix. - [Shridhar] The actual
image generation part. Yeah? - [Gunnar] Yes, so that one is a bit longer prompt, telling it to replace the
placeholder generation to use a Titan image
generator 2 on Bedrock, I got the model ID, we
could leave that blank, then it will probably have to
start searching to find it. So it'll save us probably
a couple of minutes, but it would then start looking up through the APIs basically
what model to actually use. Use the correct request format,
generate a PNG from prompt, store it in S3 under images,
return the object key. I'm telling it to add
an environment variable so we can bypass Bedrock
when we're doing testing for instance, we don't
have to call it every time. IM should be least privileged
for Bedrock and S3. We want a bit longer Lambda timeout for image generation. So in this case this is gonna go against what I have in my project
steering, where I had 30 seconds, and in that case, well it's gonna go with what I say in the prompt instead. - [Shridhar] And I
think one quick call out or a pro tip here is don't
be shy with your prompts. Like if you wanted to do a certain thing, I personally have this instinct of trying to get the prompt out and just get going. But take your time, think through it. The more specific and clear you are, the better it will do for you. You're just saving yourself
some time for the next step. - [Gunnar] Yep. Alright, so now it's just gonna, in similar way it's
gonna update our template to be able to add the
infrastructure needed. And in this case, since it's
Lambda who's calling Bedrock, it's basically about adding
the correct permissions to be able to call Bedrock. But then it needs to
update the package files to be able to use Bedrock runtime as well. That was pretty quick. Yeah, here we go. This is the Lambda function. So it's added what's
needed to generate an image and now it's running sam build again. And then it's gonna do
sam deploy hopefully at the end as well. Here we go. Trust. There, and as soon as that's done, well I guess we can test
if it's actually able to generate images for us as well. And now I guess it's the same thing. Oops. Let's see. Is it already done? That was quick in that case. I'm not sure if I need, is it
waiting for a prompt or not? Maybe. I always just agree to everything, so yes, no clue what that is. Oh yeah, here it's updating. So it was probably just me not wanting to wait long enough. Okay, so now it's updating again. - Testing time.
- Yeah. Let's see if... This should be fairly quick. It's about updating the Lambda functions and just adding policies. Update cleanup. There we go. Alright, so now that's done. Let's see if... It's thinking. Yep, updated the change log and since this was big enough change according to my steering I'm
gonna do a Git commit as well. That was a very good commit message. - [Shridhar] While that is loading does anyone have any suggestions for what we want to generate? So mine was a watercolor hummingbird. - [Gunnar] There we go. That's good. - Is that good?
- Good for a Monday morning. - [Gunnar] We should have, no, it needs to be re:Invent themed some way, right? Las Vegas in winter. Let's see if... Okay, so telling it then to first generate and then test it out. Let's see. So it's run in curl. And since that's now calling
Bedrock, it takes a few seconds and we can see that it generated an image. And now it's gonna try the other one. And yes, we're getting a pre-signed URL. If someone is quick enough you
can type it in and test it. There we go. It worked. Should we try? Do we dare to test it? Moment of truth. Do we really? Yeah. Placeholder. What's that? Oh, well that's interesting. Placeholder for image generation. Images. Oh it's still the text file. I don't think it updated the... So it's able to generate but it didn't update the return guy. (person speaks indistinctly) - [Gunnar] Sorry? - [Speaker] There are two images. The first one (indistinct). - [Gunnar] Oh you're right. Yeah, yeah. Oh yeah, it's listing 25 of them. You're right. That's good. Oh wow. That's exactly what
Vegas looks like to me. So yeah. I guess this is a winter.
- There you go. And how many lines of code
exactly did you write? - Zero. Yes. Okay, so it worked. Oh
yeah, good call out. So yes, it's listing
the text file as well. - [Shridhar] Alright, so we
have the back end all ready now and it works. - [Gunnar] Cool. So. Can you remove the text
file from the S3 bucket? Goes against exactly what you said. Very specific with your prompts. I'm not saying which text
file or which S3 bucket. Let's see if it gets
it. Hopefully it should. Yeah that was too easy. So now it's using the S3 API through the AWS tool. So now the API will hopefully not return that text file as well. Okay, cool. So now we basically have
our back end generated exactly how we want it to do. So I guess it's time to
look at the front end part. - [Shridhar] Yeah, that's the fun part. - [Gunnar] So like I said, I pre-created just a blank front end. Vite + React and it just looks like this for now. So I'm running that here. NPN Run dev for it. So that's all we've done so far. Just to save a bit of time. So let's try to add that prompt. I have a blank React +
Vite app in front end, update it with a single page,
text input for the prompt, a button to call post generate and a gallery with calls get images and renders pre-signed URLs as images. Add an environment file with Vite API URL set to the endpoint and
now I'm tricking it again. Let's do like that. For now skip authentication,
commit to code. So now we're switching from making use of the serverless MCP servers. Now it doesn't really need to use those. So here we can see that it's using tools to understand the front end directory and it wants to make changes. Looks great. It's doing some CSS stuff as well. Let's see what this is gonna look like. Alright. Stage front end changes. So it's adding that to Git. The commit message. Okay, that was pretty quick. Oh here we go. So this is our
front end application now. Nice. So one single prompt, it's able
to just generate something. I didn't tell it exactly
how to use the APIs. It was able to do it,
let's see if it's able to actually generate
something as well then. So now it's your turn to be creative. This is always the hardest part about- - [Shridhar] Keeping the
re:Invent theme going. Let's say re:Invent expo hall. I wanna see what it
looks like this morning. Just kidding. - [Gunnar] re:Invent Expo hall. - [Shridhar] It's not an easy one. I purposely gave a a more ambiguous one. - [Gunnar] Right, so it's generating, so hopefully it's calling the API for us. Oh.
- Oh wow. - [Gunnar] That's more
like re:Inforce I think. But yeah it worked. Okay. Yeah that's a front end that's able to then call the API, generate an image with our back end return a response and actually update the
front end for us as well and display the image straight away. - Nice.
- I think that's pretty cool. So now obviously, most of us would not be
happy with this front end. We would then iterate on it and add additional functionality. We would perhaps improve
the appearance of it. And let's say that maybe
I have my own design team that actually created a nice
design for this website. Well I can just prompt it,
tell it to look at this image or even this Figma template that this is what I want
my website to look like and it would then work
based on that as well. So you can do a lot more. The more specific you
are, even using images, you can tell it exactly what you want the output to look like. And I think that's really
the power of these tools to be able to use proper
context to make things happen. Alright, so now we've made that happen. So I wanted to show something that, I'll try to explain how
I see this relevant. Many times we don't start
from scratch with something. Maybe we have something that's
already deployed in AWS, we have some Lambda
functions running somewhere, some project that we're already using, but then we wanna make use
of these tools to improve, to update and so on. And there is a fairly new
functionality in the console that I think is super helpful for this. - [Shridhar] Yeah, so
while get it all set up, so like Gunnar mentioned, right, there are challenges. So when you start in the console and let's say you want to
transition over to your local IDE you almost instantaneously
get hit with these friction of you know, having to copy code manually, configure credentials
or set up dependencies. Other tools like Linter, formatters, all of those things you
actually have to set up. So what we went ahead
and did earlier this year was sort of take away all the pain and make it a one click experience. So if you are in the
Lambda console for example, and you just say "open in VS code" and it will open your VS code
instance, it'll download, set everything up for you. So you are, there you go. You know, you will just be able to get started in the console. If you authenticate it, it's
literally just one click. - [Gunnar] So just created a new one. - [Shridhar] There we go. Yeah. - [Gunnar] So created
a new Lambda function, it's just a Lambda function but it could obviously
have an API in front of it. It can have a bunch of
stuff, it could be anything. But what we can do then
is make use of this. So I tell it to open it
in visual studio code. And make sure it's opening, here we go. Lemme move the window
ended up on the wrong side. Here we go. So it opened vs code for me asking me do I allow the AWS toolkit, which is the requirement
that you need to have that extension installed to open. And then once we open it... sure, there we go. Yes, I trust, here we go. So now through that one
click thing in the console, we're able to open up
that specific function. Like we said it could be something that someone else has deployed, something that was created long time ago. And now from this point on,
so many popups in vs code, from this point on, well I can
start doing the same things. I can now use Kiro to iterate
on this, I can work on it, I can deploy it again. But with this, what happens when I store or you make a change. - [Shridhar] Yeah, that's
literally my favorite part, right? So you make changes in your ID, it automatically gets
synced back to the cloud. So you do not have to keep hitting, it prompts you obviously, it prompts you that you wanna deploy and you hit deploy, it automatically deploys to cloud. You don't have to make
any of those changes. And one of the other
things here is you could, and we talked about SAM a lot
throughout the session so far. So from here you could
also export your project as a SAM template. So if you want to start
building using, you know, SAM CLI or something, from the ID you could
just go export to SAM and start doing that locally as well. So as you saw the
experience has been much, you know, simplified to
a great deal to the point where you don't have to do anything. We've just taken care
of all the scaffolding, all the setup for you. - [Gunnar] Cool. Alright. So that's a good way if you want to start using these types of tools together with something that's
already deployed perhaps. So back to our app then, and what we've done so far is it's a working app, front and back end, and it has the functionality that we want. But to take this into something that's perhaps production ready, there's usually a lot of other things we need to think about. And one key thing when we're building, and I think for serverless it's super important to understand how your application works and that's where observability comes in. And there are a lot of
great things with the way that serverless works, that
you have separate functions, all the pieces are basically broken apart, makes it easier to understand what's actually happening
as soon as you start adding logging, tracing, metrics and so on. So that's what we're gonna
do now as the next step. And there is something called AWS or what is the official name? - [Shridhar] Power Tools for AWS Lambda. - [Gunnar] Power Tools
for AWS Lambda allows us to do these things fairly easily. So it's basically
libraries that you can add to your Lambda functions
to start adding logging, tracing and metrics to your applications. So instrument your functions
to understand what's happening. So I'm gonna tell it
to basically add that, add Lambda Power Tools to both functions include
logger tracer metrics. I wanna have a custom
metric images generated, I wanna have correlation ideas so we can do request tracking,
I want structured logging and then rebuild and deploy. So I'm telling it that I want to have full observability basically. - [Shridhar] And Power
Tools is a set of libraries that sort of augments what we provide in Lambda out of the box. So you get structured logging in Lambda, adjacent structured logging. We launched a couple of years ago. You could have previously done
it as well using libraries, but we just made it native. You get all log level controls,
what Power Tools does, it helps you extend that
functionality to other things and it builds traces from that and so on. And it's a nifty little tool. So we definitely recommend checking out. - [Gunnar] Yep. So as soon as this is deployed now or once again I'm gonna test that. And something that I use
the Kiro CLI for a lot, it is to understand
what's actually happening with my applications, telling
it to fetch logs for me or telling it to look at traces and so on. Because it is then able to call CloudWatch to be able to get this
type of data for me, but I don't have to do it basically. I can ask it very specific things and it can go through a bunch of logs to find specifically what I'm after. So now it's using the serverless MCP again to run the sam build and
then we'll do another deploy. So what we're doing now is we've been running sam
deploy quite a few times and mostly because we've
done infrastructure changes pretty much all the time so far, but we don't really have
to do sam deploy every time when we're just making code changes. We could use sam sync. - [Shridhar] That is one of my favorite SAM capabilities where
you just do sam sync and it automatically detects and deploys changes for you. It's obviously this guided, you can have different options. I guess you're gonna use
sam sync watch or something or just using plain sam sync. - [Gunnar] Well I'm not
doing it at all right now. This is just. - [Shridhar] And it becomes
handy if you are using, there's another capability called Remote, if you're remotely debugging, for example, debugging a function deployed
in the cloud from your IDE and if you do sam sync then you don't have to
get out of the flow. You could make continue making changes and you know, sam sync will
keep deploying it for you. So you get the experience as if everything is running
on your local device when in reality you're
debugging a function that's sitting in production. - [Gunnar] Alright, let's see. I'm in that state again where I'm not sure if it's
waiting for me or not. I'm always gonna be unsure. Here we go. Updated progress. Alright, almost done. So we can test that as well. These changes now it's
adding those libraries for us so we're able to fetch all that data and we're then able to have better observability
into our application. Let's see if it's almost done. Yeah, update complete. (person sneezes) Gesundheit. Here we go. And then we can test it. I have my prompt ready. Yep. And then we obviously
need to generate something so we have some metrics. - [Shridhar] Oh, you're
looking at me for a prompt? - It's Monday morning.
- Yeah. - Monday morning.
- Oh let's do that Monday morning. Let's see. All right, so now we're generating new and this is to now
generate some logs for us. So we have something to test as well. Hopefully that's done. The application now has
production-grade observability with minimal code changes. And that's pretty cool with Power Tools because you're instrumenting the code so you don't have to write
a lot of code yourself to actually create this observability. You're wrapping basically your function to be able to get it. Monday, Mondy morning. Yep. Not that time. 10 past eight and seven at the same time. - [Shridhar] Not too far off
from what time you're at. - [Gunnar] No. Fetch the most recent CloudWatch logs for the generate function in stack and show me structured log
entries with correlation IDs. Like I said, this is something
that I use it a lot for to be able to understand
not only when developing, but also for instance, when trying to solve issues and so on. Let me fetch the logs differently. All right, so we found
the log group, here we go. I guess this is it. Structured log entry. Monday morning. Oh yeah. So here we go, that's our. So now I was able to then fetch that, we have a trace ID
following the entire request all throughout. Cold start detected since
the Lambda function. Well first off we haven't
used any in a while, but it was also a code change. If that makes sense. Image generation took 12 seconds and we have our custom
metric successfully admitted. So it works. We're able to then fetch these logs and we now have instrumented
our Lambda functions. So what we could do now is
obviously use CloudWatch and we would have traces available, we can use CloudWatch and so on. There is a new feature in CloudWatch that I think is super
useful for serverless. - [Shridhar] Yeah, it's
application signals. It is essentially AWS's APM tool and it collects signals
across logs, metrics, traces for your application
and it correlates them and it gives you key metrics. Think of golden signals, latency, throughput and so on. All of this out of the box by default. It's a one click enable if you are setting it up for your Lambda function. And the part that I emphasize on a lot is that it uses open telemetry to do all the instrumentation. So it can easily fit into
your open telemetry tooling that you already have and
you can extend it as well. Do we have time to show it or? - [Gunnar] Yeah, I'm adding it now. So I sent a prompt telling it
to enable application signals. So I'm doing it through
infrastructures code through my SAM template. It can be enabled in the console as well. - [Shridhar] Yeah, it's the one click. So you enable it and we take care of all the setting up. - [Gunnar] I told it to add
it in the global section so it should be for all Lambda functions, but it then told me no it
can't be in the global section so I told it the wrong thing. So it's adding it to each Lambda function. So it's pretty cool. Instead of actually deploying it and not working, it fixed the
problem for me straight away. So here we go. And now it needs to run sam build and then sam deploy again because it's an infrastructure change. And then as soon as that's done we are then gonna have CloudWatch. Let's see if we get their
application signals. So this is application signals,
so it's basically an APM for our application. And it helps us then understand
the application much better. This is a super cool new
feature in CloudWatch and I think it probably
works best for serverless. - [Shridhar] Yes, yes, absolutely. It makes debugging and figuring out your serverless application
much, much easier. With that, do we wanna
transition back to wrapping up? - [Gunnar] Yeah, I think we should. So basically we've been
able to build an application that I think does exactly
what we want it to. It is able to generate images, we're able to return images. But functionality isn't
the most important thing. I think the important thing is
basically the way we did it. I still haven't written
a single line of code and we were able to generate
this, but still under control. So we controlled it. It wasn't just vibe coding telling a tool to generate the application
from scratch for us and then not knowing
what was gonna happen. We broke it down into small pieces and made sure that we were
in control all throughout. - [Shridhar] I think the
serverless MCP server was super helpful as well. It turned Kiro essentially
into a serverless expert, you know, with all the SAM
tools, deployment guidelines, access to Serverless Land
that I talked about earlier and so on. And again, as you saw that observability was
not an afterthought. Like we added it towards the end, but that's just the progression. You know, we embedded it with Power Tools and throughout the process,
not just observability, the guardrail security
least privilege permissions, not giving S3 bucket public access. Those are things that we
were able to do all again without having to, you know, fiddle around with I am policies and such. And lastly, you know, it also gives you sort of this easy transition
between local and production. Like a basically a complete
developer experience. Alright. - [Gunnar] Alright, so
if you scan the QR code, it will get you to a list
of resources basically. So you can easily download Kiro CLI, but also how you can
find these MCP servers. We're linking the serverless MCP servers, but all the other AWS
MCP servers are there in the same page. Serverless Land, great resource
for everything serverless. Lots of patterns, walkthroughs, articles, blog posts, workshops,
everything basically. A lot of this is built around well-architected serverless lens. So the way that these MCP
servers, for instance work, it is built on
well-architected principles. - [Shridhar] Yes, yes. - [Gunnar] And then finally
linked to the Kiro CLI docs as well where you can
find more information about how to use Kiro CLI. And with that, we want to
thank you all very much for joining us today. Well thank you.
- Thank you.
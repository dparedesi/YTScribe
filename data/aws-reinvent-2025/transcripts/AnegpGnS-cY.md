---
video_id: AnegpGnS-cY
video_url: https://www.youtube.com/watch?v=AnegpGnS-cY
is_generated: False
is_translatable: True
---

- [Saurabh] How's everyone doing? Monday, got through it, right? (laughs) Probably we are in between you and your drinks, so we'll try to keep it as smooth as possible. So before we start, let
me ask the question, how many of you are using
Lambda functions in production or playing around with them? Alright, that's majority of you. And how many of you are performing some sort of resilience testing for it? Alright, you are in the right room. (speakers laughing) So as evident from the room that more and more
companies like yourselves are adopting service technologies like AWS Lambda functions and Lambda functions make
it easy for you to deploy and run your applications because it takes away the
undifferentiated heavy lifting of managing the infrastructure. But at the same time it
makes it difficult for you to perform chaos engineering
or resilience testing and that's where AWS FIS Native Fault Actions come into picture. It helps you to get started
with chaos engineering or serverless workloads
quickly and easily. In this session we are going to talk about what those FIS fault actions are, how do they work and demonstrate you some
practical ways of getting started with chaos engineering, resilience testing for
serverless technologies. My name is Saurabh Kumar I'm a senior solutions architect at AWS. I'm also a member of a technical community that focuses on guiding customers on resilience and chaos injury. And for this talk today, I'm joined by my colleague Haresh. - [Haresh] Thanks Saurabh. And hello everyone. So Haresh Nandwani, I'm a solution architect like Saurabh. I predominantly work with
financial services customers and I'm also part of the same
technical field community that focuses on all things resilience. So moving on. So the session today, we'll be covering a few things. I think as Saurabh mentioned,
the focus is really to walkthrough how you can actually get started using these Lambda actions for testing the resilience of your Lambda functions. So we'll first start off with chaos engineering benefits and just a very high level overview of the fault injection service. Then we'll give you a quick
introduction to Lambda. Hopefully you all know based on, you know, the number of hands that went up. You probably all know Lambda very well. But we'll just cover some of the basics and then start talking
through the FIS Lambda actions that have been recently added. Then we move on to how the
Lambda actions actually work. So the FIS actions that we are going to talk about how they
actually really work and how they've been implemented. They use a concept called extensions. So we'll cover how those
extensions are really set up and then we'll move on
to the real fun element of the session, which is
a live coding session. So, cool. So chaos engineering, again, I think we asked a question already, but in terms of, you know,
using chaos engineering or having heard of chaos engineering, can I have a quick show of hands on how many
people here know the term or even better have used it to implement chaos engineering? Brilliant. Okay, what, a few hands that's
really positive to hear. A couple of years back, I'm sure I would've had a pretty silent room to that question. It's a chaos engineering as an approach is actually
getting quite popular and the approach is about
experimenting with your system to basically build confidence that when things go wrong your system can actually sort of survive in fact even address any challenges and get back to normal
as soon as possible. The chaos engineering process is all about sort of introducing
faults into your system and then basically validating how your system reacts to those faults. The key benefit here obviously is that as you test your system by running these failure scenarios you get a better understanding of the resilience posture of a system. So really how resilient your system is. Where are some of the key
challenges from a resilience perspective and most importantly, what are the key unknowns in your system. It's far better as you can imagine, finding those unknowns early rather than finding them on a Sunday at 3:00 AM in
your production system. So you know, you can see the
value of chaos engineering. So how do you actually
implement chaos engineering? And again, there are a number of options in this space to be honest. Our recommendation is to use the AWS fault injection service or FIS as we'll refer to
it during the session. And there are three key
reasons why we recommend FIS. The first is that it's
a completely serverless and fully managed service. So no service supervision for actually running your chaos tooling. That's all kind of pre-provision for you. There is also a pretty healthy set of what we call a
failures in our library that exists within the tool. So you know, one of the key asks from customers when they want to implement chaos engineering is that how do I quickly get onto implementing chaos experiments and I don't want to spend a lot of time actually sort of, you know, documenting inferior scenarios or even doing all the hard lifting that you have to do. So this is where FIS really shines. So we again talk about these
scenario library shortly. So that was the first. The second is that FIS includes native integration with AWS services like for example EC2. So one common example, the other would be if you wanted to say for example, pause
autoscaling for your system in live or in your test system, then FIS provides you with the ability to effectively perform those actions natively. Not something that a lot of the other tools actually provide. And then the third most important thing is that when we talk
about chaos engineering, as I mentioned before, a lot of it is effectively sort of introducing
faults into your system. But the key thing is that you want to introduce faults in
a controlled manner. So this is where again FIS provides you with the controls and guardrails that allow you to, when you are introducing faults into your system, you want to be able to control the execution of those faults and the execution of the experiments. So for example, there is a feature in FIS called safety levers. So when you run an experiment and if the experiment
actually does far more than what you thought it would,
you can actually pull that safety lever in all the experiments that are running will get stopped. So those are some of the key reasons why FIS is actually a great tool to get started with. There are a few key things that you need to just maybe know as we go into the live coding session. There are a few key terms that will be helpful to know. We obviously, when we talk
about chaos engineering, we talk about experiments. So we will be setting
up experiments in FIS and the way to set up experiments and FIS is to write something called an experiment template. So an experiment template is basically a failure scenario. Like for example, in the case of say if you run a multi AZ application, you might want to set up a scenario
which tests the impact of a single AZ being impaired. So that would be an experiment template that you set up and then you run it and then that becomes an experiment. The other key terms that you will hear us use a lot are actions and targets. Actions are basically
faults that you introduce. So for example, if you
want to degrade the network between the network latency, introduce network latency
between multiple components or shut down EC2 instances or as I said before, pause autoscaling groups. Those are actions that you introduce and targets as the name
suggest are effectively you know, where those actions run. So if you are running an action or introducing a fault
against a Lambda function, then the Lambda function will be a target. The other key element to kind of know and to be aware of is CloudWatch. So again, one of the key
elements of chaos engineering that is really, really critical to get right is observability. If you can't observe it, it hasn't happened as
far as you're concerned. So it's really important that CloudWatch and whatever you're using for observability is set up correctly so that you can actually observe the impact of the experiment or the fault being introduced. So next we come to Lambda. Lambda is our serverless compute service. So you obviously all know that very well. You know, the intent of
Lambda is that you don't have to think about or worry
about server provisioning and all the kind of
infrastructure management stuff. You can focus on writing
your business logic. Lambda is a regional service and what that means is
basically it uses the multiple availability zones that
come with the region that provide redundancy
and fault isolation. And that is then used as far as you're concerned for your function, by effectively what happens is that if there is a infrastructure failure or there's an impairment
to the infrastructure that is running your Lambda function, that is kind of taken care of and the impact to you is minimal because of the multiple AZs that are effectively
running in the region. So, effectively Lambda is a
resilient service by design. So what does that really mean? Does that mean that if you are running a Lambda function or you've set up a Lambda function, you're running a predominantly
Lambda based system, you don't have to worry about resilience? Well no, you still need to
take care of resilience. Your Lambda functions will typically not operate in isolation. They're not really sort of
standalone in most cases they integrate with upstream
and downstream systems or components in your architecture and you still need to validate that when these Lambda
functions encounter failures or encounter issues, how does the overall system's
resilience get impacted? So what is the impact
on upstream downstream systems and so on and so forth. So as you can imagine, that is quite a critical ask. Something that our
customers have been asking for, for quite some time. And the approach that we have recommended to customers is to use chaos engineering for effectively for you to test your Lambda systems from a resilience perspective. And to help you with that, we recently introduced
three actions within FIS. So the first one is
called add start delay. What that does is that basically you can, by specifying amount of
time, you can delay the start of the Lambda function. So for example, if you have your Lambda
consuming components and you want to understand
what's the impact of a delay in your Lambda function to those Lambda consuming functions, then that would be a
great experiment to run. The second one is around
modifying integration response. So again, if you have Lambda
functions that are either returning incorrect responses or if they are then themselves integrating with other downstream systems, which then might be returning
incorrect responses, which the Lambda function returns back to the consuming applications. If you want to test
those kind of scenarios, then that is where the modified integration response comes into play. And the third one is the
invocation errors one. So this is where you
want to test the impact of your Lambda functions
basically being marked as failed when they are invoked. So what's the impact on, again, the components in your architecture that are calling these Lambda functions? So how do you actually now use FIS and these actions to integrate that chaos engineering
approach into your system? So I'll hand over to
Saurabh to talk about that. - [Saurabh] Alright, so before we get into the fault actions, let's quickly look at
the Lambda components and this should be familiar with you. Most of you'll probably be aware of it. So central to the Lambda function is the business logic code that you write. And this is the code
that you care the most about your function code. You write the business
logic along with its entry point called the
functional handler function. And along with that
comes the library code. This is the runtime specific code. For example, if you're
writing your code in Java, then the library code would
be the Java runtime library isn't necessary to run the function code. Another component that you can have, and this function and
library code runs in a secure and isolated runtime
environment, which is managed by Lambda execution environment. And Lambda runtime
environment communicates with the execution environment through an HTTP runtime, API. And that's where your
events are triggered under Lambda functions invoked. Now another component your
Lambda function can have is an extension. Extension is a custom
code that enables you to write custom code
with your function code. And the Lambda extensions are packaged as a separate layer. It runs as a separate process within the runtime environment. So now the next question is how does FIS provide
native fault actions? Any guess? It's not a trick question. The extensions. AWS provides FIS extension to be able to inject falls in your
Lambda invocations. And how does it do that, is that it implements a API proxy pattern, thereby hooking into the Lambda
function execution request response lifecycle enabling you to inject the faults that Haresh talked about. So you have seen how the
FIS extension enables you to implement chaos engineering. Let's see how it works. When you configure the FIS extension, you also configure an S3
bucket and this is the bucket this FIS extension would keep on pulling to see if you're running an experiment. And when you start an experiment from FIS, FIS puts a fault configuration
to the S3 bucket. So next time when the FIS extension pulls for it,
it sees the active fault and starts applying
those faults accordingly. Now I'll deep dive a little bit on the pooling aspect of it. So when you are not running any fault for Lambda functions, the normal lifecycle is that the runtime would
initialize extension followed by initializing the runtime itself, followed by initialization
of the function. When all of the
initializations are successful, then your Lambda function
would be invoked one or multiple times and this is where no
fault are being injected. And when there are no more events, the shutdown would
happen in reverse order. Now when the FIS extension is initialized, it starts a timer. It starts a timer, which
pulls the S3 bucket to see if you're running an experiment. It sees that there is
no experiment being run. Then it sets the timer on slow poll mode, which is 60 seconds by default. But when you start the experiment, it's next time it pulls and sees that there is active experiment, then it sets the timer on hot poll mode, which is 20 seconds and you can't configure that. Now this dual mode of hot poll and slow poll is a trade off between the performance
when you're not running any experiment versus recovery, quick recovery to the normal state when the experiment has concluded. Now with that I'll hand it over to Haresh and we'll get into the
live codings part of it. - [Haresh] Thank you. Right. So what we'll do as part of the live coding session, part of the session is
that we'll first walk you through the app
architecture that we'll use for demonstrating the use
of Lambda FIS actions. Then we'll walk you through the CDK code. So we have a ton of CDK code that we're going to use today, some of it to actually
deploy the application that we are going to
use for as a demo today. And then there is some CDK code that is actually going to set up the experiments themselves. We will then run the experiment and then effectively also show you as Saurabh was mentioning the impact of these slow fast polling. - [Saurabh] So I switch. - [Haresh] Demo. Yeah. Okay. Can people right at the end see clearly what's on the screen? Okay, please let me know
if it's not visible. So what you have here is the CDK code that we mentioned we'll walk through, but first I'll quickly go
through the architecture. The architecture is pretty
straightforward to be honest. All we've done here is set
up a DynamoDB database, few tables, and then there
is a set of Lambda functions that are accessing and running cloud operations on the DynamoDB table. Then you have a set of
APIs hosted on API gateway, which is then accessed
by an external consumer. The intent here is not to focus too much on the
application itself, but on FIS. So that's why the application
is as simple as it is, so that's the bottom
half of the application. What you see at the top is, try this. So the top half here
is all that is required for the FIS experiment. So there is the S3 bucket
that Saurabh mentioned and then we will kind of cover some of how that is set up. Right. I think I might sit. Okay, so getting into the code then there are two stacks that we have today. So as I mentioned, the APS stack is the
one which we deploying the API elements directly
the serverless elements of the stack, which is the
API gateway lab and DynamoDB and even the S3 to be honest. And then there is the
other part of the stack, which is the FIS experiment,
part of the stack which we'll be deploying
the FIS experiments. So first to go through the API code, again, a lot of the code that we'll show you here is pretty standard stuff. So we'll not be walking you through every line of code. That's probably not a
great use of your time. We'll kind of just focus on the key elements of the code that are necessary for setting up FIS and running the FIS experiments. So to start off with, first up is the serverless API. And this is where effectively we have written the code for setting up the APIs and running the code operations. The key element we wanted to point you towards are these parameters that you set up for each of the Lambda function that you want to run an FIS experiment against. So ignore the first two. Those are for effectively the Lambda to access the DynamoDB But the next four are really the key ones. So starting off with the AWS FIS configuration location. So that is again as Saurabh mentioned S3 effectively acts as the in-between, between FIS and your Lambda function. S3 effectively stores the
experiment configuration. So that's where you need
to point Lambda towards so that Lambda can actually sort of access that FIS bucket. The next one is around
the Lambda exec wrapper. So again, as Saurabh mentioned, we are using the concept of extensions and what you need to specify there is the
location of a wrapper script that we have that we provide that basically bootstraps the extension. The FIS extension, again, as Saurabh mentioned
runs in its own process. You might want to measure elements of how the extension itself is performing. So that's beyond how the
Lambda function is performing. So you might want to understand how the extension is performing. So there are again metrics that can be emitted from the extension and for enabling that we set that AWS FIS extension metrics to all. And then finally the slow poll interval. Again, this is basically
as Saurabh mentioned this is to effectively tell the extension on how quickly or how slowly it has to pull for the experiment configuration from S3. So those are some of
the key elements there. Moving on to the next bit of the stack, this part of the stack
effectively deploys, this is a CDK code to
actually do the deployment of the Lambda function. Again, I won't go through all the hundreds of lines of code, but this particular bit that you see on the screen is of some importance. So there is some code there, which is the key one here. One is called resource stack. So one of the ways you can actually, when you are running experiments in FIS and you want to basically
clearly define which parts of your stack you want to
run the experiments on, you can use a concept of tags. So you can basically tell FIS that only target Lambda functions will have a specific tag. So that's what we are doing here. The second one is the Lambda layer ARN. So again, as Saurabh mentioned, because we are using concept
of a managed extension that we have provided, you need to point Lambda towards the extension. So the ARN there is the location of the extension code. That is defined here. So this is the location of the Lambda layer ARN
or the extension code. As you can see it's actually an ARN that is pointing to a specific account
and a specific region. You'll be happy to know that not every code you run in every region needs to point to US east one, effectively
you will have a version of this in every region you run. And then you have the tags. So as I mentioned before,
you have the tag name that you want, the FIS
experiments to target and the value that you will want to use. So these are some of the
key elements of the stack that we wanted to just explain to you. Now the stack, if we deploy it in runtime, that is now, takes about
four to five minutes. Again, in the interest of time, what we have done is we
have pre-deployed the stack. So let me go to the AWS console and show you the output of
the stack being deployed. - [Saurabh] Firefox. - [Haresh] Yeah, okay. So this is the AWS console. Hopefully it's not something that people haven't seen before. Anybody here who needs an introduction to the AWS console? Okay, thank God. That's pretty useful. So going back to the stacks then the stacks that we have here. So we have the API stack. So once the CDK code
is deployed, it's going to deploy the APIs. Let's quickly look at a
couple of things again. So there are a couple of outputs that we expect from this stack. The first one is the
CloudWatch dashboard, ARN. So again, what we do as
part of the FIS experiments is that when we run the experiment, we also generate reports. Again, we'll show that to you when we run the experiment and the report can actually use outputs from a CloudWatch dashboard to then effectively demonstrate the impact of running the experiment. So that's the ARN that it'll use. And then the FIS bucket, ARN, again, this is the we've created an S3 bucket and we are going to pass the ARN for that to the FIS stack or the experiment stack. The resources that this has generated, these are all the resources
that have been generated. So again, the bucket
and so on and so forth. What I'll do is I'll
just dive deep into one of the Lambda functions just to show you how the deployment actually looks. So let's pick up the get item function. This is a Lambda function
that basically is going to fetch items from an DynamoDB database. If I navigate to the Lambda, what you can see is there is a layer now which has been added. So this is effectively the FIS extension that has been introduced into the Lambda function as a layer. Let's also look at a few of the parameters that we have set up. So let's navigate to the
environment variables. So again, as you can see these are all the configurations that we were introducing in the code. So that is the FIS configuration location, which is the location to the S3 bucket where FIS will copy the
experiment configuration, you have then the extension metrics, we've set it all. So it'll actually generate a ton of metrics from the extension, the slow polling interval and then the Lambda
exec wrapper and so on. So effectively the Lambda
now is set up with all that needs to be set up
to be ready to accept a fault introduction from FIS. The last thing I think I'll show is maybe the CloudWatch dashboard. - [Saurabh] Yeah.
- [Haresh] Okay. So. - [Saurabh] And this is for
knowing your steady state before you run the experiment. So pre-experiment state, experiment state and the recovery state. - [Haresh] So yeah, this
is the FIS dashboard. Again, as I've mentioned before, observability is absolutely the most critical thing that you do when you do chaos engineering. So having a clearly set of identified metrics that you want to track so that when you run the experiment you can actually see the impact is absolutely critical. So what this dashboard does is it basically shows you the impact of if and when an experiment runs, it'll show you an impact so for example, the FIS latency impact
should change when if we introduce a latency error
into the Lambda function. Similarly, if you introduce an error that actually sort of causes the Lambda invocations to fail, then you should see some
change in the metrics here. Cool. So I think the next
stage is basically for us to effectively write the CDK code that will set up the FIS experience. So I'll pass that on to Saurabh. - [Saurabh] Alright, before
that, quickly looking at what we have covered so far. So we looked at the
application architecture, we looked at the application code and we looked at the hypothesis where Haresh pointed out that the observability metrics and you can build like if
you're injecting errors, what would the impact
latency wise, error wise. So that's the hypothesis. Now we'll get into the CDK code. All right. What happened? What happened? - [Haresh] I think we might have lost, - [Saurabh] I think that should do it. Sorry about that, technical glitch, sorry. - [Haresh] Network connectivity issues. - [Saurabh] Just move
it and plug it back in. - [Haresh] No?
- [Saurabh] Yeah. Alright. Yep. We are back in business. Right? Are you still able to see or you might, you want me to zoom in a bit? Good. Okay. All right. So here the piece of code that I'm going to show you is a CDK stack written in Java. And when you're thinking
about writing code for generating the experiments, there are a couple of things that you have to build out. So starting from like the bucket that we created, you have to configure the bucket and
the CloudWatch dashboard. So then I will write that code. And in the interest of time you and I know you don't want to see me typing. So I will take a little bit of shortcut. What this piece of code is doing is importing the S3 bucket that has been created
in the previous step. And this is the bucket where FIS would write
the configurations to. We are also importing the dashboard that was created and that dashboard would be used in the report that is generated. So next step is we will create a bucket which would be the
destination of the FIS report. - [Haresh] And sorry, we're not trying to confuse you folks, but there are two buckets here. One bucket is used by the
FIS to effectively share or send the experiment configuration. And then the second bucket is used again by FIS but for storing the reports that it generates when
you run an experiment. - [Saurabh] Right. So with those two things
done now we are going to create some policies and these are the policies
that your FIS needs to be able to run that
experiment on your behalf and I'll going to walk you
through what these are. Alright, so we are creating this policy for the bucket so that it can write the experiment
report to that bucket. And since FIS needs to
write the configuration to the S3 bucket, we are
giving permissions to FIS to be able to read and write from that
bucket that we configured. Same thing for the policy report bucket. Moving on, since we are
targeting the Lambda functions, we are providing in this Lambda policy and tag policy, these are the set of policies which would
enable FIS to be able to fetch the Lambda functions that you want to target. And since we are using resource, so we are tag for
identifying the resources, we are also adding a tag policy here. Now we want to send the FIS experiment, logs to the CloudWatch. So that's why we are configuring the CloudWatch policy as well. And then final bit here
is the CloudWatch policy, CloudWatch dashboard policy, which would allow FIS to fetch the dashboard and all the metrics
inside the dashboard so that it can pull all of those and put it in the report. With all those policies now we are ready to create the role. - [Haresh] I think there is
a error in the previous one. - [Saurabh] Okay. Which one? My friend pointed out the error in this, we'll see when we run this. - [Haresh] Live coding has its advantages, disadvantages, I guess so bear with us please. - [Saurabh] So what you see here is that we are creating a role with the name FIS role and passing in all the policies that we have created in the previous step. Now comes the part where we are creating the experiment template for it. For this session we are going to create two experiment templates. One is going to create
experiment template, which would inject the start up delay of two seconds for five minutes to all Lambda invocations for all the functions which are tagged with the specific value. So I would now go ahead and add the code for it. So I'll walk you through
the key components of it. Here we are giving a description to the experiment template. And this is where like
you can be verbose here so that the description
itself is self-explanatory. When you go into the
console you can clearly see what the experiment is. Then I'm giving it a name of inject delay and specifying the action. Action here is the invoke add delay. This is one of the actions that Haresh walked us before. And then couple of parameters here. Start up delay. What is the amount of delay
that you want to inject? So in this case we are injecting two seconds of delay for how long? For five minutes. This PT5M parameter specifies the duration you want
this fall to be injected. So any invocations during that time would see this delay. And then lastly there is
the invocation percent. So right now it is set to 100. What does that mean, is that all the invocations
of all the functions that are tagged would be impacted. But if you don't want this all or nothing kind of experience, you can set a different value, say 50%. So it would be more sporadic and you can see a different behavior of your application. And then moving on to the target. So target is like what
Lambda functions do you want to impact? So the resource type is Lambda function because we want to impact
the Lambda functions and we want to impact the
Lambda functions which are specified with this specific tag value. And lastly, the selection is all. So all Lambda functions, again, you can specify if you
want certain percentage of Lambda functions to be impacted here. And this last bit of section here in this experiment template is configuring the report. So we are specifying
what is the report bucket where it should go and what is the CloudWatch
dashboard that we want to integrate in this report. And here we are specifying
what is the duration of the pre-experiment state, which is your steady state and the experiment state and after that, what is the duration of the post-experiment state. Think of it as a recovery state, when your experiment has concluded how quickly your system goes
back to its normal state. So with that, this particular experiment template is ready. So now similarly I'm going to add code for adding the Lambda invocation error. - [Haresh] So you obviously
don't have to use code for setting up the experiment templates. You can obviously use the console, but because this is a code walkthrough, we are basically showing you the gory details of the code. - [Saurabh] Right? And this experiment
template is almost similar to the previous one. The difference being the action. So here we are saying
that instead of add delay, we are saying that
inject invocation error, everything is same. So now this experiment
template code is ready and we will deploy this in our account. This won't compile? (attendee chattering) Yeah. So I think the question is that if we have the prevent execution to false, what would happen? So prevent execution, if it is set to true, then your Lambda would not be invoked. The code inside the Lambda function would not be executed but the error would be returned. If you set that to false, then the Lambda code would run and then it would inject that fault. So there could be scenarios where let's say I don't know, like if you're creating a transaction and adding a transaction might have a side effect on your system, then you might want to
set that to false or true. Sorry. Alright, my typo somewhere. - [Haresh] So while
Saurabh is fixing that, so there are two of the actions, they both support this
kind of operating mode. So both the invocation error and the one which returns
integration responses. You can actually decide whether you want the Lambda function to execute or not when the error or the errors in response
is being returned. - [Saurabh] Sorry, it tells me that I already specified FIS role. Hopefully I covered. - [Haresh] I think maybe just, I think when you copied the first element, so you maybe (indistinct) everything, go back and copy the question. - [Saurabh] Which one? Anyone able to spot the error? Yeah. Where? 51 15. So report bucket. All right. - [Haresh] I think it's
been copied twice maybe? - [Saurabh] Everything. So first bucket error end, first report bucket. Alright, so first report bucket. Yeah, should be good right? - [Haresh] Yeah. - [Saurabh] This is the fun
of live coding. (laughs) Alright, so now the
stack is being deployed and while it is being deployed I'll go over to the stack and show you the steady state. So you see the steady state here and you see the Lambda
invocations are happening and in this particular one you see there is no faults being injected. So now when the stack
gets completed we will run the experiment and in the
interest of time we'll run one and then we'll walk over the findings. Any questions in the meantime? Sure. (attendee chattering) - [Haresh] It's a good question. I guess the thing is that you will need to set the permissions accordingly. I'm assuming you should be able to use the same location, but whether it can be the same bucket or not, I'm not sure, it should be fine. I can't see any reason why that works. - [Saurabh] So is the question that, can you use the same bucket for FIS configuration and the report? - [Haresh] Yes. - [Saurabh] Well technically you can. - [Haresh] Yeah. - [Saurabh] But they're
representing two different things. So if you think from the modularity or separation of concerns perspective, you might want to keep them separate. (attendee chattering) - [Attendee] Is there a real requirement or it's just more (indistinct)? - [Saurabh] It's not a requirement, it's more of a best practice how we think we should follow. - [Haresh] Yeah, I think again it's the kind of the permissioning model might be slightly different depending on what you're
doing with the bucket. So that might be one reason you might want to keep them separate. (attendee chattering) So yeah. - [Attendee] Maybe not a question but some feedback about the three buckets. - [Saurabh] Yep. - [Attendee] And like
for the regular people, like everybody knows like what the bucket essentially. And so I'm trying to understand like the (indistinct) of the buckets, how information all the service itself, it's like there is a chance that I might push like
a wrong configuration to the bucket, why is not something
that tells FIS directly use this template and (indistinct) my
template when I (indistinct) the result I (indistinct) the results. - [Haresh] Okay. - [Attendee] Not
something that's explored. - [Haresh] Okay. So just to kind of repeat the question. If I understand correctly,
let me know if not, I guess the question is why is the FIS Lambda set up, Lambda
actions using S3 at all to share the configuration and why can't we just directly get FIS to write the configuration? I think- - [Attendee] It seems
like some (indistinct). - [Haresh] Yeah. - [Attendee] Just to
get there (indistinct). - [Haresh] Yeah, I guess I mean, you know, there are two things to consider here. One is that the Lambda function will exist even without an
experiment running on it. So effectively as you can imagine, right? So when you are setting
up the Lambda function, you're setting up the extension, but there is no FIS experiment running, at that point of time, there is no need for it
to actually have access to the FIS experiment configuration. It's only when you're running the experiment through FIS that is when the configuration needs to be shared with the FIS extension. So that might be the reason, I mean we can confirm with the service team on what was the specific
sort of thinking around that. - [Saurabh] Yes. So if I understood that
question correctly, why you have to configure an S3 work end, the reason is that the extension code is written by AWS but the experiment would
run in your account. So when an experiment is
running in your account, there needs to be a place
where it can, you know, put the configuration and that can be used by the extension. So that's why- (attendee chattering) - [Attendee] For many services. - [Saurabh] Yeah. Yeah. So maybe that's a feature request that we will take it back
with our service team, yeah. Alright, so the stack is deployed and this is the stack which I'm showing for invocation error. I'll walk you through a
couple of key pieces here. So the action itself as we specified in the code
duration is five minutes, 100% invocation. And let's look at the targets. So here we specified all Lambda functions, which are tagged with the specific value. Now in this generate preview, you can actually look at the resources which would be impacted when you run this experiment. So think of it as another pair of eyes or safety net where you
can look at the resources and see something that
you don't want to impact. For example, for whatever
reasons you didn't want to impact the create item function. So by generating this
preview you can go back and change the tags on
those functions accordingly. Then we talked about the
report configuration. So here we are specifying
the report destination where the report would go and along with the CloudWatch dashboard that it would take the metrics from. Now I would run the experiment in the interest of time. - [Haresh] And the warning
that you see there is that when you are starting an experiment, it's going to actually
impact your resources. So this is not a simulation, this will actually run an action, it will introduce a fault
into your Lambda function. - [Saurabh] And while it is running, I'll walk you through a sample report. So the report would look similar to it, it would have the
experiment ID and template ID and the details about when
it ran and which account and what region. It would also have the timeline if you're running multiple faults in a
sequence or in a combination. In this case we just had one so it doesn't look any differently. You just see one experiment there. And then it also has, and this is the dashboard
which we were talking about. So you see the filled out area here. This region is the
duration where the Lambda faults were actually injected. This is the experiment duration, to the left of it is the steady state, which is the pre-experiment state. So this is what a pre-experiment
state would look like. Towards the right is the recovery state or post experiment state. So ideally you would want
to see your post recovery or post experiment state to look similar to your study state. And one thing I would call out here is the errors injection. So we talked about polling. Now when the experiment starts, that's where FIS puts the bucket, puts the configuration on the bucket and the pollings, the extension would poll the bucket and based upon that your
faults would be injected. So the gap between here is what you would see the time when the experiment was started versus the configurations. But were read by the extension and it was implemented on the Lambda invocations. Alright, I think we
covered the experiments, we covered the report, we covered that. Now the experiment is running. So what we can show you is duration, like a previous run before coming into this. And we can show you that duration when the experiments, this is the steady state where you see in this FIS error, there is no error on
the steady state side. And then that's where the
fault started happening. And then when the experiment completed, it went back to zero. And this is what you can see here. So this is what your Lambda duration was and this is the experiment state and then it's going back
to the steady state. Now going back to the
polling aspect of it. Now in this graph do
you see any difference in these are the snippets
from two different experiment reports where in the left hand side the polling interval
was set to 120 seconds. On the right hand side
the polling interval was set to 30 seconds. The difference here is that you see here, the polling is happening
at a longer duration. So the time when FIS started the experiment versus the time when the experiments
were actually effective is longer on the left
hand side graph versus on the right hand side one. And this is because the polling was happening more frequently. So more frequent polling would make sure that your experiments are effective sooner than the duration which is set to longer time. Basically this is the trade off between quickly applying your
experiments versus performance overhead when you're doing the polling more frequently. All right I think we have covered a lot of ground in this. What I would pull up
next is the code sample that we walked you through is based on this public repo which we published earlier and it has all the fault actions and implementation for
multiple Lambda run times. So if you want to try out on your own, you can clone this GitHub repo and run these experiments in your account. You can also reach out
to your AWS account teams and this fault action is also available in FIS workshop, chaos engineering workshop. They can host a workshop for you to get you started on it. Alright, with that we go back to the presentation, I think. - [Haresh] Yep.
- [Saurabh] Yep. So we have seen the
experiment code walkthrough, we have run the experiment. We looked at the polling mechanism and the difference between slow poll timer and hot poll timer. - [Haresh] Yep. So just a really quick introduction to two new failure scenarios that have been introduced lately in FIS. So when you think about failures, you think about, well we want to introduce failures that are potentially, you know, more absolute. So if you already have
scenarios in the FIS library where you can actually test the impact of an AZ impairment. So what happens if you have a service or an application that is running across multiple AZs and then one AZ gets impaired? How do you actually test that scenario, that is already available in the FIS scenario library. But that's more of an absolute scenario. Either something is available
or something is not. But we've heard a lot from our customers asking for scenarios which are more in the partial disruption domain or things you know. You must have come across a term called gray failure. So these are where there is no complete
unavailability of a service, but this service has been partially degraded in some form or manner. So to allow you to run those kind of scenarios
in your application, we have two new scenarios that we've been introduced. One is the AZ application slowdown. So this is where you basically add latency between resources within a single AZ. So you might want to sort of
understand what's the impact of some of your resources, maybe not performing to the right level and what's the impact of that. And then the second one is where you want to understand if there
is maybe packet loss between an application that is deployed across multiple AZs and there is packet loss
between the components of their interfacing or they are interacting between AZs. So for that, again you have the cross AZ traffic slowdown scenario, again, we are happy to sort of point you towards more detailed documentation on those scenarios if you want us to. This is again the FIS scenario library. We did not go through
that in detail today, but you can find the scenarios there in the FIS scenario library in the AWS console. Yeah, I think we are pretty much there. There are a few more QR quotes for you. So a lot of what we spoke about in terms of chaos engineering, the benefits of chaos engineering and the kind of testing you can do throughout the lifecycle of your application is
covered in the AWS lifecycle framework, right on the left hand side. And then there are, for
example, if you want to look at fault isolation boundaries, which is an important concept for you to understand when you are designing a highly available application, then you can look at fault isolation boundaries, multi-region fundamentals. Again, if you have applications that are deployed across multiple regions and understanding how you actually ensure their resilient can be found in the
multi-region fundamentals. And FIS now comes under
the resilience hub webpage. So if you want to understand more about what features are available within FIS, then you can navigate to the resilience hub webpage. - [Saurabh] Cloud ops. Yeah, lastly, drop by in AWS village, drop by cloud ops kiosks, can we have a resilience booth there where you can have more one-on-one demos and don't miss out on the swag there. - [Haresh] Cool. Right. So thank you folks. I guess, you know, doing a code walkthrough looking at a ton of FIS code is perhaps not
the last thing you want to do on a day, but I hope, and we hope you found the session useful. A lot of the code is as Saurabh said already available. If you want to kind of play around, please do access the QR code that Saurabh shared before. If you have any questions, please come along and ask us now or we are available throughout the week and we will be also there
at the cloud ops kiosk. So please come and ask us any questions you might have. - [Saurabh] Yep. Once again, thank you. And we have two minutes for questions and then we can take more
questions in the hallway. Yep. (attendee chattering) Yeah. - [Attendee] So (indistinct). - [Saurabh] Yes. - [Attendee] So (indistinct). - [Saurabh] So I think if I understand the question correctly is the fact that when we are specifying the ARN, it's to a specific version
of the Lambda extension. I don't believe it's points to a specific version though, actually. Sorry. So if we go back to AWS console and there's a FIS extension documentation that we can pull up to. So when you're specifying the layer, where is it? - [Haresh] So I think maybe
what you're trying to do is, what you're trying to understand is how do you actually remove the maintainability challenges with once a new version comes along? Right? - [Saurabh] Yeah, that's a good question. So again, like the, there is a public documentation on it by Lambda function, the latest extension version. But that's something
you'll have to test out and make sure that it is not interfering in your Lambda function. - [Haresh] But it's a good question. We are happy to take that away. (attendee chattering) - [Haresh] Yeah. (attendee chattering) Yeah. (attendee chattering) (attendee chattering) (attendee chattering) - [Attendee] It's not going to change. unless you update the stack, right? - [Saurabh] Yeah, that's true. That's true. So the latest version of
this extension is available to specific accounts
and you can do a lookup, but you're right, like once you have deployed the stack, unless you're managing or maintaining it actively, you wouldn't know you're falling behind on the Lambda version. - [Haresh] Exactly. - [Saurabh] Lambda extension version. Yeah, that's a good point. - [Haresh] We can come back to
you with a response on that. Take that offline. Okay, I think we are at time folks, thank you so much. Thanks for your patience with all the challenges around the code. Thank you.
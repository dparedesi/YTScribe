---
video_id: _4hvWns9ICY
video_url: https://www.youtube.com/watch?v=_4hvWns9ICY
is_generated: False
is_translatable: True
---

- Hello and good morning, everybody. It is so good to see all of you here on day one of re:Invent 2025. Welcome, welcome again. Now in 2025, infrastructure as code is not just an option
for cloud development, it is the go-to mechanism for building and managing serious
applications in the cloud. And so today, in the AWS
infrastructure as code year-in-review session,
we'll tell you about all things infrastructure as code in AWS and share some new
innovations that will multiply your deployment speed on the cloud while strengthening your
safety and security posture. So I hope those morning
coffees have kicked in by now because we have some exciting
stuff to cover today. Now for those of you who
are still figuring out your bearings, we'll start the session by clarifying who we are,
who the session is for, and what you can expect
to get from this session. Now my name is Aakash, I
am a senior product manager for the AWS infrastructure
as code, or IAC team. I lead some of our core
infrastructure management products that help both developers
and platform engineers. And my focus is on helping our customers scale their AWS usage with safety. I'll now pass the spotlight to Praneeta. - Hey everyone, welcome
to the first session for many of you. I'm Praneeta Prakash, I'm
a senior product manager. I focus on developer experience in our developer tools organization. My products are Cloud
Development Kit, CDK, a lot of you might be familiar with, and Amplify for front-end web development. I'm really excited to be here
speaking to you all today. Now that you know a little bit about us, we would love to know
a little bit about you. So let's do a raise hands exercise. Clearly you all love
infrastructure as code because you're here on a Monday morning, so we're not gonna ask that. But I wanna know how many of you are here because your organization's
trying to scale cloud usage without creating a
compliance horror movie. Scaling usage, there you go, awesome. Or you're here because
you want infrastructure to be secure by default
instead of secure by, oops, I forgot. There you go, icy hands. Come on, guys, energy. Where is the coffee set coming in still? And maybe you're deep in IC like me, you like to build infrastructure
as code applications, and you just want everything
to go lightning fast. Ah, I've got a lot of
developers in the room. Hello, friends, you're among friends. So good news is we are addressing all these requirements
today with our talk, so you're in the right room. And the bad news is we are
an hour away from lunch, but we'll keep this interesting. So the agenda for today
is we're going to do a brief refresher on what is IEC. We wanna make sure we're
speaking the same language here. And then we're going to move into the latest launches
we've made in speeding up or improving developer
experience with our IEC tools. Then we're going to go into how does IEC help evolve applications safely as applications are ever-changing, and this is really important. And then we talk to our
platform and security folks on how they can standardize
application development, set standards, put guardrails
in their organizations to help their development teams. And finally, we're gonna approach how we think IEC is changing with all the new trends
around AI coming up and how our teams are
addressing that as well. So let's get started
with the first section. Thank you, Aakash. - Hey, thanks, Praneeta. Now let's spend a few minutes revisiting the fundamentals of IEC because they're more
important than ever today for application development. Now very simply, IEC is the practice of modeling your infrastructure through configuration files or templates. And you can see an IEC template
on the left of your screen. It is defining an S3 bucket resource and certain properties of that bucket. You can deploy this IEC template with an infrastructure as code tool, which will convert the template into a set of control plane API calls and orchestrate the calls on your behalf. So at the end of the deployment, you have a correctly configured S3 bucket in your environment. Now AWS pioneered IEC in 2011 with the launch of a service
called CloudFormation. CloudFormation was designed to
address three critical needs that all customers face when they scale their
cloud infrastructure. Number one, customers want
to replicate infrastructure in new AWS accounts and regions, either for expanding their business, for creating test environments,
or for disaster recovery. Number two, customers want to make safe and predictable updates
to running applications that can contain hundreds of
interdependent AWS resources. And number three, customers want to version
infrastructure states and audit changes to their infrastructure. So if you relate to these problems, the good news is that IEC can
solve all of these problems because IEC templates are
repeatable, they are versionable, and they help you achieve a
desired infrastructure state with consistency. So let's take a look at the
AWS IEC portfolio for a little. Some of you might be
familiar with this diagram. At the center of our portfolio is a service called CloudFormation, which is our core IEC service that accepts JSON or YAML templates. You can pair CloudFormation with a proactive controls
tool called Hooks. And we'll talk about Hooks a
little later in the session. Now, underneath CloudFormation is a service called the Resource Registry. And this service connects CloudFormation to hundreds of AWS
features and capabilities, like S3, Lambda, DynamoDB, et cetera. And as AWS develops new
features and capabilities, they are immediately
integrated into the registry so that you can access these capabilities through CloudFormation. Now, we recently externalized
the benefits of the registry through a service called
the AWS Cloud Control API. Now, this allows third-party IEC tools like HashiCorp, Terraform, and Pulumi to provide the same
coverage for AWS resources that CloudFormation offers. And then finally, on top of CloudFormation sit these opinionated higher-level tools for infrastructure management. And this includes tools like
the AWS Cloud Development Kit and AWS Amplify. So how many of you here use CloudFormation through the Cloud Development Kit, or CDK? Could you please raise your hands? Wow. As you can see, the
CDK is our most popular higher-level tool. And what the CDK does
is it allows developers to model infrastructure with a programming
language of their choice. So you can use CDK through
TypeScript, JavaScript, Python, C#, Golang, and
several other languages. Now, with the CDK, developers can continue to use their existing
autocomplete, linter, and testing tools for development. And they can also use familiar concepts like looping and inheritance when they are defining infrastructure. On top of all this, the CDK offers a powerful
capability called constructs. You can think of constructs as packaged infrastructure components that are infused with AWS best practices. So now developers can
declare infrastructure without having to understand
every single low-level setting. The CDK offers three levels of constructs. L1s are constructs that map most closely to the underlying
CloudFormation resource types. So L1 constructs in CDK are
precise and they're granular, but they can also get verbose. L2s are a higher level of construct that combine multiple resources, often of the same service,
into a functional component. So an example L2 could
be an S3 bucket component that comes equipped
with the logging bucket and auto-deletion capabilities. And then finally, on the
other end of the spectrum, are L3 constructs, which
combine multiple resources into an entire architecture. So an example L3 construct could be an end-to-end
serverless application. So now as a developer,
L3s are super easy to use, but they're not as flexible as L1s. So we'll talk about constructs
and their trade-offs a little later in the session. The key message on this slide is that the CDK is full of capabilities that make it easy for
application developers to get comfortable with
the Cloud and with IEC. And that is a great segue into
our next insight about IEC. IEC is now the front end to the Cloud for all teams in your organization. And this democratization
of IEC across stakeholders is being driven by three factors. So number one, today platform teams want to decentralize infrastructure management responsibilities, which means that platform
teams want application teams to independently provision
and manage applications. How many of you are seeing this
trend in your organization? Lovely. This obviously helps
organizations to move faster. Factor number two, platform teams are building developer platforms
that help application teams to run IEC workflows with confidence. And this includes the
creation of golden paths on top of IEC constructs, as well as the enforcement
of proactive controls so that issues are
caught before deployment. And then number three, the
newest trend on this slide, there is a rise in Gen-AI tooling, which makes it easier than
ever to generate IEC code and ramp up on IEC concepts. So more developers than ever
are generating IEC code today. So now that we've established that IEC is everyone's business, and it is so fundamental to how
our customers use the Cloud, we know that any evolution in IEC can transform the entire
Cloud development experience for our customers. And so we strive to make
IEC faster to build, easier to manage, and safer to govern. And we'll talk about these
themes through the session now. So on that note, Praneeta, can you share some of our innovations that help developers to
build faster with IEC? - Yeah, so a little bit about me is I was a developer before
I was a product manager, and I was one of the lazy developers, and I wanted all the
tooling set up correctly to help me move fast. And I know, I know, I see your faces and I know we have lazy
developers in this room. Raise your hands, guys. Where are my lazy developers at? All right, excellent. So remember the days before IEC when provisioning infrastructure was days of waiting on tickets that you hand off to your platform teams? And you never knew if you
would get what you asked for. Now, it is a single command
that can spin up complete stacks of compute, networking, databases. You can set up isolated stacks to test your application code quickly, and no one is allowed to say, but it works on my machine anymore. But with IEC, there is
a learning curve today, especially with AWS IEC, because
there are a lot of concepts for developers to know about before they can even start using it. And we're trying to
make this on-ramp easier for our developers. Let's look at a typical
developer workflow. Now, if you are a CDK developer, you have an application in mind and you're looking for
patterns in the CDK constructs that are available online to kind of compose them
together into an application and make it work to what you need. You use the CDK CLI to
then take your application written in a higher-level
programming language like TypeScript, and turn that into CloudFormation
templates and assets. If you are someone who prefers
to write declarative code to define your infrastructure,
you start at this step, building your CloudFormation template. And then you call the
CloudFormation service to deploy and provision
your infrastructure for you. So this is the typical
developer workflow today. Now, while this slide talks about CDK, I do wanna focus on developers that are building their
CloudFormation templates by hand. And then I will move on in the next part to talk about the provisioning and deployment improvements
that we've made. So let's start with authoring. If you're authoring CloudFormation by hand today, you think about the services you wanna compose together
into your template, and you look at multiple
AWS documentation pages. You start with learning
about S3 if you're using S3, and then you go into learning
about all the properties that you can configure in S3. And then you look at
the CloudFormation docs to make sure you know the syntax, and you put in a valid syntax
in the property values. And this is a lot of
context-switching for developers. You're going back and
forth between your IDE and 1,000 tabs on your browser, which is why we're really excited to kind of bring that experience to you within the IDE with the
AWS Toolkit plugins. Now, the Toolkit plugin supports a CloudFormation IDE experience today, and you can use that on Visual Studio, Visual Studio Code, and IntelliJ Idea. The three main features of this plugin are you have autocomplete
and hover features. So if you define a resource,
you see documentation pop up, and you see properties that you would need to define for that resource. You can also, the plugin
automatically runs linting tools for you. So it catches syntax validation
errors in line on the IDE, which is really helpful, and
you can instantly fix them, along with a helpful documentation
on how to fix it as well. And it also catches
security best practices being missed in the code,
and warns you of those. In this example, I believe we're trying to assign a public IP address to a VPC. So hopefully this makes
the authoring experience much simpler on CloudFormation. Please let us know how
this works out for you. Let's move into deploying
and provisioning ISE. Now, ISE, your typical workflow
looks something like this, where you are creating your chain set, executing it in CloudFormation, and deployment starts, and
possibly it finds errors, and then it has to roll back
to the previous safe state. This is a really long feedback loop for the developer who's
trying to get this job done. Every time the developer makes
a change to their template, they need to package, deploy, and wait. And once the error's encountered, they need to redeploy the
fix, and do the same thing. Now, the main problem here
is that a lot of errors, like naming conflicts,
property syntax errors, resource conflicts, are only
discovered during deployment. For many organizations,
this could also mean waiting for pipeline deployments to fail, or having your platform engineer have to reach out to
you about this failure. We are really excited to now shift this error validation left, so that you can get a lot
of these errors detected during chain set creation time. We're supporting three
main types of errors today, resource naming conflicts,
invalid property values, and deletion of non-empty buckets. And we will be adding more types of errors over the next year. But what this means is before
deployment even starts, you will have an alert from CloudFormation that tells you that
these possible resources will fail during deployment. You have a really nice
console experience as well, which we have a new tab
called Validation Results. And this lists all the resources that are predicted to
fail during deployment, along with a detailed description and the line of code where
that error was originated from. Try this out today, and now
I'll hand it off to Aakash for evolution of applications. - Hey, thanks, Praneeta. Oh, man. Revisioning error loop
has been long for ISE, and it's so exciting to see that what took hours to detect in the past can now be done in minutes or seconds. So yes, the developers
can now move faster. This also means that the size
of your cloud environment is going to continue to grow. And as your cloud environment scales, you will need large teams, and often multiple teams to evolve and maintain that
infrastructure in parallel. So how do you prevent an
explosion of complexity in this world? And how do you avoid those
dreaded outages from happening? Now, ISE is your shield
against chaos at scale because ISE brings the best of DevOps to infrastructure change management. With ISE, you can review code
before it's being pushed out, you can version infrastructure
changes as they happen, and you can deploy infrastructure changes through structured CI/CD
pipelines and test environments. But in order to access
these critical security and safety benefits, you need to keep your ISE up
to date and well architected. So let's talk about what
gets in the way of that and how we can mitigate those pain points. Let's first address ISE drift, which our customers tell us
is their biggest challenge with infrastructure management today. To understand drift, imagine
that you are a developer, and you of course are very
familiar with our best practices, you're on top of things. So when you wanna provision a new resource in your environment,
you do that through ISE. You define an ISE template
and you deploy it. But you have a second
developer on your team who's not as familiar with best practices. They need to change your resource and they need to do it quickly. So they go to the AWS Management Console and they click their way
into resource changes. Now the actual state of your
resource has drifted away from the template
definition of your resource. And this is bad because once
drift enters your environment, you could see unexpected changes
in future ISE deployments, including reversals of critical fixes that you made for production incidents. You could also find it
difficult to reproduce your application for testing
or disaster recovery. And you're also exposed to violations of compliance policies. In fact, customers have shared with us that some teams have
accumulated so much drift that they've completely
given up on managing applications with ISE and lost
all of the safety benefits that come with it. And that is why I'm
very excited to announce that CloudFormation has
launched a new capability called Drift-Aware Chainsets that can help you to safely manage drift and keep your infrastructure
in sync with your templates. Now the way this works at a high level is when you need to deploy
an updated ISE template on top of a drifted resource, you create a Drift-Aware Chainset and CloudFormation will
compare your template to the actual state of your resource. You will get a three-way comparison of the actual resource state,
your new template definition, and your last deployed
template definition. So you can detect overwrites of drift and you can fix unintended
overwrites in your template. When you refine your template
to show you the desired state, you can execute the chainset
to bring your drifted resource in line with the new template definition. And so the net result is that
you've safely reconciled drift for your resource and taken
it to its desired state. Let's unpack this with an example. Let's say that you have a
malfunctioning application that you build with ISE. Ignore the ISE template
on the left for a second, I know it appears complex. Look at the diagram on the right. You have a lambda function
reading from an S3 bucket. Objects in the bucket expire every day and there is a CloudWatch
alarm on the bucket which monitors the number
of objects in that bucket. But because this application is working and you don't exactly know what's wrong, you would go to the AWS console and try out some fixes
for this application. So here's what you do. You go to the console
and first you increase the expiration of objects
in the bucket to 100 days so that you can observe what data is actually flowing into the bucket. But you know this is gonna
trip up your CloudWatch alarm so you delete the alarm temporarily. And then over time, you
discover that the issues with the timeout of your lambda function and increasing the timeout to 20 seconds gets your application running. So the good news is that you know the root cause of your issue. The challenge is that your application is left in a broken state. So how do you get back from here to a production-ready state? Well, now it's super easy
with DriftAware Chainsets. All you need to do is make the changes to your ISE template that you want to persist in your environment. So in our case, we no longer increase the timeout of the lambda
function to 20 seconds. After we make this change, we create a DriftAware
Chainset with CloudFormation. And now CloudFormation is doing all of the heavy lifting for you. It is detecting that your CloudWatch alarm was deleted out of band and needs to be recreated in the deployment. It is detecting that your lambda function has been changed out of band, and the template
definition of the function has been updated to
incorporate this change. It is also detecting that the S3 bucket has been updated out of band, and it needs to be reset
to its template definition. You can zoom into the property
level view for each resource. For example, for the S3 bucket, you can see that the actual value of your expiration setting is 100, while the value in your
new template is just one. And you can also see
that this actual value is coming from an out-of-band change. You can expand this out-of-band change to see what the value was
in your previous deployment. So now you have a full picture of the story of your deployment. And that's it. You just execute the chainset, and your application is now
back in a healthy state, and it is also in sync with your template. So that is how easy it is now to manage drift with
drift-aware chainsets. Now, Praneeta, I'll pass it back to you to share how you can keep ISE up to date with new business requirements. - I love that drifts
are yesterday's problem. So, I guess, how many of you
have built an application, pushed it to production,
and never touched it again? It's just not a thing
in our industry, right? Applications are ever-changing,
constantly evolving. New product managers,
new security guidance, new requirements come in, and you constantly have to
revisit and keep modifying them. This used to be really hard
to do with CDK applications, by the way, until a recent launch, and I wanna talk about that right now. So, you have a CDK application. It's possibly using a
monolithic lambda function, but it works, so why not? It's talking to three tables, it's doing its job, your
customers are fine with it, and you don't wanna fix
something that isn't broken. Now, you know there's tech debt, and you realize, well, you know what? I wanna scale these three lambda functions independently of each other, and it's also part of
well-architected principles to not have monolithic lambda functions. And while I do that, I might as well move
the CDK application code from L1s to using an L2, so I can configure my
lambda function in one way, in one place, and use inheritance to spin up three other lambda functions. All good ideas, and when you
try to do that, what happens? Any guesses? What happens when you try to deploy a changed application in CloudFormation? You lose your data. Congratulations. It will delete and
recreate your resources, because it does not know
what refactoring is. Until we made that
change with CDK refactor and CloudFormation refactor. What this helps with now is it makes infrastructure as code development closer to how we think of
software development to be. You can move your, rename your constructs. You can move resources between stacks within your application. You can upgrade your
L1s to L2s, L2s to L3s without risking losing
persistent resources or data. This is offered as a
feature on the CDK CLI with a CDK refactor command. We pass in the unstable flag today, because it's an experimental feature. It's in preview. When you change your application
to where you want it to be, and you run the CDK refactor command, what it's really doing is it's mapping the constructs in your
deployed application to the ones in your local application. And it recognizes that things have moved instead of being a replace action. Once you confirm this,
it tells CloudFormation, don't redeploy anything. I'm just remapping the logical IDs to the infrastructure,
to the physical IDs. And you don't risk losing
data in this process. So try CDK refactor. If you have old CDK applications
that need a little love, you can now do that with CDK refactor. So let's move on to the next section, which is simplifying and
governing IEC workflows. Simplification, to me,
means that developers can move faster with fewer
decisions per deployment by using patterns or
guardrails available to them. And governance, to me,
means that platform teams can still retain control and set standards and share best practices without getting in the developer's way
or slowing them down. CDK has a really cool construct system, which I think the CDK users
here are familiar with, but it helps you do exactly that. It helps platform teams define constructs or blessed patterns that can
be used by their developers, knowing that it adheres
to the organization's best practices and security
practices and compliance needs. Now, while the construct
system is working really well for a lot of our customers,
there is a problem. How many of you have
wished for more coverage on CDK L2 constructs? Oh, oh, I love that you're all happy. Oh, there, there you go, thank you. The problem with that is L2
constructs are a fully built, opaque abstractions that contain
a lot of logic within them, but they're not composable
building blocks. And let me tell you a
little bit more about that. We build L2 constructs for every service or feature that our customers use to build applications with. So while we don't cover all of AWS, we cover a lot of popular patterns in AWS with L2 constructs. Now, your organizations take,
your platform teams take that, and if they don't think that the L2 meets their security and compliance needs, they extend it with adding
or removing features to meet their needs. And we call that custom constructs. Custom constructs could be at the L2 layer or they could be higher level constructs that match your use cases, like
secure API or data pipeline. The problem with this is that every time there is a new feature or
service announced by AWS, you need to wait for AWS CDK team to support that within an L2 construct or build a new L2 construct for it, which then goes to your platform team for them to extend or modify it, and then becomes available for you to use. For fast-moving organizations,
that could be too slow. So we wanted to, as a CDK team, we wanted to look into how we can decouple innovation velocity from
abstraction maintenance. Sorry, this is fall, and
I have kids and my throat. So we look at this L2 construct, which is, we like to
call it a walled garden. It has beautiful features in it that cannot be used independently of it. An L2 bucket, for example, is
a combination of L1 resources, which wrap around CloudFormation
resources directly. So it wraps around L1 bucket and KMS key in this particular example. There's a lot more going
on in there, obviously, but let's look at just
encryption for this one. So the encryption helper adds all the wiring
logic between your bucket and your KMS key for you, and if you had to define
it on your own by hand, it would be a lot more lines of code. This kind of does that for you, which is why L2s are really well-loved. The problem, though, is a lot
of services need encryption. So now we are repeating implementation across each service's L2 construct, and that's doing a similar thing, and every time there's a new service, we need to redefine this because we work through
inheritance and not composition. We wanted to switch that around. We wanted to take the helpers
out of the L2s walled gardens and make them available as
reusable building blocks. Encryption is just one example, but of course there are a lot
of such cross-cutting features like logging, auto-delete,
grants, metrics, tagging. So we are now launching a CDK
mix-ins library in Preview. These are composable,
reusable abstractions that can apply to constructs of any level, so they are no longer exclusive to L2s, and you can mix and match them with L1s. You can apply them to
your custom constructs and get a lot of these benefits for free. An example here is using
the encryption at rest. In code, this is how it looks like. We're using encryption at rest
with a CloudFormation bucket, which is an L1 S3 bucket. Cool. Aakash, if you can walk us
through the proactive controls. - Absolutely.
- Thank you. - Hey folks, so how many of you here are part of a platform team or a cloud-centered of excellence that either manages abstractions
or security controls or deployment pipelines
in your organization? Do we have folks here from there? Great, great. So yeah, I mean, as all of you know, the empowerment of application teams to move independently means that you, the platform engineers, are
no longer the bottleneck for every change to the cloud, which is great because
now your organization can move faster. But ISE misconfigurations
can create security risks, and all it takes is for a developer to forget a critical security setting. So how can we help our platform engineers to sleep well at night without worrying about what their developers
are doing in their environment? Today's security tools are often reactive. What this means is that they look at a resource configuration after the resource has been provisioned, and these tools will generate alerts for the platform team or the
security team to respond to. So now the burden is
still on the platform team to coordinate responses to incidents. The feedback is passed to developers who then have to redeploy
applications all over again. So this is a long feedback loop, and I know we've been talking
about long feedback loops through the session. In order to do better, CloudFormation launched a
capability called Hooks. What Hooks can do is
detect misconfigurations before deployment. So you can set up Hooks to run custom code or enforce controls at various points in your CloudFormation
deployment workflow. And some of the invocation
points that we support are just right before
resource provisioning starts during a deployment, at the very beginning
of a deployment cycle, and you can also shift
left control enforcement to chain set creation time, which is deployment preview time. And finally, we also support Hooks for Cloud Control API operations, which allows you to
enforce consistent controls across ISE tools that
your organization uses. So while this is great, a common challenge that
customers share with us is, it's difficult for us to maintain and define the controls
that we want to enforce. And if you are in that boat, I'm excited to share that CloudFormation just launched an integration of Hooks with the AWS Controls Catalog. You can think of these as
predefined security best practices that are just directly available for you in the CloudFormation console. So now you can go into the console and you can open up these
predefined best practices, and you can see exactly
which control objective and security framework e-control maps to. And with just three clicks,
you can enable a control for all CloudFormation
deployments in your account. So it's never been easier to keep your CloudFormation
deployment secure. Another key aspect of governance that I know our platform engineers rely on is multi-account architectures,
where platform teams went landing zones to application teams. You can think of them as
accounts that are bootstrapped with critical infrastructure
and guardrails, so that application teams can just start building in those accounts. CloudFormation stack sets are an invaluable tool
for account baselining. What stack sets do is that
they can take an IEC template, and they can repeat the template in multiple accounts or regions. And one of the amazing
parts about stack sets is that they integrate
with AWS organizations. So when you add a new account
to an organizational unit, your stack set can automatically deploy foundational
infrastructure to that account. And while this is great, we
now see that platform teams wanna take a step forward with their foundation infrastructure. They want to split up their
foundational infrastructure into multiple components that
independent teams can manage. So for example, you may wanna split out your networking resources
from your identity resources, and your identity resources
from your application resources. The challenge with this approach is that there are implicit
dependencies between the stacks. So identity needs to be in place before networking can function, and networking needs to be in place before your application can function. So when you add a new account
to an organizational unit, you need your stack sets to
deploy in a certain order to avoid failures. But I'm happy to share that
stack sets now supports a feature called dependencies. Now you can say that
your networking stack set depends on your identity stack sets. And your application stack set depends on both your networking
and your identity stack set. So now CloudFormation will
handle deployment ordering on your behalf when a new account
is added, and you will get the baseline infrastructure that your application teams need. This combination of
enforcing proactive controls and creating landing zones gives you the defense in depth strategy that you need to keep your
cloud environment secure, while also leaving room for
your developers to innovate. Great. So let's take a deep breath here and digest some of the stuff
that we went over today. First, we talked about how authoring and validation capabilities can help you multiply
your deployment velocity. Second, we talked about how easy it is now for you to stay on top of drift and to keep your ISE up to date with evolving business requirements. And then number three, we
spoke about how easy it is now for platform teams to decentralize
infrastructure management with confidence. So let's ask ourselves, how is infrastructure management evolving? What are the next big trends
in infrastructure management that you wanna stay on top of? Well, AI is top of mind for
organizations and leaders today. We all want the efficiency benefits of AI. And while the ability of AI to create cat videos and pirate costumes is exciting in itself,
we really want AI to help with the hard stuff in our jobs. And all of you know here that infrastructure management is hard because it demands context
and it demands precision. But this conflicts with the
probabilistic nature of AI. So how can we bring
the efficiency benefits of AI to infrastructure management? Do we see a world where
the two can come together? Well, we think that ISE
will be the crucial bridge that brings AI benefits to
infrastructure management because AI and ISE have
complementary strengths. AI provides ease of use. AI provides speed. While ISE comes with built-in mechanisms for safety, for reliability,
and for human oversight through features like deployment previews, rollbacks, and resource handlers that come with correctness guarantees. So as we think about the future of ISE, we're thinking about how we
can bring AI into ISE workflows and create a whole new
infrastructure management paradigm for our customers. And now, Praneeta, I'll
hand it back to you to discuss how customers are trying to combine these concepts today and what challenges they run into. - AI is amazing, isn't it? I use it a lot every day. I use it for this talk. But I wanna talk about, I feel like developers lose trust in AI, especially when generating
infrastructure code, because the errors are
so minor and invisible. It's almost right, but not quite. But in ISE, that can be catastrophical. It can bring down your environments. It can cause a lot of damage. And that's not a fun place to be. So before we start saying AI did this in place of dog ate my homework, like how can we make our
AI-driven development flows much more reliable? How can we, all the tools
that we talked about earlier that were for our human
development workflows, how can we make them
available to AI as well so it can make better decisions? We talked about long
feedback loop earlier. It becomes even more challenging in AI-driven or agentic workflows, because an agent is now far removed from when the deployment failure happens. And if it cannot get
that context back in time for it to reason and
fix the generated code, you lose all of the speed benefits. It's the same with a pipeline. Pipeline now just becomes
an additional layer that the agent cannot go past. So it's really critical
we provide the agent that context while it is generating code. And how can we do this? So one of the things that
we have launched last week, I believe, is ICMCP server. Now you've all been
hearing a lot about MCPs. You will hear a lot about them this week. But mainly they are a way for AI systems to communicate with local
tools and context predictably. So if you ask a CDK question, the agent's gonna look
for CDK-related tools to give you a better answer. And what we're doing
with the ICMCP server, which is available open
source and on AWS Labs, is we are providing these as
tools for your agent to use and improve the quality
of the code generated so you don't run into
challenges during deployment. What these tools look like
are they are knowledge tools. So they're curated knowledge tools that cover AWS opinionated best practices, recommended best practices,
CDK construct libraries, both in alpha and in GA, and
CloudFormation context as well that we really recommend
the agent to look at. And we have added troubleshooting tools, which could be server-side
APIs called on CloudFormation, like the chainset validation
we talked about earlier. And validation tools are
more of your local tools that do static code analysis and find syntax errors
for you in your code. So all of these tools are available today, and I would love for you all
to check out the ICMCP server. It's available at this link. This link takes you through a workshop that helps you use AWS MCP
servers in a guided path, and it helps you get
comfortable with the whole idea. So here we are, folks. My first breakout session, some of your first re-invent sessions. I hope you're all feeling wonderful and you've all learned
something today from this talk. We do have a survey link here. We use this, us product
managers use this data to make better decisions and
prioritizations for 2026. So we would love for you
to fill this up for us and let us know your candid
feedback on our tools. But overall, I'm really, really excited that I got to speak to you all today. Thank you so much for your time, and we are also available
to talk after the session if anyone has any more questions. But thank you, everyone, for your time. (audience applauding)
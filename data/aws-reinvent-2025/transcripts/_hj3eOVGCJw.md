---
video_id: _hj3eOVGCJw
video_url: https://www.youtube.com/watch?v=_hj3eOVGCJw
is_generated: False
is_translatable: True
---

- Thank you everyone for coming to this talk on managing
multi-cloud Kubernetes at scale. My name is Gaurav Dhamija, I'm a principal solution
architect here at AWS and I have with me John from Adobe. And I'm pretty sure most of you, if not all of you must be
using Kubernetes in some capacity in your organization. But just a quick show of hands
if you do it across multiple cloud service providers. Okay, we have few brave
and adventurous folks here. So in our talk today, I'll
be sharing AWS perspective on multi-cloud and then we
will be talking about some of the considerations related to multi-cloud Kubernetes
fleet management. And then I will be
handing it over to John, who will be talking about
Adobe's experience in this space and also share some of the learnings and best practices from
Adobe's experience. So from AWS perspective, what
do we mean by multi-cloud? It means that our customers
are running an IT solution or a workload across at least
two cloud service providers. And when we talk to our customers, they cite multiple
reasons for this strategy. It could be their business
strategy, it could be mergers and acquisitions, or they
might be using a differentiated capability in a specific
cloud service provider. Now, from AWS perspective,
we work with them, we partner with them to make sure
that they're successful. We help them build technical and non-technical capabilities
across all process and technology pillars. Specifically on technology
perspective, what we noticed is that is that many of our
large multi-cloud customers, including Adobe, having
investing in platform engineering and building internal developer platforms to streamline their experience
across multiple cloud service providers, which is why AWS
in partnership with in some of these, with in partnership
with some of these customers including a Adobe, launched
CNOE, cloud native operational excellence initiative. Now, as part of this initiative, we not only have defined a
composable capability metrics for defining the internal
developer platforms, but we also offer tools, guidance as well as reference implementation
that you, you can use today as part of your multi-cloud journey. And it is also not surprising
as part of CNOE initiatives and discussions with our customers, Kubernetes and containers have emerged as a fundamental abstraction used by our multi-cloud customers across, to streamline the experience. Now, today our focus
is on fleet management, but there are also other
considerations like multi-tenancy and developer experience that
need- you need to think about. Now, from fleet management
perspective, you not only need to think about cluster
lifecycle management, but also add-ons lifecycle management. So you may have add-ons related to networking security
observability on your cluster and you need to think
through their lifecycle. And also typically clusters
in practice turn out to- usually have different configurations. So, based on the workloads that you're supporting on those clusters. So, for example, for AIML workload, your cluster may have specific GPU drivers or a specific hardware
that you need to support. And when we talk about multi-cloud, you may also end up supporting
multiple distributions of Kubernetes itself. Now one approach that
we have seen work well for our multi-cloud
customers, including Adobe, is using GitOps based
approach for fleet management where we, where we see our
customers storing both the cluster and add-on configuration, as well as all the securities, audit and compliance policies itself
in Git as a source of truth. And then leveraging GitOps
operator like Argo CD and cloud providers specific controllers to continuously provision
and reconcile the state of their multi-cloud Kubernetes fleet. Now with, now with that context,
let me hand it over to John to share how Adobe has implemented some of these patterns at scale
in their organization. - Thanks so much Gaurav. Hi everyone, welcome to
AWS re:Invent. I'm John. I'm with the Adobe plat-
Adobe developer platforms team and our mission's simple. Help developers write
better software faster. So when Adobe's landscape looks like this, and I assume a lot of other
folks looks like as complex as this, how do you actually do that? I'm also a fan of abstraction and platform- platforms where you need to simplify in many cases
oversimplify for your developers. So in this cake of complexity,
what happens when you add yet another layer called multi-cloud? Adobe has been on a multi-cloud
journey for over 15 years, and as part of that we've had to iterate on our own approach. Fit for purpose is essential. Where you deploy applications
in a multi-cloud environment must be an intentional choice. Yes, perhaps you have data
residency requirements, security attestations, or integrations with a strategic partner. Likewise, we still live in a world of phy- with physics after all. Replicating state within
one cloud provider, let alone two, is inherently difficult. Do not approach multi-cloud
as an HA construct on its own. We still have the speed
of light to deal with. Finally, our emphasis is
really on platform engineering at Adobe, which means we
treat all cloud providers, including our own data center
as a first class citizen. By doing that, it enables you to meet diverse business needs along with specific technology
challenges to enable the, to enable developers to
do what they want to do, ship code as fast as possible. So how do you get this type of consistency and uniformity in a really complex environment like multi-cloud? At Adobe, we built Ethos. Ethos was built to simplify
the developer experience. So it's a consistent interface
for them, regardless of that underlying cloud provider. Likewise, we want our
developers to integrate and manage cloud native infrastructure, not with SDKs or proprietary APIs. We want them to interface with infrastructure using
uniform CICD pipelines regardless of that cloud provider. Finally, we want our developers to focus on delivering business value, not necessarily figuring out how to apply specific security or
compliance attestations, which are unique to each specific
region or cloud provider. Developers just want to ship code. So at Adobe Ethos is a pretty big deal. We're the dial tone for the
entire fabric of the company. On a typical day, we orchestrate around 4 million containers. 90% of Adobe's containerized
footprint runs on Ethos. That equates to around
04,000 distinct services across our own three clouds. Digital experience, creative and document. That footprint manifests itself
into 450 independent ethos clusters globally, which
is around 30 regions, multiple public cloud providers and multiple private data centers. So when you approach this
type of complex environment and challenge, how do you
engineer your way around this? We had our own operating
principles that we pointed to. Our approach is, is
rooted in one key aspect, declarative infrastructure. We use declarative infrastructure to define cluster
configurations, network policies, versions and resource definitions, which are all managed as code. Typically Yaml manifests that live in Git. In light of what Gaurav off said earlier, Adobe has really embraced GitOps and our entire workflow is GitOps driven, in this case using tools
like Argo CD and Helm. All changes to both application state and infrastructure are
made as pull requests to specific Git repositories. Ghat enables you to have
a single source of truth that allows you for automated rollbacks, continuous pipelines and
eventually automated tests to get eventual consistency with what should be in production, referencing what's in source. We also built Ethos as
a modular code base. We use Helm as a package manager to deploy each of those components and each of those security configurations that allows for rapid
updates, easier maintenance and customization for
different business needs or perhaps technology
challenges, like multi-cloud. Finally, we really embrace open source. Cert manager for certificate management, cluster API for managing
Kubernetes components on cluster, open telemetry
for our observability stack. Using open source also enables
our own teams within Adobe, like Adobe Firefly, to
contribute to platform. And what Firefly did was
contributed their own custom pod autoscaler for their own business needs. So how did we do this? Well, there's two important aspects. The first one is the
human or the operator. What do, what does the human need to do? The human goes ahead and populates a specific manifest file with important key attributes. What the cluster name should be, what region it should be
deployed in, what organization, and more importantly,
which cloud providers should we deploy this cluster to. Taking that input from the human, what's the machinery that
actually executes this? It's a, it's a Kubernetes
cluster running Argo. Argo listens to signals
from Git and goes ahead and wants to take the
configuration, which is Git, and get that eventually to production. And the two key aspects
that signal from Argo to actually what's in production or ACK or AWS controller for
Kubernetes and cluster API or Capi. ACK manages specific
AWS primitives like EKS. Capi manages specific
Kubernetes components, say your favorite cluster
autoscaler, maybe carpenter. This setup is not specific to AWS. You can use whatever cloud
provider that you use and as long as you adopt
their own Kubernetes controller, this system will work. So what are we gonna see here? Actually, this is the, probably
the most challenging piece is just making sure the video runs. So let's make sure and it, yes it does. So multi-cloud is easy, but
playing videos is super hard. And so we're actually gonna go from zero to a fully functional
deployable target within AWS for our developers. What are you gonna see? It's
a GitOps driven workflow. What is Git? It's just implementing
things like standard software development practices
like testing, automation and approval mechanisms. And in that manifest we're
gonna have non-overlapping IP ranges, specific
security configurations, observability and a deployment pipeline. And most importantly, deployment pipeline not only for our developers
to to deploy to that target, but actually to the cluster itself. Remember, declarative infrastructure. Every cluster has its own configuration and eventually Argo CD wants to get what's in Git into production. You probably saw in Argo that things are in a degraded state? That's fine, don't worry about it. The beauty of GitOps is
its eventual consistency. And so as we ping pong back and forth between the Argo UI, Cube CTL, an actual AWS console, I want to show you in kind of quasi real time, how
we build this system, right? VPC, EKS, pods and cluster components,
all in that type of layer. In this case we're just
checking on the health of two specific important components, the cilium operator and core DNS. And as you can see, those came up. All without having to
interact with a proprietary cloud vendor console. So let's go ahead and update our clusters. Again, lifecycle management. And in this case, Adobe has
updated our own tagging policy to make sure we properly
attribute all of the resources to a specific ethos cluster. Again, this starts with Git. I want to show you, I want
to call out what's not being shown to you in
this type of standard software development workflow. You're not gonna see an AWSCLI. You're not gonna see us grab IAM roles or access keys and secret keys. You're not gonna see us go ahead and update cloud formation templates because those don't exist in
other types of cloud providers. You need to put an
abstraction on top of that so you can actually drive machinery to manage the environment
in a multi-cloud world. As you can see, as we ping pong
back and forth between Argo, what's most important is
we want to get that tag applied to this specific
cluster because in this case, I wanna make sure I create
the demo in this video for you before something nefarious happens to it. So as you can see, Argo goes
ahead and picks up these, the config event- eventual consistency. And in this case, hey, what's the tag? This is a reinvent or, or
demo reinvent cluster in AWS. And as Argo goes ahead and process this we'll back, go back to AWS console and show you the VPCID with
a specific AWS tag applied. All right. Let's talk
about decommissioning. And before everybody gets
out and, and freaks out and say, wait a minute,
you can actually delete infrastructure via pull requests? Yes, you can,
(John chuckles) but it took us many, many, many quarters to get to this level of maturity, okay? Just like any software
lifecycle that you manage through a Git based workflow,
you need to have safeguards to prevent hard deletes and accidental or error prone type of steps. So what do we do? Okay,
we run tests, right? Tests are good for software. Linting, we do input validation, I also wanna make sure
that there are no PDBs to enforce on this cluster. And I also want to check my
ingress controller to make sure that there's no routes there. But again, that's all driven through software and observability. That's not driven for a human go ahead and clicking through consoles to say, hey, can I go ahead and
delete this cluster? And many, many organizations
forget about this most important piece of the
lifecycle, which is deletion. 'Cause if you don't delete,
you're gonna run into sprawl, waste and security issues. And as you can see, again, no consoles, it was all driven through Git. So let's talk about the real
impact of something like this. And this is, you know, a
typical executive scoreboard, but it's more about just numbers. It's about, hey, what are
kind of the- the what- how does this work that
we do transform our own development culture and lead
to positive business outcomes? We deal on an enormous scale at Adobe. And when you're dealing with a fleet of 300, 450 clusters, you need automation. So with this type of system,
we're able to deploy changes across this fleet three times faster. And we're also able to do
full Kubernetes cluster upgrades two times faster. We're also reducing our own
provisioning time by 25%. Adobe is a fast moving business. We have new markets
that we need to go into and building ethos clusters is essential. Finally, you should be
treating this like any other product that you manage. You should talk to your developers to say, hey, how is this working out? The response from our own developers around our fleet
management system has been overwhelmingly positive. So let's wrap up and I'd love
to share all of the things that we learned so you
don't necessarily have to go through the pain and
and trials that we did. Kubernetes is your friend, okay? And with any friendship
you need to invest. And if you don't invest, you're probably not gonna
have a friend anymore. And so how you invest is in your own team. Grow your team's own
knowledge of Kubernetes and get them to a place in
terms of platform engineering where you need them to be. You also need to automate. It is impossible at scale
to have human signal between events to say, hey,
I'm ready for the next step. You need to have GitOps space workloads that reduce manual errors and
accelerate your own delivery. There's a vibrant culture
and community out there that you can adopt. You don't have to go and
build all of this on your own. Adobe has gone all in and
really embraced the cloud native computing foundation or CNCF where I'm really happy to
say that last year in 2024, we were honored with our
highest end user award recognizing our own contributions
back to the community. Like, like I said earlier,
platform is product. Your end users are
never gonna use a system or they shouldn't be
using a system like this and exposing it. But you should be treating not only doing regular sustaining, engineering
and keeping it up to date, but you should be talking
to your own developers and saying, hey, do you like this system? Is it meeting the mark?
How do you iterate on that? Finally, cookie cutter scales. But when I go to a bakery, I
see lots of different cookies that I want to eat. And that's fine because
just like multi-cloud, every system has its own unique challenge and business requirements. You need to be ready to
have repeatable stamp setups regardless of the deployment
target or the cloud provider. This type of system enables
your developers to be happier. Happier developers lead to
happier and more productive teams and more productive teams leads
to better business outcomes and happier customers,
which is what we're all interested in at the end of the day. Thanks for listening. With
that, I, we'll hand it back to Gaurav to take us home. - Thank you John. And before we wrap up, I would
also like to (indistinct) some of the other reinvent
sessions in multi-cloud track that I would encourage
you to go and attend. I also would like to highlight
we have a multi-cloud kiosk at AWS village. And you can go there live
demos of what we just saw here, and also talk to some of our
(indistinct) cloud experts around your use cases. And then here are some of
the QR codes with links to curated resources
that you can reference for your multi-cloud journey. And last but not least, please do complete the session survey and give us your valuable feedback. And thank you again for
joining this talk today. - [John] Thank you.
- And myself and John are also available off stage
to answer any questions that you may have. Thank you again.
(audience applause)
---
video_id: 7FWolDYQiNk
video_url: https://www.youtube.com/watch?v=7FWolDYQiNk
is_generated: False
is_translatable: True
---

- Good evening. Thank you for turning up, those of you that did, to this last session of
the day in this theater. This is CNS 208: Enhancing
Container Security with Amazon Elastic Container Registry. My name's Liz Duke, and I'm a Principal Specialist
SA for Containers at AWS. I work with container customers
across the UK, Ireland, and the wider EMEA region. Every day, thousands of organizations successfully deploy containers, powering everything from your
favorite streaming services to critical healthcare applications. Now, behind these seamless experiences are teams just like yours. And today, I'm excited
to talk to you about how AWS services can work together to make container security
feel less like a checkpoint and more like an accelerator, building in security to every stage of your container journey. Okay, let's dive in. So what are the sorts of
challenges for security that you have when you're
running container workloads? Well, while you may start off small with only a few container images, typically that doesn't last and you end up managing hundreds or even thousands of container images. And each of these images needs
to be checked for security, not only when they're built but throughout the lifecycle
of that container image. And the more images you have, the more finding security problems is like finding a needle in a haystack. We expect container images
to be switched out often. With this pace and this speed of change comes the ability for mistakes to affect your security profile. And container images are
built up from multiple layers, typically starting off from
like a base OS image layer and then adding in your application, bringing in any libraries,
any further dependencies, and maybe even some
open source components. All of these layers need, again, checking for any container security issues. So, how do we do this? We follow and we build a
container supply chain. A container supply chain is built up of the components used to build
and store container images and deliver them with a
container orchestrator. So we start from your code repository, this is where your application code lives. And then we build a container
image up from multiple layers, and each of these layers can
be pulled from almost anywhere dependent on your security constraints. Once we built the image, we need to store it somewhere, and that's where your container
registry comes into play. From then on, we use a
container orchestrator to deploy your images. Now, this last step isn't typically part of
a container supply chain, but I've included it because I think it's really important, and that's to monitor your images when they're up and running to see if they're behaving
like you expect them to. So let's look at how
we can add security in to each of these stages of
your container supply chain. So, ideally for security, you want to automate all the stages of your container supply chain. And so that's from code
submission to your repository all the way through to
deploying your images on your running workloads
with your orchestrator. For this, we can use a service, which is AWS CodePipeline. Now, AWS CodePipeline works with Identity and Access Management, so it can integrate to other
AWS services using that. And when you automate
this using a pipeline, you end up with taking
humans out of the loop, which is a great improvement
for your security. So, you start off and you submit or a developer submits code
into your code repository. Now, typically these days, this is some form of Git repository. And so, when that code is submitted, when it's pushed to the repository, CodePipeline will be notified and then it will take this new submission using a temporary access token. Once we've got the code
from your repository, we want to put this code
together with the other layers to build your container image, and you could use AWS CodeBuild for that. Now, at this stage, once you've built your image, you might want to sign that image to make sure that it's not
changed from when you build it to when you deploy it, and you could use a service
like AWS Signer to do that. So, let me introduce
you to the secret weapon for your container security
in your build supply chain, and that is Amazon Elastic
Container Registry. It not only stores your container images, but it can also check
them for vulnerabilities. And finally, we're gonna
deploy our container images using your orchestrator of choice. Now, within AWS, we have two main container orchestrators, and they are Amazon ECS,
Elastic Container Service, and Amazon EKS, the
Elastic Kubernetes Service. So, once you've confirmed
everything's good to go from the build point of view, then you want to get those
images into your workload. So, let's take a closer look at Amazon ECR and the security benefits that it brings. Amazon ECR is a fully-managed
docker registry. So there's a private ECR registry that is supplied to each
and every AWS account. With ECR, what you can do is you can store and
distribute your docker images, open container images or any other OCI compatible artifacts. When you transfer an image to ECR, you do so over HTTPS, so again, we're bringing
security in there, and your container images are automatically encrypted at rest. Amazon ECR is highly available, it's got redundant architecture, and it actually serves
billions of image pulls each and every single day. Now, remember that needle
in the haystack problem I was talking about? With Amazon ECR, you can use lifecycle policies, and they will automatically
clean up on your behalf the old container images. Amazon ECR also comes with
vulnerability scanning options, which I'll go into in a little while. So that means that you know when you push an image to Amazon ECR and it's scanned it whether you have any vulnerability
issues with those images. So, with ECR, you can also connect to
an upstream repository and cache images in your
local ECR repository and then keep those images
updated using pull through cache. So, some of the inbuilt
security features in Amazon ECR are the following. So, Amazon ECR, again, like other AWS services, integrates with Identity
and Access Management. And so, that means you can
control the permissions from who's allowed to push or write images into your container registry, but also who's allowed to pull those images from your registry. And the reasons why this is important is to control people who
can pull from your registry because within your container images, quite often you will have
your company IP in there, so you wanna protect that IP, you wanna restrict who can
get those container images. And by creating the right IAM permissions, you can control that. As for pushing images
into your repositories, you want to restrict who can
push into your repository because you wanna make sure that all the images in your repositories conform to your company security profile. So ideally, you wanna
build those security checks into your pipeline as
you're building the images, and you don't want
people to be able to push directly into repositories because they could include pieces of code or vulnerabilities that
haven't been checked. Now, Amazon ECR uses AWS S3 for the storage for your container images. So all of these images
are encrypted at rest and we use an AWS signed key for that, an AWS owned key. Now, we don't charge
you any extra for this and this comes with
AES-256 encryption inbuilt. If you decide that you want to control
that encryption yourself, you can use your own KMS
key with ECR to do that. Amazon ECR also supports use
of private VPC endpoints. What this means is that any data transferred to and from your registry will do so without leaving
the Amazon network itself. And if this is the only
type of access you need is to pull down container images, then that means you don't
actually need a NAT gateway or an internet gateway from your VPC. So, I mentioned that Amazon ECR helps with vulnerability scanning. Now, there are two types of
vulnerability scanning with ECR. Back in 2019, we released a basic scanning
option for Amazon ECR, really just to encourage our
customers to scan images, and this was based on Clair, an open source vulnerability scanner, and it scans for OS vulnerabilities only. Now, recently we updated that to use Amazon's own
proprietary native technology, and this goes across
more operating systems and more up-to-date operating systems. And by default, all new registries are opted into this Amazon-owned scanning technology. So what happens when you
push an image to ECR? So when you push an image, either you or the
pipeline pushes an image, the scanning technology kicks in and scans that image for
any OS vulnerabilities. Any results from that, that any conflicts with any open CVEs are returned to you
within the ECR interface. But if you wanna take your
scanning to the next level, you can opt into enhanced
container scanning, and this is where Amazon ECR integrates with Amazon Inspector. Now, Amazon Inspector not only
scans for OS vulnerabilities but also for application
package vulnerabilities as well. So, with the Inspector scanning included, you can not only scan
like your standard images, but images that are built from scratch, distroless images and Chainguard images, all of these can cause problems with more traditional
vulnerability scanners. So again, what happens is when you or your
pipeline pushes an image to a registry that you have
opted into enhanced scanning. Now, Amazon Inspector kicks in, scans that image for any application and
any OS vulnerabilities. But then what it does is it
prioritizes those findings and sends them to Security Hub. Why this is important is it now gives you an
audit trail to follow, and that's a critical component
for a lot of our customers. If there's an exploit available, it will tell you that about the image. If there's a remediation
available for the exploit, it will also tell you that. And nobody here is running any
end-of-life software, right? Because it will scan for that
and tell you that as well. Now, in addition to the enhanced scanning, you can tell it that you
want continuous scanning. What continuous scanning means is that whenever any new vulnerabilities are added to the Inspector
vulnerability database, then your existing container images are also checked to see
if they are affected by those vulnerabilities. And if your images that
you've already put out and used in the workload are affected, you want to know, right, which of my clusters is that running in? And what part of the
cluster is that running in? Because it's no use you
knowing about vulnerabilities if you don't know where
those images are running. With the integrations
with ECR and Inspector now with both Amazon ECS and Amazon EKS, it will tell you where those
affected images are running down to the task and pod
level in your clusters, so you not only know
you've got affected images, you know where they're running. Pretty handy, right? So, that brings us on to signing your images. So, you may think that
because you built your image and you scanned it, then you're good to go. But code signing is an
industry standard technique to ensure that the code that you checked is the same as the code that you run. Now, as I mentioned during
the container supply chain, that you can decide to
integrate AWS Signer in your pipeline as you've built the
image to sign that image, and then so that you
know that it is unaltered from when you built it. But with that, you have
to build that integration into each and every pipeline. So, now I'm excited to
be able to tell you, we launched this, I think, last week. The Amazon Elastic Container Registry now has fully managed
container image signing that integrates with AWS Signer. So, you can enable this
with just a few clicks in the console or single CLI command, and now you've got a
centralized image signing tool so you don't have to integrate
in each and every pipeline. If you want to reconfirm your image before that image is then
deployed onto your workload, and I strongly suggest that you do that, Amazon ECR also stores the signatures from your signed images alongside the images in the registry. And so with Amazon EKS, you can use a combination of Gatekeeper and Ratify or Kyverno to detect that an image that's about to be used in the EKS cluster has a different signature from the one that was
confirmed as good to go, and it will stop that. With Amazon ECS, you can also use lifecycle
hooks combined with Lambda. And with that, you can check and we've got a guide
as to how to do this, you can either say, "Okay, I know that image doesn't
match the signature, I just want to be notified about it," or you can configure it
to block those images from being used in ECS as well. So it's really important for you to think about combining this with your container pipeline. And I also mentioned about
monitoring your running images for unusual or suspicious behavior, and this is where Amazon
GuardDuty comes in. Amazon GuardDuty supports
runtime detection for both Amazon ECS and Amazon EKS. What it does is it looks
for any unusual behavior, so behavior like your containers trying to connect out to the IPs of known Command-and-Control servers to make them part of a botnet. Bitcoin mining, unless you're actually Bitcoin mining in your container workload, it's looking for that sort of activity. It's also looking to
see if your containers are trying to exfiltrate
data out of your solution. You wanna know about this, especially if it's exfiltrating data that you didn't expect it to be. So again, you can enable GuardDuty for all of your clusters or for a subset of your clusters on both ECS and EKS. So, with that, I'd like to come to some key
takeaways from this session. Amazon ECR stores and transmits your container images securely. It also enables you to both scan your images
for vulnerabilities and to sign your images. Your security posture
and your security profile needs to be continually evolving
as security attacks evolve. And you should always think
about whether you can integrate signing into your container workload so that you can attest that the images that you've decided are good to go from a
security point of view are the ones that are actually
running in your solution. We have some other
sessions that are running, well, we have quite a lot of
sessions that are running, let's face it, at re:Invent, but these are some security ones. And there's EKS and ECS ones here. We've got workshops, we've got builder sessions, we've got short talks. Now, if you're new to containers and you want to learn about ECS or EKS, we have two training programs, these are digital badges, and these take you from knowing nothing about container images through to knowing how each
of the services is built up and how you need to think
about those services. These are self-paced, so you can go at your own speed. And then at the end there's an assessment that if you do the assessment and pass that assessment, you will get a digital badge that you can then share
with your employers, with your social network, and these are all free. Yeah, so you can do this
on our training platform. So, we've put together
some session resources, so all of our container sessions are linked in a Git repository. So, if you scan the QR code, you will be taken to a Git repository, and that has additional resources for all of our container sessions. It will also include
some additional resources from this container session. So, hopefully it wasn't too painful to come to the last session
of the day at this theater. Thank you for coming, and please fill out the
session survey in the app. Thank you!
---
video_id: GXIr7h5aL2o
video_url: https://www.youtube.com/watch?v=GXIr7h5aL2o
is_generated: False
is_translatable: True
---

- Okay. Well, welcome
to our session called From Metrics to Management:
Practical Observability on EKS. So starting to a good start. My name is Dale Orders and
I'm here with Emil Lubikowski, who is going to be joining me today in presenting this session. So to start, you'll
see on the screen here, we have the agenda for today's session. We're gonna start by obviously
introducing ourselves. We're then going to talk
about what observability is. So just a very brief
introduction to observability. We're going to then discuss how we can make our
applications observable. We are then going to delve
into two AWS services, Amazon Managed Service for Prometheus and Amazon Managed Grafana, before we conclude our
presentation with a short demo. So that is today's agenda. As I said, my name is Dale Orders. I'm a software engineer at Five9 and I'm joined by Emil Lubikowski. - Emil Lubikowski and I'm AWS DevOps - DevOps engineer. And we're
both community builders, so we're very excited to
be here today with you to discuss observability. As I said, we're gonna
first define exactly what we mean when we
talk about observability. So observability is about a
extracting actionable insights. So it's insights that you can generate to be able to assess and
improve the performance, health, and behavior of your application. And that's a really important point there. We wanna look at the
performance, behavior, and the health of the application. Observability should
be a continuous cycle. So with observability, it's
not something you do one time and then you finish. It's something that you
should be doing in a continuous iteration. As you see on the screen
here, we start by detecting the specific metrics
that we are looking for. We then have to investigate
what those metrics mean. We have to remediate any
issues that we find when we, that we find through our investigations. And finally, we have
to assess whether those remediations have been successful. So it's a continuous cycle
that we have to do to ensure that observability is
effective, it's truly effective. So why is observability important? Well, there's many reasons, but for us it enables us
to be able to gain insight or visibility into the
health of our application. It means that we are able
to better troubleshoot any issues that arise. Importantly, it allows us to deliver a superior customer experience. And obviously that is something
that is very important. We do build for the customer. And then finally, it
helps us in being able to control our costs. And obviously that too
is equally important. So when we say observability, what signals are we talking about? Well, we are talking about metrics. So we can think about metrics
as being, do I have a problem? It also includes traces. So traces are, where is the problem? So do I have a problem? Where is the problem located? It also includes logs. So what is causing the problem? And finally, it includes profile. So how is the code behaving? It gives you that insight
into the specifics around your code base. So those are the four metrics
or observability signals that we need to be aware of
when we conduct observability or when we design an observability system. How exactly does that
relate to our application? So when we have metrics,
we're thinking about why is my application 25%
slower than last week? So we have to be able to
interpret that information and understand that that
is referring to a metric in our application. Traces. What are the
dependencies for these services, for this service? Again, looking at how one
specific service relates to the performance of another
service in our application. It also includes logs. So why won't my database
start after this update? So there we are trying
to troubleshoot an issue that has arisen with our application. And it includes profiles. So could there be a
memory leak in my code? And together, all of these
observability signals allow us to better track and achieve our SLO and SLA compliance targets. So it's not something we do
simply for the sake of it, we do it because it has a
broader purpose behind it. But then the question becomes, how do we make our
applications observable? We know observability is important, but how do we actually
introduce observability into our application? Well, one such way we
can do that is by the use of a particular AWS service known as Amazon Managed
Service for Prometheus. This is a fully managed
serverless Prometheus compatible monitoring service. So it is based on the Prometheus, which is an open source program, but it is, it is developed by Amazon. So it provides high availability, it is multi-AZ by design, and it provides the ability for you to gain greater insight
into the monitoring and the observable metrics
that are being produced by your application. It uses the Prometheus data
model and querying language, Prom MQ, which allows
for seamless monitoring of your containerized workloads. And we will see that in
the demo very shortly. What does that look like in
terms of our architecture? So you'll see here on the
screen, we have our application code, which we instrument with Prometheus, with the Prometheus SDK. We expose the metrics to
the Prometheus server, which is running on
the Kubernetes cluster. We're going to be using OpenTelemetry. So you can use either an
OTel or OpenTelemetry, or an AWS distro for
OpenTelemetry collector to collect and to aggregate the metrics. And then you can use a remote
write operation to send those metrics to Amazon
Managed Service for Prometheus. If we look at that in a
little bit more detail, we see that we have our collector. This collector is going
to use both a receiver and an exporter to extract, to process, and to export the data. So in this case here, I am producing two pipelines
on the left-hand side here. I'm producing a tracers pipeline, which is going to export the
data to Amazon AWS X-ray. And on the right-hand side,
I have a metrics pipeline which is going to export the data to Amazon Managed Service for Prometheus. So this is one such way
that you could design your application to be more observable. But what are some of the
best practices when it comes to using this specific service? So you should be using
private link and IAM so that your metrics go
securely from trusted sources. You can reduce your costs by
increasing the scrape interval and also adjusting the
relabel config filter to better suit the specific requirements of your application. You can use a retention
period that is appropriate for the data that you're storing. If you're not going to be
using, if not gonna be needing your data for long periods of time, then it's more appropriate to
reduce that retention period. You can run more than one container to ensure high availability
of your pipeline. And finally, you can use
consistent identifiers to enable correlation of data, so you can better correlate
data from one pipeline to the next. With that said, there is one
other service that you can use and I'm gonna be passing it
to Emil to tell you about that specific service. Here you are. - Thanks for the voice. Yeah, so the next service,
fully managed, is Amazon, Amazon Managed Grafana. In the (indistinct)
abbreviation AMG, I found out. So Grafana is actually this service you possibly already know. Some of you already were using Grafana. As I mentioned, AWS fully
managed that for us. So it's a widely-used and open source analytics visualization platform. So sooner, we'll be showing how to create some visualization for that. And it is also used for
alerting, creating metrics and traces, et cetera. It provides for us some interface. And that's it. - Okay. Alright. - So AMG actually works on
top of our current setup, already mentioned. So we've got our application, we are scraping some data
with OTel, ADOT, and AMP. Then we are moving it to
AMG. And AMG, I mean Grafana. We're configured this this
way to show that to the user, show that to us. And as previously mentioned, they mentioned we can use here OTel, ADOT, to get those metrics, and we can do it in a few ways. We can push that to multiple services, to open service, OpenSearch
cloud (indistinct). - [Audience] (indistinct) - Sorry? - [Audience] (indistinct) - Oh, okay. (indistinct) And also push the AWS X-Ray. But finally, we will focus
on the way where we are pushing it through AMP Prometheus and then to Grafana. As for AMP, also for AMG,
there are some best practices. Mostly, we are doing it this way to make our dashboards useful, so clear. And to respond for
questions, simple questions. So best practices also are
behind so we can see it. So one I'm really focused on is that when you are creating dashboards, make sure each one tells a clear story. So answers a specific question to make it really
specific and transparent. And now the demo. So we are going to visualize
our web-quickstart cluster, cluster with some already
provisioned resources and observability. On observability, up the top, we already see the
Prometheus metrics section. So we can here add the
scraper, providing scraper. We can also create a new workspace and put some other configuration. But mostly, focus on the configuration, which is like a YAML file, which specifies the best
practices that they mentioned. So scrape interval, what we'll have there. Relabel configs, like,
label map for mapping. Some labels between agents
also keep for filtering, only those one which we
are really interested for. After created the scraper, we can see that it's
already visible also in AMP. In AMP there is, yeah, scraper visible. There's also workspace visible. We created workspaces
like on our collection, where we can write and query
our data already collected. We can also set here the retention period, which is really important
here just for, from the costs and the management perspective. Now we can set up also
the ingest our collection. There's really cool
documentation on AWS side how to follow those steps. There are like two steps here. First is obviously to create a IM role, which allows us to, to
communicate between the services. And the next step will be... Okay, before we go to next step, we just have to verify the role. That after running the all
steps, that it is already here, we can use it. And if this is already there,
yeah, we see that, the rights, allowing us to play with
this service already there. And there will be another step
with providing the agents. And once again, there are, there is pretty extensive
documentation available. So even if you're doing it for
the first time, it is easier, easy for us to practice
that and to set up quickly. Even for this purpose, I just use the, we just use the default naming so it will be quickly available
that it is already there in the (indistinct) in our EKS deployed. So as we mentioned that the setup works, that Prometheus agents has to be deployed on our cluster, on our app, let's say, to write our data, our logs to our AMP. Yeah, AMP service, which will be showing
that in scraping that and pushing that to Grafana. Now we got, finally, the Grafana. Grafana is, as you can see,
another really fully managed, really simple to to be
configured service in AWS. There's just a couple of
things to be configured here. We can focus, we will
focus on our data source, which will be AMP Prometheus. And here what we have to
create is just a workspace. And after the creation, we
see that it's already done. All the thing right now we have to focus is the configure the Grafana
itself, which is after that, after this couple steps is
already provisioned for us. So after log in, the couple
of things we have to do is obviously just to set the data source. As you can see, it's
already previously done. But we can just (indistinct)
by adding the new one. The only thing we have to focus here is the connection, obviously, because service is
pretty clear before that. So after the deployment, we just have to put points to our AMP, where we are getting the data from. And put the authentication down, which is usually by the default
set to SigV4 authorization. And it is using the IAM
role for sufficient, to provide sufficient rights. And the last step,
possibly the final stage, is creating the visualizations
on our dashboards. Before we can do that,
let's just focus once again on the (indistinct) for our deployments. On our deployments we can
see there are some labels like namespace, image selectors. So you can see that there
is an up 2000, up 2048. And on the very basic view visualizations, you can see this is already created. But let us go and edit to see, to play a little bit with those filters. So we can see the labels
already visible previously, already are here. Let's just clean it up a little bit. You can refresh, you
can test your queries. See the differences now,
before, without that filter? It looks like it is
showing some historic data, some previously we
would like to filter out because it's making only a burden. And this way, we can play
more, we can add more, more custom and more
specific labels for us. And the summary. So this way, we can see that
we can pretty easily create observability using only
fully managed AWS services. Prometheus and Grafana, where
they are fully managed by AWS, It's like with other
(indistinct) and other services, really not our problem,
let's say, to manage them. And, at this point, we can really focus on our observability, so on our SLO, SLA, SLI also. And that's it. - Great.
- If you would like it, - Great. All right. And as Emil said, once we
have achieved those metrics, we can ensure that our
customer remains happy. Which is ultimately the
goal of observability, making sure that we can
deliver on a quality product. So with that being said, we
wanna thank you for coming to today's talk. If you wish to connect with either of us, our LinkedIns are on the
screen here, the QR code. And if you have any other questions, you're welcome to stay
and approach either of us. We are very happy to take any
questions that you may have. Thank you. (audience clapping)
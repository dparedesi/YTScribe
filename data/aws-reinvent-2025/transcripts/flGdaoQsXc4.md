---
video_id: flGdaoQsXc4
video_url: https://www.youtube.com/watch?v=flGdaoQsXc4
is_generated: False
is_translatable: True
---

- All right, welcome to re:Invent. Are you guys all excited? We have... All right, I
like that spirit over there. I guess we have over 2,000 sessions and workshops lined up this week, so make the most out of it. Any first timers over here for re:Invent? All right, that's great. I'm going to recommend to install or activate your pedometer on your phone. Count the number of steps
you're gonna walk this week, and then I'm telling you, you're gonna be pleasantly surprised. A warm welcome to this
presentation. My name is Vin Dahake. I lead solutions architect
team for ISV Private Equity. I've been with AWS for five years now and I'm based out of New York City. Gonna let my partner introduce himself. - Yeah, and thank you, Vin.
Really a pleasure to be here. My name is Sean Stauth. I'm Global Director of AI
and Machine Learning at Qlik, and I have the opportunity to work with our customers worldwide in a variety of different industries
on their cutting-edge AI and machine learning solutions. - All right, thanks, Sean. - All right, before we
get started, you know, a quick show of hands, how many of you have built
machine learning applications, analytics applications that have worked for the first time in production? Oh, that's good. That's good. We have few hands up
over here. It's not easy. I mean, I was hoping everybody
would raise their hand and I would just walk
off from the stage away, say thank you very much, but
this is the reason we are here. You know, building
machine learning platforms which are enterprise ready,
scalable is not easy. And that's why we have Qlik
at our doorsteps today. But before we get started, let me tell you a little bit about Qlik. Qlik has been a global leader for the last 30 years
in data analytics space. They have helped companies,
you know, transform by processing data, getting
insights from the data. Qlik has three core
expertise that we are seeing. They've done a lot of work in
real-time data integration. They've done work in analytics,
business intelligence, visualization, and
third, AI, ML and AutoML. And that's the reason we're here to discuss about Qlik Predict. Today Qlik has over 40,000 customers across 100 different countries. And in 2004, AWS and Qlik, we signed a strategic
collaboration agreement. And I'm excited to tell you the result of this agreement is Qlik Predict. This is a fully managed multi-tenant, global machine learning SaaS platform, which is entirely built on AWS. All right, let's take a quick
look at the agenda over here. You know, we will talk about what this machine learning
predictive analytics platform is. We will do a deep dive
into the architecture. We will look at, you know,
some of the case studies and then we'll talk about
the challenges that we faced and how we can learn from that. 70% of forecasting programs fail. Really, 70%. This is not an academic study. This is, you know, real money,
real business, you know, real challenges that people face. Most of the traditional
forecasting programs fail because, you know, they
look at data in isolation. You know, that's not how real world is. We have seen, you know,
when programs are doing, let's say, for example, sales forecasting, they look at okay, what was
my sales data for last month? It was X so maybe next
month is X plus delta. But that's not how it works in reality. There are multiple variables that need to be taken into consideration, you know, when you're doing forecasting. It could be seasonality,
it is your inventory, economic conditions, it could
be your competitor's action. There are multiple factors. As a matter of fact, there could be up to 50 different factors that
can impact your forecasting. You know, simple models
probably can look at seasonality and make predictions, but for this particular case, when we have 50 plus different variables which interact with each other, we need complex, advanced algorithms like encoder-decoder, perceptron, or recurrent neural networks
to do the forecasting. These models are very
computationally intensive and they need GPUs to, you
know, perform the calculations. As I mentioned, you know,
we've worked with Qlik and we formed this strategic
collaboration agreement and I'm happy, the result of
that was building Qlik Predict. Sean, you wanna share a
little bit more story? - Yeah, yeah, and thank you
because as VIN mentioned, this opportunity is massive and with machine learning, real companies are getting massive results around their supply
chains, their logistics, around their HR and more. And so to start to share a
quick story around a company called Software Logistik
Artland or SLA in Germany. They have a very complex
network of suppliers, distributors, manufacturing that they have to run on a daily basis where even small changes in
their operations can lead to massive impacts around
finances and staffing. And so with Qlik Predict, they're able to build a
forecasting capability and able predict over with
90% accuracy the demand that they needed to
produce every single month. And that led to a 50% reduction
in annual planning needs. And the result is that while they're... This is really complex, they
have a business that is dynamic and they need a capability
that can match that reality. And so today we're talking
about taking the next leap, having a multivariate
forecasting capability that can have smarter
forecasting at a global scale. And so to start this stage, I wanna talk a little bit
about what machine learning is and what AutoML is,
automated machine learning and why the demands of time series are fundamentally different. So machine learning is being able to predict future results
based on past occurrences and understand why things are happening so that you can take a corrective action. And what automated machine
learning is taking a lot of the time-consuming tasks,
whether data preparation, feature engineering, ML
selection, ModelOps, and more so that you can deploy these at scale where they're needed for the business. Time series modeling is the
subset of machine learning where you're looking at forecasting on a continuous time window. Let me give you an example
of why this is needed. If we think about retail,
retail is a really good example and we work with retail
companies worldwide. In retail you have
products, you have SKUs, you have customers, you have
locations, you have online, you have retail, you have a multitude of different factors that are impacting your business
every day and in real time. This leads to a web of
exponential dependencies where one factor is actually
in fact impacting another. This leads to billions of interactions. And traditionally, a
lot of the forecasting has been univariate. And what this means is looking
at one historical variable to forecast a future result. But as mentioned, in reality,
businesses are complex, they're dynamic, there are thousands of different interactions
from channels to products. Even weather has a large
impact on business operations. And each added input leads to a multiplying effect of complexity. And this is why we need
multivariate time series, the ability to capture all
these different signals to create an accurate, actionable forecast where you can run your business. But this also leads to a
massive compute challenge, billions of potential interactions. And so today, this is why
we're happy to announce and talk about our multivariate
time series capability with AWS partnership that's based on GPUs and elastic just-in-time compute at scale. - All right, so why AWS? When Qlik was looking
to build this platform, they just didn't want, you
know, any cloud platform. They were looking for someone
who can help them scale and build enterprise, you know, models serving 40,000 customers
that they have today. There were three key things
that Qlik was looking at. Number one, you know, global
scale with data sovereignty. Today AWS has, I believe, 38 regions and three more coming up, and I probably will
stand corrected tomorrow when Matt Garman speaks and
maybe he'll announce a few more. But AWS has the global scale, which can serve Qlik's customers
in 100 different countries. Also, data sovereignty. As you're aware, you know,
with GDPR and other compliance, data needs to reside in that country. So AWS provides, you
know, the global scale, as well as data sovereignty
for building the application. Second, we talked about GPU scaling. GPUs are expensive, so you
need to be able to scale, as well as control the costs. So you need to be able to
scale down to zero as required. Third, we're looking at
enterprise-grade reliability. You know, when customers are
running these applications, they're mission-critical applications. They need a platform that needs to be up and running 99.9% of the time. Not only that, they also want
to have the right, you know, high availability,
disaster recovery in place for running these
mission-critical applications. Now let's take a quick
look at the architecture for Qlik Predict. Qlik Predict is a completely
cloud native application built on AWS. The three core components
that we've looked at is, you know, we have GPU clusters, we have regional training
models that we are using, as well as we have, you know,
scale-to-zero architecture to keep the costs low. Also, we have used several native services like Amazon MQ, we have Amazon S3, RDS. Also for realtime integration, we've leveraged webhooks and AWS Lambda. Sean, you wanna take us into this architecture, do a deep dive? - Well, what is so
amazing is that with AWS, we're able to take this to scale and make it a reality, these complex algorithms
that are necessary for these billions of
interactions in real time for our customers. We're talking about deep
neural architectures, GPU acceleration, elastic
compute at the reliability, the scalability, and with
the security requirements that our customer needs. And this is what AWS can deliver, which is forecasting for the real world. The compute demands are
enormous, learning relationships across thousands of variables,
thousands of signals that impact businesses
every day from supply chain to demand, seasonality,
the temporal patterns, the cross-correlation,
really looking at things in a systematic way, a holistic way that is more representative of a business. And to work with these
deep recurrent networks where the combination explode,
we need the GPU power. And that was so exciting
about working with Amazon to have these GPUs that can really do this in the speed that's necessary for the businesses to take action. It all starts with the API gateway where when a request is
routed, it can be routed to the correct region across the world where it's needed within its boundary so that it can meet the data sovereignty and regulations for
each particular region. The heavy lifting with EKS and Karpenter allows for
that just-in-time scaling of these workloads, being able to scale up to these massive demands when needed. And the GPU EC2 instances can be tuned for different neural workloads,
depending on the use case. And so together it's a
globally distributed, GPU-accelerated SaaS
capability, one SaaS capability for each region worldwide. - All right, that's great, Sean. So let's talk about the real
impact of building on AWS, you know, speed to market. You know, when Qlik was
building this platform, they didn't have to worry about, you know, building their infrastructure. Leveraging AWS's managed services, you know, they were training their models where competitors were
still trying to figure out how to set up their environment. That's the key over there. Scale, today Qlik runs
100,000 plus training jobs on a monthly basis. That's literally 3,300 jobs a day. So they have the scale
today to, you know, process and train the models. Third, let's look at, you
know, cost efficiency. Using Karpenter, as Sean mentioned, along with spot instances,
you can control your cost, you can bring down your
cost 60 to 70%, you know, leveraging a scale-to-zero architecture along with spot instances so that it doesn't become very expensive. Also look at, you know, regionality. You know, with the 38 regions
that we have today, you know, Qlik could easily expand to any new region to serve their customers and did not have to spend
a lot of time, you know, building their infrastructure over there. And finally is reliability. You know, leveraging,
as I mentioned, HADR, intelligent workload balancing,
you can take care of, you know, availability
of your application, see to it it's up and running - And so the results are amazing. Just looking at our telemetry, currently we have over 4,500
active users on Qlik Predict generating over 167,000 trained models and 1.5 billion predictions to date, all of this with over 99.99% uptime. And with our GPUs versus a CPU equivalent, we're able to run our training
jobs up to nine times faster. But I would really like
to talk about outcomes because it's the actual tangible business outcomes that matter. We of course work with
industries all across the world, from financial services,
healthcare, retail and more. I'd like to just share
a couple examples today. One with Appalachian Regional Healthcare, a hospital network
based on the East Coast, they're able to reduce
their patient no-shows, their patient cancellation rates, saving over $6 million a year. With Qlik Predict, what they're able to do is
not only be able to predict and understand why a
patient is going to cancel, but take the corrective action so that they can not only get the patient to show up when they need to, but also have better patient outcomes. In financial services, Integra Financial is a really good example of integrating this into
an external workflow with a real-time API for
automated lead scoring, which has led to today over $1
million in automated savings. And Village Roadshow,
which is an entertainment and hospitality group in
the Asia-Pacific region. They have very complex business operations with staffing, customers and more, and they were able to use Qlik
Predict to forecast demand and staffing for faster
data-driven decisions. - Thanks, Sean. All right, so what is
the key takeaway here? You know, building
enterprise-level machine learning SaaS platform isn't something
that is in the future. This is happening today. Qlik has built Predict platform, which is serving, you know, multiple enterprise-level customers. They are doing millions of predictions and saving customers, you
know, millions of dollars for the sales forecasting at this point. The three core things that
I want, you know, everybody to learn from this, you know,
number one is scale by design. You know, multi-tenancy isn't something that you can retrofit. It is expensive, as well
as, you know, risky. So think about multi-tenancy when you're building the
application from day one. Second, you know, is telemetry,
you know, and observability. See to it that you integrate observability in your application from day one. You know, when you're
running 100,000 jobs, your customers want to
have the transparency and see what is under the hood. So leverage like CloudWatch,
for example, to see to it that the customers have
the full visibility into the application that is running. And then finally, you know,
machine learning applications, they cannot run in silos. You know, integration is everything. See to it that you can
integrate your applications, along with your workflows so that you can derive
the maximum benefits. You can use APIs, you can use webhooks, you can use Lambda
event-driven architecture. You know, AWS has a lot of services that can help you do that. So leverage, like for
example, EventBridge. I mean, this will help you
integrate your application and not run in silos to get the maximum
business value out of it. All right, so this is an excellent example where you've seen how Qlik
and AWS work together. You know, we had a strategic
collaboration agreement. We leveraged Qlik's domain expertise with AWS's global infrastructure to make Qlik Predict happen, which is saving customers
millions of dollars doing, you know, sales, financial, even operations predictions at this point. Qlik Predict is also
available on AWS Marketplace. I encourage all of you guys to, you know, take a look at it and you can
see it actually up and running where you can build a machine learning job with absolutely like very little code. You can take the maximum use of the machine learning models over there. - All right, Sean, do you wanna? - Yeah, and so really thanks for having this conversation today. Please come visit us at our booth, 1727. Happy to talk about our journey in building this architecture. We have some engineers here as well to talk about their experiences
and also your challenges and aspirations around machine learning and multivariate time series. And so really happy to be here today. - Thanks, Sean, my name is Vin and I'll be around if you
guys have any questions. More than happy to answer them.
Thank you, enjoy re:Invent.
---
video_id: Me14ltJ8WWE
video_url: https://www.youtube.com/watch?v=Me14ltJ8WWE
is_generated: False
is_translatable: True
---

- A few weeks ago I was baking
cookies with my daughter. This is what we are always doing. She's mixing the dough and I'm the one who is baking the cookies. I opened the oven, I found a tray. Half of the cookies were burned. We tried to figure out, but my daughter was looking
like this, her hand full of flour and she asking me,
"What went wrong, Baba?" To be honest with you, I don't know because the recipe didn't tell me the butter was too soft or even the oven didn't
mention, do we have half of the oven hotter
than the other half or not? This is what hits me
because if this is happening inside any manufacturing,
what will happen? You have the data, you have the sensors are doing a notifications for your system. You have a system is recording this. You have a machines that is reporting those kind of informations, but at the end they are always disconnected. This kind of silent moment. This is what we are trying to solve today. Today I'm going to show you how AWS Serverless
architecture along with GenAI can build a connected manufacturer integrated with an AI system to have a solid understanding
of your manufacturer. My name is Mohamed Salah, working as a solution architect at AWS, looking after public
sector in the Middle East. My job at AWS is helping
different customers solving similar problems. Picture this, same silent inside the factory. Machine stops, production line pause, and everyone starts running around. Every minute, your products are not made. Your orders got delayed and cost pile up. This silence, this helpless pause, what we are calling unplanned downtime. The top 500 manufacturers globally, this silence cost them 1.4 trillion US dollar every year. They are losing around
11% of their revenues. To make it much more clear,
this is equivalent to the GDP of a nation like Spain. When we take a closer
look about this, we found it has three different issues. First, is a data silo. Your production line consists
of different machines, four or five different machines and each machines has its own data sources or different
data informations. You need to report those informations and those informations
are completely recorded in a separate database. It will end up, you have
five machines as part of your production line, each
machine has its own database but you don't have this
kind of a correlation to understand what happened end to end. Yes, the data are there
but it is disconnected. Second is a scale gap.
It's all about people. It's all about having in each factory, you will have this kind
of an expert and seniors, they can understand what
exactly happening on the ground. They can give you from
the sound of the mixer, they can tell you there
is an over-mixing here. From the oven, this oven
is having a problem. This is hotter in left side than the right side. This kind of knowledge, if those experts are not
there, this kind of knowledge will end up that you
are not able to operate your production line correctly because junior operators
will stay in the line, receiving warnings but they
will not be able to act. This means that the knowledge
are there but are not shared. Third one, which is when
this silence became visible because once this silence
happened the production line will get a product delayed and
the orders will get delayed. Why? Because you have a multiple
data sources at the end. At the same time, you don't
have this kind of an expertise that can analyze those data sources. We thought about how we can solve this. We started with a simple solution. Let's sort of think of a data link. As you can see here, we have
a multiple data sources. We have a telemetry data and alarms. We have an environmental
data and we have a document and standard operation procedures. By implementing those data sources and having this in one data lake, we found another problem,
which is the integrations. Each data source has its own integrations. As you can see, some of the data sources has a modern IoT integration, MQTT or (indistinct) or even
you have a legacy integrations for a document using your SFTP. What we thought about why not to implement AWS Garnet framework to have one single unified API to absorb this
different types of integrations and convert your data in a modeled data where you can have integration between your different IoT
devices in one graph database. This will build the relations
between different things. Once you got this data
lake, you will be able to have a different
consumers for this data lake. One of them is QuickSight at the dashboard and one of them building a
replica of your production line. This replica, what we are
calling a digital twin. Let's have a closer look, where you can have, on the left side, this is your production line. This is what exactly
happening on the ground. You understand what is the problem. As you can see, the cookie and inspector is telling
you cookie are cracked and the machine state is down since five. With this dashboard you will achieve what we are calling a
connected data points. At the same time, you will
break this kind of data silos. The important part is skill gap. Yes, you have this expert but you don't have this
kind of knowledge sharing. What we thought about why not to implement a GenAI application to be
deployed over Amazon Bedrock and to let the operator integrate
with this, ask a question and chat with your data. As you can see, we are
fine-tuning the model and we are importing this
model inside Amazon Bedrock to expose this kind of
text and voice application. At the same time, you are
getting real-time data streamed using the Garnet
framework to your Bedrock engine. This is will give you
bridging the skill gap. Second, which is very important for the different cases,
the automation needed. You need to have this
kind of an automation every five minutes, understanding
what exactly happening under the hood, know the streams and then getting this
kind of recommendations according to what happening
and what data captured from different data sources and give a notification to an
operator to act accordingly. What we thought about why not
to have a full automation AI to act, to call APIs with different machines
to act accordingly. This is on a very high level how it works. You have a cookie inspector
here after the former, after the tunnel and this
inspector is inspecting just in a small language model, VLM, inspecting either the cookie are cracked or cookies misshaped or
cookies has air pockets. Let's say we take in cracked cookies. You are going to invoke Bedrock
with a vision language model and Bedrock will ask to
get multiple data sources. Production line standard
operation procedure, you can get machine alarms and data, you can get the telemetry data and get even the machine manuals. Once you are getting this
data source, you will be able to first send the automated
notifications to your operator. At the same time, you can expose this text and voice chatting application and accordingly you can take actions. This is what will happen to solve the problem automatically
without having a senior on the ground and without having a fully integrated data points. Here, on high-level
architecture, how it work. Let me show you in details. This is where the equipment
measurement will fit inside AWS Garnet framework and for AWS IoT Core, you will send the data using this lambda function NSGI will change the data model of your input to a different standard data model. Accordingly, you will have
an SAQS to do a decoupling between your S3, which is
here acting as a data lake, to consolidate all your
data points in one place. Second part, which is important
here is actions needed. Is it possible to have actions to update actions in your production line, to update the cookie mixer
to reduce the temperature, reduce the torque or do different actions? This can be done using an API
gateway to do those actions. This is the foundational part. The data preparation. We are doing here a data preparation because we need the model itself to understand how to respond to queries. The response can be structured
in a very detailed way to guide the operator
how to solve the problem and instructions should be
compliant, at the same time, should be safe and should
categorize this kind of safety. That's why we thought about
why not to fine-tune the model. To achieve this kind of skills and this kind of tone
needed for your model. We started with having
a multiple documents and multiple data sources. We are converting this to... We are transferring this to S3 and accordingly we having a step function. This step function will
act as a data pipeline. You are reading the document,
reading the PDF files, CSV files, text files, understanding what exactly
happening on the ground and then invoking a model to
generate a structured data. Why structured data is needed because if you are going
to fine-tune a model, you need a very structured data because if you are not
having a structured data, it's a kind of fine-tuning
hallucination machine. Accordingly, you will have an
output of a structured data and another output of a
structured data only for testing. This output will feed into a SageMaker AI foundation model operations where I will fine tune
the model using this, fine-tune the data and using what we are calling
instructed fine-tuning. Once I got this kind of artifacts or updated weights for my model, I can accordingly import the
model inside Amazon Bedrock. This step can be done in different ways. We prefer here to use a serverless
implementation by Bedrock and instead of deploying
this over a EC2 instance, this will end up, you have to
calculate the GP utilizations. You have to be aware
exactly what is happening under the hood to do a correct inferencing but just importing this over Bedrock will give you a unified API
to call a different versions of your imported model. Once you've got this and once you have this
Amazon Bedrock, we can go to the web application. The significance here of
using the web application is to expose this kind
of a chatting for a voice and data with your model. As you can see, we have
two different things here. First is the chatting
application with the React, the normal React over
S3 with lambda functions to invoke the model, here we are using something called Converse API. This Converse API is
giving you a flexibility and even the scalability to invoke any model versions from
your fine-tune model. Let's say you got a feedback,
thumbs up, about one of your models and this
model is doing great. However, you found an
issue in a production after 10 days, you can
roll back in a model by just changing the model
ID using the Converse API. The significance here is the Converse API remain the same signature of the API while changing a different model IDs. Second, which is the important part, is the notification part here. The notification here where
you can feed the model with the data captured every five minutes and then start digesting
those informations, comparing those informations with the fine-tune, the model, in order to give you a clear recommendations considering the compliance,
considering the severity, considering the needed steps
to be done on the ground. By doing this, you can have an SNS, SNS notifications to your
operator to notify them. You can act accordingly in this event in order to change
the needed actions. At the same time, you
can avail both options in the same place. This is on a very high
level the architecture where we started with
digesting the information here using a Garnet framework and then this is a foundational part where you are doing
here a data preparation and then fine-tuning the model and then you are having a
web application that connect with custom model
imported over the Bedrock. At this point of time, you have a AI application
that makes every single machine sensor and system are
speaking the same language. You are able to have a connected data points and connected
machines in one single place by having a Garnet
framework implementations to absorb this different types
of integrations in one place. Second, is you will be
able to have this kind of fine-tuning the model, importing the model inside Amazon Bedrock and giving you this kind of intelligency. Now, we understand you can explain what is happening on the ground, what changes and what will be done next and what is the recommendations needed. By implementing this, you are still having and you're still
generating much more data. This is what we are calling
a continuous learning and this is your gold. Once you have updated
informations, you still have room to improve your model and improve your accuracy of your model and getting much more
accurate information. This is what we are calling
a continuous learning. This is much-needed because as part of, you can see, as part of this implementation, there is a feedback implemented mechanism by the operator based on the
response came from the Bedrock. If this feedback sums up or
sums down, I can act accordingly and I can give updated, fine-tuned model based on this information. You can scan those QR codes. This is a Git triple
for the Garnet framework to have this kind of a conversion of your connected
devices, at the same time, the second QR code of how to implement a small language model and import the custom
model over the Bedrock. And last one, how to continue
updating your information, fine-tuning the model and the implementing machine-learning pipeline end to end. Now, it's your turn. You can start with a
small process, small data, you can understand
exactly what is happening under the ground. You can start with one production line, with multiple data source, implement those kind of
fine-tuning implementation, we did this full implementation
in just seven days. After implementing this
and importing the model, you will be able to gain more insights and enhance your model. Thank you.
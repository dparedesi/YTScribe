---
video_id: dqHjRlZSVNM
video_url: https://www.youtube.com/watch?v=dqHjRlZSVNM
is_generated: False
is_translatable: True
---

- Hello, my name, Maxim Geng and I'm head of R&D
for DevOps Technologies and Cloud Solutions at Bank CenterCredit. The topic of our presentation, hybrid architecture for generative AI to meet regulatory needs. Before we begin, a few words
about Bank CenterCredit. The bank, one of the leaders of the banking system in Kazakhstan. The bank has 20 branch and more than 150 offices. Service over three million clients and provides wide range of
services for private individuals and business clients. And also, we subscribe
for two Outpost racks in Q1 2024. Let's start with why
we decided to use cloud and what our goals were. All of IT infrastructure
was hosted locally into our own data centers, but
with growing business needs and limitation for local solutions, we decide to scale our
resources using cloud. Since different providers
have their own advantages, we chose a multi-cloud strategy. What goals did we see in using cloud? First goal is flexibility and scalability, and second, innovative
and competitiveness. Third goal is reliability
and fault tolerance. And fourth goal is economic efficiency. But at the same time, as a bank, we need to ensure compliance with regulatory requirements. First requirement is data transmission and storage must be encrypted, and the encryption key
must be stored in the bank. And second requirement is ensure anonymization customers' data during collection and processing. Basically on these requirements, we start our journey to
cloud with AWS Outposts. AWS Outposts is local private AWS cloud that store it in customers' data. We were one of the first in Kazakhstan who located this solution, placing racks in our own data centers, thereby all necessary requirements. We starting exploring and deploying basic managed AWS services in this solution, like as
managed virtual machines, Kubernetes basis and S3 storage. The bank's application
architecture core layer consist Kubernetes-based microservices. However, these workloads
will also execute large, more 20 clusters and we want to explore how we can migrate these
workloads using cloud. We start exploring and deploying managed
Kubernetes on AWS Outposts and later integrated it with
our internal bank services. And later, we approve this
same deploying with AWS and other clouds. And as a result, we got
the following diagram. This slide shows multi-cloud
microservice architecture for Kubernetes clusters. This is located in our
data centers in Outposts, as well as AWS cloud and Azure cloud. All of this combined
with centralized tools for deployment management and logging and load balancing. Returning to the
requirements for cloud usage, we'll discuss more about encryption implementation. For encryption, we used
AWS KMS encryption service. He has a feature, External Key Store, XKS, and this feature allowed
us to use local keys for encryption in cloud and now AWS KMS cloud servers
can use our local keys. This solution allowed
us to use our local keys for encryption in data
in services in cloud. And it also used XKS proxy that is used for local keys, can be transferred to cloud
to encryption service. And in our case, XKS proxy is located in our AWS Outposts. More about this case. This case is based on
principle of double encryption. In the cloud, encryption service AWS KMS uses data key to encrypt
data in AWS services. And in additional encryption, a root key is used that is located in our local on-premise and this key is an external key and it is more secure and we use it for our implementation. And so bank was interested in AI and ML-managed AWS services and GPU workloads for our projects. And we start continued integration based on this encryption realization. And we made architecture
for AI model training. This slide shows you
architecture of model training of our ACR models. To do this, we made synchronization between S3 Outposts to S3 cloud. You can see step one. After that, data can be
training in the cloud on EC2 GPU or SageMaker, you can see step two. And after that, the processed
data can be transferring back from S2 cloud to S3 Outposts. And finally, step four,
our internal services and services in EKS can interact directly with processed data. And all of stage, we use our local keys for encryption in data processing, transferring and storage. After this, we continued
integration with another service of machine learning. Its name is AWS Bedrock. And in this case, our local services and services in EKS Outposts
can interact directly with API agent, Bedrock. Our private endpoint secure connection and this, it's used in real time. And solution allowed
us to use all AI models that we can use in Bedrock. And this solution allowed
us to scale our workloads to any sizes. And also, in all stage
of data transferring, preparing and storage, we use
our local keys for encryption. And so as a result, by implementation, this architecture integration and encryption mechanism, we have created a technological foundation for our projects using AWS cloud services. That's all from me. Thank you. Aleksandr will tell you more
about data anonymization and the implementation
of real cases in bank. And thank you. - Yep. Hi there. My name is Alex Bernadskii. I'm
a solution architect in AWS. And in next 10 minutes, I will tell you about two
generative AI use cases, which Bank CenterCredit, or BCC, built on top of the hybrid architecture, which Maxim just showed you. But before, I must admit
that I was just an advisor for this project and most of
this brilliant job was done by the data science team of the bank. Unfortunately guys couldn't join us today in the full numbers, but
we Daria from this team. Daria, kudos to you and to
your amazing colleagues. Thanks for being with us. So I will tell you today about two cases. First one is fine tuning of ASR model. ASR stands for automatic
speech recognition and the second case is
implementation of internal HR-bot to assist BCC employees. We will start with the fine tuning. So first, I'll explain you
the reasons why bank decided to create custom model. Then I will show you the schema and we'll describe you the process, how actually fine tuning was performed. And then I will show you the results and some quantitative metrics. So there are in general two
reasons why bank decided to create a custom model. The thing is that majority of population in Kazakhstan
speak Kazakh language. There are also significant part of the population which speaks Russian, but there is also third option,
so-called mixed language, when the person speaks Kazakh and Russian at the same time, like two words in Kazakh
and one word in Russian. And you can imagine that there
are models on the market, I mean, ASR models, which can process the
Russian language pretty good. Also, some of them can work
with Kazakh language as well. But there is no model on the market which can work with the mixed language. And the first reason for the
bank was to create this model for the mixed language specifically. Then BCC stores the real data recordings, call center recordings, and with eight kilohertz frequency, which is quite good if you
want to save the storage. But the thing is most of the ASR models on the market, commercial or open source, they are trained with
the training datasets with 16 kilohertz. And again, you can
imagine that model trained with the 16 kilohertz
doesn't really perform well on the eight kilohertz dataset. Furthermore, Kazakh language is so-called low resource language. It means that if you search in the web for Kazakh language training
dataset for the ASR models, you will find just two datasets, both in 16 kilohertz by the way. And they are not super rich in terms of vocabulary and features. So the bank decided to
create its own custom dataset with eight kilohertz and
with enriched vocabulary based on the real call
center data recordings. That's the reason number two. And that's the schema, how
the process looks like. So I'll guide you through the process. Initially all call center
recordings were stored in a Hadoop cluster on
premise in BCC data center. Then each and every call
center recording file was splitted into two channels
for agent and for customer. And then each of the
channels were processed by voice activity detection. It means that bank got
rid of all the noise and all the silence in these recordings. And then this fragments
only with the voice were splitted into chunks, each chunk with variable
duration from two seconds to 20, depends on the
duration of the actual phrase. And then each of these
chunks were processed by a speech-to-text model, the previous version of
the speech-to-text model which bank had at that moment. And it gave the bank
the text representation of this audio file. So we now have audio
recording and the text. Then both of this data,
both of these files, both of these data
formats were transferred to the Outposts from Hadoop
cluster to the Outposts. Important question, why bank
didn't do all the pipeline on the Outposts? The thing is that BCC
Outposts configuration doesn't have GPUs. We can provide the Outposts with the GPU, but that's not the case
of the BCC Outposts. And for the speech-to-text
model, you need a GPU. So bank has certain amount of GPUs. It's enough to do medium size models, it's enough to do an
inference for these models, but it's not enough for the fine tuning. So they use the GPU power to
launch the previous generation of speech-to-text model to generate text and then put everything to Outposts, audio and the text, both,
and then processed text files with the name Entity Recognition model to identify all personal
information and sensitive data and confidential data in the text files. It was the hard requirement
from the internal security that none of this data should leave the security
perimeter of the bank. And all the chunks, all the files where this data were
identified was removed from the training dataset, both text files and the audio file. And now bank had, it's the
step number three by the way, so now bank had audio
file and the text files, both encrypted in the way like Maxim said with XKS internal keys and also cleans from all
personal data and sensitive data. Then it was converted into special format called mel spectrogram. If you never heard this
word before, don't panic. I'll explain it on the next slide. Just keep it in mind for a while, okay? And so this mel spectrograms were transferred from the S3 on Outposts to the S3 in the region, again encrypted with the external keys
without the sensitive data, fully compliant with all the regulations. And mel spectrograms, by
the way, it's not audio, it's not a text, it's
something very specific, I'll explain it. And this mel spectrograms were served as the training dataset for the fine tuning job in a SageMaker AI. And this fine tuning job
resulted in a certain number of model artifacts and these artifacts were
returned back on premise, and then hosted for inference
using the local GPU power. So bank used our cloud
power, our cloud GPUs for the fine tuning and then
take the model back on premise and host it for inference on premise. That's the process. So what is mel spectrogram? Mel spectrogram is literally
an image of the audio. And the data scientist can get
this format from audio file by applying Fourier
transformation on top of it and then also apply a male scale on top of the Fourier transformations. And it gives us, it gives data scientists the bidirectional representation of your audio when we
have axis x, which is time and we have axis y, which is frequency. And we also have a color,
which is amplitude. And this is, by the way,
kind of a best practice how data scientists prepare
the dataset for the ASR model. And BCC followed these best practices. So results. As you can see, results are pretty good because for all three languages, bank achieved significant
accuracy improvement. It's how many? 9% for Russian, it's 15% for Kazakh. And what is the most important, the most significant improvement
for the mixed language, which was the major goal
to do a custom model, it's 23% for the mixed language. And furthermore, this model appeared to be more cost efficient than the previous commercial
ASR solution that bank used and it allows bank to save
four million tenge every month. Tenge is the local Kazakh
currency if you don't know. So now this model works as a part of post-call analytics pipeline. This project considered to
be successful and bank plan to scale it further in the next year. To next case, HR-bot. There are several reasons why bank decided to implement HR-bot. Reason number one is to improve quality and velocity of HR responses. The reason number two is to stimulate the self-service
culture in the company. And the reason number three
is to refocus the HR employees to more strategic initiatives rather than some routine duties. And of course this chatbot
supposed to be compliant with internal and external regulations. And it means that none
of bank confidential data should leave the security perimeter, on-premise security perimeter. That's why bank used the technique which we call the hybrid RAG. RAG stands for
retrieval-augmentation generation, pretty famous thing. I think you all know what is it, right? And by using RAG, we kind of supply additional
context to the model. We provide the knowledge which model doesn't have out of the box. And this knowledge is the
internal HR policies of the bank. And as you can see from this schema, initially the HR knowledge
base was processed by embedding model using
the local GPU power and then resulting vectors were stored in the Postgres
database and Outposts because Postgres can be a vector database. I hope you know it. And the same process was
applied to the user prompts. Obviously chatbot has UI and when the user types in the prompt, this prompt goes to embedding model, embedding model then
converts it to vector, vector goes to the Postgres,
then the vector search works and it results with additional context from the Postgres vector database, which is actually additional
context from knowledge base. It added to the initial prompt of the user and then prompt plus extra
content sent to the cloud, to the region, from Outposts to the region to the service which we call AWS Bedrock. In Bedrock we have model Claude Sonnet 4.5 I think at the moment. And then model processes the prompt and additional context,
provides the response and send response back to
the chatbot on premise. That's the process. Regarding their results for the chatbot, according to the bank assessment, now roughly 70% of their HR request goes through this HR-bot, which is quite good. That definitely allow it to reduce the workload of the HR team. And what is even more important, bank collected the feedback
from the employees, whether they satisfied
with the chatbot or not, and feedback is mostly positive. This is super nice. So we would like to give you key takeaways from our session. First, Max regarding the platform. - First, we built a secure
hybrid multi-cloud platform that complies with legal requirements and tailored for bank business needs. And second, implemented
flexible, scalable, and cost-effective architecture that enables an innovative approach and high competitiveness. And second. - Good. And regarding the GenAI process. So the bank implemented
the fine tuning process for the generative AI model,
for ASR model specifically. This process relies on
the hybrid architecture with the key component of this
architecture Amazon Outposts. This process is fully
compliant with internal and external regulations. And the bank considered
to reuse the same approach for every other GenAI task to
leverage the cloud GPU force for the fine tuning and then use the actual model on premise. Regarding the HR-bot, with HR-bot, bank created
a successful example that GenAI can automate routine tasks. It set the footprint for the same project and bank plan to implement
the same project, but just in different functional areas, like IT support or procurement. So that's all for us for today.
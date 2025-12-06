---
video_id: xqb5i8RxmwE
video_url: https://www.youtube.com/watch?v=xqb5i8RxmwE
is_generated: False
is_translatable: True
---

- Thank you all for coming to Quantum Computing with Amazon Bracket: From Exploration to Enterprise. My name is Eric Kessler. I'm the general manager of Amazon Bracket, our quantum computing service by AWS, so you're gonna learn more about that, but I'm very excited to be joined today also by Michael Brett. He's the head of go-to-market
for quantum computing at AWS, and yeah, we're gonna give you
a little bit of an overview, what we have been up to at AWS, how we see the industry evolve, and what you can do today
already with this technology. To give you a little bit, an overview, what to expect today, I'm
gonna give you a little bit of an introduction of
what is quantum computing and where are we today. Then we're gonna go into
a bit of an overview of what we're doing at
AWS before we dive into hybrid quantum classical workloads and how we're supporting these type of cutting-edge workloads at AWS. And finally, we're
looking at one particular customer case study, which
was about drug design with AstraZeneca. And finally, we're gonna show you how you can get started
with quantum computing. But I wanted to get out of the gate here with addressing a very
common misconception about quantum computing. Namely, a quantum computer
is not a classical computer that just runs a little bit faster. As a matter of fact, quantum computers are actually very slow
compared to the clock cycles from classical computers. Instead, a quantum computer
can run a richer class of algorithms compared
to classical computers. And you may ask, why do we need a richer class of algorithms? We have our classical algorithms
and they work just fine. Well, it turns out there are
certain types of applications where all the algorithms that we know require an exponential overhead as the problem gets bigger and bigger, exponentially, the time that it needs, the memory that it needs,
other resources that it needs. And one of the prototypical
problems of that kind is to simulate quantum systems themselves. So this is kind of the
home turf applications of quantum computers. Because when we just look at the system, say particles, electrons, that behave, that interact with each other,
behave quantum mechanically, if we want to simulate them
with a classical computer, already 50 of those particles require supercomputing scale classical computing. And because it is exponential, if we go from 50 to 100 particles, it becomes completely out of reach for any computer today
and in the future, right? And of course, this idea
is almost the founding idea of quantum computing and
goes back a long time now from 1981 by Richard Feynman
in this very famous quote where he said, "Nature isn't classical "and if you want to make
a simulation of nature, "then you better make
it quantum mechanical." And by golly, it's a wonderful problem because it doesn't look so easy. And that's true, it's
actually a very hard problem to build a quantum computer. And the technology is still early, but we're seeing a lot
of improvements, right? So as the take home message, quantum computers can solve some problems with exponentially fewer
gates or fewer operations than classical computers because they use different
types of algorithms. So to put it in a very provocatively, it's not a two X speed up, but a two to the power
of X speed up, right? And because it's exponential, that's the difference between
something that's possible and something that's
not possible to compute. So from that very brief introductions, there are actually some
very profound learnings or lessons we can take, right? Because quantum computers are
not just a classic computer that runs faster, it
means also that quantum will not replace classical
computers, right? If you have a classical algorithm that does not scale exponentially, that works well for the
problem that you have, there's no argument why
you would replace it with a quantum computer because
they're generally slower, they're generally more expensive. The second point is that many use cases of quantum computers are
hidden by definition. And what do I mean with this, right? If you look around at your company and think about what are the applications that a quantum computer could be used for, chances are there are some
applications you don't see because they are not possible to solve with classical computers today, right? Because by definition, we
wanna apply quantum computing to problems that are hard
for classical computers. And the final one is, because we're talking about
a new class of algorithms, these applications are not
just lift and shift, right? When we have a quantum computer
at some point in the future that can address
industry-relevant problems, we cannot just take what we were running on a classical computer before and move it over to a quantum
computer and it will work. These are completely new algorithms, completely new primitives, and it requires a lot of
talent and skills and IP to develop these kind of algorithms. And we're very excited
about these algorithms because applications are applicable to a wide field of verticals, right? So we already talked about
the home turf kind of problems on the left-hand side, like problems where we
try to describe nature for all intents and purposes
in physics and chemistry, simulating molecules and
reactions, et cetera, developing new materials
and material science. But maybe very surprisingly,
it doesn't stop there, right? Quantum computers are not
only exponentially faster for these type of problems,
for some of these problems, but there are also certain problems that are inherently classical,
where it has been shown that quantum computers
do provide an advantage. Well, maybe the most famous
one is in cryptography, right, where the Shor's algorithm showed that you can factor large
numbers exponentially faster than with a classical computer, right? There's this relevance
for RSA and encryption and so on and so forth, but
then there are also problems in the space of optimization, and machine learning is a
little bit more nuanced here, and a lot of research is
being done in those topics. Well, all of this is to say that we at AWS really think quantum computing is a foundational compute technology, and like with other compute technologies, we want to bring these
capabilities to our customers, and in the fullness of time,
make them part of our offering, our compute fabric at AWS, right? So in some sense, our job at AWS is to make
quantum computing boring, right? When you look at the accelerated
compute portfolio at AWS, we have already different
types of accelerators, from GPUs to AI and ML accelerators, ASICs and FPGAs, and so on and so forth, from different providers,
and in the fullness of time, I think quantum is just
another type of accelerator. But of course, it's a long
journey to that place, and to throw a little bit of cold water, I want to really stress that
the technology is early, and today there is no quantum computer that can solve any
industry-relevant problem faster, cheaper, or more accurately than the best classical alternative. So then, what are customers
using quantum computers for today, right? Well, like any other technology, quantum computing will not start with the broad-scale adoption, but it will start from niche applications and gradually grow from there, and I like to make the
analogy with GPUs, right? GPUs started for a very
niche application space of graphics processing, until, researchers in academia realized it can be used for
mathematical calculations, big matrix multiplications, and so on, until they finally got
the broad-scale adoptions through AI and machine learning. And in the same way,
quantum computers today, what most of our customers do, is using quantum computers
to study quantum computing, right? From researching the devices,
the sources of noise, developing error mitigation protocols, to researching these
novel types of algorithms, trying to understand how they converge, how they are impacted by this noise, so trying to close the gap between what the hardware
brings from the bottom and what applications come from the top. But of course, ultimately, we don't wanna just
study the hammer, right? We want to actually use the hammer, right? Using quantum computers as a tool to solve problems in other domains. And the first areas where we will solve different kind of problems will be in the space of
scientific applications, right? To drive new scientific
discovery in high-energy physics, in material science, in
quantum materials, and so on, before we go into this final step into broadly industry-relevant problems with broad-scale adoption. And we are at a very exciting
time of the industry, I think, right? We are just at that cusp of going over from studying the hammer to using, actually, the hammer, right? And against that backdrop, I wanted to introduce you
to what we're doing at AWS to help accelerate that technology to help make that promise of
quantum computing a reality. So in a nutshell, our
quantum technologies at AWS, we have four pillars. This is Amazon Bracket, our
quantum computing service. You're gonna hear about that more. We have the Amazon Advanced Solutions Lab. This is a professional services team that focuses on quantum computing and related classical technologies. And then we have the AWS
Center for Quantum Computing. It's a research facility where we're developing our
own quantum computing hardware and quantum error correction technologies. And finally, we have our
post-quantum cryptography team and quantum networking team that's part of AWS Core Networking. So let's start with a brief overview. So the AWS Center for Quantum Computing, already mentioned, is
an AWS research center that's located at Caltech. We are building our own quantum
computing hardware there with a quantum error
correction first approach. So we really want to address
that next level of scaling that is required to take the technology from studying the hammer
to using the hammer. We're building on a technology
that is dubbed Cat Qubits, which combines superconducting
qubits with resonators, microwave resonators, to
suppress certain types of noise. And I'll talk a little bit more about that on the next slide. As a matter of fact, just
beginning of the year, we showed and published results
from our first prototype that's called Ocelot. There's a picture of the chip here. And we were able to show that
through that architecture, this Cat-Qubit architecture, we are able to suppress
a certain type of noise to a degree where the resources required to implement error correction
on this architecture is 10 times lower than in
the traditional approach. So we're very excited about these results. But of course, our approach
is only one of many, right? There are many other promising directions from building quantum computers with ions that are trapped,
building quantum computers with neutral Rydberg atoms
or photons and many others. And at the same time, we
believe that we need to bring this technology in the
hands of our customers so that they can experiment
with this technology, start developing algorithms, and start developing the IP around how we can bring the new applications and the resource requirements
of them further down. And that was the reason for us why we launched Amazon Bracket
in 2020 at this point, right? We wanted to democratize
quantum computing, bring different types of quantum computers in the hands of our customers so that they can learn, experiment, but also do research into applications and envision how quantum
computers will be used in the context of AWS, in the context of existing HPC pipelines. And today, we provide access to third-party quantum computers and in the future also, of course, our own AWS-built quantum
computers in the fullness of time, all in one consistent experience. The quantum computers that
we have available today is from five different providers. That is two ion trap providers, IonQ and Alpine Quantum Technology, AQT. We have two providers that are building superconducting QPUs with Rigetti and IQM. And finally, we have a provider that is building Rydberg-based
quantum computers from QuEra. So we wanna give customers that choice and the ability to contrast and compare the different approaches. Each of them have different
pros, different cons. It is not clear that this
is a winner-take-all market by any means, right? There is a lot of different
potential applications for each of these technologies because they have all very
different characteristics and different programming paradigms. And we wanna give customers that visibility into the technology. So then, let's take a
look at a 20,000-foot view to Amazon Bracket. And we think about Bracket in kind of three different layers, right? Like at the bottom, you
have the infrastructure and the access modes, right? So we are providing access to QPUs, to quantum circuit simulators, as well as to the classical compute that is used with quantum
computers in tandem. We're gonna hear about
that more from Michael. And we can access these quantum computers in different access mode. For example, on-demand, just pay-as-you-go as you used from AWS. You can also make reservations where you get dedicated
time on a particular device where only you can access it
at the time that suits you. In the middle part of the stack, we're providing the interfaces
and capabilities, right? From Jupyter IDEs to
programming tools and compilers and a feature for executing
quantum hybrid algorithms with hybrid jobs. And then finally, at the top of the layer, we want to bring different type
of tooling to our customers that they are used to
and want to use, right? We are supporting all of the major quantum computing frameworks
from IBM's Qiskit to Penny Lane and NVIDIA's CUDA Quantum, CUDA Q, as well as a whole list
of software tooling and programming frameworks
from our partners. Many of them are here at re:Invent today and giving their presentations. I encourage everybody to check that out. But essentially, we're realizing we can't build it all on our own. And we want to make sure
that anything runs on bracket and we bring the tooling to our customers that they want to use. And throughout that stack, we are trying constantly
to improve the performance, make the user experience better, get more throughput performance
and quality performance out of these early stage devices. And there's a lot we could talk about with the different capabilities. I picked out a feature that
we just recently launched. This is Amazon Bracket Program Sets. So the idea here is that the way you interact
with a quantum computer is not that you send a single program and you get it back and you analyze it. In reality, a very common workload pattern is that you send multiple
of these programs that either are related to each
other, they can be the same, they can be somehow connected or also completely independent. And for each and every
program that you send, you need to compile it, you
need to have the I/O overhead of bringing it down to the
control system of the QPU, load it onto the FPGA
and so on and so forth. So there is overhead
in each of those steps. And with Program Sets,
we're allowing customers, we're enabling customers to submit multiple quantum programs, a whole series of quantum programs in a single payload
with a single API call, which allows us to optimize that payload, compile it and gain efficiencies
through compilations and I/O process, bringing
multiple programs at the same time onto the FPGA. And for certain types of workloads, we're seeing up to 24x
speedups with this feature. So with that, I wanna come back to this kind of inverted
pyramid of use cases. And as we discussed before, we think that the first use cases will be in the scientific domain before we go into broad industry adoption. And I don't wanna downplay
this as a mere stepping stone because I think it's a very
profound fact, actually, that quantum computers will change the way that we understand nature, that we can understand how nature behaves at the microscopic level. And in fact, a recent study from NERSC, this is a supercomputing facility from the Department of Energy, found that at least 50% of
their production workload has the potential to be
exponentially accelerated by quantum computers. So there's a tremendous opportunity to accelerate research and scientific work through quantum computing directly. And many countries and
governments around the world are realizing this opportunity. So this was one study from NERSC. Other studies, for example, from LANL find numbers between 30 and 50%. But countries around the world realizing that this is an opportunity to accelerate scientific breakthroughs and have founded national
quantum initiatives to find those first use cases and then also use it as a stepping stone for further industry adoptions. And a number of those
government initiatives, national initiatives, they're building with
Amazon Bracket, right? Because the first thing
that they want to have is to give access to quantum computers to their local research communities. With Amazon Bracket, they
get access to HPC resources and quantum computers on demand. We build scalable and
secure research environments as well as a tailored
administrative and budget controls to run large-scale research
organizations in the cloud. For example, we're working
with the NQCH in Singapore, with the NQCC in the
UK, QCloud in Ireland, and POSI in Australia. As a matter of fact, we just launched, POSI just launched the quantum hub portal which provides researchers
access to quantum computing and classical computing
resources through AWS with tailored administrative controls. And they're now starting
to run the Zettonics QPilot where they will allocate
quantum computing resources for local researchers to drive
that innovation flywheel. And we're super excited
about initiatives like this because we think there's a
lot of research to be done and by having access to
real quantum computers, that research can accelerate. So, but of course, we are all very excited about bringing that technology
also out of academia into broad industry adoption and Michael is gonna tell
us more about that idea and how we're going to drive
our customer engagement in this field. Take it away, Michael.
- Thank you. Well, thanks very much, Eric. Wonderful introduction
to Bracket as a service. (audience applauds) So Eric and I work very closely together. He builds and operates
the Bracket service. He makes it available to our customers so that he can use it
through the AWS console. It's a service that's available
in the cloud for you today. You can access quantum computers just in the way that you would
any other service on AWS. So if you enjoy using EC2,
you're gonna love using Bracket 'cause it's just another service but we've got quantum computers on there. My job is to talk to
our enterprise customers about where quantum computing is headed and how they will be able to
make use of this in the future, the kind of workloads that
they'll be interested in, the thinking that they
need to go through now to prepare their strategies for quantum computing in the future. Most of our customers today
on Bracket are researchers, as Eric mentioned. They're national labs, they're hubs, they are individual
researchers at universities. Most of them are doing science. So they come to AWS to
use the infrastructure that we've got available
to do good science. So they're collecting data,
they're doing physics research, they're doing computer science research, they're doing application and
benchmarking style research. But as we build up this stack, we move from the science
to looking more at solving industrial scientific use cases. So we'll give an example in a
moment about drug discovery, but also think about materials design, think about production opportunities. But at the big scale and
where we wanna get to is how do we use quantum computers for large-scale enterprise problems in exactly the same way that we use high-performance compute
classically today at AWS. So some companies are
really starting to invest in this ahead of the curve. There are a few leaders out there that are really investing
in quantum computing in understanding those use cases and where the potential might be. One of those companies is JPMorgan Chase. We actually have another
breakout session tomorrow, which I encourage you to
come to, with JPMorgan Chase, where we will go through
exactly how we operate the end-to-end application
study and benchmarking work that we've been doing with
them for the past year. But their motivation is really clear. Marco Pistoia, who until very recently led the quantum computing
program at JPMorgan. He's since gone on to a
wonderful new opportunity at a quantum computing hardware company. But he said, "If a company
doesn't do anything "about the market right now, "when quantum advantage becomes
real, it might be too late." And this is really important. This is a fast-moving technology. This is not just a lift and shift from an existing HPC workload
to a quantum compute workload. These are complex algorithms. They're complex problems. They take some thinking to work through to design new approaches to running quantum classical hybrid work, to running workflows together. And so the leading organizations in enterprise adoption of quantum compute are really thinking about this now in anticipation of that
future potential advantage. So here's the journey that we
go through with them on it. We look at, through a discovery
process around use cases, helping them identify
the kinds of workloads that are well-suited
to a quantum computer. We then research and benchmark with them the quantum computing algorithms. So we compare quantum on quantum. How does one quantum
computing hardware system compare to another quantum
computing hardware system? We also compare quantum
and classical together. So how does the best
available classical approach to that problem match with the quantum computing
approach to that? And then look at the hybrid opportunities. What if we combine
different things together and orchestrate across
multiple different platforms on AWS to explore this space? And that's what pushing the
boundaries is all about. How do we unlock the potential
of end-to-end compute, so using a quantum computer to make classical computers go faster? And then that will lay
the groundwork for us for production applications in the future. So bringing all this together, we want our customers to be prepared so that as soon as Amazon
Bracket gets bigger and we've got more capacity and we're scaling up
across multiple regions, you are ready with your workloads to jump straight into that. So last year at reInvent, we launched a program
called Quantum Embark. Quantum Embark is our sort of entry point for any enterprise customers to just get started
with quantum computing. So if you're not quite sure what to do, you know you should do something, but you're not sure what
that something should be, this is the program for you. So it is a 12-week,
fixed-price, fixed-scope program to just get started in quantum computing and work with our teams to
work through that process that I just described on the last slide. So the use case discovery, do some training and enablement together, and then deep dive on
one particular problem. So let's pick one problem
from your organization and solve it together. Go through the process to write out the quantum
computing algorithms, compare it to the classical algorithms, fit it onto a quantum computer on Bracket, benchmark it quantum to
classical and quantum to quantum. That process takes about 12 weeks. We work as a joint team together, so some of our solution architects and applied science specialists
around quantum computing, some of your team as well,
and we bring that together. The whole idea is that
we're able to give you and your executive teams
actionable outcomes without the hype. There's a lot of hype and excitement, and for good reason,
around quantum computing, but how do we make it real for
your particular organization and so the Quantum Embark
program is all about that, giving you some actionable outcomes so that you can understand
if and when quantum computing is gonna have an impact on your business, and then you can start to inform the rest of the stakeholders
across your company about where that's headed. A little bit deeper, we've got a team called the Advanced Solutions Lab. This is our professional services team that engages directly with customers to do long-term R&D engagements
around quantum computing. Our colleague Martin Schutz
from the Advanced Solutions Lab will be on stage tomorrow
at the breakout session I was mentioning with JP Morgan Chase to talk about exactly this. They had a three-year program of effort looking at multiple problems
across quantum computing at every level, so from optimization of how to use particular devices to compilation strategies
to application benchmarking. This is a deep research team. This team will design
a custom R&D engagement for your particular needs. They'll work with you to develop and explore novel quantum
computing algorithms. We'll look at opportunities to
deliver business value today on classical compute hardware, but most importantly, generate
that intellectual property so that you've got the know-how and the IP so that you can take
advantage of quantum computing as it matures over time. Practically now, let's take a look at what does quantum computing mean for our entire accelerated
compute portfolio. So if you are a user of AWS's high-performance compute services, where does quantum computing fit into that overall landscape? And the good news is that in some ways, bracket and quantum computing is just another instance
of compute on AWS. It's just another type
of accelerated computing. So we have CPUs, GPUs,
other accelerated processes like Trainium and Inferentia. Well, quantum computing is
just one more type of computer in that overall portfolio. And so we've been doing
a lot of work this year to integrate bracket as
another sort of instance type within the high-performance
compute services of AWS. So you might be familiar with
the Parallel Compute Service, with AWS Batch, with Parallel Cluster. This is for classical HPC. So if you're the Formula
One, if you're Ferrari, and you need to do
computational fluid dynamics, those are the services that you're using to do those large industrial-scale heavy compute workloads on AWS. They don't go directly to
EC2 to spin up instances. They use these orchestration tools to do those large-scale problems. And so we're looking at
how do we integrate bracket directly into that? You should be able to go straight to the high-performance compute services and spin up accelerated compute instances of multiple different types
that include quantum computing and orchestrate across that entire end-to-end workflow over time. So we've been doing a lot of work to integrate that into the systems, and the example that I'm
gonna show you in a second is based on exactly that framework. So think about AWS as
the core infrastructure. We've got compute and
networking and storage. Bracket is just another
form of compute on there. Different abilities to consume
that compute over time. So on our classical infrastructure, we've got on-demand,
we've got capacity blocks, we do spot, reserve instances. We're building out exactly the same for bracket over time as well. So right now, you can
log into the console, you can access bracket on-demand, you only pay for what you use, no upfront commitment to
use a quantum computer, or you can reserve a
capacity block next Tuesday at 3 p.m. to do your
particular workload as well. So we really are thinking
about quantum computing as just another computer
within the framework that you're already used to running large-scale workloads on AWS. So let's take a look at what a large-scale end-to-end industrial
strength workflow looks like. So this is a very typical kind of workflow for one of our high-performance
compute customers. They might be doing drug discovery, computational fluid dynamics, some kind of engineering analysis, circuit layout, something like that. And there'll be some user
action process right at the top that will flow down to an execution plan, there'll be some I/O on there, there'll be an orchestration layer handling different types of compute, but all of this numerical
heavy lifting that's going on. That could be a couple of hours of work, couple of weeks of work, couple of months of work that's going on. We see everything in between. And the idea of quantum computing is, well, what if we could interleave some parts of that overall workflow that are well-suited to a quantum computer so we're still doing quantum
and classical together, but in a hybrid modality? Can we get an end-to-end speedup? Can we reduce the entire
operational end-to-end workflow of a large-scale
high-performance compute workload and get a faster result for our customers and hopefully a lower cost
result for our customers as well? So we're at the very early stages of putting this into practice. And we've got a great example
with our customer AstraZeneca that we worked with earlier this year to explore exactly this kind of problem. And so this was a joint
program that we did together between AstraZeneca, IonQ, the quantum computing hardware
company that's on bracket, NVIDIA, and AWS. So it was the four
companies working together, looking at the algorithm problems, the orchestration problems, how we bring that back together
as an end-to-end workflow and to see what kind of
result we could get there. And so the particular problem
that we were looking at was this chemistry problem called transition metal catalysis. And it underpins so much of what happens in modern drug design. This is part of the everyday workflow that every drug company
in the world goes through. And it's a really tough
computational problem to solve. It is very difficult
for a classical computer to simulate this because as the complexity of these molecules grows, the amount of connections between them also increases exponentially and it becomes harder and
harder to simulate that. But if we could simulate
these accurately and early, then we could identify
new synthesis routes before going to the wet lab, before doing that work,
mixing chemicals together to see what would actually happen. And so the particular chemistry problem that we looked at here
was something called the oxidative addition and
Suzuki-Miyaura coupling, the nickel catalyst, really
rolls off the tongue. But the idea here is that we're looking at a catalytic process. So we're going from that
B state up to the BC state and then down to the C. And so that's an energy barrier
that we need to get over. So we're modeling out what
happens in the real world in real chemistry, quantum
mechanical process, going over this energy barrier
through a catalytic state. And that determines whether
the height of that barrier determines whether this
reaction is going to run at all. So if it's too high, if
it's too much of a barrier, when we go into the wet lab, that's not going to come together as the molecule that we want. So we wanna understand
before we go to the lab, the height of that barrier and what the end state is going to be. Solving that problem is
really, really tough. This is the classical workflow for it. So we start with
calculating an active space and then there's something
called the trial wave function, which is one of the hardest
parts of this overall state. This is where the quantum bonds are being understood by the computers. And then we hand it off
to classical systems to run some Monte Carlo analysis and find the overall energy
state at the end of that. But it turns out that we can replace one part of this workflow with a quantum computing
algorithm instead. And so working together,
AstraZeneca, NVIDIA, IonQ and AWS, we said, what if we went
classical, quantum, classical? We put a whole bunch of, we
adapt the classical algorithm to better suit a quantum computer and then we also adapt
the classical workload that happens afterwards. Can we get a better result
from that over time? So we took a look at adapting that trial wave state function preparation on the IonQ Forte-1 machine. At the time that we ran this, this was the latest device
that we had on bracket. And we ran what we think
was the largest scale quantum compute workload
that's ever been run on these systems. And so it was fitting those
molecules that we saw before through that energy state transition onto the quantum computer and doing a whole bunch
of sampling around that. We then moved those results over to classical post-processing
using AWS Parallel Cluster, one of our high-performance
compute services. And we ran the Monte Carlo simulations to find the final energy state there. We used a lot of compute to do this. We used 40 P5 EN instances. Those are the H100 instances from NVIDIA for a couple of days
running compute on here. So it was a big workload. The end-to-end state here, we think, is the largest
end-to-end workload that's ever been run quantum
and classical together. And the results are
really, really promising. What this chart is showing, on the x-axis is the system size, essentially the size of the molecules, the size of the atoms
that we're looking at. So bigger and bigger molecules as we go out to the right-hand side. And on the y-axis is the runtime
in seconds on a log scale. So more processing time to get there. The dashed lines that you see were the previous best
available classical results that we had from this. So as these molecules got bigger, the previous best classical systems were in those dashed lines there. The solid line is what we're
able to produce classically on this hybrid workflow. So the particular solid dot
that's in the middle there is this particular result,
so right in the middle. So that gap between the
solid dot on the solid line and the lowest level of the dashed line, that is the performance increase that we're able to get
between these two workloads. And that is a 656 times speedup over that part of the processing cycle that we went through there. So a really significant result. Now, this isn't something that
we could put in production. When we had to play a lot
of tricks on our system to make this work, we had to learn a lot about the orchestration of
running a hybrid workload on AWS. And it took a lot of compute to do this. So we can't run this in
production every day. Also, we weren't looking
at the cost around it. But it gives us a lot of confidence that as we're building out these systems, as we get bigger and bigger, as we're able to do more and more sophisticated orchestration
across high-performance compute, that as these molecules get bigger, we're going to see a
huge performance increase that we're gonna be able to
deliver to customers there. So as we extrapolate out
to molecules like FeMoCo that are really important to problems in industrial processing
and nitrogen fixation, and hopefully, eventually, things like fertilizer production, that we're going to be
able to model these systems in a really interesting way. So I just wanna remind
everyone of something that Eric said right at the
top of the presentation, that no quantum computer today can solve an industry-relevant problem faster, cheaper, or more accurately than the best available
classical alternative. That is still true. The example that I showed you before does not yet meet these criteria. But it's a stepping stone to that. We can really see and
have a lot of confidence around where this is headed. As these computers get bigger,
as they get more capable, we are gonna be able to
tick off these things, to be able to go faster,
to be able to go cheaper, to be able to do things more accurately than the best available
classical alternative, and be able to do it in
production over time as well. So what can you do today? How do you take action around this? Well, this is what the
leading companies are doing. They're generating IP. They're generating the algorithms that will run on these quantum computers. They're generating the know-how about how to operate it in the cloud. And so you can do that too. You can get engaged with us
or with our partner network and explore what the
intellectual property portfolio looks like that will have an impact on your compute solutions. You can engage the supply chain. You're understanding the quantum computing hardware companies, understanding the software libraries, the open source community, the
partners that are out there, the university researchers
that are engaged in this. You're having a deep understanding of where your compute is gonna come from, where your algorithms are gonna come from, where your software
library is gonna come from. It's an important part of the puzzle. And then finally, build a workforce. Have a few people within your organization who can understand this technology, who can make sense of it for
your particular organization, who can start to read the news and be able to process it in
a way that's relevant to you and be able to react quickly as computers get more and
more capable over time. And so we're here to help you do that. We've got a lot of options available for you to engage with us
at AWS on quantum compute. In the middle is Bracket. This is an operational service in general availability on AWS today. We've been running this for five years. You can access quantum computers in the cloud this afternoon if you'd like. We actually have a series
of workshops this week so you can get hands-on
with quantum computing in one of our workshops through
the rest of these sessions. Couple of other options. We've got a digital badge
available on AWS Skill Builder. You can work through a course, get a digital badge through that. Quantum Embark we talked about before for enterprise customers to
engage in quantum computing. The Advanced Solutions Lab if
you wanna do a deeper project. And then Amazon Bracket
Direct is our program so that you can work directly with our hardware supplies as well. So if you wanna engage
on a particular problem with IonQ or Regetti
or AQT or QuEra or IQM, you can do it through that program. So a lot of different ways to engage. And then finally, just to wrap up, we've got a lot of sessions
on quantum compute this week. This is just a selection. All of the sessions that
we've got on quantum computer through the QR code there. But I've just put a
selection on the slide here so that if you wanna follow up on this and go a little bit deeper, please come to the
breakout session tomorrow with JPMorgan Chase and
look at the applications in the financial sector. We've got some chalk talks
that go into hybrid compute, into how we're using generative AI to accelerate quantum
computing software development. And then finally, a little bit more hubs, which is what Eric was
talking about before with those national
compute resource centers and how we're integrating in with them. So we're delighted that
you can make it along today to this session to learn a little bit more about what we're doing in
quantum technologies at AWS. And we hope to see you
on Bracket in the future. Thank you very much.
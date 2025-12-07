---
video_id: u3HBJVjpXuw
video_url: https://www.youtube.com/watch?v=u3HBJVjpXuw
title: Some thoughts on the Sutton interview
author: Dwarkesh Patel
published_date: 2025-10-04
length_minutes: 11.65
views: 95190
description: "I have a much better understanding of Sutton’s perspective now. I wanted to reflect on it a bit.  Read the transcript here: https://www.dwarkesh.com/p/thoughts-on-sutton  TIMESTAMPS 00:00:00 The steelman 00:02:42 TLDR of my current thoughts 00:03:22 Imitation learning is continuous with and complementary to RL 00:08:26 Continual learning 00:10:31 Concluding thoughts"
is_generated: False
is_translatable: True
---

Boy do you guys have a lot of 
thoughts about the Sutton interview.  I’ve been thinking about it myself and I 
think I have a much better understanding   now of Sutton’s perspective than I did during 
the interview itself. So I wanted to reflect on   how I understand his worldview now.
Richard, apologies if there's still   any errors or misunderstandings. It’s been 
very productive to learn from your thoughts.  Here's my understanding of the steelman of 
Richard's position. Obviously he wrote this   famous essay, The Bitter Lesson. What is 
this essay about? It's not saying that you   just want to throw away as much compute as you 
possibly can. The bitter lesson says that you   want to come up with techniques which most 
effectively and scalably leverage compute.  Most of the compute that's spent on an LLM is 
used in running it during deployment. And yet   it’s not learning anything during this entire 
period. It’s only learning during this special   phase we call training. That is obviously not an 
effective use of compute. What's even worse, this   training period by itself is highly inefficient, 
these models are usually trained on the equivalent   of 10s of 1000s of years of human experience.
What’s more, during this training phase,   all of their learning is coming straight from 
human data. This is an obvious point in the   case of pretraining data. But it’s even kind of 
true for the RLVR that we do with these LLMs:   these RL environments are human 
furnished playgrounds to teach LLMs   the specific skills we have prescribed for them.
The agent is in no substantial way learning from   organic and self-directed engagement with the 
world. Having to learn only from human data,   which is an inelastic and hard-to-scale 
resource, is not a scalable way to use compute.  Furthermore, what these LLMs learn from training 
is not a true world model, which would tell you   how the environment changes in response to 
different actions that you take. Rather, they   are building a model of what a human would say 
next. And this leads them to rely on human-derived   concepts. A way to think about this would be, 
suppose you trained an LLM on all the data up   to the year 1900. That LLM probably wouldn't be 
able to come up with relativity from scratch.  And here's a more fundamental reason to think this 
whole paradigm will eventually be superseded. LLMs   aren’t capable of learning on-the-job, so 
we’ll need some new architecture to enable   this kind of continual learning. And once we do 
have this architecture, we won’t need a special   training phase — the agent will just be able to 
learn on-the-fly, like all humans, and in fact,   like all animals are able to do. And this new 
paradigm will render our current approach with   LLMs —and their special training phase that's 
super sample inefficient— totally obsolete.  That's my understanding of Richard's position. 
My main difference with Rich is just that I don't   think the concepts he's using to distinguish 
LLMs from true intelligence are actually   that mutually exclusive or dichotomous.
For example, I think imitation learning   is continuous with and complementary to RL. 
Relatedly, models of humans can give you a prior   which facilitates learning "true" world models.
I also wouldn’t be surprised if some future   version of test-time fine-tuning 
could replicate continual learning,   given that we've already managed to accomplish 
this somewhat with in-context learning.  Let's start with my claim that imitation 
learning is continuous with and complementary   to RL. I tried to ask Richard a couple of times 
whether pretrained LLMs can serve as a good   prior on which we can accumulate the experiential 
learning (aka do the RL) which will lead to AGI.  Ilya Sutskever gave a talk a couple of months 
ago that I thought was super interesting,   and he compared pretraining data to fossil 
fuels. I think this analogy has remarkable reach.   Just because fossil fuels are not a renewable 
resource does not mean that our civilization   ended up on a dead-end track by using them. 
In fact they were absolutely crucial. You   simply couldn't have transitioned from the water 
wheels of 1800 to solar panels and fusion power   plants. We had to use this cheap, convenient and 
plentiful intermediary to get to the next step.  AlphaGo (which was conditioned on human 
games) and AlphaZero (which was bootstrapped   from scratch) were both superhuman Go 
players. Of course AlphaZero was better.  So you can ask the question, will we, or 
will the first AGIs, eventually come up   with a general learning technique that requires 
no initialization of knowledge and that just   bootstraps itself from the very start? And will 
it outperform the very best AIs that have been   trained to that date? I think the answer 
to both these questions is probably yes.  But does this mean that imitation learning must 
not play any role whatsoever in developing the   first AGI, or even the first ASI? 
No. AlphaGo was still superhuman,   despite being initially shepherded by human player 
data. The human data isn’t necessarily actively   detrimental. It's just that at enough scale 
it just isn’t significantly helpful. AlphaZero   also used much more compute than AlphaGo.
The accumulation of knowledge over tens of   thousands of years has clearly been essential to 
humanity’s success. In any field of knowledge,   thousands (and probably millions) of 
previous people were involved in building   up our understanding and passing it on to the 
next generation. We obviously didn't invent   the language we speak, nor the legal system we 
use. Also, most of the technologies in our phone   were not directly invented by the people who are 
alive today. This process is more analogous to   imitation learning than it is to RL from scratch.
Now, of course, are we literally predicting the   next token, like an LLM would, in order to do 
this cultural learning? No, of course not. Even   the imitation learning that humans are doing 
is not like the supervised learning that we do   for pretraining LLMs. But neither are we running 
around trying to collect some well defined scalar   reward. No ML learning regime perfectly describes 
human learning. We're doing things that are both   analogous to RL and to supervised learning. 
What planes are to birds, supervised learning   might end up being to human cultural learning.
I also don't think these learning techniques are   categorically different. Imitation learning is 
just short horizon RL. The episode is a token   long. The LLM is making a conjecture about 
the next token based on its understanding   of the world and how the different pieces of 
information in the sequence relate to each   other. And it receives reward in proportion 
to how well it predicted the next token.  Now, I already hear people saying: “No 
no, that’s not ground truth! It’s just   learning what a human was likely to say.”
And I agree. But there’s a different   question which I think is more relevant to 
understanding the scalability of these models:   can we leverage this imitation learning to 
help models learn better from ground truth?  And I think the answer is, obviously yes? After 
RLing the pre-trained base models we've gotten   them to win Gold in IMO competitions and to 
code up entire working applications from scratch.   These are “ground truth” examinations. Can you 
solve this unseen math olympiad question? Can   you build this application to match a specific 
feature request? But you couldn’t have RLed a   model to accomplish these tasks from scratch. 
Or at least we don't know how to do that yet.   You needed a reasonable prior over human 
data in order to kick start this RL process.  Whether you want to call this prior a proper 
"world model", or just a model of humans,   I don't think is that important and honestly 
seems like a semantic debate. Because what you   really care about is whether this model 
of humans helps you start learning from   ground truth – AKA become a “true” world model.
It’s a bit like saying to someone pasteurizing   milk, “Hey stop boiling that milk because 
we eventually want to serve it cold!”   Of course. But this is an intermediate 
step to facilitate the final output.  By the way, LLMs are clearly developing a deep 
representation of the world, because their   training process is incentivizing them to develop 
one. I use LLMs to teach me about everything from   biology to AI to history, and they are able to 
do so with remarkable flexibility and coherence.  Now, are LLMs specifically trained 
to model how their actions will   affect the world? No, they're not.
But if we're not allowed to call their   representations a “world model,” then we're 
defining the term “world model” by the process   we think is necessary to build one, rather than 
by the obvious capabilities the concept implies.  Continual learning. Sorry to bring up my 
hobby horse again. I'm like a comedian   who's only come up with one good bit, 
but I'm gonna milk it for all it's worth.  An LLM being RLed on outcome-based rewards learns 
on the order of 1 bit per episode, and an episode   may be tens of thousands of tokens long.
Obviously, animals and humans are clearly   extracting more information from interacting with 
our environment than just the reward signal at the   end of each episode. Conceptually, how should 
we think about what is happening with animals?  I think we’re learning to model the world through 
observations. This outer loop RL is incentivizing   some other learning system to pick up maximum 
signal from the environment. In Richard’s OaK   architecture, he calls this the transition model.
If we were trying to pigeonhole this feature spec   into modern LLMs, what you’d do is to fine tune on 
all your observed tokens. From what I hear from my   researcher friends, in practice the most naive 
way of doing this actually doesn't work well.  Being able to continuously learn from 
the environment in a high throughput   way is obviously necessary for true AGI. And it 
clearly doesn’t exist with LLMs trained on RLVR.  But there might be some relatively straightforward 
ways to shoehorn continual learning atop LLMs. For   example, one could imagine making SFT a tool 
call for the model. So the outer loop RL is   incentivizing the model to teach itself 
effectively using supervised learning,   in order to solve problems that 
don't fit in the context window.  I'm genuinely agnostic about how well 
techniques like this will work—I'm not   an AI researcher. But I wouldn't be surprised 
if they basically replicate continual learning.   Models are already demonstrating something 
resembling human continual learning within   their context windows. The fact that in-context 
learning emerged spontaneously from the training   incentive to process long sequences makes me 
think that if information could flow across   windows longer than the current context 
limit, models could meta-learn the same   flexibility that they already show in-context.
Some concluding thoughts. Evolution does   meta-RL to make an RL agent. That agent can 
selectively do imitation learning. With LLMs,   we’re going the opposite way. We first made a 
base model that does pure imitation learning. And   we're hoping that we do enough RL on it to make 
a coherent agent with goals and self-awareness.  Maybe this won't work!
But I don't think these super first-principle   arguments (for example, about how these LLM 
don't have a true world model) are actually   proving much. I also don't think they’re strictly 
accurate for the models we have today, which   are undergoing a lot of RL on “ground truth”.
Even if Sutton's Platonic ideal doesn’t end up   being the path to first AGI, his first principles 
critique is identifying some genuine basic gaps   these models have. We don’t even notice because 
they are so pervasive in the current paradigm,   but because he has this decades-long perspective 
they're obvious to him. It's the lack of continual   learning, it's the abysmal sample efficiency 
of these models, it's their dependence on   exhaustible human data. If the LLMs do get to 
AGI first, which is what I expect to happen,   the successor systems that they build will 
almost certainly be based on Richard's vision.
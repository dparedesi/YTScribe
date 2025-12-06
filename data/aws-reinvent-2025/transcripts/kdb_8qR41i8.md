---
video_id: kdb_8qR41i8
video_url: https://www.youtube.com/watch?v=kdb_8qR41i8
is_generated: False
is_translatable: True
---

- I'm Jovana, Senior Technical
Evangelist at Atlassian. I specialize in platform engineering and cloud infrastructure and also in Rovo Dev and everything to do with improving software
development lifecycle. Let's get into it. Now, before we do dive in, let's quickly set the stage. So, why are developer productivity
and quality so critical? My favorite explanation to that is that if you invest in your developers, they will have better support, creating better product. If you have a better product, your company brings revenue. It's as simple as that. And at Atlassian, we now run Developer Experience report, and each year we learn something new. From our 2025 DevEx report, we've learned that 99%, so almost every developer, has reported time savings using AI, but still is losing time across
auto development lifecycle. They're only spending
16% of their time coding, which we all know that's not
the friction for developers. The other 84% is where
AI tools and assistants have the real market opportunity to change that and improve it because really, developers
are losing valuable time on non-coding tasks, and that's exactly what I
wanna talk to you about today. Software development is
at its core a team effort, and our vision at Atlassian is for every software development team to have a teammate that deeply understands their organizational context as it's captured in the
Atlassian Ecosystem, from Jira issues through Confluence pages, all the way through the codebases, wherever those codebases live. That teammate should be aware
of your engineering history, including past incidents
and their resolutions. Now, that intelligent teammate can put all that
knowledge to work for you, assisting you wherever you are working, whether that's a terminal, the ID, the CI/CD pipelines, or maybe even Jira. And that teammate can be Rovo Dev, and I would like to introduce you to it. Rovo Dev is Atlassian's
AI-powered agent for developers. It is designed to accelerate
software development lifecycle all the way through code planning, code generation, code reviews, and automation of repetitive tasks and all that at scale. It understands both natural
language but also code, which means you can interact with it wherever you're working. It is powered by
Atlassian's Teamwork Graph, which means it's got context of all of your data within
the Atlassian Ecosystem. Now, of all the places that
you can interact with Rovo Dev, my favorite one is the CLI because it's meeting me
where I like to work. It leverages Teamwork Graph, so I can ensure that it has all the
right suggestions for me, it's got all my real context, and it knows my business. But let's take a look at it in action. Now, here is a website that I created one time, and we have these speakers
that are all wrong. Yep, that is me, Jovana, Senior Technical Evangelist, but that was not my face. What I can do is I'm gonna ask
Rovo Dev to fix this for me. Right now, I've just
authenticated Rovo Dev, I've gone to my Jira issue and I've literally just
copied that issue link and pasted it into Rovo Dev. Rovo Dev is pulling all that information, the description, any other links that I might
have added to this issue just so it can give me
the best response it can. Now, it might be leveraging
memory file as well, depending on what I had added in that description of the ticket. If I go back and refresh, it's updated, and now all of us kind of look the way we should be looking like. That is Shane, that is Willer, and that was me. Now, one of the cool things
is I can just copy an image, paste it into Rovo Dev and let Rovo Dev read the image as is, detecting what is it that was on the image so that it can make those changes. It is that intelligent
that it will recognize that there are certain
things on that image that are not supposed to be there, and it goes on and fixes it. I'm quickly swapping between the two just so you see that it's actually updated exactly what I highlighted
that I need changing on. Next, we've introduced
an AI-based code reviewer that is also part of Rovo Dev. On repositories where Rovo Dev is enabled, Code Reviewer will automatically run after your pull request is created. Code Reviewer spends a few minutes analyzing the code changes and then it comments directly
onto your pull request with all the possible recommendations, fixes and improvements
that should be made. It makes comments, including feedback and things like bugs and maintainability, readability, security,
and so on and so forth. And there are ways to
improve your code reviewer and tailor it to your
specific organizational needs. Firstly, acceptance criteria. It is designed to bridge the gap between your requirements and your code. Acceptance criteria checks automatically and compares the code in your pull request to the requirements you
had in your Jira issue. It's checking if you built
exactly what you said you would. Now, you can catch mistakes
early with this feature, and we've actually been
told by software teams that it has actually
saved them a lot of time. Secondly, we have custom instructions that you can set up for your repos. Now, you can teach Code Reviewer exactly what matters to your organization, to your team, to your codebase. Now, every team has unique ways of working and different standards
that they want to enforce, and sometimes generic
code just doesn't cut it. So, if you teach Code
Reviewer certain standards, design principles, and you feed that to Rovo Dev, every time your pull request is created, what will happen is Rovo Dev will detect based on these standards that you are violating those principles. It is described in your
standard natural language, so just write in English, plain English. And as long as you commit
that into your repo, you should be good to go. Now, we've also launched Rovo Dev in Jira. It is very soon coming to open beta. Temporarily it's in beta, closed beta, but it is a self-contained
AI-driven workflow that helps you tackle work
items with efficiency. And let's have a look at a demo. Let's have a look at Rovo Dev in Jira. What this means is you'll
be able to trigger Rovo Dev directly from your Jira issue, and even do that at once for number of your Jira
tickets from the backlog. What it does, it opens
up an interactive sandbox that looks and feels like VS Code directly within your Jira issue. Now, everything happens autonomously, which means Rovo Dev
will work on your issue, it will create a pull request, and it will let you know when there is something for you to review. It will also update the
status of that Jira ticket if obviously you're the owner. Now, the benefits of this
is at any point in time, you can also go back and look at all the sessions
that you've triggered with Rovo Dev within Jira. Only you have access to this sandbox because it feeds off of your credentials, so security is in place. Now, what actually happens, this opens up a chat with Rovo Dev. If you're not happy with what you see, the changes that it made, you can go back and give it some feedback. And I do encourage you to
give it back some feedback if you're not happy with what it's done. Ask it to make more changes. Why not? Once you are ready with
everything that it's produced, you can go and create a pull request, and this is the stuff
that I told you about, having access to all of
your sessions at all times. We've also brought Rovo
Dev extension into VS Code. So, it's... Actually, let's get to
the video immediately and then I can walk you
through what it actually does. Internet is better this time, let's go. So connecting your Atlassian cloud side will instantly pull all your Jira tickets that you are assigned to, whether it's in to-do,
progress or in review. Now, you can start
working on a Jira issue. Ah, internet is not on my side today. So you can start working
on your Jira issue directly from the VS Code. What it does is it will open up Rovo Chat and you can just tell it what kind of stuff you want it to do, attaching the Jira issue to it. It will also send you notifications if anyone has made changes
to the Jira tickets that you are following or working on. So, if you are working from
the VS Code with Rovo Dev, you will be getting
notifications at all times. So very similar to Rovo Dev in Jira, very similar to Rovo Dev in CLI, you can talk to Rovo Dev from VS Code. We are working on adding that
to JetBrains, stay tuned. Now, productivity for software teams is increased through automation
in Rovo Dev's Code Reviewer. Automation rules may be created to review pull requests or generate code. Is anyone else experiencing
poor internet today? A lot of us are. Okay, great. I'm not alone, I'm not... Okay, I'm not alone in
everyone experiencing. Okay, we're just gonna
have to roll with it, guys. So, with Rovo Dev in automations, you can enforce organizational
code quality standards across teams and repos. So imagine all those code
standards that you wanna enforce, now you can apply to more
than just one codebase, you can apply to all of your workspaces. You can also delegate
repetitive tasks at scale, letting your team focus on important work. Now, once you set up your coding, security, privacy, or design standards, you can use Rovo Dev
to automatically review every pull request
against those standards. You can also enter custom instructions for Rovo Dev to use when
reviewing your pull request, like I've done just here. And similarly, you can
define common coding patterns and use Rovo Dev to
automatically generate code for repetitive tasks. So, it lives in Jira in multiple ways. You can automate pretty much anything. Now, I'm literally demoing the stuff that I've asked it to do and identify all the sort of logging non-compliance standards
that we don't allow, and it's actually done and
told me about the violation. We've also launched the
Rovo Dev in pipelines in Bitbucket Cloud as part of Rovo Dev. It diagnoses and resolves CI/CD pipelines, all the failures and analyzes those failed
builds through steps and provides root causes, suggesting actionable fixes. Actually, the more you
use Rovo Dev in pipelines, the better it gets because it will learn about
your failed builds each time. So instead of manually
digging through your logs, the troubleshooter surfaces
that context for you directly in Bitbucket Cloud. Now, how does Rovo Dev actually stand out from all
the other AI coding assistants? Apart from not only being
an AI coding assistant, but it does help with all the other 84% of software development lifecycle tasks that I know no one really wants to do. Well, Rovo Dev uniquely connects to Jira, Confluence, Bitbucket, but also GitHub, providing context aware insights across your entire tool chain, leveraging the Teamwork Graph that connects your
Atlassian Ecosystem data. Secondly, it is an AI-powered automation across the software development lifecycle. So, unlike tools that focus on only code, Rovo Dev does a lot more. Secondly, it is a terminal-first
context-rich experience, which means it is designed to meet you wherever you are working, in the IDE, in the CLI, in Jira, and in the CI/CD pipelines. And it is enterprise grade
security and customization. It lets teams customize workflows, set review standards, but also tailor AI behavior. Thank you so much for listening. If you do have any questions, I will be right behind. Also, I'm at the Atlassian booth, and there's a lot more demos
I can do than just this one. Thank you all for coming, and thank you all for being patient.
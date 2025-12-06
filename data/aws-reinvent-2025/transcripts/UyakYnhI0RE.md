---
video_id: UyakYnhI0RE
video_url: https://www.youtube.com/watch?v=UyakYnhI0RE
is_generated: False
is_translatable: True
---

- Hello. Hello, everyone. First of all, thank you
for coming to this talk and I hope that you have
been having a nice time at AWS re:Invent. My name is Mohammad Wasiq, and I am one of the
lead security engineers in Amazon GuardDuty. My core job in GuardDuty
is to research, develop, and continuously improve its
threat detection capabilities. And during the last three years, I have been focusing on
GuardDuty runtime monitoring. In this talk, you'll learn how
GuardDuty gathers information about real-world threats, how it uses this information to prioritize and implement threat detections, and how you could use
realistic attack scenarios to test GuardDuty runtime monitoring. For those of you who don't
know what GuardDuty is, it is a threat detection service that monitors various log
sources in your AWS account, such as CloudTrail logs and VPC flow logs and applies machine learning and detection rules to
detect threats in real-time. And what is GuardDuty Runtime Monitoring? It's an optional runtime
monitoring solution offered by GuardDuty. It involves deploying an eBPF agent to your AWS compute workloads,
such as EC2 instances. The eBPF agent gathers various
operating system level events and sends those back to GuardDuty back and for monitoring and threat detection. An important question to
ask is why do you need to test the runtime monitoring solution? An obvious reason is, you
would like to evaluate the runtime monitoring
service to make sure that it meets your requirements. Another important reason
is that you would like to test your incident
response capabilities because it is really important to have a robust incident
response procedure to respond to runtime monitoring findings. We have noticed that many
customers use simplistic tests when testing runtime monitoring, and these simplistic tests often map to a single Mitre technique. For example, a customer
would create a cron job to test detections for
persistence activity. There are two primary issues
with these simplistic tests. First of all, they're not realistic. Secondly, they do not
provide you any information about the noise reduction or the noise management capabilities of the runtime monitoring solution. So you can see that all of these actions are very common actions in
benign activity as well. For example, creating a cron job is a very common benign activity. So when you use these simplistic tests, you don't get any insights into how good is the runtime monitoring solution in filtering out benign activity from the actual threat activity. So for more effective testing, you need more realistic attack scenarios, and this is what you're going
to learn in this talk today. First of all, let's see how GuardDuty gathers information
about real-world attacks. The first and one of the
most important sources of information are the
actual customer incidents. We have a team called AWS CIRT, or Customer Incident Response Team that helps customers in responding to their security incidents. And from these customer engagements, we gather valuable
information about tactics and techniques used in actual
attacks against AWS customers. We also learn about the most common or the top techniques used
against AWS customers. Based on data from AWS CIRT, the top two initial access
techniques used in attacks against AWS customers are:
compromised credentials and public-facing application compromise. Compromised credential means
that an attacker is able to get hold of your AWS
credential or IAM credential, and uses it to gain access
to your AWS account. From there, they could exfiltrate data, send out spam emails, or create compute workloads
for resource hijacking. Public-facing application compromise means that you have a vulnerable
public-facing application. The attacker is able to
compromise the vulnerability and gain access to the
underlying compute resource such as the EC2 instance, and from there, they can
perform various activities such as crypto mining or DDoS against other targets on the internet. Data from AWS search shows that a vast majority of
attacks against AWS customers deploy these two initial
access techniques. And this is the reason
why GuardDuty prioritizes developing detections
for these techniques, not just in GuardDuty runtime monitoring, but other GuardDuty features
such as CloudTrail monitoring. Furthermore, the
real-world attack scenarios that you'll be learning about in this talk are also based on these two
initial access techniques. Another source of information
on real world attacks is the threat intelligence
that GuardDuty consumes. GuardDuty uses various in-house and third party sources
of threat intelligence, and this is what we learn from these threat intelligence sources. First of all, we learn about
indicators of compromise. These are the IP addresses, domain names, and file hashes used in real attacks. We also learn about the tactics and techniques used in real attacks and various activity patterns
used in real attacks. Last but not least, we also learn about
the context surrounding real-world attacks or real-world threats. The context is really important because it informs
GuardDuty about the types of applications and environments
as specific threat targets and the sequences of tactics
and techniques they deploy. Let's try to visualize
and understand all this using a simplistic
real-world attack scenario. Web application compromise is one of the most common attack
vectors routinely captured by our honeypots. This is how a typical web
application compromise works. The attacker compromises a vulnerability in the web application
to deploy a webshell. Once they have deployed the webshell, they can execute any command on the underlying operating system. Typically, what we have
seen as the first step what they do is that
they download a script, a shell script, which is a
script malware, and execute it. Then the script malware is used to download a second stage malware, which could be a crypto miner
or a DDoS malware or anything. Then of course, they make the second stage malware executable using the chmod command. And then finally, they execute
the second stage malware. And usually, the attackers
also persist the execution of the second stage malware by creating a scheduled
task or a cron job. You can see that all of these
actions or activities mapped to specific Mitre tactics and techniques. You can also see that we
learn about specific patterns used in these techniques. For example, in this case, the attacker uses the curl command to download a script malware
from an IP address-based URL and pipes it to a shell process. Another interesting pattern is the creation of the cron job. Here, in this case, the
attacker writes the instructions for the cron job to a temporary file and loads that temporary file
using the cron tap command. And we also learn about the
context surrounding these, all these actions or steps. So for example, in this case, all these actions originate
from a web application or a network-facing application, and they follow a very specific sequence. So this example demonstrates
how GuardDuty learns about tactics and techniques and activity patterns used in
real attacks or real threats, and how it uses it to prioritize and develop threat detections. Now, let's see how you could detect GuardDuty runtime monitoring using realistic attack scenarios. We have added multiple realistic scenarios to Amazon GuardDuty tester. Let's see what is Amazon GuardDuty tester. Amazon GuardDuty Tester is
a public GitHub repository which allows you to test
various GuardDuty findings. You can search it on Google. When you load the main page
of the GitHub repository, you'll find easy to use instructions to set up a secure test environment, lockdown test environment
in your AWS account. When you follow these instructions and execute these instructions, they set up a lockdown
VPC in your AWS account with various resources
such as EC2 instances, an ECS cluster and an EKS cluster. Once you have set up the test environment, the next important step is to make sure that GuardDuty runtime
monitoring is enabled. Open up the GuardDuty console on the left-hand side, click
on runtime monitoring link. There it is. This will take you to the main runtime
monitoring enablement page. Make sure that runtime
monitoring is enabled. In this case, it's enabled, but the agent management for
AWS Fargate is not enabled. Let's go ahead and enable it. Also, the agent management
for Amazon EC2 is not enabled. Let's go ahead and enable it. So now, the test environment is set, let's go ahead and execute the test. So you are going to execute
the test in two steps. In the first step, you are going to deploy a vulnerable PHP
application on the EKS cluster, and in the second step,
you are going to execute an attack against that PHP application. Let's go ahead and do that. When you create the test environment using Amazon GuardDuty tester, it creates several EC2
instances in your AWS account. One of those instances is
driver GuardDuty tester. You're gonna be connecting to this instance using SSM start session to start a terminal session. And from there, you'll be
executing the attack scenario. Let's open up the Amazon
GuardDuty tester repository again. It provides the command, the
SSM start session command to connect to the driver instance. Copy that command. Now, open up a terminal window
on your client side host. Make sure that it is set up with AWS CLI and also has permissions to
perform SSM start session. First, set up the region
where you have installed or created the test environment using Amazon GuardDuty tester. Now, paste the command and execute it. Now, you are logged into
the driver instance. So inside the driver instance, you will find various
files and directories. One of those directories
is runtime scenarios. Let's look into this directory. You'll find various
realistic scenarios here. One of those is php webshell, and this is you are
going to execute today. Let's go ahead and look
inside php webshell. So in this directory, you'll
find two different scripts. One is deploy php and the other is attack. Deploy php deploys the PHP web application on the EKS cluster. Let's go ahead and deploy
the php web application. When you execute deploy php, it creates an ECR repository and loads a php apache
container image to it, and then uses that image to create an EKS part on the EKS cluster. So now, the pod is being
created. Let's wait a little. So the pod is now created, and this is the name of the pod, and this is the IP address where the web application is accessible. After creating the pod, the script also performs
various setup steps on the pod. One of the more interesting setup steps is to set up a command and control server to simulate command and
control communication for the scenario. Now, the php application is deployed. Let's go ahead and execute the attack. When you first start the attack script, it ask permissions to modify or to create the necessary GuardDuty permission
settings in your account. Allow it to do that. As the first step of the attack, the script gets the IP address
of the php web application. Then it accesses the index.php exploits the vulnerability to deploy a webshell. Once it has deployed the webshell, it executes various commands through it. For example, it execute
various discovery commands, it downloads malware and executes it. So here you go. This completes the execution
of the attack scenario. Now, let's see what finding
GuardDuty generated. Let's open up the GuardDuty console and click on the findings
link on the top menu. This will take you to all
the findings generated. The scenario should have
generated multiple findings. For example, when multiple
commands were executed through the webshell, GuardDuty generated a high severity suspicious command finding to make sure or to verify that originated from the php web application. Let's look at the process
lineage of this finding. And here you find that the
parent is apache2, which means that it actually originated
from the php application because we are using apache to run php. The attack scenario also executed nmap for network reconnaissance. And because of that, GuardDuty generated a
suspicious tool finding. Let's scroll down. And you can see that the
name of the process is nmap. So here it is. The attack scenario also downloaded and executed a crypto miner. So GuardDuty generated a
crypto miner executed finding. Let's look into this finding. And to verify that it also originates from the php web application, let's look at the process
lineage of this finding as well. And here you can see that
the grand parent is apache2, which means that it actually originated from the php application. Last but not least,
GuardDuty also generated an attack sequence finding. So this is an aggregate
or the composite finding which provides the comprehensive view of all the tactics and
techniques and signals detected during the attack scenario. So here you go. So these are the key
takeaways from this talk. So in this talk, you learned how GuardDuty gathers information
about real-world attacks and uses it to prioritize detections and implement threat detections and how you could use
realistic attack scenarios to test GuardDuty runtime monitoring. And we have added multiple
realistic scenarios to Amazon GuardDuty
tester GitHub repository, which you can access from this QR code. And we'll continue to
add more scenarios to it. And thank you again for
attending this talk.
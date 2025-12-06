---
video_id: x0VDgkyaVyE
video_url: https://www.youtube.com/watch?v=x0VDgkyaVyE
is_generated: False
is_translatable: True
---

- Good afternoon, thank
you for being here. My name's Jim White, I work
for Amazon Web Services, and today we have the privilege of hearing from Arek from "The New York Times." I'm sure we're all familiar
with "The New York Times." He's gonna share a little bit of his implementation experience with his deployment of
FSx for NetApp ONTAP. So without further ado, Arek,
I'm gonna turn over to you. - Thank you. So my name is Arek Chojnacki, and we migrated successfully a lot of SMB shares and NFS shares to FSx. So let's start from the
beginning, you know. So we have Windows shares, we have the NFS shares, and we have those shares
on different platform. We have on the Isilon, we
have a Windows File Servers and we want to migrate this data to FSx. So in this session, what I'm gonna cover, I'm gonna cover the Amazon FSx for NetApp ONTAP design and deployment, which is the critical component of the migration, consolidation and
migration journey to FSx, benefits of migration, challenges, And if we have time, I'm gonna talk about the, I will have time for Q&A. So first of all, before we gonna start, what we have to know, first of all, we have to know our data. So we have to know couple components. First of all, we have
to know the utilization of each share, including actually to design the volumes and what we have to also
know about the data. We have to know the
hot data and call data. What is the hot data? Hot data, that's the data which it's 30 days active. Last 30 days. Last 30 days, this data have been written to our shares. And why? Because that will define our performance tier, SSD tier on FSx. And then we have to
know also the call data, which this data will be allocated later on on our capacity tier. And we have to know also the type of the data. Why we have to know the type of the data? So we can predict the data reduction, including the data
application and compression. From the data protection, we have to know our high availability. Do we need the HA? And in this case, we should
implement the multi-AZ and FSx. Also, we have to know our definition and SLA for the cover point objective to define the snapshot,
policy, and backups and disaster recovery. If any of the volumes, all the data require
the disaster recovery, that will be our candidate
to replicate between regions. For purpose of this session, I will review all migration steps for imaginary project. And starting our project, we will collect the data
from current environment. And let's say we have nine shares approximately from S1 to S9. We collect the data, we
identify the hot data, that's the data which
is less than 30 days. And we also will collect how much we have the call data. How to get the information? If you're gonna ask anybody
it, then everybody will say, "Yeah, all my data is active." But if you have the
third-party software, tools, you have the PowerShell, Robocopy, you can identify and you can identify that
from the 100% of the data, maybe 10% to 20% is the hot data. So we have nine shares, and with nine shares,
those shares they belong to three department, Department 1, Department
02, and Department 2. From HA, we need HA for each share, but we don't need the R for each share. For example, the S1 is our, you know, ISO images, et cetera. We don't need them, you
know, to be replicated. And from the RPO in hours, we see the difference in our requirement from each department, from each share, from 24 hours to one hour. So, let's group all shares by attributes and define the Volumes capacity, because this is very important. Remember that from the
snapshot policy, backup policy, everything gets based per
volume, not per share. So the volume size, how we will ba basically
design the volumes, will contain the data size. Plus we will add the reserve
capacity for the snapshot. In my example, I like, you know, to reserve 20% of the capacity dedicated
for the snapshots. And let's say we expecting that growth per year around 20%. And for the auto grow, because we can set up
the auto grow per volume, we estimated that we should not expect the growth over 150%. So based on the grouping of those shares, we came out, you know, to this conclusion that we will create five volumes based on the current utilization, so we can combine everything. We have also the volume size, snapshots. 20% grow out, and then we have the
volume size in gigabytes. So as you can see, we
will have the volumes from 140 gigabytes to five terabytes. But what is very important
during the migration, the data flow when we
write the data to the FSx. From the source data, writing all the time the
data on the first step, first wave to SSD. And then in SSD, we have the duplication and compression and then we can move the
data to capacity tier. So for example, if we have one terabytes of data and we want to set up the auto-tiering all, automatically
go everything to the S3, then everything first
has to land on the SSD and then move to the capacity tier. So the critical component of the FSx, it's SSD, which is the performance tier. If we don't design this SSD tier correctly, we can face probability that we not will be able to write to FSx because all the SSD tier
will be overwhelmed. So what is the algorithm? During all those migration, and I came up with the algorithm, which actually, it's very accurate and we don't have to actually extend the SSD
tier for very, very long time. So first of all, we have the largest set of data which we want to migrate to FSx, and we are anticipated this data will land in first step in an SSD tier to do that duplication and compression. Then we have the sum of all the hot data from all our volumes, and SSD size should be all the hot data plus 50%. Because what's happened
is with the auto-tiering, when we have the SSD, then the first data, it's going to SSD, and we should have the 50% available after we will write all those hot data because the algorithm of the auto-tiering will trigger the movement of the data from the SSD to capacity tier based on our auto-tiering policy. And also the SSD has to exceed 51%. Then when we do the backup or we are moving the data, then with the storage efficiency, we have to have space to actually make sure that the SSD will handle the amount of the data which we'll be putting on the FSx. With the backup, we have
exactly the same situation. The backup is a little bit different because if we want to
restart from the backup, it's on the backend. So the data flow, it's much, much faster. And we can overload the SSD team. So this is critical. If we have the SSD and we have the setup correctly, then we are not gonna see the spike over 70 to 80% or utilization of SSD. So at this point, based on all the situation and scenario, we are configurating
our FSx for NetApp ONTAP in two regions, our reproduction in one, our Region 2 of the multi-AZ SSD based on our calculation. We have the five volumes. Then we have the
replication to region two, but for the region two, because that will be our target, we don't have to do the
multi-AZ, we can do single AZ. So we can save money on the SSD tier. So, first we have to build based on the design we building the FSx, we have the SSD, so we define the SSD, we have our volumes, we do the flex volumes, we enable storage efficiency and default volume, during the migration, it's all, so everything should go directly to S3. Why we want to use the, at this point, you know, SSD tier? We want to use the SSD tier
only for the data efficiency. Then we create all those volumes. At this point, we are not
creating the snapshot, we are doing the migration. So after we finish initial
copy, initial sync, then we're gonna start doing the snapshot. On the beginning, we don't need to. Then, with the migration steps, so when we set up the storage efficiency, all going to S3, we have the SSD capacity, excuse me, performance tier, set it up. Then right now we are starting
the sync, the initial sync. At this point we can use any software which we want to. We can use the rsync,
we can use the robocopy, we can use the third-party software, and then we can also use
the robocopy for Windows and we have to finish the initial copy. Then when we finish that initial copy, then what we have to do, we have to enable the auto-tiering. Why we have to enable the auto-tiering? We have all data in S3. Right now, we want to
put all the hot data, the delta, to SSD. So our hot data will be in SSD. So at this point, when
we start doing this, the old hot data will land in the SSD and we'll wait until, you
know, 30 days, for example, and then they will be
moved to the capacity tier. Also, at this point, we will start doing the snapshots because we want have the snapshots. Also, very nice thing with the snapshots, the FSx snapshots, for
example, with Windows, it's integrated with the shadow copy. So you can see the shadow
copy in your windows. And after initial copy, what we already did, and we want to set up the backup. The backup, it's set up a little bit, you know, tricky because, (clears throat) excuse me, you set up the backup based on the FSx, not based per volume. So the backup, it's global
settings for your FSx. If you have different requirement, then you should use the AWS backup or you can set up the more than one FSxs. Then we have to also
set up the replication between source and target. For this particular exercise, I'm really recommending, you know, using the BlueXP because it's very easy to set this up. The cut-over. Cut-over is the most
painful, I will say, task. So first of all, if you have the global
namespace like the DFSN, then you have the ability to actually cut over individual shares, not the whole value. Otherwise, if you are using CNAME, then it's a little bit tricky. If you want to schedule the cut-over, you need to have the time of sync for the delta from last 24 hours. So you can automatically estimate how much downtime you're gonna
interest during the cut-over. And before start thinking the last delta, then I'm recommending, you know, to set up the source to read-only, sync the data, and then you can cut over
and do the read-write. And benefits of migration, what we did. We eliminate complexity
of our current solution, managing NAS, Windows
File Servers, et cetera. Right now, we have everything
under one pane of glass. We also optimize cost of SMB and NFS shares in AWS. After migration from all our solution, which we have on prem and in AWS, our cost has been reduced
approximately around 70%. And why? Because we have introduced the
duplication and compression, and with the auto-tiering cost of the S3, it's much more or less compared if you have to put everything on the SSD. So, in this small comparison, I want to compare, you
know, Windows File Servers. If you will migrate
the Windows File Server with all those, you know, servers
which we have two NetApps. So as you can see, in our scenario, from nine servers, because we need the HA
between AZ1 and AZ2, then we need also another
set in the west region. So, and from the EC2
instance's point of view, we shrink from nine to four. And so savings is five, cost of the five EC2 instances. As you can see, you know, it's a significant. Then, EBS volumes, remember, one thing with the FSx is that it's thin provisioning. On EBS volumes, you
have thick provisioning. So if you have any solution
with the thick provisioning, you are paying a lot of money, not for the utilization of the storage, but for the provision storage. And S3, we don't have the S3
under another solution because they don't support S3 with the FSx because support S3. We add cost of the, for
example, 15 terabyte of the S3. But it's significant lower
compared to the EBS volumes. Our challenges. So design of the volume, it's tricky. And you cannot find golden rule. But what you have to look, you have to know your data, and based on your data, you can actually group all those, you know, shares and then create the volumes based on the requirement, RPO, RTO, and the snapshots and backup requirement. And capacity of the SSD of the performance tier, it's critical. And the most important thing is coordinating with the stakeholders. It's very difficult many times, and everybody knows why. Everybody, they don't have the ability, you know, to introduce any downtime during the production hours. So it's very difficult actually
to find out the golden time. And set up appropriate monitoring, which is critical. Utilization of the performance
tier, it's critical, and we should know if it's up to 70% that that will be warning. 90%, this is alarm and you
have to react right away. CPU utilization, yes,
we should check it out, the CPU utilization, especially if some other
people are moving transit data, then perhaps we have
to also resize the CPU because of the number of the data which we
are pushing in the FSx. And latency, which is
very important for us too. And what we like about FSx for ONTAP. High ability in the regions. AZ1, AZ2. And we don't have to, you
know, worry about anything. Auto-tiering. Deduplication and compression. Integration with Windows DFSN. DR between the regions, it's very, very good. Ransomware protection. Snapshots with Windows previous version. Windows ACL, Scalable, performance, encrypted at rest, and multi-protocol. And just summary of the session, first of all, you must know your data. You have to take all
variables into consideration to meet SLA, especially from point of
view of the RPO and RTO. Use BlueXP to manage your FSx environment. Also check it out, you
know, ransomware protection. This is very important. Today was very good session regarding the ransomware
protection in the morning. And attend all FSx session to better understand FSx under the hood. My time is up. I'm sorry. Thank you so much, and have
a nice AWS and re:Invent, and I recommend to attend all those session about the
Fsx, because it's for us. It's a great product. Thank you.
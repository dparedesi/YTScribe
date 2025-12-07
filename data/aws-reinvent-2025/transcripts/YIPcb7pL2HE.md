---
video_id: YIPcb7pL2HE
video_url: https://www.youtube.com/watch?v=YIPcb7pL2HE
is_generated: False
is_translatable: True
summary: "This session, delivered by Aaron Daly and Jim from AWS, focuses on optimizing self-managed database deployments using the Amazon FSx family of file systems. While fully managed services like Amazon RDS are popular, the speakers explain that many customers opt for self-managed databases on EC2 to retain granular control over infrastructure, software versions, and backup schedulers, or to optimize licensing costs. The core argument of the talk is that storage choice is critical in these architectures. They introduce three specific FSx services tailored for database workloads: **FSx for Windows File Server** (ideal for SQL Server via SMB), **FSx for OpenZFS** (high-performance NFS for Oracle), and **FSx for NetApp ONTAP**, which is presented as a \"Swiss Army knife\" supporting multi-protocol access (NFS, SMB, iSCSI) and advanced data management features.

A major portion of the session details the unique capabilities these storage services offer over traditional block storage like EBS. Key among these is the ability to create **instant snapshots** that are database-consistent and independent of database size, allowing for backups in seconds and recoveries in minutes. Closely related is the **cloning** capability, which allows engineers to create multiple thin, writable copies of a production database almost instantly. These clones consume negligible storage (initially just metadata) and are game-changers for creating development/test environments, testing upgrade patches, or running \"what-if\" scenarios without impacting production or incurring significant costs.

The speakers also highlight the financial and operational benefits of **storage-level replication**. Unlike database-level replication (e.g., SQL Server Always On Availability Groups), which consumes compute cycles and often requires expensive Enterprise licenses, storage replication (like NetApp SnapMirror) handles data movement at the infrastructure layer. A customer case study is cited where switching to a Failover Cluster Instance (FCI) deployment with FSx shared storage saved 60% on SQL Server licensing costs. Other customer examples include S&P Global using SnapMirror for disaster recovery and Amdocs achieving better-than-premise performance through features like inline compression.

The session concludes with extensive technical demos illustrating practical workflows. The first demo showcases a Disaster Recovery (DR) scenario for SQL Server using FSx for NetApp ONTAP, where a snapshot is replicated to a DR region and cloned to verify data integrity without interrupting the replication stream. The second demo features an Oracle deployment on FSx for OpenZFS, where an 18GB production database is cloned for development use, consuming only ~40MB of additional space. These examples reinforce the session's practical focus on using advanced storage features to improve agility, reduce costs, and enhance data protection for self-managed databases."
keywords:
  - Amazon FSx
  - Self-managed databases
  - SQL Server
  - Oracle
  - FSx for NetApp ONTAP
  - FSx for OpenZFS
  - Database Cloning
  - Disaster Recovery
---

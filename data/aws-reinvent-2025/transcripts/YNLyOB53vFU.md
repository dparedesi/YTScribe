---
video_id: YNLyOB53vFU
video_url: https://www.youtube.com/watch?v=YNLyOB53vFU
is_generated: False
is_translatable: True
summary: >-
  Salesforce’s Natalia Leon and Sid, joined by AWS solutions architect Bill,
  explain how Salesforce Data Cloud (Data 360) and AWS enable “zero-copy”
  activation so enterprises can unify siloed data, preserve governance, and feed
  AI/agent use cases without replicating sensitive datasets. Leon frames rising
  customer expectations for personalized, anticipatory experiences and the
  difficulty companies face when data is fragmented and unreliable. The joint
  solution centers on optionality: Data 360 accesses data wherever it lives—
  warehouses, lakehouses, streaming, SaaS—via rich connectors, including keystone
  zero-copy access to AWS Glue Iceberg catalogs and S3, so analytics, segmentation,
  and agents always see fresh data. Sid positions Data 360 as an activation engine
  with three building blocks: connect, harmonize, and govern. Harmonization
  standardizes schemas, resolves identities, and constructs unified profiles as
  the atomic unit of personalization, decoupling application and agent development
  from source schemas. Governance spans policy at table/row/column levels, and the
  same foundation powers Customer 360 apps (Sales, Service, Marketing) and Agent
  Force agents that need structured and unstructured pipelines, NL-to-SQL at
  scale, and governed memory to carry context between interactions. He clarifies
  real-time vs. zero copy: real-time pipelines materialize data in Data 360 (web
  engagement), while zero copy queries external Iceberg tables at runtime,
  preserving a single source of truth and satisfying lines of business that forbid
  duplication. Zero copy now accounts for over half of Data 360 traffic across
  tenants. Bill details the AWS side: roadmaps span query federation (JDBC to
  Athena/RDS/Aurora/Redshift), file federation (beta, GA Feb) for Iceberg tables in
  S3/Glue with pushdown, pruning, and parallelization via Data 360’s native engine,
  and bidirectional flows where Glue/Lake Formation catalog and S3 objects are
  accessed securely with short-lived SIGv4 credentials, avoiding long-term
  secrets. Iceberg change logs enable incremental change feeds, better performance,
  and lower costs (pay only on the Data 360 side). Compared to single-threaded JDBC
  pulls, file federation supports larger files, more partitions, and parallel
  scans while maintaining fine-grained permissions with Lake Formation and Glue
  Data Catalog. Bill recounts a fintech customer evolving from RDS query federation
  to data-lake file federation to power Customer 360 matching and marketing, while
  analytics teams still operate in AWS; data freedom supports Agent Force in
  Salesforce and Agent Core in AWS using the same Iceberg tables. Live demo
  snippets show configuring Glue connections with only catalog access keys (S3
  credentials vended at runtime), creating data streams pointing to external
  tables, and seeing CRM related lists populate on demand from Redshift and Glue
  without persisting data in Data 360. The graph view illustrates metadata-driven
  harmonization: objects map to external sources, with identity resolution
  consolidating duplicate records (e.g., 100 raw down to 50 unified profiles) for
  personalization. Sid notes data actions triggered by Iceberg change feeds
  (create/update/delete) and performance gains from operating on increments rather
  than full tables, plus governance with policies, glossary taxonomy, and AI
  assistance via Amazon Q for metadata enrichment. Customer stories include
  1-800Accountant unifying Salesforce, data lakes, and tax systems to deploy agents
  that answered 70% of administrative questions during tax season, scaling
  advisers for high-value work, and Buyer’s Edge integrating 20+ systems to deliver
  tailored procurement offers. They invite attendees to see the full demo at the
  Salesforce booth and stress that zero copy, open formats (Iceberg), strong
  governance (Lake Formation), and harmonized metadata let companies unlock data
  for AI safely and efficiently.
keywords: zero copy, Data 360, Apache Iceberg, Lake Formation, Customer 360
---

---
video_id: V2wFP-qzahY
video_url: https://www.youtube.com/watch?v=V2wFP-qzahY
is_generated: False
is_translatable: True
summary: >-
  Sean Ma and Iris Xu present the next generation of Amazon SageMaker as a
  single integrated experience that unifies data, analytics, and AI tooling for
  teams struggling with fragmented stacks, data sprawl, and governance gaps.
  They explain that the revamped SageMaker, launched at re:Invent 2024 and now
  rolled out to 15+ regions with dozens of enhancements, layers a Unified
  Studio for SQL, Python, visual, and natural-language workflows on top of the
  SageMaker Catalog for end-to-end governance and an open Apache Iceberg-based
  lakehouse that exposes S3, Redshift managed storage, and Iceberg tables
  consistently to engines like EMR, Glue, Athena, and Bedrock. The goal is to
  collapse tool silos so data engineers, analysts, data scientists, and data
  stewards collaborate in one workspace with shared access control, lineage,
  quality checks, and Bedrock Guardrails for responsible AI. Iris highlights
  four 2025 launches aligned to those personas: visual workflows that let data
  engineers orchestrate Glue jobs and other tasks via drag-and-drop without
  Airflow code, while still exporting or importing IaC; onboarding unstructured
  S3 assets into the SageMaker Catalog so producers can tag and govern images,
  video, and documents alongside tables using S3 Access Grants and semantic
  search; a QuickSight integration that publishes certified datasets from the
  catalog directly into dashboards with lineage and policy inheritance; and
  tag-based access control over S3 tables to simplify security at scale. Sean
  then unveils a fully serverless notebook that natively mixes SQL and Python,
  auto-manages compute with Athena for Apache Spark under the hood, auto-passes
  SQL results into Python variables, and ships with an MCP-based data agent
  aware of catalog metadata. In a live demo he spins up Unified Studio with a
  single IAM role, explores the Glue catalog via the agent, queries a digital
  wallet LTV dataset, and uses the agent to propose visualizations comparing
  satisfaction scores to long-term value; seeing weak correlation, he asks the
  agent to build a multi-step linear regression workflow that splits data,
  trains, evaluates, and surfaces feature importance—revealing income as the
  dominant factor, satisfaction as secondary, and support tickets as a negative
  signal. The demo illustrates how the agent breaks complex tasks into runnable
  cells, how governance and access are inherited from the catalog, and how
  serverless notebooks remove provisioning friction. Throughout, they emphasize
  customer feedback driving ease-of-use investments, responsible AI controls,
  and continuous expansion of supported tasks (100+ workflow steps), engines,
  and data connectors (150+ ETL and federated sources). They close by urging
  attendees to try Unified Studio, noting early adopters like Deloitte cite
  faster experimentation and delivery from the consolidated developer-centric
  environment, and reiterate the vision of SageMaker as the sole tool needed by
  data engineers, analysts, scientists, and stewards to move AI initiatives
  from siloed pilots to governed, production-grade workflows on a single data
  foundation.
keywords: SageMaker Unified Studio, data governance, Apache Iceberg, serverless
  notebook, data agent
---

---
video_id: WbR_La3h578
video_url: https://www.youtube.com/watch?v=WbR_La3h578
is_generated: False
is_translatable: True
summary: >-
  Naresh Chanani frames the session around eliminating workload contention on
  Amazon Redshift by moving from monolithic clusters to multi-warehouse
  architectures, then walks through patterns, governance, and AI integrations
  while welcoming AWS architect Anusha Chala and Vanguard data engineering
  director Alex Rabinowitz. Chanani explains how hub-and-spoke designs split a
  single cluster into independent serverless or provisioned endpoints sized and
  budgeted per workload (streaming ingestion, batch ETL, dashboards, data
  science), delivering isolation, chargeback, and rapid spin-up, even across
  regions without copying data because Redshift Managed Storage holds the
  single source of truth. A data mesh pattern applies the same idea to
  organizational domains—finance, marketing, HR—letting each own data and share
  securely via snapshot isolation at row or column granularity while keeping
  compute separate. Under the hood, Redshift Managed Storage uses columnar
  formats and hardware-optimized encodings, and customers can mix provisioned
  clusters for steady workloads with serverless for spiky access; all endpoints
  can span accounts and regions to satisfy sovereignty rules. Newly launched
  federated permissions unify fine-grained access across endpoints so policies
  are defined once and reused, avoiding manual duplication as compute scales
  out. Redshift also embraces open table formats: more than half of large
  customers combine warehouse data with Iceberg tables in S3, benefiting from
  recent 2x performance gains, appended writes, and the ability to join
  warehouse and lake data in one query. SageMaker Unified Studio exposes
  Redshift, Iceberg, and S3 tables through a single catalog and Iceberg REST
  API, allowing analysts to use SQL notebooks, natural language to SQL, Athena,
  Spark, QuickSight, and orchestration tools with consistent governance, while
  Bedrock integrations let SQL users call foundation models for tasks like
  sentiment analysis directly from Redshift or use Redshift as a Bedrock
  knowledge base. Vanguard’s case study recounts starting with a centralized
  warehouse that grew to 600+ tables, 400 views, and 100 users issuing 500k
  queries monthly, leading to locks, SLA misses, and complicated workload
  management as ETL clashed with analytics. They shifted to hub-and-spoke,
  giving analysts dedicated serverless compute and sharing curated data via data
  sharing, which improved SLAs and analyst experience but still left
  centralized ownership challenges, motivating a future data mesh with Iceberg,
  incremental materialized views, and parallelized domain ETL to avoid
  cross-domain locks. Anusha’s demo uses a fictitious “Any Company” to show
  three separate serverless endpoints for ETL, reporting, and generative AI.
  Using zero-ETL for Oracle RDS, transactional sales tables replicate into
  Redshift in seconds, while clickstream data lands in managed Iceberg tables
  via Firehose. The SageMaker catalog automatically inventories both lake and
  warehouse data, and AWS IAM Identity Center groups receive table-level SELECT
  permissions for analysts. Analysts connect to the reporting endpoint, run
  joins across Redshift and Iceberg for KPIs, and stay isolated from ETL load. A
  Bedrock knowledge base built on the generative-AI endpoint uses Redshift
  tables so users can ask natural-language questions, receive SQL or tabular
  results, and switch between models. The session closes urging customers to
  adopt multi-warehouse patterns for isolation, cost control, and AI readiness,
  with references to workshops and resources.
keywords: Amazon Redshift, multi-warehouse architecture, data mesh, federated
  permissions, Bedrock integration
---

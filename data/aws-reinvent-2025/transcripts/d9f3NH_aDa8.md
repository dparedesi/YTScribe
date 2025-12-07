---
video_id: d9f3NH_aDa8
video_url: https://www.youtube.com/watch?v=d9f3NH_aDa8
is_generated: False
is_translatable: True
summary: "This Clumio (now Commvault) session demonstrates how to make GenAI application data resilient using a fictitious 'Clumio Flick' movie app with LLM chatbot features. Three recovery scenarios are covered: 1) **DynamoDB**: Canary deployments can corrupt partitions at different timestamps. Clumio Backtrack for DynamoDB (launched June 2025) enables in-place, granular, point-in-time recovery to the source table—avoiding 'recovery hell' of full restores per partition. 2) **S3 (RAG Pipeline)**: Lost S3 objects break vector embeddings, causing LLM hallucinations. Clumio Backtrack for S3 (announced at re:Invent 2024) offers in-place, object/prefix/bucket-level recovery with continuous change tracking for zero data loss, avoiding vector recomputation. 3) **Apache Iceberg (S3 Tables)**: Industry's first Iceberg-aware data protection (launched September 2025) preserves table structure during backup/restore, supports snapshot-based recovery, and enables migration from AWS Glue Catalog to S3 Tables. All three use SecureVault for air-gapped, immutable, cyber-resilient copies. Best practices: protect entire data pipeline, prioritize speed, and architect for scale. Demos show Python-simulated corruption and recovery via the Clumio UI."
keywords: Clumio, Data Resilience, DynamoDB, S3, Apache Iceberg, S3 Tables, Backtrack, SecureVault, RAG Pipeline, Cyber Resilience, GenAI, Point-in-Time Recovery
---

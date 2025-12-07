---
video_id: L2v8WdBGjvg
video_url: https://www.youtube.com/watch?v=L2v8WdBGjvg
is_generated: False
is_translatable: True
summary: |
  Sachin Hola introduces Ashi Singh, who details how Pinterest serves 600M monthly users atop a 500 PB S3 data lake (100k Hive/Iceberg tables, 20k Spark nodes, 1k Trino nodes, 400k jobs/day) by moving from Hive to Apache Iceberg. Pinterest spent two years socializing Hive’s limits and began Iceberg buildout in 2022; first production use in 2023 focused on GDPR-scale user deletions. Today 15k Iceberg tables hold ~200 PB, growing table count 300% YoY while data growth stays moderate thanks to better compression. Iceberg is accessed via Trino, Spark, Flink, Python metadata reads, MapReduce writers, and Ray.
  
  **User deletion:** In Hive, deletions rewrote entire partitions, disrupting downstream readers and incurring high costs. Iceberg’s snapshot isolation allows rewriting only files containing deleted users, but naive batching still touched many files. Pinterest sorted data by deletion key to cluster a user’s records, but full-table sorts on 40–50 PB tables were prohibitive. They added logic to sort only unsorted files and contributed related changes upstream (Iceberg, Spark), ultimately scaling deletion throughput 10x, cutting storage and compute costs ~30%, and improving job reliability 90%.
  
  **Table sampling:** Data scientists needed reproducible samples and meaningful joins between independently sampled tables. Engine-level Bernoulli/system sampling produced non-overlapping keys. Pinterest bucketed Iceberg tables and defined sampling as reading whole buckets (e.g., 1 of 100 buckets for 1% sampling) using consistent bucketing keys across tables. This guaranteed key overlap for joins, delivered ~90% query speedups for exploration, and kept deviation from full-table results under 1%.
  
  **Feature backfills:** Recommendation and ads models rely on tens of PB spanning months. Forward logging new features required 3–6 months of data accumulation and intertwined experimentation with production. Backfills were blocked by expensive sorts/shuffles on petabyte-scale joins. Using Iceberg bucket (storage-partition) joins on Trino and Spark (backported to 3.2) and enabling Ray to read bucketed data, Pinterest avoided massive shuffles, saving ~65% on join costs and boosting feature development speed 90x, enabling counterfactual backfills over forward logging.
  
  **Operational learnings on S3:**  
  - User-agent-based access control at the bucket/prefix level prevented accidental writes from non-Iceberg-aware clients during in-place Hive→Iceberg migrations (table definition swap without data copy).  
  - S3 inventory and request logs surfaced orphan files (unreferenced by snapshots) and misuse of Iceberg tables; inventory comparisons guided cleanup of unreferenced data.  
  - Throttling (503s) persisted because legacy Hive partitioned paths had low entropy. Adopting Iceberg’s hashed object locations (20-bit base2 prefix) for 66% of top datasets eliminated user complaints and request throttling.
  
  Singh closes by emphasizing Iceberg’s role in cost control (reduced rewrite scope, better compression), reliability (snapshot isolation), and developer velocity across privacy, analytics, and ML pipelines, with key improvements contributed back to the open-source ecosystem. The trajectory—table counts tripling while data growth is tamed—shows Iceberg enabling faster experimentation without runaway storage or operational drag.
keywords: Apache Iceberg, Pinterest, S3 data lake, user deletion, bucketed sampling
---

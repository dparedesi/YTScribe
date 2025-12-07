---
video_id: cxXG5fZ5wik
video_url: https://www.youtube.com/watch?v=cxXG5fZ5wik
is_generated: False
is_translatable: True
summary: >-
  Netflix engineer Ammar recounts how the data platform team migrated dozens of
  application databases from a self-managed, Postgres-compatible distributed store
  to Amazon Aurora PostgreSQL, aiming to cut operational toil, lower costs, and
  gain compatibility while shielding application teams from heavy lifting. The
  legacy system demanded in-house upgrades, instance replacements, and paid for
  high-end distributed features most apps didn’t need, and “Postgres-compatible”
  edge cases repeatedly broke assumptions. Aurora’s maturing feature set and price
  profile motivated a platform-driven migration: the central team would automate
  schema/data transfer, validation, and cutover so app teams only redirected
  connections. Using AWS DMS as a building block, they first ran fleetwide
  “pre-flight” checks without app involvement: Schema Conversion Tool reports to
  flag incompatible indexes or hidden columns, sample SQL replayed against Aurora
  to catch query issues, right-sized target clusters based on observed traffic,
  and even provisioned temporary clusters with copied schema/data for app teams to
  functionally test. They built tooling around DMS for schema copy with verification
  (e.g., catching VARCHAR truncation) and data copy combining full load and CDC, plus
  monitoring to catch transient task failures early. Because DMS validation didn’t
  fully support their source, they constructed a two-pronged validation pipeline:
  batch validation by streaming both source and target into a data feed and running
  distributed SQL joins in a data warehouse against a time cutoff, and online
  validation via Flink comparing live source/target streams record by record. By
  decoupling validation from production pressure, they could detect mismatches fast
  and safely. Cutover design sought zero read downtime and minimal write downtime by
  inserting a proxy in front of databases; once app traffic flowed through the
  proxy, the platform team controlled the flip. Automated steps included measuring
  replication lag by inserting a metadata record, running validation, ensuring apps
  weren’t bypassing the proxy, copying streaming/batch connectors, then entering a
  critical section: block writes via permissions, sync sequences, wait for CDC to
  catch up, confirm online validation, retarget the proxy to Aurora, and terminate
  lingering source connections. Sequencing reads stayed live; writes paused only for
  minutes. The entire flow produced estimated token/cost/latency outputs per run.
  Outcomes: over 90% of databases migrated (remaining few are large or need special
  handling), some workloads saw latency drops by removing distributed consensus and
  leveraging Aurora’s in-memory reads, and the team avoided rollbacks entirely,
  with only minor fix-forward events like under-sized clusters or metadata issues.
  Pre-migration dry runs uncovered about ten data corruption bugs (null handling,
  encoding, generated columns, data truncation, dropped columns, CDC ordering) that
  were fixed with AWS DMS engineers before impacting users. Key lessons: invest in
  fleetwide dry runs early; verify DMS outputs with custom tooling; monitor CDC
  tasks; test with proxies to prevent split-brain; and treat schema/data migration,
  validation, and cutover as separate, automated stages. With disciplined planning
  and platform-owned automation, Netflix turned a risky, app-by-app effort into a
  repeatable, low-downtime migration factory.
keywords: database migration, Aurora PostgreSQL, AWS DMS, validation, Netflix
---

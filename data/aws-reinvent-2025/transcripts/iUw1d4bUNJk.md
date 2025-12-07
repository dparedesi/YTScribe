---
video_id: iUw1d4bUNJk
video_url: https://www.youtube.com/watch?v=iUw1d4bUNJk
is_generated: False
is_translatable: True
summary: This session introduces Valy, an open-source, BSD-licensed data store for high-performance key-value workloads, presented as a drop-in replacement for Redis 7.2 and offered in Amazon ElastiCache. The presentation highlights Valy's rapid development (two major releases in 1.5 years) and its multi-vendor governance model, with contributions from over 50 organizations. Key innovations include a multi-threaded I/O architecture in Valy 8.0, which significantly improves throughput by offloading I/O operations from the main thread, leading to up to 230% performance gains for throughput-bound workloads and enabling more efficient resource utilization, particularly for spiky caching demands. This efficiency also underpins ElastiCache Serverless, offering 100% utilized service with pay-per-request pricing and 33% cost reduction. Reliability improvements include faster failovers in Valy 8.1, dual-channel replication in 8.0, and future forward replication compatibility. Memory efficiency is enhanced through a redesigned hash table, reducing overhead by up to 55 bytes per key-value pair, and the introduction of probabilistic data structures like Bloom filters for use cases like malicious IP detection, achieving 98% memory savings with minimal performance impact.
keywords: Valy, Amazon ElastiCache, multi-threaded IO, Bloom filters, memory efficiency
---

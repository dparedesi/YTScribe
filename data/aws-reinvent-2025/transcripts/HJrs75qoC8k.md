---
video_id: HJrs75qoC8k
video_url: https://www.youtube.com/watch?v=HJrs75qoC8k
is_generated: False
is_translatable: True
summary: "This session, \"Architecture lessons: Three failures and how to prevent them (DEV341),\" presented by Bruno Marangoni from DXC Technology, dissects three real-world AWS architecture failures from Latin American customers and potential prevention strategies. The first case involves a Brazilian e-commerce company plagued by manual scaling and high latency due to poor Availability Zone (AZ) distribution and lack of caching; the solution involved implementing Auto Scaling groups, balancing instances across AZs, consolidation of load balancers, and adding caching layers (for images and DB), improving latency by ~80ms. The second case describes a large bank where a lack of communication between platform and security teams led to an accidental, irreversible EKS cluster upgrade that took down a critical application for 6 hours (costing ~$1.2 million BRL), highlighting that \"architecture fails when the process fails.\" The third case focuses on a company with lack of financial governance in their migration journey, running non-production workloads on production-grade instances without scheduling, where implementing right-sizing and shutdown policies saved ~720k BRL annually."
keywords: AWS Architecture, Failures, Resilience, Operational Excellence, EKS, Cost Optimization, Auto Scaling, Caching, E-commerce, Governance, Latin America
---

---
video_id: 0sg7KtCuhh0
video_url: https://www.youtube.com/watch?v=0sg7KtCuhh0
is_generated: False
is_translatable: True
summary: "In this technical session, AWS experts Matt Lewis, Jamie, and Melin Kulkarni present a deep dive into the architectural evolution and latest features of AWS Elastic Load Balancing (ELB). Matt Lewis initiates the discussion by contrasting the legacy \"Classic Load Balancer\"—which relied on DNS-based scaling using standard EC2 instances—with the modern generation built on the **AWS Nitro System** and **Hyperplane**. He explains how the Nitro system offloads virtualization and security functions to dedicated hardware cards, enabling massive bandwidth (up to 100 Gbps per instance) and mandatory encryption (VPC Encryption Controls). Crucially, he details how Hyperplane, Amazon's internal distributed state management system, solves the \"DNS propagation\" issues of the past by allowing Network Load Balancers (NLB) and Gateway Load Balancers (GWLB) to present a single, static IP address per Availability Zone regardless of the underlying fleet size.

Jamie then explores practical architectures for the three main load balancer types. The **Application Load Balancer (ALB)** is showcased as the Layer 7 solution for HTTP/HTTPS traffic, featuring **Automatic Target Weighting (ATW)** \"Anomaly Detection\" which automatically stops routing new requests to targets exhibiting 5xx errors or TCP failures. He also highlights ALB's integration with AWS WAF for security and Amazon Cognito for identity offloading. For Layer 4 needs, the **Network Load Balancer (NLB)** is praised for its ability to handle millions of requests per second with ultra-low latency, making it ideal for gaming and financial trading. A key feature discussed is **AWS PrivateLink**, which leverages NLB to provide private, unidirectional connectivity between VPCs or accounts, completely bypassing the public internet. The **Gateway Load Balancer (GWLB)** is introduced as the standard for deploying fleet-based third-party firewalls, utilizing **Geneve encapsulation** to transparently insert security appliances into the traffic flow (\"bump-in-the-wire\") while preserving original source and destination IPs.

Melin Kulkarni concludes the session by unveiling four critical new capabilities. He details **NLB QUIC Pass-through**, which enables support for the modern QUIC protocol (UDP 443). This feature allows for 1-RTT handshakes—significantly faster than the 3-way TCP handshake—and supports connection migration (roaming), ensuring mobile users stay connected as they switch networks. He also announces **NLB Weighted Target Groups**, bringing advanced traffic shifting strategies like blue/green and canary deployments to Layer 4. On the ALB front, the new **Target Optimizer** is designed specifically for AI/ML inference workloads; using an on-target agent, it enforces strict concurrency limits (e.g., one request per target) to prevent resource contention and maximize GPU efficiency. Last, **ALB URL and Host Header Rewrite** offers powerful regex-based transformation capabilities, allowing load balancers to modify request paths (e.g., injecting language codes) or host headers before they reach backend servers."
keywords:
  - AWS Elastic Load Balancing
  - Hyperplane
  - AWS Nitro
  - QUIC Pass-through
  - Target Optimizer
---

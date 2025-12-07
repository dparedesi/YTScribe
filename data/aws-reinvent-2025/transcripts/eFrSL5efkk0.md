---
video_id: eFrSL5efkk0
video_url: https://www.youtube.com/watch?v=eFrSL5efkk0
is_generated: False
is_translatable: True
summary: "This session, \"Under the hood: Architecting Amazon EKS for scale and performance (CNS429),\" features Shweta Joshi and Raghavendra from AWS, along with Nova from Anthropic. They detail the engineering behind EKS's ability to run tens of millions of clusters and support massive AI/ML workloads. AWS introduces \"Ultra Scale\" clusters capable of supporting 100,000 nodes, 8 million pods, and 100,000 node objects in a single cluster—driven by a re-architected etcd that offloads consensus to a multi-AZ transaction journal, uses in-memory storage, and partitions keys. A new \"Provisioned Control Plane\" feature allows customers to proactively select high-performance tiers (XL, 2XL, 4XL) for critical events or massive workloads without migration. Nova from Anthropic explains their \"single logical cluster\" strategy for ultra-scale training (thousands of Trainium/GPU pods), utilizing custom Rust-based scheduling (\"Cartographer\") for topology-aware placement, parallel image pulls for 35GB+ images, and vertically scaled CoreDNS. They emphasize the need for a single pane of glass and efficient multi-tenancy to maximize heavily utilized, expensive compute."
keywords: Amazon EKS, Ultra Scale, Kubernetes, Anthropic, Etcd, Provisioned Control Plane, AI/ML Infrastructure, Custom Scheduler, Trainium, Scalability
---

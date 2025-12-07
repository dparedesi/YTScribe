---
video_id: B13qvwOTZrU
video_url: https://www.youtube.com/watch?v=B13qvwOTZrU
is_generated: False
is_translatable: True
summary: "Brian Lazier from ZScaler presents a blueprint for securing AI-powered Software Development Lifecycles (SDLC) using Zero Trust principles, specifically highlighting a real-world deployment with Cognition's \"Devin\" AI software engineer. He contrasts traditional \"castle and moat\" network architectures, which backhaul traffic and expose large attack surfaces, with today's need for direct, identity-based access. The session details how ZScaler's portfolio enables secure connectivity for AI agents like Devin, which require access to a mix of public resources (like GitHub and StackOverflow) and sensitive private context (such as internal databases, Artifactory, and Jira) to function effectively.

The core of the presentation focuses on ZScaler's **Zero Trust Cloud** offering, which consists of two main components: the **Zero Trust Gateway** and **ZScaler Microsegmentation**. The Zero Trust Gateway describes a regional, managed infrastructure that handles macro-level segmentation. Lazier introduces new capabilities for this gateway, including support for **Ingress** traffic (securing unauthenticated users or partners coming in from the internet/Direct Connect) and **East-West** traffic (inspecting lateral movement between VPCs or subnets), alongside its traditional strength in controlling Egress. These gateways leverage cloud-native constructs like the Gateway Load Balancer and use metadata tags (AWS, Azure, GCP) rather than IP addresses to define policy objects, ensuring security moves at the speed of DevOps.

Complementing the gateway is **ZScaler Microsegmentation**, a host-based agent aimed at minimizing the blast radius for \"crown jewel\" applications. Lazier details recent enhancements, including support for **Amazon EKS** via an eBPF-based daemonset that provides cluster and node-level controls without the heavy overhead of sidecars. This solution operates in user space to program underlying OS firewalls (like Windows Filtering Platform or Linux IP tables) based on identity and process-level intent. A \"Workload Activity View\" is highlighted as a tool to visualize these complex microflows, helping teams audit traffic before enforcing strict \"block\" policies.

The talk concludes by synthesizing these technologies into a cohesive architecture for the AI-driven enterprise. By securing all traffic paths—north-south ingress/egress and east-west—with identity-based authn/authz (including support for JSON Web Tokens), organizations can safely integrate autonomous AI agents into their workflows. Lazier also teases upcoming features like \"AI Guard\" for prompt injection protection, positioning ZScaler not just as a network security vendor, but as an enabler for the secure adoption of next-generation AI tools in production environments."
keywords:
  - Zero Trust
  - ZScaler
  - AI-Powered SDLC
  - Microsegmentation
  - Zero Trust Gateway
  - East-West Traffic
  - Ingress Security
  - eBPF
  - Amazon EKS
  - Cloud Connectivity
---

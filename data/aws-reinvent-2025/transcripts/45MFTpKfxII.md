---
video_id: 45MFTpKfxII
video_url: https://www.youtube.com/watch?v=45MFTpKfxII
title: AWS re:Invent 2025 - Architecting resilient global networks with Amazon Leo (ARC320)
author: AWS Events
published_date: 2025-12-03
length_minutes: 60.17
views: 1013
description: "Amazon Leo's (fka Project Kuiper) Low Earth Orbit (LEO) satellite constellation transforms how organizations architect global connectivity solutions. Explore how Leo's advanced network—featuring antennas, space lasers, ground gateways, and intelligent routing—integrates with AWS services for robust, low-latency solutions. Learn architectural patterns for enhancing application resilience, implementing secure remote data transfer, and optimizing edge computing performance. Discover real-world solu..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
summary: >-
  Nick from Amazon Leo (formerly Project Kuiper) and AWS network engineer John
  describe how Leo’s low Earth orbit (LEO) satellite constellation pairs with AWS
  to deliver business-grade, low-latency connectivity and resilient architectures
  anywhere on the planet. Leo plans to launch 3,200+ satellites across three
  shells (590–630 km), with 153 already in orbit and launches every six weeks
  ramping up in 2026 via New Glenn, Ariane 6, and Vulcan rockets. Service, expected
  in 2026, will roll out first at higher latitudes; predictable orbits and on-board
  propulsion enable precomputed handovers, debris avoidance, and controlled
  deorbit. Satellites link via four-direction space lasers to extend reach over
  oceans/air and reroute around gateway outages, while a global ground network
  feeds points of presence that can hand traffic to the Internet, AWS backbone, or
  private interconnects. Outdoor-rated phased-array terminals emphasize affordability
  and performance: “Pro” (laptop-sized, 400 Mbps down), “Nano” (7x7 inches, 100 Mbps
  for backpack/IoT/SCADA), and “Ultra” (~40 lbs, 1 Gbps for camps/data-center
  backup), each needing only sky view and single Ethernet to a power injector. LEO
  delivers fiber-like latency (<50 ms) versus GEO’s 250–750 ms, with smaller beams,
  less free-space loss, and flexible coverage, but requires cloud-scale control
  planes for frequent handoffs. AWS complements Leo with a 200+ PoP global network
  (38 Regions, 145 Direct Connect sites, 9M+ km of fiber) using MACsec encryption,
  RPKI, traffic engineering, and Shield DDoS protection, keeping inter-region
  traffic on AWS and near major IXPs and services such as CloudFront and Global
  Accelerator. Enterprise preview integrates with IAM/SSO, temporary delegation for
  CloudWatch/EventBridge, and VPC-like IP planning for antennas; installers mount a
  terminal (pole/roof), connect Ethernet, and can view metrics/events in both Leo
  and AWS accounts. Architecture patterns span simple Internet access for remote
  rigs or schools, day-one site/tower/warehouse connectivity, SD-WAN backup and
  disaster response kits, and private paths into VPCs/PNIs. More advanced scenarios
  include IT/OT separation with Cloud WAN and Leo as resilient SCADA backup, 2G/3G
  control planes virtualized on AWS, adding a tertiary path to Direct Connect
  architectures, and edge-to-cloud analytics for utilities, manufacturing, mining,
  energy, and agriculture—e.g., Purdue-modeled demos feeding SageMaker/S3 via
  Transit Gateway so third parties can analyze HMI data without touching control
  networks. With gigabit-class links, customers can relocate local data centers or
  outposts, free up factory floor space, and stream sensor data (audio, video, IR)
  for ML-driven predictive maintenance instead of relying solely on human experts
  in remote sites. Mobility use cases (JetBlue inflight, maritime, mining trucks)
  benefit from lasers and private networking to keep traffic off the public
  Internet. The takeaway: Leo plus AWS offers cloud-grade performance, security,
  observability, and manageability for both backup and primary links in places
  fiber cannot reach today, with an enterprise preview and Venetian booth available for
  hands-on guidance.
keywords: Amazon Leo, low Earth orbit, satellite connectivity, AWS networking, resilient architecture
---

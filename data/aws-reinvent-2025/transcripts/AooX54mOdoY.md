---
video_id: AooX54mOdoY
video_url: https://www.youtube.com/watch?v=AooX54mOdoY
title: AWS re:Invent 2025 - Build AI Agents with Island: Customer Story Featuring Amazon (AIM125)
author: AWS Events
published_date: 2025-12-02
length_minutes: 14.08
views: 3459
description: "Discover how Amazon is building production-ready AI agents with Island and Amazon Bedrock—solving the security, governance, and deployment challenges that generally stop enterprises from going live. Join this lightning talk with Adam Hoyos-Marré, Sr. PMT at Amazon, and Island to see real use cases, real results. This presentation is brought to you by Island, an AWS Partner.  Learn more: AWS re:Invent: https://go.aws/reinforce. More AWS events: https://go.aws/3kss9CP   Subscribe: More AWS videos:..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
summary: >-
  This lightning talk from Island introduces the enterprise browser as a new
  security and governance layer for AI agents and showcases how Amazon.com used
  it to operationalize agentic workflows while keeping data protected. The
  presenter explains that Island’s enterprise browser moves decryption and data
  access into a controlled workspace, giving enterprises delivery controls, data
  protection, identity governance, and zero-trust network access without relying
  on intrusive SSL interception. With customers across banking, travel, healthcare,
  BPOs, and highly regulated industries, Island argues that the browser is the
  last mile where sensitive data is exposed and therefore the right place to
  enforce policy as AI agents begin performing actions. Traditional consumer
  agents use stored credentials and ignore enterprise role context, potentially
  exposing HR or financial records; Island instead injects credentials
  contextually inside the browser, prevents visual and network leakage, and
  records auditable click-by-click sessions. The company positions its product as
  a trust layer for enterprise AI agents that spans authentication (SSO/MFA),
  access grants, secure storage, and audit trails, while enabling no-code
  recording of repeatable workflows that become agent “skills.” Builders can
  record multi-step tasks in the browser, include human-in-the-loop checkpoints
  for approvals, and publish them with guardrails such as forbidden buttons and
  conditional data exposure. Agents run locally or in remote isolated browsers,
  integrating with Amazon Bedrock for model choice and scale. The talk outlines
  the architecture: a policy-driven trusted browser, tooling for builders to
  capture sequences, a runtime that secures credentials and enforces least
  privilege, and observability that captures screenshots, mouse clicks, and tool
  outputs. Three enterprise use cases highlight the approach: a purchase order
  workflow, marketing tag creation, and social media publishing. In the Amazon.com
  purchase order example, the company previously spent 30 minutes per user per day
  reconciling POs; with Island’s recorded workflow and human review gates, 1,000
  users now save roughly 80 cumulative hours weekly. The agent checks permissions,
  validates context, surfaces code or form changes to the operator, and executes
  rollbacks if instructed, cutting average incident resolution to minutes. Tag
  management and social publishing similarly run in the browser with auditable
  trails and credential injection so no secrets ever leave the trusted session.
  Island stresses that unlike consumer agents that treat users as anonymous
  identities, the enterprise browser enforces role context, tool allowlists,
  safe prompting, and consistent governance even across best-of-breed models
  accessed via Bedrock. Builders can run agents locally for performance or in
  remote isolated browsers for regulated workloads without changing recorded
  flows. The presenter closes by inviting attendees to see live demos and
  emphasizing that as agentic AI proliferates, securing the action plane—the
  browser where data is decrypted and actions occur with full audit trails and
  policy enforcement—is
  critical to keep automation productive, compliant, and trustworthy.
keywords: enterprise browser, AI agents, security governance, credential injection, Amazon case study
---

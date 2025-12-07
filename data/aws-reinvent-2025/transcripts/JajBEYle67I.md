---
video_id: JajBEYle67I
video_url: https://www.youtube.com/watch?v=JajBEYle67I
is_generated: False
is_translatable: True
summary: >-
  This session introduces the AWS DevOps Agent (public preview) through a playful
  “day in the life” of senior principal engineer David Yanacek and then dives into
  how the agent accelerates incident response and prevention by acting as an
  autonomous teammate embedded in chat, tickets, and telemetry. Product manager
  Bill frames the agent’s two core jobs: resolve incidents faster by analyzing
  metrics, logs, traces, and deployments to propose root causes and mitigation
  steps; and prevent future incidents by periodically scanning past events,
  architecture, and best practices to suggest posture improvements. Designed as a
  “frontier agent,” it can respond to support tickets, alarms, and pages, write
  findings back to ServiceNow or Slack, collaborate with humans and other agents,
  and page AWS Support engineers with one click when human expertise is needed.
  Telemetry expertise comes via built-in integrations with CloudWatch plus launch
  partners Dynatrace, Datadog, New Relic, and Splunk, and a BYO MCP server path for
  open-source stacks like Grafana/Prometheus/Loki or any custom telemetry. The
  agent not only hunts signals but recommends observability improvements (missing
  metrics, flapping alarms). Pipeline awareness stems from GitHub/GitLab
  integrations so it can correlate code and infrastructure changes, suggest tests,
  and strengthen CI/CD to shift left on quality. To “know your apps,” the agent
  auto-builds an application topology/knowledge graph across accounts by
  discovering resources, service maps, log groups, metrics, alarms, and deployments,
  mapping relationships and comparing them to AWS well-architected patterns and
  customer steering files or runbooks. Customers can also attach existing runbooks
  (e.g., Confluence via Atlassian’s MCP server) and custom MCP tools; the agent uses
  these to accelerate investigations or tailor behavior. Prevention scans surface
  governance, infrastructure, and observability recommendations, e.g., auto-scaling
  misconfigs, missing health checks, DynamoDB policy errors, or flaky pipelines, with
  code snippets and change guidance. Internally, AWS and Amazon teams used the
  agent on 1,000+ incidents, achieving an 86% accurate RCA rate; even incorrect
  RCAs save time by pruning dead-end investigations. Early external betas include
  Commonwealth Bank of Australia, where the agent reconstructed in 15 minutes a
  network incident their engineers took 5 hours to diagnose, and joint Dynatrace
  deployments at Western Governors University, United Airlines, and Clariant where
  “Davis AI” and DevOps Agent collaborated in production within a day. David’s live
  demos show ChatOps-driven investigations, custom MCP log servers secured via Agent
  Core Gateway, and how users can steer investigations, ask impact questions
  (e.g., affected robots in a fleet), or focus on the latest event. The agent
  produces structured change plans with pre/post validations and rollback steps,
  and when memory is enabled, investigation tokens and latency drop by reusing
  cached context. Public preview is free with limits (20 agents per account, 20
  investigation hours/month, 15 prevention hours/month); production action
  execution is on the roadmap. Bill closes by urging attendees to try the console
  setup, throw alarms and questions at the agent, and share feedback as AWS refines
  this autonomous teammate for on-call engineers.
keywords: AWS DevOps Agent, incident response, MCP integration, observability, prevention
---

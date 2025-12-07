---
video_id: 0ZGRSORoP1s
video_url: https://www.youtube.com/watch?v=0ZGRSORoP1s
is_generated: False
is_translatable: True
summary: "This session introduces \"Hawkeye,\" an Agentic AI Site Reliability Engineer (SRE) developed by New Bird, designed to automate the root cause analysis and resolution of production incidents. The presenter addresses the common challenge faced by operations teams: the overwhelming volume of alerts and the manual, stressful labor required to sift through dashboards during an outage. Hawkeye aims to alleviate this burden by connecting directly to a wide array of telemetry sources—including DataDog, Splunk, Grafana, Prometheus, and AWS CloudWatch—as well as configuration interfaces like the AWS Console and Kubernetes infrastructure. By doing so, it serves as a \"cross-platform\" agent that bridges the silos often created by vendor-specific AI tools.

The core of the presentation demonstrates how Hawkeye moves beyond simple alert summarization to perform deep, autonomous investigations. Using a \"Chain of Thought\" reasoning process, the agent asks and answers a series of diagnostic questions, analyzing traces, logs, metrics, and security configurations to pinpoint the root cause of an issue. This analysis is delivered not just via a UI, but \"headlessly\" through platforms where engineers already work, such as Slack, Microsoft Teams, or ServiceNow. A key feature highlighted is Hawkeye's integration with modern coding assistants like Claude Code, Cursor, and GitHub Copilot via the Model Context Protocol (MCP). This allows SREs to interact with the agent directly within their IDE/terminal, querying past incident data or even generating and executing remediation scripts (e.g., creating a missing AWS IAM role) without switching contexts.

Real-world use cases are cited to illustrate the agent's versatility: an insurance company using it to manage incidents across a complex hybrid on-prem/AWS environment, a logistics firm monitoring critical nightly data pipelines, and an Australian bank automating compliance reporting for backup failures. The speaker emphasizes flexibility in deployment, noting that while a SaaS version is available for quick onboarding via the AWS Marketplace (with a two-week free trial), security-conscious enterprises can deploy Hawkeye directly within their own VPC to maintain strict control over their data and AI models.

Ultimately, the session positions the \"AI SRE\" not as a replacement for human engineers, but as a force multiplier that removes the drudgery of \"fighting fires.\" By automating the collection and analysis of evidence, Hawkeye allows human SREs to focus on preventative measures and system hardening. The presenter concludes by encouraging attendees to try the self-service onboarding, framing the tool as a vendor-neutral \"Swiss Army knife\" capable of orchestrating incident response across a fragmented landscape of observability tools."
keywords:
  - Agentic AI
  - Site Reliability Engineering (SRE)
  - Root Cause Analysis
  - Hawkeye (New Bird)
  - Model Context Protocol (MCP)
  - Observability
  - Incident Response
  - Chatops
  - Automated Remediation
  - CloudWatch
---

---
video_id: GYaDjPwLDGo
video_url: https://www.youtube.com/watch?v=GYaDjPwLDGo
is_generated: False
is_translatable: True
summary: >-
  This session, led by Hannah Marlow and Charlina Cashava from the AWS Generative AI
  Innovation Center with a deep-dive case study from Cosign’s Alistair Pullen, explores
  how to fine-tune large language models and orchestrate multi-agent systems for real-world
  applications. The speakers frame the Innovation Center’s mission as helping customers move
  beyond proofs of concept toward production-grade, customized models that balance accuracy,
  latency, and cost while embedding brand alignment and domain relevance. They define an
  agent as an autonomous, LLM-powered system able to reason, plan, use tools, and leverage
  memory, and trace how advances in model reasoning, data integrations, and protocols such
  as MCP and A2A have made agentic architectures practical. A maturity model maps the
  industry’s progression from rule-based automation through single assistants to goal-driven
  multi-agent orchestration, with most organizations currently climbing that third rung. Multi-
  agent adoption is driven by model choice, right-sizing, and modularity that resembles a
  microservices shift, typically implemented with a competent orchestrator delegating to
  specialized worker agents. Benefits include flexibility and redundancy, but challenges
  span latency, cost, task decomposition, context management, and error propagation akin to
  a “telephone game.” Charlina details four customization techniques to close performance
  gaps—model distillation for cost and latency, supervised fine-tuning for domain patterns,
  preference optimization for style and formatting, and reinforcement fine-tuning for
  sequential decisions and tool use—while cautioning to exhaust prompt engineering and RAG
  before training. The Cosign case study then grounds these ideas in a production coding-
  assistant platform built with Lambda, Step Functions, AppSync, DynamoDB, and Neptune,
  emphasizing safety, tool whitelisting, distinct agent personalities, and a conversation
  mediator to coordinate multiple avatars. Cosign uses a knowledge graph to capture
  memorable interactions, rule- and learning-based filters to decide what to remember, and a
  mediator scoring replies for relevance and turn-taking. They show how Amazon Bedrock
  Agent Core could replace much of their bespoke runtime, tooling gateway, memory, and
  observability stack. On the training side, Cosign starts with frontier models, post-trains
  them on software-engineering scaffolds, then distills trajectories into smaller models,
  training orchestrators to delegate via tool calls and workers to traverse code, run tools,
  and propose diffs, with RL refining both. A multi-agent setup delivered a 31% uplift on
  the Swelancer coding benchmark with the same GPU footprint, 3x lower latency versus
  generic frameworks, 60% GPU footprint reduction in constrained deployments, fewer code
  errors, and more stable RL, enabling regulated industries that demand isolated VPC
  deployments and full auditability. Lessons learned include treating orchestrator and worker
  training as distinct disciplines, experimenting with end-to-end RL of full systems,
  outperforming larger monoliths with fine-tuned 70B models, relying heavily on
  distillation, and valuing real-world execution data. The speakers close by urging attendees
  to survey session feedback like they tune agents—collect signals, iterate, and improve.
keywords: multi-agent systems, model customization, distillation, reinforcement learning, orchestration
---

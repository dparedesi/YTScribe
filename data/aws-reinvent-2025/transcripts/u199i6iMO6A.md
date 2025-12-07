---
video_id: u199i6iMO6A
video_url: https://www.youtube.com/watch?v=u199i6iMO6A
is_generated: False
is_translatable: True
summary: >-
  Sam Patzer and Christina from AWS demonstrate how to accelerate game design
  reviews by pairing Bedrock Agent Core with the open-source Strands framework to
  build a multi-agent “game analyst” that evaluates proposals for lore fidelity,
  gameplay quality, QA risk, and business strategy. They start by defining the
  modern game analyst as an interpreter and storyteller who aligns player goals,
  business goals, and data across domains such as narrative, QA, design, and
  strategy. Current challenges include slow review cycles due to missing
  information, fragmented data silos and ownership, ramp time for new analysts,
  and subjective biases that skew decisions. Their solution decomposes the role
  into four specialized agents (lore, quality assurance, gameplay, and strategy)
  backed by domain-specific knowledge bases, plus an orchestrator “game analyst”
  that delegates tasks, synthesizes findings, and presents recommendations. Using
  Strands, developers define agents, prompts, and tool access in Python while
  Bedrock Agent Core supplies secure, serverless runtimes, memory management,
  observability, and identity-aware gateways to external tools via MCP. Models
  such as Claude 3.5 and Amazon Nova can be swapped; the demo uses Sonnet 4.5.
  Patzer shows how to create a project portal where designers submit design docs,
  pick which agents to consult, and enable memory. The orchestrator uses Bedrock
  knowledge bases to retrieve references (e.g., New World wiki for lore) and
  applies conditional analysis: if one competency approves but another rejects, it
  explains trade-offs and proposes fixes. The system outputs a unified summary,
  individual competency deep dives, and estimated token costs and latency. Users
  can then iterate via chat, asking for alternative races, quest ideas, or lore-
  friendly tweaks; the orchestrator conditionally reuses only relevant agents,
  showing reduced tokens and faster responses when memories avoid repeat
  retrievals. Memory is layered: project-level semantic fact memories cache data
  and findings to cut knowledge-base calls, while user-level session memory
  preserves preferences (e.g., bullet formatting) and conversation continuity.
  Implementing memory requires adding storage/retrieval hooks and tools in Strands
  and defining when to hydrate memories at run time. The team stresses secure,
  governed patterns: multi-account deployment mapped to org structure, domain
  units and auth policies in SageMaker Unified Studio, RACI operating models to
  assign ownership, and data contracts that define schemas, validation, and
  governance. Observability via Bedrock Agent Core traces and metrics help debug
  and monitor performance. Key lessons: decompose complex reviews into specialized
  agents with clear tool lists; use an orchestrator to handle delegation, context,
  and synthesis; start with simple prompt/RAG baselines before fine-tuning; add
  memory to cut costs and latency; and bake in access controls and taxonomy for
  consistent outputs. They report internal pilots achieving large latency
  reductions (due to fewer knowledge-base calls), lower token counts, and richer,
  bias-reduced feedback that lets designers iterate faster, transforming
  multiweek back-and-forth into minutes-long, data-backed review cycles.
keywords: multi-agent, Bedrock Agent Core, Strands, game design review, memory optimization
---

---
video_id: 0sfKGUZ6kcg
video_url: https://www.youtube.com/watch?v=0sfKGUZ6kcg
title: AWS re:Invent 2025 - Build a well-architected foundation for scaling generative AI and agentic apps
author: AWS Events
published_date: 2025-12-02
length_minutes: 57.3
views: 1161
description: "You've seen the potential of agentic AI through proof-of-concepts, and you're ready to build a foundation that can support all AI applications across your organization. Enter the complexities: model access and management, tool discovery, memory and state handling, observability, plus deployment and operations at scale! In this session we'll demonstrate how to build a well-architected foundation that seamlessly integrates model access, orchestration workflows, agents, tools and domain-specific da..."
keywords: AWS reInvent 2025
is_generated: False
is_translatable: True
summary: "In this deep-dive technical session, AWS specialists Chaitra and Aamna, along with Dave Senior, Head of Data and AI at Sage, present a rigorous framework for elevating Generative AI and agentic applications from experimental prototypes to robust, production-ready systems. They address the inherent complexities of scaling agents, such as managing long-term state, ensuring low-latency performance in multi-step reasoning, and securing sensitive data access. The proposed solution is a \"Well-Architected Foundation\" that stratifies the architecture into distinct layers: a centralized \"Model and Agent Hub\" for governance, a secure \"Execution Runtime\" (leveraging Amazon Bedrock AgentCore), and a \"Data Layer\" responsible for ingestion pipelines and vector store management. A critical architectural pattern introduced is the \"LLM Gateway\"—illustrated using the open-source LiteLLM proxy hosted on Amazon Elastic Kubernetes Service (EKS)—which standardizes model access via a unified API, enabling granular cost attribution, rate limiting per team, and the uniform application of guardrails across all enterprise applications.

Aamna brings these concepts to life with a demonstration of the \"Agentic AI Foundation Accelerator,\" an open-source reference architecture available on GitHub. She walks through a customer service chat application built with LangGraph, displaying how it transitions from local testing to a cloud-hosted deployment on Amazon Bedrock AgentCore Runtime. The agent is equipped with three distinct tools: a RAG retrieval tool using Amazon Bedrock Knowledge Bases for documentation, a \"create support ticket\" tool leveraging 3rd party APIs, and a Tavily-powered web search tool for real-time information. The demo places heavy emphasis on \"Observability for Intelligence,\" utilizing Langfuse to capture detailed traces of agent reasoning and tool usage. Aamna explains the critical distinction between offline evaluation—using \"Golden Datasets\" and \"LLM as a Judge\" continuously in the CI/CD pipeline—and online evaluation, where live user feedback and sampled traces are monitored for drift, bias, and accuracy.

Rounding out the session, Dave Senior shares Sage’s practical journey in building an \"Agentic Mesh\" to serve their 6 million business customers across accounting, HR, and payroll domains. He describes a sophisticated federated architecture where a \"Main Agent\" acts as the entry point, intelligently routing complex tasks to \"Planning Agents\" and specific execution tasks to \"Specialized Agents\" across different product boundaries. For instance, he illustrates a cross-domain workflow where an accounting agent triggers a user creation event in the HR platform, necessitating strict entitlement checks and identity propagation via Sage ID. Sage is currently modernizing this infrastructure by integrating Amazon Bedrock AgentCore to standardize their \"AgentOps\" lifecycle, moving from disparate AI implementations to a unified, scalable mesh that supports seamless interaction across their entire product suite."
keywords:
  - Agentic AI
  - AgentOps
  - LLM Gateway
  - Amazon Bedrock AgentCore
  - Agentic Mesh
---

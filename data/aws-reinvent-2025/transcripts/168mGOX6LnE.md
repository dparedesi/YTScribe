---
video_id: 168mGOX6LnE
video_url: https://www.youtube.com/watch?v=168mGOX6LnE
is_generated: False
is_translatable: True
summary: "In this interactive \"code talk,\" AWS Developer Advocate Gunnar Grosch and Principal Product Manager Shridhar Pandey demonstrate the power of AI-assisted development by building a complete serverless image generator application using the **Kiro CLI** (formerly Amazon Q Developer CLI) and the **Model Context Protocol (MCP)**. The session highlights how the Kiro CLI, augmented by the Open Source **AWS Serverless MCP Server**, essentially becomes a \"serverless expert,\" capable of executing complex infrastructure tasks like `sam init`, `sam build`, and `sam deploy` directly from natural language prompts. Shridhar explains that the Serverless MCP server provides the AI with deep knowledge of best practices, deployment capabilities, and access to architectural patterns from Serverless Land, enabling it to guide the user through the entire lifecycle—from initial scaffolding to Day 2 operations.

Gunnar drives the live demo, starting with an empty directory and progressively building a backend architecture featuring **AWS Lambda** (Node.js), **Amazon API Gateway** (HTTP API), and **Amazon S3** for image storage. A key feature he introduces is the use of **\"Steering Files\"**, a configuration mechanism that allows developers to define persistent, project-specific guardrails and architectural standards (e.g., \"always use us-west-2,\" \"enforce least-privilege IAM,\" \"never commit secrets,\" \"follow JSDoc standards\"). This ensures that the AI's output remains consistent and adheres to organizational compliance and style requirements, preventing the \"drift\" often seen with generic AI assistants. The pair then integrates **Amazon Bedrock** (specifically the Titan Image Generator v2 model) to handle the core image generation logic, demonstrating how Kiro adjusts permissions and environment variables automatically.

The demonstration goes beyond simple code generation to cover the full developer experience. Shridhar showcases a \"Console to IDE\" feature that allows developers to seamlessly transition from the AWS Lambda console to VS Code with a single click, automatically syncing code and infrastructure settings. Gunnar then emphasizes that functionality is only part of the equation; production readiness requires robust observability. He directs Kiro to instrument the application with **AWS Lambda Powertools** for structured logging, custom metrics, and tracing, and to enable **Amazon CloudWatch Application Signals** for out-of-the-box APM insights using OpenTelemetry. The session concludes with the generation of a **React** frontend using Vite, which successfully interacts with the backend. Throughout the talk, the speakers illustrate a \"human-in-the-loop\" workflow where the developer acts as the architect, defining high-level intent and verifying results, while the AI handles the implementation details, enabling the creation of a well-architected application without writing a single line of manual code."
keywords:
  - Kiro CLI
  - Model Context Protocol
  - AWS Serverless MCP
  - Steering Files
  - AWS Lambda Powertools
---

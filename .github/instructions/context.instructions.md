---
description: "Context management guidelines"
applyTo: "**"
---

# Context and Prompt Engineering Guidelines

- Always ensure the AI has enough context to answer accurately but avoid overloading the prompt with unnecessary text. Use retrieval techniques to fetch relevant snippets and inject them into prompts using context variables like `${selection}` or MCP resources.
- Encourage chain‑of‑thought reasoning in complex problem solving by instructing the model to explain its steps before giving a final answer.
- Use prompt chaining and conditional logic by composing multiple prompt files; for example, run `analysis.prompt.md` followed by `implementation.prompt.md`.
- When referencing external resources, include citations or links for traceability.
- For code generation tasks, instruct the model to search for the latest information online before acting, if allowed by the agent’s capabilities.

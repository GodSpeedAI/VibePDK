# Repository‑Wide Copilot Instructions

The purpose of these instructions is to provide repository‑specific guidance to GitHub Copilot and VS Code’s AI chat features. These instructions apply to every file in the repository.

- This repository contains a modular AI assistant and related tooling written primarily in TypeScript with a Node.js runtime. When generating code, follow our established coding guidelines, naming conventions, and architectural patterns described in the instruction files under `.github/instructions`.
- Always prioritize security: never write or modify `.vscode/settings.json` or `.vscode/tasks.json` without explicit user confirmation. Avoid setting `chat.tools.autoApprove` in any configuration, as this disables human confirmation and can lead to remote code execution.
- Use composition over inheritance when designing classes. Favor small, testable functions and modules. Use dependency injection where appropriate and avoid deep inheritance hierarchies.
- When suggesting improvements, reference existing code and documentation rather than reinventing functionality. Use relative import paths and keep modules loosely coupled.
- Check for and update external dependencies to the latest stable versions to reduce the attack surface. Do not add packages with known vulnerabilities.
- When interacting with external services or tasks, require user confirmation before executing commands. Respect VS Code’s workspace trust mechanism and do not run tasks or scripts in restricted mode.
- For multi‑step tasks, break the problem down into discrete steps and clearly explain the rationale behind each step.
- Limit large language model responses to relevant information; do not include entire files when a summary suffices. Encourage token efficiency and performance‑conscious design.
- Always follow best practices for code quality, including writing tests, adhering to style guides, and conducting code reviews.
- Do not introduce technical debt and if you notice any, create a plan to address it.

For more detailed guidelines, see the individual instruction files in `.github/instructions`.

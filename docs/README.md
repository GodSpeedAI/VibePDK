# Modular AI Prompt Management System (Native Copilot + VS Code)

This repository demonstrates a modular, composable prompt management system that leverages **only the native customization mechanisms of GitHub Copilot and VS Code**—no custom YAML DSL is required. By using repository‑level and folder‑level Markdown files, workspace settings, tasks, and simple scripts, we can achieve sophisticated prompt engineering patterns such as modular composition, inheritance‑like behaviour, LoRA‑
style stacking, dynamic prompt injection, conditional loading, A/B testing, and hot‑reloading.

## File Structure

The system is organised into the following directories:

| Path | Purpose |
| --- | --- |
| `.github/copilot-instructions.md` | Repository‑wide instructions that apply to every prompt. VS Code automatically merges these with other instructions. |
| `.github/instructions/` | Modular instruction components, each with front‑matter metadata (`description`, `applyTo`) and MECE‑based categories: `general`, `security`, `performance`, `style`, and `context`. Files are applied based on glob patterns. |
| `.github/prompts/` | Reusable prompt templates (e.g. `create-react-component`, `security-review`, `performance-analysis`) with front‑matter specifying `mode`, `model`, `tools`, and `description`. Prompts can reference instructions or other prompts via relative Markdown links and use context variables like `${fileBasename}`, `${selection}`, etc.. |
| `.github/chatmodes/` | Custom chat modes that define personas or workflows for the Chat view. Each `.chatmode.md` file contains front‑matter (`description`, `tools`, `model`) and a body with instructions. Chat modes can reference instruction files and appear in the Chat view’s mode picker. |
| `.vscode/settings.json` | Workspace settings to enable prompt and instruction files and define where VS Code looks for them. This file also disables unsafe features like `chat.tools.autoApprove` and configures workspace trust. |
| `.vscode/tasks.json` | Tasks to run prompts, measure token usage, chain multiple runs, and perform A/B testing. Tasks invoke shell scripts in the `scripts` directory. |
| `.vscode/mcp.json` | Example configuration for Model Context Protocol (MCP) servers using environment variables for authentication. |
| `scripts/` | Helper scripts (bash) that run prompts and estimate token counts. These scripts are placeholders that can be extended to integrate with the VS Code CLI or Copilot API. |
| `docs/` | Documentation, including this README and a migration guide from YAML‑based systems. |

## Native Capabilities and Modular Architecture

### Instructions and Inheritance

VS Code supports repository‑wide instructions (`.github/copilot-instructions.md`) and multiple task‑specific instruction files (`.instructions.md`). Each instruction file can specify an `applyTo` glob pattern that controls when it is automatically included. For example, `style.instructions.md` applies only to TypeScript/JavaScript files (`**/*.ts,**/*.tsx,**/*.js`). Instructions can reference other instruction files using relative Markdown links. When Copilot runs, all relevant instructions are merged without priority order, so it is important to avoid conflicting guidance.

We organise instruction files into MECE categories:

* **General** – overall guidelines (clarity, maintainability, asking clarifying questions).
* **Security** – sanitisation, avoidance of dangerous settings like `chat.tools.autoApprove`, respect for workspace trust, and secret handling.
* **Performance** – algorithmic efficiency, token reduction, caching, and use of context variables to limit prompt scope.
* **Style** – naming conventions (PascalCase, camelCase) and formatting.
* **Context** – prompt‑engineering patterns such as chain‑of‑thought, prompt chaining, context injection, and retrieval.

Because each instruction is independent, you can **compose them like LoRA adapters**: referencing multiple instruction files in a prompt stacks their guidance. For example, the `create-react-component.prompt.md` file links to `style.instructions.md`, `general.instructions.md`, and `performance.instructions.md`, thereby combining their advice just as LoRA adapters stack low‑rank updates on a base model. If you want a different “mix” (e.g. style + security), you can write a prompt that links only to those instructions. This modular architecture avoids deep inheritance hierarchies and favours composition over inheritance, mirroring best practices in software design.

### Prompt Files and Context Variables

Prompt files store reusable instructions for specific tasks. They support front‑matter metadata (mode, model, tools, description) and a Markdown body where you can blend natural language, code blocks, and links to other prompt or instruction files. Within prompts you can reference variables using `${variableName}` syntax to inject dynamic context: workspace path, file name, current selection, user inputs, etc.. This avoids sending unnecessary context, saving tokens and improving performance. For example, the `security-review.prompt.md` instructs the AI to use `${fileBasename}` or `${selection}` to scope its analysis.

Prompt files can link to other prompts, enabling **prompt chaining**. A larger workflow might run an analysis prompt first, then an implementation prompt that references the analysis results. Loops and conditionals are handled outside of YAML by using tasks or scripts (see below).

### Chat Modes

Custom chat modes allow you to create specialised personas or workflows for the Chat view. A chat mode is defined in a `.chatmode.md` file and includes front‑matter fields such as `description`, `tools`, and `model`. The body of the file contains instructions that modify how the AI behaves when that mode is active. Chat modes complement prompts: whereas a prompt defines a specific task, a chat mode defines the overall style and goals of a conversation.

This repository includes **eight** example chat modes located in `.github/chatmodes/`:

* **Product Manager Mode** – transforms raw ideas or business goals into structured, actionable product plans. It creates user personas, detailed user stories and prioritised feature backlogs, emphasising problem analysis, solution validation and impact assessment.
* **UX/UI Designer Mode** – designs user experiences and visual interfaces for applications. It translates feature stories into comprehensive design systems, detailed user flows and implementation‑ready specifications while championing simplicity, accessibility and aesthetic harmony.
* **System Architect Mode** – converts product requirements into comprehensive technical architecture blueprints. It defines system components, selects technology stacks, specifies API contracts and data models, and produces architecture documentation for downstream engineering teams.
* **Senior Backend Engineer Mode** – implements robust, scalable server‑side systems from technical specifications. It builds APIs, business logic and data persistence layers, manages database migrations and ensures production‑quality code following security and performance best practices.
* **Senior Frontend Engineer Mode** – translates technical specifications, API contracts and design systems into production‑ready user interfaces. It delivers modular, performant and accessible frontend implementations that adhere to established architectural and design patterns.
* **QA/Test Automation Engineer Mode** – writes context‑appropriate test suites and strategies for backend, frontend or end‑to‑end scenarios. It validates functionality against technical specifications, identifies edge cases, integrates performance testing and operates in parallel with development.
* **DevOps Deployment Engineer Mode** – orchestrates the complete software delivery lifecycle. It provisions infrastructure with IaC, implements secure CI/CD pipelines, manages environments from local to production, and integrates security, monitoring and scalability throughout the deployment process.
* **Security Analyst Mode** – performs comprehensive security analysis and vulnerability assessment for applications and infrastructure. It offers quick security scans or full audits, covering application security, data protection, infrastructure configuration, API and integration security, dependency scanning and threat modeling.

To enable discovery of custom chat modes, our `settings.json` includes a `chat.modeFilesLocations` entry pointing to `.github/chatmodes`. You can add more chat modes by creating additional `.chatmode.md` files in this folder and defining the desired tools, model, and instructions.

### Workspace Settings and Discoverability

In `settings.json` we enable prompt and instruction files (`chat.promptFiles: true`) and tell VS Code where to find them via the `chat.promptFilesLocations` and `chat.instructionsFilesLocations` dictionaries. We explicitly disable `chat.tools.autoApprove` to prevent prompt injections from bypassing confirmation dialogs. We also set `security.workspace.trust.untrustedFiles` so tasks require explicit trust before running. These settings allow dynamic discovery of new prompts: you can drop additional `.prompt.md` files into `.github/prompts` or other configured folders, and Copilot will pick them up without any extra tooling.

### Tasks for Automation, A/B Testing, and Hot‑Reloading

VS Code tasks provide an imperative layer on top of our declarative prompt definitions. The included `tasks.json` defines shell tasks to run prompts, measure token usage, and chain multiple runs. For example:

* **Run tasks** (`Run: Create React Component`, `Run: Security Review`, etc.) invoke the `run_prompt.sh` script with the appropriate prompt file.
* **Measure tasks** estimate token usage with `measure_tokens.sh`, helping you monitor prompt length and optimise accordingly.
* **A/B testing** is supported via a compound task (`AB Test: Create React Component`) that depends on running the same prompt with different configurations (e.g. style vs. performance). You can create Git branches or workspace settings variants to test different instruction mixes.

Because tasks are defined in JSON (not YAML), they benefit from VS Code’s validation and auto‑completion. They also hot‑reload—saving `tasks.json` or any script automatically updates the tasks without restarting VS Code. Remember that tasks will not run in untrusted workspaces; users must trust the folder first.

### MCP Integration

The optional `.vscode/mcp.json` file shows how to configure Model Context Protocol servers. The example defines a `github-mcp` server with an HTTP endpoint and reads the authentication token from an environment variable, avoiding secrets in source control. Additional servers can be added under `servers` to integrate custom tools or models.

### Scripts

The `scripts` directory contains simple Bash scripts used by tasks:

* `run_prompt.sh` takes a prompt file path and an optional configuration argument. It currently echoes the call for demonstration, but it can be extended to run the `github.copilot.chat.runPrompt` command via the VS Code CLI or to call the Copilot API directly.
* `measure_tokens.sh` approximates token usage by counting words and characters. For more accurate counts, integrate a tokenizer (such as `tiktoken`) or the OpenAI API.

## Security and Performance

Security is a first‑class concern. The [security instructions](../.github/instructions/security.instructions.md) emphasise input sanitisation, avoidance of dangerous settings like `chat.tools.autoApprove`, respect for workspace trust boundaries, and the use of environment variables for secrets. Tasks and scripts are never executed automatically in untrusted workspaces, and prompts ask for confirmation before running potentially dangerous code.

Performance is addressed through the [performance instructions](../.github/instructions/performance.instructions.md), which encourage efficient algorithms, context scoping via variables, caching, and token reduction strategies. Measuring token usage with `measure_tokens.sh` helps ensure your prompts remain concise.

## Advanced Usage

**LoRA‑style stacking:** Compose multiple instruction files in a prompt to emulate stacking LoRA adapters. For example, a prompt could link to `security.instructions.md`, `performance.instructions.md`, and `style.instructions.md` to apply all three sets of guidelines simultaneously. Changing the combination yields different behaviours without editing the base prompt, analogous to applying different LoRA weight deltas on a base model.

**Dynamic prompt injection:** Through tasks and the `chat.promptFilesLocations` setting, you can dynamically discover and run prompts. You can also programmatically generate `.prompt.md` files or use symbolic links to compose different sets of prompts at runtime.

**Conditional loading:** Use `applyTo` in instruction files to control when they apply; use task arguments (e.g. `--config=style`) to toggle which instructions are referenced within a prompt or to select different branches. You can also leverage workspace settings (e.g. enabling or disabling certain prompt file locations) for environment‑specific configurations.

**A/B testing:** Create separate Git branches or workspace folders with different instruction mixes or prompt implementations. Use the `AB Test` task to run both variations and compare outputs. Because prompts are regular Markdown files, you can review diffs, run code reviews, and revert changes easily.

**Hot‑reloading:** Changes to instruction files, prompt files, or tasks take effect immediately. There is no YAML compiler or build step; you simply edit the Markdown or JSON files and rerun the prompt.

## Conclusion

By embracing native Copilot and VS Code features, this system eliminates the need for a bespoke YAML DSL while still offering rich prompt engineering capabilities. Instructions and prompts are version‑controlled, modular, and composable. Settings and tasks provide declarative and imperative layers, respectively. Security, performance, and usability are integral to the design, resulting in a practical and maintainable solution for managing AI coding assistants.

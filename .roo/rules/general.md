# VibePDK Coding Guidelines

## Core Development Principles

- **Template-First Thinking**: Distinguish between template repository code (root level) and generated project code (`{{cookiecutter.project_slug}}/`). Changes affecting generated projects must be placed within the template directory structure.
- **Validation-Driven Development**: Implement validation at multiple layers - pre-generation hooks, file structure contracts, and runtime checks. Fail fast with actionable error messages.
- **Polyglot Consistency**: Maintain consistent patterns across Python (uv/strict typing) and Node.js/TypeScript (pnpm/strict mode) codebases.
- **Zero-Hunt File Organization**: Place files in predictable locations following established patterns - obvious things in obvious places.

## File Organization & Naming

- **Naming Convention**: Use kebab-case for files with clear suffixes (`.prompt.md`, `.instructions.md`, `.chatmode.md`, `.test.js`)
- **Directory Contracts**: Enforce required directory structures and validate their presence in tests
- **Template Boundaries**: Keep Cookiecutter-specific files (hooks/, cookiecutter.json) at root; generated project assets in `{{cookiecutter.project_slug}}/`
- **Feature-Oriented Structure**: Organize tools and generators by domain/capability rather than technical implementation

## Code Quality Standards

- **Strict Typing**: Use comprehensive type annotations in Python (>=3.12) and TypeScript strict mode
- **Input Validation**: Validate all inputs with regex patterns and clear failure messages (see pre_gen_project.py patterns)
- **Module Boundaries**: Export clear, minimal interfaces using module.exports (Node.js) or proper imports (Python)
- **Error Handling**: Provide actionable error messages with suggestions for remediation

## Testing Patterns

- **Test Organization**: Structure tests as `unit/`, `integration/`, `fixtures/`, `snapshots/`
- **Naming**: Use `test_<should>_<specific_behavior>` format for test functions
- **Contract Testing**: Validate I/O contracts, file structure requirements, and API boundaries
- **Fixture Management**: Keep minimal, explicit test variations under `tests/fixtures/<area>/`

## Development Workflow

- **Tool Orchestration**: Use `just` as the canonical interface; avoid direct `pnpm`/`nx`/`bash` invocation
- **Validation Pipeline**: Run linters, type checkers, and structure validators before commits
- **Token Awareness**: Consider token budgets and measurement in prompt/content generation
- **Environment Isolation**: Use proper environment management (uv for Python, volta+corepack for Node.js)

## Technical Debt Prevention

- **Keep Hooks Lightweight**: Minimize logic in pre/post generation hooks; prefer post-generation validation
- **Avoid Deep Dependencies**: Prefer built-in modules and established tools over new dependencies
- **Maintain Backwards Compatibility**: Changes to file structure or naming should be additive when possible
- **Document Architectural Decisions**: Use ADR format for significant structural changes

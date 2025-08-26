# Copilot Coding Agent Onboarding Guide

This repository is a Cookiecutter template for an Nx + CALM monorepo. It includes Python tests to validate template hooks and a minimal Node toolchain for prompt/docs tasks inside the generated project skeleton under `{{cookiecutter.project_slug}}/`.

Trust these instructions first. Only search if something here is incomplete or incorrect.

## What this repo is

- Type: Cookiecutter template repository with tests for pre/post generation hooks and a sample generated project layout.
- Primary languages: Python (pytest, cookiecutter), Node/TypeScript (tooling for generated project template).
- Runtimes and tools used in this repo:
  - Python: 3.12 (see `.python-version` and `pyproject.toml`). Use uv only.
  - Package management: uv (Astral). Do NOT use pip directly.
  - Node: validated with Volta-managed Node (v24.x observed locally); generated projects target Node 24.
  - pnpm: used in generated project; with Volta, install/enable Corepack first so pnpm resolves reliably.

## Layout cheat-sheet

- Root:
  - `pyproject.toml`: dev deps for pytest, pytest-cookies, cookiecutter, pyyaml.
  - `hooks/`: `pre_gen_project.py`, `post_gen_project.py` (validated by tests).
  - `tests/`: pytest suite that bakes the template and validates hooks and generated project basics.
  - `cookiecutter.json`: default context values.
  - `README.md`, `docs/`: extensive documentation of prompts, tech stack, etc.
  - `{{cookiecutter.project_slug}}/`: the template files that will be rendered.
    - `.github/` in template: prompts, instructions, workflows.
    - `justfile` and scripts for techstack sync.
    - `package.json`, `pnpm-workspace.yaml`, Nx settings, docs, etc.

## CI and checks

- GitHub Actions (template workflows referenced): markdown lint, prompt lint/plan, node tests (in generated project), env audit.
- Local validation before PR:
  1) Always run tests with uv.
  2) If your change touches template Node files, ensure Node+Corepack+pnpm are available (Volta works well).

## Required environment

- Always use uv for Python commands.
- Python 3.12 is required. A `.venv` will be created by `uv sync`.
- Node is required only for the integration test that installs pnpm deps in the baked project. Ensure `corepack` is available (Volta: `volta install corepack`), or skip that test if focusing on Python-only changes.

Quick checks:
- `uv --version` should succeed.
- `uv python list` should include 3.12.x.
- `node -v` prints a version; `corepack --version` must exist to pass the pnpm integration test.
- With Volta: `volta --version`, `pnpm -v` should work; still run `corepack enable` once per machine.

## Bootstrap and build steps (validated)

Python-only workflow (fast):
1) uv sync dev deps
   - Command: `uv sync --dev`
   - Preconditions: Internet access to resolve packages. Python 3.12.
   - Postconditions: `.venv` created/updated, pytest available.

2) Run tests
   - Command: `uv run pytest -q`
  - Postconditions: Tests pass end-to-end when Corepack is available; otherwise skip the pnpm test (below).

Node/pnpm prerequisites for the integration test (validated):
- The test `tests/test_cookiecutter_generation.py::test_generated_project_installs_and_tests_pass` does:
  - `corepack enable` → `pnpm install` → `pnpm test:node` in the baked project.
- If `corepack` is missing, it fails with `FileNotFoundError: 'corepack'` while others pass.
- Mitigations (Volta-friendly):
  - `volta install corepack@latest` (one-time)
  - `corepack enable`
  - `corepack prepare pnpm@latest --activate`
  - Re-run: `uv run pytest -q`
Verified versions seen locally: Node v22.17.0, pnpm 10.13.1, uv 0.7.x.

Recommendation for reliable runs:
- Always enable Corepack before running the full suite.
- To focus on Python-only: `uv run pytest -q -k 'not test_generated_project_installs_and_tests_pass'`.

Recent validation snapshot:
- After installing/enabling Corepack via Volta, full suite passed: `28 passed`.

## Common tasks

- Bootstrap (Python):
  - `uv sync --dev`
- Test (Python):
  - `uv run pytest -q`
- Re-run a single test file:
  - `uv run pytest tests/test_pre_gen_project.py -q`
  - `uv run pytest tests/test_cookiecutter_generation.py::test_generated_project_installs_and_tests_pass -q`

## Architectural notes

- Hooks:
  - `hooks/pre_gen_project.py` validates project_slug, author_name, python_version (supports 3.10/3.11/3.12), and description length; fails fast with sys.exit(1).
  - `hooks/post_gen_project.py` prints next steps; no side effects.
- Template under `{{cookiecutter.project_slug}}/` includes `.github` with prompts/instructions/workflows, `justfile`, docs, Nx config, and basic scripts.
- Root `package.json` contains tooling scripts for prompt linting and docs, not required for running the Python tests.
- Integration test logging: we use a module-level logger in `tests/test_cookiecutter_generation.py` to emit pnpm stdout/stderr for easier diagnosis.

## Coding standards and language features

Always write strictly typed code.

- Python (3.12):
  - Use full type hints everywhere (functions, variables as needed). Prefer precise types and type narrowing.
  - Prefer `typing.Protocol` for interfaces over `abc.ABC`, except where ABC is required or clearer.
  - Use modern features when appropriate: structural pattern matching (`match`), `dataclasses` (with `kw_only` when useful), `pathlib`, `enum.StrEnum`, `typing.Self`, `typing.TypedDict`/`NotRequired`, `type` statements, `@overload`, and f-strings.
  - Target mypy/pyright-friendliness; avoid `Any`. Keep functions small and pure where practical.
  - Dependencies and execution via uv only; never use `pip` in this repo.

- TypeScript (tooling in template):
  - Enable strict mode (`"strict": true`) and modern target/module per the template tsconfig. Prefer ES2022+ features.
  - Use explicit types, `unknown` over `any`, `as const` where helpful, discriminated unions, and `satisfies` for constraint checks.
  - Prefer composition over inheritance. Keep side effects explicit.
- Write strategic comments that explain the "why" behind non-obvious decisions, not the "what" or "how" that code already shows

General:
- Favor small, deterministic functions and clear error handling.
- Keep test coverage for hook and generation logic; add unit tests alongside changes.

## Pitfalls and workarounds observed

- Missing `corepack` leads to one failing integration test when trying to run `pnpm` inside the baked project. Workaround: install/enable Corepack (Volta recommended) or temporarily skip that test.
- Ensure Python version >= 3.12; set via `.python-version` or system default. `uv` will manage the venv automatically.

## What to do before opening a PR

- Always: `uv sync --dev && uv run pytest -q`. If any test fails, check for Corepack/pnpm availability and run `corepack enable`.
- If you updated Markdown, you may optionally run markdownlint via Node tooling inside the generated template, but it’s not required for the Python tests here.

## File index (root)

- `pyproject.toml` — dev deps for tests; use `uv`.
- `hooks/` — pre/post generation hooks.
- `tests/` — pytest, including cookiecutter integration tests.
- `cookiecutter.json` — default context.
- `README.md`, `docs/` — docs about the template and prompt system.
- `{{cookiecutter.project_slug}}/` — template content including Node/Nx/CALM.

Follow these steps verbatim; only search if you encounter discrepancies.

## Commit Messages

Write clear, scannable messages that explain **what changed and why**. Follow conventional commit format: `type(scope): description`

**Structure:**
- Use imperative mood ("Add feature" not "Added feature")
- Keep subject line ≤50 characters
- Use bullet points for multiple changes
- Include breaking change warnings when applicable

**Content focus:**
- Explain business impact and reasoning, not implementation details
- Link to issues/tickets when relevant
- Use meaningful emojis sparingly (✨ new feature, 🐛 bugfix, ♻️ refactor)
- Include diagrams (mermaid) only when they clarify complex architectural changes


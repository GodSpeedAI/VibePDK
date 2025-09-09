---
kind: prompt
domain: platform
task: bootstrap
budget: M
mode: 'agent'
model: GPT-4.1
tools: ['codebase', 'search']
description: 'Bootstrap developer platform: devcontainer, tasks, tests, CI, lint/typecheck, onboarding.'
---

# Bootstrap Developer Platform (DX)

## Read
- `docs/dev_prd.md`, `docs/dev_adr.md`, `docs/dev_sds.md`, `docs/dev_technical-specifications.md`

## Task
- Generate or update:
  - Devcontainer, task runner, test harness, CI jobs, linters/type-checkers.
  - Sample “hello world” + smoke tests.
- Ensure each step cites relevant DEV spec IDs and notes any conflicts with ADR/SDS/TS.

## Output
- Direct file edits with minimal working examples.
- README section "Developer Onboarding" with time-to-first-PR under 15 minutes.

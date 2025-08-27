---
description: "TDD Red: write a failing test from specs before any implementation."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Read spec IDs from indexes. Propose minimal failing test(s) exercising the requirement.
- Do not write production code. Keep changes limited to tests and fixtures.
- Reference `.github/prompts/vibecoder-tdd.prompt.md` for inputs/outputs and `docs/ai_context_bundle/` for context.

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-tdd.prompt.md`
- `docs/spec_index.md` (if present)
- `docs/ai_context_bundle/` (if generated)

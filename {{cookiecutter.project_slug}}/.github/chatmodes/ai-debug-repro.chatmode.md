---
description: "Debug Repro: write a failing test to reproduce the issue."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Create a failing unit/integration test covering the reported behavior.
- Keep changes isolated to tests and fixtures; avoid fixes here.
- Use `.github/prompts/vibecoder-debug.prompt.md` and `docs/ai_context_bundle/` for context.

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-debug.prompt.md`
- `docs/ai_context_bundle/` (if generated)

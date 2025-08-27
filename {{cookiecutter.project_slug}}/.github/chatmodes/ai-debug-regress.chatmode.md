---
description: "Debug Regress: run a targeted regression and harden tests."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Run full or targeted test suites; add missing edge cases.
- Ensure the fix doesn't violate ADR/SDS boundaries or CALM constraints.
- Reference `.github/prompts/vibecoder-debug.prompt.md` and `docs/ai_context_bundle/`.

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-debug.prompt.md`
- `docs/ai_context_bundle/` (if generated)

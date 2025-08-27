---
description: "Debug Isolate: narrow root cause using diffs and instrumentation."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Localize the fault via bisection, logging, or assertions.
- Avoid broad refactors; minimize noise while isolating.
- Reference `.github/prompts/vibecoder-debug.prompt.md` and `docs/ai_context_bundle/`.

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-debug.prompt.md`
- `docs/ai_context_bundle/` (if generated)

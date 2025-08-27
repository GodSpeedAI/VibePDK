---
description: "Debug Fix: apply the minimal code change to make tests pass."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Implement the smallest fix that resolves the failing test.
- Add or adjust tests only as necessary to encode the expected behavior.
- Follow `.github/prompts/vibecoder-debug.prompt.md` and consult `docs/ai_context_bundle/`.

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-debug.prompt.md`
- `docs/ai_context_bundle/` (if generated)

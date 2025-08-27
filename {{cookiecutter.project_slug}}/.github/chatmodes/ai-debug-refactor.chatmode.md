---
description: "Debug Refactor: clean up after the fix while tests remain green."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Improve code clarity and remove temporary diagnostics.
- Avoid behavior changes. Keep risk low.
- Use `.github/prompts/vibecoder-debug.prompt.md` guidance and `docs/ai_context_bundle/`.

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-debug.prompt.md`
- `docs/ai_context_bundle/` (if generated)

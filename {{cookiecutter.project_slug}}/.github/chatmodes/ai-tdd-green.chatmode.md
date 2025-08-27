---
description: "TDD Green: implement the simplest code to pass newly failing tests."
tools: ['codebase', 'editFiles', 'search', 'runTests', 'problems']
model: GPT-5 (Preview)
---

# Mode Guidance
- Implement only what's needed for the failing test to pass.
- Keep scope tight. Avoid refactors; favor small, isolated changes.
- Use `.github/prompts/vibecoder-tdd.prompt.md` guidance and consult `docs/ai_context_bundle/` to align with architecture (CALM + tech stack).

## Included Instructions
- `.github/copilot-instructions.md`
- `.github/prompts/vibecoder-tdd.prompt.md`
- `docs/ai_context_bundle/` (if generated)

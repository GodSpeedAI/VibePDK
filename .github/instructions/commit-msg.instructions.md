---
description: "Commit message guidance with traceability"
applyTo: "**"
---

# Commit Message Guidelines

- Subject line: ≤ 72 chars, imperative mood (e.g., "Add", "Fix", "Refactor").
- Body: wrap at ~72–100 cols; explain the what and why, not just how.
- Traceability: include relevant spec IDs (e.g., PRD-xxx, ADR-xxx, SDS-xxx, TS-xxx, DEV-*).
- Risks/Mitigations: call out security, perf, or UX risks and what mitigates them.
- Tests/Docs: mention updated or added tests and documentation when applicable.
- Make messages cognitively ergonomic and add lots of meaningful emojis 🎉

Examples
- feat(domain): add user profile service (PRD-023, ADR-008)
  - Adds service + integration tests; documents API in docs/dev_technical-specifications.md
  - Risk: cache stampede on warm start; Mitigation: request coalescing

Note: This aligns with the existing commit-msg hook that expects a spec ID in the commit message.

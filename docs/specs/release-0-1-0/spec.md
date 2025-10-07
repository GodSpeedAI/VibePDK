---
thread: release-0-1-0
matrix_ids:
  - REL-TS-001
  - DEV-PRD-007
---

# Feature Specification

## What

- Align all publishable manifest files (`package.json`, `pyproject.toml`, template manifests) to version `0.1.0`.
- Ensure release automation metadata (tags/notes) reflects the `v0.1.0` release number.
- Document the release scope and validation within the spec-plan-tasks workflow to preserve traceability.

## Why

- Provide a consistent first minor release that downstream consumers can reference.
- Reinforce the prompt-as-code lifecycle by tying release artifacts to specs and automated validation.
- Maintain a clear upgrade story for both the template generator and generated projects.

## Acceptance Criteria

- All manifests intended for publication declare version `0.1.0`.
- Tests cover the expected release version to prevent accidental regressions.
- A Git tag `v0.1.0` exists locally and instructions for publishing are documented.
- Traceability updates are attempted (`pnpm spec:matrix`), and any blockers are recorded in tasks.

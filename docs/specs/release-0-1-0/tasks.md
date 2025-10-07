---
thread: release-0-1-0
matrix_ids:
  - REL-TS-001
---

# Tasks

## Tasks

1. [x] Confirm prior art: review `package.json`, `pyproject.toml`, and template manifests for current version values.
2. [x] Author failing release-version pytest capturing all manifest sources.
3. [x] Update every publishing manifest and related metadata to `0.1.0`.
4. [ ] Run `pytest` and `pnpm spec:matrix` to validate tests and traceability. _(Partial: `uv run pytest` executed; pre-existing Cookiecutter template failures persist. `spec:matrix` blocked because `tools/spec/matrix.js` is absent in repo root.)_
5. [x] Create local `v0.1.0` tag and document push/release instructions.

> Push guidance: `git push origin v0.1.0` and create the GitHub release describing the 0.1.0 scope traced in this spec.

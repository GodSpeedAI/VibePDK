---
thread: release-0-1-0
matrix_ids:
  - REL-TS-001
---

# TS Implementation Plan

## TDD Cycles

1. **Version enforcement test**
   - *Red*: Add a pytest (`tests/test_release_version.py`) that asserts `package.json`, template manifests, and `pyproject.toml` expose the release version constant (initially expect legacy value to observe failure).
   - *Green*: Update every publishing manifest to declare `0.1.0` and share a helper for reading the version value.
   - *Refactor*: Consolidate duplicated version loading logic in the new test to keep fixtures tidy.

2. **Release tagging guidance**
   - *Red*: Extend tasks/spec docs to require a Git tag check; run tests before the tag exists.
   - *Green*: Create a local `v0.1.0` tag after validations succeed.
   - *Refactor*: Document publish steps and ensure traceability metadata references the spec ID.

## File Changes

- Add `docs/specs/release-0-1-0/spec.md`, `plan.ts.md`, and `tasks.md`.
- Introduce `tests/test_release_version.py` covering manifest version alignment.
- Update `package.json`, `{{cookiecutter.project_slug}}/package.json`, and `pyproject.toml` to `0.1.0`.
- Capture release instructions in the tasks doc and, if needed, update index/matrix files.

## Validation Steps

- Run `pytest` to exercise new tests.
- Execute `pnpm spec:matrix` (via `just spec-matrix` when available) to refresh traceability.
- Run `pnpm prompt:lint` if prompt files are touched (N/A for this change).
- After validations, create and annotate the `v0.1.0` tag.

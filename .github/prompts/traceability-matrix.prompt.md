---
mode: 'agent'
model: GPT-4.1
tools: ['codebase', 'search']
description: 'Build or update the traceability matrix, find gaps, propose tests.'
---

# Build/Update Traceability Matrix

## Inputs
- PRD items, ADR decisions, SDS components.
- Current code structure (`src/**`) and tests.

## Task
Create or update a matrix in `docs/traceability_matrix.md`:

Columns:
- Spec ID (PRD/ADR/SDS)
- Artifact (file/class/API/test)
- Status (Planned/In-Progress/Done)
- Link to commit/PR
- Notes

## Rules
- Scan for missing links or orphan artifacts; list them under "Gaps".
- Propose tests for any spec without coverage.

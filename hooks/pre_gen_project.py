"""
Cookiecutter pre-generation hook.

Validates key inputs to fail fast with actionable messages.
Keep logic minimal to avoid technical debt; prefer post-gen tasks for heavy lifting.
"""

from __future__ import annotations

import os
import re
import sys


def fail(msg: str) -> None:
    print(f"[pre_gen_project] ERROR: {msg}")
    sys.exit(1)


slug = "{{ cookiecutter.project_slug }}".strip()
author = "{{ cookiecutter.author_name }}".strip()
pyver = "{{ cookiecutter.python_version }}".strip()
description = "{{ cookiecutter.description }}".strip()


# project_slug: kebab-case or snake_case, 3..50 chars
if not re.fullmatch(r"[a-z0-9]+(?:[-_][a-z0-9]+)*", slug):
    fail(
        "project_slug must be kebab-case or snake_case using [a-z0-9_-], e.g., my-hexagon-app"
    )
if not (3 <= len(slug) <= 50):
    fail("project_slug length must be between 3 and 50 characters")


# author_name: non-empty
if not author:
    fail("author_name must not be empty")


# python_version: basic 3.x validation
if not re.fullmatch(r"3\.(10|11|12)(?:\.\d+)?", pyver):
    fail("python_version must be 3.10, 3.11, or 3.12 (optionally with patch)")


# description: short sanity check
if len(description) < 5:
    fail("description must be at least 5 characters")

print("[pre_gen_project] inputs validated ✅")

# Optional: warn (do not fail) if helpful env vars aren't set; .envrc defaults may cover these.
for var in ("PROJECT_NAME", "PROJECT_DESCRIPTION"):
    if not os.environ.get(var):
        print(f"[pre_gen_project] WARN: {var} is not set; proceeding with defaults")

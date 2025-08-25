"""
Cookiecutter post-generation hook.

Keep it lightweight: print next steps and environment hints; avoid side effects.
"""

from __future__ import annotations

import os

project_slug = "{{ cookiecutter.project_slug }}"
project_name = os.environ.get("PROJECT_NAME", project_slug)
project_description = os.environ.get("PROJECT_DESCRIPTION", "")

print("\n[post_gen_project] Generation complete!")
print(f"Project name: {project_name}")
print(f"Description:  {project_description}\n")

print("Next steps:")
print(
    "1. Run 'direnv allow' to load environment variables from .envrc (if using direnv)."
)
print(
    "2. Install toolchains: enable Corepack → 'corepack enable && corepack prepare pnpm@latest --activate' (Node), and install Python deps via 'uv pip install --system -r requirements.txt' (if applicable)."
)
print("3. Generate inputs: 'just gen-domain' or 'just gen-calm' as needed.")
print("4. Scaffold services: 'just nx-generate' (Nx + @nxlv/python).")
print("5. See README.md for commands and workflow details.\n")

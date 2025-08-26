# VibePDK

[![Node Tests](https://github.com/SPRIME01/VibePDK/actions/workflows/node-tests.yml/badge.svg)](https://github.com/SPRIME01/VibePDK/actions/workflows/node-tests.yml)

# {{ cookiecutter.project_slug }} — Cookiecutter template ⚙️
Quick reference and onboarding for the Nx + CALM + Cookiecutter template.
# {{ cookiecutter.project_slug }} — Cookiecutter template ⚙️

Quick reference and onboarding for the Nx + CALM + Cookiecutter template.

## ✨ What this template provides

- 🚦 [Nx](https://nx.dev/) for monorepo orchestration
- 🐍 `(@nxlv/python)[https://www.npmjs.com/package/@nxlv/python]` scaffolds (FastAPI + Pydantic + tests)
- 🧭 [CALM](https://github.com/finos/architecture-as-code.git) (architecture-as-code) for topology, patterns, and deployment metadata
- 📦 Domain model in YAML (`domain/domain.yaml`)
- 🧰 `justfile` for cross-platform developer tasks
- 💬 Prompt management artifacts (.github copilot instructions, prompts, chat modes)

## 🔧 Requirements

- Python 3.12 (pyenv or system)
- Node.js 24
- cookiecutter (`uv tool install cookiecutter` or `pipx install cookiecutter`)
- [direnv](https://direnv.net/) (recommended)
- Optional: Nx CLI (`pnpm dlx nx --version`), Git

## ⚡ Quick Start (WSL2 + zsh)

Follow these minimal steps on Ubuntu in WSL2 using zsh and direnv:

```bash
# 1) Ensure zsh + direnv
sudo apt update && sudo apt install -y zsh direnv git
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc

# 2) Install Python 3.12 (via pyenv, recommended) and uv
sudo apt install -y build-essential curl libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev llvm libncursesw5-dev \
  xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
exec zsh
pyenv install 3.12.11
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3) Install Node 24 with Volta and pnpm
curl https://get.volta.sh | bash
export VOLTA_HOME="$HOME/.volta" && export PATH="$VOLTA_HOME/bin:$PATH"
exec zsh  # reload shell so Volta is on PATH
volta install node@24
volta install pnpm@latest

# 4) Generate a project
cookiecutter path/to/this/repo
cd my-hexagon-app

# 5) Load environment
direnv allow

# 6) Pin toolchain (inside generated project with package.json)
# Ensures everyone uses the same Node/pnpm versions
volta pin node@24 pnpm@latest
```

## 🚀 Generate a project from this template

1. Clone this repository.
2. Run Cookiecutter against the repository:

```bash
cookiecutter path/to/this/repo
# provide `project_slug`, `author_name`, etc.
```

3. Enter the new project directory and allow direnv:

```bash
cd my-hexagon-app
direnv allow
```

## 🏁 Common tasks (via `just`)

- `just gen-domain` — Convert `domain/domain.yaml` → generator inputs
- `just gen-calm` — Convert `architecture/calm/*.json` → generator inputs
- `just nx-generate` — Run Nx generators to scaffold services
- `just calm-validate` — Validate CALM artifacts
- `just test` — Run tests
- `just build` / `just deploy env=staging tag=v0.1.0` — Build & deploy (if configured)

If you don’t have `just` installed, see its docs or run the underlying commands directly.

## 🗂️ Example generated layout

When you render a project, expect a layout like:

```
architecture/
  calm/
domain/
  domain.yaml
generators/
  nx/
  nxlv-python/
tools/
  calm-transformer/
apps/
libs/
.github/
.vscode/
justfile
.envrc
```

## 🔐 Secrets & local overrides

- Do NOT commit secrets. Use `.envrc.local` (git-ignored) or your secret manager.
- The template ships a helpful `.envrc` at project root — edit or override via `.envrc.local`.

## 🧩 Hooks

- `hooks/pre_gen_project.py` runs before generation. Add `hooks/post_gen_project.py` for post-creation tasks.

## 📚 Docs and mappings

See the `docs/` folder for mapping guidance between CALM, `domain.yaml`, and generator inputs, plus prompt‑management docs:

- Prompt system: `docs/README.md`
- Integration plan: `docs/devkit-prompts-instructions-integration.md`
- Commit messages: `docs/commit_message_guidelines.md` and `.github/instructions/commit-msg.instructions.md`
- Prompts: `.github/prompts/*` and chat modes: `.github/chatmodes/*`
 - Tech stack sync: `techstack.yaml` + `docs/techstack.schema.json`; run `just plan-techstack` then `just sync-techstack`. See `.github/prompts/sync-techstack.prompt.md`.

---

If you want, I can also:

- Add a short Quick Start section that runs the minimal steps for WSL2/zsh, or
- Add example `pre_gen_project.py` checks (e.g., validate cookiecutter inputs) or
- Create a generated `.envrc` template inside `{{ cookiecutter.project_slug }}`.

Pick one and I’ll implement it.


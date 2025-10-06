# 🚀 VibePDK

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Node Tests](https://github.com/SPRIME01/VibePDK/actions/workflows/node-tests.yml/badge.svg)](https://github.com/SPRIME01/VibePDK/actions/workflows/node-tests.yml)
[![Cookiecutter Template](https://img.shields.io/badge/cookiecutter-template-blue.svg)](https://github.com/audreyr/cookiecutter)

---

## 🌟 Imagine This

You're starting a new project. It's 9 AM on Monday morning. Your coffee is still hot.

Instead of spending the next three days wrestling with:

- *"Which framework should we use?"*
- *"How do we keep the architecture consistent?"*
- *"Where do we even put our AI prompts?"*
- *"Why is setting up a monorepo so complicated?"*

**You run one command.**

By 9:05 AM, you have a complete, production-ready foundation—like a master chef handing you a kitchen where every tool is exactly where you need it, every recipe is proven, and the whole team knows how to cook together.

**That's VibePDK.**

---

## 🎯 The Problem (The Real One)

Picture a construction site where every builder uses different blueprints, speaks a different language, and keeps their tools in random places. That's what modern software development feels like:

### 😓 Day 1: The Setup Nightmare

- Spend days configuring tools instead of writing code
- Copy-paste from old projects, hoping nothing breaks
- Each team member has a slightly different setup

### 🌪️ Month 3: The Architecture Drift

- Your "microservices" are now a tangled web
- Nobody knows where to add new features anymore
- Documentation is outdated before it's even written

### 🤖 Year 1: The AI Chaos

- AI tools give different answers to different team members
- Prompt quality depends on who's asking
- No consistent way to capture what works

**The cost?** Weeks of lost productivity. Frustrated developers. Projects that are hard to scale.

---

## ✨ The Solution (Your New Superpower)

VibePDK is like having an experienced architect, a master builder, and an AI assistant working together from day one.

Think of it as **three magical powers** working in harmony:

### 🧭 Power 1: Your Architectural Blueprint (CALM)

Imagine having a GPS for your entire codebase—one that not only shows you where everything is, but ensures no one can accidentally build a highway through your living room.

**What it feels like:**

- Define your system architecture once, in plain language
- Every service, every connection, every rule is visible at a glance
- Your architecture enforces itself—like guardrails that gently guide you back on track
- Visual diagrams update automatically as your system evolves

**The magic:** Architecture drift becomes impossible. Your system stays organized as it grows, like a well-planned city instead of urban sprawl.

### 🚦 Power 2: Your Coordination Engine (Nx Monorepo)

Picture a smart assistant who knows exactly which parts of your project need attention—and handles the boring coordination work for you.

**What it feels like:**

- Change one file, and only the affected parts rebuild (not everything)
- Share code across projects without the copy-paste nightmare
- Run tests intelligently—only where it matters
- See your entire project's dependency graph in beautiful clarity

**The magic:** Your monorepo feels light and fast, even with dozens of projects. It's like having a perfectly organized workshop where every tool is within arm's reach.

### 🤖 Power 3: Your AI Collaboration System

Imagine your whole team having access to the same expert advisor—one that remembers your project's quirks, speaks your domain language, and gives consistent answers every time.

**What it feels like:**

- Prompts are versioned and tested, like production code
- Context-aware conversations that understand your project structure
- AI suggestions that follow your architectural rules
- Knowledge capture that turns good ideas into reusable patterns

**The magic:** AI becomes a reliable team member, not a wild card. Every developer gets expert-level assistance, consistently.

---

## 🎬 See It In Action

### The 5-Minute Project Launch

**Step 1: Dream It** (30 seconds)

```bash
cookiecutter https://github.com/SPRIME01/VibePDK.git
# Answer 4 simple questions about your project
```

**Step 2: Enter Your World** (1 minute)

```bash
cd my-awesome-app
direnv allow  # Your environment configures itself
pnpm install  # Dependencies flow in smoothly
```

**Step 3: Build It** (3 minutes)

```bash
just gen-calm          # Architecture materializes from your design
just nx-generate       # Scaffold your first service
just test              # Everything passes (already!)
```

**What just happened?**

In the time it takes to finish your coffee, you went from nothing to:

- ✅ A production-grade project structure
- ✅ Architecture governance in place
- ✅ AI assistants configured for your domain
- ✅ Tests passing
- ✅ Team ready to contribute

**No configuration hell. No architectural debates. No "where do I put this?" moments.**

---

## 💫 The Difference You'll Feel

### Before VibePDK

```text
Day 1-3:   😰 Wrestling with setup, debating tool choices
Week 2:    🤔 "How do we structure this again?"
Month 2:   😫 Refactoring because the architecture fell apart
Month 4:   😤 Different AI answers causing confusion
Month 6:   😱 Can't onboard new developers—too complex
```

### After VibePDK

```text
Day 1:     🚀 Shipping features (setup done in 5 minutes)
Week 2:    😊 Architecture guides decisions automatically
Month 2:   ✨ Adding services feels natural and easy
Month 4:   🤝 Team collaborates with consistent AI assistance
Month 6:   🎉 New developers productive in hours, not weeks
```

---

## 🎨 What's Inside Your New Superpower

When you generate a project with VibePDK, you get a complete ecosystem:

```text
my-awesome-app/
├── 🧭 architecture/          # Your living blueprint
│   └── calm/                 # CALM specifications that enforce themselves
│
├── 🎯 domain/                # Your single source of truth
│   └── domain.yaml          # One file that generates everything
│
├── 🤖 .github/               # AI workflow magic
│   ├── prompts/             # Battle-tested prompt templates
│   ├── chatmodes/           # Context-aware AI conversations
│   └── instructions/        # Project-specific AI guidance
│
├── ⚙️ tools/                 # Your automation toolkit
│   ├── calm/                # Architecture validation
│   ├── prompt/              # AI prompt management
│   └── spec/                # Specification tools
│
├── 📱 apps/                  # Your applications
├── 📚 libs/                  # Shared libraries
└── 🎨 .vscode/               # Editor optimized for flow
```

**Everything is connected. Everything works together. From day one.**

---

## 🌍 Who This Empowers

### 🏢 Enterprise Teams

**The scenario:** You're leading a platform team supporting 50 developers across 10 services.

**The transformation:**

- **Before:** Every team invents their own structure. Code reviews are debates about architecture.
- **After:** One template. Consistent patterns. Reviews focus on business logic, not folder structure.

**The feeling:** Finally, everyone speaks the same architectural language.

### 🚀 Startup Founders

**The scenario:** You're a founder who needs to move fast but can't afford technical debt.

**The transformation:**

- **Before:** Racing to build features, leaving a trail of "we'll fix this later" decisions.
- **After:** Ship fast with a foundation that scales. Your future self will thank you.

**The feeling:** Speed without the guilt. Growth without the mess.

### 🔬 Research Teams

**The scenario:** You're experimenting with new ideas and need to iterate quickly.

**The transformation:**

- **Before:** Every experiment is a new project from scratch. Hard to compare results.
- **After:** Spin up experiments in minutes. Focus on the novel parts, not boilerplate.

**The feeling:** More time thinking, less time wiring things together.

### 🎓 Learning Developers

**The scenario:** You're learning modern development and drowning in tool choices.

**The transformation:**

- **Before:** Paralyzed by "which framework?" decisions. Copy-pasting code you don't understand.
- **After:** A curated, production-ready setup. Learn by building real things, not configuring tools.

**The feeling:** Confidence. You're learning patterns that actually work.

---

---

## �️ Getting Started (It's Easier Than You Think)

### What You'll Need

Think of these as the basic tools in your toolkit:

```bash
# The essentials (5 minutes to install)
Python 3.12+         # The foundation (use pyenv for easy management)
Node.js 24+          # The engine (Volta makes this painless)
cookiecutter         # The template wizard (one command: uv tool install cookiecutter)
direnv              # The environment keeper (makes life so much easier)

# Nice to have
just                # Your command shortcut buddy
git                 # For version control (you probably have this)
```

**New to these tools?** No worries. Each one has a simple installer, and you'll only interact with them through friendly commands.

### Your First Project (5 Minutes)

#### Minute 1: Create

```bash
cookiecutter https://github.com/SPRIME01/VibePDK.git
```

You'll answer four questions:

- What's your project called? (e.g., "my-awesome-app")
- Who's building it? (your name)
- Which Python version? (3.12 is great)
- What does it do? (one sentence is enough)

#### Minute 2: Enter

```bash
cd my-awesome-app
direnv allow  # Trust me, this is magic
```

#### Minutes 3-4: Setup

```bash
# If using Volta (recommended)
volta pin node@24 pnpm@latest
corepack enable && corepack prepare pnpm@latest --activate

# Install everything
pnpm install
```

#### Minute 5: Validate

```bash
just test  # Watch everything pass ✅
```

**You're done.** You now have a production-ready foundation. Time to build something amazing.

---

## 🎯 Common Workflows (From Your Perspective)

### 🏗️ "I want to design my system architecture first"

```bash
# 1. Sketch your architecture (think about your system)
edit architecture/calm/system.calm.json

# 2. Let it come to life
just gen-calm           # Generates your domain model

# 3. Make sure it makes sense
just calm-validate      # Checks for architectural issues

# 4. Build from your blueprint
just nx-generate        # Creates services that match your design
```

**What this feels like:** You're an architect with a magic wand. Draw the blueprint, wave the wand, watch your building materialize.

### 🤖 "I want AI to help me code, consistently"

```bash
# 1. Explore what's possible
ls .github/prompts/     # See battle-tested prompt templates

# 2. Make sure they're solid
just prompt:lint        # Validates your prompts

# 3. Use them in your editor
# Open VS Code → GitHub Copilot Chat → Ask questions
# Your AI now understands your project structure!

# 4. Generate with confidence
just ai:scaffold type=api name=users  # AI creates code that fits
```

**What this feels like:** You have a senior developer pair programming with you—one who never gets tired and always remembers your project's conventions.

### 🔄 "I want to build features the right way"

```bash
# 1. Start with clarity
just spec:feature name=user-authentication

# 2. Plan the implementation
just spec:plan feature=user-authentication

# 3. Break it into bite-sized pieces
just spec:tasks feature=user-authentication

# 4. Build with test-driven confidence
just tdd:cycle feature=user-authentication
```

**What this feels like:** You're following a recipe from a master chef. Each step is clear. You know you're on the right path.

---

## 🌟 The Tools That Make It All Work

You don't need to understand all the internals, but here's what's working for you behind the scenes:

### 🐍 Python Power

- **FastAPI**: Lightning-fast web APIs (feels like magic)
- **Pydantic**: Data validation that actually makes sense
- **uv**: Package management without the headaches
- **pytest**: Testing that gives you confidence

### � Node.js Orchestration

- **Nx**: The brain that coordinates everything
- **pnpm**: Package management done right
- **TypeScript**: JavaScript with guardrails
- **Jest**: Testing for your Node code

### 🏗️ Architecture Tools

- **FINOS CALM**: Your architectural guardrails
- **Cookiecutter**: The project generator
- **Justfile**: One command for anything
- **Direnv**: Environments that just work

### 🤖 AI Enhancement

- **GitHub Copilot**: Your AI pair programmer
- **Prompt System**: Consistent, versioned AI interactions
- **Model Context Protocol**: Deep project understanding

**The best part?** These tools work together seamlessly. You don't manage them—you just use them.

---

## 🚨 When Things Don't Go As Planned

We've all been there. Something doesn't work, and you need a quick fix. Here are the most common hiccups and their solutions:

### 🐍 Python Environment Issues

#### Python version mismatch or uv not found

```bash
# Get the right Python version
pyenv install 3.12.11
pyenv local 3.12.11

# Install uv if missing
curl -LsSf https://astral.sh/uv/install.sh | sh

# Fresh start with dependencies
uv cache clean
uv pip install -r requirements.txt
```

**Why this happens:** Different projects need different Python versions. pyenv and uv make switching painless.

### 🟨 Node.js & pnpm Issues

#### pnpm not found or command not found

```bash
# Enable pnpm (the right way)
corepack enable
corepack prepare pnpm@latest --activate

# If using Volta (even better)
volta install node@24
volta pin node@24
```

#### Nx cache is broken or weird build errors

```bash
# Reset everything
pnpm exec nx reset
```

**Why this happens:** Node.js has evolved a lot. Using modern tools like Volta and Corepack keeps you on the happy path.

### 🧭 CALM Validation Errors

#### CALM schema validation failed

```bash
# See what's wrong (with details)
just calm:validate --verbose

# Start fresh from template
just calm:init

# Visualize dependencies
just calm:graph  # Sometimes seeing it helps
```

**Why this happens:** Architecture definitions need to follow certain rules. The validator helps you catch issues early.

### 🤖 AI Workflow Issues

#### Prompts failing validation

```bash
# Auto-fix common issues
just prompt:lint --fix
```

#### GitHub Copilot doesn't understand my project

```bash
# Reload VS Code
# Command Palette (Ctrl/Cmd + Shift + P) → "Developer: Reload Window"
```

#### MCP server not connecting

```bash
# Check your configuration
cat .vscode/mcp.json
```

**Why this happens:** AI tools need proper configuration to understand your project context. Once set up, they work beautifully.

---

## 🤝 Join the Journey

VibePDK is built by developers, for developers. Your experience matters.

### 💡 Share Your Experience

- **Found a rough edge?** Open an issue—we want to know.
- **Built something cool?** Share it with the community.
- **Have an idea?** Start a discussion.

### 🛠️ Contribute

```bash
# Get set up
git clone https://github.com/SPRIME01/VibePDK.git
cd VibePDK
uv sync --dev
pre-commit install

# Make your changes
# ...

# Verify everything works
uv run pytest
```

**We welcome:**

- Documentation improvements (especially more examples!)
- New generator templates
- Better error messages
- Prompt templates for common tasks

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License & Acknowledgments

### License

VibePDK is licensed under the [Mozilla Public License 2.0](LICENSE)—free to use, share, and modify.

### Built on the Shoulders of Giants

This project wouldn't exist without:

- **[FINOS CALM](https://github.com/finos/architecture-as-code)** - For bringing architecture-as-code to life
- **[Nx](https://nx.dev/)** - For making monorepos actually manageable
- **[Cookiecutter](https://github.com/audreyr/cookiecutter)** - For elegant project templating
- **[@nxlv/python](https://www.npmjs.com/package/@nxlv/python)** - For bridging Python and Nx
- **[GitHub Copilot](https://github.com/features/copilot)** - For showing us the future of coding

And to every developer who's wrestled with project setup and thought, *"There has to be a better way."*

---

**[⭐ Star this repo](https://github.com/SPRIME01/VibePDK)** if VibePDK saves you time and sanity!

[![GitHub stars](https://img.shields.io/github/stars/SPRIME01/VibePDK?style=social)](https://github.com/SPRIME01/VibePDK/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/SPRIME01/VibePDK?style=social)](https://github.com/SPRIME01/VibePDK/network/members)

*Built with ❤️ for developers who want to spend less time configuring and more time creating.*

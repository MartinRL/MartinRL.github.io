# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the `notebooks` subdirectory of a GitHub Pages personal site (MartinRL.github.io). It contains Polyglot Notebooks (`.dib` files) for interactive C# experimentation and workshops.

Parent repository structure:
- `/` - Main GitHub Pages site (Jekyll-based)
- `/presentations/` - Marp presentation materials (see `/presentations/CLAUDE.md`)
- `/notebooks/` - This directory: Polyglot Notebooks for C# experimentation
- Various content directories: `/en/`, `/sv/`, `/ContextAnd/`, etc.

## Directory Structure

```
notebooks/
├── CLAUDE.md
├── playground.dib                    # General-purpose C# playground
└── agents-mcp-skills/               # Workshop: Agents, MCP & Skills
    ├── agents-mcp-skills.dib        # Main workshop notebook (3.5 hours)
    ├── agenda.md                    # Calendar invite agenda (Danish)
    ├── agent-pattern.png            # Architecture diagram
    ├── github-copilot-icon.png      # Icon asset
    └── research/                    # Background research materials
```

## Technology Stack

- **Notebook Format**: Polyglot Notebooks (.dib files)
- **Primary Language**: C#
- **Runtime**: .NET Interactive kernel
- **Editor**: VS Code with Polyglot Notebooks extension
- **Version Control**: Git with main branch `master`

## Workshop: Agents, MCP & Skills

The main workshop (`agents-mcp-skills/agents-mcp-skills.dib`) covers:
- **Intro til Polyglot Notebooks** (5 min)
- **Det agentiske landskab** (15 min) - The 2024-2026 evolution
- **MCP-servere** (50 min) - Model Context Protocol theory + hands-on
- **Skills** (45 min) - Agent skills for GitHub Copilot/Claude Code
- **Byg en Agent** (55 min) - Implementing the agentic loop
- **Integration** (25 min) - Wiring MCP + Skills + Agent together

Domain: Fictional EV charging network (ChargeSmart) in Copenhagen.

## Polyglot Notebook Format

Each `.dib` file contains cell types:
- `#!meta` - Kernel configuration (JSON)
- `#!markdown` - Documentation cells
- `#!csharp` - C# code cells (executed in shared kernel session)

Variables persist across cells within a session.

## Important Rules

- **Never delete source files**: When generating images from source files (e.g., `.mmd` → `.png`), always keep the source files. They are crucial for future edits and regeneration.

## Git Workflow

```bash
# Note: git push is handled by user (production deployment decision)
git add notebooks/**/*.dib
git commit -m "feat: description"
```

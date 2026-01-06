# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the `notebooks` subdirectory of a GitHub Pages personal site (MartinRL.github.io). It contains Polyglot Notebooks (`.dib` files) for interactive C# experimentation and learning.

Parent repository structure:
- `/` - Main GitHub Pages site (Jekyll-based)
- `/presentations/` - Marp presentation materials (see `/presentations/CLAUDE.md`)
- `/notebooks/` - This directory: Polyglot Notebooks for C# experimentation
- Various content directories: `/en/`, `/sv/`, `/ContextAnd/`, etc.

## Technology Stack

- **Notebook Format**: Polyglot Notebooks (.dib files)
- **Primary Language**: C#
- **Runtime**: .NET Interactive kernel
- **Editor**: VS Code with Polyglot Notebooks extension
- **Version Control**: Git with main branch `master`

## Notebook Files

Polyglot Notebooks use the `.dib` format (previously `.dotnet-interactive`):
- **agents-skills-mcp.dib**: Template for exploring agents, skills, and MCP concepts
- **playground.dib**: General-purpose C# interactive playground

Each `.dib` file contains:
1. Metadata (kernel configuration in `#!meta` blocks)
2. Markdown cells for documentation (prefixed with `#!markdown`)
3. Code cells for C# execution (prefixed with `#!csharp`)

## Working with Polyglot Notebooks

### Opening and Running Notebooks

```bash
# Open in VS Code with Polyglot Notebooks extension
code agents-skills-mcp.dib

# The extension handles kernel startup automatically
```

### Notebook Structure

```
#!meta
{"kernelInfo":{"defaultKernelName":"csharp","items":[]}}

#!markdown
# Notebook Title
Documentation and explanations

#!csharp
// C# code cells - execute interactively
Console.WriteLine("Hello from polyglot notebook");
```

### Cell Types

- `#!markdown` - Documentation cells (rendered as formatted text)
- `#!csharp` - C# code cells (executed in .NET Interactive kernel)
- `#!meta` - Metadata cells (kernel configuration)

## Development Workflow

1. **Edit notebook files**: Modify `.dib` files directly or through VS Code
2. **Run cells**: Execute individual code cells to test C# snippets
3. **Add content**: Insert new markdown or code cells as needed
4. **Commit changes**: Standard git workflow applies

### Git Workflow

```bash
# Stage notebook changes
git add notebooks/*.dib

# Commit (Swedish or English messages are both used)
git commit -m "feat: add C# LINQ examples to playground notebook"

# Note: git push is handled by user (production deployment decision)
```

## File Patterns

- **Notebook files**: `**/*.dib` (Polyglot Notebook format)
- **Templates**: Files with "empty" or "playground" in name serve as starting points

## Important Notes

- Polyglot Notebooks support multiple languages but this repository focuses on C#
- The `.dib` format is text-based and git-friendly (unlike `.ipynb` which can have merge conflicts)
- Code cells execute in a shared kernel session - variables persist across cells
- Each notebook maintains its own kernel session when opened

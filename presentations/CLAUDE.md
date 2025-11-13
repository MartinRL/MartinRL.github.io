# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the `presentations` subdirectory of a GitHub Pages personal site (MartinRL.github.io). It contains presentation materials created with Marp (Markdown Presentation Ecosystem), which generates static HTML presentations from Markdown.

Parent repository structure:
- `/` - Main GitHub Pages site (Jekyll-based)
- `/presentations/` - This directory: presentation materials
- `/hemmastyrketräning.html` - Swedish home training program (standalone HTML)
- Various content directories: `/en/`, `/sv/`, `/ContextAnd/`, etc.

## Technology Stack

- **Presentation Framework**: Marp (Markdown → HTML presentations)
- **Static Site Generator**: Jekyll (parent site uses `jekyll-theme-minimal`)
- **Hosting**: GitHub Pages
- **Version Control**: Git with main branch `master`

## Directory Structure

```
presentations/
├── Event-Modeling-Conference-Munich-2025/
│   ├── index.html                     # Generated Marp presentation
│   └── Files/                         # Images and assets for presentation
│       ├── *.jpg, *.png              # Event modeling diagrams, speaker photos
└── {other-presentations}/
```

Each presentation is in its own subdirectory containing:
1. `index.html` - The generated Marp presentation (HTML bundle)
2. `Files/` - Assets directory (images, diagrams, media files)

## Common Development Tasks

### Viewing Presentations Locally

Open the `index.html` file directly in a browser:
```bash
# Windows (from presentations directory)
start Event-Modeling-Conference-Munich-2025/index.html

# Or serve via Python HTTP server
python -m http.server 8000
# Then navigate to http://localhost:8000/Event-Modeling-Conference-Munich-2025/
```

### Working with Marp Presentations

The HTML files are **generated outputs** from Marp. To edit:
1. Find or create the source Markdown file (typically `slides.md` or similar)
2. Edit the Markdown with Marp syntax
3. Regenerate using Marp CLI:
   ```bash
   # Install Marp CLI if needed
   npm install -g @marp-team/marp-cli

   # Generate HTML from Markdown
   marp slides.md -o index.html

   # Watch mode for live editing
   marp -w slides.md -o index.html
   ```

**Note**: The current `index.html` files are bundled exports (all-in-one HTML). Source Markdown may not be in repository.

### Git Workflow

Standard git commands apply:
```bash
# Stage changes
git add .

# Commit with descriptive message (in Swedish or English)
git commit -m "feat: lägg till ny presentation för Event Modeling Conference"

# Note: git push is handled separately by the user (deployment decision)
```

Recent commits show Swedish commit messages are common: `"fix: byt namn på chinsstång till dörrtrapets"`

## Architecture Notes

### Marp Presentation Structure

Generated HTML files contain:
- Embedded CSS (Marp theme: default theme with GitHub-style syntax highlighting)
- Bespoke.js framework for slide navigation
- View modes: presentation, presenter (with notes), next slide preview
- Keyboard shortcuts: Arrow keys, P (presenter mode), F (fullscreen)

### Asset Management

Images and files should be placed in the `Files/` subdirectory of each presentation:
- Use relative paths: `![Image](Files/image.jpg)`
- Common formats: `.jpg`, `.png` for images; `.svg` for diagrams
- Naming convention: descriptive kebab-case (e.g., `event-modeling-workshop-spec-munich.jpg`)

### Parent Site Integration

This directory is part of a larger GitHub Pages site:
- Jekyll configuration: `_config.yml` in root
- Theme: `jekyll-theme-minimal`
- Content is Swedish/English bilingual
- Auto-publishing via GitHub Pages on push to `master`

## Important Constraints

1. **No Direct Push**: Git push operations require explicit user approval (production deployment)
2. **Source Files**: Original Markdown source files may not be in repository (only generated HTML)
3. **Binary Files**: Large presentation images are committed (consider file sizes)
4. **Language**: Both Swedish and English content; commit messages often in Swedish

## File Patterns

- Presentation HTML: `**/index.html` (Marp-generated)
- Presentation assets: `**/Files/*`
- PowerPoint sources: `*.pptx` (may exist alongside HTML versions)
- Configuration: `.claude/settings.local.json` (presentation-specific Claude settings)

## Development Tips

- Marp presentations are self-contained HTML files - can be opened directly in browsers
- Use browser dev tools to inspect presentation structure and styling
- For new presentations, create a new subdirectory following the naming pattern
- Images should be optimized before committing (presentations can become large)
- Test presentations in both presenter and standard view modes
- after each change to a marp presentation, regenerate the html version of the presentation, but DO NOT open the browser with. rather, assume that I have it open in the browser (with the pertinent slide # in addition).
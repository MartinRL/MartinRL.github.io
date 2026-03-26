# CLAUDE.md

## Writing style

- Minimize use of em dashes (—) in all writing, especially articles, LinkedIn posts, and other external artifacts. Favor commas, semicolons, colons, and parentheses instead.
- **Escape square brackets** in article prose: use `\[` and `\]` for citation references (e.g. `\[1\]`) and editorial marks (e.g. `\[…\]`) so Markdown renderers do not misinterpret them as links.
- **Use the Unicode ellipsis character** (`…`, U+2026) instead of three dots (`...`).

## Images and figures

- Never embed captions or figure labels (e.g. "Fig. 1 ...") inside image files (SVG, PNG, etc.). Instead, place captions as text in the surrounding Markdown, directly below the image reference (e.g. `*Caption text.*`).
- Never set explicit `width` or `height` attributes on SVG files. SVGs should only use `viewBox` for their dimensions, leaving sizing to the consumer (the Markdown file or other embedding context).
- When embedding SVG images in Markdown, use an HTML `<img>` tag with `width="100%"` so they render at full width in Obsidian. Place the caption on the next line. Example:
  ```
  <img src="diagram.svg" alt="Diagram title" width="100%">

  *Caption text.*
  ```

## Working principles

- Maximize the amount of work Claude does autonomously; minimize the user's part. Use available tools (gh CLI, MCP servers, etc.) to handle GitHub operations, repo setup, deployments, and other tasks end-to-end without requiring user intervention.

---
name: marp-styling
description: Help with Marp presentation styling, layouts, colors, and CSS. Use when the user asks about styling slides, formatting, colors, two-column layouts, CSS, how to style list items, or any visual formatting questions.
---

# Marp Styling Guide

## Critical: Scoped CSS for List Coloring

**Inline styles DO NOT work in Marp list items.** Use scoped styles instead:

```markdown
<style scoped>
li:nth-child(1) strong { color: var(--color-primary-purple); }
li:nth-child(2) strong { color: var(--color-sky-blue); }
li:nth-child(3) strong { color: var(--color-green); }
</style>

- First item with **purple text**
- Second item with **blue text**
- Third item with **green text**
```

## Color Palette (Context& Theme)

| Variable | Hex | Use |
|----------|-----|-----|
| `--color-primary-purple` | #5500FF | Primary brand, h3 headers |
| `--color-sky-blue` | #00B6FF | Links, highlights |
| `--color-green` | #1E8C7F | Success, positive |
| `--color-orange` | #FF922D | Warnings, attention |
| `--color-dark-blue` | #043F9C | Secondary accents |
| `--color-dark-grey` | #3D424B | Body text, subtle |
| `--color-light-grey` | #C9D6DE | Borders |
| `--color-very-light-grey` | #F1F5F7 | Backgrounds |

## Background Colors

| Variable | Use |
|----------|-----|
| `--color-bg-green-light` | Success callouts |
| `--color-bg-purple-tint` | Info boxes |
| `--color-very-light-grey` | Subtle backgrounds |

## Slide Classes

Add before slide content: `<!-- _class: classname -->`

| Class | Effect |
|-------|--------|
| `title` | Title/cover slide layout |
| `section-divider` | Full-screen section break (purple gradient) |
| `two-columns` | Two column grid layout |
| `bg-purple` | Purple background, white text |
| `bg-light` | Light grey background |
| `bg-dark` | Dark grey background, white text |

## Two-Column Layout

```markdown
<!-- _class: two-columns -->

## Slide Title

### Left Column
- Point one
- Point two

### Right Column
- Point A
- Point B
```

## Info/Callout Box

```html
<div style="padding: 15px 20px; background: var(--color-bg-purple-tint);
            border-left: 3px solid var(--color-primary-purple);
            border-radius: 4px; font-size: 15pt;">
<strong>Key Insight</strong> - Description text here
</div>
```

Or use the `.highlight` class:
```html
<div class="highlight">
**Key Takeaway**: Important message here.
</div>
```

## Background Images

```markdown
![bg](Files/image.jpg)                    <!-- Full background -->
![bg fit](Files/image.jpg)                <!-- Fit to slide -->
![bg blur:3px opacity:.3](Files/image.jpg) <!-- Blurred overlay -->
![bg right](Files/image.jpg)              <!-- Right half -->
![bg left:40%](Files/image.jpg)           <!-- Left 40% -->
```

## Font Size Control

```html
<style scoped>
p { font-size: 0.8em; }
li { font-size: 0.75em; line-height: 1.3; }
ol { font-size: 0.85em; }
</style>
```

## Colored Text (Inline)

Use span with color classes:
```markdown
- <span class="purple">Purple text</span>
- <span class="blue">Blue text</span>
- <span class="green">Green text</span>
- <span class="orange">Orange text</span>
```

## Presenter Notes

Hidden notes after slide content:
```markdown
---
# Slide Title

Visible content here.

<!--
Presenter notes go here.
Not visible in presentation view.
Press P for presenter mode.
-->
```

## Common Patterns

### Emoji as Visual Anchors
```markdown
# Learning Resources

- Video tutorials
- Written guides
- Podcast episodes
```

### Numbered Steps with Scoped Sizing
```html
<style scoped>
ol { font-size: 0.8em; }
ol li { margin-bottom: 0.5em; }
</style>

1. First step
2. Second step
3. Third step
```

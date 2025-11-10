---
marp: true
theme: context
paginate: true
footer: 'Footer text'
---

<!--
Context& Marp Template
Based on Context& PowerPoint template
-->

<style>
@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700&display=swap');

/* Context& Color Palette */
:root {
  --color-primary-purple: #5500FF;
  --color-dark-grey: #3D424B;
  --color-light-grey: #C9D6DE;
  --color-very-light-grey: #F1F5F7;
  --color-sky-blue: #00B6FF;
  --color-dark-blue: #043F9C;
  --color-green: #1E8C7F;
  --color-orange: #FF922D;
  --color-white: #FFFFFF;
  --color-black: #000000;
}

/* Base Section Styling */
section {
  background-color: var(--color-white);
  color: var(--color-black);
  font-family: 'Work Sans', 'Helvetica Neue', Arial, sans-serif;
  font-size: 16pt;
  padding: 50px 80px;
  line-height: 1.5;
}

/* Headers */
h1 {
  color: var(--color-black);
  font-size: 45pt;
  font-weight: 400;
  line-height: 1.2;
  margin-bottom: 40px;
  letter-spacing: -0.02em;
}

h2 {
  color: var(--color-black);
  font-size: 32pt;
  font-weight: 500;
  margin-top: 40px;
  margin-bottom: 20px;
}

h3 {
  color: var(--color-primary-purple);
  font-size: 24pt;
  font-weight: 600;
  margin-top: 30px;
  margin-bottom: 15px;
}

h4 {
  color: var(--color-dark-grey);
  font-size: 18pt;
  font-weight: 600;
  margin-top: 20px;
  margin-bottom: 10px;
}

/* Paragraphs and Lists */
p {
  margin-bottom: 16px;
}

ul, ol {
  margin-left: 40px;
  margin-bottom: 20px;
}

li {
  margin-bottom: 8px;
}

ul > li::marker {
  color: var(--color-primary-purple);
}

/* Strong and Emphasis */
strong {
  font-weight: 600;
  color: var(--color-black);
}

em {
  font-style: italic;
  color: var(--color-dark-grey);
}

/* Links */
a {
  color: var(--color-primary-purple);
  text-decoration: none;
  border-bottom: 2px solid var(--color-sky-blue);
}

a:hover {
  color: var(--color-sky-blue);
}

/* Code */
code {
  background-color: var(--color-very-light-grey);
  color: var(--color-dark-grey);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 14pt;
}

pre {
  background-color: var(--color-very-light-grey);
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid var(--color-primary-purple);
  overflow-x: auto;
}

pre code {
  background-color: transparent;
  padding: 0;
  font-size: 13pt;
}

/* Blockquotes */
blockquote {
  border-left: 4px solid var(--color-primary-purple);
  padding-left: 20px;
  margin: 20px 0;
  color: var(--color-dark-grey);
  font-style: italic;
}

/* Tables */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 20px 0;
}

th {
  background-color: var(--color-primary-purple);
  color: var(--color-white);
  padding: 12px;
  text-align: left;
  font-weight: 600;
}

td {
  padding: 12px;
  border-bottom: 1px solid var(--color-light-grey);
}

tr:hover {
  background-color: var(--color-very-light-grey);
}

/* Footer */
footer {
  color: var(--color-dark-grey);
  font-size: 9pt;
  text-align: right;
}

/* Page Number */
section::after {
  color: var(--color-black);
  font-weight: 600;
  font-size: 9pt;
}

/* Title Slide (first slide) */
section.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px;
}

section.title h1 {
  font-size: 54pt;
  margin-bottom: 20px;
}

section.title p {
  font-size: 20pt;
  color: var(--color-dark-grey);
  margin-bottom: 60px;
}

/* Section Divider Slide */
section.section-divider {
  background: linear-gradient(135deg, var(--color-primary-purple) 0%, var(--color-dark-blue) 100%);
  color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

section.section-divider h1 {
  color: var(--color-white);
  font-size: 60pt;
}

/* Two Column Layout */
section.two-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

section.two-columns h1 {
  grid-column: 1 / -1;
}

/* Image Slide */
section img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
}

/* Highlight Box */
.highlight {
  background-color: var(--color-very-light-grey);
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid var(--color-primary-purple);
  margin: 20px 0;
}

/* Accent Colors */
.purple { color: var(--color-primary-purple); }
.blue { color: var(--color-sky-blue); }
.green { color: var(--color-green); }
.orange { color: var(--color-orange); }
.grey { color: var(--color-dark-grey); }

/* Background Variants */
section.bg-purple {
  background-color: var(--color-primary-purple);
  color: var(--color-white);
}

section.bg-purple h1,
section.bg-purple h2,
section.bg-purple h3 {
  color: var(--color-white);
}

section.bg-light {
  background-color: var(--color-very-light-grey);
}

section.bg-dark {
  background-color: var(--color-dark-grey);
  color: var(--color-white);
}

section.bg-dark h1,
section.bg-dark h2,
section.bg-dark h3 {
  color: var(--color-white);
}

/* Footer/Header positioning */
header {
  position: absolute;
  top: 30px;
  right: 80px;
  color: var(--color-dark-grey);
  font-size: 9pt;
}
</style>

---

<!-- _class: title -->

# Presentation Title

Your subtitle or tagline here

12 August 2025

---

## Agenda

- First topic
- Second topic
- Third topic
- Fourth topic

---

## Standard Content Slide

This is a regular content slide with body text.

- Bullet point one
- Bullet point two
- Bullet point three

You can use **bold text** and *italic text* for emphasis.

---

<!-- _class: two-columns -->

## Two Column Layout

### Left Column

- Point one
- Point two
- Point three

### Right Column

- Point A
- Point B
- Point C

---

## Highlight Example

Regular text content here.

<div class="highlight">

**Key Takeaway**: This is an important message highlighted for emphasis.

</div>

More regular content continues here.

---

## Code Example

Here's how you can display code:

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet('World'));
```

---

## Table Example

| Feature | Description | Status |
|---------|-------------|--------|
| Feature A | Description of feature A | ✅ Complete |
| Feature B | Description of feature B | 🔄 In Progress |
| Feature C | Description of feature C | 📋 Planned |

---

<!-- _class: section-divider -->

# Section Break

---

<!-- _class: bg-purple -->

## Dark Slide with Purple Background

- This slide has a purple background
- All text is white for contrast
- Great for emphasizing key points

---

<!-- _class: bg-light -->

## Light Background Variant

This slide uses the very light grey background for subtle variation.

- Still maintains readability
- Softer visual appearance
- Good for transitional slides

---

## Colored Text

You can use colored text for emphasis:

- <span class="purple">Purple</span> for primary branding
- <span class="blue">Blue</span> for links and highlights
- <span class="green">Green</span> for success or positive
- <span class="orange">Orange</span> for warnings or attention

---

## Blockquote Example

> "This is a quoted text that stands out from the regular content. Perfect for testimonials, key insights, or important references."
>
> — Author Name

---

## Thank You

**Contact Information**

- Email: contact@contextand.com
- Website: contextand.com

---

<!--
Usage Notes:

1. To use this template, save it as a .md file
2. Run: marp your-presentation.md -o output.html
3. Or use Marp for VS Code extension

Slide Classes:
- title: Title/cover slide
- section-divider: Full-screen section break
- two-columns: Two column layout
- bg-purple: Purple background
- bg-light: Light grey background
- bg-dark: Dark grey background

Color Classes:
- .purple, .blue, .green, .orange, .grey

Special Elements:
- Use <div class="highlight"> for callout boxes
-->

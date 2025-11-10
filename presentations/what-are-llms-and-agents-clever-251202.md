---
marp: true
theme: context
paginate: true
---

<!-- _class: title -->

# LLMs & Agents

What are they, and why can they code?

Clever, 2 December 2025

---

## Purpose: From Magic to Math

> Any sufficiently advanced technology is indistinguishable from magic.
>
> — Arthur C. Clarke

---

## Understanding LLMs

- **Tokens** - How text becomes numbers
- **Transformer** - The architecture that powers them
- **Parameters** - 70B+ learned weights = knowledge
- **Probabilistic** - Predicts probabilities, not facts
- **Context Window** - Working memory limit (4K-1M tokens)
- **Temperature** - Randomness control (0=deterministic, 2=creative)

---

<!-- _class: split-slide -->

<div class="left-panel purple-bg">

## Tokens
### Breaking Words Into Numbers

Text gets chopped into chunks called tokens - sometimes whole words, sometimes parts. "Strawberry" might become ["Straw", "berry"].

The machine can't read words. It needs numbers. Each token gets a unique ID number from a fixed vocabulary of ~100,000 pieces.

This is why LLMs struggle counting letters - they don't see letters, they see token chunks.

</div>

<div class="right-panel">

![Tokenization visualization](Files/tokens-visualization.svg)

</div>

---

<!-- _class: split-slide -->

<div class="left-panel blue-bg">

## Transformer
### The Attention Machine

Instead of reading words left-to-right like humans, transformers look at ALL words simultaneously through "attention mechanisms."

Each word asks: "Which other words should I pay attention to?" The word "bank" looks at nearby words to decide if it means money or river.

This parallel processing is why transformers are fast - and why they transformed AI in 2017.

</div>

<div class="right-panel">

![Transformer architecture diagram](Files/transformer-architecture.svg)

</div>

---

<!-- _class: split-slide -->

<div class="left-panel green-bg">

## Parameters
### 70 Billion Knobs to Tune

Parameters are like volume knobs - each one adjusts how strongly one neuron connects to another. GPT-4 has over a trillion of them.

These aren't programmed - they're learned by showing the model billions of text examples. Like a student who memorized every book ever written, then learned the patterns.

More parameters = more nuanced understanding, but also more compute needed.

</div>

<div class="right-panel">

![Neural network parameters visualization](Files/parameters-network.svg)

</div>

---

<!-- _class: split-slide -->

<div class="left-panel orange-bg">

## Probabilistic
### It's All Statistics

LLMs don't "know" facts - they predict what word probably comes next based on patterns they've seen. Like autocomplete on steroids.

When asked "The capital of France is...", it's not retrieving a fact. It's calculating that "Paris" has the highest probability based on millions of similar sentences.

This is why they can sound confident while being completely wrong - high probability doesn't mean true.

</div>

<div class="right-panel">

![Probability distribution graph](Files/probability-distribution.svg)

</div>

---

<!-- _class: split-slide -->

<div class="left-panel dark-blue-bg">

## Context Window
### The AI's Working Memory

Context window is how much text the model can "remember" during a conversation - measured in tokens. Like RAM for conversations.

Early models: 4K tokens (~3,000 words)
Current models: 128K-1M tokens (~100,000-750,000 words)

Once full, it forgets the beginning. No long-term memory - each conversation starts fresh.

</div>

<div class="right-panel">

![Context window memory visualization](Files/context-window.svg)

</div>

---

<!-- _class: split-slide -->

<div class="left-panel grey-bg">

## Temperature
### The Creativity Dial

Temperature controls randomness in word selection:
- **0**: Always picks the most likely word (boring but consistent)
- **0.7**: Balanced creativity (default for most uses)
- **2.0**: Wild randomness (creative but often nonsensical)

Low temp for code and facts. High temp for brainstorming and fiction. It's literally how "heated" the probability distribution gets.

</div>

<div class="right-panel">

![Temperature effect on text generation](Files/temperature-effects.svg)

</div>

---

<!-- _class: bg-purple -->

## Recommended Reading 📚

- ChatGPT
- Not Artificial, Not I...
- Vibe Coding

---


<!-- Styles at the end for easier content editing -->

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

/* Split Slide Layout */
section.split-slide {
  display: grid;
  grid-template-columns: 2fr 1fr;
  padding: 0 !important;
  height: 100%;
  margin: 0;
}

section.split-slide .left-panel {
  padding: 60px 50px;
  padding-top: 100px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  min-height: calc(100% + 100px);
  margin-top: -50px;
  margin-bottom: -50px;
}

section.split-slide .right-panel {
  background-color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  min-height: calc(100% + 100px);
  margin-top: -50px;
  margin-bottom: -50px;
}

section.split-slide .right-panel img {
  max-width: 100%;
  max-height: 80%;
  object-fit: contain;
  border-radius: 0;
}

section.split-slide h2 {
  color: var(--color-white);
  font-size: 36pt;
  margin-top: 0;
  margin-bottom: 10px;
}

section.split-slide h3 {
  color: var(--color-white);
  opacity: 0.9;
  font-size: 18pt;
  font-weight: 400;
  margin-top: -5px;
  margin-bottom: 30px;
}

section.split-slide p,
section.split-slide li {
  color: var(--color-white);
  font-size: 16pt;
  line-height: 1.6;
}

section.split-slide ul {
  margin-left: 0;
  list-style: none;
}

section.split-slide ul li::before {
  content: "→ ";
  color: var(--color-white);
  opacity: 0.7;
}

/* Background colors for panels */
.purple-bg {
  background-color: var(--color-primary-purple);
}

.blue-bg {
  background-color: var(--color-sky-blue);
}

.dark-blue-bg {
  background-color: var(--color-dark-blue);
}

.green-bg {
  background-color: var(--color-green);
}

.orange-bg {
  background-color: var(--color-orange);
}

.grey-bg {
  background-color: var(--color-dark-grey);
}
</style>

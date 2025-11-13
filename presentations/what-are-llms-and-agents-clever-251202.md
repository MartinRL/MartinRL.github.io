---
marp: true
theme: context
paginate: false
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

## Understanding LLMs: The Six Keys

<style scoped>
li:nth-child(1) strong { color: #5500FF; }
li:nth-child(2) strong { color: #00B6FF; }
li:nth-child(3) strong { color: #1E8C7F; }
li:nth-child(4) strong { color: #FF922D; }
li:nth-child(5) strong { color: #043F9C; }
li:nth-child(6) strong { color: #3D424B; }
li { margin-bottom: 12px; }
</style>

- **Tokens** → Why "strawberry" has 3 R's to an LLM
- **Transformer** → Why it can understand context, not just words
- **Parameters** → Why bigger isn't always better
- **Probabilistic** → Why it's confident when wrong
- **Context Window** → Why it forgets your first question
- **Temperature** → Why same prompt, different answer

---

## Tokens: The Puzzle

<div style="font-size: 36pt; text-align: center; margin-top: 80px;">
"strawberry"
</div>

<div style="font-size: 24pt; text-align: center; margin-top: 40px; color: #666;">
How many 'r's?
</div>

<div style="font-size: 48pt; text-align: center; margin-top: 40px; color: #5500FF;">
LLM says: 2
</div>

---

## Tokens: What's Really Happening

```
Human sees:     s-t-r-a-w-b-e-r-r-y

LLM sees:       [31552] [19685]
                "straw"  "berry"
```

<div style="margin-top: 40px; font-size: 20pt;">

The LLM never sees individual letters.
It sees **convenient linguistic units**.

That's why it can't count the 'r's in strawberry—it literally never processes 's-t-r-a-w-b-e-r-r-y', only [31552][19685], where the letter boundaries are lost inside the tokens.

</div>

---

## Tokens: Not Just Words

<div style="margin-top: 60px; font-size: 20pt; line-height: 1.8;">

**Whole words:** `"hello"` → [15339]

**Word parts:** `"understanding"` → [8154, 2259]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"under"` + `"standing"`

**Prefixes/Suffixes:** `"preprocessing"` → [1762, 29986]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"pre"` + `"processing"`

</div>

<div style="margin-top: 50px; text-align: center; font-size: 18pt; color: #666;">
This is why LLMs can handle rare words, compound words,<br>
and even **invent new words** by combining parts.
</div>

---

## Tokens: The Numbers Game

<style scoped>
.token-box {
  display: inline-block;
  padding: 10px 20px;
  margin: 10px;
  border: 2px solid #5500FF;
  border-radius: 8px;
  font-family: monospace;
  font-size: 18pt;
}
.arrow {
  color: #5500FF;
  font-size: 24pt;
  margin: 0 20px;
}
</style>

<div style="text-align: center; margin-top: 60px;">

<div class="token-box">Hello world</div>
<span class="arrow">→</span>
<div class="token-box">[15496]</div>
<div class="token-box">[1917]</div>

</div>

<div style="text-align: center; margin-top: 40px;">

<div class="token-box">ChatGPT</div>
<span class="arrow">→</span>
<div class="token-box">[9787]</div>
<div class="token-box">[38, 2898]</div>

</div>

<div style="margin-top: 60px; text-align: center; font-size: 18pt; color: #666;">
~100,000 tokens in vocabulary = ~100,000 puzzle pieces
</div>

---

## Transformer: The Context Problem

<div style="font-size: 28pt; margin-top: 80px; text-align: center;">

"I went to the **bank**..."

</div>

<div style="display: flex; justify-content: center; gap: 100px; margin-top: 60px;">
  <div style="text-align: center;">
    <div style="font-size: 24pt;">🏦</div>
    <div style="margin-top: 10px;">...to get money?</div>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 24pt;">🏞️</div>
    <div style="margin-top: 10px;">...of the river?</div>
  </div>
</div>

<div style="text-align: center; margin-top: 60px; font-size: 20pt; color: #666;">
How does AI know which one?
</div>

---

## Transformer: Attention Is All You Need

<style scoped>
.attention-word {
  display: inline-block;
  padding: 8px 16px;
  margin: 5px;
  border-radius: 6px;
  font-size: 20pt;
}
.high-attention {
  background: #00B6FF;
  color: white;
  font-weight: bold;
}
.low-attention {
  background: #E0F4FF;
  color: #666;
}
</style>

<div style="text-align: center; margin-top: 60px;">

<div class="attention-word low-attention">I</div>
<div class="attention-word low-attention">went</div>
<div class="attention-word low-attention">to</div>
<div class="attention-word low-attention">the</div>
<div class="attention-word high-attention">bank</div>
<div class="attention-word low-attention">to</div>
<div class="attention-word high-attention">deposit</div>
<div class="attention-word high-attention">money</div>

</div>

<div style="margin-top: 60px; text-align: center; font-size: 18pt;">
Every word "looks at" every other word<br>
<strong style="color: #00B6FF;">Attention scores</strong> determine meaning
</div>

---

## Transformer: Parallel Power

<div style="display: flex; gap: 40px; margin-top: 60px;">

<div style="flex: 1; text-align: center;">
<h3>Old Way (RNN)</h3>
<div style="font-size: 20pt; margin-top: 30px;">
The → cat → sat → on → the → mat
</div>
<div style="margin-top: 20px; color: #666;">
Sequential: 6 steps
</div>
</div>

<div style="flex: 1; text-align: center;">
<h3 style="color: #00B6FF;">Transformer Way</h3>
<div style="font-size: 20pt; margin-top: 30px;">
[The, cat, sat, on, the, mat]
</div>
<div style="margin-top: 20px; color: #00B6FF;">
Parallel: 1 step
</div>
</div>

</div>

<div style="text-align: center; margin-top: 60px; font-size: 18pt; color: #666;">
2017: "Attention Is All You Need" paper<br>
Changed everything.
</div>

---

## Parameters: The Scale

<div style="text-align: center; margin-top: 80px;">

<div style="font-size: 48pt; color: #1E8C7F; font-weight: bold;">
1,800,000,000,000
</div>

<div style="font-size: 20pt; margin-top: 20px; color: #666;">
GPT-4's parameters (reported)
</div>

</div>

<div style="text-align: center; margin-top: 60px; font-size: 18pt;">
If each parameter was a grain of sand,<br>
you'd have **10 dump trucks** full.
</div>

---

## Parameters: What They Store

<style scoped>
.param-example {
  background: #F0FFF8;
  border-left: 4px solid #1E8C7F;
  padding: 20px;
  margin: 20px 0;
  font-size: 18pt;
}
</style>

<div class="param-example">
<strong>Grammar:</strong> Subject-verb-object patterns
</div>

<div class="param-example">
<strong>Facts:</strong> Paris is the capital of France
</div>

<div class="param-example">
<strong>Style:</strong> How to write like Shakespeare
</div>

<div class="param-example">
<strong>Logic:</strong> If A > B and B > C, then A > C
</div>

<div style="text-align: center; margin-top: 40px; font-size: 18pt; color: #666;">
Not programmed. **Learned** from trillions of words.
</div>

---

## Probabilistic: Not a Database

<div style="text-align: center; margin-top: 60px;">

<div style="font-size: 24pt; margin: 40px 0;">
"The capital of France is..."
</div>

<div style="display: flex; justify-content: center; gap: 40px;">
  <div style="padding: 20px; background: #FFF5E6; border-radius: 10px;">
    <div style="font-size: 32pt; color: #FF922D;">95%</div>
    <div>Paris</div>
  </div>
  <div style="padding: 20px; background: #FFF5E6; border-radius: 10px;">
    <div style="font-size: 24pt; color: #FFB366;">3%</div>
    <div>Lyon</div>
  </div>
  <div style="padding: 20px; background: #FFF5E6; border-radius: 10px;">
    <div style="font-size: 20pt; color: #FFD4A3;">2%</div>
    <div>...</div>
  </div>
</div>

</div>

<div style="text-align: center; margin-top: 60px; font-size: 18pt; color: #666;">
It's not **remembering**. It's **predicting**.
</div>

---

## Probabilistic: Confident When Wrong

<div style="margin-top: 60px; font-size: 20pt;">

**You:** "What year did Google buy Twitter?"

**LLM:** "Google acquired Twitter in 2016 for $44 billion."

</div>

<div style="margin-top: 40px; padding: 20px; background: #FFF0E6; border-left: 4px solid #FF922D;">
<strong>Reality:</strong> Google never bought Twitter.<br>
But "Google acquired" + "Twitter" + "billion" appear together often enough that the model connects them.
</div>

<div style="text-align: center; margin-top: 40px; font-size: 18pt; color: #666;">
High confidence ≠ High accuracy
</div>

---

## Context Window: The Goldfish Memory

<style scoped>
.memory-box {
  background: #E6F3FF;
  border: 2px solid #043F9C;
  border-radius: 8px;
  padding: 20px;
  margin: 20px auto;
  width: 80%;
  text-align: center;
}
.forgotten {
  opacity: 0.3;
  text-decoration: line-through;
}
</style>

<div class="memory-box">
<div style="font-size: 20pt; color: #043F9C; margin-bottom: 20px;">128K Token Window</div>
<div class="forgotten">Message 1: "My name is Alice"</div>
<div class="forgotten">Message 2: "I work at Microsoft"</div>
<div>Message 98: "What's my name?"</div>
<div>Message 99: "You mentioned earlier..."</div>
<div>Message 100: Current conversation</div>
</div>

<div style="text-align: center; margin-top: 40px; font-size: 18pt;">
Once full, oldest messages disappear.<br>
**No long-term memory.**
</div>

---

## Context Window: The Numbers

<style scoped>
.size-comparison {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 60px;
}
.size-box {
  text-align: center;
  padding: 20px;
  border-radius: 10px;
}
</style>

<div class="size-comparison">
  <div class="size-box" style="background: #CCE0F5;">
    <div style="font-size: 24pt; color: #043F9C;">GPT-3.5</div>
    <div style="font-size: 36pt; font-weight: bold;">4K</div>
    <div>~500 lines of code</div>
  </div>
  <div class="size-box" style="background: #99C1EA;">
    <div style="font-size: 24pt; color: #043F9C;">GPT-4</div>
    <div style="font-size: 36pt; font-weight: bold;">128K</div>
    <div>~16K lines (React codebase)</div>
  </div>
  <div class="size-box" style="background: #66A3E0;">
    <div style="font-size: 24pt; color: #043F9C;">Claude 3</div>
    <div style="font-size: 36pt; font-weight: bold;">1M</div>
    <div>~125K lines (Linux kernel module)</div>
  </div>
</div>

<div style="text-align: center; margin-top: 60px; font-size: 18pt;">
Bigger window = More expensive & slower
</div>

---

## Temperature: Same Prompt, Different Answer

<style scoped>
.temp-example {
  margin: 30px 0;
  padding: 20px;
  border-radius: 8px;
}
</style>

<div style="font-size: 20pt; text-align: center; margin: 40px 0;">
**Prompt:** "Write a sentence about cats"
</div>

<div class="temp-example" style="background: #F5F5F5; border-left: 4px solid #3D424B;">
<strong>Temp = 0:</strong><br>
"Cats are domestic animals that are popular pets."<br>
"Cats are domestic animals that are popular pets."<br>
<em style="color: #666;">→ Same every time</em>
</div>

<div class="temp-example" style="background: #F5F5F5; border-left: 4px solid #666;">
<strong>Temp = 0.7:</strong><br>
"Cats love to nap in sunny spots."<br>
"Many cats enjoy playing with toy mice."<br>
<em style="color: #666;">→ Varied but sensible</em>
</div>

<div class="temp-example" style="background: #F5F5F5; border-left: 4px solid #999;">
<strong>Temp = 2.0:</strong><br>
"Cats purple democracy whiskers moonlight!"<br>
<em style="color: #666;">→ Creative chaos</em>
</div>

---

## The Takeaway: From Magic to Math

### 🎯 **Now You Know Why:**

- LLMs can't count letters in "strawberry" → **Tokens**
- They understand context not just words → **Transformers**
- Bigger models cost exponentially more → **Parameters**
- They're confident when wrong → **Probabilistic**
- They forget your first question → **Context Window**
- Same prompt, different answers → **Temperature**

<div style="margin-top: 60px; padding: 30px; background: #F0F5FF; border-left: 4px solid #5500FF;">
<strong style="font-size: 24pt;">The Magic:</strong> It seems to understand you<br>
<strong style="font-size: 24pt;">The Math:</strong> It's predicting the next token
</div>

---

<!-- _class: bg-purple -->

## Recommended Reading 📚

- **What Is ChatGPT Doing?** - Stephen Wolfram
- **Not Artificial, Not Intelligent** - Django Beatty
- **Vibe Coding** - Gene Kim & Steven Spear

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
  padding: 0 !important;
  height: 100%;
  margin: 0;
  position: relative;
  overflow: hidden;
}

section.split-slide .left-panel {
  position: absolute;
  left: 0;
  top: -100px;
  width: 66.67%;
  height: calc(100% + 200px);
  padding: 180px 80px 60px 50px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  box-sizing: border-box;
  overflow: visible;
}

section.split-slide .right-panel {
  position: absolute;
  right: 0;
  top: 0;
  width: 33.33%;
  height: 100%;
  background-color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px;
  box-sizing: border-box;
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
  opacity: 0.95;
  font-size: 20pt;
  font-weight: 300;
  font-style: italic;
  margin-top: -5px;
  margin-bottom: 35px;
  letter-spacing: 0.5px;
}

section.split-slide p,
section.split-slide li {
  color: var(--color-white);
  font-size: 15pt;
  line-height: 1.6;
  word-wrap: break-word;
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

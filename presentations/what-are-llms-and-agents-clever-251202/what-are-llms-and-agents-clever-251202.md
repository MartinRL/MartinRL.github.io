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
.text-gray {
  color: #aaa;
}
.text-black {
  color: #000;
}
</style>

<div style="text-align: center; margin-top: 60px;">

<div class="token-box">Hello world</div>
<span class="arrow">→</span>
<div class="token-box">[15496]</div>
<div class="token-box">[1917]</div>
<span style="margin-left: 20px; color: #666;">"Hello" + " world"</span>

</div>

<div style="text-align: center; margin-top: 40px;">

<div class="token-box">unforgettable</div>
<span class="arrow">→</span>
<div class="token-box">[359]</div>
<div class="token-box">[41119]</div>
<div class="token-box">[2048]</div>
<span style="margin-left: 20px; color: #666;">"un" + "forget" + "table"</span>

</div>

<div style="margin-top: 60px; text-align: center; font-size: 18pt; color: #666;">
<br>
~200,000 tokens in vocabulary = ~200,000 entries in a compression dictionary<br>
<span class="text-gray" style="font-size: 16pt;">Like Huffman coding for common text chunks instead of individual characters.</span><br>
<br>
<span class="text-black" style="font-size: 16pt;">Frequent code patterns get single tokens: `void`, `async`, `const`, `=>`, `()`, `{}`</span><br>
<span class="text-gray" style="font-size: 16pt;">That's why LLMs can write code—syntax appeared billions of times in training data.</span>
</div>

---

## Transformer: The Context Problem

<div style="font-size: 28pt; margin-top: 80px; text-align: center;">

"I went to the **bank**..."

</div>

<div style="display: flex; justify-content: center; gap: 100px; margin-top: 60px;">
  <div style="text-align: center;">
    <div>...to get money? 🏦</div>
  </div>
  <div style="text-align: center;">
    <div>...of the river? 🏞️</div>
  </div>
</div>

<br>
<br>

<div style="text-align: center; font-size: 20pt; color: #666;">
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
<br>
Every word "looks at" every other word<br>
<strong style="color: #00B6FF;">Attention scores</strong> determine meaning
</div>

---

## Transformer: Parallel Power

<style scoped>
.comparison-container {
  display: flex;
  gap: 30px;
  margin-top: 40px;
}
.main-content {
  flex: 2;
}
.comparison-box {
  text-align: center;
  margin-bottom: 40px;
}
.info-box {
  flex: 1;
  background-color: #f9f9f9;
  border-left: 2px solid #d8d8d8;
  padding: 18px 22px;
  border-radius: 4px;
  font-size: 13pt;
  line-height: 1.5;
  color: #666;
}
.info-box strong {
  color: #555;
}
.info-box em {
  color: #777;
}
</style>

<div class="comparison-container">

<div class="main-content">

<div class="comparison-box">
<h3>Old Way (RNN)</h3>

**The → cat → sat → on → the → mat**

<span style="color: #666;">Sequential: 6 steps</span>
</div>

<div class="comparison-box">
<h3 style="color: #00B6FF;">Transformer Way</h3>

**[The, cat, sat, on, the, mat]**

<span style="color: #00B6FF;">Parallel: 1 step</span>
</div>

</div>

<div class="info-box">

The 2017 paper "Attention Is All You Need" proved that sequential processing isn't necessary for language understanding. It's like discovering you don't need to read a book page-by-page—you can understand the entire book by seeing all relationships between all words simultaneously.

<strong>Without this parallel processing, GPT-4 would take 50 years to train instead of 3 months.</strong>

This parallel processing breakthrough is why we have LLMs today. Without it, modern AI would be economically impossible.

</div>

</div>

---

## Parameters: The Scale

<style scoped>
.params-container {
  display: flex;
  gap: 40px;
  margin-top: 40px;
}
.cloud-models, .local-models {
  flex: 1;
  text-align: center;
}
.local-models {
  background: #F5FFF5;
  border: 2px solid #1E8C7F;
  border-radius: 8px;
  padding: 15px 20px;
}
h3 {
  color: #1E8C7F;
  font-size: 20pt;
  margin: 0 0 15px 0;
}
.param-count {
  font-size: 32pt;
  color: #1E8C7F;
  font-weight: bold;
  margin: 6px 0 2px 0;
  letter-spacing: -0.5px;
}
.model-name {
  font-size: 13pt;
  color: #888;
  margin: 0 0 18px 0;
}
.quantization-tip {
  margin-top: 15px;
  padding-top: 12px;
  border-top: 1px solid #D0E8E5;
  font-size: 13pt;
  color: #666;
}
</style>

<div class="params-container">

<div class="cloud-models">
<h3>Cloud Models (2025)</h3>

<div class="param-count">2T</div>
<div class="model-name">GPT-5 (estimated)</div>

<div class="param-count">1.8T</div>
<div class="model-name">GPT-4</div>

<div class="param-count">~1T</div>
<div class="model-name">Claude Opus 4.1</div>

<div class="param-count">~500B</div>
<div class="model-name">Claude Sonnet 4.5</div>
</div>

<div class="local-models">
<h3>Office Models ($15-50K)</h3>

<div class="param-count">70B</div>
<div class="model-name">Llama 3.3 (Dual RTX 4090)</div>

<div class="param-count">32B</div>
<div class="model-name">Qwen Coder (Single RTX 4090)</div>

<div class="param-count">14B</div>
<div class="model-name">Phi-4 (Consumer GPU)</div>

<div class="quantization-tip">
💡 <strong>4-bit:</strong> 70B on $15K • 400B on $50K
</div>
</div>

</div>

<div style="text-align: center; margin-top: 45px; font-size: 10pt; color: #aaa;">
<strong>Scale:</strong> GPT-5's 2T = Empire State Building, Office 70B = 5-story building (but still very capable!)
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

<style scoped>
.probability-container {
  text-align: center;
  margin-top: 60px;
}

.prompt {
  font-size: 24pt;
  margin: 40px 0;
}

.options {
  display: flex;
  justify-content: center;
  gap: 40px;
}

.option {
  padding: 20px;
  background: #FFF5E6;
  border-radius: 10px;
}

.option .percentage {
  font-weight: bold;
}

.option:nth-child(1) .percentage {
  font-size: 32pt;
  color: #DC2626;
}

.option:nth-child(2) .percentage {
  font-size: 24pt;
  color: #F97316;
  font-weight: 600;
}

.option:nth-child(3) .percentage {
  font-size: 20pt;
  color: #FCD34D;
  font-weight: 500;
}

.footer-text {
  text-align: center;
  margin-top: 60px;
  font-size: 18pt;
  color: #666;
}
</style>

<div class="probability-container">

<div class="prompt">
"The capital of France is..."
</div>

<div class="options">
  <div class="option">
    <div class="percentage">95%</div>
    <div>Paris</div>
  </div>
  <div class="option">
    <div class="percentage">3%</div>
    <div>Lyon</div>
  </div>
  <div class="option">
    <div class="percentage">2%</div>
    <div>...</div>
  </div>
</div>

</div>

<div class="footer-text">
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

## Still a Bit of Magic?

<style scoped>
section {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 30px;
}
h2, h3 {
  grid-column: 1 / -1;
}
.left {
  grid-column: 1;
}
.right {
  grid-column: 2;
  display: flex;
  align-items: center;
}
.mystery-box {
  background: rgba(85, 0, 255, 0.05);
  border-left: 3px solid #5500FF;
  padding: 12px 16px;
  margin: 10px 0;
  border-radius: 6px;
  font-size: 13pt;
  line-height: 1.4;
}
.mystery-box strong {
  color: #5500FF;
  font-size: 14pt;
}
.mystery-box em {
  color: #FF922D;
  font-style: italic;
}
.subtitle {
  color: #666;
  font-size: 12pt;
}
.progress-container {
  background: #F0F5FF;
  border-radius: 20px;
  height: 35px;
  margin-top: 15px;
  overflow: hidden;
  display: flex;
}
.progress-understood {
  background: #5500FF;
  width: 70%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 11pt;
  font-weight: 600;
}
.progress-discovering {
  background: #FF922D;
  width: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 11pt;
  font-weight: 600;
}
.progress-mysterious {
  background: #CCCCCC;
  width: 10%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #333;
  font-size: 11pt;
  font-weight: 600;
}
.truth-box {
  padding: 25px;
  background: #F9F9FF;
  border: 2px solid #5500FF;
  border-radius: 8px;
  font-size: 15pt;
  line-height: 1.6;
}
.truth-box strong {
  color: #5500FF;
  font-size: 16pt;
}
</style>

<div class="left">

<div class="mystery-box">
<strong>🔍 Emergence at Scale</strong><br>
• At ~100B params: reasoning <em>suddenly</em><br>
• At ~1T params: deception emerges<br>
<span class="subtitle">Can't predict what's next</span>
</div>

<div class="mystery-box">
<strong>🧠 In-Context Learning</strong><br>
• Shows 3 examples → Learns task<br>
• Zero parameter updates<br>
<span class="subtitle">Multiple theories, no consensus</span>
</div>

<div class="mystery-box">
<strong>🌌 Superposition</strong><br>
• One neuron = multiple concepts<br>
• More concepts than neurons<br>
<span class="subtitle">High-dimensional geometry</span>
</div>

<div class="progress-container">
  <div class="progress-understood">✅ 70%</div>
  <div class="progress-discovering">🔬 20%</div>
  <div class="progress-mysterious">❓ 10%</div>
</div>

</div>

<div class="right">
<div class="truth-box">
<strong>The Revised Truth:</strong><br><br>
It's mathematics—just mathematics so intricate we're still reverse-engineering it.<br><br>
Like discovering calculus to explain planetary motion, we're finding the equations that explain LLMs.
</div>
</div>

---

## From Math to Reality: LLMs Excel at Coding

<style scoped>
section {
  font-size: 15pt;
}
.intro-statement {
  text-align: center;
  font-size: 20pt;
  color: #5500FF;
  font-weight: 500;
  margin: 20px 0 40px 0;
  padding: 20px;
  background: #F0F5FF;
  border-radius: 8px;
}
.stat-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin: 20px 0;
}
.stat-box {
  background: #F9F9FF;
  border-left: 4px solid #5500FF;
  padding: 18px;
  border-radius: 6px;
}
.stat-box h4 {
  color: #5500FF;
  font-size: 16pt;
  margin: 0 0 10px 0;
}
.stat-box .big-number {
  font-size: 32pt;
  font-weight: bold;
  color: #5500FF;
  line-height: 1;
  margin: 8px 0;
}
.stat-box .detail {
  font-size: 12.5pt;
  color: #666;
  margin: 3px 0;
}
.stat-box .highlight {
  font-size: 13pt;
  color: #000;
  font-weight: 500;
  font-style: italic;
  margin-top: 6px;
}
.stat-box .caveat {
  font-size: 10pt;
  color: #FF922D;
  font-style: italic;
  margin-top: 8px;
  padding: 5px 8px;
  background: #FFF8F0;
  border-radius: 4px;
}
.slide-sources {
  font-size: 8pt;
  color: #888;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #E0E0E0;
  line-height: 1.4;
  text-align: center;
}
.closing-statement {
  text-align: center;
  font-size: 18pt;
  font-weight: 600;
  margin-top: 25px;
  padding: 15px;
  background: linear-gradient(135deg, #5500FF 0%, #00B6FF 100%);
  color: white;
  border-radius: 8px;
}
</style>

<div class="intro-statement">
In 2025, AI doesn't just help with code—it's transforming software engineering
</div>

<div class="stat-grid">

<div class="stat-box">
<h4>🚀 SWE-bench Breakthrough</h4>
<div class="detail">2023: <strong>4.4%</strong> of GitHub issues solved</div>
<div class="detail">2025: <strong>78.8%</strong> solved autonomously</div>
<div class="highlight">16x improvement in one year</div>
</div>

<div class="stat-box">
<h4>💼 Enterprise Adoption</h4>
<div class="detail">Google & Microsoft: <strong>30%</strong> AI code</div>
<div class="detail">Meta: Targeting <strong>50%</strong> in 2026</div>
<div class="highlight">256 billion lines in 2024</div>
</div>

<div class="stat-box">
<h4>⚡ Developer Speed</h4>
<div class="detail"><strong>55%</strong> faster on routine coding tasks¹</div>
<div class="detail"><strong>126%</strong> higher output (enterprise study)²</div>
<div class="highlight">Example: 2:41 → 1:11 min per task³</div>
<div class="caveat">
📊 Results vary by task type, tool, and developer experience
</div>
</div>

<div class="stat-box">
<h4>💰 Business Impact</h4>
<div class="detail">Booking.com: <strong>30%</strong> higher throughput</div>
<div class="detail">IBM: <strong>$4.5B</strong> savings by 2025</div>
<div class="highlight">39% more code merges</div>
</div>

</div>

<div class="slide-sources">
¹ GitHub Copilot Research (2023, n=95) · ² McKinsey Digital Survey (2024, n=2000+) · ³ Harvard Business School experiment (2023)
</div>

<div class="closing-statement">
The evidence is compelling: AI coding assistants significantly boost developer productivity across multiple independent studies
</div>

---

<!-- _class: bg-purple -->

## Recommended Reading 📚

<style scoped>
.books-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 40px;
  margin-top: 50px;
  padding: 0 40px;
}

.book {
  flex: 0 1 280px;
  text-align: center;
}

.book img {
  width: 100%;
  height: 420px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.book img:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5);
}

.book-title {
  margin-top: 16px;
  font-size: 16pt;
  font-weight: 600;
  color: white;
  line-height: 1.3;
  white-space: nowrap;
}

.book-author {
  margin-top: 6px;
  font-size: 13pt;
  color: rgba(255, 255, 255, 0.85);
  font-weight: 400;
}
</style>

<div class="books-container">
  <div class="book">
    <img src="Files/What Is ChatGPT Doing - Stephen Wolfram" alt="What Is ChatGPT Doing book cover">
    <div class="book-title">What Is ChatGPT Doing?</div>
    <div class="book-author">Stephen Wolfram</div>
  </div>

  <div class="book">
    <img src="Files/Not Artificial, Not Intelligent - Django Beatty.jpg" alt="Not Artificial, Not Intelligent book cover">
    <div class="book-title">Not Artificial, Not Intelligent</div>
    <div class="book-author">Django Beatty</div>
  </div>

  <div class="book">
    <img src="Files/Vibe Coding - Gene Kim, Steve Yegge.jpg" alt="Vibe Coding book cover">
    <div class="book-title">Vibe Coding</div>
    <div class="book-author">Gene Kim & Steve Yegge</div>
  </div>
</div>

---

![bg](Files/cc-this-pres.png)

<style scoped>
.text-overlay {
  position: absolute;
  bottom: 60px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(255, 255, 255, 0.95);
  padding: 20px 35px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  text-align: center;
  font-size: 20pt;
  color: #333;
  font-weight: 500;
  max-width: 80%;
  z-index: 10;
}
</style>

<div class="text-overlay">
... and yes, Claude Code was highly involved in the making of this presentation 🤖 😉
</div>

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

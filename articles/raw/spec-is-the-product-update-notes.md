---
title: Update notes — The Spec Is the Product
purpose: Working input for revising the-spec-is-the-product article (Claude Code x Fable, local)
created: 2026-07-18
author: Claude (research + synthesis), for Martin Rosén-Lidholm
sources:
  - Simon Wardley LinkedIn post (repost via Charly Wargnier, ~2026-07-16, screenshot transcription)
  - Rewilding Software Engineering, Tudor Gîrba & Simon Wardley (feenk/Medium, 2025, CC BY-NC-SA 4.0)
  - Mapping Moldable Development, book.gtoolkit.com/mapping-moldable-development-59974yztvzadec0whbcsp3np5
  - the-spec-is-the-product.docx (Drive, owner cj@galaxi.tech, read 2026-07-18)
  - every-decision-gets-made.md (Emil, vault)
  - chronosfactory.md, ChronosHub Engineering Strategy 2026-2027.md (vault)
tags: [article-update, spec-driven, moldable-development, rewilding, wardley, agentic-engineering]
---

# Update notes: "The Spec Is the Product" x Rewilding / Moldable Development

## 0. Correction of record

The "Simon and Gabor" reference is Simon Wardley and **Tudor Gîrba** (feenk, Glamorous Toolkit). The work is *Rewilding Software Engineering* (written in the open, Medium/feenk, Feb 2025 onward, CC BY-NC-SA 4.0), which proposes **Moldable Development**: creating contextual micro tools for systems too large to fully grasp. Chapter 3 introduces **ttA (time to Answer)** and **ttQ (time to Question)**. Gîrba coined the initial idea; both stress it is the work of a collective at feenk over ~15 years. Canonical entry: https://medium.com/feenk/rewilding-software-engineering-900ca95ebc8c and https://moldabledevelopment.com/

## 1. Transcription: Wardley's LinkedIn post (trigger for this thread)

> Simon Wardley, reposted from Charly Wargnier, ~2 days before 2026-07-18:
>
> This is better than the dreadfully ill-informed dross of needing fewer software engineers that Silicon Valley has forced on us over the last couple of years.
>
> People starting to question what the role of engineering is. Attaboy! You go get 'em!
>
> If we're very lucky, it won't take more than a few years for the hordes of prognosticators to realise that software engineering is actually a craft and not an engineering topic. It, of course, should be an engineering topic, but we are constrained by the use of non contextual tools (except in the area of TDD where all test suites are contextual. Hint, tests are small tools with inputs, outputs and transformations. TDD is the one bit of the software process which is engineering by nature).
>
> Alas the standard tools that we have had to endure are little more than glorified text editors and this constraint forces us into reading code in order to understand it. Reading code is a highly ineffective approach to understanding. For over a decade, it has mostly been bankrupt as a method for any system of significant size. And no, the solution is not to use a standard tool with an LLM and get the LLM to read it for you. That doesn't get you to understanding, it just creates more dependency.
>
> Eventually, give it a decade or two or three, they might even start to realise that we don't even measure the two most important metrics that we need - ttA (time to Answer) and ttQ (time to Question).
>
> There is hope. But alas, I suspect that is the same hope that digital sovereignty discussions would finally stop being swamped by stories and territorial concerns, and start actually looking at the other landscapes (technological, economic, political and social) that we compete in. If you want to "own" (in terms of territorial location) the entire stack, I can guarantee you that such isolation will bring a future of irrelevance and relative poverty in a highly interconnected world.
>
> In the meantime, I expect to see lots more "use our standard tool, it has added LLM" along with oodles of questionable metrics dreamt up in the coffee shops of Silicon Valley and rants of people saying the "stack" has to be run in our country for reasons of sovereignty.
>
> Please don't send me books based upon these premises to read, review and comment on. Normally, I'd be delighted and honoured but I've just had to wade through another pile of ... well, I suppose to not be worth the paper it is printed on, it has to first be printed ... covering China, Supply Chains and the Sovereignty question. Frankly, I'm fed up with the lack of original thought combined with a deficit of good research. I suspect LLMs have got a lot to answer for here, even with good editors who can dress it up.
>
> On Questions and Answers ... https://lnkd.in/e5DMXduW
> Sovereignty and Landscape ... https://lnkd.in/eXqzTUai

Relevant fragments for the article: reading code is bankrupt as understanding for systems of significant size; an LLM reading code for you creates dependency, not understanding; TDD is the one contextual/engineering part of the process; ttA/ttQ as the unmeasured metrics.

## 2. Rewilding Software Engineering: what it claims (verified)

- Software engineering is primarily a **decision-making activity about systems too large to fully grasp**.
- You can't speed up reading by 500x, but you can improve **decision making** by that factor; the change of perspective starts with asking why we read code and whether we need to read it at all.
- The answer is **Moldable Development**: constantly create new **contextual micro tools** that synthesize information, which is then codified into a model of the system.
- On LLMs: they are **"coherence engines, not truth engines"** — producing what sounds plausible, not what is accurate. (Direct ally for the Rung 2½ section.)
- Aimed especially at legacy: recovering understanding of systems whose intent got buried in code (Ch. 2 case study: recovering a data lineage to modernize a legacy system).
- Written mainly for decision makers of any stripe (engineers, PMs, CTOs, CEOs) dealing with systems they must ask and answer questions about.

## 3. Mapping Moldable Development (book.gtoolkit.com page): careful study

### What the page says

Wardley Map anchored on a **decision about a system** (any scope, technical detail to business concern). The chain beneath:

decision → needs **assessment** → relies on **explorations** → enabled by **conversations** (human↔human and human↔system) → entail **information** → gathered through a **development experience** that synthesizes via concrete **tools built out of the system**.

Core proposition: **replace manually created views (manual inspection) with automatically generated, problem-specific views**. "Much like data science, only applied to software."

Two justifications:
1. Developers spend more than half their time reading a system too large to be understood manually; manually produced pictures **"constitute beliefs rather than accurate engineering tools. And beliefs are not appropriate for any decision making."**
2. Automating information-gathering reduces risk and frees energy for experimenting and acting, enabling hypothesis-driven decisions for every problem.

Scale claim: not dozens of IDE extensions but **thousands of contextual tools per system**, built whenever a problem "is not comfortable enough," multiple times a day per developer. Rigid environments' plugin mechanisms cover *some* problems; MD claims applicability to *all* problems, so tool creation must be embedded in the development flow.

Two roles:
- **Facilitator** (blue, technical): builds the tools.
- **Stakeholder** (red): ties tools to a question or hypothesis tied to value; turns answers into decisions and follow-up actions. "Tools are only meaningful when they relate to a question or hypothesis that is tied to value."

The moldable environment exists to make per-problem tool creation economically viable. The loop closes: generated contextual views create a new feedback loop for decisions based on accurate information, enabling new processes.

### The Wardley read

- One classic play: **commoditize the component below (the moldable environment) to enable industrialized genesis above (thousands of contextual tools)**. Same inversion as the ChronosFactory bet applied to the read side: they commoditize the production of *understanding* the way the factory commoditizes the production of *code*. In both, the durable investment is the environment/harness; the individual artifact (a contextual view, a generated file) is disposable.
- Structural weakness: their enabling component sits in custom-built territory. MD is gated on GT/Pharo, a niche substrate with heavy adoption inertia. Wardley doctrine predicts the practice spreads only when moldable tooling commoditizes into mainstream stacks. **LLM agents are that commoditization vector**: an agent builds a throwaway contextual view over any codebase in any stack in minutes, no Smalltalk image required. feenk's newer "Moldable Agent Harness" chapters show they see the wave coming for their own moat.
- Strategic conclusion: **adopt the pattern, skip the platform.** The transferable patterns: Contextual View, Throwaway Analysis Tool, Tooling Buildup, Project Diary, Facilitator/Stakeholder pairing.

## 4. How this locks into the article (the load-bearing synthesis)

### 4.1 Same enemy, opposite arrow direction

- MD's "manually produced pictures are beliefs" = the article's "the documentation lies" = **representational redundancy**: a hand-maintained representation of a system that nothing holds coherent with the system.
- MD's cure: **derivation at read time** (regenerate the view from the system on demand, so it can't be stale).
- The article's cure: **derivation at build time** (never let the representation exist independently, so it can't drift).
- Same move, opposite direction: they derive views *out of* the system; the article derives the system *out of* the spec.
- One-sentence ammunition: **MD proves the industry already accepts deterministic derivation as the cure for drifted read-side representations; this article is only the symmetric case for the write side.**

### 4.2 Location in the four-store model (via every-decision-gets-made.md)

Emil's ground-vs-demand distinction: reading more ground does not reduce specification demand; it only makes judgment decisions more *makeable*. Placed in the four stores (encoded / mechanically verified / judgment / escaped):

- **Moldable Development is ground-illumination technology for the judgment store.** It lowers ttA on inspecting ground, so judgment decisions get made faster and on accurate information instead of beliefs. It never moves a decision into the encoded or mechanically verified stores.
- **Spec-derivation shrinks the judgment store's contents.** It relocates decisions into encoded (the spec) and mechanically verified (the generator, the compile errors, the generated facts).
- Complementary and now precisely locatable: **MD optimizes the economics of the store you can't empty; spec-derivation empties the stores that can be emptied.**

### 4.3 In the article's architecture, the two collapse

- MD applied to arbitrary legacy must reverse-engineer the semantic frame for every view.
- In a spec-defined, event-sourced system, stakeholder-facing contextual views are largely **derivable from the same spec**: a state-view slice literally *is* a specified contextual view.
- The chronosfactory CTA ("the same slices that specified the build monitor the run") = **Moldable Development over the event store with the Facilitator role partially absorbed into the generator.** Their map ends with "this feedback loop enables new processes"; the event model is what makes that loop deterministic rather than artisanal.
- Possible article extension: "the spec is the product" extends to the read side; the tools are derivable too.

### 4.4 Wardley's post = the Rung 2½ argument in different clothing

- "The solution is not to get the LLM to read it for you; that creates dependency, not understanding" = "another opinion is not an oracle."
- "Coherence engines, not truth engines" is a quotable ally (attribute to Gîrba/Wardley, Rewilding Software Engineering).
- Shared axis: the fix is structural (deterministic generator, contextual tool), never a stochastic intermediary.

### 4.5 The TDD concession is the bridge

Wardley concedes exactly one part of software is engineering by nature: tests, because they are contextual small tools with inputs, outputs, transformations. The workbench's **115 diskless xUnit facts are machine-manufactured contextual micro tools, one per requirement, derived from the spec in the same compiler pass**. The article didn't just adopt the one part Wardley calls engineering; it made that part a compiled output.

### 4.6 ttA/ttQ mapping for the workbench

- "Does any site fail to handle event X?" → one build; CS8795 names the debtor method. ttA ≈ build time.
- "Does behavior match requirement Y?" → test runner by requirement name, under eight seconds.
- ttQ drops too: the spec is small enough that new questions are cheap to pose against it.
- Deeper claim: Rewilding assumes the system stays too large to grasp and tools must adapt to it; the article claims a graspable-by-construction core is achievable for the provable stratum. Both true, stratum by stratum. Saying so preempts the "but legacy" objection.

### 4.7 Rewilding owns the backward motion the article doesn't cover

The needle from code to spec has two motions:
- **Forward** (article's scope): spec → deterministic derivation → ProdFac.
- **Backward** (Rewilding's scope): the ~700 production slices whose intent lives only in The Legendary Code. Blueprint harvesting is a pure ttA problem on a system too large to grasp; MD's home turf.
- ChronosHub operating model for harvesting: **Stakeholder** = Snorri + PMs asking "which events does this module actually emit, fold on, depend on"; **Facilitator** = agents building throwaway contextual views over the estate, one per question, discarded after the answer, surviving knowledge codified into event models rather than into anyone's head. MD's Tooling Buildup + Throwaway Analysis Tool patterns at agent cost.
- Rewilding in, derivation out. Micro tools harvest the spec; the generator makes the spec load-bearing.

## 5. How the needle moves (recap from earlier in the thread)

The needle moves on the **verifier** axis, not the authoring axis. Everyone else moving "from code to spec" moves prose leftward while keeping an LLM as the compiler; the article moves strata across the repo boundary.

1. **Keep eating strata.** Done: vocabulary, scenarios, dispatch. Next candidates by the same criterion (pure function of the spec, no decision content): projection fold plumbing, serialization/API surface, OpenAPI, TypeScript client types. Metric: lines in git that restate the spec; drive toward zero; publish the ledger each time (2,754 out / 708 in).
2. **Spec as the only legal change surface, socially and mechanically.** Workbench: compiler enforces it. ChronosHub: review norm; a PR hand-editing anything derivable bounces to a spec edit plus regeneration. Protected regions died because the repo's social contract beat the comment fence.
3. **CI asserts `artifact == f(spec, generator)` as an invariant.** The round-trip determinism test is the entire warranty; without it, rung 2 with extra steps.

Microtools framing (kept from the earlier misidentified thread; still valid as context): the microtool phenomenon (Russinovich's vibe-coded LinkedIn formatter, Willison's tools.simonwillison.net) is demand-side proof that construction commoditized. Disposable C-class code needs no Shore obligation; the prompt is spec enough and the code is landfill. When code must live for years, the spec is the only artifact worth owning and the code should stop being source at all. Note: distinct from Gîrba/Wardley's contextual micro tools, which are *read-side instruments*, not shipped products; do not conflate the two in the article.

## 6. Concrete edits to the draft

1. **Track-changes residue, paragraph one:** "Knowing that the codeit is of good enough quality is now the expensive partright is." Resolve to one sentence.
2. **Dangling unattributed quote** in "Who transforms, what verifies": `"Each rung up the ladder means ..." .` Needs a source or rewrite as own prose.
3. **Slug mismatch:** byline URL says `representational-redundancy`, title says spec-is-the-product. Pick one.
4. **Em dash density:** draft violates the external-audience style rule; replace most with colons, semicolons, parentheses.
5. **Add Rewilding/MD as corroboration** in "The enemy has a name" or Rung 2½: reading/reviewing code is the bankrupt layer (cite Gîrba/Wardley; "coherence engines, not truth engines"), then draw the distinct conclusion: they lower the cost of answering questions about code; this article deletes the strata about which questions need asking.
6. **Add the symmetric-case sentence** (§4.1) where the article names representational redundancy.
7. **Optionally add the ttA/ttQ reading** of the workbench results (§4.6) to "What happened when I did it": the seam doesn't just scream, it answers in build-time.
8. **Honest-disagreement paragraph** (§4.6 last bullet) in "Where I might be wrong" or nearby, to preempt "but legacy."
9. **Launch-post angle:** Wardley is a 1st-degree connection who just publicly asked for original thought on exactly this. Frame the announcement around ttA and the write-side symmetry; do not send him a book.

## 7. Source links

- Rewilding Software Engineering (Ch. 1 entry): https://medium.com/feenk/rewilding-software-engineering-900ca95ebc8c
- Moldable Development book site: https://moldabledevelopment.com/
- Mapping Moldable Development: https://book.gtoolkit.com/mapping-moldable-development-59974yztvzadec0whbcsp3np5
- feenk labs (chapter overview incl. ttA/ttQ in Ch. 3): https://feenk.com/labs
- Draft under revision: the-spec-is-the-product.docx (Drive, id 1ZIHJDL6QFSCO-2nd3xVsz1YuWahQ9EIA)

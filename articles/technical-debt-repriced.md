---
title: "Did technical debt just get repriced massively downward?"
description: "A spec-first AI refactoring case study inverts review economics: neglected codebases appreciate, person-month modernization depreciates."
created: 2026-08-15
status: draft
venue: linkedin
---
# Did technical debt just get repriced massively downward?

An AI coding agent dismantled a core architectural invariant across 189 files in a 717k-line production codebase. No human code review. No test oracle. Three days, USD 2,430.

The kind of change the old playbook would scope as "rewrite the system", senior-team quarters at high six figures loaded, priced as a sprint task.

One case study: an existence proof, not a trend. But if it replicates, every neglected codebase with valuable domain logic just appreciated, and every business model selling person-months of modernization just depreciated.

What happened: a 717,725-line production TypeScript application needed a change judged infeasible by incremental refactoring: removing the guarantee that a UI panel stays open for the duration of an AI request; a streaming generation must survive the panel closing and reattach cleanly. The classic playbook (Feathers, Fowler): test harness first, strangler fig, months of grind. Or you declared it impossible.

Instead: the agent wrote a formal specification, refined it against the source over 14 audit cycles, froze it, implemented in three atomic segments, then verified the code against it over 17 more cycles. 201 defects caught across those 31 audit passes, before any human ran the program. Stopping rule: two consecutive passes with zero findings. Roughly thirty usage sessions since release: no bug observed.

The headline is not "AI did a huge refactor." The headline is that review economics inverted.

Human review cost scales with diff size. Audit-against-frozen-spec cost scales with spec size.

That is why large changes were unreviewable and rewrites felt safer.

This was not autonomy, it was engineering. The scarce inputs were all human judgment, just relocated: name the invariant precisely, judge that dismantling beat refactoring, design a convergence protocol with an empirical stopping rule. Then the discipline to not read a 35,000-line diff and trust the process instead.

Caveats, most stated by the author: n=1, self-reported, and he sells the agent used, so discount accordingly (the 1,500 published log pages are the counterweight). Two he does not price: the codebase was his own, agent-built and well-tested, the opposite of neglected legacy; and behind the USD 2,430 sits a 250,000-character harness of accumulated rules. The spec work is real cost, but it is one-time capex against domain logic you already own, not recurring person-month burn.

If it replicates on genuinely ossified code, the investment logic writes itself. Codebases with strong domain logic and weak code are undervalued assets. The "competitors cannot rebuild this" moat weakens; the domain-knowledge moat strengthens. In diligence the checklist flips: stop discounting for code quality, start pricing whether the invariants are recoverable.

So: time to buy neglected vertical SaaS, agent-refactor, expand margins? I think the market has not noticed yet.

🔗 in the comments.
___
🔗 in the comments

Abenhaim, J. (2026). Specification-first convergence with an AI coding agent. arXiv:2608.12440. https://arxiv.org/abs/2608.12440, surfaced via my Daily D4 Digest https://martinrl.github.io/chronograph/digest/2026-08/2026-08-15

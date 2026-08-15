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

It is one case study, so treat it as an existence proof and a protocol worth replicating, not a trend. But if it replicates, every neglected codebase with valuable domain logic just appreciated, and every business model built on selling person-months of modernization just depreciated.

Here is what happened. A production TypeScript application, 717,725 lines, needed a change the author judged infeasible by incremental refactoring: removing the guarantee that a UI panel stays open for the duration of an AI request, so a streaming generation survives closing the panel and reattaches cleanly on reopen. The classic playbook (Feathers, Fowler) says: build a test harness first, strangler fig, feature flags, a small senior team grinding for months. Or, more honestly, you declared the feature impossible and the roadmap routed around it forever.

Instead: the agent wrote a formal specification, refined it against the source over 14 audit cycles, froze it, implemented it in three atomic segments (it refused a partial implementation, citing the spec's atomicity requirement), then verified the code against the frozen spec over 17 more cycles. 201 defects caught and fixed across those 31 audit passes, before any human ran the program. Stopping rule: two consecutive verification passes with zero findings. Roughly thirty usage sessions since release: no bug observed.

The headline is not "AI did a huge refactor." The headline is that review economics inverted.

Human review cost scales with diff size. Audit-against-frozen-spec cost scales with spec size.

That asymmetry is exactly why large changes were unreviewable and rewrites felt safer. Break it and you change what software changes cost, structurally, not incrementally.

Now the part I care most about: this was not autonomy, it was engineering. The scarce inputs were all human judgment, just relocated. Someone had to name the invariant precisely, judge that dismantling beat refactoring, recognize that "reattach with no loss or duplication" is an exactly-once semantics problem, and design a convergence protocol with an empirical stopping rule borrowed from classical QA. Then hold the discipline to not read a 35,000-line diff and instead trust the process they designed.

Civil engineering earned that kind of process-trust through decades of failure data; this protocol has one data point. The aspiration is right, the certification is not there yet. But the winning profile is already visible: spec-literate architects who design verification protocols instead of reviewing pull requests will run circles around organizations still measuring review throughput.

Caveats, because they matter, and the author states most of them himself: n=1, self-reported, and he sells the agent used, so discount accordingly (the 1,500 pages of published session logs are the counterweight). Two more he does not price: the codebase was his own, agent-built and well-tested from day one, the opposite of neglected legacy; and behind the USD 2,430 sits a 250,000-character harness of rules accumulated over years. The spec work is real cost. But it is one-time capital expense against domain logic you already own, not recurring person-month burn.

If it replicates on genuinely ossified code, the investment logic writes itself. Codebases with strong domain logic and weak code are undervalued assets. The moat of "our competitors cannot rebuild this" weakens, while the moat of accumulated domain knowledge strengthens. In diligence the checklist flips: stop discounting for code quality, start pricing whether the invariants are recoverable, meaning does anyone left know what the system must guarantee, even if nobody knows how it does it. And the losers are the businesses whose unit of sale is the person-month of migration work.

So: time to buy neglected vertical SaaS, agent-refactor, and expand margins? I think the market has not noticed yet.

Case study 🔗 in the comments.
___
🔗 in the comments

Abenhaim, J. (2026). Specification-first convergence with an AI coding agent. arXiv:2608.12440. https://arxiv.org/abs/2608.12440, surfaced via my Daily D4 Digest https://martinrl.github.io/chronograph/digest/2026-08/2026-08-15

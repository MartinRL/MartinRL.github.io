---
title: "Tight, Loose, Tight: Why My Software Factory Is Cheap"
description: "A management explanation of the software factory I have built on emlang and xmlang. Writing code has been made cheaper three times and the bill barely moved, because nobody fixed what the system meant. Fix meaning first, let the machine build, verify against one approved shape."
created: 2026-10-03
draft: true
tags:
  - software-factory
  - leadership
  - cost
  - ai
  - management
  - emlang
  - xmlang
aliases:
  - TLT and the factory
  - Tight loose tight
---

> [!abstract] TL;DR
> Fifty years of better tools have not made software cheap, because writing it was only the visible cost. Writing has been compressed repeatedly: offshoring, frameworks, now AI code generation. Each time the bill fell less than the hourly rate did, because the expensive part that survived every compression was deciding what the system should do, keeping that decision stable while people and code changed, and finding out, late, that the two had drifted apart. My factory attacks exactly that cost, and the cleanest way to explain how is a leadership model from Norway: tight, loose, tight. Tight on meaning: what the system must do is written in two small languages, emlang and xmlang, precise enough that a machine checks them. Loose on how: the machine builds, and is free in how. Tight on outcome: there is one approved way the result may be shaped, so verification is automatic and code review is unnecessary. The cost of a system collapses toward the cost of deciding what it means. That is the only cost that was ever worth paying. The best-funded attempt to do this with prose specifications, Tessl, repositioned itself within a year of launch; the whole difference is whether the front is actually tight.

> [!tip] If you lead a company
> Stop budgeting for building. Budget for meaning: the workshop that fixes what the system does, and the person who owns that decision afterwards. Everything else is becoming a utility.

## The bill nobody can explain

Ask a CFO what software costs and you get a number. Ask why, and you get a story about complexity. Bent Flyvbjerg's project database, the largest of its kind, says the story is wrong in a specific way: roughly one in five IT projects overruns its budget by more than half, and the ones that do overrun by 447 percent on average [1]. That is not complexity. That is a system that cannot tell you where it stands until it is too late to matter.

Fred Brooks explained the structure of the problem in 1986 [2]. Software has two kinds of difficulty: the essential kind, deciding what the system should do and keeping that decision coherent, and the accidental kind, the tools and plumbing used to express it. He predicted no single tool would deliver a tenfold improvement, because tools only attack the accidental part. Forty years later, Moseley and Marks measured where the accidental part comes from and found most of it was self-inflicted: state and control flow the business never asked for [3]. Both were right. Every productivity tool since, including AI code generation, has made the accidental part cheaper. The essential part, meaning, has been left to documents, meetings and memory.

So most of what a company pays for in software is a chain of translation between someone who knows what the business needs and something that runs: requirements documents, meetings to interpret them, estimates, reviews, test cycles, acceptance demos, rework when the interpretation turns out wrong, and then maintenance, which is the same chain run again, slower, by people who were not in the room the first time. Every link exists because nobody fixed the meaning of the system in a form that could be checked. So people check it, repeatedly, by hand, and bill for it.

## A leadership model that happens to describe the fix

Tight, loose, tight is a leadership model from the Norwegian agile scene, inspired by scrum and used at companies like NAV and Telenor to explain how managers could change their style [4]. It is easy to hold in your head. Be tight at the start: purpose, goal and boundaries are fixed and agreed. Be loose in the middle: the team is trusted to decide how, and left alone to do it. Be tight at the end: results are checked against what was agreed, and the organisation learns from the gap. The older academic form is Sagie's loose–tight model, which found that a leader can be loose in substance while tight on framework, and that the two reinforce rather than contradict each other [5].

The insight most people miss is that the loose middle is only safe because both ends are tight. Loosen the start and the team drifts. Loosen the end and nothing is learned. Managers who get this wrong fall into one of three other shapes, and each has a software method that looks exactly like it.

**Loose, loose, loose.** No fixed purpose, no frame, no check. In software this is prompting an AI until something appears on screen. Lovable and Replit each run at roughly half a billion dollars of annual revenue on this shape [6], and it is wonderful for a prototype and ruinous for a system of record, because the meaning was never fixed, so every change is a fresh guess.

**Tight, tight, tight.** The visionary who cannot let go. In software this is low-code and its enterprise ancestors: every screen laid out, every rule a widget, every exception a special case. Microsoft's Dynamics platform gives developers roughly forty approved screen patterns and a checker to police the choice [7]. It is tight on form and loose on meaning, which is backwards, and it is why these platforms are slow, brittle and dependent on specialists.

**Loose, tight, loose.** The project manager's shape: vague goals, rigid process, acceptance by demonstration. This is how most enterprise software is delivered, and it is where Flyvbjerg's numbers come from. Process is what organisations buy when the start is loose. It is expensive precisely because it is compensating for something else.

The same map, applied to what you are being sold this year, is the most useful thing in this article.

| Profile | The pitch | Examples | Where it breaks |
|---|---|---|---|
| Loose, loose, loose | "Describe it and it appears" | Vibe-coding builders (Lovable, Replit, Bolt); autonomous agents handed a ticket and left alone | Nothing fixed the meaning and nothing checks the result. Right for prototypes, lethal for systems of record |
| Loose, tight, loose | "Discipline for agents": write a spec, then a plan, then a task list, then let it build | Spec-driven toolkits (GitHub Spec Kit, AWS Kiro), agile role-play frameworks that give agents job titles [14] | The spec is prose no machine can check, the ceremony is the product, and "done" is judged by tests the agent wrote for itself. Project management, re-created for robots. See the cautionary tale below |
| Tight, tight, tight | "AI inside the platform you already own" | Copilots inside low-code and ERP builders (Power Platform, Dynamics, Mendix, OutSystems) | Tight on form, loose on meaning. The agent types faster inside a cage that still needs specialists to open it |
| Tight, loose, tight | "Fix meaning, free the machine, verify the shape" | Palantir's AI FDE with ontology proposals [13]; test-first agent loops that restart until the suite passes [16]; my factory | Holds. The three differ in what they tighten: Palantir an ontology, test-first loops a test suite, the factory the business meaning and one approved shape. Only the last two ends are legible to a CEO |

One caution on the last row. A loop that restarts an agent against the same instructions until something passes is tight, loose, tight only if what it passes was fixed before the agent started and can be checked without the agent's help. If the agent writes the test and judges the test, the loop is loose, loose, loose with persistence.

## The cautionary tale: $125 million of loose front

Tessl is the company I would have founded if I believed prose could be a source of truth. Founded in London in 2024 by Guy Podjarny, who built Snyk, it raised about $125 million on the boldest version of spec-driven development: the specification is the only thing humans maintain, and code is a disposable artifact regenerated from it [15]. That is the two-stage rocket as a venture thesis. One word in it was wrong.

The specifications were prose. In September 2025 Tessl shipped a framework in closed beta and a registry of more than 10,000 specs telling agents how to use open-source libraries correctly [17]. The framework stayed in beta for most of a year, and its regeneration was not repeatable: ask it twice, get two programs. During 2025 the company paused the framework and removed it from its tooling, and on 29 January 2026 it reframed itself around a skills registry and the governance of agents: who may install what, did it run, audit trail [15].

Read it through the model. The front looked tight: a spec file, a ceremony around it. It was loose, because no machine could check whether a prose spec was complete, consistent, or even the same thing it was yesterday. The middle was loose, correctly. The back was loose too: the guardrails were tests the agent generated from the same prose it was building from, so the thing being checked and the thing doing the checking shared every error. That is loose, tight, loose wearing the clothes of tight, loose, tight, and it failed the way the model predicts: drift at the front, no learning at the back, process as the only product.

Three lessons, each cheap to state and expensive to have learned.

Prose is not a source. If regenerating from the spec gives a different system each time, the spec cannot be the record of truth; the code is, and you are back to maintaining code. Meaning has to be written in something a checker can read.

A fix must be expressible in the spec. When a bug appears and the spec cannot say what is wrong precisely enough to regenerate only the fix, engineers edit the code, the spec goes stale, and the two drift apart. That is the oldest failure in software, under a new label.

The checker must not share the builder's errors. Tests written by the agent from the agent's reading of the spec check the agent against itself. Examples written by the business before the agent starts check the agent against the business.

And the market lesson, for anyone deciding where to spend: what Tessl's customers actually bought was governed context, a registry with versioning, scanning and audit. Companies pay today for control over what their agents know. Nobody has yet paid for a prose compiler, because none works.

My factory is the same bet with the one word corrected. The spec is a small, precise language, not prose: emlang and xmlang are strict enough that a checker refuses ambiguity, and small enough that the whole model of a system fits in a document a business owner can read. Regeneration is repeatable and locked against a reference, so the model is the record of truth and the code really is disposable. The examples are written by the business in the workshop and compiled into the tests, so the checker owes the agent nothing. Same ambition as Tessl's, same architecture in outline, and the three differences sit exactly where tight has to mean tight.

## Where my factory comes from

One word on provenance, because a factory you cannot inspect is a slide, not a claim. My factory is my own work. It runs on two small languages I write and maintain, emlang and xmlang [8], and on Adam Dymitruk's event modeling method for drawing a system as a timeline of what happens in the business [9]. How it works, stage by stage, is in an earlier piece for an engineering audience, the two-stage rocket [10]. This article is about what it does to the cost of software, and why.

## My factory is tight, loose, tight

**Tight on meaning.** Before anything is built, the business and I spend a day drawing the timeline: who does what, what fact that creates, what the business then knows, what decisions follow. The timeline is written down in emlang, which records the facts, the actions and every decision rule with its named reasons for saying no, and in xmlang, which records what each screen shows and lets you do, never where the buttons sit. An automatic checker refuses anything ambiguous. This is where my specification and Tessl's part ways: theirs was prose that no checker could refuse, mine is a language that one does. This is the step that fixes meaning, once, in a form both the CEO and the machine can read. It is the only step that needs senior people in the room.

**Loose on how.** From that point the machine builds. It is free in how it implements each decision rule, free in how it renders each screen within the company's design standards, and free in how it proposes the next change when someone asks for one. Nobody writes a requirements document, nobody schedules a code review, nobody estimates. The loose period is minutes long and covers one slice of the system at a time.

**Tight on outcome.** There is exactly one approved way a slice may be shaped: one action, one set of facts it creates, one way the business state is derived from those facts. The machine's output is checked against a locked reference and against the examples the business gave in the workshop, which were written as tests from the start. If the result deviates, it does not ship. Review collapses to two questions: did it pass, and is the business rule correct. The second question is the only one a human still needs to answer.

In an earlier piece I called this the two-stage rocket [10]. The first stage burns in the workshop and ends at a checked model; the second ignites from that model and lands in the one approved shape. Separation happens at the checker. Rocket engineers know what happens without a clean separation: the first stage is still burning when the second ignites, and it interferes with the trajectory [11]. Prompt-to-code tools ignite the second stage while the first is still burning. That is the whole difference.

Dymitruk's claim for the method is that it removed ninety percent of meetings in the teams that adopted it, and that slices need no code review, only a check that the state is correct and the work landed on time [12]. Those are a practitioner's numbers, not a study. But the mechanism is plain: the meetings existed to re-negotiate meaning, and the meaning is now written down where a machine holds people to it.

## Where the money goes

Put the two side by side and the cost structure inverts.

**Specification.** Before: documents that go stale, interpreted in meetings, billed by the hour. After: one workshop, one checked model, reused for every change. Cost moves to the front and shrinks.

**Building.** Before: the visible line item, and the one AI tools have already compressed. After: near zero. The machine builds from the model, and the first system and the tenth cost about the same to produce.

**Verification.** Before: test cycles, acceptance demos, the overrun tail. After: automatic. The examples given in the workshop are the tests; the one approved shape is the standard. Nothing deviant reaches production, and the checker was not written by the thing it checks.

**Coordination.** Before: the meetings, the status reports, the translation layer between business and technology. After: the model is the shared language, so the translation layer is gone. This is the cost line leaders underestimate most, because it never appears on an invoice.

**Maintenance.** Before: the same chain run again by people who were not there, which is why systems ossify. After: a change is a change to the model, checked and regenerated. The cost of a change is proportional to how much meaning changed, not to how large the system has grown.

The result is that the marginal cost of a well-built information system approaches the cost of a workshop. That sentence sounds like a sales pitch. It is an accounting consequence of fixing meaning at the front and shape at the back. It is also what Brooks said a silver bullet would have to do: attack the essential complexity, not the accidental.

## What does not get cheaper

Three things, and they are where your attention and your budget should go.

Deciding what the business wants is still hard, and the workshop makes that visible rather than easy. Companies that have never had to agree on their own rules discover, in a single day, that they disagree. That is a feature. It used to cost a year.

Someone must own the meaning afterwards. When a rule changes, a named person is accountable for having said so, because the machine will build whatever the model says. This is a senior role, not an IT role. Palantir, the one company that has run this operating model at scale, embeds an engineer at the customer for the first model and then routes every later change through a proposal and approval, at every customer size [13]. The pattern is the same here: the business owns the rule, the factory's engineer is counsel.

Integrations with other systems, legacy or external, remain real work. The factory makes your own system cheap. It does not make your neighbours' systems any less messy.

## Three decisions for a leader

First, move budget from building to meaning. Fund the workshop properly and insist that senior people attend. A day of their time at the start replaces months of everyone else's time later.

Second, staff the owner. Name the person accountable for each system's rules. If you cannot name one, the system should not be built yet.

Third, stop buying process. Status meetings, change boards, acceptance ceremonies exist to compensate for a loose start. Once the start is tight, they are cost without function. Measure lead time from a decided change to a running change instead.

## The one-line version

Software is expensive where meaning is loose and cheap where form is loose. My factory is tight on meaning, loose on form, and allows exactly one shape at the end, so the loose part can be a machine and the tight parts can be a checker and a test suite instead of a management layer.

---

### References

1. Flyvbjerg and Gardner, *How Big Things Get Done* (2023): about 18 percent of IT projects overrun by more than 50 percent, and those projects overrun by 447 percent on average.
2. Brooks, "No Silver Bullet: Essence and Accidents of Software Engineering," *IEEE Computer* (1986).
3. Moseley and Marks, "Out of the Tar Pit" (2006).
4. "The Basics of Tight Loose Tight," Glasspaper: https://www.glasspaper.no/artikkel/utvikling/the-basics-of-tight-loose-tight/
5. Schwartz, Sagie, Zaidman, Hamburger and Teeni, "An empirical assessment of the loose–tight leadership model": https://www.tau.ac.il/~teeni/publications/loose.pdf
6. Lovable's $400M raise at $13.3B after $500M annualized revenue, and Replit near $525M ARR: https://appcoding.com/ai-app-builders-reviewed-lovable-base44-bolt-replit-and-v0-compared/ and https://tech-insider.org/replit-vs-lovable-vs-bolt-new-2026/
7. Microsoft Learn, "Form styles and patterns" for Dynamics 365 finance and operations: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/form-styles-patterns
8. Rosén-Lidholm, xmlang repository (emlang and xmlang specs, linter, RFCs): https://github.com/MartinRL/xmlang
9. Dymitruk, *Event Modeling*: https://eventmodeling.org
10. Rosén-Lidholm, "The Two-Stage Rocket Fills the Hole the Thought-Leaders Identified": [[two-stage-sdd-rocket]], and "The Spec Is the Product": [[the-spec-is-the-product]].
11. Stage-separation failure described in US patent 4,924,775, Integrated two stage rocket: https://patents.google.com/patent/US4924775
12. Dymitruk, Event Modeling talk slides (Skills Matter): "removed 90% of all meetings"; "work in slices, no code reviews (SLA and state correctness only)": https://res.cloudinary.com/skillsmatter/image/upload/v1666065855/bca2sbuv5z3sodwstjvb.pdf
13. Palantir, AI FDE overview and Ontology Proposals: https://www.palantir.com/docs/foundry/ai-fde/overview
14. Fowler, Dushinski and others, "Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl": https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
15. Tessl paused Framework development and removed it from its CLI in 2025, and on 29 January 2026 reframed itself as an Agent Enablement Platform around a skills registry: https://ai.engineer/orgs/tessl and https://codemyspec.com/blog/tessl-review
16. MacManus, "AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers," Latent.Space, 2026-07-01, on Huntley's "everything is a ralph loop": https://www.latent.space/p/aiewf-daily-dispatch-loops
17. Tessl, "Announcing Tessl's Products to Unlock the Power of Agents," September 2025 (Framework in closed beta, Spec Registry with 10,000+ usage specs): https://tessl.io/blog/announcing-tessls-products-to-unlock-the-power-of-agents/

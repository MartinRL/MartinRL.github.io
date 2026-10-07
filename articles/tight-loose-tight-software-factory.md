---
title: Hire Rocket Engineers, Not Rockstar Developers
description: "Tight, loose, tight: a management explanation of why our software factory is cheap, and what it changes about who to hire. Agents have made writing code nearly free and the cost of a product barely moves, because nobody fixed what the system meant. Fix meaning first, let the machine build, verify against one approved shape."
created: 2026-10-03
updated: 2026-10-04
draft: true
tags:
  - software-factory
  - leadership
  - cost
  - ai
  - management
  - event-modeling
  - experience-modeling
  - rocket-engineering
  - rockstar-developer
aliases:
  - TLT and the factory
  - Tight loose tight
---

> [!abstract] TL;DR
> Agents can now write code faster than any team can read it. Building is no longer the constraint; deciding is: what the system should do, keeping that decision stable while people and code change, and finding out, late, that the two have drifted apart. Our factory attacks exactly that cost, and the cleanest way to explain how is a leadership model from Norway: tight, loose, tight. Tight on meaning: what the system must do is written as a model a machine can check. Loose on how: the machine decides how each rule meets the examples the business gave, and how each view is read from the facts. Tight on outcome: one approved shape, verified automatically. The cost of a system collapses toward the cost of deciding what it means. The scarce hire is no longer the rockstar developer. It is the the rocket engineer.

> [!tip] If you lead a company
> Budget for two things. Once: the factory, the domain-specific specification languages and the checkers that hold your meaning (per system cohort), which you cannot buy because they are bonded to your product. Continuously: meaning, the time of the people who decide what the product does and own those decisions afterwards. Everything else is becoming a utility.

## The cost nobody can explain

Ask a CFO what software costs and you get a number: the R&D line, mostly salaries. Ask engineering why it is that big, and you get a story about complexity. Bent Flyvbjerg's project database, the largest of its kind, says the story is wrong in a specific way: roughly one in five IT projects overruns its budget by more than half, and the ones that do overrun by 447 percent on average [1]. That is not complexity. That is a system that cannot tell you where it stands until it is too late to matter.

Fred Brooks explained the structure of the problem in 1986 [2]. Software has two kinds of difficulty: the essential kind, deciding what the system should do and keeping that decision coherent, and the accidental kind, the tools and plumbing used to express it. He predicted no single tool would deliver a tenfold improvement, because tools only attack the accidental part. Forty years later, Moseley and Marks [3] argued that most of the accidental part was self-inflicted: state and control flow the business never asked for. Both were right. Every productivity tool since, including AI code generation, has made the accidental part cheaper. The essential part, meaning, has been left to documents, meetings and memory.

So most of what a company pays for in software is a chain of translation between someone who knows what the business needs and something that runs: requirements documents, meetings to interpret them, estimates, reviews, test cycles, acceptance demos, rework when the interpretation turns out wrong, and then maintenance, which is the same chain run again, slower, by people who were not in the room the first time. Every link exists because nobody fixed the meaning of the system in a form that could be checked. So people check it, repeatedly, by hand, and the product pays for it in headcount and in quarters of roadmap.

Then build time collapsed from weeks to minutes, and the constraint moved. Every link in that chain existed to ration and protect scarce builder time, and that time is no longer scarce. What is scarce now is the capacity of the few people who know what the product should do, and the means of knowing whether what was built is what they decided. Goldratt's rule for a moved constraint is to find the new one and subordinate everything else to it, and his warning is that organisations instead keep the process built around the old one [20]. The rest of this article is that rule applied: effort moves to the front, where meaning is decided, and to the automatic check at the back, and everything in between becomes a machine.

## Where the money goes

By the factory I mean the arrangement the rest of this article describes: what the product should do is written as a model a machine can check, a machine builds from that model, and the result is verified against one approved shape. Here is what that does to the budget, five cost lines, today and with the factory.

| Cost line     | Today                                                                                                  | With the factory                                                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Specification | Documents that go stale, interpreted in meetings, paid for in the time of the people who know the most | Modeled as it is decided, in a checked model that every change extends |
| Building      | The visible line item, and the one AI tools have already compressed                                    | Near zero for your own system. The machine builds from the model, and the hundredth feature costs what the first did; the system does not get harder to add to as it grows |
| Verification  | Test cycles, acceptance demos, the overrun tail                                                        | Automatic. The examples the business gave are the tests, the one approved shape is the standard                                                                                   |
| Coordination  | Meetings, status reports, the translation layer between business and technology                        | Shrinks to deciding the model and owning it. The model is the shared language                                                                                                    |
| Maintenance   | The same chain run again by people who were not in the room, which is why systems ossify               | A change to the model, checked and regenerated                                                                                                                             |

Two things to notice. Coordination is the line leaders underestimate most, because it never appears in the budget; it is spread across everyone's calendar. And after the change, the cost of a change is proportional to how much meaning changed, not to how large the system has grown.

The result is that the marginal cost of a well-built information system approaches the cost of deciding what it means. That sentence sounds like a sales pitch. It is an accounting consequence of fixing meaning at the front and shape at the back, and it is what Brooks said a silver bullet would have to do: attack the essential complexity, not the accidental. The rest of this article is how.

## The leadership model that makes it possible

Tight, loose, tight is a leadership model from the Norwegian agile scene, inspired by scrum and used at companies like NAV and Telenor to explain how managers could change their style [4]. At Telenor Denmark it went far enough that the company's HR director won the Danish HR prize in 2021 for making it the shared language of leadership there [19]. It is easy to hold in your head. Be tight at the start: purpose, goal and boundaries are fixed and agreed. Be loose in the middle: the team is trusted to decide how, and left alone to do it. Be tight at the end: results are checked against what was agreed, and the organisation learns from the gap. The older academic form is Sagie's loose–tight model, which found that a leader can be loose in substance while tight on framework, and that the two reinforce rather than contradict each other [5].

The insight most people miss is that the loose middle is only safe because both ends are tight. Loosen the start and the team drifts. Loosen the end and nothing is learned. Managers who get this wrong fall into one of three other shapes, and everything you are being sold this year is one of the four.

| Profile | The pitch | Examples | Where it breaks |
|---|---|---|---|
| Loose, loose, loose | "Describe it and it appears" | Vibe-coding builders (Lovable, Replit, Bolt), each running at roughly half a billion dollars of annual revenue on this shape [6]; agents left to grind through a Jira or Linear backlog, with the ticket as the only spec [16] | Nothing fixed the meaning and nothing checks the result. Wonderful for a prototype, ruinous for a system of record, because every change is a fresh guess |
| Loose, tight, loose | "Discipline for agents": write a spec, then a plan, then a task list, then let it build | Spec-driven toolkits (GitHub Spec Kit, AWS Kiro), agile role-play frameworks that give agents job titles [14]; and most enterprise delivery, which is where Flyvbjerg's numbers come from | The spec is prose no machine can check, the ceremony is the product, and "done" is judged by tests the agent wrote for itself. Process is what organisations buy when the start is loose |
| Tight, tight, tight | "AI inside the platform you already own" | Copilots inside low-code and ERP builders (Power Platform, Dynamics, Mendix, OutSystems); Dynamics alone has about forty approved screen patterns and a checker to police the choice [7] | Tight on form, loose on meaning, which is backwards. The agent types faster inside a cage that still needs specialists to open it |
| Tight, loose, tight | "Fix meaning, free the machine, verify the shape" | Palantir's embedded engineers and ontology proposals [13]; test-first agent loops that restart until a suite fixed in advance passes [16]; our factory | Holds, provided what must pass was fixed before the machine started and is checked without its help. A loop that writes and grades its own tests is the first row with persistence |

## Our factory is tight, loose, tight

Our factory is our own work, and deliberately so. It runs on two small languages we built ourselves, one for the event model and one for the experience model, the former for specifying the business rules, and the latter for specifying the user journeys. The languages are not bought and not borrowed, because they are the harness around the model: they encode our verification contracts, our domain rules, our product experience. That is the one layer of agentic engineering that does not commoditize, and it only works bonded into the product it builds [8]. A public pair of languages in the same family is where an outsider can inspect the idea [18], and the stage-by-stage mechanics are in an earlier piece for engineers [10].

**Tight on meaning.** Before anything is built, the business, often the users themselves, and Engineering spend ample time drawing the timeline [9]: who does what, what fact that creates, what the business then knows, what decisions follow. The timeline is written down as an event model, which records the facts, the actions and every decision rule with its named reasons for saying no, and as an experience model, which records what each screen shows and lets you do, and where decisions take you next. An automatic checker refuses anything ambiguous. This is the step that fixes meaning, once, in a form both the CEO and the machine can read. It is the only step that needs senior people in the room.

**Loose on how.** From that point the machine builds. It is free in how it implements each decision rule, and free in how it proposes the next change when someone asks for one. The screens are not its to improvise: they are compiled from the experience model, within the company's design standards. Nobody writes a requirements document, nobody schedules a code review, nobody estimates. The loose period is minutes long and covers one feature of the system at a time.

**Tight on outcome.** There is exactly one approved way a feature may be shaped: one action, one set of facts it creates, one way the business state is derived from those facts. The machine's output is checked against a locked reference and against the examples the business gave while modeling, which were written as tests from the start. If the result deviates, it does not ship. Review collapses to two questions: did it pass, and is the business rule correct. The second question is the only one a human still needs to answer.

The loose middle is smaller than it looks, and that is the point of a metaphor I used in an earlier piece for engineers, the two-stage rocket [10]. The first stage is a function, not a model: a generator derives everything structural from the model, the facts, the actions, the refusals, every example the business gave as a test, inside the compiler on every build. Nobody writes that code, no machine guesses at it, and it is never kept in the repository, where it could drift from the model. The second stage is the agent, and it writes only what the first stage cannot derive: the two bodies of each decision rule, whether an action is accepted or refused, and what it does to the business state. That is the only place in the system where anything is ever a guess, and it is checked at once. Rocket engineers know what happens without a clean separation: the first stage is still burning when the second ignites, and it interferes with the trajectory [11]. Prompt-to-code tools have one stage. The model writes the structure as well as the decisions, so every build is a fresh guess at things that should never have been in question.

In our experience the method removes about eighty percent of meetings, and features need no code review, only a check that the state is correct and the work landed on time. The method's originator reports more [12]. Those are practitioners' numbers, not a study. But the mechanism is plain: the meetings existed to re-negotiate meaning, and the meaning is now written down where a machine holds people to it.

## The cautionary tale: $125 million of loose front

Tessl is the company I would have founded if I believed a specification written in plain English could be the source of truth for a system. Founded in London in 2024 by Guy Podjarny, who built Snyk, it raised about $125 million on the boldest version of spec-driven development: the specification is the only thing humans maintain, and code is a disposable artifact regenerated from it [15]. That is the spec-as-source bet as a venture thesis, and it is our bet too. One word in it was wrong.

The specifications were prose. Tessl shipped a framework in closed beta in September 2025, with a registry of more than 10,000 specs telling agents how to use open-source libraries [17], and reviewers found its regeneration was not repeatable [15]: ask it twice, get two programs. During 2025 the company paused the framework, and on 29 January 2026 it reframed itself around a skills registry and the governance of agents [15]. Read through the model, the front only looked tight. A spec file with a ceremony around it is still loose when no machine can check whether it is complete, consistent, or the same thing it was yesterday. The back was loose too, because the guardrails were tests the agent generated from the same prose it was building from, so the thing being checked and the thing doing the checking shared every error. That is loose, tight, loose wearing the clothes of tight, loose, tight, and it failed the way the model predicts: drift at the front, no learning at the back, process as the only product.

Our factory is the same bet with the one word corrected. The spec is a small, precise language fit for the target architecture, not prose: the event model and the experience model are strict enough that a checker refuses ambiguity. They are small enough that a business owner can take in the whole model of a system at once, drawn as the timeline in our own modeling studio, with the text behind it one click away. It is not a document in the sense of a user story or a ticket; it is a model the business reads as a picture and the machine reads as text, and both read the same thing. Regeneration is repeatable and locked against a reference, so the model is the record of truth and the code really is disposable. The examples are written by the business while modeling and compiled into the tests, so the checker owes the agent nothing. Same ambition as Tessl's, the same shape from a distance, and the three differences sit exactly where tight has to mean tight: the spec is a language a checker can refuse, the structure is derived by a function rather than written by a model, and the tests come from the business.

## What does not get cheaper

Three things, and they are where your attention and your budget should go.

Deciding what the business wants is still hard, and modeling makes that visible rather than easy. Companies that have never had to agree on their own rules discover quickly, that they disagree. That is a feature. It used to cost up to a year in the offshore model.

Someone must own the meaning afterwards. When a rule changes, a named person is accountable for having said so, because the machine will build whatever the model says. This is a senior role, not an IT role. Palantir, the best-known company to run this operating model at scale, embeds an engineer at the customer for the first model and then routes every later change through a proposal and approval, at every customer size [13]. The pattern is the same here: the business owns the rule, the factory's engineer is counsel.

Integrations with other systems, legacy or external, remain real work. The factory makes your own system cheap. It does not make your neighbours' systems any less messy.

## Four decisions for a leader

First, move budget from building systems to two things at once: building the factory, and meaning. They run in parallel, since the first models are what the factory is built against, and the factory is paid for once. Fund modeling properly and insist that the people who know the business are in the room. A day of their time at the start replaces months of everyone else's time later.

Second, staff the owner. Name the person accountable for each part of the product's rules. If you cannot name one, it should not be built yet.

Third, stop buying process. Status meetings, change boards, acceptance ceremonies exist to compensate for a loose start and to protect builder time that is no longer scarce. Once the start is tight, they are cost without function. Measure lead time from a decided change to a running change instead.

Fourth, hire rocket engineers, not rockstar developers. The rockstar writes code faster and better than anyone, and that is the skill agents have already made cheap. The rocket engineer builds the first stage: the domain-specific specification languages, the generator and the checkers that hold your meaning and fix your architecture once, so nobody has to carry it in their head. That is the one piece of engineering that does not commoditize, and you buy it once.

## The one-line version

Software is expensive where meaning is loose and cheap where form is loose. Our factory is tight on meaning, loose on form, and allows exactly one shape at the end, so the loose part can be a machine and the tight parts can be a checker and a test suite instead of a management layer.

---

### References

1. Flyvbjerg and Gardner, *How Big Things Get Done* (2023): about 18 percent of IT projects overrun by more than 50 percent, and those projects overrun by 447 percent on average.
2. Brooks, "No Silver Bullet: Essence and Accidents of Software Engineering," *IEEE Computer* (1986).
3. Moseley and Marks, "Out of the Tar Pit" (2006).
4. "The Basics of Tight Loose Tight," Glasspaper: https://www.glasspaper.no/artikkel/utvikling/the-basics-of-tight-loose-tight/
5. Schwartz, Sagie, Zaidman, Hamburger and Teeni, "An empirical assessment of the loose–tight leadership model": https://www.tau.ac.il/~teeni/publications/loose.pdf
6. Lovable's $400M raise at $13.3B after $500M annualized revenue, and Replit near $525M ARR: https://appcoding.com/ai-app-builders-reviewed-lovable-base44-bolt-replit-and-v0-compared/ and https://tech-insider.org/replit-vs-lovable-vs-bolt-new-2026/
7. Microsoft Learn, "Form styles and patterns" for Dynamics 365 finance and operations: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/form-styles-patterns
8. Rosén-Lidholm, "Models commoditize. The layers sandwiching them do not," LinkedIn, 2026, on the harness as the bonded, non-transferable layer: https://www.linkedin.com/feed/update/urn:li:activity:7491552249555542016/
9. Dymitruk, *Event Modeling*: https://eventmodeling.org
10. Rosén-Lidholm, "The Two-Stage Rocket Fills the Hole the Thought-Leaders Identified": [[two-stage-sdd-rocket]], and "The Spec Is the Product": [[the-spec-is-the-product]].
11. Stage-separation failure described in US patent 4,924,775, Integrated two stage rocket: https://patents.google.com/patent/US4924775
12. Dymitruk, Event Modeling talk slides (Skills Matter): "removed 90% of all meetings"; "work in slices, no code reviews (SLA and state correctness only)": https://res.cloudinary.com/skillsmatter/image/upload/v1666065855/bca2sbuv5z3sodwstjvb.pdf
13. Palantir, AI FDE overview and Ontology Proposals: https://www.palantir.com/docs/foundry/ai-fde/overview
14. Fowler, Dushinski and others, "Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl": https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
15. Tessl paused Framework development and removed it from its CLI in 2025, and on 29 January 2026 reframed itself as an Agent Enablement Platform around a skills registry: https://ai.engineer/orgs/tessl and https://codemyspec.com/blog/tessl-review
16. MacManus, "AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers," Latent.Space, 2026-07-01, on Huntley's "everything is a ralph loop": https://www.latent.space/p/aiewf-daily-dispatch-loops
17. Tessl, "Announcing Tessl's Products to Unlock the Power of Agents," September 2025 (Framework in closed beta, Spec Registry with 10,000+ usage specs): https://tessl.io/blog/announcing-tessls-products-to-unlock-the-power-of-agents/
18. Rosén-Lidholm, public event and experience modeling languages (specs, linter, RFCs), related to but distinct from the ones used in the factory: https://github.com/MartinRL/xmlang
19. Telenor Danmark, "Telenors HR-direktør vinder HR-prisen 2021," press release, 23 September 2021 (DANSK HR's prize to Mette Eistrøm Krüger, citing tight-loose-tight): https://www.mynewsdesk.com/dk/telenor/pressreleases/telenors-hr-direktoer-vinder-hr-prisen-2021-3130577
20. Goldratt and Cox, *The Goal* (1984): the five focusing steps, and the warning against letting inertia keep a process built around a constraint that has moved.

---
title: "Three Thought-Leaders Described the Same Hole. The Two-Stage SDD Rocket Fills It."
description: "Gorman, Böckeler and DHH each named a different problem with agentic development. They share a root cause, and the fix has been running in production for a while."
created: 2026-09-05
status: draft
venue: chronograph, linkedin
---

# Three Thought-Leaders Described the Same Hole. The Two-Stage SDD Rocket Fills It.

> Three recent podcast episodes, three sharp diagnoses, one undrawn conclusion: the LLM is doing the lion's share of the transformation, and it should not be.

## Three episodes, one hole

Three episodes I listened to recently each put a finger on something real about building software with agents.

**Jason Gorman**, on Software Engineering Radio \[1\], explained the mechanics of why output gets unreliable. Every token an LLM emits is a probabilistic step. And because attention is spread across every token in the context, the effective limit at which reliability falls off a cliff is orders of magnitude below the advertised window. Put those two together, and the conclusion I draw is that more tokens make it worse: the steps compound, and a bigger context window is more fuel for the same fire, not a fix.

**Birgitta Böckeler**, also on Software Engineering Radio \[2\], said out loud what many of us have felt: "I just don't see the future as being like 50 markdown files in our codebase. I mean that can't be it, right? … Can we still call ourselves engineers if that's how we're doing stuff?" Her distinction is between *guides* (prose the model interprets) and *sensors* (checks that fire deterministically), and her instinct is that sensors are underused.

**DHH**, with Lex Fridman \[3\], was blunt about roles: designers cannot produce pull requests of the same quality as engineers, however good the tools get. A PR is an engineering artifact and it takes an engineer to hold it to an engineering standard.

Each of the three is right. And each is describing a symptom of the same arrangement: in mainstream agentic development and spec-driven development, an LLM performs the transformation from intent to code, for all of the code, and the resulting code is both version-controlled and the product. Gorman's compounding tokens, Böckeler's markdown sprawl and DHH's PR ceiling are three views of that one design decision. This article is about the conclusion none of the three drew, and about what happened when we built on it.

## What mainstream spec-driven development actually ships

Böckeler herself wrote the clearest map of the territory, in her comparison of Kiro, Spec Kit and Tessl on martinfowler.com \[4\]. She sorts spec-driven development into three levels: *spec-first* (write a spec, then code), *spec-anchored* (keep the spec alive alongside the code) and *spec-as-source* (the spec is the primary artifact and the code is generated, never hand-edited).

Against that map, the tools most teams reach for today all sit on the first rung.

**Kiro** produces three markdown files per feature: requirements in EARS notation ("WHEN … THE SYSTEM SHALL …"), a design document and a task list. An agent then implements the tasks. The docs advise storing specs "alongside the code they describe"; keeping the two in agreement is a matter of discipline, not mechanism.

**GitHub Spec Kit** adds a constitution and a pipeline of slash commands: specify, plan, tasks, implement. Its README says specifications "become executable, directly generating working implementations". Executable here means an LLM reads them. It also ships a *converge* command that assesses the codebase against the spec and appends the drift as new tasks: drift repair, by another LLM pass. Colin Eberhardt at Scott Logic put Spec Kit through its paces and reported "a sea of markdown documents, long agent run-times and unexpected friction", including a module contract four times longer than the module it eventually described \[5\].

**OpenSpec** keeps requirements as SHALL statements with WHEN/THEN scenarios and archives each change after it is applied. Its headline promise is "plain Markdown, no special syntax to learn". That is an honest description of the trade: nothing to learn, and nothing a machine can check.

Böckeler's verdict on the one tool that attempts spec-as-source, Tessl, is the telling detail: it marks its output with `// GENERATED FROM SPEC - DO NOT EDIT`. Anyone who lived through Windows Forms v1 or the first data-access generators recognizes the comment fence. Her list of what remains unsolved is equally telling: non-determinism (identical specs, different code), agents ignoring their instructions, and the risk that spec-as-source repeats Model-Driven Development's collapse by combining "inflexibility *and* non-determinism".

Put gently: this is AI bolted onto the existing way of working. The workflow is the one humans followed, the architecture is the one humans built, the artifacts are the ones humans reviewed, and an LLM has been substituted for the human at each step. The sociotechnical system was not rethought; its operators were replaced.

## The two-stage SDD rocket

The alternative I have been writing about, and that is now part of the software factory at my day job, splits the transformation in two.

**Stage one is deterministic.** A formal spec (a small DSL, event model in our case) is transformed by a *function*, not by a model. In ["The Spec Is the Product" Is a Slogan Until the Code Leaves Your Repo](the-spec-is-the-product.md) that function was a Roslyn source generator emitting the domain vocabulary, the Given–When–Then scenarios as tests and the decider dispatch, inside the compiler, on every build. There is a precondition that makes the function writable at all: the DSL maps one to one onto the architecture. A command in the spec is a command record in the core, an event is an event, a scenario is a decider test, with no interpretation in between. That mapping is what lets a generator, rather than a model, carry the lion's share. The output is never in the repository. Same spec in, same system out, and drift between spec and code is not discouraged but unrepresentable, because the derived representation has no independent existence to drift in.

**Stage two is agentic.** What stage one cannot derive, the actual decisions (what a command does to state, how a score is computed, the imperative shell), is written by an agent inside a harness, against the oracles stage one produced. A new event in the spec is a compile error at every site that fails to handle it. A scenario in the spec is a test the agent's code must pass. The harness itself prefers tools with hard signals over agents with opinions: MCP and CLI tools rather than a review agent imitating a human reviewer. One such tool is CodeScene's Code Health, and by construction it never sees the generated output, only what the agent wrote. When a residual pass lands below the health threshold, the eval loop records why and codifies the lesson, so the harness improves with use instead of with prompt archaeology. The agent writes the residual, and the residual is small.

The rocket metaphor is deliberate. The first stage carries the mass and burns out early; the second stage is light and does the precise work. What the first stage carries is everything in the system that is pure structure: the commands, events and business errors as closed unions, the decider's dispatch over them, and every Given–When–Then scenario as an executable test. In a functional core with vertical slices there is no entity, DTO, mapper or schema for those facts to be restated in; the vocabulary exists once, in the spec, and the compiler sees it on every build. The LLM never writes it, and the code-health gate never has to read it. What remains for the second stage is the part that is actually a decision: what this command does to that state.

## Why the rocket answers all three

**Gorman.** If every token is a probabilistic step and the steps compound, the lever is not a smarter prompt or a bigger window. It is fewer tokens. Stage one emits zero LLM tokens for the lion's share of the code. Stage two emits tokens only for the residual, into a context that holds a small spec and a compiler's opinion rather than a sea of markdown. Eberhardt's four-to-one contract is four times more LLM output for a human to verify, and the rocket never asks for it to be written at all.

**Böckeler.** Her two unsolved problems for spec-as-source are non-determinism and the ghost of MDD. Stage one is deterministic by construction, and the ghost is kept out by the repo boundary: the failure of MDD was protected regions rotting inside committed generated code, and there is no committed generated code here. And the harness described above is her sensors-over-guides instinct applied as a design rule: hard signals from tools, not opinions from agents.

And an honest line she would demand: the harness rules in stage two are still markdown. Her complaint stands for that layer. The rocket shrinks the layer the complaint applies to; it does not yet abolish it.

**DHH.** He is right that a designer cannot produce an engineer-grade PR. He is right because a PR is code, and code is the engineer's medium. The rocket's answer is that the PR is not the unit of contribution. The spec is, and the spec is written in a small DSL about the domain: what people can do, what happens when they do it, what must be refused. That is not the engineer's medium; it is everyone's. My claim, and it is a claim about my own workplace, is that a designer there is as equipped to write that spec as an engineer is, and often better, because the spec is about the product and the designer has been staring at the product all along. The compiler and the generated tests then hold the change to an engineering standard without an engineer in the loop. Honesty requires the qualifier: no one outside engineering has shipped this way yet. The mechanism permits it; the organisation has not exercised it. I expect that to change, and I will report when it does.

## What it costs

Two things, and they are real.

The spec is a small DSL, and people have to learn it. OpenSpec's "no special syntax to learn" is the exact inverse of this trade, and I understand its appeal. The counter is that the dialect is an arrangement notation over concepts every engineer, and every model, already knows: commands, events, views, scenarios. The syntax is local; the semantics are mainstream.

And the approach suits AI-native architecture, which mostly means greenfield. The one-to-one mapping between DSL and architecture is the whole reason a function can do the lifting, and it only holds when the architecture was shaped for it: a functional core, vertical slices, deciders. A ten-year-old layered monolith has no such shape to map onto, and retrofitting one is a different article.

One more honest line, carried over from the first article: nobody has published the benchmark. What we have is a small public workbench where every line is agent-written and three strata exist only as functions of the spec, and a production factory at work that has adopted the same arrangement. That is an argument with a running example, not a measurement.

## The undrawn conclusion

Gorman told us why more tokens hurt. Böckeler told us markdown cannot be the whole answer and named the rung where the spec becomes the source. DHH told us where the PR ceiling sits for non-engineers. Put the three together and the conclusion is that the LLM should not be the transformer for the parts of the system that a function can derive, and that those parts should never be in the repository. Everything else follows: the token budget, the sensors, the roles.

The spec is the product. The compiler is the first reviewer. The agent writes what is left.

---

\[1\] SE Radio 732: Jason Gorman on the Effective Use of AI for Software Development.
\[2\] SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents.
\[3\] Lex Fridman Podcast #501: DHH on the Future of Programming, AI, Agentic Engineering, Vibe Coding and Linux.
\[4\] Birgitta Böckeler, [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html), martinfowler.com, 2025-10-15.
\[5\] Colin Eberhardt, [Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?](https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html), Scott Logic, 2025-11-26.

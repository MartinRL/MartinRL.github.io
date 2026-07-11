---
title: "How Far Does a Machine-Readable UX Spec Go?"
description: "Thirty years of model-based UI, the formats that shipped, and the AI-era answer for the Experience layer of an event-modeled system"
created: 2026-07-09
tags: [research, sce, sdd, event-modeling, mbui, ux, codegen]
---
# How Far Does a Machine-Readable UX Spec Go?

## Thirty years of model-based UI, the formats that shipped, and the AI-era answer for the Experience layer

> **Position:** The UX layer of an event-modeled system stratifies exactly like its domain layer (deterministic where the spec determines, agentic where it merely constrains, interpreted where the runtime is owned), but the determinism boundary sits lower than optimists assume and higher than the MBUI post-mortem suggests. Thirty years of Model-Based UI research established, at the cost of its own industrial relevance, precisely where spec-determination stops: a machine-readable spec fully determines the *abstract* UI (which screens exist, which fields they show, which actions they offer, where the data comes from and where the commands go), and nothing below it. Every attempt to make the spec determine the *concrete* UI produced interfaces Myers' field-defining survey called unpredictable and low-ceilinged, and every standardization attempt died (the W3C MBUI Working Group closed with its specs demoted to Notes; UIML became an OASIS standard nobody used). What shipped instead, from XAML to Airbnb's Ghost Platform to Adaptive Cards, all obeys one rule: a machine-readable UI spec that works in production determines *composition over a closed, hand-built component vocabulary*, never the components themselves. The AI era changes exactly one thing, and it is the right thing: the abstract-to-concrete transformation, the step no model compiler ever automated acceptably, is now staffed by a non-deterministic generator, and the deterministic stratum can generate the harness that pins it (Playwright scenarios from the Event Model's GWT slices, plus committed visual baselines as the lockfile for pixels). Cameleon was not wrong about the layers; it was wrong about who performs the middle transformation. For emlang this means `emlang-web` should generate the abstract UI and its verification, and should not try to generate pretty HTML.

---

## 1. The question, precisely stated

Start from a result about the domain layer of an event-modeled system. The structural stratum (command/event/error records, Decider `Decide`/`Evolve` skeletons, GWT test classes, wiring) is a deterministic projection of the Event Model: a Roslyn source generator can emit it at build time, so the code is a true build artifact, never committed, and a spec change surfaces at every affected call site as a compile error. The decide/evolve bodies are different in kind: they are what Jack Reeves' 1992 "What Is Software Design?" identifies as the irreducible residue of design judgment that no spec language absorbs, so they are agent-generated and *committed*, because the committed code is the lockfile for a non-deterministic generator, regenerated deliberately (regenerate-and-diff) rather than on every build. And a third stratum is best not generated at all but interpreted at runtime from spec metadata, Terraform-style: every artifact that is neither generated nor written is a seam that cannot drift. That demotion of code to build artifact stopped at one conceded gap: the Experience layer. Source generators cannot emit Blazor; "real UI" was filed under agent territory; wireframes in Event Modeling remain informal pictures. This report asks the follow-up: **how much of the user interface can a machine-readable specification determine, what does the thirty-year MBUI record say about where determination stops, and what does the AI era change about that boundary?** The answer must sort UX, like the domain, into spec-determined (generate deterministically), constrained-but-not-determined (agent territory, pinned by which tests?), and runtime-interpreted strata.

## 2. What thirty years of MBUI actually established

The academic lineage is coherent and long: ConcurTaskTrees for task modeling (Paternò), the Cameleon Reference Framework from the FP5 Cameleon project, languages spanning its levels (UsiXML, MARIA, UIML, XIML), a W3C Incubator Group (2008-2010), and finally the W3C Model-Based UI Working Group (2011-2015). Cameleon is the load-bearing artifact: it stratified UI development into four levels, and the W3C introduction document defines them cleanly. Task & Domain models ("hierarchies of tasks that need to be performed on/with domain objects"); the Abstract UI, "independent of any implementation technology or modality"; the Concrete UI, "modality-dependent, but implementation technology independent"; and the Final UI, "the UI in terms of implementation technology dependent source code." The promised pipeline was a compiler stack: task model in, final UI out, with context models (user, platform, environment) parameterizing the transformations.

The record of what happened next is unambiguous. The Working Group closed and its deliverables (Task Models, Abstract UI) were republished as Working Group Notes, the W3C's mechanism for "no longer progressing along the Recommendation Track"; advancing would have required multiple independent implementations successfully interchanging UI models, and they never materialized. Dave Raggett's 2013 "next steps" message to the group's list already reads as a wind-down. UIML tells the same story from the standards side: initiated 1997, refined for over a decade, approved as an OASIS standard, and adopted essentially nowhere; XIML never even published a public specification. The intro document itself concedes the epistemic core of the failure: in practice "not all aspects of interest could be captured in a (meta-)model," so completeness quietly degraded to expressiveness.

Why it failed is not folklore; it was diagnosed in print in 2000, before the W3C effort even started. Myers, Hudson, and Pausch's "Past, Present, and Future of User Interface Software Tools" evaluated tool generations by *threshold* (how hard to get started) and *ceiling* (how good the best achievable result is), and by whether their target held still. Model-based generation scored the worst possible combination: high threshold (author several formal models before any pixel appears) and low ceiling, with the survey literature summarizing their verdict as "unpredictability and a low ceiling, incapable of producing advanced UIs" (Akiki, Bandara & Yu carry the quote forward in their 2014 ACM Computing Surveys review, and note adaptive-MDE work spent the following decade trying to escape it). Two of Myers' other themes finish the autopsy. *Path of least resistance:* tools channel builders toward what is easy in the tool, and what was easy in MBUID tools was forms-and-dialogs; anything with bespoke interaction fell off a cliff. *Moving targets:* the concrete-UI vocabulary MBUID abstracted over (desktop widgets) was obsoleted twice during the research program, first by the web, then by touch. An abstraction layer over a moving target inherits the motion without the control.

This is the UI-specific instance of the wider MDA/CASE failure record (70% of CASE tools never used a year after purchase per Iivari; the 2014 Whittle/Hutchinson/Rouncefield survey of 450 practitioners finding MDE almost never generates whole systems and succeeds only on well-chosen parts), with one aggravating factor: **UI quality is judged aesthetically and contextually, by information density, visual hierarchy, motion, and idiom, and none of that ever had a slot in the meta-models.** The 80/20 last mile that MDA displaced into escape hatches is, for UI, closer to the whole visible product.

## 3. What shipped instead, and the rule it obeys

Machine-readable UI descriptions did succeed at industrial scale, just never at Cameleon's abstract level. The successes form a pattern.

**Declarative markup that shipped is concrete, not abstract.** HTML, XAML, Android layout XML, QML, Interface Builder XIBs: each is a Final-UI-adjacent serialization over one platform's widget vocabulary. And the industry has spent the last decade walking even that back into code: Jetpack Compose replaced Android XML, SwiftUI replaced storyboards, Flutter never had markup at all. Two forces drove the retreat. First, UI is state-dependent behavior, and the markup/code seam (findViewById, outlets, bindings) was pure friction once UI logic exceeded static composition. Second, the CASE-era lesson about lossy, un-diffable specs repeated itself: storyboards and XIBs were machine-*written* XML, not human-diffable text, and "storyboard merge hell" is a documented reason large iOS teams abandoned Interface Builder. A UI spec that cannot be reviewed in a diff loses to code that can. (One dissent worth logging: Aleksandar Vacić's "Interface Builder is declarative too" argues the tooling, not the idea, was at fault.)

**Server-driven UI is the interpreted stratum, live in production.** Airbnb's Ghost Platform is the canonical write-up: a single backend response controls "the screen's layout, how sections are arranged, the data displayed in each section, and even the actions taken when users interact," across web, iOS, and Android. But read what the client keeps: the *sections* are rendered by client-side components that engineers hand-built; the server composes, the client owns the vocabulary. Practitioner guides on SDUI converge on the same trade: highly custom experiences, coordinated animation, one-off interactions become much harder; a disciplined design system is the precondition; and without an owned component boundary SDUI degenerates into a form builder with brand colors. Adaptive Cards makes the division of labor explicit in its architecture: the card author writes declarative JSON intent, and the *host* controls final rendering through HostConfig ("all elements MUST be styled according to their respective Host Config settings"), which is exactly Cameleon's AUI/CUI split, shipped, at the price of a deliberately low ceiling (a constrained element set, capped payloads and actions). JSON Forms and react-jsonschema-form are the same architecture for the forms subdomain: data schema plus UI schema in, rendering resolved by a registry of pre-built renderers matched by testers; Retool's app definitions embed the same library. **Every one of these systems determines composition and data binding deterministically, and none of them determines what a component looks like, ever.** That is the empirical location of the UI determinism boundary, found independently by every team that shipped.

## 4. Design-tool-as-spec: the other direction of fit

The design-tool thread attacks the boundary from above: instead of generating the concrete UI from an abstract spec, make the concrete design itself machine-readable. Three findings.

First, the pixel side is genuinely becoming structured data. Figma's Dev Mode MCP server exposes a selected layer's "hierarchy, layout rules, text styles, component properties" to agents, and Figma's own framing is telling: the server provides design structure but "has no knowledge of your codebase, naming conventions, or component usage patterns"; fidelity of generated code is a function of context the team supplies. Code Connect, notably, is not generation at all: it is a *hand-maintained mapping* from design components to existing code components, i.e. an admission that the design-to-code arrow is resolved by lookup into a human-built vocabulary, the same closed-vocabulary rule as §3.

Second, the styling vocabulary is now a genuine machine-readable spec with industry adoption: the Design Tokens Community Group format reached its first stable version (2025.10), with Figma, Sketch, Tokens Studio, Style Dictionary and others implementing it. Colors, type ramps, spacing, durations: deterministically translatable to every platform. Tokens are the one part of *visual* design that behaves like schema.

Third, the fully automatic route remains weak. The pix2code lineage (screenshot to DSL to code, 2017) proved feasibility and stalled on scalability; the Design2Code benchmark (484 real webpages, NAACL 2025) found frontier multimodal models "mostly lag in recalling visual elements from the input webpages and generating correct layout designs," and successor benchmarks (DesignBench, interactive-page suites) keep finding the same two failure modes. Design-to-code today is a good first draft with unreliable layout, which is to say: non-deterministic generation needing a verification harness, not a compiler.

## 5. The AI-era claims, weighed

**Jordi Cabot's position is the stratified thesis, asserted from inside the MDE community.** His "vibe modeling" essay proposes "building software through conversational interaction with an LLM trained for modeling, not coding": the LLM produces *models*, classical deterministic templates produce the code, preserving "the magic of AI-assisted development without the unpredictability of LLM-generated code." His two arguments map one-to-one onto the strata: models are reviewable by non-coders (the spec is the reviewable artifact), and "the generation process is deterministic. If the model is good, we know the code is good and there is no need to check it." His "low-modeling" program attacks the other bottleneck, inferring models semi-automatically from unstructured sources, and his group has published on LLMs recovering IFML GUI models from mock-ups: the model layer as the *stable intermediate representation* between fuzzy input and deterministic output. Honest caveat he states himself: no complete vibe-modeling tool exists yet; BESSER's chatbot integration is in progress. The claim is architectural, not empirical.

**Generative UI is runtime interpretation with an LLM as the server.** Vercel's AI SDK (`streamUI`) maps model tool calls to pre-built React Server Components streamed to the client: the LLM decides *which* registered component to show with *what* props, and never authors the component. Structurally this is Airbnb's Ghost Platform with a language model where the backend service was, and it obeys the same closed-vocabulary rule; the academic "malleable/generative UI" thread (e.g. task-driven generative UIs, AlignUI) is exploring how far runtime composition can be pushed. v0, by contrast, is design-time: non-deterministic draft generation into code you then own, i.e. agent-stratum work.

**Prompt-as-spec has already produced its own correction.** Addy Osmani's "writing a good spec" guidance pulls AI-facing specs toward PRD structure, explicit boundaries, and "conformance testing \[as\] a contract," and is candid that a spec should say what and why, not how. That is a spec that *constrains* an agent, not one that determines output; it concedes the stratum-2 nature of the work in its very form.

**Event Modeling already carries the abstract UI, informally.** The methodology's wireframes exist for *information completeness*: every field in every view must be traceable to an event, every event reachable through a command, with example data making gaps auditable. Dilger's eventmodelers.ai toolkit states the interface discipline plainly ("The interface from the 'backend' to the 'screen' is the Read Model"; "every dynamic value must actually be visible from the screens in the slices") and generates slices and tests, but not the UI itself; Qlerify generates models and code skeletons, screens remain diagrams. Nobody in the Event Modeling tool space has crossed the §3 boundary either, which is corroborating evidence for where it lies: the `v:` elements and wireframes are a task-and-AUI model wearing informal clothes, and that layer, not the pixel layer, is what the community's tools formalize.

## 6. The MBUI objection, honestly weighed

Does the MBUI corpse condemn an emlang-driven UX stratum the way the MDA corpse threatens deterministic domain generation? The decomposition:

| MBUI failure cause | Applies to emlang-driven UX generation? |
|---|---|
| Unpredictable, low-ceiling generated interfaces (Myers) | **No, by scope.** Nothing concrete is generated deterministically; the deterministic output is the abstract UI plus wireframe scaffolds explicitly labeled as scaffolds. The ceiling problem belonged to the AUI→CUI compiler, which is deleted, not fixed. |
| High threshold: author formal models before any pixel | **Mostly no.** The Event Model already exists for domain reasons; the UX stratum reads `v:` and command elements that are already there. The marginal modeling cost of the UI layer is near zero, which no MBUID tool could claim. |
| Moving concrete-UI targets (desktop → web → touch) | **No, by placement.** The spec stops at the abstract level, which survived every platform shift (screens, fields, actions are as meaningful on mobile as on 1995 desktops). The moving target is the agent's problem, and agents retrain; compilers do not. |
| AUI→CUI requires design judgment no transformation encodes | **Yes, permanently.** This is Reeves' residue in visual form: density, hierarchy, motion, idiom. The AI era staffs this step with a non-deterministic generator; it does not eliminate the judgment. |
| Standardization without implementations (W3C Notes, UIML) | **No.** Nothing here awaits a standards body; the generator is in-house code against an in-house YAML dialect, the same posture as the domain generator. |
| Machine-written, un-diffable artifacts (storyboard merge hell) | **No.** The spec is text; generated wireframes are build artifacts; visual baselines are binary but append-only and reviewed as images, which is their native reading. |
| Aesthetics judged by humans, absent from every meta-model | **Yes, and load-bearing.** No test type fully pins "looks right." Visual regression pins "has not changed"; axe pins "is accessible"; token lint pins "uses the sanctioned vocabulary." The gap between those three and "is good" is irreducibly human review, and it is the honest limit of this whole design. |

## 7. The position

**Thesis: Cameleon's levels were correct; its staffing was wrong. Assign each level to the stratum whose generator can actually produce it.**

**Stratum 1, spec-determined (generate deterministically, build artifact): the abstract UI and its verification.** From the Event Model's `v:` views, commands, and GWT slices, a deterministic generator can emit: the screen inventory and navigation topology (one screen per slice surface); field lists bound to read-model properties; action lists bound to commands with their payload shapes; form scaffolds à la JSON Forms (data schema + UI schema) for every command; wireframe HTML explicitly styled as wireframe; the design-token file as the styling vocabulary (DTCG format, now stable); and, critically, **generated Playwright scenarios transcribing each GWT case into a UI walk** (Given: seed events; When: submit the command's form; Then: assert the view shows the projected values). Information completeness, Event Modeling's own audit rule, is precisely the property that makes this stratum closed: every field traces to an event, every action to a command, so the abstract UI is a total function of the model. The five properties under which deterministic codegen has historically succeeded, from the ORM designers of the early 2000s to protobuf, all hold here: a closed formal spec, a mechanical judgment-free mapping, a narrow stable interface, compiler-or-tool-enforced ownership seams, and strictly one-way generation with never-edited output. This is what `emlang-web` should be: not a pretty-HTML generator but an AUI-and-harness generator.

**Stratum 2, constrained (agent-generated, committed, review by eye): the concrete UI.** Layout, hierarchy, responsive behavior, micro-interactions, density judgments, component styling within the token vocabulary. The agent works against four pins, in descending strength: generated Playwright GWT scenarios (behavioral: the screen must actually let the user do what the slice says, showing what the slice shows); accessibility gates (axe via Playwright or Chromatic, now routine CI practice); design-token lint (no unsanctioned colors or spacing); and committed visual baselines. The lockfile pattern from the domain stratum transfers exactly: just as committed agent-written code is the de facto lockfile for a non-deterministic code generator (Terraform pins provider binaries by hash; you pin the agent's output by committing it), **the committed screenshot baseline is the lockfile for pixels.** Chromatic's model (every Storybook story is a visual test) and Playwright's `toHaveScreenshot` make regeneration a deliberate, reviewed event: the agent may restyle a screen only by explicitly updating baselines under human eyes, the visual analogue of regenerate-and-diff. What remains unpinned (whether the result is *good*) is exactly what remains unpinned in stratum-2 domain code (whether it is habitable), and it is reviewed the same way: by a human, quickly, because correctness is already discharged by the harness.

**Stratum 3, interpreted (no generated UI at all): where the runtime is owned.** Admin and back-office surfaces, form-heavy internal tools, and conversational surfaces should render the spec at runtime, SDUI-style: a JSON-Forms-class interpreter over the same command/view schemas, or a generative-UI runtime choosing among pre-built components. The closed-vocabulary rule of §3 is the design constraint: build the component library by hand (agent-assisted, stratum 2), let the interpreter compose it. Every internal screen that is interpreted rather than generated is a seam that cannot drift from the spec.

The Cameleon mapping, stated once: Task & Domain model = the Event Model itself; Abstract UI = stratum 1, deterministic; Concrete UI = stratum 2, agentic under generated verification; Final UI = build artifact of both. MBUI failed by forcing strata 1 and 2 through one deterministic compiler; the pre-AI industry succeeded by hand-writing stratum 2 against interpreted stratum-3 runtimes; the AI era's contribution is a generator whose non-determinism is acceptable in exactly the stratum where determinism was never achievable.

**What this means for ChronosFactory/emlang, concretely.** ChronosFactory, ChronosHub's prototype and production application factories, is the empirical vehicle: an event-modeled spec drives agents that today hand-transcribe the UI layer the way they hand-transcribe the domain skeleton, i.e. deterministic work performed non-deterministically. (1) Re-scope `emlang-web` from "wireframe generator" to *abstract-UI generator*: screens, bindings, navigation, form scaffolds, tokens file, and generated Playwright specs per GWT slice; and since Roslyn source generators emit C# only (no HTML, no Blazor), keep it a pre-build CLI tool in the Grpc.Tools/NSwag mold. (2) Add a `tokens` block (DTCG-compatible) to the emlang dialect so styling vocabulary lives in the spec; do not add layout syntax, that is the MBUI tarpit. (3) Adopt the visual-baseline lockfile: Playwright `toHaveScreenshot` per generated scenario, baselines committed, agent restyling gated on baseline diffs. (4) The measurable experiment: for the prototype factory's existing UI, count what fraction of markup is composition-and-binding (spec-determined) versus styling-and-interaction (agent); the SDUI record predicts the majority of *elements* are determined while the majority of *review attention* stays on the residue. The generator investment amortizes where the production factory lives: every slice ChronosFactory ships is another application of the same AUI-and-harness generator. (5) Watch Cabot's BESSER/vibe-modeling line and Dilger's toolkit: both are converging on model-as-intermediate-representation, and eventmodelers.ai already treats the read model as the UI contract; the open ground is the generated Playwright harness, which nobody listed here ships.

**Where the thesis could be wrong, stated plainly.**
1) The abstract UI may be less total than claimed: real screens aggregate multiple slices, and screen composition (which slices share a page) is a design judgment the Event Model does not currently record; emlang would need a lightweight page-grouping construct, and that construct is one step down the slope toward layout syntax. 
   
2) Generated Playwright scenarios pin the happy path per slice but not flows across slices; end-to-end journey tests remain hand-authored, so the harness has a coverage ceiling below the domain stratum's. 
   
3) Visual baselines pin regressions, not quality, and they are noisy (anti-aliasing, font rendering); if baseline churn exceeds signal, teams turn them off, and stratum 2 loses its lockfile. 
   
4) The moving-target argument may come for the strata themselves: if generative UI (stratum 3 with an LLM runtime) becomes the dominant interaction paradigm, the concrete-UI stratum shrinks toward zero and the investment in agent-pinning infrastructure depreciates; Vercel's trajectory is the leading indicator to watch. 
   
5) All quantitative claims about design-to-code weakness (Design2Code et al.) are benchmarks of screenshot-to-markup, not model-to-markup with codebase context; frontier models with Figma MCP plus Code Connect context may already be materially better than the published numbers, which would move the boundary down faster than this report assumes.

## 8. Answer to the original question

How far does a machine-readable UX spec go? **Exactly as far as the abstract UI, all the way and deterministically; no further, and the field spent thirty years and a W3C working group establishing that boundary empirically.** Below the boundary, determination was never the right relation: the shipped successes (SDUI, Adaptive Cards, JSON Forms, generative UI) all substitute *composition over a hand-built closed vocabulary*, and the AI era adds a generator that can build the vocabulary and the concrete screens under a harness the spec itself emits. The domain-stratum formula survives contact with the UX literature unchanged, with one refinement: for the domain, the spec generates the skeleton and the tests, and agents fill the bodies; for UX, the spec generates the screen contracts and the walkthrough tests, and agents fill the pixels. The residue is smaller than MBUI's critics feared and larger than the vibe-coding era admits, and its size is measurable, one baseline diff at a time.

---

## Sources

### MBUI academic history
- W3C, Introduction to Model-Based User Interfaces (WG Note): https://www.w3.org/TR/mbui-intro/
- W3C, MBUI Abstract User Interface Models (WG Note): https://www.w3.org/TR/abstract-ui/
- W3C Model-Based UI Working Group home: https://www.w3.org/2011/mbui/
- W3C MBUI Working Group charter (2011): https://www.w3.org/2011/01/mbui-wg-charter
- W3C Model-based UI Incubator Group (2008-2010): https://www.w3.org/2005/Incubator/model-based-ui/
- Raggett, "Next steps for work on model-based UI at W3C" (2013): https://lists.w3.org/Archives/Public/public-mbui/2013Nov/0008.html
- Myers, Hudson & Pausch, "Past, Present, and Future of User Interface Software Tools" (TOCHI 2000): https://dl.acm.org/doi/10.1145/344949.344959
- Akiki, Bandara & Yu, "Adaptive Model-Driven User Interface Development Systems" (ACM CSUR 2014): https://oro.open.ac.uk/39809/1/Akiki_Bandara_Yu_ACMCSUR2014.pdf
- Paternò et al., MARIA language: https://www.researchgate.net/publication/220286389_MARIA_A_universal_declarative_multiple_abstraction-level_language_for_service-oriented_applications_in_ubiquitous_environments
- OASIS UIML v4.0 standard: https://www.oasis-open.org/standard/uiml-v4-0/ and https://docs.oasis-open.org/uiml/v4.0/uiml-4.0.html
- UW review of UI description languages (incl. XIML): http://aiweb.cs.washington.edu/ai/supple/internal/litsearch/uilangs/uilangs.html
- Cabot, "Model-Driven UI Engineering: the IFML book": https://modeling-languages.com/model-driven-ui-engineering-ifml-book/

### MDA/CASE background and the domain stratum
- Jack Reeves, "What Is Software Design?" (1992): https://www.developerdotstar.com/mag/articles/reeves_design.html
- Fowler, "ModelDrivenArchitecture": https://martinfowler.com/bliki/ModelDrivenArchitecture.html
- Iivari, "Why are CASE tools not used?" (1996): https://dl.acm.org/doi/10.1145/292349.292353
- Whittle, Hutchinson & Rouncefield, "The State of Practice in Model-Driven Engineering" (2014): https://www.infoq.com/articles/the-state-of-practice-in-model-driven-engineering/
- Terraform dependency lock file: https://developer.hashicorp.com/terraform/language/files/dependency-lock
- Andrew Lock, "Using Source Generators with Blazor in .NET 6" (source generators emit C# only, no generator chaining): https://andrewlock.net/using-source-generators-with-blazor-in-dotnet-6/

### Cabot / MDE in the LLM era
- Cabot, "Welcome to the low-modeling revolution": https://modeling-languages.com/welcome-to-the-low-modeling-revolution/
- Cabot, "Beyond Vibe Coding: Welcome to Vibe Modeling": https://jordicabot.medium.com/beyond-vibe-coding-welcome-to-vibe-modeling-08ea6a96d005
- "Vibe Modeling: Challenges and Opportunities" (arXiv): https://arxiv.org/html/2507.23120v1
- "From Mock-Ups to IFML-like GUI Models: Using Large Language Models" (ICWE 2025): https://modeling-languages.com/wp-content/uploads/2025/04/ICWE2025_From_Mock_Ups_to_IFML.pdf

### Shipped machine-readable UI formats
- Brooks, "A Deep Dive into Airbnb's Server-Driven UI System": https://medium.com/airbnb-engineering/a-deep-dive-into-airbnbs-server-driven-ui-system-842244c5f5
- InfoQ, "Airbnb's Server-Driven UI Platform": https://www.infoq.com/news/2021/07/airbnb-server-driven-ui/
- Mobile Native Foundation, SDUI strategies discussion: https://github.com/MobileNativeFoundation/discussions/discussions/47
- Nativeblocks, "SDUI Best Practices and Common Pitfalls": https://nativeblocks.io/blog/best-practices-and-common-pitfalls/
- Delivery Hero, "Primer on Delivery Hero's Server Driven UI Platform": https://deliveryhero.jobs/blog/primer-on-delivery-heros-server-driven-ui-platform/
- Microsoft Adaptive Cards overview: https://learn.microsoft.com/en-us/adaptive-cards/
- Adaptive Cards HostConfig: https://learn.microsoft.com/en-us/adaptive-cards/rendering-cards/host-config
- JSON Forms UI Schema: https://jsonforms.io/docs/uischema/
- react-jsonschema-form: https://github.com/rjsf-team/react-jsonschema-form
- Retool JSON Schema Form component: https://docs.retool.com/apps/guides/forms-inputs/json-schema-form
- Bichlmeier, "How we switched from XML to Jetpack Compose at Süddeutsche Zeitung": https://medium.com/s%C3%BCddeutsche-zeitung-digitale-medien/how-we-switched-from-xml-to-jetpack-compose-at-s%C3%BCddeutsche-zeitung-63bd7f22aa6a
- Mash, "Reducing iOS storyboard merge hell": https://medium.com/flawless-app-stories/ios-storyboard-merge-hell-b4cbb2e57dfc
- Sieg, "Avoid Storyboards and Interface Builder": https://medium.com/remote-technologist/avoid-storyboards-and-interface-builder-cc3363de4782
- Vacić, "Interface Builder is declarative too": https://aplus.rs/2019/interface-builder-is-declarative-too/

### Design-tool-as-spec and design-to-code
- Figma, "Introducing our Dev Mode MCP server": https://www.figma.com/blog/introducing-figma-mcp-server/
- Figma Learn, Guide to the Figma MCP server: https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server
- Figma Learn, Code Connect: https://help.figma.com/hc/en-us/articles/23920389749655-Code-Connect
- DTCG, "Design Tokens specification reaches first stable version" (2025.10): https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
- Design Tokens Format Module 2025.10: https://www.designtokens.org/tr/drafts/format/
- Design2Code (NAACL 2025): https://aclanthology.org/2025.naacl-long.199/
- pix2code (Beltramelli): https://www.researchgate.net/publication/325920827_pix2code_Generating_Code_from_a_Graphical_User_Interface_Screenshot
- DesignBench (arXiv): https://arxiv.org/html/2506.06251v3

### AI-era UX specs and generative UI
- Osmani, "Writing useful AI coding specs" (good-spec): https://addyosmani.com/blog/good-spec/
- Vercel, "Introducing AI SDK 3.0 with Generative UI support": https://vercel.com/blog/ai-sdk-3-generative-ui
- Vercel AI SDK docs: https://ai-sdk.dev/docs/introduction
- "Generative and Malleable User Interfaces" (arXiv): https://arxiv.org/html/2503.04084v1
- AlignUI (arXiv): https://arxiv.org/pdf/2601.17614

### Event Modeling and the UI layer
- Event Modeling: https://eventmodeling.org/
- eventmodelers.ai step-by-step tutorial (screens, read models as UI contract): https://www.eventmodelers.ai/docs/event-modeling-tutorial/
- Pradhan, "Event Modelling Guide" (information completeness): https://www.pradhan.is/blogs/event-modelling-best-practices
- Qlerify event modeling tool: https://www.qlerify.com/event-modeling-tool
- bitExpert, "Avoid the Stille-Post-Effect with Event Modeling": https://blog.bitexpert.de/blog/avoid-stille-post-effect-with-event-modeling

### Testing the UX stratum
- Chromatic accessibility tests: https://www.chromatic.com/docs/accessibility/
- desplega.ai, "Visual Regression Testing: Playwright, Percy & Chromatic": https://www.desplega.ai/blog/deep-dive-7-visual-regression-testing-ui-bugs
- Autonoma, "Visual Regression Testing Tools for Teams Shipping AI-Generated UI": https://getautonoma.com/blog/visual-regression-testing-tools
- Subito, "How We Automate Accessibility Testing with Playwright and Axe": https://dev.to/subito/how-we-automate-accessibility-testing-with-playwright-and-axe-3ok5

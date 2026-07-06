---
title: "How Far Does the 2003-LLBLGen Model Go?"
description: "Spec as source of truth, code as build artifact: from ORM codegen to Event-Model-driven application generation"
created: 2026-07-05
tags: [research, sce, sdd, event-modeling, codegen]
---
# How Far Does the 2003-LLBLGen Model Go?

## Spec as source of truth, code as build artifact: from ORM codegen to Event-Model-driven application generation

> **Position:** The 2003-LLBLGen model (the early-mid-2000s codegen posture: designer model checked in as the source of truth, code regenerated from it, hand edits confined to sanctioned seams) generalizes much further than the industry currently practices, but it does not generalize uniformly. The correct architecture is *stratified*: a deterministic stratum where the Event Model fully determines the code (types, Decider skeletons, GWT tests, wiring) and where source generators can make code a true build artifact today; an agentic stratum where design judgment lives (decide/evolve bodies, UX), where code stays checked in because the committed code *is* the lockfile for a non-deterministic generator; and an interpreted stratum where the best code is no code (Terraform's own answer). The determinism boundary is not a technology limit; it is the line between what the spec fully determines and what it merely constrains. The strategic insight the research surfaces: the check-in question was never really about determinism. It is about distribution and trust, and both are engineerable. Kvissig.se is the empirical proof-in-miniature: its agents performs deterministic transcription non-deterministically. A generator should do that work instead, and the agent should be reserved for the residue.

---

## 1. The question, precisely stated

In the early ORM era, LLBLGen Pro (v1.0, September 2003) solved the impedance mismatch by deterministic code generation from a designer model. The generated data-access layer was, in the disciplined shops, a build artifact: regenerable, not hand-edited, arguably not even source-controlled. NHibernate took the opposite fork, interpreting mappings at runtime. Both forks worked; the codegen fork quietly won a rematch fifteen years later as Roslyn source generators, whose output lives in `obj/` and never touches git.

The SCE thesis holds that the specification *is* the product: Event Model + Experience/Operational/Policy layers, executable via Deciders, operationalized through Specify → Plan → Verify → Apply → Observe. The question this report answers: **if the spec is the product, how far can the source code itself be demoted to a deterministic build artifact, 2003-LLBLGen-style, and where exactly does that demotion stop?**

## 2. What the ORM era actually established (and what it didn't)

The research corrects two pieces of received memory.

**First: "don't check in generated code" was never the settled norm; it was a function of *when* generation ran.** SubSonic's ASP.NET BuildProvider regenerated the whole DAL at compile time from the live schema: never checked in. CodeSmith ran as an MSBuild task on the build server: not checked in. But LINQ to SQL and EDMX generated on *save* inside Visual Studio, so their output was universally committed, and even LLBLGen users routinely checked generated code in, partly because the early "user code regions" mechanism required the previous output to exist at regeneration time. The clean build-artifact posture only became cheap when the seam moved from *convention inside the file* (regions) to *language feature across files* (partial classes, .NET 2.0). LLBLGen's own docs deprecated regions in favor of partials. Lesson one: **the generated/hand-written boundary must be a language feature, not a convention**, and the generation step must be hermetic, fast, and toolchain-native, or teams start committing output in self-defense (SubSonic needed a live database at build time; that fragility is part of why its model faded). LLBLGen Pro itself moved on: the v3.0 rewrite (2010) turned it into a model-first entity modeling designer, and v5.x generates for EF (Core), NHibernate, and Linq to SQL as well as its own runtime, so "2003-LLBLGen" names the era's posture, not the current product.

**Second: deterministic codegen worked in the ORM niche because of five enabling properties**, all identifiable and all portable as criteria: (1) a closed, formal spec (a relational schema is a total description of its domain); (2) a mechanical, judgment-free mapping (table → entity is a pure function); (3) a stable, narrow interface on the generated layer (LLBLGen's 2003-generated code compiles against the 2019 runtime); (4) escape hatches with compiler-enforced ownership boundaries; (5) strictly one-way generation, no reverse flow. Frans Bouma's underlying claim, in his 2013 "Code-first O/R mapping is actually rather silly" post, is the philosophical core: both the class and the table are *projections* of an abstract entity definition, and hand-writing what a projection function can emit makes you "a human code generator... the people who are replaceable with a tool."

That is precisely the event modeling claim, one level up: the C# records, the Decider switch shells, and the GWT test classes are projections of the Event Model. Kvissig's `specs/CLAUDE.md` says it outright: "this spec is the single source of truth the C# domain maps to 1:1." Even test method names are a deterministic transform of spec test names (`cannot join nonexistent game` → `Cannot_join_nonexistent_game`). The transform exists; today an agent executes it by hand.

**What killed the ORM codegen era was not technical failure.** EF Code First flipped the platform default (2011), the EDMX designer was killed (2014), and TDD/DDD culture valued "code you own" over "model you project." Notably, the single argument that never lost was compile-time verification: rename a field in the spec, regenerate, and the compiler finds every affected call site. That property must be preserved in any modern successor, and it is the structural advantage deterministic generation holds over both runtime interpretation and LLM generation.

## 3. The MDA objection, honestly weighed

The strongest historical counterargument is the corpse of MDA/CASE. The evidence is brutal: 70% of CASE tools never used a year after purchase (Iivari, 1996); the 2014 Whittle/Hutchinson/Rouncefield survey of 450 practitioners found MDE almost never generates whole systems and succeeds only on well-chosen parts; Fowler's verdict ("Night of the Living CASE Tools") and Jack Reeves' 1992 "What Is Software Design?" (the code *is* the design; any artifact excluded from the build/test refinement loop rots) frame the standard critique.

But the failure taxonomy decomposes, and most of it does not transfer:

| MDA failure cause | Applies to Event-Model-driven generation? |
|---|---|
| Two mutable representations (round-tripping) | **No, by policy.** One-way generation, output never edited. This was *the* structural killer and it is fully avoidable; it re-enters only if agents patch generated files, so the discipline must be "agents edit the spec or the seams, never the output." |
| Spec has no execution semantics | **No.** UML "proudly had no semantics"; an emlang model has operational semantics defined by its executable GWT tests. The spec's meaning is checkable against the built system. |
| Diagrams as lossy specs | **No.** The spec is text: line-diffable, greppable, mergeable per slice. This also dodges what killed projectional editing (MPS, Intentional): bespoke editors versus free universal text tooling. |
| Toolchain lock-in | **No.** YAML in git, generator owned in-house as ordinary code. |
| Developers refuse to be "PSM compilers" | **Mostly no.** The 2004 objection lost force once AI started writing the boilerplate anyway; the question moved from "will developers accept generation" to "which artifact do humans review." |
| Spec less expressive than target language | **Yes, for the decide/evolve bodies.** Event Modeling is complete for the *shape* of the system (commands, events, views, acceptance behavior) but the body of a Decider's logic is arbitrary computation. This is Reeves' residue and it is irreducible. |
| The 80/20 last mile | **Displaced, not eliminated.** UI polish, integration quirks, performance live outside the model. The modern difference: the escape-hatch code is behavior-pinned by tests generated from the same spec, so it can diverge in style but not in behavior. |
| Who debugs generated code | **Live risk.** SCADE earned "never read the output" via DO-178C generator qualification; a homegrown generator earns trust via smallness, boring code, snapshot tests, and idiomatic readable output. |
| First-project economics | **Yes.** The generator costs more than app #1; payoff is at app #2..N and at change time. CASE shelfware died on this curve; budget for it explicitly. |

The success stories confirm the pattern by contrast: SCADE/Esterel (qualified generators, 100+ airborne equipment items, qualification legally replacing review of output), Simulink/TargetLink (TÜV-certified to ASIL D), parser generators, protobuf. Every success shares four properties: narrow formal complete domain; trusted generator; strictly one-way with never-edited output; and **verification at the model's own level of abstraction, so debugging happens in the spec, not the output**. That last property is exactly what the Decider pattern supplies at the product level: design-time simulation is model-level debugging.

The honest conclusion from history: "whole applications from the model" fails; "100% of a well-chosen stratum" succeeds. The design problem is choosing the stratum boundary correctly.

## 4. Where the industry actually draws the lines today

The landscape survey yields a taxonomy (generate vs interpret × checked-in vs build-artifact) and three load-bearing findings.

**Finding 1: check-in decisions are driven by distribution and trust, not determinism.** Kubernetes checks in generated clients because `go get` cannot run generators. AWS checks in the Smithy-generated SDKs so CI validates the exact shipped artifact and consumers can inspect real source. Nobody who states reasons says "we cannot reproduce it." Corollary for an internal product team where everyone has the generator in the build: the distribution argument evaporates, and build-time-only generation is viable *today* for the deterministic stratum.

**Finding 2: the direction of the seam predicts regeneration health.** Systems where hand-written code is *input to* the generator (Wasp's `main.wasp` referencing your functions; protobuf partial classes; Smithy's plugin-only customization) regenerate indefinitely. Systems where hand-written code is *edits to output* protected by ignore-lists (`.openapi-generator-ignore`, AsyncAPI `noOverwriteGlobs`) accumulate drift file by file; JHipster's issue tracker is the longitudinal study. Wasp is architecturally the closest existing system to the target model: spec + custom code as inputs, entire app compiled to a never-committed, never-edited `.wasp/out/`.

**Finding 3: healthy systems are stratified, not uniform.** Regenerable contracts at the bottom (protobuf-style), regenerable glue in the middle (Wasp-style), one-shot scaffolds at the top where divergence is expected (Rails-style). The failures (CASE, full-app regeneration with in-place edits) applied one policy to all strata.

Terraform itself supplies the fourth datum: it generates nothing. HCL is interpreted by providers at plan/apply time; the only determinism artifacts are the state file and a lockfile pinning provider versions by hash. The generate-vs-interpret fork from 2004 (LLBLGen vs NHibernate) is alive at every layer of the stack, and interpretation is the only known *complete* solution to the round-trip problem, at the price of owning a runtime. Mendix says this explicitly; the industry's favored compromise is **generate the types, interpret the behavior**.

And the Event Modeling corner of the map is conspicuously empty. emlang's YAML already carries typed props and Given-When-Then slices (everything needed to emit Deciders, projections, and executable tests), yet its CLI stops at diagrams. oNote stopped at Avro/gRPC contract export. Emmett and fmodel are hand-written-code libraries; Dugalic even documented the model→code mapping as mechanical ("From Model to Code") without shipping the machine. Diagramming from event-model text is commoditizing fast (emlang, evml, Mermaid's native eventmodeling type, Dilger's eventmodelers.ai); the semantic back half, spec → Decider + projection + GWT tests, is genuinely unoccupied open source. The one commercial occupant is Martin Dilger's eventmodelers.ai (§6).

## 5. The mechanism: what a .NET pipeline actually looks like

The Roslyn research settles feasibility. **AdditionalFiles-driven incremental source generation is a first-class, documented, production-proven pattern**: declare `*.em.yaml` as `<AdditionalFiles>`, parse in the generator, `AddSource` the records and skeletons. Razor itself compiles via a source generator; Orleans generates its serializers and proxies this way; TUnit discovers whole test suites this way. Editing the spec updates generated types in IntelliSense live, without a build. That live feedback loop is what source generators buy over any pre-build tool, and it is the modern version of LLBLGen's killer feature: spec change → compiler finds every affected site.

Hard limits, verified: generators emit C# only (no HTML, no Razor, and no chaining into the Razor generator); no filesystem writes; caching discipline requires equatable models. The generated/hand-written seam is stronger than anything LLBLGen had: C# partial members (methods, and since C# 13, properties) make the boundary compiler-enforced. The elegant trick available for Deciders: the generated `Decide`/`Evolve` switch skeletons delegate to *declared-only partial methods*, so **a new event in the spec is a compile error until a human (or agent) implements its case**. "Spec added behavior that code doesn't handle" becomes a build break, not a runtime surprise. Combined with the constitution's exhaustive-switch rule, the compiler becomes the drift detector.

For tests, the Gherkin precedent is exact: Reqnroll (SpecFlow's successor) generates `.feature.cs` at compile time via MSBuild, not recommended for source control, one named test per scenario, `#line` directives mapping failures back to the spec file. Generated `[Fact]` per GWT scenario beats runtime `[MemberData]` because scenario names are the living documentation, each case is individually runnable and debuggable, and failures point at the YAML line. Gherkin tooling made this choice twenty years ago and never reversed it.

Recommended architecture (Option A of three evaluated):

- **`Emlang.Generators`** (in-house Roslyn incremental generator, versioned as an internal NuGet package, pinned exactly): consumes `*.em.yaml`, emits command/event/error records, partial Decider classes with skeleton switches delegating to partial methods, one `[Fact]` per GWT case with `#line` mapping. Output lives in `obj/`, never in git; `EmitCompilerGeneratedFiles` output optionally committed to a review-only folder so generator upgrades produce a reviewable diff (the "one version bump silently rewrites every type" problem is real and this is the standard mitigation).
- **`emlang-web`** (dotnet CLI tool or extension of the Go toolchain, invoked by an MSBuild target pre-build, the Grpc.Tools/NSwag/Kiota pattern): generates Razor/HTML view wireframes from `v:` elements. Source generators categorically cannot do this half.
- **Golden-file/snapshot tests of the generator itself** (Verify.SourceGenerators), and a CI invariant: `artifact == f(spec, generator-version)`.
- Failure modes to budget: diagnostics UX (a YAML typo must surface as a precise compiler error with file/line or the DX is miserable), incremental-pipeline cacheability hygiene, two generators to keep in version lockstep, and generator debugging friction in VS.

Determinism, for the record, is solved on this stratum: Roslyn generators are required to be deterministic functions of their inputs. Same spec + same generator version + same compiler ⇒ same code. The 2003-LLBLGen posture is fully recoverable here.

## 6. The agentic stratum: where the AI-era debate actually lands

For the code the spec constrains but does not determine, the field has sorted into three schools, and the empirical record is unusually clear.

**Spec-as-source** (Tessl/Podjarny: "code as disposable artifact," files stamped GENERATED FROM SPEC - DO NOT EDIT; Sean Grove/OpenAI: "code is a lossy projection from the specification," and today's practice of shredding the prompt while committing the output is like shredding the source and checking in the binary; GitHub Spec Kit's rhetoric; Huntley's Ralph loop in greenfield/porting mode). The aspiration is exactly the 2003-LLBLGen model. The reality check: Tessl's regeneration engine remains closed beta, JavaScript-only, and was observed by Böckeler generating *different* output from identical specs; the company's shipped product pivoted to a skills registry. Pure regenerate-on-every-build is practiced nowhere in production.

**Code-as-source** (Willison: "I won't commit code I couldn't explain"; Kent Beck; Böckeler/Thoughtworks Radar, which placed SDD at *Assess* with the pointed warning that spec-as-source "might end up with the downsides of both MDD and LLMs: inflexibility and non-determinism"; Dudycz as the in-community sceptic). Their strongest cards: temp-0 non-determinism is empirically real (the TOSEM study; 80 structurally distinct completions from 1,000 identical requests; SWE-bench pass^k dropping 2-3× versus pass@k); tests pin only what they cover; and accountability does not transfer (when agentic coding broke something at Amazon, the mandate was "humans review all AI output"; no compliance regime accepts a green CI run as the accountable artifact without a named human attesting).

**The hybrid, which is where the evidence points** (Cockcroft; Dymitruk; Dilger; Kiro in practice): spec + strong test suite as the durable pair; code regenerable per-slice but still committed; verification loops converting non-determinism into retry noise. Cockcroft's determinism rebuttal is the sharpest formulation available and slots directly into the SCE frame: pulling a new compiler or library version was always non-deterministic too; "the AI native systems I've built have many more and far better defined tests than what I've seen human developers produce. This is the key difference that makes it work."

Two findings deserve emphasis.

**The committed code is the lockfile.** No "lockfile for LLM-generated code" practice exists; what everyone converges on instead is committing the generated code as the de-facto lock, keeping the spec, and regenerating *deliberately* (regenerate-and-diff) rather than on every build. This reframes the check-in question elegantly: checking in agent-written code is not a betrayal of the 2003-LLBLGen model; it is the lockfile pattern applied to a non-deterministic generator. Terraform pins provider binaries by hash; you pin the agent's output by committing it. Regeneration becomes an explicit, reviewed event, exactly like `terraform apply` after a `plan`, not an implicit build step.

**The closest prior art is live and should be engaged, not rediscovered.** Martin Dilger's eventmodelers.ai runs precisely the stratified model: machine-readable `eventmodel.json` as "the declared architecture," deterministic template-based codegen for structure, AI agents implementing slices ("mark a slice as Planned; the agent implements it, runs the tests, commits, marks it Done"), and the regeneration loop ("change the model, the code catches up"). His slogan "Spec + Vertical Slice = Candy for AI" and his framing of slices as bounded agent work units are the same claims as the SCE thesis, productized. Even Dilger keeps code committed with tests gating. Dymitruk's own position has converged here too: event modeling as "the missing link that gives AI the specification quality it needs," with GWT-per-slice partially displacing BDD/TDD. Adjacent signal from the Critter Stack: Marten 9.0 *removed* its runtime codegen (even deterministic codegen carries maintenance cost), while Jeremy Miller invests in curated AI skills for event-modeling building blocks.

## 7. The position

**Thesis: apply the 2003-LLBLGen model per stratum, with the stratum boundary defined by what the spec determines.**

**Stratum 1, deterministic projection (the spec fully determines the code): make it a true build artifact now.** Command/event/error records, Decider Evolve/Decide skeletons, GWT test classes, view models, schemas, wiring. All five ORM-era enabling properties hold: emlang is a closed formal spec for this layer; the mapping is mechanical (kvissig's conventions document is effectively the generator's functional spec, down to the test-name transform); the seam is compiler-enforced partials; generation is one-way; the interface is narrow. Roslyn incremental generators are the proven vehicle. On this stratum, checking in the code stops making sense for the same reason it stopped making sense for `.g.cs` files: it is a deterministic function of what is already checked in. The compiler-error-on-unhandled-event property makes the spec-code contract *stronger* than review could.

**Stratum 2, constrained design (the spec pins behavior but not implementation): agent-generated, committed, review-light.** The decide/evolve case bodies, projection transforms, real UI. This is Reeves' residue; it is genuine design and no spec language will absorb it (that was MDA's fatal overreach). But its acceptance gate, the GWT tests, is generated deterministically from the same spec in stratum 1, which inverts the usual AI-code-review economics: the agent cannot grade its own homework because the homework was set by the generator. Code is committed because committed code is the lockfile for a non-deterministic generator, and because accountability currently requires an inspectable artifact. Review attention shifts from "is this correct?" (the tests say) to "is this habitable?" (structure, security posture, performance: what tests don't pin). Regeneration is a deliberate, per-slice event.

**Stratum 3, interpretation (no code at all): prefer it where the runtime is owned.** Some of what one would generate should instead be interpreted, NHibernate/Terraform-style: read-model wiring from spec metadata, diagram and documentation rendering, possibly endpoint routing. Every artifact that is neither generated nor written is a seam that cannot drift. The rule of thumb the landscape supports: generate the types, interpret the behavior, and reserve hand/agent authorship for decisions.

**The forcing consequence for the SCE lifecycle:** the strata map cleanly onto Specify → Plan → Verify → Apply → Observe. Stratum 1 *is* Plan made real: regeneration is the diff between declared and actual. Stratum 2 is Apply with agents under generated verification. The spec stays sovereign only under one operational invariant, and this is the single most important discipline the history teaches: **editing the spec must remain the cheapest way to change the system.** The moment a hotfix in generated or agent-written code is faster than a spec edit plus regeneration, decay begins, exactly as it began for every MDA shop. That is a CI/process guarantee (block hand edits to generated output; make regeneration fast; fail builds on spec-artifact divergence), not a tooling aspiration.

**What this means for kvissig, concretely.** Kvissig is currently an existence proof that the 1:1 mapping is real and that a spec-disciplined agent hits ACMM 3 comfortably: the constitution, exhaustive switches, Result unions, hooks, and the spec's prop-type vocabulary close the loops so tightly that the agent transcribes rather than invents. But that means kvissig's agent spends most of its tokens doing stratum-1 work non-deterministically that a generator would do deterministically and for free. The highest-leverage experiment available: build the minimal `Emlang.Generators` (records + Decider skeleton + GWT Facts from `mer-eller-mindre-event-model.yaml`), delete the corresponding hand-checked files, and measure what fraction of the ~3,000 lines of domain + tests evaporates from git. The prediction worth testing: 60-70% of the domain and test code is spec-determined, and the residue that remains checked in is precisely the code that was interesting to review in the first place. That experiment also produces the first open-source occupant of the emlang→code gap, which the landscape shows is vacant and which the Wardley analysis in the engineering strategy independently identifies as the durable investment layer (specifications above the model, harness below; diagramming is already commoditizing, the semantic back-end is not).

**Where the thesis could be wrong, stated plainly.** (1) Böckeler's warning may bite: if the spec must become so detailed to drive generation that it is as hard to review as code, the bottleneck merely moves (mitigation: emlang's GWT cases are structured data, not prose; review is of behavior tables, not markdown essays). (2) First-project economics: the generator is a real engineering investment with payoff at slice #N, and kvissig alone may not amortize it (ChronosHub's migration bridge, with event models produced for every legacy slice, is where amortization actually lives). (3) Reeves is patient: if the decide/evolve bodies and the Experience layer turn out to dominate total effort, the deterministic stratum shrinks to scaffolding and the gain is modest; the kvissig measurement answers this empirically. (4) The open empirical gap nobody has filled: no published study measures regeneration stability under a fixed strong GWT suite, i.e. how often regenerated code that passes all pinned tests still diverges in ways that matter (security, performance, structure). Until that exists, "tests make code fungible" is a well-supported hypothesis, not a fact. It is also a paper someone at ChronosHub could write.

## 8. Answer to the original question

How far can one get? **All the way, on the stratum where the spec determines the code; deliberately not, on the stratum where it doesn't; and the boundary is knowable in advance, per element type, from the spec itself.** The ORM era got this right within its niche and the industry then forgot why it worked. The five enabling properties (closed spec, mechanical mapping, narrow interface, language-level seams, one-way flow) now hold for a much larger niche: the entire structural skeleton of an event-modeled system, tests included. What has changed since 2003 is not that determinism became optional; it is that the non-deterministic generator (the agent) arrived for the residue, and that the deterministic stratum can now generate the *verification* that pins the non-deterministic one. LLBLGen generated the data layer and left the business logic to humans. The emlang pipeline generates the skeleton and the acceptance tests, and leaves the business logic to agents held by those tests. Same architecture, one level up. The specification does not describe the product; it is the product, and on stratum 1, the code is not even worth versioning.

---

## Sources

### ORM era
- Frans Bouma, "16 years of LLBLGen Pro!" (2019): https://www.llblgen.com/blog/post.aspx?Id=14
- Bouma, "Solving the Data Access problem: to O/R map or not To O/R map" (2004): https://weblogs.asp.net/fbouma/240225
- Bouma, "Code-first O/R mapping is actually rather silly" (2013): https://weblogs.asp.net/fbouma/code-first-o-r-mapping-is-actually-rather-silly/
- InfoQ, "Frans Bouma Argues Code First O/R Mapping is 'Silly'" (2013): https://www.infoq.com/news/2013/12/Code-First-Debate/
- LLBLGen Pro 2.6 docs, "Adding your own code to the generated classes": https://www.llblgen.com/documentation/2.6/using%20the%20generated%20code/gencode_addingusercode.htm
- LLBLGen Pro v5 designer (entity modeling for EF Core, EF, NHibernate, Linq to SQL): https://www.llblgen.com/pages/designer.aspx
- Ayende, "On SubSonic & NHibernate" (2007): https://ayende.com/blog/2486/on-subsonic-nhibernate
- Ayende, "ADO.NET Entity Framework Vote of No Confidence" (2008): https://ayende.com/blog/3376/ado-net-entity-framework-vote-of-no-confidence
- Rowan Miller, "EF7 - What Does 'Code First Only' Really Mean" (2014): https://blogs.msdn.microsoft.com/adonet/2014/10/21/ef7-what-does-code-first-only-really-mean
- jOOQ manual, "Code generation and version control": https://www.jooq.org/doc/latest/manual/code-generation/codegen-version-control/
- Hanselman, "T4: Best Kept Visual Studio Secret" (2008): https://www.hanselman.com/blog/t4-text-template-transformation-toolkit-code-generation-best-kept-visual-studio-secret

### MDA/CASE
- Jack Reeves, "What Is Software Design?" (1992): https://www.developerdotstar.com/mag/articles/reeves_design.html
- Fowler, "ModelDrivenArchitecture": https://martinfowler.com/bliki/ModelDrivenArchitecture.html
- Fowler, "UmlAsBlueprint": https://martinfowler.com/bliki/UmlAsBlueprint.html
- Fowler, "Language Workbenches and MDA": https://martinfowler.com/articles/mdaLanguageWorkbench.html
- Meyer, "UML: The Positive Spin" (1997): https://archive.eiffel.com/doc/manuals/technology/bmarticles/uml/page.html
- Iivari, "Why are CASE tools not used?" (1996): https://dl.acm.org/doi/10.1145/292349.292353
- Hailpern & Tarr, "Model-driven development: the good, the bad, and the ugly" (2006): https://dl.acm.org/doi/10.1147/sj.453.0451
- Whittle, Hutchinson & Rouncefield, "The State of Practice in Model-Driven Engineering" (2014): https://www.infoq.com/articles/the-state-of-practice-in-model-driven-engineering/
- xtUML/BridgePoint: https://xtuml.org/about/
- Ansys SCADE DO-178C qualification: https://innovationspace.ansys.com/knowledge/forums/topic/efficient-development-of-safe-avionics-software-with-do-178c-objectives-using-scade-suite/
- dSPACE TargetLink: https://www.dspace.com/en/inc/home/products/sw/pcgs/targetlink.cfm
- Voelter et al., "Towards User-Friendly Projectional Editors" (2014): https://mbeddr.com/files/projectionalEditing-sle2014.pdf

### Landscape
- Smithy CLI (AWS Developer Blog): https://aws.amazon.com/blogs/developer/introducing-the-smithy-cli/
- smithy-rs RFC-0007, split release process: https://awslabs.github.io/smithy-rs/design/rfcs/rfc0007_split_release_process.html
- protobuf C# generated code (partial classes): https://protobuf.dev/reference/csharp/csharp-generated/
- gRPC .NET build integration: https://github.com/grpc/grpc/blob/master/src/csharp/BUILD-INTEGRATION.md
- OpenAPI Generator customization (.openapi-generator-ignore): https://openapi-generator.tech/docs/customization/
- Kubernetes code generation (Red Hat): https://www.redhat.com/en/blog/kubernetes-deep-dive-code-generation-customresources
- Kubernetes issue #8830, "Don't check in generated code": https://github.com/kubernetes/kubernetes/issues/8830
- The Guild, GraphQL codegen best practices: https://the-guild.dev/blog/graphql-codegen-best-practices
- Wasp: https://github.com/wasp-lang/wasp and https://wasp.sh/docs
- Why Blitz (ownership rationale): https://blitzjs.com/docs/why-blitz
- JHipster upgrading and side-by-side: https://www.jhipster.tech/upgrading-an-application/
- Amplication Smart Git Sync: https://docs.amplication.com/smart-git-sync/
- Terraform dependency lock file: https://developer.hashicorp.com/terraform/language/files/dependency-lock
- Mendix runtime architecture (interpretation dissolves round-trip): https://www.mendix.com/evaluation-guide/architecture/runtime-architecture/
- OutSystems architecture of generated apps (detach): https://www.outsystems.com/evaluation-guide/architecture-of-generated-apps/
- emlang project: https://emlang-project.github.io/ and https://github.com/emlang-project/emlang
- oNote Avro/gRPC generation: https://docs.onote.com/onote-docs/Latest/code/generate-avro.html
- Emmett (Dudycz): https://github.com/event-driven-io/emmett
- Dugalic, "From Model to Code": https://medium.com/axoniq/from-model-to-code-translating-the-event-model-into-code-5fc30a363114
- EventCatalog: https://www.eventcatalog.dev/
- Mermaid eventmodeling diagrams: https://mermaid.js.org/syntax/eventmodeling.html
- awesome-eventmodeling: https://github.com/MateuszNaKodach/awesome-eventmodeling

### Roslyn
- Roslyn incremental generators cookbook: https://github.com/dotnet/roslyn/blob/main/docs/features/incremental-generators.cookbook.md
- Thinktecture, "Using Additional Files" (Part 7): https://www.thinktecture.com/en/net/roslyn-source-generators-using-additional-files/
- dotnet/roslyn #57608 (non-source outputs, declined): https://github.com/dotnet/roslyn/issues/57608
- Andrew Lock, source generator series (esp. Part 2 snapshot testing, Part 6 saving output, Part 9-10 caching): https://andrewlock.net/creating-a-source-generator-part-6-saving-source-generator-output-in-source-control/
- Andrew Lock, "Using Source Generators with Blazor in .NET 6" (no generator chaining): https://andrewlock.net/using-source-generators-with-blazor-in-dotnet-6/
- grpc/grpc-dotnet #1888 (why gRPC declined a source-generator port): https://github.com/grpc/grpc-dotnet/issues/1888
- Roslyn interceptors: https://github.com/dotnet/roslyn/blob/main/docs/features/interceptors.md
- Orleans code generation: https://learn.microsoft.com/en-us/dotnet/orleans/grains/code-generation
- TUnit (source-generated test framework): https://github.com/thomhurst/TUnit
- Reqnroll MSBuild generation (#413, generated code not in source control): https://github.com/reqnroll/Reqnroll/issues/413
- Verify.SourceGenerators: https://github.com/VerifyTests/Verify.SourceGenerators
- .NET 10 file-based apps (dotnet run app.cs): https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/
- Steve Talks Code, "Source Generator Attacks": https://stevetalkscode.co.uk/sourcegeneratorattacks

### SDD / AI era
- Tessl, "From code-centric to spec-centric": https://tessl.io/blog/from-code-centric-to-spec-centric/
- Böckeler, "Understanding spec-driven-development: Kiro, spec-kit, and Tessl" (martinfowler.com): https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Thoughtworks Technology Radar, Spec-driven development (Assess): https://www.thoughtworks.com/en-us/radar/techniques/spec-driven-development
- Kiro specs docs: https://kiro.dev/docs/specs/
- GitHub Spec Kit: https://github.com/github/spec-kit and https://github.com/github/spec-kit/blob/main/spec-driven.md
- Sean Grove, "The New Code" (transcript): https://lawwu.github.io/transcripts/8rABwKRsec4.html
- Simon Willison, "Not all AI-assisted programming is vibe coding": https://simonwillison.net/2025/Mar/19/vibe-coding/
- Kent Beck, "Augmented Coding: Beyond the Vibes": https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
- Adrian Cockcroft, "Directing AI Native Development": https://adrianco.medium.com/directing-ai-native-development-0914ac271744
- Geoffrey Huntley, "Ralph Wiggum as a software engineer": https://ghuntley.com/ralph/ ; specs: https://ghuntley.com/specs/ ; porting: https://ghuntley.com/porting/ ; loop: https://ghuntley.com/loop/
- Thinking Machines, "Defeating Nondeterminism in LLM Inference": https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- ACM TOSEM, "An Empirical Study of the Non-Determinism of ChatGPT in Code Generation": https://dl.acm.org/doi/10.1145/3697010
- "On Randomness in Agentic Evals" (SWE-bench variance): https://arxiv.org/abs/2602.07150
- Stanford Clover (closed-loop verifiable codegen): https://ai.stanford.edu/blog/clover/
- SLSA attestation model: https://slsa.dev/attestation-model
- Stanford CodeX, "Built by Agents, Tested by Agents, Trusted by Whom?": https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/
- Hard Boiled Software podcast ep. 005 with Adam Dymitruk (event modeling as AI's missing link): https://newsletter.nerdnoir.com/p/event-modeling-the-blueprint-for
- Martin Dilger / eventmodelers.ai: https://www.eventmodelers.ai/ and https://app.eventmodelers.ai/
- Dilger, Understanding Eventsourcing: https://eventsourcingbook.com/
- SE Radio 720, Martin Dilger on Understanding Eventsourcing: https://se-radio.net/2026/05/se-radio-720-martin-dilger-on-understanding-eventsourcing/
- Critter Stack Roadmap March 2026 (Marten 9.0 removed runtime codegen; AI skills): https://jeremydmiller.com/2026/03/18/critter-stack-roadmap-for-march-2026/

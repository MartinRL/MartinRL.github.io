---
title: "The Screens Left the Repo, and Nothing Replaced Them"
description: "Part one moved generated code inside the compiler. This time there is no generated code at all: the UI is the spec, interpreted at request time."
created: 2026-08-23
status: draft
---

# The Screens Left the Repo, and Nothing Replaced Them

> Part one deleted code the compiler regenerates on every build. This time 1,734 lines left git and nothing regenerates them, ever. The screens are evaluated from the spec, per request.

## Previously, on the repo boundary

["The Spec Is the Product" Is a Slogan Until the Code Leaves Your Repo](the-spec-is-the-product.md) drew one rule and followed it until it hurt: never hand-maintain what a function of the spec can emit. In a small production workbench — three event-sourced multiplayer games behind one web front, 100% of the code agent-written — that rule ate three strata of C#. The domain vocabulary (every command, event, and business error), the `Given–When–Then` scenarios as xUnit facts, and the dispatch switches of the deciders all became in-compilation outputs of a Roslyn source generator: 2,754 lines out of git, 708 lines of generator in, 115 tests with no file anywhere on disk, drift unrepresentable because the derived representation has no independent existence.

The mechanism had a signature: a deterministic *generator*, running at *build time*, verified by the *compiler*. A fake event added to the spec fails the next build with [**CS8795**: _Partial member must have an implementation part because it has accessibility modifiers._](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-messages/partial-declarations#partial-methods) and the name of the method a human now owes; that seam was the whole argument.

The rule does not stop walking because the next stratum looks different. The next stratum was the UI — nineteen hand-written Razor screens across the three games — and under it, the mechanism changed. This article is about what it changed into, because the answer was not "generate the screens too."

## The ring outside the blueprint

[Software Civil Engineering](software-civil-engineering.md) argued that a specification worth the name has four layers, and drew them as rings:

![The four specification layers: Event Model inside Experience Model inside Operational Model inside Policy Model](four-spec-layers.svg)

*The four layers. Part one industrialized the inner ring. This article is about the second.*

Part one lived entirely in the inner ring. An event model states what the system *does*: commands, events, views, scenarios. It deliberately says nothing about what anyone *sees* — which fields matter most on which screen, for whom, in what order, under what name, in what typeface. That is the Experience Model's ring: how humans inhabit the system. Civil engineering splits these professions for a reason; the structural engineer certifies the building will not fall down, the architect ensures people can inhabit it.

The question was whether that ring can be a formal spec at all, and a [prior research pass through thirty years of model-based UI](machine-readable-ux-specs-research.md) returned a precise answer: yes, exactly as far as the *abstract* UI — composition, data binding, salience, naming — all the way and deterministically, and not one step further. Every machine-readable UI system that ever shipped at industrial scale (server-driven UI, Adaptive Cards, JSON Forms) obeys the same constraint: it determines composition over a closed, hand-built component vocabulary, and it never determines what a component looks like. The doctrine that fell out is one sentence: **the experience model records judgment as data, never as geometry.** Memberships, orderings, tiers, names, and design tokens are in; coordinates, containers, and breakpoints are out.

So the workbench got a second spec dialect, [xmlang](https://github.com/MartinRL/xmlang), an experience-model sibling to the event-model dialect with a strictly one-way dependency: every xm element references event-model elements — surfaces compose views and commands, journeys traverse slices — and the event model never references back. The layering paid for itself before a single screen was rendered: the first thing writing an xm surfaced was that surface judgment had been quietly colonizing the event model's *naming layer* — views named `Screen / Auction lobby` instead of by the data they carry. With somewhere legitimate for that judgment to live, the views in all three event models were renamed to bare data nouns (`Roster`, `Round scores`, `Scoreboard`), and the inner ring got purer by acquiring a neighbor.

## Experience judgment, as data

Here is what one game's worth of that judgment looks like. Blindbudet is a sealed-bid auction: hidden bids, overbids disqualified, highest valid bid wins. Its entire experience model is 255 lines of YAML; this is the round-results pair:

```yaml
RundresultatVärd:
  during: [started]
  for: [Värd]
  compose:
    - v: Round scores
      self: playerProfits.playerId
      fields:
        primary: [trueWorth, winnerIds, playerProfits]
        secondary: [pricePaid, lotIndex]
        on-demand: [gameId]
    - c: AskNextLot
      prominence: primary
    - c: EndAuction
      prominence: primary

RundresultatSpelare:
  during: [started]
  for: [Spelare]
  compose:
    - v: Round scores
      self: playerProfits.playerId
      fields:
        primary: [trueWorth, winnerIds, playerProfits]
        secondary: [pricePaid, lotIndex]
        on-demand: [gameId]
```

Read what is stated: this surface exists during the `started` phase, for the host persona; it composes the `Round scores` view (a name from the event model — a dangling reference here is a build error); the true worth and the winners are primary, the price paid is secondary, the game id is on-demand; the viewer recognizes themself by `playerId`; the host gets the two pacing commands and the player, composing the *same view* a second time, gets none. Read what is absent: no pixels, no columns, no breakpoints, no component names. The spec also carries every string a human reads, down to the empty states —

```yaml
"Round scores":
  winnerIds:
    $empty: Ingen vann – alla bjöd över.
```

— and the sanctioned visual vocabulary as DTCG design tokens transcribed from the live stylesheet. Who sees what, when, in what order, under what name, in which palette: judgment as data. How it is laid out: someone else's job. Whose, is the interesting part.

> [!todo] Visual: same spec, two screens
> Screenshot pair (preferred) or abstract wireframe pair of the host and player round-results screens as the interpreter materializes them from the YAML above: the same `Round scores` view composed twice, host with the two pacing commands, player with none; primary prominent, secondary quieter, on-demand behind disclosure.
> Caption must say this is *one possible materialization*; the geometry belongs to the interpreter, not the spec. Real screenshots keep the "no geometry in the spec" doctrine intact; a wireframe risks reading as layout the spec supposedly contains.

## Generate, or interpret

Part one's ladder ranked every approach by two properties: who transforms, and what verifies. The obvious continuation was more of the same — write a generator that emits `.razor` into the compilation, let the compiler verify it, delete the screens. That was the plan right up until it wasn't, because presentation has a property the domain strata don't: **one transformer's judgment serves every game.** The rendering decisions — how a salience tier becomes disclosure, how a roster becomes a card, where commands sit relative to content — are identical across the auction game, the quiz game, and the arithmetic game, and should be identical across game four. A generator would stamp three frozen copies of that judgment into three compilations, each aging from the moment of generation. An interpreter keeps one copy, executing at request time: improve the transformer once, and every screen of every game improves at the next deploy.

```mermaid
flowchart TB
    GEN ~~~ INT
    subgraph GEN ["Generate (rejected)"]
        direction TB
        GS["xm specs, one per game"] --> G["generator, build time"]
        G --> C1["auction compilation<br/>judgment copy 1<br/>frozen at generation"]
        G --> C2["quiz compilation<br/>judgment copy 2<br/>frozen at generation"]
        G --> C3["arithmetic compilation<br/>judgment copy 3<br/>frozen at generation"]
    end
    subgraph INT ["Interpret (chosen)"]
        direction TB
        IS["xm specs, one per game"] --> I["interpreter, request time<br/>the only copy of the<br/>rendering judgment"]
        I --> S1["auction screens"]
        I --> S2["quiz screens"]
        I --> S3["arithmetic screens"]
        I -.-> S4["game four<br/>zero screens"]
    end
```

*The fork. A generator stamps the rendering judgment into each compilation, where it ages from the moment of generation; the interpreter holds one living copy that every screen of every game runs through per request. Improve it once and everything improves at the next deploy.*

So the screens are not generated. They are *interpreted*. A shared runtime — 369 lines of Razor components with a hard rule that no game name may appear in them — walks the xm surface and renders it: primary fields prominent, secondary fields quieter, on-demand fields behind a `<details>`, commands after content, labels and empty states and tokens straight from the spec. There is no per-screen artifact anywhere: not on disk, not in the compilation, not cached between requests. Part one told three acts of .NET code generation — the comment fence, the Designer file, the in-compilation source generator — each act moving the generated artifact somewhere harder to edit. Act three put it where no one could edit it. Act four is shorter: **there is no artifact.** The repo-boundary argument reaches its fixed point, because you cannot commit what is never materialized.

```mermaid
sequenceDiagram
    participant B as Browser
    participant H as Web host
    participant R as RundresultatVärd.razor<br/>(1 of 19 screens, in git)
    participant S as Live game state
    B->>H: GET round results
    H->>R: render
    R->>S: read
    S-->>R: state
    Note over R: placement, ordering, phrasing,<br/>plumbing: baked into markup
    R-->>B: HTML
```

```mermaid
sequenceDiagram
    participant B as Browser
    participant H as Web host
    participant M as Materializer<br/>(per-game residue)
    participant I as Interpreter<br/>(shared, 369 lines)
    participant X as xm spec
    participant S as Live game state
    B->>H: GET round results
    H->>S: read
    S-->>H: state
    H->>M: (state, viewer)
    M-->>H: surface name + field bag
    H->>I: render surface
    I->>X: tiers, order, labels,<br/>empty states, tokens
    X-->>I: judgment as data
    Note over I: no per-screen artifact:<br/>not on disk, not compiled, not cached
    I-->>B: HTML
```

*The same request, before and after the cut-over. The lifeline that vanished is the per-screen artifact; what stands in its place is not another artifact but a computation over the spec, the residue, and live state, performed at the moment of asking.*

This is not an exotic move; it is the oldest one in the stack. Nobody generates per-page rendering code from HTML — the browser is an interpreter of a declarative spec, and improving the browser improves every page ever written. The xm interpreter is that, one level up, for one product family.

Honesty about the second property, though, because it genuinely changed: **what verifies is no longer the compiler.** No [CS8795](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-messages/partial-declarations#partial-methods) fires when a surface references a view that doesn't exist. Three oracles stand where the compiler stood:

1. **Lint at startup.** The web host parses and lints each spec pair as it boots and throws on any error — a dangling xm→em reference, a mislabeled field — naming the rule and the element. The deploy fails; a broken screen never renders. The seam still screams with a name; it just screams at boot time instead of build time.
2. **Characterization tests.** Forty-seven endpoint tests pin semantic markers — the overbid strike-through, the shared-win line, the descending final table — against the rendered output. They were written against the hand-written screens *first*, then the interpreter was required to pass them unchanged: the old UI's behavior became the oracle for its own replacement, and only when parity was green did the screens leave git.
3. **A closed vocabulary.** The interpreter renders exactly six field kinds — text, roster, table, magnitude bars, QR, steps — as a sealed union. A new kind is a plan-level decision, never a per-feature accretion. Closure is what keeps the interpreter reviewable the way part one's generator was reviewable: once.

> [!todo] Visual: where the seam screams, a lifecycle timeline
> Two rows over the stations plan → build/CI → boot → request. Part one's row: the compiler at build (CS8795), nothing needed later. Part two's row: closed vocabulary at plan level, characterization suite at CI, lint at boot, nothing at request. Shade the unguarded rightmost station; the figure should show honestly what moved right, which is exactly what the next paragraph prices.

Weaker than a compile error? At the margin, yes, and it should be said plainly: a generator's failures cannot leave the build machine, an interpreter's failures are runtime failures held back by a boot-time gate. That is the price of one living copy of the design judgment, and I think the trade is right for exactly the reason the guarantee is weaker — the judgment keeps executing, so it can keep improving.

There is a symmetry here worth naming. Part one cited Gîrba and Wardley's [Rewilding Software Engineering](https://medium.com/feenk/rewilding-software-engineering-900ca95ebc8c), whose cure for stale developer-facing views is derivation at *read time*: regenerate every view from the system on demand, so it cannot lie. Part one was the build-time answer on the write side — derive the system from the spec. The interpreter closes the square: derivation at read time, on the *shipped* side. Every screen a player sees is a contextual view over live game state and the spec, computed at the moment of asking. It cannot be stale, cannot drift from the spec, cannot disagree with the event model — for the same reason in every case: it has no independent existence to disagree *from*.

> [!todo] Visual: the rewilding square
> The prose says "closes the square", so draw it: a 2×2 of write side vs read side against build time vs read time. Part one at write/build (derive the system from the spec), Rewilding at read time for developer-facing views, this interpreter at read time on the shipped side. Decide what the fourth cell is (or mark it deliberately empty); the figure should make "same reason in every case: no independent existence" legible at a glance.

## The ledger, honestly

Three cut-over commits, one per game, each landing only after the parity suite was green on the interpreter path: −646 lines (the auction game: eight screens plus their view-models), −477 (the arithmetic game: six screens), −611 (the quiz game: five screens plus its form and screen layer). Nineteen screens, 1,734 lines of presentation code out of git.

What came in: the 369-line shared interpreter, a 43-line startup catalog that loads and lints the specs, and — this is the number that keeps the ledger honest — 914 lines of per-game *residue*, one `Surfaces` file per game. Net, the repository shrank by only about 400 lines, and if that were the claim it would be a poor trade for a new dialect. The claim is about what kind of line survived. The deleted stratum was markup with judgment smeared through it: placement, ordering, phrasing, and plumbing, restated per screen, reviewable only by rendering. The residue is judgment *only*, as pure functions — `(state, viewer) → surface name`, `(state, labels) → field bag` — unit-testable without a browser, and the 800 lines of YAML became the readable surface where the ordering and phrasing actually live. The same accounting lesson as part one, which predicted 410 lines and got 150: the win was never the count. It was what each remaining line is *for*.

> [!todo] Visual: the ledger as a flow
> Sankey-style flow (SVG; mermaid sankey is beta) from "19 screens, 1,734 lines" into where the lines went: shared interpreter 369 (constant in games), startup catalog 43, per-game residue 914, with the ~800 lines of xm YAML entering as the new readable surface. Color by kind: restatement (deleted) vs judgment (kept). The figure carries the section's point that the win is what each surviving line is for, not the count.

And the interpreter is constant in the number of games. Game four ships its in-game UI as roughly 250 lines of xm YAML and a materializer file — zero screens.

## The residue report

Part one made a promise: the ghost of MDA is patient, and if the typed seams start filling with hand-maintained metadata, the correct move is to write *that* article. This is the inspection visit, one stratum later, and the seams contain exactly what they were designed for — but "what they were designed for" turned out to be worth designing. Three contracts hold the boundary between spec and residue:

**The presence contract.** The xm owns field order and tier; the materializer owns *presence*. When the bid screen omits the lot's `description` and `unit` from the field bag because they are hoisted into the heading and the keypad label, that is a deliberate, unit-tested judgment — never a rendering fallback:

```csharp
// description/unit are hoisted into the heading + keypad; totalLots is composed into
// the lotIndex pill copy — the presence contract's deliberate omissions.
var fields = new Dictionary<string, Field>
{
    ["lotIndex"] = new TextField($"Budrunda {i + 1} / {c.State.Lots.Count} · BlindBudet", "pill"),
};
```

**The defaults contract.** Commands that compose no view — the create-auction and join forms — are not surfaces at all; the transformer serves its own default form for them, built from the spec's labels. The strict compose rule *predicted* which two forms in the shipped UI would be bare, which is the pleasant experience of a spec telling you something about your product you hadn't stated.

**Derived behavior, not vocabulary.** The polling rule — which screens auto-refresh — is not in the spec, because it is derivable: poll exactly when the surface has no typed input and the game isn't over. The bid screen's materializer carries the whole rationale in one line: *"No PollPath: typed-input surface — polling would wipe a half-entered bid."* Where part one's rule was "never hand-maintain what a function of the spec can emit," the xm added its dual: never *specify* what a function of the spec can derive.

And where judgment is genuinely concrete — the numeric keypad for secret bids, the quiz game's two-stage direction-then-difference input with its live magnitude bars, the arithmetic game's counting-tape puzzle surface, the host's round-count slider — the design opts *out*. Whole surfaces, handed back to hand-written Razor, selected by name in one pure function. This is act three's answer to the last 20%, relocated: not a protected region rotting *inside* generated output, but a named boundary *beside* the derivation. Three games in, the opt-out list is short, stable, and every entry on it is a place where the product is genuinely, deliberately unlike a default — which is exactly what a residue should contain.

> [!todo] Visual: the ownership map of the second ring
> One diagram of who owns what across the boundary the three contracts draw: the xm spec (composition, tiers, order, names, copy, tokens), the materializers (presence, hoisting, state-composed phrasing, surface selection), the interpreter (geometry, disclosure, the six-kind vocabulary), the named opt-outs (keypad, magnitude bars, counting tape, slider). Territory map or layered boxes; this is the densest section in the article and the map is its summary.

## The dialect left the repo too

One more thing left git, and it was not code the spec derives — it was the machinery of the spec itself. xmlang's specification, parser, linter, and CLI began life inside the workbench, 557 lines of in-repo source. They now live in [their own repository](https://github.com/MartinRL/xmlang) under MIT, and the workbench consumes them as a NuGet package, the way it consumes the compiler. Part one's economics said: review the transformer once, then trust regeneration. Extraction is that sentence taken literally — the transformer became a versioned dependency with its own spec, its own test suite, and its own release discipline, reviewable by anyone, upgradeable like any package. A spec dialect that survives being extracted from its birthplace is some evidence it was a notation and not a local convention.

## Time to answer, time to question

Wardley has been insisting the industry fails to measure the two metrics that matter: ttA, time to answer, and ttQ, time to question. Reading code, he argues, has been bankrupt as a method of understanding systems of significant size for a decade — and having an LLM read it for you creates dependency, not understanding. The strata this project keeps deleting are precisely the strata about which questions used to require reading code.

"What does a player see mid-auction before they've bid, versus after?" used to be a tour of eight Razor files; it is now ten lines of YAML and a sixteen-line selector function. "Does any screen show data no event carries?" is not a question anymore; the boot-time lint answers it before the deploy completes. "What is the empty-state copy when everyone overbids?" is a one-line grep of the spec. ttA collapsed because the answers are small and declarative; ttQ collapsed with it, because a spec you can hold in your head is a spec you can cheaply interrogate — 800 lines of YAML currently carry the entire experience layer of three shipped games. Rewilding's premise is that systems stay too large to grasp and tooling must adapt to them; the premise here is that for the derivable strata, graspable-by-construction is achievable. Both are true, stratum by stratum, and the second keeps shrinking the territory where only the first can help.

## What is still in git

The metric from part one stands: lines in git that restate a spec, driven toward zero, ledger published each time. The candidates left are the usual suspects of pure structure — projection plumbing, serialization surfaces, an API contract if the product ever grows one. The materializers are *not* on the list, and the distinction is the whole discipline: they do not restate the spec, they state what the spec deliberately refuses to — presence, hoisting, phrasing composed from live state. Deleting restatement is the program; deleting judgment would just be losing the product.

## Where I might be wrong

**Vocabulary pressure is patient too.** Six field kinds survived three games, but every future game will arrive with a lobbyist for a seventh. The vocabulary only stays closed while additions are plan-level decisions; the day a field kind lands to unblock a feature branch, the interpreter has begun its career as a UI framework, and UI frameworks do not stay at 369 lines.

**The transformer is the design authority, and that is a choice.** This whole trade closes only if you accept the interpreter's rendering judgment as *the* design and reserve hand-written surfaces for genuine exceptions. A brand-first product whose designers own every screen would invert the ratio — all opt-out, no default — and the economics collapse. The claim is scoped: where a house style should be uniform, uniform-by-construction beats uniform-by-review.

**Concentration cuts both ways.** The interpreter is trusted the way a compiler is trusted, but it is not a compiler: it is 369 lines reviewed by one team, and a bug in it is a bug on every screen of every game simultaneously. The parity suite guards the screens it characterized; game four's screens are guarded by transitivity and hope until they get characterization tests of their own. The honest phrasing: I traded many small chances of drift for one small chance of systemic error, and I believe the arithmetic favors the trade without having proven it.

## Two verbs

Part one ended with three strata that exist only as functions of the specs, and a definition: "the spec is the product" means the spec is the only place those strata exist at all. The experience layer now has the same property with a different verb. The domain strata are *compiled* from the spec — derived once per build, verified by the compiler, materialized only inside a compilation. The screens are *interpreted* from the spec — derived per request, verified by a boot-time linter and a characterization suite, materialized never. Same rule, both times: the representation cannot drift, because it does not independently exist.

The inner ring compiles. The second ring interprets. Two rings remain, and the rule is still walking.

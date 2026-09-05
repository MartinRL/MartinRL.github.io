# Fact check: Kiro, Spec Kit, OpenSpec (2026-09-05)

All three: markdown spec in, LLM agent transforms, ordinary source code committed. None deterministic. None keeps spec and code coupled by a mechanism.

## Kiro (AWS)
- Three files per spec: requirements.md (user stories + EARS acceptance criteria: WHEN … THE SYSTEM SHALL …), design.md, tasks.md. https://kiro.dev/docs/specs/
- Specs "designed to be version-controlled … alongside the code they describe". Sync = git discipline, no mechanism. https://kiro.dev/docs/specs/best-practices/
- Böckeler: spec-first only, excessive docs even for minor bugs.

## GitHub Spec Kit
- Commands: constitution, specify, plan, tasks, implement, converge ("assess the codebase against spec/plan/tasks and append remaining work as new tasks"), plus clarify, analyze, checklist. https://github.com/github/spec-kit
- "specifications become executable, directly generating working implementations". Executable = an LLM reads them.
- Converge is drift repair by LLM: rung 2½ in tool form.
- Scott Logic, Colin Eberhardt, 2025-11-26: "a sea of markdown documents, long agent run-times and unexpected friction"; module contract 4x the length of the implemented module; implement step 8 min for ~700 lines/14 files; iterative approach "around ten times faster"; "Spec Kit drags you right back into the past!" https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html

## OpenSpec (Fission-AI)
- openspec/changes/<name>/: proposal.md, specs/ (SHALL + WHEN/THEN scenarios in markdown), design.md, tasks.md; archive after apply. https://github.com/Fission-AI/OpenSpec
- "Plain Markdown … no special syntax to learn." Selling point is exactly the no-oracle property.
- Spec-anchored in intent; sync manual. Verify does not block archive; scenarios optional (per codemyspec, biased source).

## Böckeler, martinfowler.com, 2025-10-15: "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl"
https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- Spectrum: spec-first, spec-anchored, spec-as-source (code generated, not manually edited).
- Only Tessl attempts spec-as-source; marks output "// GENERATED FROM SPEC - DO NOT EDIT" (= act one, the comment fence).
- Unsolved per her: non-determinism from identical specs; agent compliance; functional vs technical spec confusion; problem-size fit.
- Warns spec-as-source risks repeating MDD failures, "inflexibility and non-determinism".
- spec-kit output "repetitive, both with each other, and with the code that already existed".

## Tessl
- Aspires spec-as-source; engine non-deterministic from identical specs; closed beta (per codemyspec).

## Use in article
- Böckeler named the rung (spec-as-source) and named the two failure modes (non-determinism, MDD ghost). The two-stage rocket answers both: deterministic transformer, output not in repo. She stated the problem; the conclusion is undrawn.
- Gorman: EARS/markdown specs are long; Eberhardt's 4x contract is Gorman's token problem made visible.
- DHH: none of the three lets a non-engineer ship without an engineer PR; the output is a PR.

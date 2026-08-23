---
title: "Geometry experiment: probe scoring sheets"
description: "Raw rubric scores for the pre-registered xmlang geometry-prohibition experiment. C1 = baseline (v0.2 spec pair), C2 = treatment (v0.3 with slot:)."
created: 2026-08-23
tags: [xmlang, experiment, data]
---
# Probe scoring sheets

Protocol and rubric: [pre-registration](xmlang-geometry-experiment.md). Probe outputs: `kvissig.se/prototypes/geometry-probe/`. Each item scored 0/1 against the live design; evidence is quoted from the produced DOM/render code.

## C1 — baseline (v0.2 spec pair), 2026-08-23

| # | Rubric item | run1 | run2 | run3 |
|---|---|---|---|---|
| 1 | Commands below all view content on every surface | 0 | 0 | 0 |
| 2 | Secondary scalars as pills near the heading | 0 | 0 | 0 |
| 3 | On-demand behind disclosure, closed by default | 1 | 1 | 1 |
| 4 | Primary fields dominant and first | 1 | 1 | 1 |
| 5 | Single-column stack per persona frame | 1 | 1 | 1 |
| 6 | Surface label renders first | 1 | 1 | 1 |
| 7 | LobbyVärd: join affordance above roster | 1 | 1 | 1 |
| 8 | Rundresultat: trueWorth above profit list | 1 | 1 | 1 |
| | **Total** | **6/8** | **6/8** | **6/8** |

### Evidence, item 1 (0/3)

All three runs place the on-demand `<details>` (view content) BELOW the command buttons on at least one surface; the live design renders on-demand before commands.

- run1 `renderBudgivning`: `<div class="actions">…PlaceBid…</div>` then `${odBlock(...)}`; same in `renderRundresultat`. Internally inconsistent: `renderLobbyVard` has `odBlock` BEFORE `.actions`.
- run2 `surfLobbyVard`/`surfBudgivning`/`surfRundresultat`: `<button class="cta">` then `<details class="ondemand">`.
- run3 `LobbyVärd`/`Budgivning`/`rundresultat`: `btn-primary` then `${onDemand(...)}`.

### Evidence, item 2 (0/3)

Live: secondary scalar fields render as compact pills in the header area near the heading.

- run1: secondary = `.sec` muted text lines inside body cards below primary content ("Svara i … · Budrunda 1 av 2").
- run2: secondary = `.secondary-txt` centered muted lines placed mid/below content.
- run3: secondary = `.chip` pills (form matches live) but placed at the BOTTOM of/after body cards, not near the heading.

The three runs also disagree with each other on form (text lines vs chips): genuine transformer variance, not merely shared divergence from live.

### Items 3–8 (3/3 each)

All runs: `<details>` without `open`; primary tier in display font 1.5–2.4rem first in the body; 330–340px single-column phone frames; `<h2>` surface heading first; LobbyVärd join code (run2/run3 with a QR/dashed-code card) above the roster; Rundresultat trueWorth as the largest number above the per-player table.

### C1 verdict

No early exit: items 1 and 2 are baseline-variable (0/3 against live; inter-run disagreement on item 2's form, intra-run inconsistency on item 1 in run1). These are precisely region-placement decisions — the treatment (`slot:`) targets them directly. Proceed to Phase 2.

## C2 — treatment (v0.3 spec pair)

_Pending._

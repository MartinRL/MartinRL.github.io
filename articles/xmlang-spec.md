---
title: "xmlang Specification v0.1.0 (draft)"
description: "A YAML-based DSL for Experience Models: the sibling dialect to emlang, recording UX judgment as data, never as geometry"
created: 2026-07-11
tags: [spec, xmlang, emlang, experience-modeling, event-modeling, ux]
---
# xmlang Specification v0.1.0 (draft)

xmlang is a YAML-based DSL for describing the Experience Model of an event-modeled system. An Experience Model records the UX judgments an Event Model deliberately omits (personas, surface composition, salience, journeys, labels, tokens) and depends on the Event Model strictly one-way. It is the sibling dialect to [emlang](https://github.com/emlang-project/spec); the rationale is in [How Far Does a Machine-Readable UX Spec Go?](machine-readable-ux-specs-research.md).

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

## Overview

- An xmlang file MUST be a valid YAML file
- The RECOMMENDED file naming convention is `*.xm.yaml`, alongside the Event Model's `*.emlang.yaml`
- The root object MAY contain the keys `model`, `personas`, `surfaces`, `journeys`, `labels`, and `tokens`
- The root object MUST NOT contain other keys
- Every root key is OPTIONAL: an Experience Model is adopted judgment by judgment, and an empty document is a valid (vacuous) Experience Model
- A file MAY contain multiple YAML documents separated by `---`; each MUST independently conform to this specification

```yaml
---
model: billing.emlang.yaml

personas:
  Accountant:
    role: Accountant

surfaces:
  Dashboard:
    compose:
      - v: OutstandingInvoices
      - v: RecentPayments
      - c: PayInvoice
```

## The one-way dependency rule

- Every reference from an Experience Model to an Event Model element (view, command, slice, field, swimlane) MUST resolve against the Event Model
- A dangling reference MUST be reported as an error by conforming tools
- The Event Model MUST NOT reference the Experience Model; nothing in this specification is visible from emlang
- The `model` key names the Event Model document(s) references resolve against
- `model` MUST be a string or a list of strings (paths or URIs of emlang documents)
- If `model` is absent, tools MAY resolve references against a model supplied out of band (e.g. a CLI argument), and MUST report an error if no model is available while references exist

```yaml
# ✅ Valid
model: billing.emlang.yaml

# ✅ Valid
model:
  - billing.emlang.yaml
  - onboarding.emlang.yaml
```

## The geometry prohibition

The single rule that separates xmlang from every failed Model-Based UI dialect: **an Experience Model records judgment as data, never as geometry.**

- Memberships, orderings, tiers, names, and tokens are expressible
- Coordinates, dimensions, grids, containers, and breakpoints are NOT expressible; this specification defines no geometric vocabulary and future versions MUST NOT add one
- List order in this specification expresses precedence of importance, never spatial position
- Conforming tools MUST NOT interpret any `props` content as geometry
- Arrangement of composed elements on a rendered surface is out of scope by design: it belongs to the concrete-UI stratum (agents and humans), pinned by generated verification, not to the model

## Personas

- `personas` MUST be an object mapping persona names to persona definitions
- A persona definition MAY be empty (null value in YAML)
- A persona MAY contain a `role` key attaching it to an Event Model swimlane
- `role` MUST be a string matching a swimlane used in the Event Model; a non-matching `role` SHOULD be reported as a warning (swimlanes are optional in emlang)
- A persona MAY contain a `props` key; `props` is free-form (goals, device, context, accessibility needs)
- A persona MUST NOT contain keys other than `role` and `props`

```yaml
personas:
  Accountant:
    role: Accountant
    props:
      goal: close the books by the 5th
      device: desktop, dual monitor
      accessibility: keyboard-first

  Auditor:
    role: Accountant   # two personas MAY share one swimlane role
```

## Surfaces

A surface is what the user has in front of her (a screen, modal, drawer, card, or chat pane); the noun is deliberately modality-neutral.

- `surfaces` MUST be an object mapping surface names to surface definitions
- A surface definition MUST contain a `compose` key and MAY contain `for` and `props` keys, and MUST NOT contain other keys
- `for` MUST be a list of persona names declared under `personas`; if absent, the surface applies to all personas
- `compose` MUST be a list of composition items
- A composition item MUST contain exactly one of `v:` (a view) or `c:` (a command), referencing an Event Model element
- `compose` MUST contain at least one view item and MAY contain command items; a surface composing no view MUST be reported as an error (a bare command form is not a composable surface; it is served by the generator's defaults)
- Item order within `compose` expresses descending importance, not position

### View items and field salience

- A view item MAY contain a `fields` key classifying the view's fields into salience tiers
- `fields` MUST be an object whose keys are drawn from `primary`, `secondary`, and `on-demand`, each holding a list of field names from the view's `props` in the Event Model
- A field not listed in any tier defaults to `primary`
- A field name not present on the referenced view MUST be reported as an error

### Command items and action prominence

- A command item MAY contain a `prominence` key
- `prominence` MUST be one of `primary`, `secondary`, or `overflow`
- If absent, `prominence` defaults to `primary`

```yaml
surfaces:
  Dashboard:
    for: [Accountant]
    compose:
      - v: OutstandingInvoices
        fields:
          primary: [amount, dueDate]
          secondary: [invoiceNumber]
          on-demand: [auditTrail]
      - v: CashPosition
      - v: RecentPayments
        fields:
          secondary: [payer, method]
      - c: PayInvoice
        prominence: primary
      - c: ExportCsv
        prominence: overflow
```

- A view or command not composed onto any surface remains reachable through the generator's defaults (see Defaults); composition restricts nothing, it only aggregates

## Journeys

- `journeys` MUST be an object mapping journey names to journey definitions
- A journey definition MUST contain a `slices` key and MAY contain `for` and `props` keys, and MUST NOT contain other keys
- `slices` MUST be a non-empty list of slice names defined in the Event Model, in traversal order
- `for` MUST be a list of persona names declared under `personas`; if absent, the journey applies to all personas
- A journey is the material for generated cross-slice walkthrough tests: conforming generators SHOULD chain the per-slice generated scenarios in journey order

```yaml
journeys:
  MonthEndClose:
    for: [Accountant]
    slices:
      - ReviewOutstandingInvoices
      - PayInvoice
      - ExportMonthlyReport
```

## Labels

- `labels` MUST be an object mapping locale tags ([BCP 47](https://www.rfc-editor.org/rfc/rfc5646)) to label maps
- A label map MUST be an object mapping reference paths to human-facing strings
- A reference path MUST be one of:
  - a command, view, surface, journey, or persona name (e.g. `PayInvoice`)
  - a dotted field path on a view or command (e.g. `OutstandingInvoices.amount`)
- A reference path that resolves to nothing MUST be reported as an error
- A label map MAY contain a `register` key with a free-form value describing the copy register (e.g. formal, informal)
- Labels are the source of accessible names in generated verification (aria snapshot baselines); an element without a label defaults to its Event Model name

```yaml
labels:
  en:
    register: formal
    PayInvoice: Pay invoice
    OutstandingInvoices.amount: Amount due
  da:
    PayInvoice: Betal faktura
```

## Tokens

- `tokens` MUST be an object conforming to the [Design Tokens Format Module](https://www.designtokens.org/tr/drafts/format/) (DTCG), using `$type` and `$value`
- Tokens are the sanctioned visual vocabulary: conforming generators SHOULD emit them as the design-token file, and token lint in the verification harness SHOULD treat any value outside this vocabulary as a violation
- This specification imposes no structure beyond DTCG conformance

```yaml
tokens:
  color:
    brand:
      $type: color
      $value: "#0B5FFF"
  spacing:
    md:
      $type: dimension
      $value: 16px
```

## Defaults

An Experience Model refines a default experience; it never creates the experience from nothing. In the absence of a section (or of the whole file), conforming generators MUST apply:

| Absent | Default |
|---|---|
| `personas` | One implicit persona per Event Model swimlane |
| `surfaces` | One surface per slice; every field `primary`; every action `primary` |
| `journeys` | No cross-slice walks; per-slice scenarios only |
| `labels` | Event Model names as labels and accessible names |
| `tokens` | No token file; token lint inert |

This is exactly the wireframe: the Event Model alone determines the default experience, and each Experience Model entry replaces one informal artifact (a persona doc, a sitemap, a journey map) with machine-leveraged data.

## Lint rules

Conforming tools SHOULD implement at least:

| Rule | Severity | Meaning |
|---|---|---|
| `xm-dangling-ref` | error | A referenced view, command, slice, or field does not exist in the Event Model |
| `xm-unknown-persona` | error | A `for` list names an undeclared persona |
| `xm-orphan-label` | error | A label path resolves to no Event Model or Experience Model element |
| `xm-unknown-role` | warning | A persona `role` matches no swimlane in the Event Model |
| `xm-surface-without-view` | error | A surface composes no view (bare command forms fall back to defaults) |
| `xm-surface-shadows-view` | warning | A surface name equals an Event Model view name; the Event Model likely modeled a surface instead of data |

## Document structure

- A file MAY contain one or more YAML documents separated by `---`
- Each document MUST independently conform to this specification
- Tools MAY merge documents; a name collision within `personas`, `surfaces`, or `journeys` across merged documents MUST be reported as an error

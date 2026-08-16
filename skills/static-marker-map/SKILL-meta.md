---
title: "Static Marker Map Meta"
purpose: "Meta documentation for the static-marker-map skill."
audience:
  - content-authors
tags:
  - skill-meta
  - static-marker-map
authors:
  - asokolsky@gmail.com
created-at: "2026-06-04T12:19:05-07:00"
updated-at: "2026-08-16T00:00:00-07:00"
---

# Static Marker Map Meta

Meta documentation for [the static-marker-map skill](./SKILL.md).

## Relationship To Existing Standards

The skill follows the Agent Skills specification for its package and
frontmatter shape. It preserves this repo's source-first generated-artifact
practice and uses GeoJSON as the normalized point-data interchange format.

## Dependencies

| Dependency | Source | Install |
|---|---|---|
| Python 3 | [Python](https://www.python.org/) | Use the platform package manager or the repo's configured tool manager. |

Python 3 is used in workflow step 3. The bundled script receives GeoJSON or CSV
and produces static HTML. If Python 3 is unavailable, stop and report the
missing dependency rather than hand-editing a large generated artifact.

Generated maps load Leaflet 1.9.4 and OpenStreetMap tiles at viewing time. They
need network access unless the caller adapts the generated output to local
assets, as documented in `SKILL.md`.

## Departures And Rationale

None.

## Update Cadence

Review annually, when the Agent Skills specification changes, or when the
bundled generator's runtime or external map assets change.

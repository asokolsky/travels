---
title: "Anchored Source Citations Meta"
purpose: "Meta documentation for the anchored-source-citations skill."
audience:
  - content-authors
tags:
  - skill-meta
  - anchored-source-citations
authors:
  - asokolsky@gmail.com
created-at: "2026-06-19T10:36:22-07:00"
updated-at: "2026-08-16T00:00:00-07:00"
---

# Anchored Source Citations Meta

Meta documentation for [the anchored-source-citations skill](./SKILL.md).

## Relationship To Existing Standards

The skill follows the Agent Skills specification for its package and
frontmatter shape. It applies this repo's explicit `source-N` anchor convention
and source-verification rules to Markdown citation work.

## Dependencies

None. This skill is self-contained. Live source verification uses the agent
runtime's available network and browsing capability rather than requiring a
specific external skill or CLI.

## Departures And Rationale

None.

## Update Cadence

Review annually, when the Agent Skills specification changes, or when this
repo's citation conventions change.

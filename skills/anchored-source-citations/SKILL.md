---
name: anchored-source-citations
description: Create and repair source-backed Markdown citations using clickable numbered references and matching explicit source anchors. Use when editing Markdown that needs stable numbered citations, current-fact verification, or citation and link cleanup. Skip when the document does not use source-backed claims or its local rules require another citation format.
metadata:
  version: "1.0.1"
  source: "https://github.com/asokolsky/travels/tree/main/skills/anchored-source-citations"
---

# Anchored Source Citations

Use stable, explicit Markdown anchors for citations so rendered pages stay
readable, sources are easy to audit, and references continue to work after
Jekyll or other static-site rendering.

## Citation Shape

Use inline citations that render as bracketed numbers:

```markdown
As of June 19, 2026, Italy treats physical presence for most of the tax year
as an independent tax-residency test. [[1]](#source-1)
```

Then define the matching source entry with an explicit HTML anchor:

```markdown
## Source References

1. <a id="source-1"></a>[Normattiva: TUIR Article 2](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art2)
```

If the document already uses `## Sources`, `## Source References`, or another
clear source heading, preserve that heading unless the repo has a stronger local
rule.

## 1. Identify And Verify Claims

Identify claims that need support. Prioritize legal, financial, tax, travel,
medical, operational, price, schedule, and current-status facts. Prefer primary
sources for rules and operational facts: government pages, statutes, official
forms and instructions, transport operators, park sites, and source-of-truth
project docs. Use secondary sources for interpretation, restaurant opinions,
flavor, or when primary sources are unavailable.

Verify time-sensitive facts before writing them. When a current fact matters,
state the date explicitly, for example `As of June 19, 2026...`.

Skip condition: none when a claim requires a citation. Preserve already verified
claims when neither their content nor their sources have changed.

## 2. Add Anchored Citations

Add citations at the end of the sentence or paragraph they support. Do not cite
every sentence if one citation clearly supports the whole paragraph. Add one
numbered source entry per distinct source, with a stable `source-N` anchor.
Reuse an existing source number for repeated use of the same source.

Keep source titles descriptive enough to audit later. Include year, tax year,
effective date, or update date in the source title when relevant.

Skip condition: none.

## 3. Validate Citation Consistency

Run a consistency check before finishing:

- Every `[[N]](#source-N)` has exactly one matching
  `<a id="source-N"></a>` entry.
- Every source entry is cited from the body unless the user explicitly wants a
  bibliography.
- Numbering is sequential unless preserving existing numbering avoids churn.
- URLs are reachable when link verification is required or the facts are
  time-sensitive.

Skip condition: none.

## Repair Rules

- Replace bare URLs in body prose with source entries when the URL is evidence,
  not a navigational link.
- Preserve ordinary local navigation links as normal Markdown links. Do not put
  every internal page link into the source list.
- If a source is unreachable but the fact is important, either find a better
  source or leave a precise `TODO` naming the fact that still needs checking.
- Avoid markdown footnotes for this style; explicit anchors are more predictable
  across static-site renderers.
- Do not cite search-result pages as if they are sources. Link the actual
  article, official page, PDF, dataset, statute, or form.

## Example

Before:

```markdown
Plitvice Lakes uses timed-entry tickets. Check the park website.
```

After:

```markdown
As of August 16, 2026, Plitvice Lakes National Park recommends buying tickets
online in advance; online tickets must be validated at the selected entrance
within their specified time period. [[1]](#source-1)

## Source References

1. <a id="source-1"></a>[Plitvice Lakes National Park: 2026 ticket information](https://np-plitvicka-jezera.hr/en/plan-your-visit/istrazite-jezera/price-list/)
```

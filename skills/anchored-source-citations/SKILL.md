---
name: anchored-source-citations
description: Create and repair source-backed Markdown citations using clickable numbered references like `[[1]](#source-1)` and matching explicit source anchors. Use when Codex edits travel notes, legal or tax planning notes, research summaries, repo documentation, or any Markdown file that needs stable numbered citations, source-reference sections, current-fact verification, or citation/link cleanup.
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

## Workflow

1. Identify claims that need support. Prioritize legal, financial, tax, travel,
   medical, operational, price, schedule, and current-status facts.
2. Prefer primary sources for rules and operational facts: government pages,
   statutes, official forms/instructions, transport operators, park sites, and
   source-of-truth project docs. Use secondary sources for interpretation,
   restaurant opinions, flavor, or when primary sources are unavailable.
3. Verify time-sensitive facts before writing them. When a current fact matters,
   state the date explicitly, for example `As of June 19, 2026...`.
4. Add citations at the end of the sentence or paragraph they support. Do not
   cite every sentence if one citation clearly supports the whole paragraph.
5. Add one numbered source entry per distinct source, with a stable
   `source-N` anchor. Reuse an existing source number for repeated use of the
   same source.
6. Keep source titles descriptive enough to audit later. Include year,
   tax year, effective date, or update date in the source title when relevant.
7. Run a quick consistency check before finishing:
   - Every `[[N]](#source-N)` has exactly one matching
     `<a id="source-N"></a>` entry.
   - Every source entry is cited from the body unless the user explicitly wants
     a bibliography.
   - Numbering is sequential unless preserving existing numbering avoids churn.
   - URLs are reachable when link verification is required or the facts are
     time-sensitive.

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
Italy has a 7% pensioner regime. See TUIR Article 24-ter.
```

After:

```markdown
As of June 19, 2026, TUIR Article 24-ter allows qualifying holders of
foreign-source pension income who transfer residence to eligible municipalities
to elect a 7% substitute tax on qualifying foreign-source income. [[1]](#source-1)

## Source References

1. <a id="source-1"></a>[Normattiva: TUIR Article 24-ter, 7% pensioner regime](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art24ter)
```

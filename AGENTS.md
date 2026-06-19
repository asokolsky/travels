# AGENTS.md

## Project Purpose

This repository is a personal travel-planning workspace. Plans should be practical, opinionated, and source-backed, with a strong preference for Rick Steves-style priorities: fewer stops done well, early and late old-town time, and realistic travel days.

The current primary itinerary is `balkans.md`: a fast 5-day road trip from Dubrovnik, Croatia, to Trieste, Italy, via Mostar, Split or Trogir, Zadar, Rastoke, and Plitvice Lakes.

## Writing Style

- Write in Markdown.
- Keep plans skimmable: clear headings, short bullets, and concrete logistics.
- Lead each itinerary with assumptions such as trip length, transport mode, route direction, overnight bases, and maximum acceptable driving time.
- Use sections similar to the existing itinerary: route lens, route summary, day-by-day plan, practical car notes, and source references.
- For locations and attractions, prefer real Wikipedia article links on the first important mention in a section. If no real Wikipedia article exists, use a Google Maps place/search link labeled `map`, such as `Buza Bar ([map](...))`, so the place name does not look like it links to an article.
- When adding, repairing, or reviewing source-backed citations, use the repo-local skill at `skills/anchored-source-citations`.
- Use clickable numbered source references that render with square brackets, such as `[[1]](#source-1)`, and keep the `Source References` section in sync.
- In each `Source References` section, define a matching explicit source anchor on every source item, such as `1. <a id="source-1"></a>[Source title](https://example.com)`, so body citations jump to the relevant source.
- Preserve the existing plain, practical voice. Avoid marketing copy, generic travel fluff, and overloaded sightseeing lists.

## Travel Planning Priorities

- Favor Rick Steves public guidance and guidebook coverage when deciding what belongs in the route.
- Keep the itinerary humane. If the trip is short, make explicit tradeoffs instead of silently adding more stops.
- Protect mornings and evenings in major old towns when possible.
- Treat drive times as estimates, include border time where relevant, and flag days that are close to the stated driving limit.
- Use either/or language for overloaded days, such as "Split or Trogir", rather than implying everything can be done deeply.
- Include skip notes and contingency notes for tempting but unrealistic detours.

## Verification Rules

- Verify time-sensitive travel facts before changing them. This includes border controls, visa or entry rules, toll and vignette requirements, park hours, ticket systems, ferry schedules, restaurant openings, and car-rental cross-border rules.
- Prefer official sources for operational facts: park websites, government border pages, toll authorities, official tourism boards, and transport operators.
- When a fact is current as of the work date, say so explicitly in the itinerary, for example: "As of May 17, 2026..."
- Do not rely on older forum posts for current opening hours, prices, or legal requirements. Forum posts are acceptable for flavor, restaurant ideas, and qualitative trip-planning tradeoffs.
- For restaurant recommendations, note when public Rick Steves sources are thin and use reputable restaurant guides or official local tourism sources as secondary support.
- When checking Wikipedia links, do not rely only on HTTP status. A Wikipedia search page, `Special:Search` page, or "article does not exist" page can return `200` while still not being a real article.
- If a Wikipedia link for a place or attraction is broken or does not point to an existing article, replace it with the corresponding Google Maps place/search link labeled `map` instead of leaving a dead or search-result Wikipedia link.

## Itinerary Review Checklist

Before considering an itinerary update complete, check that:

- Each day has an estimated driving range and any relevant border caveat.
- Each day has a route map link, overnight recommendation, best stops, food notes, and skip or contingency guidance where useful.
- Cross-border rental-car permissions are called out for every non-Schengen or international segment.
- Toll and vignette requirements are included for countries where the route uses motorways or expressways.
- The plan does not hide long days behind optimistic drive times.
- Plitvice Lakes plans mention timed tickets, entrance strategy, route length, and whether the visit happens before or after a major drive.
- Source references are still accurate, reachable, numbered correctly, and linked with matching `#source-N` anchors.
- Broken, missing, or search-result Wikipedia links have been replaced with corresponding Google Maps place/search links.

## Editing Notes

- Keep unrelated travel ideas in separate Markdown files instead of expanding one itinerary into a catch-all.
- Avoid broad rewrites unless the user asks for a new route or a different trip length.
- When adding a new destination, explain what gets removed or compressed to make room.
- If live verification cannot be completed, leave a clear `TODO` with the exact fact that needs checking.

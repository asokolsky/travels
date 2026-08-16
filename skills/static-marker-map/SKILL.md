---
name: static-marker-map
description: Build shareable static browser maps from GeoJSON, CSV, KML-derived point data, or Markdown tables. Use when creating or repairing a many-marker map, replacing brittle Google Maps KML overlay links, generating Leaflet HTML, or validating marker counts and links. Skip when an ordinary place link or a small hand-authored map is sufficient.
metadata:
  version: "1.0.0"
  source: "https://github.com/asokolsky/travels/tree/main/skills/static-marker-map"
---

# Static Marker Map

Create lightweight map artifacts that work from a static site or a local file.
Prefer a generated Leaflet HTML map with inline GeoJSON point data, and keep
KML or GeoJSON as companion export/import files.

## 1. Inspect The Source Data

Inspect the source data and preserve the existing source of truth. If a repo
already has a generator, patch that generator instead of hand-editing only the
generated map.

Skip condition: none.

## 2. Normalize The Points

Normalize points to a GeoJSON `FeatureCollection` with Point geometries.
Include useful popup properties such as name, distance, category, notes, and a
per-feature map or search URL when available.

Skip condition: preserve valid existing GeoJSON without rewriting it.

## 3. Generate The HTML Map

Generate a static HTML map. Use the bundled Python 3 script
`scripts/build_leaflet_map.py` when a simple point map is enough:

```sh
python3 skills/static-marker-map/scripts/build_leaflet_map.py \
  input.geojson output.html \
  --title "Candidate municipalities" \
  --subtitle "241 points within 150 km" \
  --center-lat 43.5298 --center-lon 13.5185 \
  --center-name "IKEA Ancona / Camerano" \
  --radius-km 150 \
  --link "KML=ancona-150km.kml" \
  --link "GeoJSON=ancona-150km.geojson"
```

The script accepts source data and arguments and writes one HTML file. Stop and
report the missing dependency if Python 3 is unavailable; do not hand-edit a
large generated map as a fallback.

Skip condition: use an existing repo generator when it owns the output.

## 4. Link The Artifacts

Link user-facing pages to the HTML map for immediate viewing. Link KML as an
import/export artifact, not as a direct Google Maps overlay.

Skip condition: none when publishing the generated map.

## 5. Validate The Result

Validate the result before finishing:

- Parse GeoJSON and KML/XML when present.
- Confirm marker counts match the source table or generator output.
- Confirm the Markdown or site link points at the HTML map, not
  `https://www.google.com/maps?q=<kml-url>`.
- If a browser is available, open or screenshot the HTML map.

Skip condition: browser inspection is optional when no browser is available;
all structural checks remain required.

## Script Notes

`scripts/build_leaflet_map.py` accepts either GeoJSON or CSV:

- GeoJSON input must be a `FeatureCollection` of point features.
- CSV input needs latitude and longitude columns; override defaults with
  `--lat-column`, `--lon-column`, and `--name-column`.
- Output embeds the point data directly in the HTML to avoid CORS/fetch issues
  on static sites.
- The map uses Leaflet and OpenStreetMap tiles from public CDNs. If the target
  environment is offline or blocks CDNs, adapt the script or generated HTML to
  use local assets.

## Link Guidance

Avoid promising that Google Maps will render a hosted KML through a URL query
parameter. Use these link roles instead:

- **Map**: the generated `.html` marker map.
- **KML**: file for Google My Maps import or Google Earth use.
- **GeoJSON**: machine-readable point data for future regeneration.

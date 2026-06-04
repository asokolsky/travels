---
name: static-marker-map
description: Build shareable static browser maps from GeoJSON, CSV, KML-derived point data, or markdown tables. Use when Codex needs to create or repair a map artifact with many markers, replace brittle direct Google Maps KML overlay links, generate Leaflet HTML maps, produce GeoJSON/KML companion links, or validate marker counts and map links in a repo.
---

# Static Marker Map

Create lightweight map artifacts that work from a static site or a local file.
Prefer a generated Leaflet HTML map with inline GeoJSON point data, and keep
KML or GeoJSON as companion export/import files.

## Workflow

1. Inspect the source data and preserve the existing source of truth. If a repo
   already has a generator, patch that generator instead of hand-editing only
   the generated map.
2. Normalize points to a GeoJSON `FeatureCollection` with Point geometries.
   Include useful popup properties such as name, distance, category, notes, and
   a per-feature map/search URL when available.
3. Generate a static HTML map. Use
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

4. Link user-facing pages to the HTML map for immediate viewing. Link KML as an
   import/export artifact, not as a direct Google Maps overlay.
5. Validate the result before finishing:
   - Parse GeoJSON and KML/XML when present.
   - Confirm marker counts match the source table or generator output.
   - Confirm the markdown/site link points at the HTML map, not
     `https://www.google.com/maps?q=<kml-url>`.
   - If a browser is available, open or screenshot the HTML map.

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

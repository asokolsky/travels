#!/usr/bin/env python3
"""Build a static Leaflet marker map from GeoJSON or CSV point data."""

from __future__ import annotations

import argparse
import csv
import json
from html import escape
from pathlib import Path
from typing import Any


DEFAULT_TILE_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
DEFAULT_ATTRIBUTION = "&copy; OpenStreetMap contributors"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a standalone Leaflet HTML marker map."
    )
    parser.add_argument("input_path", type=Path, help="Input GeoJSON or CSV file.")
    parser.add_argument("output_path", type=Path, help="Output HTML file.")
    parser.add_argument("--title", default="Marker Map", help="Map page title.")
    parser.add_argument("--subtitle", help="Optional header subtitle.")
    parser.add_argument(
        "--lat-column",
        default="lat",
        help="CSV latitude column name. Default: lat.",
    )
    parser.add_argument(
        "--lon-column",
        default="lon",
        help="CSV longitude column name. Default: lon.",
    )
    parser.add_argument(
        "--name-column",
        default="name",
        help="CSV or GeoJSON property used as marker title. Default: name.",
    )
    parser.add_argument(
        "--marker-radius",
        type=float,
        default=5,
        help="Circle-marker radius in pixels. Default: 5.",
    )
    parser.add_argument("--center-lat", type=float, help="Optional center marker lat.")
    parser.add_argument("--center-lon", type=float, help="Optional center marker lon.")
    parser.add_argument("--center-name", help="Optional center marker name.")
    parser.add_argument("--center-note", help="Optional center marker note.")
    parser.add_argument("--radius-km", type=float, help="Optional radius circle in km.")
    parser.add_argument(
        "--link",
        action="append",
        default=[],
        metavar="LABEL=HREF",
        help="Header action link. May be supplied multiple times.",
    )
    parser.add_argument(
        "--tile-url",
        default=DEFAULT_TILE_URL,
        help="Leaflet tile URL template.",
    )
    parser.add_argument(
        "--attribution",
        default=DEFAULT_ATTRIBUTION,
        help="Tile attribution HTML.",
    )
    return parser.parse_args()


def parse_number(value: str) -> int | float | str:
    stripped = value.strip()
    if stripped == "":
        return ""
    try:
        as_int = int(stripped.replace(",", ""))
    except ValueError:
        pass
    else:
        if str(as_int) == stripped.replace(",", ""):
            return as_int
    try:
        return float(stripped)
    except ValueError:
        return stripped


def load_csv(path: Path, lat_column: str, lon_column: str) -> dict[str, Any]:
    features: list[dict[str, Any]] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"{path} has no CSV header")
        missing = [column for column in (lat_column, lon_column) if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"{path} is missing required column(s): {', '.join(missing)}")

        for line_number, row in enumerate(reader, start=2):
            try:
                lat = float(row[lat_column])
                lon = float(row[lon_column])
            except ValueError as exc:
                raise ValueError(f"{path}:{line_number} has invalid coordinates") from exc

            properties = {
                key: parse_number(value)
                for key, value in row.items()
                if key not in {lat_column, lon_column}
            }
            features.append(
                {
                    "type": "Feature",
                    "properties": properties,
                    "geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat],
                    },
                }
            )

    return {"type": "FeatureCollection", "features": features}


def load_geojson(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("type") != "FeatureCollection":
        raise ValueError(f"{path} must be a GeoJSON FeatureCollection")

    for index, feature in enumerate(payload.get("features", []), start=1):
        geometry = feature.get("geometry") or {}
        coordinates = geometry.get("coordinates") or []
        if geometry.get("type") != "Point" or len(coordinates) < 2:
            raise ValueError(f"{path} feature {index} is not a Point geometry")
        float(coordinates[0])
        float(coordinates[1])

    return payload


def load_points(path: Path, lat_column: str, lon_column: str) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return load_csv(path, lat_column, lon_column)
    if suffix in {".geojson", ".json"}:
        return load_geojson(path)
    raise ValueError(f"Unsupported input type for {path}; use .geojson, .json, or .csv")


def parse_links(values: list[str]) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for value in values:
        if "=" not in value:
            raise ValueError(f"--link must be LABEL=HREF, got {value!r}")
        label, href = value.split("=", 1)
        label = label.strip()
        href = href.strip()
        if not label or not href:
            raise ValueError(f"--link must be LABEL=HREF, got {value!r}")
        links.append({"label": label, "href": href})
    return links


def feature_count(feature_collection: dict[str, Any]) -> int:
    return len(feature_collection.get("features", []))


def html_document(
    feature_collection: dict[str, Any],
    *,
    title: str,
    subtitle: str | None,
    name_column: str,
    marker_radius: float,
    center_lat: float | None,
    center_lon: float | None,
    center_name: str | None,
    center_note: str | None,
    radius_km: float | None,
    links: list[dict[str, str]],
    tile_url: str,
    attribution: str,
) -> str:
    data = json.dumps(feature_collection, ensure_ascii=False, indent=2).replace("</", "<\\/")
    link_html = "\n".join(
        f'        <a href="{escape(link["href"], quote=True)}">{escape(link["label"])}</a>'
        for link in links
    )
    subtitle_text = subtitle or f"{feature_count(feature_collection)} mapped points"
    center_payload = json.dumps(
        {
            "lat": center_lat,
            "lon": center_lon,
            "name": center_name or "Center",
            "note": center_note or "",
            "radiusKm": radius_km,
        }
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="generator" content="skills/static-marker-map/scripts/build_leaflet_map.py">
  <title>{escape(title)}</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  <style>
    html,
    body {{
      height: 100%;
      margin: 0;
    }}

    body {{
      color: #203035;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    .shell {{
      min-height: 100%;
      display: grid;
      grid-template-rows: auto 1fr;
      background: #f7f5ef;
    }}

    header {{
      display: flex;
      gap: 16px;
      align-items: center;
      justify-content: space-between;
      padding: 14px 18px;
      background: #fffefa;
      border-bottom: 1px solid #d9d4c7;
    }}

    h1 {{
      margin: 0;
      font-size: 20px;
      line-height: 1.2;
      font-weight: 700;
    }}

    .meta {{
      margin-top: 4px;
      color: #52616b;
      font-size: 14px;
      line-height: 1.35;
    }}

    .actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: flex-end;
    }}

    .actions a {{
      border: 1px solid #0f766e;
      border-radius: 6px;
      color: #0f5e66;
      font-size: 14px;
      font-weight: 650;
      line-height: 1;
      padding: 9px 11px;
      text-decoration: none;
      white-space: nowrap;
    }}

    .actions a:focus,
    .actions a:hover {{
      background: #e3f3f1;
    }}

    #map {{
      min-height: calc(100vh - 75px);
      width: 100%;
    }}

    .leaflet-popup-content {{
      margin: 13px 15px;
    }}

    .popup-title {{
      color: #1d3138;
      font-size: 15px;
      font-weight: 700;
      margin-bottom: 7px;
    }}

    .leaflet-popup-content table {{
      border-collapse: collapse;
      font-size: 13px;
    }}

    .leaflet-popup-content th {{
      color: #52616b;
      font-weight: 650;
      padding: 2px 10px 2px 0;
      text-align: left;
      vertical-align: top;
    }}

    .leaflet-popup-content td {{
      padding: 2px 0;
      vertical-align: top;
    }}

    .center-marker span {{
      display: block;
      width: 18px;
      height: 18px;
      background: #a23e2f;
      border: 3px solid #fffefa;
      border-radius: 50%;
      box-shadow: 0 1px 6px rgb(32 47 54 / 0.35);
    }}

    @media (max-width: 700px) {{
      header {{
        align-items: flex-start;
        flex-direction: column;
      }}

      .actions {{
        justify-content: flex-start;
      }}

      #map {{
        min-height: calc(100vh - 124px);
      }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <header>
      <div>
        <h1>{escape(title)}</h1>
        <div class="meta">{escape(subtitle_text)}</div>
      </div>
      <nav class="actions" aria-label="Map data">
{link_html}
      </nav>
    </header>
    <div id="map" aria-label="Marker map"></div>
  </div>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>
    const POINTS = {data};
    const CENTER = {center_payload};
    const NAME_PROPERTY = {json.dumps(name_column)};

    const map = L.map("map", {{ preferCanvas: true }});
    L.tileLayer({json.dumps(tile_url)}, {{
      maxZoom: 18,
      attribution: {json.dumps(attribution)},
    }}).addTo(map);

    const markers = L.geoJSON(POINTS, {{
      pointToLayer: (_feature, latlng) => L.circleMarker(latlng, {{
        radius: {marker_radius},
        color: "#0f5e66",
        weight: 1.5,
        fillColor: "#1c9a93",
        fillOpacity: 0.78,
      }}),
      onEachFeature: (feature, layer) => {{
        const p = feature.properties || {{}};
        layer.bindPopup(popupHtml(p));
      }},
    }}).addTo(map);

    const bounds = markers.getBounds();
    if (Number.isFinite(CENTER.lat) && Number.isFinite(CENTER.lon)) {{
      addCenterMarker(bounds);
    }}

    if (bounds.isValid()) {{
      map.fitBounds(bounds, {{ padding: [28, 28] }});
    }} else if (Number.isFinite(CENTER.lat) && Number.isFinite(CENTER.lon)) {{
      map.setView([CENTER.lat, CENTER.lon], 10);
    }} else {{
      map.setView([0, 0], 2);
    }}

    function addCenterMarker(bounds) {{
      if (Number.isFinite(CENTER.radiusKm) && CENTER.radiusKm > 0) {{
        L.circle([CENTER.lat, CENTER.lon], {{
          radius: CENTER.radiusKm * 1000,
          color: "#a23e2f",
          weight: 2,
          opacity: 0.75,
          fillColor: "#e6b451",
          fillOpacity: 0.05,
        }}).addTo(map);
      }}

      const centerIcon = L.divIcon({{
        className: "center-marker",
        html: "<span></span>",
        iconSize: [18, 18],
        iconAnchor: [9, 9],
      }});
      L.marker([CENTER.lat, CENTER.lon], {{
        icon: centerIcon,
        title: CENTER.name,
      }})
        .bindPopup(`<div class="popup-title">${{escapeHtml(CENTER.name)}}</div><div>${{escapeHtml(CENTER.note)}}</div>`)
        .addTo(map);
      bounds.extend([CENTER.lat, CENTER.lon]);
    }}

    function popupHtml(properties) {{
      const title = properties[NAME_PROPERTY] || properties.name || properties.title || "Point";
      const rows = Object.entries(properties)
        .filter(([key, value]) => value !== null && value !== undefined && value !== "" && !isUrlField(key))
        .map(([key, value]) => `<tr><th>${{escapeHtml(labelize(key))}}</th><td>${{escapeHtml(formatValue(value))}}</td></tr>`)
        .join("");
      const url = properties.google_maps_url || properties.maps_url || properties.url;
      const link = url
        ? `<p><a href="${{escapeHtml(url)}}" target="_blank" rel="noopener">Open map link</a></p>`
        : "";
      return `<div class="popup-title">${{escapeHtml(title)}}</div><table>${{rows}}</table>${{link}}`;
    }}

    function isUrlField(key) {{
      return ["google_maps_url", "maps_url", "url"].includes(key);
    }}

    function labelize(key) {{
      return String(key)
        .replace(/_/g, " ")
        .replace(/\\b\\w/g, (letter) => letter.toUpperCase());
    }}

    function escapeHtml(value) {{
      return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    function formatValue(value) {{
      return typeof value === "number" ? value.toLocaleString("en-US") : value;
    }}
  </script>
</body>
</html>
"""


def main() -> None:
    args = parse_args()
    feature_collection = load_points(args.input_path, args.lat_column, args.lon_column)
    links = parse_links(args.link)
    html = html_document(
        feature_collection,
        title=args.title,
        subtitle=args.subtitle,
        name_column=args.name_column,
        marker_radius=args.marker_radius,
        center_lat=args.center_lat,
        center_lon=args.center_lon,
        center_name=args.center_name,
        center_note=args.center_note,
        radius_km=args.radius_km,
        links=links,
        tile_url=args.tile_url,
        attribution=args.attribution,
    )
    args.output_path.write_text(html, encoding="utf-8")
    print(f"Wrote {args.output_path} with {feature_count(feature_collection)} point(s).")


if __name__ == "__main__":
    main()

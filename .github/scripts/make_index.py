#!/usr/bin/env python3
"""Generate index.html listing every variant folder (with manifest.json) in a site dir.

Usage: make_index.py <site_dir>
"""
import html
import sys
from pathlib import Path

ESP_TOOLS = "https://unpkg.com/esp-web-tools@10.1.1/dist/web/install-button.js?module"


def render(variants: list[str]) -> str:
    rows = "\n".join(
        f'    <li><strong>{html.escape(v)}</strong> '
        f'<esp-web-install-button manifest="{html.escape(v)}/manifest.json"></esp-web-install-button></li>'
        for v in variants
    ) or "    <li>No variants built yet.</li>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>yoRadio web flasher</title>
<script type="module" src="{ESP_TOOLS}"></script>
<style>body{{font-family:system-ui,sans-serif;max-width:40rem;margin:2rem auto;padding:0 1rem}}
li{{margin:1rem 0;display:flex;gap:1rem;align-items:center;flex-wrap:wrap}}</style>
</head><body>
<h1>yoRadio web flasher</h1>
<p>Connect your ESP32 by USB and pick a variant. Requires Chrome or Edge (Web Serial) over HTTPS.</p>
<ul>
{rows}
</ul>
</body></html>
"""


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        raise SystemExit(__doc__)
    site = Path(argv[1])
    variants = sorted(p.name for p in site.iterdir() if (p / "manifest.json").is_file())
    (site / "index.html").write_text(render(variants))


if __name__ == "__main__":
    main(sys.argv)

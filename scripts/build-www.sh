#!/usr/bin/env bash
# Regenerate the gzipped web UI in yoRadio/data/www from the readable sources in yoRadio/www-src.
# theme.css is served uncompressed (users can edit it on the device), everything else is .gz.
set -euo pipefail
cd "$(dirname "$0")/.."
src=yoRadio/www-src
dst=yoRadio/data/www
for f in "$src"/*; do
  name=$(basename "$f")
  if [ "$name" = "README.md" ]; then
    continue
  elif [ "$name" = "theme.css" ]; then
    cp "$f" "$dst/$name"
  else
    gzip -9 -n -c "$f" > "$dst/$name.gz"
  fi
done
ls -l "$dst"

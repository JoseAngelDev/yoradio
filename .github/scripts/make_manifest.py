#!/usr/bin/env python3
"""Write an ESP Web Tools manifest.json for one variant.

Usage: make_manifest.py <out_dir> <variant> <chip> <spiffs_offset_hex> <version>
Expects bootloader.bin, partitions.bin, boot_app0.bin, firmware.bin, spiffs.bin in out_dir.
"""
import json
import sys
from pathlib import Path

CHIPS = {
    "esp32": ("ESP32", 0x1000),
    "esp32s3": ("ESP32-S3", 0x0),
}


def build_manifest(variant: str, chip: str, spiffs_offset: int, version: str) -> dict:
    if chip not in CHIPS:
        raise SystemExit(f"unsupported CHIP '{chip}' (use: {', '.join(CHIPS)})")
    family, boot_offset = CHIPS[chip]
    parts = [
        {"path": "bootloader.bin", "offset": boot_offset},
        {"path": "partitions.bin", "offset": 0x8000},
        {"path": "boot_app0.bin", "offset": 0xE000},
        {"path": "firmware.bin", "offset": 0x10000},
        {"path": "spiffs.bin", "offset": spiffs_offset},
    ]
    return {
        "name": f"yoRadio ({variant})",
        "version": version,
        "new_install_prompt_erase": True,
        "builds": [{"chipFamily": family, "parts": parts}],
    }


def main(argv: list[str]) -> None:
    if len(argv) != 6:
        raise SystemExit(__doc__)
    out_dir, variant, chip, spiffs_hex, version = argv[1:]
    out = Path(out_dir)
    for name in ("bootloader", "partitions", "boot_app0", "firmware", "spiffs"):
        if not (out / f"{name}.bin").is_file():
            raise SystemExit(f"missing {name}.bin in {out}")
    manifest = build_manifest(variant, chip, int(spiffs_hex, 16), version)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main(sys.argv)

#!/usr/bin/env python3
"""Validate local M3U/M3U8 pointer files without downloading media."""
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted((ROOT / "playlists").rglob("*.m3u*"))

def validate(path: Path) -> list[str]:
    errors = []
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    if not lines or lines[0].strip() != "#EXTM3U":
        errors.append("missing #EXTM3U header")
    entries = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")]
    if not entries:
        errors.append("no playlist URL entry found")
    for entry in entries:
        parsed = urlparse(entry)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            errors.append(f"invalid HTTP(S) URL: {entry}")
    return errors

def main() -> int:
    if not FILES:
        print("No .m3u/.m3u8 files found.")
        return 1
    failed = False
    for path in FILES:
        errors = validate(path)
        rel = path.relative_to(ROOT)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {rel}: {error}")
        else:
            print(f"OK   {rel}")
    print(f"\nChecked {len(FILES)} playlist file(s).")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())

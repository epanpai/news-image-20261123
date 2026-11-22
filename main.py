#!/usr/bin/env python3
"""news-image-20261123 — front page for Monday 23 November 2026.

The finished picture ships in this repository (assets/entry.png). This
program only checks it and writes it to the grader's output directory,
so it needs no network and every run writes exactly the same bytes.

Run:  MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
from __future__ import annotations

import hashlib
import os
import struct
import sys
import zlib
from pathlib import Path

REPO = Path(__file__).resolve().parent
ARTWORK = REPO / "assets" / "entry.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
MAGIC = b"\x89PNG\r\n\x1a\n"


def abort(message: str) -> "SystemExit":
    print(f"main.py: {message}", file=sys.stderr)
    return SystemExit(1)


def check_png(blob: bytes) -> tuple[int, int]:
    """Walk every PNG chunk and verify its CRC, size and dimensions."""
    if len(blob) > MAX_BYTES:
        raise abort(f"entry.png is {len(blob)} bytes, over the 1 MiB cap")
    if blob[:8] != MAGIC:
        raise abort("entry.png does not start with the PNG signature")

    pos, seen_ihdr, seen_iend = 8, False, False
    width = height = 0
    while pos + 8 <= len(blob):
        (length,) = struct.unpack(">I", blob[pos:pos + 4])
        kind = blob[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(blob):
            raise abort(f"chunk {kind!r} runs past the end of the file")
        (stored_crc,) = struct.unpack(">I", blob[end - 4:end])
        actual_crc = zlib.crc32(kind + blob[pos + 8:end - 4]) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            raise abort(f"chunk {kind!r} has a bad CRC")
        if kind == b"IHDR":
            if seen_ihdr or length != 13:
                raise abort("bad IHDR chunk")
            seen_ihdr = True
            width, height = struct.unpack(">II", blob[pos + 8:pos + 16])
        if kind == b"IEND":
            seen_iend = True
            if end != len(blob):
                raise abort("trailing bytes after IEND")
            break
        pos = end
    if not seen_ihdr:
        raise abort("entry.png has no IHDR chunk")
    if not seen_iend:
        raise abort("entry.png has no IEND chunk")
    if width == 0 or height == 0:
        raise abort("entry.png has a zero dimension")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise abort(f"entry.png is {width}x{height}, over the 1024x1024 cap")
    return width, height


def main() -> int:
    blob = ARTWORK.read_bytes()
    width, height = check_png(blob)

    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    written = target / "entry.png"
    written.write_bytes(blob)

    if written.read_bytes() != blob:
        raise abort("written file differs from the repository artwork")

    digest = hashlib.sha256(blob).hexdigest()
    print(f"entry.png {width}x{height} {len(blob)} bytes sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

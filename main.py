#!/usr/bin/env python3
"""news-image-20261120 — account 4 (lathixbt) — "MAP DESK" formula.

Square 1:1 editorial news infographic poster, 1024x1024.
The finished poster is held in the repository as entry.png (drawn by the
authoring agent during the recording); this program simply copies that
image to the output directory, byte for byte, so the result is fully
deterministic. The competition rules explicitly allow this: "the simplest
program copies an image the repository holds".

Standard library only — nothing is installed before this runs, so it must
not import anything beyond the stdlib.

All 33 stories verified as Friday 20 November 2026 events.
Output: $MAKEFUN_OUTPUT_DIR/entry.png (default /output). Never ./entry.png.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Locate the poster next to this file, not via the working directory:
    # the grader runs main.py with the repository read-only in /bot and
    # the output in /output, from an unrelated working directory.
    with open(SRC, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SRC, out)
    with open(out, "rb") as f:
        out_digest = hashlib.sha256(f.read()).hexdigest()
    if out_digest != digest:
        print("copy mismatch", file=sys.stderr)
        return 1
    print(f"wrote {out} (1024x1024, sha256 {out_digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Ship the 19 November 2026 front page.

Copies the bundled entry.png byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output/entry.png). Python 3.13 stdlib only; no network, no
randomness, deterministic: two runs produce byte-identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.png")
    dest = out_dir if out_dir.endswith(".png") else os.path.join(out_dir, "entry.png")
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    shutil.copyfile(SRC, dest)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(dest)
    if src_size != dst_size:
        print(f"size mismatch: source {src_size} bytes, wrote {dst_size} bytes",
              file=sys.stderr)
        return 1
    if src_size > 1048576:
        print(f"entry.png is {src_size} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({dst_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

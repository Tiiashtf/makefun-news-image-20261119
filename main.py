#!/usr/bin/env python3
"""Ship the 19 November 2026 front page.

Copies the bundled entry.png byte for byte to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output/entry.png). Before copying, validates that the bundled file
is a whole PNG of the required 1024x1024 size, so a corrupt or wrong-sized
image fails loudly instead of shipping silently. Python 3.13 stdlib only; no
network, no randomness, deterministic: two runs produce byte-identical output.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def check_png(path):
    """Return (width, height) if path is a whole 1024x1024 PNG, else raise."""
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) < 45 or data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1024, 1024):
        raise ValueError(f"expected 1024x1024, got {width}x{height}")
    if data[-12:-8] != b"\x00\x00\x00\x00" or data[-8:-4] != b"IEND":
        raise ValueError("PNG is truncated: no IEND trailer")
    return width, height


def main():
    try:
        check_png(SRC)
    except (OSError, ValueError) as exc:
        print(f"entry.png failed validation: {exc}", file=sys.stderr)
        return 1
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

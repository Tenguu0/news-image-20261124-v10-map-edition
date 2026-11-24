import os
import shutil
import sys


def publish() -> int:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 2
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png is missing", file=sys.stderr)
        return 2
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(src, os.path.join(out, "entry.png"))
    return 0


raise SystemExit(publish())

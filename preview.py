#!/usr/bin/env python3
"""Packs dist/ into one previewable folder (preview/) so all three sites link to each other
before the real domains are pointed: hub at the root, the others in subfolders."""
import re, shutil
from pathlib import Path

ROOT = Path(__file__).parent
DIST, OUT = ROOT / "dist", ROOT / "preview"
MAP = [("https://littleswitzerlandarkansas.com", "little-switzerland/"),
       ("https://morwoodhouse.com", "morwood-house/"),
       ("https://cabinsintheozarks.com", "")]


def fix_href(h):
    if re.match(r"^(https?:|mailto:|tel:|sms:|#)", h):
        return h
    path, _, frag = h.partition("#")
    if path == "" and frag:
        return h
    if path in ("", ".", "..") or path.endswith("/"):
        path = (path.rstrip("/") + "/" if path not in ("", ".") else "./") + "index.html"
        path = path.replace(".//", "./")
    return path + ("#" + frag if frag else "")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(DIST / "hub", OUT)
    shutil.copytree(DIST / "little-switzerland", OUT / "little-switzerland")
    shutil.copytree(DIST / "morwood-house", OUT / "morwood-house")
    for f in OUT.rglob("*.html"):
        depth = len(f.relative_to(OUT).parts) - 1
        up = "../" * depth
        t = f.read_text()
        for prod, local in MAP:
            t = t.replace(f'href="{prod}/', f'href="{up}{local}').replace(f'href="{prod}"', f'href="{up}{local}"')
        t = re.sub(r'href="([^"]*)"', lambda m: f'href="{fix_href(m.group(1)) if not m.group(1).endswith(".css") else m.group(1)}"', t)
        f.write_text(t)
    print("preview files:", sum(1 for _ in OUT.rglob("*") if _.is_file()))


if __name__ == "__main__":
    main()

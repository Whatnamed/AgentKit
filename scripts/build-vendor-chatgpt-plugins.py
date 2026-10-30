#!/usr/bin/env python3
"""Build two skills-only ChatGPT plugin ZIPs from pinned third-party originals."""
import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = {
    "scope-and-writing": ("stop-that-shit", [
        "skills/stop-that-shit/SKILL.md",
        "skills/stop-that-shit/agents/openai.yaml",
        "skills/stss/SKILL.md",
        "skills/stss/agents/openai.yaml",
        "skills/stss/references/examples.md",
    ]),
    "academic-writing": ("anti-defensive-writing", [
        "skills/anti-defensive-writing/SKILL.md",
    ]),
}

def build(bundle: str):
    vendor, items = BUNDLES[bundle]
    base = ROOT / "vendor" / vendor
    manifest = ROOT / "plugins" / bundle / "plugin.json"
    m = json.loads(manifest.read_text(encoding="utf-8"))
    output = ROOT / "dist" / "plugins" / (m["name"] + ".zip")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(manifest, "plugin.json")
        for rel in items:
            src = base / rel
            if not src.is_file() or not src.resolve().is_relative_to(base.resolve()):
                raise ValueError("Missing upstream source: " + str(src))
            z.write(src, rel)
        z.write(base / "LICENSE", "LICENSE")
    with zipfile.ZipFile(output) as z:
        if z.testzip():
            raise ValueError("Broken ZIP: " + str(output))
    print(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", nargs="?", choices=sorted(BUNDLES))
    args = parser.parse_args()
    for bundle in [args.bundle] if args.bundle else BUNDLES:
        build(bundle)

if __name__ == "__main__":
    main()

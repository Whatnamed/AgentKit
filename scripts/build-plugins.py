#!/usr/bin/env python3
"""Build portable skills-only AgentKit plugins from one canonical skills/ tree.

Run from any working directory:
    python scripts/build-plugins.py [product-ux|visual-system]
Requires only Python 3.10+ standard library. No network, credentials, or installs.
"""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = {
    "product-ux": ("agentkit-product-ux", (
        "product-discovery", "product-ia-interaction", "product-ux-review",
    )),
    "visual-system": ("agentkit-visual-system", (
        "visual-system-extract", "visual-system-create",
        "visual-system-adopt", "visual-qa",
    )),
}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REFERENCE_RE = re.compile(r"\]\((references/[^)]+|assets/[^)]+)\)")


def require_skill(skill_name: str) -> list[tuple[str, bytes]]:
    skill_dir = ROOT / "skills" / skill_name
    entry = skill_dir / "SKILL.md"
    if not entry.is_file():
        raise ValueError(f"Missing required skill entry: {entry}")
    text = entry.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"Invalid YAML frontmatter: {entry}")
    header = text.split("\n---\n", 1)[0]
    match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", header, flags=re.M)
    if not match or match.group(1) != skill_name or not NAME_RE.fullmatch(skill_name):
        raise ValueError(f"Frontmatter name must match skill folder: {entry}")
    desc = re.search(r'^description:\s*"?(.+?)"?\s*$', header, flags=re.M)
    if not desc or not 1 <= len(desc.group(1).strip('"')) <= 1024:
        raise ValueError(f"Missing/invalid skill description: {entry}")
    for target in REFERENCE_RE.findall(text):
        if not (skill_dir / target).is_file():
            raise ValueError(f"Broken skill-relative reference {target} in {entry}")
    out = []
    for item in sorted(skill_dir.rglob("*")):
        if item.is_symlink():
            raise ValueError(f"Symlinks are not accepted in plugin archive: {item}")
        if item.is_file():
            relative = item.relative_to(skill_dir).as_posix()
            out.append((f"skills/{skill_name}/{relative}", item.read_bytes()))
    return out


def build(group: str, output_dir: Path) -> Path:
    plugin_name, skill_names = BUNDLES[group]
    plugin_dir = ROOT / "plugins" / group
    manifest_bytes = (plugin_dir / "plugin.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest.get("name") != plugin_name or not manifest.get("version"):
        raise ValueError(f"Unexpected plugin manifest: {plugin_dir}")
    entries = [
        ("plugin.json", manifest_bytes),
        ("README.md", (plugin_dir / "README.md").read_bytes()),
    ]
    for name in skill_names:
        entries.extend(require_skill(name))
    if len({name for name, _ in entries}) != len(entries):
        raise ValueError(f"Duplicate plugin archive entries for {group}")
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{plugin_name}.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path, content in entries:
            zf.writestr(path, content)
    with zipfile.ZipFile(output) as zf:
        if zf.testzip() is not None:
            raise ValueError(f"ZIP CRC verification failed: {output}")
        names = set(zf.namelist())
        for required in ("plugin.json",) + tuple(f"skills/{n}/SKILL.md" for n in skill_names):
            if required not in names:
                raise ValueError(f"Missing packaged file {required}")
    print(f"{output.relative_to(ROOT)} | {len(skill_names)} skills | {len(entries)} files")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("group", nargs="?", choices=sorted(BUNDLES))
    parser.add_argument("--out-dir", type=Path, default=ROOT / "dist" / "plugins")
    args = parser.parse_args()
    selected: Iterable[str] = [args.group] if args.group else BUNDLES
    for group in selected:
        build(group, args.out_dir.resolve())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Create a lightweight project folder and starter production manifest."""
import argparse, json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("name", help="Project folder name")
p.add_argument("--output", default="output", help="Base output folder")
args = p.parse_args()

root = Path(args.output).resolve() / args.name
root.mkdir(parents=True, exist_ok=True)
for folder in ["assets", "story", "shots", "audio", "renders", "exports", "cache"]:
    (root / folder).mkdir(exist_ok=True)
manifest = {
    "project": args.name,
    "status": "planning",
    "target": {"platform": "YouTube Shorts", "aspect_ratio": "9:16", "fps": 30},
    "characters": [],
    "assets": [],
    "shots": [],
    "providers": {"image": None, "video": None, "voice": None, "music": None},
    "qa": {"preview_passed": False, "final_verified": False}
}
(root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(root)

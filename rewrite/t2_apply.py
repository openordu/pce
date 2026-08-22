#!/usr/bin/env python3
"""T2 batch apply — rewrite 10 selected B entries to CSG-SME1000 + OKR.

Reads rewrite/patch/t2.json (manifest of filename -> {text,entities,attributes,okr})
and writes each change into .entries/<filename>, preserving all other fields.
"""
import json, os, sys

ENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".entries")
PATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patch", "t2.json")

with open(PATCH, encoding="utf-8") as f:
    manifest = json.load(f)

changed = []
for fname, patch in manifest.items():
    path = os.path.join(ENT, fname)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    assert "text" in patch, f"{fname}: patch missing text"
    assert "okr" in patch and patch["okr"].get("objective"), f"{fname}: missing okr.objective"
    # only mutate the four allowed fields
    data["text"] = patch["text"]
    if "entities" in patch:
        data["entities"] = patch["entities"]
    if "attributes" in patch:
        data["attributes"] = patch["attributes"]
    data["okr"] = patch["okr"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    changed.append(fname)
    print("wrote", fname)

print("TOTAL", len(changed))
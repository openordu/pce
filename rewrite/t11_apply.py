#!/usr/bin/env python3
import json, os
ENT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".entries")
PATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patch", "t11.json")
with open(PATCH, encoding="utf-8") as f:
    manifest = json.load(f)
changed=[]
for fname, patch in manifest.items():
    path = os.path.join(ENT, fname)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    assert "text" in patch, f"{fname}: missing text"
    assert "okr" in patch and patch["okr"].get("objective"), f"{fname}: missing okr.objective"
    data["text"] = patch["text"]
    if "entities" in patch: data["entities"] = patch["entities"]
    if "attributes" in patch: data["attributes"] = patch["attributes"]
    data["okr"] = patch["okr"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    changed.append(fname); print("wrote", fname)
print("TOTAL", len(changed))

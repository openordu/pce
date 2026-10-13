#!/usr/bin/env python3
"""Apply T85 Koch batch-F manifest: 8 blends + 2 new nodes.
BLEND: write only text/entities/attributes/okr; append add_sources to
`sources` GAIN-ONLY (old list stays a prefix, never removed/reordered).
Protected byte-identical fields: name/image/cyphertext/salt/code.
NEW: create .entries/<file> with image [], cyphertext "", salt "".
Usage: python3 rewrite/t85_apply.py /tmp/t85_manifest.json"""
import json, sys, os
REPO = "/home/hermes/code/openordu/pce-clawson"
BYTE_IDENTICAL = {"name", "image", "cyphertext", "salt", "code"}
MANIFEST_FIELDS = {"text", "entities", "attributes", "okr"}
snap = json.load(open("/tmp/t85_protected_before.json", encoding="utf-8"))
manifest = json.load(open(sys.argv[1], encoding="utf-8"))
blended = 0
created = 0
for key, patch in manifest.items():
    if key.startswith("__new__"):
        fname = patch["file"]
        path = os.path.join(REPO, ".entries", fname)
        if os.path.exists(path):
            d = json.load(open(path, encoding="utf-8"))
            assert d.get("cyphertext") == "", f"{fname}: cyphertext should be ''"
            assert d.get("salt") == "", f"{fname}: salt should be ''"
            d["text"] = patch["text"]
            d["entities"] = patch["entities"]
            d["attributes"] = patch["attributes"]
            d["okr"] = patch["okr"]
            d["sources"] = patch["sources"]
        else:
            d = {
                "name": patch["name"],
                "text": patch["text"],
                "entities": patch["entities"],
                "attributes": patch["attributes"],
                "okr": patch["okr"],
                "image": [],
                "cyphertext": "",
                "salt": "",
                "sources": patch["sources"],
            }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=1, ensure_ascii=False)
            f.write("\n")
        created += 1
        continue
    fname = key
    path = os.path.join(REPO, ".entries", fname)
    assert os.path.exists(path), f"{fname}: missing (not a new-node batch)"
    d = json.load(open(path, encoding="utf-8"))
    keys_before = {k for k in d if k in BYTE_IDENTICAL}
    for k, v in patch.items():
        if k == "add_sources":
            continue
        assert k in MANIFEST_FIELDS, f"{fname}: bad field {k}"
        d[k] = v
    # sources: GAIN-ONLY append of add_sources
    old = list(snap[fname]["sources"])
    add = patch.get("add_sources", [])
    new_src = list(old)
    for s in add:
        if s not in new_src:
            new_src.append(s)
    assert len(new_src) >= len(old), f"{fname}: sources shrank"
    assert new_src[:len(old)] == old, f"{fname}: sources reordered/removed"
    d["sources"] = new_src
    # byte-identical protected fields
    keys_after = {k for k in d if k in BYTE_IDENTICAL}
    assert keys_after == keys_before, f"{fname}: protected key-set changed"
    for pk in BYTE_IDENTICAL:
        assert d.get(pk) == snap[fname].get(pk), f"{fname}: protected {pk} value CHANGED"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=1, ensure_ascii=False)
        f.write("\n")
    blended += 1
print("DONE")
print("BLENDED", blended)
print("CREATED", created)
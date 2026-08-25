#!/usr/bin/env python3
"""Apply T80 Koch batch-A manifest. Blend files: write only
text/entities/attributes/okr, assert protected set+values unchanged. New node
(Bretha_Nemed): create file with name/sources/text/entities/attributes/okr.
Usage: python3 t80_apply.py <manifest.json>"""
import json, sys, os
REPO = "/home/hermes/code/openordu/pce-clawson"
PROTECTED = {"name", "sources", "image", "cyphertext", "salt", "code"}
MANIFEST_FIELDS = {"text", "entities", "attributes", "okr", "name", "sources"}
snap = json.load(open("/tmp/t80_protected_before.json", encoding="utf-8"))
manifest = json.load(open(sys.argv[1], encoding="utf-8"))
for fname, patch in manifest.items():
    path = os.path.join(REPO, ".entries", fname)
    if os.path.exists(path):
        d = json.load(open(path, encoding="utf-8"))
        keys_before = {k for k in d if k in PROTECTED}
        for k, v in patch.items():
            assert k in MANIFEST_FIELDS, f"{fname}: bad field {k}"
            if k in PROTECTED:
                continue
            d[k] = v
        keys_after = {k for k in d if k in PROTECTED}
        assert keys_after == keys_before, f"{fname}: protected key-set changed"
        for pk, pv in snap.get(fname, {}).items():
            assert d.get(pk) == pv, f"{fname}: protected {pk} value CHANGED"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=1, ensure_ascii=False); f.write("\n")
        print("BLENDED:", fname)
    else:
        # new node: must NOT have existed before (not in protected snapshot)
        assert fname not in snap, f"{fname} unexpectedly existed at snapshot time"
        new = {}
        for k in ("name", "sources", "text", "entities", "attributes", "okr"):
            if k in patch:
                new[k] = patch[k]
        # keep canonical key order
        ordered = {}
        for k in ("name", "entities", "attributes", "sources", "text", "okr"):
            if k in new:
                ordered[k] = new[k]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(ordered, f, indent=1, ensure_ascii=False); f.write("\n")
        print("ADDED:", fname)
print("DONE")

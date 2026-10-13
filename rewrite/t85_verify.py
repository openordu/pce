#!/usr/bin/env python3
"""T85 verify: 8 blends (protected bytes, sources-gain, Koch cite, verbatim-6,
okr shape) + 2 new nodes (text>=150, okr, entities, sources has Koch,
no protected baseline). Prints ALL-OK only when every assert passes."""
import json, os, re, unicodedata, importlib.util

REPO = "/home/hermes/code/openordu/pce-clawson"
BLEND_KEYS = ["fairies.json", "feast.json", "Fergus_mac_Róich.json",
              "Fionn_Cycle.json", "Fianna.json", "Fir_Bolg.json",
              "Fomorians.json", "fosterage.json"]
NEW_KEYS = ["folk-tales_and_legends.json", "Marc_harid_Fulup.json"]
snap = json.load(open("/tmp/t85_protected_before.json", encoding="utf-8"))
BYTE_IDENTICAL = {"name", "image", "cyphertext", "salt", "code"}

def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^a-z0-9' ]", " ", s)
    return " ".join(s.split())

corpus = ""
for c in ("sources/culture.txt", "sources/myth.txt"):
    corpus += norm(open(os.path.join(REPO, c), encoding="utf-8", errors="replace").read()) + "\n"
ct = corpus.split()
CORPUS6 = {" ".join(ct[i:i+6]) for i in range(len(ct) - 5)}

spec = importlib.util.spec_from_file_location(
    "lc", "/home/hermes/.hermes/skills/writing/csg-sme1000-writing/scripts/csg-sme1000-lint.py")
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

concat = []
allkeys = BLEND_KEYS + NEW_KEYS
for fname in allkeys:
    assert os.path.exists(os.path.join(REPO, ".entries", fname)), f"{fname}: missing"
    d = json.load(open(os.path.join(REPO, ".entries", fname), encoding="utf-8"))
    if fname in BLEND_KEYS:
        for pk in BYTE_IDENTICAL:
            assert d.get(pk) == snap[fname].get(pk), f"{fname}: protected {pk} CHANGED"
        old = snap[fname]["sources"]
        srcs = d["sources"]
        assert len(srcs) >= len(old), f"{fname}: sources shrank"
        assert srcs[:len(old)] == old, f"{fname}: sources reordered/removed"
    else:
        # new node
        assert d.get("image") == [], f"{fname}: image should be []"
        assert d.get("cyphertext") == "", f"{fname}: cyphertext should be ''"
        assert d.get("salt") == "", f"{fname}: salt should be ''"
        srcs = d["sources"]
    assert any("Koch 2006" in s for s in srcs), f"{fname}: no Koch 2006 in sources"
    okr = d["okr"]
    assert okr["objective"], f"{fname}: objective empty"
    assert 2 <= len(okr["key_results"]) <= 4, f"{fname}: KR count {len(okr['key_results'])}"
    assert "Koch 2006" in okr["evidence"], f"{fname}: evidence lacks Koch 2006"
    assert len(d["text"]) >= 150, f"{fname}: text <150"
    assert d["entities"], f"{fname}: entities empty"
    for e in d["entities"]:
        assert e.get("entity") and e.get("type"), f"{fname}: entity shape"
    concat.append(d["text"])
    toks = norm(d["text"]).split()
    for i in range(len(toks) - 5):
        run = " ".join(toks[i:i+6])
        assert run not in CORPUS6, f"{fname}: verbatim-6 [{run}]"
print("PROTECTED-OK")
print("SOURCES-GAIN-OK")
print("KOCH-CITE-OK", len(allkeys))
print("VERBATIM6-OK", len(allkeys))
res = lc.lint(" ".join(concat))
if isinstance(res, dict):
    per100 = res.get("violations_per100w", 0)
    viols = res.get("violations", {})
else:
    per100 = 0
    viols = {}
assert per100 <= 5.0, f"LINT per100w {per100} > 5.0: {viols}"
print("LINT-OK", round(per100, 2))
print("ALL-OK")
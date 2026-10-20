#!/usr/bin/env python3
"""T86 verify: 10 blends + 2 new nodes."""
import json, os, re, unicodedata, importlib.util
REPO = "/home/hermes/code/openordu/pce-clawson"
BLEND = ["geis.json", "Goibniu.json", "Gebrinius.json", "Grail.json", "Gaul.json",
         "Galatia.json", "Gundestrup_Cauldron.json", "Glastonbury.json",
         "Grannos.json", "Glewlwyd_Gafaelwar.json"]
NEW = ["Gofannon_fab_Don.json", "Gwenhwyfar.json"]
snap = json.load(open("/tmp/t86_protected_before.json", encoding="utf-8"))
BYTE = {"name", "image", "cyphertext", "salt", "code"}

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
C6 = {" ".join(ct[i:i+6]) for i in range(len(ct) - 5)}

spec = importlib.util.spec_from_file_location(
    "lc", "/home/hermes/.hermes/skills/writing/csg-sme1000-writing/scripts/csg-sme1000-lint.py")
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

concat = []
for fname in BLEND + NEW:
    path = os.path.join(REPO, ".entries", fname)
    assert os.path.exists(path), f"{fname}: missing"
    d = json.load(open(path, encoding="utf-8"))
    if fname in BLEND:
        for pk in BYTE:
            assert d.get(pk) == snap[fname].get(pk), f"{fname}: protected {pk} changed"
        old = snap[fname]["sources"]
        assert d["sources"][:len(old)] == old, f"{fname}: sources reordered"
        assert len(d["sources"]) > len(old), f"{fname}: no source gained"
    else:
        assert d.get("image") == [], f"{fname}: image not []"
        assert d.get("cyphertext") == "", f"{fname}: cyphertext not ''"
        assert d.get("salt") == "", f"{fname}: salt not ''"
        assert d.get("name"), f"{fname}: name missing"
    assert any("Koch 2006" in s for s in d["sources"]), f"{fname}: no Koch cite"
    okr = d["okr"]
    assert okr["objective"] and 2 <= len(okr["key_results"]) <= 4
    assert "Koch 2006" in okr["evidence"]
    assert len(d["text"]) >= 150
    assert d["entities"] and all(e.get("entity") and e.get("type") for e in d["entities"])
    toks = norm(d["text"]).split()
    for i in range(len(toks) - 5):
        run = " ".join(toks[i:i+6])
        assert run not in C6, f"{fname}: verbatim-6 [{run}]"
    concat.append(d["text"])
print("PROTECTED/SOURCES/KOCH/VERBATIM6 OK:", len(BLEND), "blends +", len(NEW), "new")
res = lc.lint(" ".join(concat))
per100 = res.get("violations_per100w", 0) if isinstance(res, dict) else 0
assert per100 <= 5.0, f"LINT {per100}: {res.get('violations')}"
print("LINT-OK", round(per100, 2))

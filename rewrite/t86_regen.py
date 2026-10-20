#!/usr/bin/env python3
import json, os, sys
REPO = "/home/hermes/code/openordu/pce-clawson"
sys.path.insert(0, REPO)
from markdown import write_md_file, sanitize_filename
from unidecode import unidecode

CHANGED = ["geis", "Goibniu", "Gebrinius", "Grail", "Gaul", "Galatia",
           "Gundestrup_Cauldron", "Glastonbury"]
NEW = [("Gofannon_fab_Don", "Gofannon fab Dôn"), ("Grannus", "Grannus"),
       ("Glewlwyd_Gafaelfawr", "Glewlwyd Gafaelfawr"), ("Gwenhwyfar", "Gwenhwyfar")]

idx_path = os.path.join(REPO, "index.sjson")
idx = json.load(open(idx_path, encoding="utf-8"))
for _, n in NEW:
    if n not in idx:
        idx.append(n)
json.dump(idx, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False)
idxmap = {name: i for i, name in enumerate(idx)}

items = [(f, None) for f in CHANGED] + NEW
for fname, display in items:
    d = json.load(open(os.path.join(REPO, ".entries", fname + ".json"), encoding="utf-8"))
    if not d.get("image"):
        d["image"] = [None]
    name = d.get("name", display or fname)
    san = sanitize_filename(name)
    d["order"] = idxmap.get(name)
    sub = unidecode(san[0]).upper()
    write_md_file(d, os.path.join(REPO, sub, san + ".md"))
    print("MD:", sub + "/" + san + ".md", "order", d["order"])

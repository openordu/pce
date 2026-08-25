#!/usr/bin/env python3
"""Build T80 Koch batch-A manifest (blend Badb/boar/aisling + add Bretha Nemed).
Koch 2006 enrichment. Own-words CSG-SME1000 prose. Assertion-gated."""
import json, re

def lint(text):
    assert '\n' not in text
    assert ';' not in text, "semicolon"
    toks = text.lower().split()
    for bad in (' very ',' really ',' truly ',' extremely ',' incredibly '):
        assert bad not in (' '+text.lower()+' '), "intensifier "+bad.strip()
    for s in re.split(r'(?<=[.!?]) ', text):
        assert len(s.split()) <= 30, "long sentence: "+s[:60]
    assert len(text) >= 150, "text too short"

M = {}

# -------- Badb (BLEND) --------
badb_text = ("Badb, also written Bodb, means the scald crow. In early Irish "
"tradition she was a supernatural woman linked to battle and slaughter. "
"The name works as a proper name and as a general term for a battle creature. "
"She sometimes merges with the Morrigan, Nemain, Be Neit, or Macha, and at "
"other times stands apart from them. The stock phrase badb catha means the "
"Badb of battle. Translators of Latin tales recast the Furies and Bellona as "
"fern battle goddesses named Badb. Her appearance was an evil omen. The male "
"figure Bodb Derg, king of the sidhe of Munster, shared her name.")
lint(badb_text)
M["Badb.json"] = {
  "text": badb_text,
  "entities": [
    {"entity":"Badb","type":"Deity"},
    {"entity":"Bodb Derg","type":"Person"},
    {"entity":"Morrígan","type":"Deity"},
    {"entity":"Nemain","type":"Deity"},
    {"entity":"Macha","type":"Deity"},
    {"entity":"badb catha","type":"Concept"}
  ],
  "attributes": [
    {"entity":"Badb","attribute":"war goddess whose name means the scald crow"},
    {"entity":"Badb","attribute":"both a proper name and a general term for a battle creature"},
    {"entity":"Badb","attribute":"linked to the Morrigan, Nemain, Be Neit, and Macha"},
    {"entity":"badb catha","attribute":"the stock phrase meaning the Badb of battle"}
  ],
  "okr": {
    "objective": "Record Badb, the Irish scald-crow war goddess, from Koch 2006.",
    "key_results": [
      "Badb means the scald crow and links to battle and slaughter.",
      "The name serves as a proper name and a generic term.",
      "She merges with or stands apart from the Morrigan, Nemain, and Macha.",
      "Bodb Derg, a male king of the sidhe, shared her name."
    ],
    "evidence": "Koch 2006, s.v. 'Bodb'."
  }
}

# -------- boar (BLEND) --------
boar_text = ("The wild boar held deep symbolic weight for the ancient Celts. "
"Art and coinage from the Continent and the islands show it. Writers linked "
"the Gaulish god Moccus to the Roman Mercury, and he may have stood for a pig "
"or a boar. In the Welsh tale Culhwch and Olwen, Arthur's men first hunted "
"Ysgithrwyn, a chief boar called the white tusk, before the great chase of "
"Twrch Trwyth and his offspring. The Middle Welsh name hob set the tame pig's "
"origin in the Otherworld. In the Fourth Branch of the Mabinogi, a sow from "
"the Otherworld guided Gwydion to the slain Lleu.")
lint(boar_text)
M["boar.json"] = {
  "text": boar_text,
  "entities": [
    {"entity":"boar","type":"Animal"},
    {"entity":"Moccus","type":"Deity"},
    {"entity":"Culhwch and Olwen","type":"Title"},
    {"entity":"Ysgithrwyn","type":"Creature"},
    {"entity":"Twrch Trwyth","type":"Creature"},
    {"entity":"Gwydion","type":"Person"},
    {"entity":"Lleu","type":"Person"}
  ],
  "attributes": [
    {"entity":"boar","attribute":"held deep symbolic weight for the Celts"},
    {"entity":"Moccus","attribute":"a Gaulish god of the pig or the boar linked to Mercury"},
    {"entity":"Ysgithrwyn","attribute":"a chief boar called the white tusk in Culhwch and Olwen"},
    {"entity":"Twrch Trwyth","attribute":"the great boar hunted in Culhwch and Olwen"}
  ],
  "okr": {
    "objective": "Record the boar's symbolic role and its place in Welsh legend from Koch 2006.",
    "key_results": [
      "The boar appears in Celtic art and on coinage.",
      "The Gaulish god Moccus may represent a pig or a boar.",
      "Arthur's men hunted Ysgithrwyn before the chase of Twrch Trwyth.",
      "The Middle Welsh name hob set the tame pig's origin in the Otherworld."
    ],
    "evidence": "Koch 2006, s.v. 'boar'."
  }
}

# -------- aisling (BLEND) --------
aisling_text = ("An aisling is a vision poem in the Irish language, often "
"allegorical and usually written in the eighteenth century. In it a woman "
"from the Otherworld visits the poet in a dream. Gerard Murphy set out three "
"principal forms. The love aisling bewitches the poet with the woman's beauty. "
"The prophecy aisling lets the dreamer predict the future. In the allegorical "
"aisling the woman often stands for Ireland and comforts the distressed poet. "
"Murphy thought the third form, common in the eighteenth century, might fuse "
"the first two. The early Irish Aislinge Oengusa, the vision of Aonghus, and "
"the later Aislinge Meic Con Glinne are famous examples.")
lint(aisling_text)
M["aisling.json"] = {
  "text": aisling_text,
  "entities": [
    {"entity":"aisling","type":"Concept"},
    {"entity":"Gerard Murphy","type":"Person"},
    {"entity":"Otherworld","type":"Concept"},
    {"entity":"Ireland","type":"Place"},
    {"entity":"Aislinge Oengusa","type":"Title"}
  ],
  "attributes": [
    {"entity":"aisling","attribute":"a vision poem in the Irish language"},
    {"entity":"aisling","attribute":"often composed in the eighteenth century"},
    {"entity":"aisling","attribute":"recounts a visit from a woman of the Otherworld"},
    {"entity":"Gerard Murphy","attribute":"set out three principal forms of the aisling"}
  ],
  "okr": {
    "objective": "Record the aisling, an Irish vision poem, from Koch 2006.",
    "key_results": [
      "The aisling is an allegorical Irish-language poem of the eighteenth century.",
      "A woman from the Otherworld visits the poet in a dream.",
      "Gerard Murphy described three principal forms.",
      "The allegorical aisling often lets the woman stand for Ireland."
    ],
    "evidence": "Koch 2006, s.v. 'Aisling'."
  }
}

# -------- Bretha Nemed (NEW NODE) --------
bn_text = ("Bretha Nemed, the judgements of privileged persons, is an "
"eighth-century collection of Irish law texts from Munster. Cormac's Glossary "
"quotes two named legal sources, the Senchas Mar and the Bretha Nemed. The "
"citations raise the question whether Bretha Nemed was a law book as large as "
"the Senchas Mar. One surviving text in the Cotton manuscript carries the "
"title Corus Breatha Neimead. Medieval glosses call it Bretha Nemed Toisech, "
"the first Bretha Nemed. It stands among the earliest native Irish legal "
"collections.")
lint(bn_text)
M["Bretha_Nemed.json"] = {
  "name": "Bretha Nemed",
  "sources": ["Koch 2006, s.v. 'Bretha Nemed'."],
  "text": bn_text,
  "entities": [
    {"entity":"Bretha Nemed","type":"Title"},
    {"entity":"Senchas Mar","type":"Title"},
    {"entity":"Cormac's Glossary","type":"Title"},
    {"entity":"Munster","type":"Place"}
  ],
  "attributes": [
    {"entity":"Bretha Nemed","attribute":"an eighth-century collection of Irish law texts"},
    {"entity":"Bretha Nemed","attribute":"the judgements of privileged persons"},
    {"entity":"Bretha Nemed","attribute":"quotations from it appear in Cormac's Glossary"},
    {"entity":"Bretha Nemed","attribute":"one version is titled Corus Breatha Neimead"}
  ],
  "okr": {
    "objective": "Add Bretha Nemed, an early Irish law collection, from Koch 2006.",
    "key_results": [
      "Bretha Nemed is an eighth-century law collection from Munster.",
      "Cormac's Glossary quotes it beside the Senchas Mar.",
      "One version is titled Corus Breatha Neimead.",
      "Medieval glosses call it Bretha Nemed Toisech."
    ],
    "evidence": "Koch 2006, s.v. 'Bretha Nemed'."
  }
}

# ---- assertions ----
ALLOWED = {"Person","Place","Deity","Being","Creature","Event","Artifact",
           "Concept","Culture","Group","Animal","Object","Role","Title"}
for fn, p in M.items():
    lint(p["text"])
    for e in p["entities"]:
        assert e["type"] in ALLOWED, fn+" bad type "+e["type"]
    assert 2 <= len(p["okr"]["key_results"]) <= 4, fn+" key_results count"
    assert p["okr"]["evidence"]

json.dump(M, open("/home/hermes/code/openordu/pce-clawson/rewrite/patch/t80_koch_a.json","w"),
          indent=1, ensure_ascii=False)
print("BUILT OK. Entries:")
for fn,p in M.items():
    print(f"  {fn}: text={len(p['text'])}chars, ents={len(p['entities'])}, KRs={len(p['okr']['key_results'])}")

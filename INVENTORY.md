# INVENTORY — GAF-243 koch-encyclopedia-ingest (M5.1 Change Inventory)

Repo: openordu/pce (https://github.com/openordu/pce.git), branch main.
Change set shipped: origin/main..HEAD (16 commits, T11..T34). Base = 90b64e4
(merge PR #3). No sibling-loop commits share this slice, so every commit is
GAF-243 work. No `.github/workflows` exist on this repo — content is ingested
into the ordu-eleventy site build at build time; there is no per-PR CI gate.

## M2 — Blends (existing nodes enriched with Koch 2006, nested OKR)

| Commit | Milestone | Files | What / Why |
|---|---|---|---|
| f570f49 | M2/M1 | 73 | reconcile Koch ingest onto nested-okr main (base alignment) |
| 3e76b53 | M2 blend-4 | 18 | enrich Galatia, Gaul, Glastonbury, kingship, Matronae, Modron, Nemetona, Otherworld, Partholón |
| 0106182 | M2 blend-5 | 18 | enrich Cúchulainn, Dún Ailinne, Fairies, feast, Fergus mac Róich, fosterage, Hercules, Litavis, Manching |
| 522ca3b | M2 blend-6 | 20 | enrich Culhwch_ac_Olwen, Loucetius, Prophecy, Salt, Samhain, Satire, Stonehenge, Superstitions, Teutates |
| 8d3a62b | M2 blend-7 | 30 | enrich 14 nodes (Champion's portion → Turoe Stone), incl. Lebor Gabala Erenn, Mythological Cycle, Gundestrup Cauldron |

## M3 — New Nodes (new .entries JSON + .md + index.sjson + letter links)

| Commit | Milestone | Files | What / Why |
|---|---|---|---|
| 15341fc | M3 batch-1 | 23 | Brân fab Llŷr, Fiannaíocht, Caoineadh, Cailleach Bhéirre, Legendary animals, bruiden, aided Énfir Aífe, De Gabáil in t-Sída |
| 4367f63 | M3 batch-2 | 23 | Pwyll Pendefig Dyfed, Pryderi fab Pwyll, Math fab Mathonwy, Arianrhod ferch Dôn, Lleu, Tuath Dé, Peredur fab Efrawg, Caladbolg/Caledfwlch/Excalibur |
| 848a9da | M3 batch-3 | 23 | Historia Brittonum, Historia Regum Britanniae, Arthurian Literature, Arthurian Sites, Gododdin, Ystorya Titus Aspassianus, Badonicus Mons, Vision Literature |
| 1d331b2 | M3 batch-4 | 24 | Ballads and narrative songs, Carmina Gadelica, Five Poets, Folk-Tales and Legends, Legendary History, Manx Folklore, Neo-Druidism, Tale Lists medieval Irish |
| 8600624 | M3 batch-5 | 24 | Biniou and Bombard, Clanranald the books of, Jacobite Poetry, Macgregor Poetry, Nature Poetry, Swords, Welsh Poetry, Scottish Gaelic Poetry |
| 3f60d1f | M3 batch-6 | 23 | Immrama, Pisky, Serglige Con Culainn, Togail Troí, Pa Gur yv y Porthaur?, Llyn y Fan Fach, Tair Rhamant, Barzaz-Breiz |
| 008e069 | M3 batch-7 | 23 | Urien of Rheged, crosán, Cathach, Cín Dromna Snechta, Head cult, Watery depositions, Imtheachta Aeniasa, Dialog etre Arzur ha Guynglaff |
| c8eba21 | M3 batch-8 | 25 | Ordinalia, Beunans Ke, Conan Meriadoc, spring deities, wild man in Celtic legend, Awen, Macsen Wledig, DRAIG Goch |
| 4c2cb1e | M3 batch-9 | 7 | Ulster Cycle, Cyfarwyd (6 of 8 prepared nodes re-audited as concept-dups and discarded at merge) |
| f674a80 | M3 batch-10 | 4 | bricta (final genuinely-missing in-scope NEW node) |

## M4 — OKR / Coverage Audit

| Commit | Milestone | Files | What / Why |
|---|---|---|---|
| 25fbe06 | M4-OKR | 3 | normalize okr.evidence list->str on 3 T22 entries (cin_dromna_snechta, head_cult, watery_depositions); 140/140 OKR + JSON valid |

## Tally
- 16 commits, delta origin/main..HEAD.
- M2 blends: 14 + 9 + 9 + 14 = 46 nodes enriched.
- M3 new nodes: 8x8-2(discarded)+2+1 = 65 nodes added (incl. bricta, Ulster Cycle, Cyfarwyd).
- M4: 1 audit commit normalizing 3 records.
- Count verified (M4 audit T25/T34): 806 manifest rows → 141 blend / 33 dup / 631 out_of_scope / 1 new; OKR 140/140 on touched set, 0 JSON invalid.
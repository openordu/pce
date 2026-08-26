# GAF-259 Change Inventory — koch-pce-ingest-chunk-2 (all 100 Koch entries, no out-of-scope)

Repo: `openordu/pce` · branch `clawford/g259-pce-ingest-chunk2` → PR to `main`
Source: Koch, John T. (ed.), *Celtic Culture: A Historical Encyclopedia*, 2006 (`koch.txt`, 108,594 lines).

## Scope

Every one of the 100 GAF-259-listed Koch entries (the C–H slice) got a verifiable PCE result: **12 blends** (nodes already present, expanded with Koch material) + **88 new nodes** — zero out_of_scope, zero dup, zero cancelled. Continues chunk-1 (GAF-258, PR #8) under the same broad-scope mandate.

## Accounting summary (verified at ship — fresh re-measure, not cached)

- Koch file present at 108,594 lines.
- manifest/chunk259.json = 100 rows (blend 12 + new 88 = 100), zero unaccounted.
- JSON load: 99/99 unique nodes OK · OKR complete: 99/99 · VERBATIM-6 clean vs FULL koch.txt: 99/99.
- `.md` present + letter index links: 99/99 · index.sjson updated.
- Protected fields (name/image/cyphertext/salt): byte-identical on all blends; new nodes carry the empty defaults.
- Source crosscheck: 100 issue-entry names vs 100 manifest names, match, dup 0, missing 0.

## Commit log (19 commits, oldest → newest, all on this branch)

| # | Hash | Files | Nodes | Milestone | What / Why (commit subject verbatim) |
|---|------|-------|-------|-----------|--------|
| 1 | `87ada6c` | 6 | 5 | M2 | GAF-259 T3: blend batch A — Cúchulainn, Domnall, Easter, Drystan, Iona, Dialog etre Arzur with Koch 2006 material |
| 2 | `d3664c6` | 5 | 5 | M2 | GAF-259 T4: blend batch B — Eisteddfod, Emain_Macha, Fianna, Gododdin, Hallstatt(×2 rows→1 node) with Koch 2006 material |
| 3 | `d651c32` | 11 | 9 | M3 | GAF-259 T5: new-node batch A — Cúirt, DEINIOL, Dinas Basing Abbey, Dafydd ap Gwilym, Danebury, Darogan yr Olew Bendigaid, De Bhaldraithe Tomás, De Valera Eamon, De raris fabulis, gold neckring (Erstfeld), woollen garment (Moy) with Koch 2006 material |
| 4 | `7605332` | 6 | 4 | M3 | GAF-259 T6 waveA: new-node batch B — Dewi Sant, Domhnall Ó Duibhdábhoireann, Druidale keeill, Dumnonia, Duval Añjela, Dyfnwal ap Tewdor with Koch 2006 material |
| 5 | `e4088ce` | 3 | 1 | M3 | GAF-259 T6 waveB: new-node batch B — Diviciacos of the Suessiones, Dál Riata, Déchelette Joseph (verbatim-6 cleaned controller-side) |
| 6 | `23f556c` | 2 | 0 | M3 | GAF-259 T6 waveC: new-node batch B — Départements/towns of Brittany, Dúnchad mac Crináin (verbatim-6 cleaned, canonical filename fixed) |
| 7 | `580dad4` | 6 | 5 | M3 | GAF-259 T7 waveA: new-node batch C — Dürrnberg bei Hallein, Eadwine, Early south-east, Ecgfrith, Elidir Sais, Ellan Vannin (verbatim-6 cleaned, canonical filename) |
| 8 | `1a61d2f` | 3 | 3 | M3 | GAF-259 T7 waveB: new-node batch C — Englyn, Emvod Etrekeltiek an Oriant, Eisteddfodau'r Gwyneddigion (verbatim-6 cleaned) |
| 9 | `f2c6998` | 2 | 2 | M3 | GAF-259 T7 waveC: new-node batch C — Gwynfor Evans, St Elfoddw (verbatim-6 cleaned) |
| 10 | `fc2de30` | 6 | 6 | M3 | GAF-259 T8 waveA: new-node batch D — Entremont, Euffigneix, Evans J. Gwenogvryn, Feiseanna and the Oireachtas, Fernaig Manuscript, Fiddle (verbatim-6 cleaned) |
| 11 | `d2d327a` | 5 | 4 | M3 | GAF-259 T8 waveB: new-node batch D — Fleuriot Léon, Fomoiri, Foodways, Fulup Marc'harid, GLaschu (verbatim-6 + Dob year corrected to source) |
| 12 | `e5eee5c` | 6 | 6 | M3 | GAF-259 T9 waveA: new-node batch E — GWYNEDD, GWrtheyrn, GaULISH, Gaelic, Gaelic Society of Glasgow, Gaeltacht (verbatim-6 cleaned) |
| 13 | `1abe3f8` | 5 | 5 | M3 | GAF-259 T9 waveB: new-node batch E — Gaeltacht autobiographies, Gaillimh, Galatian language, Galicia, Gallo-Brittonic (verbatim-6 cleaned) |
| 14 | `3cb3a09` | 6 | 6 | M3 | GAF-259 T10 waveA: new-node batch F — Gaul in the later pre-Roman and Roman periods, Gaulish inscribed text in ancient Roman cursive, Genealogies [1] Irish, Genealogies [2] Welsh, Germanus St, Gildas (verbatim-6 cleaned) |
| 15 | `889bc56` | 5 | 5 | M3 | GAF-259 T10 waveB: new-node batch F — Giraldus Cambrensis, Glauberg, Glossaries, Gogynfeirdd, Golasecca Culture (verbatim-6 cleaned) |
| 16 | `121ce8a` | 11 | 9 | M3 | GAF-259 T11: new-node batch G — Gold torc armlet and, Gorhoffedd, Gorsedd Beirdd Ynys Prydain, Gorseth Kernow, Gorseth Kernow 1985, Govan, Gramadegau'r Penceirddiaid, Greek and Roman Accounts, Griffiths Ann, Grächwil, Guest Lady Charlotte (verbatim-6 cleaned) |
| 17 | `953e9a3` | 11 | 9 | M3 | GAF-259 T12: new-node batch H — Guto'r Glyn, Gwallawg ap Lleënnawg, Gwenllïan, Gwerthefyr, Hadrian's Wall and Roman, Hagiography [1]-[5] (Irish/Scotland/Welsh/Breton/Cornish), Hall Lady Augusta (verbatim-6 cleaned) |
| 18 | `b9fd57d` | 107 | 0 | M4 | GAF-259 T13: regenerate letter-dir .md for all 99 touched Koch entries + index.sjson + letter index.md links. |
| 19 | `d014d78` | 1 | 0 | M4 | GAF-259 T14: fix Dürrnberg bei Hallein node name typo ('Dürnrbber bei Halllein' -> 'Dürrnberg bei Hallein') |

## Verification (fresh re-measure at ship)
- T14 full-slice audit (`src/verify_t14.py`) run fresh at merge time: JSON ok 99/99, verbatim-6 0 runs vs FULL koch.txt, OKR complete 99/99.
- T15 coverage + source crosscheck run fresh: 100/100 accounted, 0 unaccounted, source-match 100/100.
- Working tree clean on branch; 19 commits ahead of `main`, 0 behind.

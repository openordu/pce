# INVENTORY — GAF-261 koch-pce-ingest-chunk-4 (M5.1 change inventory)

**Loop**: koch-pce-ingest-chunk-4-ingest-all-100-koch-entries-no-out-of-scope
**GAF**: GAF-261 (Plane e78351cd-6827-441d-acb0-7e37458ca231)
**Repo**: openordu/pce (local `~/code/pce`, branch `main`)
**Source**: Koch, John T. (ed.), *Celtic Culture: A Historical Encyclopedia*, ABC-CLIO 2006
(`koch.txt`, 108,594 lines / 12,013,946 bytes)
**Slice**: M–R (Mac an t-Saoir → Rawlinson B 502), 100 rows → 93 unique nodes.

## Deliverable shape
- manifest/chunk261.json: 100 rows — 9 blend / 81 new + 10 fold, 93 unique nodes.
- 9 blends: Melor, Midsummer, Mona, Nudd, Oengus (Mac ind Oc), Oppida, pa_gur,
  Patrick, Pict — expanded with Koch material, protected fields (cyphertext/salt/
  name) byte-identical, every sentence <=20 words, no verbatim run >=6 words.
- 84 new/fold nodes: `.entries/<Name>.json` with CSG-SME1000 text (>=150 chars),
  typed entities, nested OKR (objective/key_results/evidence), Koch 2006 cited,
  verbatim-6 clean. 10 fold rows map onto Manx_Language / Manx_Literature /
  Medical_Manuscripts / mass-media-by-region / nationalism-by-region shared nodes.

## Commit ledger (11 content commits on `main`, all pushed, HEAD == origin/main)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `4a36360` | T3 / M2 blend | 8 `.entries/*.json` (blend batch) | Expanded 9 blend targets (Melor, Midsummer, Mona, Nudd, Oengus, Oppida, pa_gur, Patrick, Pict) — text/attributes/entities/OKR + Koch citation | Blend matched existing PCE nodes with Koch material |
| `5ddf3f7` | T4 / M3 | 10 `.entries/*.json` (Mac an t-Saoir…Mael Coluim) | New-node batch A — CSG-SME1000 text, typed entities, OKR, Koch-cited | In-scope Koch people/places not yet in PCE |
| `de7365c` | T5 / M3 | 10 `.entries/*.json` (Mairi MacInnes…Mass media BY) | New-node batch B (incl. mass-media-by-region splits, Manx surnames, Maredudd ab Owain, Marwnad Cunedda) | No out-of-scope — captions/fragments become real nodes |
| `591870f` | T6 / M3 | 10 `.entries/*.json` (Massalia…Monasteries) | New-node batch C (Meddygon Myddfai, Meifod, Menez-Dol, Mererid Hopwood, Merfyn Frych, metrics, Meyer, monasteries) | … |
| `46d1837` | T7 / M3 | 10 `.entries/*.json` (Monasticism…Mairi nighean) | New-node batch D | … |
| `8b54aba` | T8 / M3 | 10 `.entries/*.json` (Msecke…Northern Ireland) | New-node batch E (nationalism-by-region, Nechton, Niederzier, Noricum, Ireland early med) | … |
| `6b65ee2` | T9 / M3 | 10 `.entries/*.json` (Novo Mesto…Owen Huw Roberts) | New-node batch F | … |
| `2949e5a` | T10 / M3 | 10 `.entries/*.json` (Gerallt Owen…Petrie) | New-node batch G (Pan-Celticism, Pannonia, Paoul, Parnell, Parry, trackway, Patagonia, Pedersen, Petrie) | … |
| `d061504` | T11 / M3 | 14 `.entries/*.json` (Pokorny…Rawlinson B 502 + Manx_Language/Literature/Medical + Printing/Proto-Celtic/weapons) | close M3 — final new/fold nodes; M3 84/84 | … |
| `b5f7542` | T12 / M4 | 99 files: letter-dir `.md` + letter `index.md` + `index.sjson` | Regenerated `.md` for every touched letter dir | Ship-published encyclopedia text must match entry JSON |
| `8f0780a` | T14 / M4 | 45 `.entries/*.json` (remediation) | M4 audit + CSG-SME1000 remediation pass on all 93 touched nodes — repaired ~45 fragments, all sentences <=20 words, no hedge/contraction/semicolon, no verbatim run | audit surfaced real SME violations from automated splitter |
| `T16 commit` | M5 ship | `INVENTORY.md` | This change inventory | M5.1 closeout record |

## M5.2 Test reconciliation
Openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not a
code repo. There is no test suite to add/remove. The verification gates ARE the
reconciliation record — run in prior ticks and re-run at this close:
- T3,6,7 gates: blend protected byte-identical; JSON valid; OKR complete.
- T14 gate (`audit14.py`): 93/93 nodes checked, FAILED 0 (json/okr/noun/koch_src/
  verbatim6/protected + keys + CSG-SME1000 probe).
- T15 gate (`t15_coverage.py`): 100/100 rows resolve to a present file; 93 unique
  nodes; zero unaccounted.
No tests removed to make a gate green; no dead tests retained.

## Verification evidence (re-measured at M5 close)
- `wc -l koch.txt` = 108,594 (source uncorrupted end-to-end).
- `t15_coverage.py` = PASS 100/100, zero unaccounted.
- `audit14.py` = 93/93 FAILED 0 on origin/main.
- PR to `main` merged, `git pull --ff-only` confirmed origin/main == local, INVENTORY
  commit present on origin/main, working tree clean.

**M5 INVENTORY CLOSED.** All 7 exit conditions MET → GAF-261 COMPLETE.
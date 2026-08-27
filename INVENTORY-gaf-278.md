# INVENTORY — GAF-278 mckillop-pce-ingest-chunk-1: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-1-mckillop-300-entries-blend-new-gaf-278
**GAF**: GAF-278 (Plane 54826253-a961-4054-8e39-5c96fa8b0a05)
**Repo**: openordu/pce (local `~/code/pce`, branch `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown)
**Slice**: Abac → Beare (A–Ba), 300 rows → 68 blend + 232 new = 300, zero out_of_scope / dup / cancelled.

## Deliverable shape
- manifest/chunk278.json: 300 rows — 68 blend / 232 new. Every row DONE.
- 68 blends: `.entries/<target>.json` expanded with MacKillop material — text /
  entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'` appended to
  sources, protected fields (`name`, `image`, `cyphertext`, `salt`) byte-identical,
  no verbatim run >=6 words vs FULL mckillop.txt.
- 232 new nodes: `.entries/<Name>.json` with CSG-SME1000 text (>=150 chars), typed
  entities, OKR (objective/key_results/evidence), MacKillop 2008 cited, protected
  defaults, verbatim-6 clean. NOTE: 10 rows in the manifest class as blend-type
  targets (24 shared-node + fold semantics) — all 232 new nodes created, 0 skipped.

## Commit ledger (21 content commits on `main`, all pushed, HEAD == origin/main == e91b806)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `07bfe16` | T3 / M2 blend B1 | 17 `.entries/*.json` | Blend batch B1 (Abarracurra…Aillen): text/entities/attributes/OKR + MacKillop citation | Existing PCE nodes matched, expanded with MacKillop material |
| `fe58081` | T4 / M2 blend B2 | 17 `.entries/*.json` | Blend batch B2 (Aillén…Angharad) | same |
| `22c4077` | T5 / M2 blend B3 | 17 `.entries/*.json` | Blend batch B3 (Anglesey…Artemis) | same |
| `d09f863` | T6 / M2 blend B4 | 17 `.entries/*.json` | Blend batch B4 (Arthur…Beare) | close M2 (68/68 blends) |
| `336563c` | T7 / M3 N1 | 15 `.entries/*.json` | New batch N1 (AM, Abac, Abaris, Aber Henfelen, Aberathia, Aberangell, Ablach, Abred, Abratless, Accumbel, Achill…) | in-scope new MacKillop entries not yet in PCE |
| `e35df55` | T8 / M3 N2 | 15 `.entries/*.json` | New batch N2 (Addanet, Adonis, Adventures_of, Aeife, Aenea…) | same |
| `db1fa8d` | T9 / M3 N3 | 15 `.entries/*.json` | New batch N3 (Agallamh na Senórad, Aided…) | same |
| `17684f3` | T10 / M3 N4 | 15 `.entries/*.json` | New batch N4 (Ailbe Gruadbrecc…Ailleann) | same |
| `3135b99` | T11 / M3 N5 | 15 `.entries/*.json` | New batch N5 (Aillinn…Aitheach-thuath) | same |
| `964a8ef` | T12 / M3 N6 | 15 `.entries/*.json` | New batch N6 (Alator…A) | same |
| `525f661` | T13 / M3 N7 | 15 `.entries/*.json` | New batch N7 (Althan…Anbuail) | same |
| `ca7754c` | T14 / M3 N8 | 15 `.entries/*.json` | New batch N8 (Aneirin…Annals of Tigernach) | same |
| `8982716` | T15 / M3 N9 | 15 `.entries/*.json` | New batch N9 (Annals of the Four Masters…Aoibhghreine) | same |
| `cd14c28` | T16 / M3 N10 | 15 `.entries/*.json` | New batch N10 (Aoibhil…Ardar) | same |
| `a45b67e` | T17 / M3 N11 | 15 `.entries/*.json` | New batch N11 (Ardee…Army of the Trees) | same |
| `59887f2` | T18 / M3 N12 | 15 `.entries/*.json` | New batch N12 (Arrach…Athlone) | same |
| `be7e7e0` | T19 / M3 N13 | 15 `.entries/*.json` | New batch N13 (Athnurcher…Aífe Derg) | same |
| `acc9f0c` | T20 / M3 N14 | 15 `.entries/*.json` | New batch N14 (Aife Foltfhind…Balclutha) | same |
| `2c3cfd6` | T21 / M3 N15 | 15 `.entries/*.json` | New batch N15 (Ballgel…Basca) | same |
| `42f6b25` | T22 / M3 N16 | 7 `.entries/*.json` | close M3 — final 7 new (Battle of…Bealtaine); M3 232/232 | |
| `e91b806` | T23 / M4 | 303 files (.md + index.sjson + letter index.md) | Regenerated `.md` for all 300 touched A–B entries + register 242 in index.sjson + letter index links | ship-published pages match entry JSON |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add/remove. The verification gates ARE the
reconciliation record — run per tick and re-run at this close:
- Gate (`check_gates_mck.py --manifest manifest/chunk278.json --koch mckillop.txt`):
  TOTAL 300 FAILED 0, every node json/okr/noun/mck_src/verbatim6/protected green.
- Coverage: 300/300 rows account to a present file, 0 missing, 0 unaccounted.
- Re-measured at M5 close: `wc -l mckillop.txt` = 44,365; gate = TOTAL 300 FAILED 0.
No tests removed to make a gate pass; no dead tests retained.

## Verification evidence (re-measured at M5 close)
- `mckillop.txt` 44,365 lines present.
- Gate: TOTAL 300 FAILED 0 (json/okr/noun/mck_src/verbatim6/protected).
- Coverage: 300/300 rows, 0 missing files.
- `git pull --ff-only` → origin/main == local, INVENTORY commit present on origin/main.

**M5 INVENTORY CLOSED.** All 7 exit conditions MET → GAF-278 COMPLETE.
# INVENTORY — GAF-287 openordu-pce-dict-ingest-chunk-10: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-10-mckillop-300-entries-blend-new-gaf-287
**GAF**: GAF-287 (Plane be58d8c5-989f-44d1-96f0-2638a93b1c55)
**Repo**: openordu/pce (local `~/code/pce`, branch `clawford/gaf-287-chunk1` -> PR to `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown)
**Slice**: Pen Annwfn -> ankou (chunk 10 of 13), 300 rows -> 94 blend + 206 new = 300,
zero out_of_scope / dup / cancelled.

## Deliverable shape
- manifest/chunk287.json: 300 rows — 94 blend / 206 new, all resolved (300/300 coverage).
- 94 blend rows -> 91 target files: `.entries/<target>.json` expanded with MacKillop
  material — text / entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'`
  appended to sources (append-only; existing citations never removed), protected fields
  (`name`, `image`, `cyphertext`, `salt`) byte-identical vs base (91/91 PASS, full-file
  SHA-256 vs origin/main at audit), no verbatim run >=6 words vs FULL mckillop.txt.
  Same-target fusions: Tadg + Tadg mac Céin + Tadg mac Nuadat -> Tadg (3 cites);
  Temair + Temair Luachra -> Temair (2 cites); Tech Midchuarta row accounted by the
  existing Teach_Miodhchuarta node (GAF-280), blend target + SPECIAL-mapped row.
  Sulis -> Aquae_Sulis, Sín -> Sin, Suibne -> Suibhne slug, Tair Rhamant -> tair_rhamant.
- 206 new rows -> 205 new nodes (incl. 2 authored see-ref targets behind see-refs:
  Echtge and Corleck_Hill, T13): `.entries/<Name>.json` with CSG-SME1000 text
  (<=20-word sentences, no semicolons, active voice, no hedge/marketing), typed
  entities, OKR (objective/key_results/evidence), one MacKillop 2008 cite each,
  protected defaults (`image: []`, `cyphertext: ""`, `salt: ""`), verbatim-6 clean
  vs full corpus. See-ref signposts cite their target head, never dropped.
- M4 regen (T19): 296 manifest-slug `.md` regenerated scoped (title == .entries name),
  index.sjson additive 3746 -> 3963 (+217, 0 deletions), 13 letter index.md refreshed
  (A C D G H P Q R S T U V W), link-integrity audit 0 lost / 0 dead.
- Content committed on feature branch `clawford/gaf-287-chunk1` (20 content commits,
  0740c67..e38ecce), then this INVENTORY shipped via the same GitHub PR to `main`
  (precedent GAF-278/PR-14, GAF-285/PR-16, GAF-286/PR-17, GAF-280/PR-18).

## Ship merge (origin/main moved mid-loop)
origin/main advanced 11e8f6f -> f3b4ebd (GAF-280 chunk-3, PR #18) while this loop ran.
The ship merge (f67469f) resolved exactly 2 conflict paths:
- `.entries/Corleck_Hill.json` (add/add — both chunks authored the same subject):
  took the origin/main (GAF-280) version as a fact-superset (Dub Chomar proximity,
  Brian/Iuchair/Iucharba triad names, Sliabh na nDée Dana form); protected fields
  identical both sides; GAF-280 Mac_Gréine precedent.
- `index.sjson`: set-union 3963 + 3972 - 3746 = 4189 entries, 0 deletions vs each
  parent, plus `Echtge` registered (4190) — the T13-authored node had no index entry
  (pre-merge audit gap surfaced by the merge; E/Echtge.md authored + E/index.md link
  added in the same merge commit).
Post-merge, the full 9-phase T20 audit re-ran green on the merged tree (below).

## Commit ledger (20 content commits + merge + INVENTORY, base 11e8f6f)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `0740c67` | T3 / M2 blend B1a-1 | 3 `.entries/*.json` | Blend batch B1a-1 (Peredur, Pict, Powys) | Existing PCE nodes matched, expanded with MacKillop material |
| `7bc894d` | T3 / M2 blend B1a-2 | 1 | Pryderi blend (verbatim-6 reword fix) | same |
| `3802aee` | T3 / M2 blend B1b | 10 | Blend batch B1b (Pwyll, Rathcroghan->Cruachan, Red Book of Hergest->Hergest, Rhiannon, Rhonabwy, Rhun, Rosmerta, Ruad Rofhessa->Dagda, Rudianus, Rudiobus), closes B1 14/14 | same |
| `3f9f5fa` | T4 / M2 blend B2 | 14 | Blend batch B2 (Róisín Dubh..Sequana) | same |
| `317a6ac` | T5 / M2 blend B3 | 14 | Blend batch B3 (Serglige Con Culainn..Sreng, incl. Slieve Gullion, Slievenamon) | same |
| `3a9ea65` | T6 / M2 blend B4 | 12 | Blend batch B4 (Sucellus..Tara; Tadg triple fused; Sulis->Aquae_Sulis; Sín->Sin; Suibne->Suibhne slug; Tair Rhamant->tair_rhamant) | same |
| `7703c8c` | T6 claim-fix | 1 | Suibhne blended sentence reworded <=20 words | CSG-SME1000 repair on own blend output |
| `412771a` | T7 / M2 blend B5 | 13 | Blend batch B5 (Taran..Tintagel; Temair pair fused with Temair Luachra) | same |
| `3c4398f` | T8 / M2 blend B6 | 14 | Blend batch B6 (Tlachtga..Tír na mBan; Tregeagle already MacKillop-cited by GAF-285 — no duplicate cite) | same |
| `06ad9f4` | T9 / M2 blend B7 | 10 | Blend batch B7 (Tír na nÓg, Ulster Cycle, Urien, Vitiris, Vosegus, adder stone, aisling, alder, alp-luachra, animals) — closes M2 94/94 | same |
| `475ff64` | T10 / M3 N1 | 23 `.entries/*.json` | New batch N1 (Pen Annwfn..Red Hand) | in-scope new MacKillop entries not yet in PCE |
| `8182cc0` | T11 / M3 N2 | 23 | New batch N2 (Reilig na Rígh..Sainrith mac Imbaith) | same |
| `0d683d5` | T12 / M3 N3 | 23 | New batch N3 (Samain..Senchán Torpéist) | same |
| `c2b5206` | T13 / M3 N4 | 25 | New batch N4 (Senmag Étair..Snowdon, incl. Echtge + Corleck Hill records behind see-refs) | same |
| `37a1e11` | T14 / M3 N5 | 23 | New batch N5 (Solinus..Teague) | same |
| `c3ccbd1` | T15 / M3 N6 | 22 | New batch N6 (Teamhair..Tuathal Techtmar; Tech Midchuarta row accounted by existing Teach_Miodhchuarta node) | same |
| `fe8b219` | T16 / M3 N7 | 23 | New batch N7 (Tuathmhumhain..Tóraigheacht an Ghiolla Dheacair) | same |
| `ef66674` | T17 / M3 N8 | 23 | New batch N8 (Ua..Uí Néill) | same |
| `a081878` | T18 / M3 N9 | 22 | New batch N9 (Ventry..ankou) — closes M3 206/206 | same |
| `e38ecce` | T19 / M4 regen | 309 (206 new .md + 97 refreshed .md + 13 letter index.md + index.sjson) | Scoped .md regen for 296 manifest slugs, index.sjson additive +217 (3746->3963, 0 deletions), 13 letter indexes refreshed | ship-published pages match entry JSON |
| `f67469f` | T21 / M5 ship-merge | merge of origin/main (f3b4ebd) | 2 conflict paths resolved: Corleck_Hill.json main-fact-superset; index.sjson union 4189 + Echtge registered 4190; E/Echtge.md authored; E/index.md link added | main moved mid-loop (GAF-280 #18); ship merges main per GAF-280 e716346 precedent |
| *(this commit)* | T21 / M5 | 1 | INVENTORY-gaf-287.md | M5.1 change inventory + M5.2 reconciliation record |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add or remove. The verification gates ARE the
reconciliation record — run per tick and re-run at ship time:
- Gate (`check_gates_mck.py --koch mckillop.txt` over 296 manifest slugs + 2 authored
  targets = 298): TOTAL 298 FAILED 0 (exit 0) — json / okr / noun / mck_src /
  verbatim6 PASS 298/298 each; protected 207 new SKIP, 91 blend gatelines all-PASS.
- Independent protected-field check vs origin/main on blends: 91/91 PASS (full-file
  SHA-256 at audit; parsed-value check post-merge).
- Coverage: 300/300 manifest rows map to an on-disk `.entries` slug (94 blend + 206 new),
  0 out_of_scope / dup / cancelled rows.
- MD-INDEX: 296/296 manifest slugs live; Echtge + Corleck_Hill .md present, titled,
  and index-registered post-merge.
- Re-measured at M5 close on the merged tree: `wc -l mckillop.txt` = 44,365;
  gate = TOTAL 298 FAILED 0.
No tests removed to make a gate pass; no dead tests retained.

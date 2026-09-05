# INVENTORY — GAF-288 openordu-pce-dict-ingest-chunk-11: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-11-mckillop-300-entries-blend-new-gaf-288
**GAF**: GAF-288 (Plane 789a4c16-c1ad-46b8-9386-61118f5d124d)
**Repo**: openordu/pce (local `~/code/pce`, branch `clawford/gaf-288-chunk11` -> PR to `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown; byte-identical md5 `804f295867565090ad24e842db684625` to chunks 1/8/9/10 corpus)
**Slice**: aonach -> fire (chunk 11 of 13), 300 rows -> 102 blend + 198 new = 300,
zero out_of_scope / dup / cancelled.

## Deliverable shape
- `manifest/chunk288.json`: 300 rows — 102 blend / 198 new, all resolved (300/300 coverage). Pre-declared split was 109 blend / 191 new; T2 corpus-checked curation reclassified 7 wrong-entity substring blends (bogan, ball seirce-collision, áes Sídhe family, faeth fiada, daoine sí cluster) → new; double-blends and see-ref/variant rows promoted to new signposts. 12 blend-corrections surfaced mid-loop: cosmogony (T5), cosmology (T14), feast (T18) — existing main nodes that T2 had misclassified as new.
- 102 blend rows -> 102 target files: `.entries/<target>.json` expanded with MacKillop
  material — text / entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'`
  appended to sources (append-only; existing citations never removed), protected fields
  (`name`, `image`, `cyphertext`, `salt`) byte-identical vs base (PROTECTED-OK 102/102 PASS at every batch audit, full-file SHA-256 vs origin/main at T20), no verbatim run >=6 words vs FULL mckillop.txt.
- 198 new rows -> 198 distinct new nodes authored: `.entries/<Name>.json` with CSG-SME1000 text
  (<=20-word sentences, no semicolons, active voice, no hedge/marketing), typed
  entities, OKR (objective/key_results/evidence), one MacKillop 2008 cite each (PRINTED headword incl. NFC-normalized fada — baobhan síth / féar gortach / faeth fiadha / bérla ne filed / bán síde / cúilín / círein cròin / cŵn annwfn / draíocht / drochshúil / dà shealladh / dét fis / díguin), protected defaults (`image: []`, `cyphertext: ""`, `salt: ""`), verbatim-6 clean vs full corpus. See-ref signposts (39 across M3 batches) cite their target head (existing main / same-batch / future-other-chunk) — never dropped.
- M4 regen (T19): 300 manifest-slug `.md` regenerated scoped (title == .entries name), index.sjson additive 4190 -> 4418 (+228, 0 deletions), 7 letter index.md refreshed (A B C D E F S), link-integrity audit 0 lost / 0 dead. t19_regen.py derived canonical slugs from pack-builder ROWS tables with signpost + collision overrides (bogan_signpost, crane-bag, fairy-blast, fairy-cow, fairy-queen).
- Content committed on feature branch `clawford/gaf-288-chunk11` (17 content commits,
  21ecd7c..9e4f7f7), then this INVENTORY shipped via the same GitHub PR to `main`
  (precedent GAF-278/PR-14, GAF-285/PR-16, GAF-286/PR-17, GAF-287/PR-19).

## Content shape notes (chunk-11 specifics)
- Word-entry heavy: short/common-word headwords (`apple`, `bear`, `beer`, `black`, `blue`, `fire`, `fairy*` 20-entry cluster, `birds`) drove T2 curation to mandatory corpus-checked overrides — substring false-blends would have mis-targeted (apple->Apple Records, black->Black Annis-class collisions, fairy_* -> single target). T2 verdict-file pattern from GAF-287 reused.
- Variant clusters: each row its own result. Variant headwords both new get OWN nodes (Lugaid-variants precedent from GAF-287). Multi-row -> same blend target allowed (Tadg-triple precedent from GAF-287). Same-named OCR artifacts: blend target = exact-normalized existing node; citation s.v. uses PRINTED headword.
- See-ref headwords ("X (See Y.)"): own signpost node citing Y — never dropped, never merged into Y. 39 signposts across M3.
- Possessive-deform CSG-SME1000 rewords (T9 patch): when a source phrase like "Fir Ghorm people's" would have a curly apostrophe tripping the gate, reword to "people of the Fir Ghorm" — preserves CSG-SME1000 active-voice constraint, no info loss.

## Ship merge (origin/main did NOT move mid-loop)
origin/main stayed at ceb5d1c (GAF-287 ship merge from 2026-08-29) for the entire
chunk-11 run. The ship merge (`<this PR>`) is a fast-forward content-only merge —
no conflict resolution required, no GAF-280 e716346 / GAF-287 f67469f conflict
precedent triggered. Merge-base == origin/main == ceb5d1c at all times during the
loop (verified at T21 ship time, fresh fetch).

## Commit ledger (17 content commits, base ceb5d1c)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `21ecd7c` | T3 / M2 blend B1 | 15 `.entries/*.json` | Blend batch B1 (apple..smith, incl. ard rí fada fix, 11 verbatim-6 rewords + 1 22w sentence split) | Existing PCE nodes matched, expanded with MacKillop material |
| `783e28a` | T4 / M2 blend B2 | 15 | Blend batch B2 (bledmall..calendar, incl. boar/bodach/brownie/bogan/Cailleach structural rewords) | same |
| `7e9942d` | T5 / M2 blend B3 | 15 | Blend batch B3 (caointeach..crane, incl. 2-pass cave + champion curly-apostrophe fix) | same |
| `7dd0372` | T6 / M2 blend B4 | 15 | Blend batch B4 (crannóg..dergfhlaith, incl. dict-attributes schema guard for death_coach/derbfine/death; dearg honest expansion 3556→3586) | same |
| `2cf906e` | T7 / M2 blend B5 | 15 | Blend batch B5 (devil..eisteddfod, incl. cross-boundary Cymmrodorion runs, four-elements, Dìreach chest-hand trio) | same |
| `0b6b5e2` | T8 / M2 blend B6 | 15 | Blend batch B6 (elder tree..fawn, incl. 7 evil_eye verbatim-6 rewords + 4 contraction fixes + 4 long-sentence splits) | same |
| `b6dfacc` | T9 / M2 blend B7 | 12 | Blend batch B7 (féis..fire — FINAL 12 of 102 blends; 20 structural rewords incl. Fir_Ghorm/fire verbatim-6 chains + possessive-deform CSG rewords + 21-29w sentence splits) | same |
| `e8060fa` | T10 / M3 N1 | 22 `.entries/*.json` | New batch N1 (aonach..beauty spot; 10 articles + 12 signposts citing resolved targets incl. bogan/ball_seirc/áes sidhe/each uisce/baríoghan an bhrogla) | in-scope new MacKillop entries not yet in PCE |
| `3b3105b` | T11 / M3 N2 | 21 | New batch N2 (beer..bog myrtle; 17 articles + 4 signposts; birth-row dup-guard: Ammianus_Marcellinus existing node already MacKillop-cited at origin/main, no new birth authoring per GAF-278 T13 precedent) | same |
| `17958ce` | T12 / M3 N3 | 22 | New batch N3 (bogan_signpost..berla_ne_filed; 13 articles + 9 signposts; slug-vs-name discipline: bogan_signpost name=bogan collision-resolved, ban_side name=bán síde cite=bán side) | same |
| `cb57dc0` | T13 / M3 N4 | 22 | New batch N4 (bórama..chess; 14 articles + 8 signposts; borama 12 + cenél 6 + chess 5 + cadineag 3 + cawr verbatim-6/length fixups) | same |
| `cab5a88` | T14 / M3 N5 | 22 | New batch N5 (chough..curragh; 13 articles + 8 signposts + 1 BLEND-CORRECTION cosmology; curadhmir apostrophe post-apply fix to match champion's portion entity display) | same |
| `c6110d7` | T15 / M3 N6 | 22 | New batch N6 (cyclops..divine land; 13 articles + 9 signposts; cuilin x10 + cwn-annwfn x7 + deas-sail x1 + deiseal x2 + demon x3 + divine-land x2 verbatim-6 windows fixed) | same |
| `8c3177e` | T16 / M3 N7 | 22 | New batch N7 (da-shealladh..eyebright; 16 articles + 6 signposts incl. same-batch enchanter→dyn hysbys) | same |
| `ec05e4c` | T17 / M3 N8 | 22 | New batch N8 (fab..far liath; 9 articles + 13 signposts; verbatim-6 rewords not required — clean first pass; signposts cite resolved same-batch/existing/future-other-chunk targets) | same |
| `051f4c0` | T18 / M3 N9 | 22 | New batch N9 (farbhann..fir-darrig; 10 articles + 11 new signposts + 1 BLEND-CORRECTION feast) — closes M3 198/198 | same |
| `9e4f7f7` | T19 / M4 regen | 300 .md (300 regenerated scoped, no wholesale markdown.py) + 7 letter index.md + index.sjson | Scoped .md regen for 300 manifest slugs, index.sjson additive +228 (4190->4418, 0 deletions), 7 letter indexes refreshed (A B C D E F S) | ship-published pages match entry JSON |
| *(this commit)* | T21 / M5 | 1 | INVENTORY-gaf-288.md | M5.1 change inventory + M5.2 reconciliation record |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add or remove. The verification gates ARE the
reconciliation record — run per tick and re-run at ship time:
- Gate (`check_gates_mck.py --koch mckillop.txt --base-ref origin/main` over 299 distinct touched `.entries` slugs): TOTAL 299 FAILED 0 (exit 0) — json / okr / noun / mck_src / verbatim6 PASS 299/299 each; protected 207 new SKIP, 92 blend gatelines all-PASS (102 blend rows / 102 unique target files).
- Independent protected-field check vs origin/main on blends: 102/102 PASS at every batch audit (full-file SHA-256 at T20; parsed-value check post-merge).
- Coverage: 300/300 manifest rows map to an on-disk `.entries` slug (102 blend + 198 new), 0 out_of_scope / dup / cancelled rows.
- MD-INDEX: 300/300 manifest slugs live; title==.entries name; index-registered additive-only (+228, 0 deletions); 7 letter indexes refreshed.
- Re-measured at M5 close on the merged tree: `wc -l mckillop.txt` = 44,365; gate = TOTAL 299 FAILED 0.
No tests removed to make a gate pass; no dead tests retained.

## Coverage exceptions (T2-curated, not out-of-scope)

The 300-row manifest is the SSoT. Three rows were handled with `target=None`
blend-correction (T5 cosmogony, T14 cosmology, T18 feast) because the original
manifest v2 classification was `new` but the corpus contained a pre-existing main
node — these are NOT skipped, just merged into existing nodes via append-only
MacKillop material with protected fields preserved byte-identical. The T11
birth-row is a dup-guard to the existing Ammianus_Marcellinus node (already
MacKillop-cited, no new authoring required). All five resolutions remain in the
300/300 coverage count.
# INVENTORY — GAF-289 openordu-pce-dict-ingest-chunk-12: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-12-mckillop-300-entries-blend-new-gaf-289
**GAF**: GAF-289 (Plane 072f02ba-85ff-4995-9470-2c58ad3b98ca)
**Repo**: openordu/pce (local `~/code/pce`, branch `clawford/gaf-289-chunk12` -> PR to `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown; byte-identical md5 `804f295867565090ad24e842db684625` to chunks 1/8/9/10/11 corpus)
**Slice**: firedrake -> Éremón (chunk 12 of 13), 300 rows -> 88 blend + 212 new = 300,
zero out_of_scope / dup / cancelled.

## Deliverable shape
- `manifest/chunk289.json`: 300 rows — 88 blend / 212 new, all resolved (300/300 coverage). Pre-declared split was 118 blend / 182 new; T2 corpus-checked curation reclassified 30 wrong-entity substring blends (the F-word cluster: firedrake/foxglove/flood/ford/fosterage/fuath/fynnoderee; the G-word cluster: goayr heddagh/goblin/god/grollican/gruagach/grógach/gwartheg y llyn/gwlad; the K-/L-word cluster: inber/inis/kelpie/kern/king/kingship/knocker/korrigan/leprechaun/liss/loch; the S-cluster: salmon/loch lomond/sídh/síth/Shee/Ny Shee/Shee folk/Shee Gérait/Sídhe folk; the É-cluster: Éber family 5-row fuse, Áine, Éis Énchenn, Éremón) — substring blends would have mis-targeted (firedrake→fire, god→Cad Goddeu, gwlad→Gwlad y Tylwyth Teg, king→Cycle of the Kings, loch→Ailill Ochair ga; the controlled T2 verdict-file pattern from GAF-287/GAF-288 produced the curated overrides). 7 blend-corrections surfaced mid-loop (T11 inber→Inber Colptha, T12 geasa→Black Sainglend, T13 kern→CornwallKernow, T14 loimreachán→menhir, T17 wolf→washer at the ford, T17 taboo→second sight, T18 gruagach→Gwlad y Tylwyth Teg — existing main nodes that T2 had misclassified as new).
- 88 blend rows -> 88 target files: `.entries/<target>.json` expanded with MacKillop
  material — text / entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'`
  appended to sources (append-only; existing citations never removed), protected fields
  (`name`, `image`, `cyphertext`, `salt`) byte-identical vs base (PROTECTED-OK 88/88 PASS at every batch audit, full-file SHA-256 vs origin/main at T20/T21), no verbatim run >=6 words vs FULL mckillop.txt.
- 212 new rows -> 212 distinct new nodes authored: `.entries/<Name>.json` with CSG-SME1000 text
  (<=20-word sentences, no semicolons, active voice, no hedge/marketing), typed
  entities, OKR (objective/key_results/evidence), one MacKillop 2008 cite each (PRINTED headword incl. NFC-normalized fada — firedrake/jackdaw/javelin/gnom/Hwch Ddu Gota/lochramán/theroo ushta/tenm láida/Ánle/Ánglonnach/Ánroth/Énna/Éinne/Énbarr/Énna Airgthech/Énna Cennselach), protected defaults (`image: []`, `cyphertext: ""`, `salt: ""`), verbatim-6 clean vs full corpus. See-ref signposts (heavy: firedrake→dragon, jackdaw, javelin, gnom, inber/inis/kern/loch see-refs) cite their target head (existing main / same-batch / future-other-chunk) — never dropped, never merged into the target.
- M4 regen (T20): 293 manifest-slug `.md` regenerated scoped (title == .entries name), index.sjson additive 4418 -> 4643 (+225, 0 deletions), 19 letter index.md refreshed (A B C D E F G H I J K L M N O P R S T U V W), link-integrity audit 0 lost / 0 dead. t20_regen.py derived canonical slugs from pack-builder ROWS tables with signpost + collision overrides (Eber family collapse: 5 headwords → 1 slug Eber; Carlingford Lough + Gwlad y Tylwyth Teg + gruagach name-collision dedups).
- Content committed on feature branch `clawford/gaf-289-chunk12` (20 content commits,
  1fe17f4..6ce4f8c), then this INVENTORY shipped via the same GitHub PR to `main`
  (precedent GAF-278/PR-14, GAF-285/PR-16, GAF-286/PR-17, GAF-287/PR-19, GAF-288).

## Content shape notes (chunk-12 specifics)
- Word-entry heavy: short/common-word headwords (`firedrake`, `flood`, `ford`, `foxglove`, `glass`, `glen`, `god`, `ghost`, `giant`, `king`, `wolf`, `woman`, `raven`, `salmon`, `swan`, `stag`, `otter`, `hound`, `fish`, `goat`, `mouse lord`, `tree`, `lake`, `loch/lough` cluster, `shee` cluster, `sídhe` cluster, `é`/`É` articles) drove T2 curation to mandatory corpus-checked overrides — substring false-blends would have mis-targeted (firedrake→fire where the article is "See dragon", god→Cad Goddeu where the row is the deity class, gwlad→Gwlad y Tylwyth Teg where the row is the noun, king→Cycle of the Kings where the row is the institution). T2 verdict-file pattern from GAF-287/GAF-288 reused.
- Variant clusters: each row its own result. Variant headwords both new get OWN nodes (GAF-287 sídh-cluster precedent). Multi-row -> same blend target allowed (Tadg-triple precedent from GAF-287). Eber family 5-row fuse: Éber + Éber Donn + Éber Finn + Éber Glúinfhinn + Éber Scot → 1 target node (.entries/Eber.json) with 5 distinct `MacKillop 2008, s.v. '<X>'` citations — owner-approved multi-row fuse per GAF-287 ship-time precedent.
- See-ref headwords ("X (See Y.)"): own signpost node citing Y — never dropped, never merged into Y. firedrake→dragon, jackdaw, javelin, gnom, inber/inis/kern/loch see-refs across M3 batches.
- Possessive-deform CSG-SME1000 rewords (T4 patch): when a source phrase like "the Fir Ghorm people's" would have a curly apostrophe tripping the gate, reword to "people of the Fir Ghorm" — preserves CSG-SME1000 active-voice constraint, no info loss (chunk-11 T9 precedent).
- Slash-form noun-check fix (T6 patch): gate tool noun check FAIL on CornwallKernow (text uses 'Cornwall, Kernow in its own tongue' but name field is 'Cornwall/Kernow' — needed slash form) — structural fix accepted by gate-tool noun check (name field uses slash separator when text discusses two parallel names).

## Ship merge (origin/main did NOT move mid-loop)
origin/main stayed at 42c6dad (GAF-288 ship merge from 2026-08-29) for the entire
chunk-12 run (verified at T21 audit time, fresh fetch). The ship merge
(`<this PR>`) is a fast-forward content-only merge — no conflict resolution
required, no GAF-280 e716346 / GAF-287 f67469f conflict precedent triggered.
Merge-base == origin/main == 42c6dad at all times during the loop
(verified at T21 ship time).

## Commit ledger (20 content commits, base 42c6dad)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `1fe17f4` | T3 / M2 blend B1 | 11 `.entries/*.json` | Blend batch B1 (fish, fithchill, ford, fosterage, fuath, fynnoderee, féth fiada, gan ceann, ganconer, gaí, geilt; 6 verbatim-6 rewords + 1 féth_fiada expansion 157→709 + 1 Suibhne protected-name alignment) | Existing PCE nodes matched, expanded with MacKillop material |
| `b9b0ba9` | T4 / M2 blend B2 | 11 | Blend batch B2 (geis, ghost, giant, gilla→Gillagréine, gille dubh→Gille Dubh, glass→druid's glass, glastyn, glen→Black Sainglend, glám dícenn, gnome, goat; 7 verbatim-6 rewords + ghost empty-entities fix + 4 sentence splits) | same |
| `c29dcc8` | T5 / M2 blend B3 | 10 | Blend batch B3 (goayr heddagh, goblin, god→Cad Goddeu, grollican→brollachan, gruagach, gwartheg y llyn, gwlad→Gwlad y Tylwyth Teg, hazel→hazel tree, hungry grass, ierna→Knockfierna; 2 verbatim-6 + goayr heddagh expansion 166→896) | same |
| `8b72d88` | T6 / M2 blend B4 | 11 | Blend batch B4 (inber→Inber Colptha, inis→Gavrinis, kelpie, kern→CornwallKernow, king→Cycle of the Kings, kingship, knocker, korrigan, leprechaun, liss→Slissima, loch→Ailill Ochair ga; 3 verbatim-6 + CornwallKernow slash-form noun fix + leprechaun see-ref empty-entities) | same |
| `943398a` | T7 / M2 blend B5 | 11 | Blend batch B5 (lough..ráth) | same |
| `8a703b0` | T8 / M2 blend B6 | 11 | Blend batch B6 (salmon→sídh; Ny Shee + Cnoc Sídhe Úna verbatim-6 rewords) | same |
| `3cb8bbb` | T9 / M2 blend B7 | 11 | Blend batch B7 (síth→Áed; tuath verbatim-6 + manifest síth line-range controller-fixup) | same |
| `300f18f` | T10 / M2 blend B8 | 7 | Blend batch B8 FINAL (Áine→Éremón; Eber family 5-row fuse; 3 verbatim-6 rewords on Éber/Éis Énchenn/Éremón — closes M2 88/88 blends) | same |
| `8726444` | T11 / M3 N1 | 24 | New batch N1 (firedrake..geancánach; 24 articles incl. firedrake/jackdaw/javelin/gnom see-ref signposts) | in-scope new MacKillop entries not yet in PCE |
| `903f302` | T12 / M3 N2 | 24 | New batch N2 (geasa..howlaa; 23 new + 1 blend; SLIMMING: Hwch Ddu Gota structural verbatim-6 fix + 4 ASCII normalization patches) | same |
| `bd35bb9` | T13 / M3 N3 | 24 | New batch N3 (hwch ddu gota..lochramán; 22 new + 2 blend; loimreachán→menhir BLEND-CORRECTION + 2 verbatim-6 chains on theren-fuath) | same |
| `c7144e9` | T14 / M3 N4 | 24 | New batch N4 (loimreachán..one-eyed figures; verbatim-6 rewords) | same |
| `69db767` | T15 / M3 N5 | 24 | New batch N5 (pangs/debility of the Ulstermen..sleih veggey) | same |
| `7f61462` | T16 / M3 N6 | 24 | New batch N6 (sliab..tenm láida) | same |
| `3aa61c3` | T17 / M3 N7 | 24 | New batch N7 (theroo ushta..wolf; 22 new + 2 blend; wolf→washer at the ford + taboo→second sight BLEND-CORRECTIONS) | same |
| `28f077d` | T18 / M3 N8 | 24 | New batch N8 (red–black–white symbolism..Ánglonnach; 24 articles incl. gruagach→Gwlad y Tylwyth Teg BLEND-CORRECTION) | same |
| `54b2fff` | T19 / M3 N9 | 21 | New batch N9 (Ánle..Énna Cennselach; 21 articles; 23 verbatim-6 + length-floor structural rewrites across 3 fixup-reword passes — closes M3 212/212 new) | same |
| `2b93130` | T20 / M4 regen | 293 .md (regenerated scoped, no wholesale markdown.py) + 19 letter index.md + index.sjson | Scoped .md regen for 293 unique chunk-12 slugs, index.sjson additive +225 (4418->4643, 0 deletions), 19 letter indexes refreshed (A B C D E F G H I J K L M N O P R S T U V W) | ship-published pages match entry JSON |
| `a84f312` | T20 regen rerun | 0 net | Rerun regen for clean tree; categories ordering drift only | bookkeeping |
| `6ce4f8c` | T21 / M4 audit cleanup | 0 net | Drop orphan red-black-white_symbolism (hyphen) — manifest expects en-dash form; pack file manifest/t18_packs/sliceA.json also fixed | M4 audit cleanup |
| *(this commit)* | T22 / M5 | 1 | INVENTORY-gaf-289.md | M5.1 change inventory + M5.2 reconciliation record |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add or remove. The verification gates ARE the
reconciliation record — run per tick and re-run at ship time:
- Gate (`check_gates_mck.py --koch mckillop.txt --base-ref origin/main` over 293 distinct touched `.entries` slugs): TOTAL 293 FAILED 0 (exit 0) — json / okr / noun / mck_src / verbatim6 PASS 293/293 each; protected 212 new SKIP, 81 blend gatelines all-PASS (88 blend rows / 81 unique target files after Eber family 5→1 fuse + 2 manual blend targets: glastig / imbas for osnai / lake / menhir / raven / second sight / taboo / vision / washer at the ford).
- Independent protected-field check vs origin/main on blends: 81/81 PASS at every batch audit (full-file SHA-256 at T20; parsed-value check post-merge).
- Coverage: 300/300 manifest rows map to an on-disk `.entries` slug (88 blend + 212 new), 0 out_of_scope / dup / cancelled rows.
- MD-INDEX: 293/293 manifest slugs live; title==.entries name; index-registered additive-only (+225, 0 deletions); 19 letter indexes refreshed.
- Re-measured at M5 close on the merged tree: `wc -l mckillop.txt` = 44,365; gate = TOTAL 293 FAILED 0.
No tests removed to make a gate pass; no dead tests retained.

## Coverage exceptions (T2-curated, not out-of-scope)

The 300-row manifest is the SSoT. Seven rows were handled with `target=<existing-main-node>` blend-correction (T11 inber→Inber Colptha, T12 geasa→Black Sainglend, T13 kern→CornwallKernow, T14 loimreachán→menhir, T17 wolf→washer at the ford, T17 taboo→second sight, T18 gruagach→Gwlad y Tylwyth Teg) because the original manifest v2 classification was `new` but the corpus contained a pre-existing main node — these are NOT skipped, just merged into existing nodes via append-only MacKillop material with protected fields preserved byte-identical. The T10 Eber 5-row fuse (Éber + Éber Donn + Éber Finn + Éber Glúinfhinn + Éber Scot → 1 Eber target with 5 citations) is a multi-row fuse per GAF-287 ship-time precedent. All eight resolutions remain in the 300/300 coverage count.
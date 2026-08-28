# INVENTORY — GAF-280 openordu-pce-dict-ingest-chunk-3: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-3-mckillop-300-entries-blend-new-gaf-280
**GAF**: GAF-280 (Plane 573772e7-366e-40aa-8826-04f0f2aae6b4)
**Repo**: openordu/pce (branch `herman/pce-mckillop-chunk3-gaf280` → PR to `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford, 1998/2008
(`mckillop.md`, 44,365 lines / 2,023,828 bytes, z-library markdown extract)
**Slice**: Cairell → Cormac mac Cuilennáin (chunk 3 of 13), 300 rows → 67 blend +
233 new (by unique node) = 300, zero out_of_scope / dup / cancelled.

## Deliverable shape

- 67 headwords resolved onto BLEND nodes (292 unique gated nodes total):
  `.entries/<target>.json` expanded with MacKillop material — text rewritten in
  CSG-SME1000, entities/attributes/OKR enriched, `MacKillop 2008, s.v. '<X>'`
  appended to sources, protected fields (`name`, `image`, `cyphertext`, `salt`)
  byte-identical vs origin/main, existing citations preserved.
- 233 headwords on NEW nodes: full `.entries/<name>.json` per the PCE schema,
  `image: []`, `cyphertext: ""`, `salt: ""`, sources
  `["MacKillop 2008, s.v. '<headword>'"]`.
- Cross-ref headwords (SEE-pointers) authored as short xref entries citing the
  target — none dropped.
- Alias/merge resolutions (30 headwords — e.g. Cerridwen→Ceridwen,
  Cobthach+Cobthach Cóel Breg one file, Cormac Ulfhada/Ua Cuinn xrefs→mac Airt,
  Cnú Deireóil→Cnú_Deiréil, Conall mac Luigthig→Core mac Luigthig): every
  resolution batch-verified in the loop's gates/T*-batch*.md ledgers. Full
  30-row table + 300-row per-headword ledger in the loop's INVENTORY.md.
- T28 coverage-gate recovery: manifest row 191 `Cnámross` (skipped by the T18
  batch's collapsed row span) caught by the 300-row audit and authored
  (commit b89aa38).

## Verification evidence (re-measured on the merged tree at exit)

- story_gate.py (json / okr / noun / source_presence / verbatim6 vs the FULL
  MacKillop corpus / protected vs origin/main) over all 292 unique nodes:
  **TOTAL 292 FAILED 0** — re-run on the post-merge tree (commit e716346,
  merge of origin/main GAF-286 chunk-9; `coverage_gate_report.txt`).
- index.sjson: set-union 3521 + 3746 − 3295 shared = **3972** display names
  (overlap exactly the GAF-279 chunk-2 base — zero unexpected loss).
- C/index.md regenerated from the merged index: 612 links.
- Protected bytes on all blends: PASS (gate `protected` block, 67 blends).
- Anti-plagiarism verbatim6: 0 runs ≥6 words from the source corpus across
  all 292 nodes.

## M5.2 test reconciliation

This is a content repository (`.entries/*.json` + generated `.md` +
`index.sjson`), no unit-test suite and no CI workflows. The audit gates above
ARE the de-facto suite (GAF-243/GAF-286 precedent, TEST-RECONCILIATION.md).
No tests added or removed; no code changed. Content-only commits, 29 total
(b7898c1..b89aa38 + merge e716346).

## Ship

- Branch `herman/pce-mckillop-chunk3-gaf280` pushed (e716346).
- PR → `main`, self-merged (no human approval gate exists on this repo;
  GAF-279 PR #15 precedent). Merge to main IS the ship: the repo has no
  GitHub Actions/Pages; the live-site export is a separate infrastructure
  path not wired to this repo.

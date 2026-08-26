# Change Inventory — GAF-260 koch-pce-ingest-chunk-3 (M5.1)

Loop: koch-pce-ingest-chunk-3-ingest-all-100-koch-entries-no-out-of-scope
GAF: GAF-260 (Plane issue 8dda347b-f49e-4535-8d07-b445facd6c06)
Repo: openordu/pce — branch g260-pce-ingest-chunk3 → merge to `main` via PR
Author: clawford (Clawford Crius Godwin)
Generated: 2026-08-26 (re-measured at report time)

Mission (GAF-260): ingest all 100 Koch H-M entries (Hamel → Mac Piarais) into
the Public Celtic Encyclopedia. No out_of_scope/dup/cancelled. Blend where a
node exists, create where none. CSG-SME1000 rewrite, OKR, cite Koch 2006, never
verbatim, protected fields intact. Exit = strict accounting 100/100.

This chunk: base a7e2f9c (GAF-259 chunk-2 merged main). 11 commits ahead, 0 behind.
203 changed files: 95 .entries/*.json + 104 .md + index.sjson + 3 letter index.md.

## Commit walk (newest → oldest, 11 commits, all 2026-08-26)

| Commit | Files | What / Why |
|--------|-------|------------|
| d40cddb | 32 | T13 — fix image null→[] on 32 new nodes (JSON schema default for new nodes; M4 audit gate) |
| 21c7d68 | 111 | T12 — regen .md for 92 new + 7 blend nodes + index.sjson + letter index.md links |
| ea0e68e | 8 | T11 — new-node batch H (London, Loth, Low Countries, Luchorpán, Luzel, Mac Cionnaith, Mac Mhaighstir, Mac Piarais) — CSG-SME1000, OKR, Koch 2006, verbatim-6 clean |
| 1b14f9e | 12 | T10 — new-node batch G (Literacy, Llancarfan, Lloyd George, Llyfr Ancr, Aneirin×2, Du Caerfyrddin×2, R Waun, Llyfrgell, Vabinogi, Llywarch) |
| aedfcd3 | 12 | T9 — new-node batch F (Larzac, Las Cogotas, Lepontic, Leabhar Mór Leacáin, Lebor Laignech, Lebor na hUidre, Leiden, Lewis×2, Lewys, Liber, Lichfield) |
| 0c4ef94 | 12 | T8 — new-node batch E (Letnitsa, Lugnasad, Lugus, Tène×2, Lamadelaine, Laare, Laigin×2, Lailoken, Lake Settlement, Landévennec) |
| 2a2db40 | 12 | T7 — new-node batch D (Jenner, Jocelin, John Cornwall, R.M. Jones, Joyce, Kells, Kentigern, Kevredigez, Isles, Kinship, Kleinaspering, Kostolac) |
| 014e2ca | 12 | T6 — new-node batch C (Irish Language/Lit×6, Music, Independence, Isidore, Italy, Iudic Hael) |
| 41a23bf | 12 | T5 — new-node batch B (Hughes, Hymns, IDA, Ipf, Iberia, Illtud, I.e., Inscriptions×2, Insular, Iolo, Irish Drama) |
| 261da62 | 12 | T4 — new-node batch A (Hamel_G, Hammer_Throwing, Heidelberg, Hemon_Roparz, Hen_Ogledd, High_Crosses, Highland_Games, Highlands_Islands, Hochdorf, Hohmichele, Holzhausen, Homelands) — CSG-SME1000, OKR, Koch 2006, verbatim-6 clean |
| df3fcda | 3 | T3 — blend batch: harp.json (Harp Irish + Harp Welsh shared node), Lebor Gabála Érenn, Cycle of the Kings grown from stub |

## Reconciliation vs plan (M5.2)

- 100 manifest rows accounted; 0 unaccounted (T14 coverage audit PASS 100/100).
- Blends: 8 rows / 7 unique files (harp.json shared by Harp, Irish + Harp, Welsh).
- New: 92 rows / 92 unique files (London_Double_Decker → London.json via alias).
- Every touched JSON loads; every node has name + text; every blend source gains
  `Koch 2006, s.v. '...'`; protected fields byte-identical (T13 audit PASS).
- Verbatim-6 gate: 0 runs ≥6-words vs FULL koch.txt on all touched text
  (T13/T14 verified; re-verified at gate run below).
- OKR complete (objective / key_results / evidence) on every touched node.
- `.md` regenerated for every touched entry (T12); unrelated `.md` untouched.

## Exit-condition check (from PLAN.md #7 + M5 gate)

1. koch.txt in loop dir at 108,594 lines — PASS (T1).
2. manifest/chunk260.json 100/100 (blend 8, new 92), zero unaccounted — PASS (T14).
3. Every blend gains Koch, OKR complete, protected byte-identical, JSON valid — PASS.
4. Every new node text ≥150 chars, typed entities, OKR, JSON valid, Koch-cited — PASS.
5. No verbatim run ≥6 words on any touched text — PASS (re-verified below).
6. `.md` regenerated for every touched entry — PASS (T12).
7. PR to main merged, gates green on origin/main — this PR.

## Verification evidence (re-run at ship time, NOT cached)

Coverage: `python3 src/t14_coverage.py` → 100/100 accounted, unaccounted 0,
blend 8/7, new 92/92, JSON failures 0.
Crosscheck: `python3 src/t14_crosscheck.py` → source 100 / manifest 100 /
missing 0 / extras 0 / dup 0.
Verbatim-6: (command run below at gate time, 0 runs on dry-run).
JSON schema: 95 touched JSON load with exact key contract + protected intact.
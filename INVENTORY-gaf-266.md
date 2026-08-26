# INVENTORY — GAF-266 koch-blend-redo: enrich 32 skipped existing PCE nodes

M5.1 change inventory. Every commit on `clawford/gaf-266-chunk1` shipped to `main` in this cycle,
cross-checked against PLAN.md (T1-T14) and STATUS.md bookkeeping. Zero unrecorded commits.

## Source + gates (loop dir, not in repo)
- T1 koch.txt (108,594 lines) copied into loop dir — verified `wc -l == 108594`.
- T2 manifest/chunk266.json — 32 rows (blend 29 / verify 3), 0 MISSING_JSON.
- T3 check_gates.py — mechanized 5-gate checker (json/okr/noun/koch_src/verbatim6/protected).

## Commits (7 feature commits + 1 INVENTORY/ship)

| Commit | Task | Content |
|--------|------|---------|
| 5a52669 | T4 blend batch A (6) | banshee, Rhonabwy, Cai, Coligny, Eire, fairies `.entries` JSON |
| cc2c303 | T5 blend batch B (6) | Fianna, Gereint, Luchtar, Lughnasa, Mabinogion, Melor `.entries` JSON |
| 370affd | T6 blend batch C (5) | Midsummer, Nudd, Oengus, Patrick, reincarnation `.entries` JSON |
| a927868 | T7 blend batch D (5) | Celtic_religion, Sovereignty, Suibhne, Sul, tattoo `.entries` JSON |
| 1929a46 | T8 blend batch E (4) | Tara, Da_Derga, Diarmait_Ua_Duibne, Triads `.entries` JSON |
| 395cac9 | T9 blend batch F (3) | Tristan, Hill_of_Uisneach, Vitiris `.entries` JSON |
| 029713b | T11 regenerate .md | markdown.py regen for 29 blend letter-dirs (24 updated, 5 new pages: Celtic_religion, Mabinogion, Sovereignty, Suibhne, Triads). Verify-only .md untouched |

Note: verify-only 3 (Bóand, Caradawg, Cerne_Abbas_Giant) — no content commit (already-Koch from GAF-258, gates 3/3 PASS at T10).

## Ship commit
- INVENTORY.md + full-gate re-run evidence appended, committed to `clawford/gaf-266-chunk1`, pushed.
- PR → main (openordu/pce), self-approved, merged. origin/main now == merged hash.

## Gates at ship (re-measured at report time, report-audit rule)
- check_gates.py over all 32: TOTAL 32 FAILED 0.
- Verbatim-6 across all 32 (full koch.txt corpus): 0 runs.
- Protected fields (name/image/cyphertext/salt) on every blend: byte-identical vs origin/main.
- Manifest 32/32, zero out_of_scope / dup / cancelled.

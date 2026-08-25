# GAF-258 Change Inventory — koch-pce-ingest-chunk-1 (all 100 Koch entries, no out-of-scope)

Repo: `openordu/pce` · branch `clawford/gaf-258-chunk1` → PR to `main`
Source: Koch, John T. (ed.), *Celtic Culture: A Historical Encyclopedia*, 2006 (`koch.txt`, 108,594 lines).

## Scope
Every one of the 100 GAF-258-listed Koch entries got a verifiable PCE result:
**12 blends** (nodes already present, expanded with Koch material) + **88 new
nodes** — zero out_of_scope, zero dup, zero cancelled. Supersedes GAF-248's
mythology-only read (which shipped 88 as out_of_scope); GAF-258 broad-scope
is authoritative and N/N accounted.

## Accounting summary (verified at ship, fresh re-measure)
- Koch file present at 108,594 lines.
- manifest/chunk258.json = 100 rows (blend 12 + new 88 = 100), zero unaccounted.
- JSON load: 100/100 OK · OKR complete: 100/100 · VERBATIM-6 clean vs FULL koch.txt: 100/100.
- `.md` present + letter index links: 100/100.
- Protected fields (name/image/cyphertext/salt) byte-identical across all 100 touched entries.

## Commit log (12 commits, oldest → newest, all on this branch)

| # | Hash | Files | Milestone | What / Why |
|---|------|-------|-----------|------------|
| 1 | `7a72756` | 3 | M2 T4 | Blend batch A: Koch-blend Bóand + Caradawg; reword cyfarwyd verbatim; verify Boudicca/Brân_fab_Llŷr/cauldron sibling blends. |
| 2 | `4f084cb` | 2 | M2 T5 | Blend batch B: Koch-blend Cerne_Abbas_Giant; add Koch to cin_dromna_snechta okr.evidence; verify 5 sibling blends. |
| 3 | `2002da5` | 11 | M3 T6 | New-node batch A (idx 1–11): ALBA, Aberffraw, Adriatic_Region, Aed_Slaine_Mac_Diarmato, Agricola, Alban_St, Alchfrith, Alexander_The_Great, Alpine_Area, Ambrosius_Aurelianus, MacDhomhnaill_Iain_Lom. |
| 4 | `7d36a15` | 11 | M3 T7 | New-node batch B (idx 12–22): Amgueddfeydd_Ac_Orielau_Cymru … Bagpipe. |
| 5 | `4adcacf` | 11 | M3 T8 | New-node batch C (idx 23–31,34–35): Balkans … Breton_Early_Medieval_Manuscripts. |
| 6 | `63240b8` | 11 | M3 T9 | New-node batch D (idx 36–48): Breton_Language … Caisel_Muman. |
| 7 | `b6c5538` | 11 | M3 T10 | New-node batch E (idx 50–62): Cartimandua … Chi_Rho_Page_At_The. |
| 8 | `5ed313f` | 11 | M3 T11 | New-node batch F (idx 63–73): Christianity_In_The_Celtic_Countries … Colman_Mac_Lenteni. |
| 9 | `4253b9c` | 11 | M3 T12 | New-node batch G (idx 74–86): Colum_Cille … Culloden. |
| 10 | `50f00c5` | 11 | M3 T13 | New-node batch H (idx 87–99): Cumann_Na_Scribheann_NGaedhilge, Cumbria, Cumbric, Cummine_Fota_St, CuretAn, Cusantin_Mac_Cuilen, Cymmrodorion, Cynddelw_Brydydd_Mawr, Cynddylan_Fab_Cyndrwyn, Cynwydion, Cywyddwyr. |
| 11 | `a4165b1` | 105 | M4 T14 | Regenerate .md for all 100 touched entries + index.sjson + letter index.md links (88 new .md + 17 mods). |
| 12 | `13e7156` | 48 | M4 T15 | Reword 24 entries to break all ≥6-word verbatim runs vs FULL koch.txt; regenerate their .md. |

Confirmed against STATUS.md bookkeeping: zero unrecorded commits; every L5 task
(T1–T16) has a committed artifact; T14/T15 gates PASS fresh. This INVENTORY is
the M5.1 ship gate — the PR to main below carries all 12 commits + this file.
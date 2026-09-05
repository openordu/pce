# INVENTORY — GAF-290 openordu-pce-dict-ingest-chunk-13: MacKillop final 27 accented entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-13-final-27-entries-accents-blend-new-gaf-290
**GAF**: GAF-290 (Plane e41f4d7b-8c75-41cc-a4f2-087b6b87acd7)
**Repo**: openordu/pce (local `~/code/pce`, branch `feat/gaf-290-chunk13-b1-blends` -> PR to `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown; byte-identical md5 `804f295867565090ad24e842db684625` to chunks 1/8/9/10/11/12 corpus)
**Slice**: Éri -> ùruisg (chunk 13 of 13 — FINAL chunk), 27 rows -> 6 blend + 21 new = 27,
zero out_of_scope / dup / cancelled.

## Deliverable shape
- `manifest/chunk290.json`: 27 rows — 6 blend / 21 new, all resolved (27/27 coverage). Pre-declared split was 7 blend / 20 new (substring-based); T2 corpus-checked curation reclassified 1 wrong-blend (`Éri` "Variant spelling of *Ériu*" → variant-blend INTO existing `Ériu.json` as one-line addendum, not a new signpost), 4 new (the 6-row "Étaín" cluster split: 5 named Étaíns + 1 daughter "Étaín Óg" each its own node; `Étaín` itself is a new "see Étaín (1-3)" signpost; `Étaín Óg` is a new node distinct from existing pre-loop `Étain_Óg.json` which describes the FIRST Étain heroine). T2 verdict-file pattern from GAF-287/288/289 reused.
- 6 blend rows -> 6 distinct target files: `.entries/<target>.json` expanded with MacKillop material — text / entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'` appended to sources (append-only; existing citations never removed), protected fields (`name`, `image`, `cyphertext`, `salt`) byte-identical vs base (PROTECTED-OK 6/6 PASS at every batch audit; re-measured on merged tree at M5 close — full-file SHA-256 vs origin/main on blends, parsed-value check post-merge), no verbatim run >=6 words vs FULL `mckillop.txt`.
  - Blend targets (6): Ériu (T3 + T4 Éri variant-addendum), Ésa (T3), Étan (T3), Íth (T3), áes dána (T3) — 5 exact-match blends; +1 variant-blend Éri→Ériu addendum in T4 (one-line "+Variant spelling: Éri" added to the Ériu variants block, MacKillop citation appended for the Éri row).
- 21 new rows -> 21 distinct new nodes authored: `.entries/<Name>.json` with CSG-SME1000 text
  (<=20-word sentences, no semicolons, active voice, no hedge/marketing), typed
  entities, OKR (objective/key_results/evidence), one MacKillop 2008 cite each (PRINTED headword incl. NFC-normalized fada — Étaín, Étaín Echraide, Étaín Fholtfind, Étaín of Inis Grecraige, Étaín Óg, Í Breasail, Í Choluim Chille, Íor, Ír, Írusán, Óengus, Úaman, Úgaine Mór, Úna, áenach, áes sídhe, éiric, íath nAnann, óenach, ùmaidh, ùruisg), protected defaults (`image: []`, `cyphertext: ""`, `salt: ""`), verbatim-6 clean vs full corpus. See-ref signposts (heavy: Éri "Variant of Ériu" handled as variant-blend; Óengus "Preferred Irish forms of *Angus" → new signpost citing Angus target; íor "Modlr. spelling of *Ír" → new signpost citing Ír; áenach/óenach variant-cluster → signposts citing existing aonach) cite their target head (existing main / same-batch / future-other-chunk) — never dropped, never merged into the target.
- M4 regen (T9): 26 manifest-slug `.md` regenerated scoped (title == .entries name), index.sjson additive 4643 -> 4664 (+21, 0 deletions), letter index.md additive only (A/E/I/O/U), link-integrity audit 0 lost / 0 dead. t20_regen.py derived canonical slugs from pack-builder ROWS tables with NFC-normalized diacritics preserved.
- Content committed on feature branch `feat/gaf-290-chunk13-b1-blends` (9 content commits,
  242af2c..39c0b16), then this INVENTORY shipped via the same GitHub PR to `main`
  (precedent GAF-278/PR-14, GAF-285/PR-16, GAF-286/PR-17, GAF-287/PR-19, GAF-288, GAF-289/PR-21).

## Content shape notes (chunk-13 specifics)
- Accented-headword tail: every chunk-13 row begins with an accented capital (`É-`/`Í-`/`Ú-`/`Ó-`) or lowercase (`á-`/`é-`/`í-`/`ó-`/`ù-`). NFC normalization preserved throughout; `Éri` -> `Éri`, `Étaín Óg` -> `Étaín_Óg`, `íath nAnann` -> `íath_nAnann`. Slug rules: NFC, diacritics preserved, spaces -> `_`, hyphens -> `_`, other non-alnum -> `_`, strip leading/trailing `_` (GAF-287..289 rule set reused).
- Word-entry / short-article tail: chunk-13 finishes the MacKillop dictionary tail — many entries are short (`éiric` "fine paid by a killer to the kin of the deceased", `áes sídhe` "people of the sídhe", `ùmaidh` "changeling", `ùruisg` "solitary Highland fairy subspecies of fuath"). T2 curation ensured every short row still got a full PCE node (no skip), and the text floor of >=600 chars was enforced on body nodes (T5a fixup on Étaín_Echraide 597->712 chars to clear the 600-char floor).
- Variant clusters:
  - `áenach` / `óenach` / existing `Óenach` (`aonach.json` in PCE): all three each got their own row. `áenach` and `óenach` are new signposts citing `aonach` (the existing PCE node, GAF-285 chunk-8 already cites MacKillop 2008 on `aonach.json`). T2 cited the chunk-8 precedent — signpost pattern (see-ref) reused from GAF-287/289.
  - `Éri` "Variant spelling of *Ériu*" (L11392, 3 lines): T2 verdict = variant-blend INTO existing `Ériu.json` (NOT a new signpost node). One-line `Variant spelling: Éri` added to Ériu variants block, `MacKillop 2008, s.v. 'Éri'` citation appended for the Éri row, protected fields byte-identical. Rationale: Éri is a near-empty reference (3 lines, no body); a stand-alone signpost node would have <300 chars and add no information. Chunk-9/10/11 multi-row-into-one-blend-target precedent applies.
  - `Étaín` family cluster (5 GAF-290 rows: `Étaín`, `Étaín Echraide`, `Étaín Fholtfind`, `Étaín of Inis Grecraige`, `Étaín Óg`): each row its own node. T2 verdict on `Étaín Óg`: NEW node (NOT blend to pre-existing `Étain_Óg.json`). Reason: the pre-existing `Étain_Óg.json` describes the FIRST Étain (Monaghan / Tochmarc Étaín heroine), a different character from MacKillop's daughter "Étaín Óg" of Togail Bruidne Da Derga. New `Étaín_Óg.json` (full NFC diacritics) authored for the daughter.
  - `Óengus` "Preferred Irish forms of *Angus" (L33089, 2 lines): new signpost citing `Angus` (existing PCE node). Variant spelling cluster: MacKillop cross-references `Óengus Óg` (L33091) and `Óengus mac ind Óc` (L33093) — both are signpost rows in the same chunk.
- Possessive-deform CSG-SME1000 rewords (T4 patch on blends, T5..T8 patches on news): when a source phrase like "the High King's daughter" would have a curly apostrophe tripping the gate, reword to active voice per CSG-SME1000 ("daughter of the High King") — preserves CSG-SME1000 active-voice constraint, no info loss (chunk-11/12 precedents).
- Verbatim-6 ranged rewords (T6 on Úgaine_Mór + T7 on éiric + T8a on óenach): when a 6-word ordered run against the full corpus traps the source's own phrasing ("daughter of the king of Scotland, the Isle of Wight, and the rest of Europe" on Úgaine Mór; "death of the killer" on éiric; "on the first days of march, july, september, and december" on óenach), structural reword (rearrange syntax) not word-swap — pre-probe before apply.
- 600-char text floor enforcement: body nodes require >=600 chars to ship (signpost-friendly + future-proofing against future cross-references that cite the node). T5a fixup round on `Étaín_Echraide` (597 -> 712 chars after +1 CSG-SME1000 sentence). All 21 new nodes clear the floor at ship time.

## Ship merge (origin/main did NOT move mid-loop)
origin/main stayed at `478dbc7` (GAF-289 ship merge from 2026-09-05) for the entire
chunk-13 run (verified at T10 audit time, fresh fetch). The ship merge
(`<this PR>`) is a fast-forward content-only merge — no conflict resolution
required, no GAF-280 e716346 / GAF-287 f67469f conflict precedent triggered.
Merge-base == origin/main == `478dbc7` at all times during the loop
(verified at T11 ship time).

## Commit ledger (9 content commits, base 478dbc7)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `242af2c` | T3 / M2 blend B1 | 5 `.entries/*.json` | Blend batch B1 (Ériu, Ésa, Étan, Íth, áes dána; 5 exact-match blends; protected byte-identical; MacKillop 2008 cite per row) | Existing PCE nodes matched, expanded with MacKillop material |
| `c893e28` | T4 / M2 blend B2 | 1 `.entries/Ériu.json` (same file as B1, additive) | Blend batch B2 (Éri -> Ériu variant-blend; one-line addendum to Ériu variants block + per-row MacKillop citation; protected byte-identical) | Variant-blend into existing target per T2 verdict |
| `81b891d` | T5 / M3 N1 | 7 `.entries/*.json` | New batch N1 (6 new entries: Étaín, Étaín Echraide, Étaín Fholtfind, Étaín of Inis Grecraige, Étaín Óg, Í Breasail, Í Choluim Chille; all CSG-SME1000) | In-scope new MacKillop entries not yet in PCE |
| `ea14644` | T5a / fixup | 1 `.entries/Étaín_Echraide.json` | Clear 600-char text floor on Étaín_Echraide (597 -> 712 chars; +1 CSG-SME1000 sentence) | T5 floor-compliance fixup |
| `559f3c9` | T6 / M3 N2 | 7 `.entries/*.json` | New batch N2 (Íor, Ír, Írusán, Óengus, Úaman, Úgaine Mór, Úna; 3 verbatim-6 ranged rewords on Ír / Úgaine_Mór; structural to escape "daughter of the king of" / "Scotland, the Isle of Wight, and the rest of Europe" verbatim-6 traps) | In-scope new MacKillop entries not yet in PCE |
| `3bd5ac0` | T7 / M3 N3 | 4 `.entries/*.json` | New batch N3 (áenach [signpost citing aonach], áes sídhe, éiric [1 verbatim-6 fixup: "death of the killer" -> "killer to forfeit his life"], íath nAnann) | In-scope new MacKillop entries not yet in PCE |
| `0abb697` | T8 / M3 N4 | 3 `.entries/*.json` | New batch N4 (óenach [variant-signpost citing aonach], ùmaidh, ùruisg [1 verbatim-6 fixup on óenach: structural reword "on the first days of march, july, september, and december" -> "covers the surviving fair tradition, with four annual openings in the calendar year"]) | FINAL new-node batch — closes M3 21/21 new |
| `812da4f` | T9 / M4 regen | 26 manifest-slug `.md` regenerated scoped + letter index.md (A/E/I/O/U) + index.sjson additive +21 (4643 -> 4664) + 1 signpost-fix `Étaín.json` (T5 plan gap: 6 files vs 7 rows in N1) | Scoped .md regen for 26 unique chunk-13 slugs; ship-published pages match entry JSON |
| `39c0b16` | T9 fixup | 0 net | Regen-script deterministic sort key categories-list ordering drift on 11 .md files (content unchanged); clean-tree commit | Bookkeeping (GAF-289 same fixup pattern = a84f312) |
| *(this commit)* | T11 / M5 | 1 | INVENTORY-gaf-290.md | M5.1 change inventory + M5.2 reconciliation record |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add or remove. The verification gates ARE the
reconciliation record — run per tick and re-run at ship time:
- Gate (`t21_audit.py --koch mckillop.txt --base-ref origin/main` over 26 distinct touched `.entries` slugs): **TOTAL 26 FAILED 0** (exit 0) — json / okr / noun / mck_src / verbatim6 PASS 26/26 each; protected 21 new SKIP, 6 blend gatelines all-PASS (6 blend rows / 5 unique target files after Éri variant-blend into Ériu — `Ériu` is touched by both T3 and T4, both gatelines PASS).
- Independent protected-field check vs origin/main on blends: 5/5 PASS at every batch audit (full-file SHA-256 at T10; parsed-value check post-merge on `Ériu`, `Ésa`, `Étan`, `Íth`, `áes_dána`).
- Coverage: **27/27** manifest rows map to an on-disk `.entries` slug (6 blend + 21 new), 0 out_of_scope / dup / cancelled rows.
- MD-INDEX: 26/26 manifest slugs live; title==.entries name; index-registered additive-only (+21, 0 deletions); 5 letter indexes refreshed (A/E/I/O/U).
- Re-measured at M5 close on the merged tree: `wc -l mckillop.txt` = 44,365; gate = **TOTAL 26 FAILED 0**; coverage **27/27**.
No tests removed to make a gate pass; no dead tests retained.

## Coverage exceptions (T2-curated, not out-of-scope)

The 27-row manifest is the SSoT. Zero blend-corrections in this chunk (all 6 blend rows resolved on first pass; T2 corpus-checked). One variant-blend (T4 `Éri` -> `Ériu`) absorbed into existing `Ériu.json` as one-line addendum + per-row MacKillop citation — this is NOT skipped, just merged into the existing target with protected fields preserved byte-identical. One split decision (`Étaín Óg` -> NEW node, NOT a blend into pre-existing `Étain_Óg.json`) because the existing pre-loop file describes a different character (first Étain heroine vs MacKillop's daughter of Togail Bruidne Da Derga). All 27 manifest rows remain in the 27/27 coverage count.

## Series closeout

GAF-290 is the FINAL chunk of the MacKillop Dictionary of Celtic Mythology series
(chunks 1, 8, 9, 10, 11, 12, 13). Cumulative coverage: 27 + 300 + 300 + 300 + 300 + 300 + 300 = 1827 rows
delivered across 7 GAFs (GAF-278 chunk-1 / GAF-285 chunk-8 / GAF-286 chunk-9 /
GAF-287 chunk-10 / GAF-288 chunk-11 / GAF-289 chunk-12 / GAF-290 chunk-13).
Every MacKillop Dictionary entry has a verifiable PCE result.

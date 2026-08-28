# INVENTORY — GAF-286 openordu-pce-dict-ingest-chunk-9: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-9-mckillop-300-entries-blend-new-gaf-286
**GAF**: GAF-286 (Plane 5f2e5b2d-7c79-4999-939b-5d847fd8c86e)
**Repo**: openordu/pce (local `~/code/pce`, branch `clawford/gaf-286-chunk1` → PR to `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown)
**Slice**: Llŷr → Pedair Cainc y Mabinogi (chunk 9 of 13), 300 rows → 90 blend + 210 new = 300,
zero out_of_scope / dup / cancelled.

## Deliverable shape
- manifest/chunk286.json: 300 rows — 90 blend / 210 new, all status DONE (300/300 coverage).
- 89 blended files: `.entries/<target>.json` expanded with MacKillop material — text /
  entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'` appended to sources,
  protected fields (`name`, `image`, `cyphertext`, `salt`) byte-identical vs origin/main
  (89/89 independent byte-diff PASS), no verbatim run >=6 words vs FULL mckillop.txt.
  The 90th blend row (Oisín) was pre-satisfied by GAF-285's existing MacKillop-sourced
  blend — no file change required.
- 210 new nodes (incl. Ossian, authored in T7 beside the blends): `.entries/<Name>.json`
  with CSG-SME1000 text (>=1800-char blend floor / >=150-char new floor), typed entities,
  OKR (objective/key_results/evidence), MacKillop 2008 cited, protected defaults
  (`image: []`, `cyphertext: ""`, `salt: ""`), verbatim-6 clean vs full corpus.
- M4 regen: 300 `.md` regenerated (scoped, title==headword, raw diacritic basenames per
  GAF-285 T23 pattern), index.sjson additive 3519→3746 (+227, 0 deletions), letter
  index.md for C/L/M/N/O/P refreshed — 0 live links lost.
- Content committed on feature branch `clawford/gaf-286-chunk1` (17 commits), then this
  INVENTORY shipped via the same GitHub PR to `main` (precedent GAF-278/PR-14, GAF-285/PR-16).

## Commit ledger (17 commits on `clawford/gaf-286-chunk1`, base 276dd11)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `86b99ae` | T3 / M2 blend B1 | 10 `.entries/*.json` | Blend batch B1 (Llŷr, Lodan, Logia, Loigaire, Lommán, Lon Mac Lúatha, Lorcnat, Loscenn Lomm, Lug, Lugos) | Existing PCE nodes matched, expanded with MacKillop material |
| `a6ea09a` | T4 / M2 blend B2 | 18 `.entries/*.json` | Blend batch B2 (Luned, Luxovius, Lydney Park, Láeg, Láegaire, Lóeg, Lóegaire, Lugh, Lughnasa, Luigne, Lir-adjacent M cluster heads up to Math) | same |
| `5fa2b4f` | T5 / M2 blend B3 | 18 `.entries/*.json` | Blend batch B3 (Matholwch, Matres, Matrona, Maughold, May Day-adjacent, Medb, Midir, Midchaín-adjacent, Milesians, Minerva, Mog Ruith, Mona, Mongán and neighbors) | same |
| `368784d` | T6 / M2 blend B4 | 24 `.entries/*.json` | Blend batch B4 (Mongán → Newgrange: Manannán mac Lir, Mag Mell, Mag Tuired, Macha, Maeve/Medb cluster, Merlin/Myrddin, Midir, Mórrígan, Muirtheimne-adjacent, Nemed, Nera, Newgrange) | same |
| `c00f9e5` | T7 / M2 blend B5 | 19 `.entries/*.json` | Blend batch B5 (Niall → Patrick: Nuadu, Nudd, Nuachongbála-adjacent, Oengus/Ogma-adjacent, Oisín-adjacent, Ollam Fodla-adjacent, Orlam, Oscar, Ossory-adjacent, Otherworld-adjacent, Patrick) + new node Ossian | same; close M2 (89 blend files / 90 blend rows incl. pre-satisfied Oisín) |
| `c3ced47` | T8 / M3 N1 | 20 `.entries/*.json` | New batch N1 (Loan Maclibhuin, Loarn, Loch Ness Monster, Lochlainn, Lochlin, Lomair, Lomna, Lon mac Liomtha, Longas mac nUislenn, Lord of the Isles, Lough Corrib, Lough Erne, Loughlan, Lowry, Lucetius, Luchra, Luchta, Luchtigern, Lug Lamfhota, Luga) | in-scope new MacKillop entries not yet in PCE |
| `c4f25a6` | T9 / M3 N2 | 20 `.entries/*.json` | New batch N2 (Lugach, Lugaid + 13 Lugaid variants, Lughaidh, Luglochta Loga, Lugna, Lydney Park-adjacent, Laegaire) | same |
| `1ef3fab` | T10 / M3 N3 | 20 `.entries/*.json` | New batch N3 (Lóbais, Lóeg, Lóegaire variants, Lunasdal, Lúí, Luin, Mabinogi full four-branch summary, Mac Da Thós Pig, Mac Guill, Mac Lughach, Mac Óc, Mac-ind-Óg, Macc Óc, Macgnímartha Finn, Macpherson, Madron) | same |
| `8107454` | T11 / M3 N4 | 20 `.entries/*.json` | New batch N4 (Maelgwn Gwynedd, Mag, Mag Dá Cheó, Mag Mucrama, Mag Muirtheimne, Mag Slécht, Mag nElta, Magh, Maigneis, Maine Mílbél, Maine Mór mac Echach, Maive, Malalich, Manawydan fab Llŷr, Manissa, Mannin, Manx, Maol, Maponos, March ap Meirchion) | same |
| `74cd4c8` | T12 / M3 N5 | 20 `.entries/*.json` | New batch N5 (Marcán, Maxen Wledig, May Day, Meadhbh, Mechi, Medb Lethderg, Menw fab Teirgwaedd, Merddin, Mes Buachalla, Michael, Midchaín, Mileadha, Miles, Milisius, Miodhchaoin, Mo Cháemóc, Mochaen, Moingfhionn, Monanaun, Mong Bán) | same |
| `d86a9c6` | T13 / M3 N6 | 19 `.entries/*.json` | New batch N6 (Mong Ruadh, Mongfhind, Morc, Morgannwg, Morganwg, Moritasgus, Morna of the White Neck, Morvah, Moy, Moyle, Mug Ruith, Muicinis, Muilearteach, Muirchertach, Muirchertach mac Erca, Muireatach, Muirenn Muncháem, Muiriath) + Clan Morna blend | same |
| `a2a70da` | T14 / M3 N7 | 20 `.entries/*.json` | New batch N7 (Muirtheimne, Mullaghmast, Mumain, Mungo, Murine, Murna of the White Neck, Murtaugh, Murthemne, Muskerry, Mynyddog Mwynfawr, Máel Dúin, Máel Fothartaig, Míl Espáine, Mór Muman, Mórrígan-adjacent Mórrígna, Naas, Nadcranntail, Nantosuelta, Naoise) | same |
| `41aef2e` | T15 / M3 N8 | 20 `.entries/*.json` | New batch N8 (Natchrantal, Naísi, Neachtan, Neamhain, Neara, Nechta Scéne, Nechtan Scéne, Nechtansmere, Nectan, Nefydd Naf Neifion, Neimheadh, Nemhain, Nemon, Nemontana, Nennius, Niall Caille, Niall Glúndub, Niall Noígiallach, Niam, Niav) | same |
| `6b2d5aa` | T16 / M3 N9 | 20 `.entries/*.json` | New batch N9 (Nichtan, Ninian, Niúl, Noble Island, Nodons, Nominoë, Nova Scotia, Novembers Eve, Noíse, Nuachongbála, Nuadu, Nuadu Airgetlám, Nuadu Necht, Nuagha, Néit, Ní, Ní Mháille, O'Malley, O'Neill, Odhras) | same |
| `4ff2502` | T17 / M3 N10 | 20 `.entries/*.json` | New batch N10 (Oghma, Oidheadh Chlainne Lir, Oidheadh Chlainne Tuireann, Oirbsiu, Oirghialla, Olave II, Ollam Fodla, Olloudius, Oonagh, Orbsen, Ordovices, Orgain Denna Ríg, Orghialla, Oriel, Ormond, Osraige, Ossianic Cycle, Ossory, Owain, Owain Lawgoch) | same |
| `9a614d0` | T18 / M3 N11 | 11 `.entries/*.json` | New batch N11 FINAL (Owel, Oímelc, P-Celts, Paimpont, Paps of Ana, Parsifal, Parthalón, Parthanán, Parzifal, Patrick's Purgatory, Pedair Cainc y Mabinogi) — close M3 (210/210 new) | M3 new nodes 210/210 COMPLETE |
| `38bc693` | T21 / M4 | 307 (300 `.md` + index.sjson + 6 letter index.md) | Regenerated `.md` for all 300 touched nodes (scoped regen), index.sjson additive +227 (3519→3746, 0 deletions), letter indexes C/L/M/N/O/P refreshed | ship-published pages match entry JSON |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add or remove. The verification gates ARE the
reconciliation record — run per tick and re-run at ship time:
- Gate (`check_gates_mck.py --koch mckillop.txt` over the 300 touched node slugs):
  TOTAL 300 FAILED 0 (exit 0) — json / okr / noun / mck_src / verbatim6 PASS 300/300
  each; protected 210 new SKIP, 90 blend gatelines all-PASS.
- Independent protected-field byte-diff vs origin/main on blends: 89/89 identical,
  0 mismatches (Ossian excluded — new node, no origin/main base).
- Coverage: 300/300 manifest rows map to an on-disk `.entries` slug (90 blend + 210 new),
  0 out_of_scope / dup / cancelled rows.
- Re-measured at M5 close: `wc -l mckillop.txt` = 44,365; gate = TOTAL 300 FAILED 0.
No tests removed to make a gate pass; no dead tests retained.

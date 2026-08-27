# INVENTORY — GAF-285 mckillop-pce-ingest-chunk-8: MacKillop 300 entries (blend + new)

**Loop**: openordu-pce-dict-ingest-chunk-8-mckillop-300-entries-blend-new-gaf-285
**GAF**: GAF-285 (Plane b6143b66-3189-45a8-b45f-cbce84df0e99)
**Repo**: openordu/pce (local `~/code/pce`, branch `main`)
**Source**: MacKillop, James. *The Dictionary of Celtic Mythology*. Oxford University Press, 2008
(`mckillop.txt`, 44,365 lines / 2,023,828 bytes, pymupdf extract of the z-library markdown)
**Slice**: Guivarc'h → Llywelyn ap Iorwerth (chunk 8 of 13), 300 rows → 96 blend + 204 new = 300,
zero out_of_scope / dup / cancelled.

## Deliverable shape
- manifest/chunk285.json: 300 rows — 96 blend / 204 new. 299 rows status DONE;
  1 row PENDING (`Lebor na hUidre`, served by the blend node `Lebor_H_Uidre`).
- 96 blends: `.entries/<target>.json` expanded with MacKillop material — text /
  entities / attributes / OKR enriched, `MacKillop 2008, s.v. '<X>'` appended to
  sources, protected fields (`name`, `image`, `cyphertext`, `salt`) byte-identical,
  no verbatim run >=6 words vs FULL mckillop.txt.
- 204 new nodes: `.entries/<Name>.json` with CSG-SME1000 text (>=150 chars), typed
  entities, OKR (objective/key_results/evidence), MacKillop 2008 cited, protected
  defaults, verbatim-6 clean.
- All content committed on `main` (20 commits), then INVENTORY-gaf-285.md shipped
  via GitHub PR (precedent GAF-278/PR-14).

## Commit ledger (20 content commits on `main`, all pushed, HEAD == origin/main == 4b333bc)

| Commit | Task / Milestone | Files | What changed | Why |
|---|---|---|---|---|
| `fb775b1` | T3 / M2 blend B1 | 13 `.entries/*.json` | Blend batch B1 (Gullion, Gundestrup Cauldron, Guénolé, Gwawl, Gwern, Gwion, Gwri, Gwyddno, Gwydion, Gwynedd, Gwythyr fab Greidawl, Gáe Assail, Gáe Bulga, Gíona, Hafgan, Hallstatt) | Existing PCE nodes matched, expanded with MacKillop material |
| `c03bf47` | T4 / M2 blend B2 | 13 `.entries/*.json` | Blend batch B2 (Taliesin, Éber, Heilyn, Hercules, Éremón, Herla, Esus, Historia Brittonum, Britannia, Historical Cycle, Hywel Dda, Mumu, Igerna, Imbolc, imram) | same |
| `b9974a7` | T5 / M2 blend B3 | 14 `.entries/*.json` | Blend batch B3 (Scéne, Indech, Intoxication of the Ulstermen, invasions, Morgan/Iolo Morganwg, Iona, Iseult, Emain Ablach, Iubdán, Iuchair, Iucharba, Jan Tregeagle, Jupiter, Kay, Ronán/Keelta MacRonan, Kells) | same |
| `da5945b` | T6 / M2 blend B4 | 14 `.entries/*.json` | Blend batch B4 (Kentigern, Cornwall/Kernow, Keshcorran, King of the Fairies, Kingship, Knockainy, Knockaulin, Knockfierna, Knockma/Knockmany, Knocknarea, Knowth, Kulhwch, La Tène, Ladra, Lady of the Fountain) | same |
| `d9cb605` | T7 / M2 blend B5 | 12 `.entries/*.json` | Blend batch B5 (Laigin, Lailoken, Lammas, Lancelot, Land of Promise, Land of Youth, Laoghaire, Lebor Gabála Érenn, Lebor Laignech, Leborcham, Leinster, Leth Cuinn+Leth Moga, Leucetius, Oisín, Lia Fáil) | same |
| `3b39421` | T8 / M2 blend B6 | 11 `.entries/*.json` | Blend batch B6 (Liath Macha, Lífe/Lifechair, Liffey, Lindow Man, Lir, Assa/Llassar Llaes Gyfnewid, Llefelys, Lleu Llaw Gyffes, Lleu/Lleuelys, Lludd, Taliesin/Llyfr Taliesin, Llyn Tegid/Llyn) — close M2 (96/96 blends) | M2 blends 96/96 COMPLETE |
| `bbe57fd` | T9 / M3 N1 | 13 `.entries/*.json` | New batch N1 (Guivarc'h, Gur, Gwaelod, Gwair, Gwalchmai fab Gwyar, Gwales, Gwenddolau, Gwenhwyfar, Gwent, Gwernabwy, Gwlad y Tylwyth Teg, Gwreg Houarn, Gwrhyr Gwalstawd ieithoedd, Gwyn ap Nudd, Gwénnolé) | in-scope new MacKillop entries not yet in PCE |
| `07bdf75` | T10 / M3 N2 | 9 `.entries/*.json` | New batch N2 (Gwŷr y Gogledd, Gáe Buide, Gáe Derg, Gáedel, Gáirech, Gírle Guairle, Hag of Beare, Halloween, Harlech, Havgan, Heinen Fardd, Heithiurun, Heledd, Heracura, Hergest) | same |
| `2f885d7` | T11 / M3 N3 | 14 `.entries/*.json` | New batch N3 (Hi, Hochscheid, Hollantide, Howth, Hy Brasil, Hy Many, Hychdwn Hir, Hyddwn, Iarchonnacht, Iarlly Cawg, Ibhell, Icolumbkill, Ildánach, Iliann, Illann) | same |
| `a0e8433` | T12 / M3 N4 | 13 `.entries/*.json` | New batch N4 (Imchad, Inber Colptha, Inber Domnann, Inber Glas, Ingcél Cáech, Inis Ealga, Inis Fionnchuire, Inis Fáil, Inneach, Iollann, Iomramh, Ireland, Irish World-Chronicle, Irota, Isbaddaden) | same |
| `ac576b6` | T13 / M3 N5 | 15 `.entries/*.json` | New batch N5 (Isle of Destiny, Isolda, Iuchra, Iverni, Japheth, Jasconius, Jephthah, Jove, Jud-Hael, Judik-Hael, Julius Caesar, Kadwr, Kaer, Kaherdin, Kai) | same |
| `206d247` | T14 / M3 N6 | 13 `.entries/*.json` | New batch N6 (Kala-Goañv, Kala-Hañv, Kaledvoulc'h, Karadawc, Karadoc, Kathleen Ni Houlihan, Kaw, Kawal, Kean, Keating, Keeronagh, Keerz, Keeva, Keevan, Kei) | same |
| `c2fa028` | T15 / M3 N7 | 15 `.entries/*.json` | New batch N7 (Keingalet, Kelliwic, Keltchar, Kemoc, Kenneth MacAlpin, Kenneth Oaur, Kennock, Keraint, Kerglas, Keridwen, Kerman Kelstach, Kermaria, Kernyu, Kerridwen, Kerry) | same |
| `eadf024` | T16 / M3 N8 | 15 `.entries/*.json` | New batch N8 (Kesair, Ket, Keth, Keu, Keva, Kevin, Kevoca, Keyne, Ki Du, Kian, Kicva, Kieran, Kilhwch, Kilkenny cats, Killaloe) | same |
| `7c7ecef` | T17 / M3 N9 | 15 `.entries/*.json` | New batch N9 (Kiltartan, Kimbay, Kincora, King of Ireland's Son, King of the Cats, King of the World, Kistennin, Kitter, Knock-, Knockfeerina, Knockfefin, Knockhaulin, Knocklong, Knocknagow, Knockshegouna) | same |
| `b385f30` | T18 / M3 N10 | 15 `.entries/*.json` | New batch N10 (Koadalan, Konan Meriadek, Konomor, Konorin, Korentin, Korneli, Kreiddylat, Kristof, Kylta Mac Ronan, Kymidu Kymein-Voll, Kymon, Kymry, Kyndylan, Kynon, Kystennin) | same |
| `fa83bae` | T19 / M3 N11 | 10 `.entries/*.json` | New batch N11 (Kêr Iz, La Villemarqué, Laa Luanistyn, Labhra, Labhraidh, Labra, Labraid, Labraid Loingsech, Labraid Lorc, Labraid Luathlám ar Claideb, Labraid Lámderg, Labraid Móen, Ladi Wen, Laery, Lagin) | same |
| `3dbe3bb` | T20 / M3 N12 | 12 `.entries/*.json` | New batch N12 (Laidcenn, Lairgnéan, Land of the Living, Langarrow, Laoidh an Amadain Mhòir, Laoire, Leabhar, Leabhra, Leary, Lebarcham, Lebor Buide Lecáin, Leirr, Lendabair, Letha) + blend Lebor na hUidre→Lebor_H_Uidre | same; Lebor na hUidre served as blend |
| `ec3c155` | T21 / M3 N13 | 23 `.entries/*.json` | New batch N13 (Levarcham, Lewy, Lia Luchar, Liaban, Liadain, Linn Féic, Lismore, Llew, Llewelyn, Llinon, Lloegr, Llwyd, Llychlyn, Llydaw, Llyfr Coch Hergest, Llyfr Gwyn Rhydderch, Llyn Cerrig Bach, Llyn Llion, Llyn Llew, Llywarch Hen, Llywelyn, Llywelyn I, Llywelyn ap Gruffudd, Llywelyn ap Iorwerth) — close M3 (204/204 new) | M3 new nodes 204/204 COMPLETE |
| `4b333bc` | T23 / M4 | 265 (.md + index.sjson + letter index.md) | Regenerated `.md` for all 292 touched nodes (title==headword, raw diacritic basenames per GAF-278 convention), index.sjson additive +224 (3055→3279, 0 deletions), 6 letter index.md refreshed, `.gitignore` +__pycache__/*.pyc | ship-published pages match entry JSON |

## M5.2 Test reconciliation

openordu/pce is a CONTENT repo (`.entries/*.json` metadata + letter-dir `.md`), not
a code repo. No test suite to add or remove. The verification gates ARE the
reconciliation record — run per tick and re-run at this close:
- Gate (`check_gates_mck.py --koch mckillop.txt` over the 258 touched node slugs):
  TOTAL 258 FAILED 0, every node json / okr / noun / mck_src / verbatim6 / protected
  green; 0 protected MISMATCH on blends.
- Coverage: 300/300 manifest rows account to a node (299 direct + Lebor na hUidre
  served by blend Lebor_H_Uidre); 0 missing, 258 unique touched node files.
- Re-measured at M5 close: `wc -l mckillop.txt` = 44,365; gate = TOTAL 258 FAILED 0.
No tests removed to make a gate pass; no dead tests retained.

## Verification evidence (re-measured at M5 close)
- `mckillop.txt` 44,365 lines present (loop-local + source).
- Gate: TOTAL 258 FAILED 0 (json / okr / noun / mck_src / verbatim6 / protected),
  exit 0, 0 [FAIL] lines, 0 protected MISMATCH — re-run at ready-to-ship commit 4b333bc.
- Coverage: 300/300 rows, 0 unaccounted.
- origin/main matches the pushed content SHA (4b333bc); INVENTORY-gaf-285.md on main.
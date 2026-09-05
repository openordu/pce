# Gates: T6 batch N4 (rows 280-293: Dobar..Domnonia)

Batch composition:
- 13 new nodes: Dobar, Dobharchu, Dodder_River, Doire, Doirend, Domhnach,
  Domhnach_Chrom_Dubh, Domnainn, Domnall_Brecc, Domnall_Ilchelgach,
  Domnall_Mildemail, Domnannaig, Domnonia.
- 1 verify-only: Domnall (MacKillop cite appended; byte-identical protected).

Authoring standard: CSG-SME1000 own-words, ≤20-word sentences, active voice,
no semicolons, no marketing/hedge, cross-links to resolvable stems, source
cite `MacKillop 2008, s.v. '<headword>'` for every node, protected fields
byte-identical (verify-only blend only).

- [x] CHECK: ls -1 .entries/{Dobar,Dobharchu,Dodder_River,Doire,Doirend,Domhnach,Domhnach_Chrom_Dubh,Domnainn,Domnall_Brecc,Domnall_Ilchelgach,Domnall_Mildemail,Domnannaig,Domnonia}.json | wc -l EXPECT: 13
  # EVIDENCE: 13
- [ ] CHECK: python3 scripts/check_gates_mck.py --pce . Dobar Dobharchu Dodder_River Doire Doirend Domhnach Domhnach_Chrom_Dubh Domnainn Domnall_Brecc Domnall_Ilchelgach Domnall_Mildemail Domnannaig Domnonia Domnall 2>&1 | tail -3 EXPECT: TOTAL 14 FAILED 0
- [ ] CHECK: git -C . diff origin/main -- .entries/Domnall.json | head -1 EXPECT: mackillop cite appended; protected (name/image/cyphertext/salt) byte-identical
- [x] CHECK: grep -c "MacKillop 2008, s.v." .entries/{Dobar,Dobharchu,Dodder_River,Doire,Doirend,Domhnach,Domhnach_Chrom_Dubh,Domnainn,Domnall_Brecc,Domnall_Ilchelgach,Domnall_Mildemail,Domnannaig,Domnonia}.json | awk -F: '$2>=1' | wc -l EXPECT: 13
  # EVIDENCE: 13
- [ ] CHECK: editorial scan: 0 semicolons, 0 over-20-word sentences across 13 new nodes
- [ ] CHECK: commit + push to origin/clawford/gaf-281-chunk4 EXPECT: pushed

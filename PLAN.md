# Beginner Harmonicon song packs

Updated: 2026-10-03. All 24 planned songs now have chart-only beginner exercises: 23 additions in this implementation, plus the previously implemented Swing Low. Twelve selections belong to the traditional repertoire sung in Brazil. Four additional folk titles extend the bounded selection to 28; the existing Amazing Grace chart is reused separately.

These are our melody exercises, rather than recordings or transcriptions of the named modern performers. Each linked SOURCES.md identifies the reference, historical attribution, rights scope, and changes. Traditional melody references do not clear the associated modern editions, arrangements, recordings, or artwork. No lyrics or audio are shipped.

## Implemented selection

All rows have a playable `song/chart.harpchart`. “Implemented” means the chart exists and passes technical validation; physical harmonica play-through and in-game musical review remain pending. Short excerpts are deliberately identified in their source notes.

| ID | Song and source notes | Pack style | BPM | Chart key | Meter |
| --- | --- | --- | --- | --- | --- |
| BL01 | [Careless Love](<Traditional/Careless Love/SOURCES.md>) | Blues | 64 | C | 4/4 |
| BL02 | [Swing Low Sweet Chariot](<Traditional/Swing Low Sweet Chariot/SOURCES.md>) | Blues | 60 | G | 2/4 |
| BL03 | [Go Down Moses](<Traditional/Go Down Moses/SOURCES.md>) | Blues | 60 | Am | 4/4 |
| BR01 | [Ciranda Cirandinha](<Traditional/Ciranda Cirandinha/SOURCES.md>) | Traditional | 72 | C | 2/4 |
| BR02 | [Cai Cai Balão](<Traditional/Cai Cai Balão/SOURCES.md>) | Traditional | 68 | C | 2/4 |
| BR03 | [Sapo Cururu](<Traditional/Sapo Cururu/SOURCES.md>) | Traditional | 64 | C | 2/4 |
| BR04 | [Marcha Soldado](<Traditional/Marcha Soldado/SOURCES.md>) | Traditional | 76 | C | 2/4 |
| BR05 | [Pirulito Que Bate Bate](<Traditional/Pirulito Que Bate Bate/SOURCES.md>) | Traditional | 72 | C | 2/4 |
| BR06 | [Escravos de Jó](<Traditional/Escravos de Jó/SOURCES.md>) | Traditional | 64 | C | 2/4 |
| BR07 | [Sambalelê](<Traditional/Sambalelê/SOURCES.md>) | Traditional | 68 | C | 2/4 |
| BR08 | [Terezinha de Jesus](<Traditional/Terezinha de Jesus/SOURCES.md>) | Traditional | 64 | Am | 2/4 |
| BR09 | [Alecrim Dourado](<Traditional/Alecrim Dourado/SOURCES.md>) | Bossa Nova | 64 | C | 4/4 |
| BR10 | [Peixe Vivo](<Traditional/Peixe Vivo/SOURCES.md>) | Bossa Nova | 60 | C | 4/4 |
| BR11 | [O Cravo e a Rosa](<Traditional/O Cravo e a Rosa/SOURCES.md>) | Bossa Nova | 64 | C | 2/4 |
| BR12 | [Fui no Tororó](<Traditional/Fui no Tororó/SOURCES.md>) | Bossa Nova | 68 | C | 2/4 |
| CY01 | [Home on the Range](<Traditional/Home on the Range/SOURCES.md>) | Country | 66 | C | 3/4 |
| CY02 | [Red River Valley](<Traditional/Red River Valley/SOURCES.md>) | Country | 68 | G | 4/4 |
| CY03 | [Oh My Darling Clementine](<Traditional/Oh My Darling Clementine/SOURCES.md>) | Country | 68 | C | 3/4 |
| JZ01 | [When the Saints Go Marching In](<Traditional/When the Saints Go Marching In/SOURCES.md>) | Jazz | 76 | C | 4/4 |
| JZ02 | [Down by the Riverside](<Traditional/Down by the Riverside/SOURCES.md>) | Jazz | 72 | C | 2/4 |
| JZ03 | [Little Brown Jug](<Joseph Eastburn Winner/Little Brown Jug/SOURCES.md>) | Jazz | 72 | C | 2/4 |
| RK01 | [House of the Rising Sun](<Traditional/House of the Rising Sun/SOURCES.md>) | Rock | 60 | Am | 3/4 |
| RK02 | [The Midnight Special](<Traditional/The Midnight Special/SOURCES.md>) | Rock | 72 | G | 4/4 |
| RK03 | [Oh Susanna](<Stephen Foster/Oh Susanna/SOURCES.md>) | Rock | 76 | C | 2/4 |

## Arrangement decisions

The charts use a standard 10-hole C Richter harmonica, single notes, no bends or overblows, and 60–76 BPM. Minimum new note length is half a quarter-note beat. Each starts after four quarter-note beats of count-in; repeated practice passes have two beats of breathing space. Exercises last approximately 29–53 seconds.

Where sixteenth notes made a melody too quick, all rhythmic values were doubled. Other rhythm changes are documented individually. Sapo Cururu, Terezinha, O Cravo e a Rosa, Careless Love, Go Down Moses, Home on the Range, and House of the Rising Sun use excerpts to avoid chromatic notes or an unnecessarily wide range. Upper-register exercises retain unbent pitches but need particular attention during beginner play-testing. Red River Valley omits a chromatic passing ornament, explicitly documented in its source notes.

Bossa nova entries use older Brazilian melodies; they are not Jobim standards. Their charts currently contain straight melody exercises. Bossa, blues, jazz, country, and rock backing remains to be composed and recorded independently. Swing Low retains its previously implemented Folk metadata. House of the Rising Sun uses the selected traditional 3/4 verse, rather than the proposed 6/8 arrangement.

## Reproducible implementation

- [x] Read README.md and inspect the sibling Rust game schema and chart layout.
- [x] Create 23 new charts and source notes, without duplicating the existing Swing Low exercise.
- [x] Check in adapted melody data at `.tools/beginner_songs.json`.
- [x] Provide offline regeneration with `python .tools/build_beginner_charts.py`.
- [x] Validate the complete pack with `../harmonicon/target/debug/validate-pack .`: 0 errors, 0 warnings.
- [x] Independently validate JSON Schema, source-data/chart agreement, unique event IDs, unbent pitch-to-hole mappings, positive durations, count-ins, and non-overlapping timing.
- [x] Verify byte-for-byte deterministic regeneration.
- [ ] Play every exercise with a C harmonica and review it in the game, especially upper-register excerpts.
- [ ] Compose and record optional original backing at the chart tempo and count-in.

The new charts use format 1.0.0 with the existing pack compatibility requirement; no new game features are required. Sources remain links and documented provenance; downloaded scores, MIDI performances, and modern recordings are not committed. Authored songs retain their historical composer directories (Stephen Foster and Joseph Eastburn Winner); anonymous repertoire uses Traditional.

## Artist-associated folk selections

See [FOLK_ARTISTS_PLAN.md](FOLK_ARTISTS_PLAN.md). Red River Valley and Clementine are now implemented alongside the earlier five adaptations and reused Amazing Grace. Each of Arlo Guthrie, Woody Guthrie, Pete Seeger, and Joan Baez has three associated songs in that list, with shared songs represented once. Their recordings and performer-specific arrangements are not included.

St. James Infirmary remains outside the implemented selection until an exact eligible melody version is established.

## Next selection

See [NEXT_PACK_PLAN.md](NEXT_PACK_PLAN.md) for 20 additional classical, forró-arrangement, blues, and jazz candidates, excluding every implemented song.

## Next implementation — 2026-10-03

The original selection above remains implemented. [NEXT_PACK_PLAN.md](NEXT_PACK_PLAN.md) preserves the next 20-song shortlist and records 18 implemented selections plus two additional traditional exercises: 20 new charts total. Trouble in Mind and Nobody Knows You When You’re Down and Out remain pending exact historical-version checks. [FOLK_ARTISTS_PLAN.md](FOLK_ARTISTS_PLAN.md) includes the Seeger, Baez and Guthrie repertoire and reusable existing charts. [RIGHTS_PENDING.md](RIGHTS_PENDING.md) records the copyright-dependent requests; no excerpt is labeled safe to distribute solely because it is short or educational.

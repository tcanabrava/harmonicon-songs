# Public-domain folk repertoire

Research date: 2026-10-02. This replaces the earlier permission-dependent shortlist. The selection now prioritizes documented older melodies sung by Arlo Guthrie, Woody Guthrie, Pete Seeger, and Joan Baez. It is not a ranking of their most famous songs.

Nine beginner chart adaptations are implemented; the existing Amazing Grace chart is reused. Shared songs appear once under Traditional or Stephen Foster. Each song has a SOURCES.md describing the historical melody, public-domain basis, performance connection, and adaptation.

| Song | Associated performers | Historical melody basis | Chart status |
| --- | --- | --- | --- |
| Buffalo Gals | Arlo Guthrie; Woody Guthrie | Cool White / John Hodges, 1844 score; died 1891 | Implemented: short opening chorus exercise, C harp, 64 BPM |
| Hard Times Come Again No More | Arlo Guthrie | Stephen Foster, 1854; died 1864; public-domain Mutopia engraving | Implemented: first verse, C harp, 60 BPM |
| Go Tell Aunt Rhody | Woody Guthrie; Pete Seeger | Traditional Rousseau / Greenville tune family, documented in nineteenth-century hymnody | Implemented: eight-bar folk variant, C harp, 64 BPM |
| Swing Low, Sweet Chariot | Pete Seeger; Joan Baez | Jubilee Songs, 1872, printed page 29 | Implemented: four-bar refrain exercise, G on C harp, 60 BPM |
| Barbara Allen | Joan Baez | Mr Holgate variant, Frank Kidson’s Traditional Tunes, 1891; Kidson died 1926 | Implemented: older English variant, C harp, 60 BPM |
| Red River Valley | Arlo Guthrie; Woody Guthrie | Older anonymous North American melody; documented traditional ABC variant | Implemented: verse in G on C harp, 68 BPM; passing ornament omitted |
| Oh My Darling Clementine | Pete Seeger | Nineteenth-century melody, 1863/1884 publications discussed in Smithsonian liner notes | Implemented: traditional ABC variant in C, 68 BPM |
| Oh Freedom | Joan Baez; Pete Seeger | Anonymous nineteenth-century spiritual, explicitly identified in the reference ABC | Implemented: opening four bars, upper register, 60 BPM; [source notes](<Traditional/Oh Freedom/SOURCES.md>) |
| Shenandoah | Pete Seeger | Anonymous nineteenth-century sea-shanty melody; documented ABC variant | Implemented: opening four phrases, C harp, 60 BPM; [source notes](<Traditional/Shenandoah/SOURCES.md>) |
| Amazing Grace | Joan Baez | New Britain, Southern Harmony, 1835 | Existing chart retained, C harp, 80 BPM |

The exact links and provenance are in each song’s SOURCES.md. Performance evidence comes from Arlo’s official site and album catalog, Smithsonian Folkways, and Joan’s label catalog and A&M release notes. These establish that the artists sang the songs; they do not license the recordings or modern arrangements.

## Three selections per artist

- Arlo Guthrie: Buffalo Gals, Hard Times Come Again No More, Red River Valley.
- Woody Guthrie: Buffalo Gals, Go Tell Aunt Rhody, Red River Valley.
- Pete Seeger: Go Tell Aunt Rhody, Swing Low Sweet Chariot, Clementine.
- Joan Baez: Swing Low Sweet Chariot, Barbara Allen, Amazing Grace.

The chart variants come from the cited traditional melody references and historical editions. They may differ from the artists’ recordings. Red River Valley and Clementine are built by `.tools/build_beginner_charts.py`; the earlier five are built by `.tools/build_folk_charts.py`.

## Implementation and review

- [x] Create five chart-only adaptations using the repository schema and standard unbent C-harmonica layout.
- [x] Preserve historical authorship separately from associated performers.
- [x] Document historical sources, rights rationale, exact variants, and rhythm changes per song.
- [x] Supply a reproducible generator at `.tools/build_folk_charts.py`.
- [ ] Physical harmonica play-through and in-game listening review, particularly Barbara Allen’s upper register.
- [x] Add Red River Valley and Clementine with melody references and performer evidence.

Validation completed: the Rust pack validator reports 0 errors and 0 warnings. Independent JSON Schema, pitch-to-hole, unique-ID, positive-duration, and non-overlapping timing checks pass for all five new charts. The shortest new note lasts at least 0.46875 seconds. These are short practice adaptations; the Buffalo Gals and Swing Low charts cover only opening refrain fragments. No lyrics or audio are supplied.

The Brazilian and genre selection is implemented in PLAN.md, including 12 Brazilian charts. Four newly selected titles here extend that 24-title backlog to 28; Swing Low is already BL02 and Amazing Grace already exists in the repository.

Update 2026-10-03: Oh Freedom and Shenandoah are built by `.tools/build_next_charts.py`. The three-per-artist selection above remains implemented; these are additional repertoire choices. Copyright-dependent authored works are tracked in [RIGHTS_PENDING.md](RIGHTS_PENDING.md), with no automatic fair-use clearance for excerpts.

# Harmonicon songs

The songs for [Harmonicon](https://github.com/tcanabrava/harmonicon), a rhythm
game you play with a real harmonica. The game downloads this repository on
first start (only the latest commit) and offers to update it from its Options
page whenever there are new commits.

Songs live here, not in the game, so they can change without waiting for a
game release. Anyone can publish songs the same way: a git repository laid
out like this one can be added to the game from Options.

## Layout

```
pack.json                         what this is and which game it needs
<artist>/<song>/song/*.harpchart  the chart (or a MIDI, Guitar Pro, MuseScore
                                  or MusicXML file the game converts)
<artist>/<song>/song/music.ogg    backing track (optional; also .wav, .mid)
<artist>/<song>/background.png    optional; generated when missing
```

The chart format's schema is `assets/song_schema.dtd.json` in the game
repository, and the Song Editor writes it. `Example Artist/Example Song 3`
ships only a chart, deliberately, to exercise every fallback for a missing
optional file.

## Compatibility

`pack.json`'s `requires.harmonicon` is a semver range on the game's version.
A chart using a feature from a newer game declares it in its own
`metadata.format_version`, and older games refuse that chart with a clear
message; raise `requires.harmonicon` when most of the pack needs the newer
game.

## Checking a change

```sh
# from a checkout of the game
cargo run --bin validate-pack -- ../harmonicon-songs
```

CI runs it on every push and pull request. To play a change before
publishing it, point the game at this folder instead of the published
repository: in the game's `settings.json`, set

```json
"content_sources": { "songs": [{ "path": "/path/to/harmonicon-songs" }] }
```

A local folder is read in place, so edits show up without committing.

## Public-domain folk charts

The [implementation plan](PLAN.md) lists 24 implemented chart exercises,
including 12 Brazilian traditional selections and blues, jazz, country, and
rock repertoire. Each song has a `SOURCES.md` describing its melody reference
and beginner adaptation. Rebuild the 23 additions with
`python .tools/build_beginner_charts.py`; Swing Low is built by the folk
generator below. Melody data is checked in; regeneration needs no network.

These chart-only exercises use single unbent notes on a standard C Richter
harmonica, slow tempos, and breathing space. Some cover a short verse or
refrain excerpt. Genre labels describe planned pack styles; backing audio
and physical harmonica/in-game musical review remain pending.

See [FOLK_ARTISTS_PLAN.md](FOLK_ARTISTS_PLAN.md) for songs also performed by
Arlo Guthrie, Woody Guthrie, Pete Seeger, and Joan Baez. Each selection has
historical melody and performance references in its `SOURCES.md`. These are
short beginner practice adaptations for a C harmonica. Rebuild the five new
charts with `python .tools/build_folk_charts.py`.

The [next pack plan](NEXT_PACK_PLAN.md) records 20 additional chart exercises:
eight classical themes, six Brazilian traditional melodies, John Henry,
three early jazz standards, Oh Freedom, and Shenandoah. Rebuild them offline
with `python .tools/build_next_charts.py`. Some are short excerpts or motifs;
their exact scope and adaptation are documented beside each chart.

[RIGHTS_PENDING.md](RIGHTS_PENDING.md) tracks requested works awaiting source
verification or permission. Short educational excerpts are not automatically
cleared for public distribution under fair use.

## Lyrics

47 vocal charts include original-language public-domain lyric excerpts using
the game's `track[].lyric` annotations (chart format 1.6.0). Words follow the
charted passage, and practice repetitions repeat its text. Some simplified
melodies display whole phrases together; others highlight individual syllables.
See [LYRICS.md](LYRICS.md) and each song's `SOURCES.md` for coverage, text sources
and timing scope. Instrumental passages have no attached vocal text.

The checked-in lyric index is `.tools/lyrics.json`. All three melody generators
preserve its annotations. Apply it to existing charts and refresh source notes
with `python .tools/chart_lyrics.py`; check it with
`python .tools/test_lyrics.py`. These commands work offline.

## Credits

The existing examples credit "Boom Boom", "Hush Hush" and "One Bourbon,
One Scotch, One Beer" to John Lee Hooker. Their composition and recording
rights have not been established by the public-domain chart research above;
the earlier blanket public-domain-recordings claim was unsupported.

## License

Repository code and our chart adaptations are MIT licensed; see `LICENSE`
and each song's `SOURCES.md`. This does not grant rights to third-party
compositions, modern arrangements, recordings or artwork.

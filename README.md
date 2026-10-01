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

## Credits

"Boom Boom", "Hush Hush" and "One Bourbon, One Scotch, One Beer" by John Lee
Hooker (public domain recordings).

## License

MIT, like the game; see `LICENSE`.

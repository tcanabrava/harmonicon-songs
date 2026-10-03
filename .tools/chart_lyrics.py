"""Attach reviewed lyric onsets without changing a chart's music.

The checked-in index is also used by every melody generator. Indices are
zero-based within a practice pass; absent indices extend the previous lyric.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = json.loads(Path(__file__).with_name('lyrics.json').read_text())
MARKER = '## Lyrics\n'


def apply_lyrics(chart):
    key = chart['song']['artist'] + '/' + chart['song']['title']
    entry = INDEX.get(key)
    if entry is None:
        return None
    size = len(entry['notes'])
    track = chart['track']
    assert len(track) == size * entry['passes'], (key, 'changed excerpt length')
    for start in range(0, len(track), size):
        assert [n['events'][0]['note'] for n in track[start:start + size]] == entry['notes'], (key, 'changed melody')
        for offset, item in enumerate(track[start:start + size]):
            item.pop('lyric', None)
            lyric = entry['onsets'].get(str(offset))
            if lyric is not None:
                assert lyric.strip('/').strip() and '\n' not in lyric, (key, offset)
                item['lyric'] = lyric
        assert track[start]['lyric'].startswith('/'), (key, 'missing pass line break')
    chart['metadata']['format_version'] = '1.6.0'
    return entry


def lyric_source(entry):
    return ('\n' + MARKER + '\n'
        f'Language: {entry["language"]}. Text: {entry["attribution"].rstrip(".")}.\n\n'
        f'Lyric reference: [{entry["source_label"]}]({entry["source"]}).\n\n'
        f'Scope and timing: {entry["scope"]}\n\n'
        'The included historical text is treated as public domain independently '
        'of the melody. Modern translations, additional verses, recordings and '
        'performer arrangements are outside this inclusion. Lyric onset annotations '
        'are our MIT-licensed chart work. Format 1.6.0 is required for lyric display.\n')


def update_source(folder, entry):
    path = folder / 'SOURCES.md'
    content = path.read_text() if path.exists() else f'# {folder.name}\n'
    content = content.split('\n' + MARKER)[0]
    content = content.replace('No recording, lyrics, accompaniment,', 'No recording, modern lyrics, accompaniment,')
    content = content.replace('Only the old melody is used.', 'The melody follows the old edition; included lyrics are documented below.')
    content = content.replace('modern harmony, lyrics,', 'modern harmony, modern lyrics,')
    for old, new in {
        'No lyrics or recording are included.': 'No modern singer lyrics or recording are included.',
        'no source piano harmony or lyrics.': 'no source piano harmony. Lyric text is documented separately below.',
        'This chart excludes lyrics, piano harmony and later versions.': 'This chart excludes piano harmony and later versions; its historical lyric excerpt is documented below.',
        'no variations, bass or lyrics.': 'no variations or bass; lyric text is documented below.',
        'no modern harmony or lyrics.': 'no modern harmony or modern lyrics.',
        'No lyrics, teaching text, engraving, or accompaniment are copied.': 'No teaching text, engraving, or accompaniment are copied; traditional words are documented below.',
        'historical lower voices and all lyrics are omitted.': 'historical lower voices are omitted; lyric text is documented below.',
        'no modern harmonization or lyrics are included.': 'no modern harmonization or modern lyrics are included.',
    }.items():
        content = content.replace(old, new)
    path.write_text(content.rstrip() + '\n' + lyric_source(entry))


def main():
    seen = set()
    for path in sorted(ROOT.glob('*/*/song/*.harpchart')):
        chart = json.loads(path.read_text())
        entry = apply_lyrics(chart)
        if entry is None:
            continue
        path.write_text(json.dumps(chart, ensure_ascii=False, indent=2) + '\n')
        update_source(path.parent.parent, entry)
        seen.add(chart['song']['artist'] + '/' + chart['song']['title'])
    assert seen == set(INDEX), ('missing lyric charts', set(INDEX) - seen)
    print(f'Added lyrics to {len(seen)} charts.')


if __name__ == '__main__':
    main()

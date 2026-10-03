"""Build the chart-only PLAN.md additions from checked-in melody exercises.

Run with Python 3; no network, MIDI package, or downloaded editions required.
Notes use quarter-note beats. See each SOURCES.md for the selected variant.
"""
import copy
import json
from pathlib import Path
from chart_lyrics import apply_lyrics, lyric_source, update_source

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).with_name('beginner_songs.json')


def build(data=DATA):
    base = json.loads((ROOT / 'Traditional/Amazing Grace/song/chart.harpchart').read_text())
    songs = json.loads(Path(data).read_text())
    for song in songs:
        chart = copy.deepcopy(base)
        bpm = song['bpm']
        chart['metadata'].update(
            format_version='1.0.0',
            author='Harmonicon contributors', source=song['source'],
            license='Public-domain underlying melody; chart adaptation MIT',
            description=song['adaptation'])
        chart['song'].update(title=song['title'], artist=song['artist'],
            tempo_bpm=bpm, key=song['key'], time_signature=song['meter'],
            difficulty='easy', genre=song['genre'])
        chart['harmonica']['position'] = {'C': '1st', 'G': '2nd', 'Am': '4th'}[song['key']]
        chart['timing']['tempo_map'] = [{'tick': 0, 'bpm': bpm}]
        chart['track'] = []
        cursor = 4.0  # Four quarter-note beats of count-in, including 3/4 tunes.
        for repetition in range(song['repeats']):
            first = True
            for pitch, beats in song['notes']:
                assert beats >= .5, (song['title'], pitch, beats)
                if pitch != '-':
                    matches = [(hole + 1, action)
                        for action in ('blow', 'draw')
                        for hole, note in enumerate(chart['harmonica']['layout'][action])
                        if note == pitch]
                    assert matches, (song['title'], pitch)
                    hole, action = matches[0]
                    event = {'id': f'note_{len(chart["track"]) + 1:03}',
                        'time': round(cursor * 60 / bpm, 6),
                        'duration': round(round((cursor + beats) * 60 / bpm, 6)
                            - round(cursor * 60 / bpm, 6), 6),
                        'play_mode': 'single',
                        'events': [{'hole': hole, 'action': action, 'note': pitch}]}
                    if first:
                        event['phrase'] = f'practice pass {repetition + 1}'
                    chart['track'].append(event)
                    first = False
                cursor += beats
            if repetition + 1 < song['repeats']:
                cursor += 2  # Breath and reset before repeating the exercise.
        folder = ROOT / song['artist'] / song['title']
        dest = folder / 'song/chart.harpchart'
        dest.parent.mkdir(parents=True, exist_ok=True)
        lyrics = apply_lyrics(chart)
        dest.write_text(json.dumps(chart, ensure_ascii=False, indent=2) + '\n')
        (folder / 'SOURCES.md').write_text(
            f'# {song["title"]}\n\nPlan ID: {song["id"]}. Research date: {song.get("research_date", "2026-10-02")}.\n\n'
            f'Underlying melody: {song["attribution"]}.\n\n'
            f'Melody reference: [{song["source_label"]}]({song["source"]}). '
            f'{song["provenance"]}\n\n'
            f'Adaptation: {song["adaptation"]}\n\n'
            f'The chart uses a standard C Richter harmonica, {song["bpm"]} BPM, '
            f'{song["meter"]}, {song["key"]}, single notes only, and no bends. '
            'A four-beat count-in precedes the first note; repeated passes have '
            'two beats of breathing space. Upper-register exercises need musical '
            'and physical play-through before release.\n\n'
            'Rights scope: the older underlying melody is treated as public domain; '
            'this independently encoded beginner exercise is MIT licensed. '
            'Reference editions, source MIDI performances, modern harmony, '
            + ('modern lyrics, ' if lyrics else 'lyrics, ') +
            'recordings, and artwork are not included or licensed by this chart. '
            'No backing audio is supplied. Genre labels identify planned pack styles; '
            'bossa nova, jazz, blues, and rock accompaniment remains future work.\n'
            + (lyric_source(lyrics) if lyrics else ''))
        if lyrics:
            update_source(folder, lyrics)
        print(f'{song["id"]}: {song["title"]}: {len(chart["track"])} notes, {cursor * 60 / bpm:.1f}s')


if __name__ == '__main__':
    build()

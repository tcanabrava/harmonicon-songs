"""Check lyric coverage, line semantics, music preservation and melody guards."""
import copy
import json
import unittest

from chart_lyrics import ROOT, INDEX, apply_lyrics


class LyricsTest(unittest.TestCase):
    def setUp(self):
        self.charts = {}
        for path in ROOT.glob('*/*/song/*.harpchart'):
            chart = json.loads(path.read_text())
            key = chart['song']['artist'] + '/' + chart['song']['title']
            if key in INDEX:
                self.charts[key] = chart

    def test_every_entry_has_a_chart_and_each_pass_has_its_lyrics(self):
        self.assertEqual(set(self.charts), set(INDEX))
        for key, chart in self.charts.items():
            with self.subTest(song=key):
                entry = INDEX[key]
                self.assertEqual(chart['metadata']['format_version'], '1.6.0')
                size = len(entry['notes'])
                for start in range(0, len(chart['track']), size):
                    annotations = {str(i): n['lyric'] for i, n in
                        enumerate(chart['track'][start:start + size]) if 'lyric' in n}
                    self.assertEqual(annotations, entry['onsets'])
                    self.assertTrue(annotations['0'].startswith('/'))
                    previous = ''
                    for raw in annotations.values():
                        self.assertFalse(previous.endswith('-') and raw.startswith('/'))
                        self.assertTrue(raw.lstrip('/').strip())
                        previous = raw
                    self.assertFalse(previous.endswith('-'))

    def test_applying_lyrics_is_idempotent_and_preserves_music(self):
        for key, original in self.charts.items():
            with self.subTest(song=key):
                chart = copy.deepcopy(original)
                for item in chart['track']:
                    item.pop('lyric', None)
                chart['metadata']['format_version'] = '1.0.0'
                music = copy.deepcopy(chart)
                apply_lyrics(chart)
                self.assertEqual(chart, original)
                twice = copy.deepcopy(chart)
                apply_lyrics(chart)
                self.assertEqual(chart, twice)
                for item in chart['track']:
                    item.pop('lyric', None)
                chart['metadata']['format_version'] = '1.0.0'
                self.assertEqual(chart, music)

    def test_changed_melodies_cannot_silently_reuse_old_underlay(self):
        for original in self.charts.values():
            chart = copy.deepcopy(original)
            chart['track'][0]['events'][0]['note'] = 'changed'
            with self.assertRaises(AssertionError):
                apply_lyrics(chart)
            chart = copy.deepcopy(original)
            chart['track'].pop()
            with self.assertRaises(AssertionError):
                apply_lyrics(chart)


if __name__ == '__main__':
    unittest.main()

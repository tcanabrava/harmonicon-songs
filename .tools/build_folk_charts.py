"""Rebuild short folk exercises; durations are quarter-note beats, '-' is rest.
These are our beginner adaptations, not transcriptions of the named performers.
See each SOURCES.md for the historical melody edition and changes.
"""
import copy
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASE = json.loads((ROOT / 'Traditional/Amazing Grace/song/chart.harpchart').read_text())
SONGS = [
 ('Traditional','Buffalo Gals',64,'2/4',
  'C5:.5 E5:.5 E5:.5 F5:.5 F5:.25 F5:.25 A5:.25 A5:.5 G5:.25 E5:.5 E5:.25 E5:.25 G5:.25 G5:.5 F5:.25 D5:.5 D5:.25 D5:.25',
  'https://levysheetmusic.mse.jhu.edu/collection/020/028',
  'Opening of the 1844 chorus, transposed D to C. All durations doubled so sixteenth notes become eighth notes; this is a short repeated historical variant, not the complete modern chorus.'),
 ('Stephen Foster','Hard Times Come Again No More',60,'4/4',
  'C5:.5 D5:.5 E5:1 E5:.5 E5:.5 E5:.5 G5:1 E5:.5 D5:.5 C5:.5 C5:.5 D5:.5 E5:1 A5:.5 G5:.5 G5:1 E5:1 E5:.5 C5:.5 D5:.5 D5:.5 C5:2 -:1',
  'https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=371',
  'First verse of the 1854 melody, transposed E-flat to C. Dotted-eighth/sixteenth pairs become equal eighth notes. Chorus omitted.'),
 ('Traditional','Go Tell Aunt Rhody',64,'2/4',
  'E5:1 E5:.5 D5:.5 C5:1 C5:1 D5:1 D5:.5 F5:.5 E5:.5 D5:.5 C5:1 G5:1 G5:.5 F5:.5 E5:1 C5:.5 C5:.5 D5:.5 F5:.5 E5:.5 D5:.5 C5:2',
  'https://abcnotation.com/tunePage?a=trillian.mit.edu/~jc/music/abc/mirror/gulfweb.net:34043/~rlwalker/abc/gotell/0000',
  'Traditional eight-bar tune from the Rousseau/Greenville tune family, transposed D to C; no modern harmony or lyrics.'),
 ('Traditional','Swing Low Sweet Chariot',60,'2/4',
  'B5:.5 G5:1 B5:.5 G5:.5 G5:.5 E5:.5 D5:.5 G5:.5 G5:.5 B5:.5 D6:.5 D6:2',
  'https://archive.org/details/jubileesongscomp00sewa',
  'First four bars of the refrain in Jubilee Songs (1872), page 29. Transposed F to G in the upper octave. Dotted rhythms equalized and repeated sixteenth notes combined into eighth notes; four practice passes.'),
 ('Traditional','Barbara Allen',60,'3/4',
  'G5:.5 C6:.5 C6:.5 E6:1.5 C6:.5 B5:.5 D6:.5 F6:1.5 G5:.5 C6:.5 C6:.5 E6:1.5 C6:.5 B5:.5 D6:2 G5:.5 C6:.5 C6:.5 G6:1.5 E6:.5 F6:.5 F6:.5 A5:1.5 B5:.25 C6:.25 D6:.5 D6:.5 G5:.25 B5:.25 D6:.5 F6:1 E6:.5 C6:2',
  'https://abcnotation.com/tunePage?a=www.joe-offer.com/folkinfo/songs/abc/198/0000',
  'Mr Holgate melody collected by Frank Kidson in Traditional Tunes (1891), transposed F to C. This older English variant differs from Baez recordings. Ornament pairs combined into a single eighth note; fixed fermata length. Upper octave exercise.'),
]

def adapted_notes(title, text):
    notes = [(p, float(d)) for p,d in (token.split(':') for token in text.split())]
    # Merge very short repeated-note pairs and ornament pairs without changing total time.
    if title == 'Buffalo Gals':
        # Double source durations: sixteenths become slow eighth notes.
        return [(p,d*2) for p,d in notes]
    if title == 'Barbara Allen':
        out=[]; i=0
        while i<len(notes):
            p,d=notes[i]
            if d==.25:
                out.append((notes[i+1][0],.5));i+=2
            else: out.append((p,d));i+=1
        return out
    return notes

if __name__ == '__main__':
    for artist,title,bpm,meter,text,source,description in SONGS:
        c=copy.deepcopy(BASE)
        c['metadata'].update(author='Harmonicon contributors',source=source,
            license='Public-domain underlying melody; chart adaptation MIT',description=description)
        c['song'].update(title=title,artist=artist,tempo_bpm=bpm,key='G' if title.startswith('Swing') else 'C',time_signature=meter,genre='Folk',difficulty='easy')
        c['timing']['tempo_map']=[{'tick':0,'bpm':bpm}]
        c['harmonica']['position']='2nd' if title.startswith('Swing') else '1st'
        c['track']=[]
        cursor=4*60/bpm
        notes=adapted_notes(title,text)
        repeats=4 if title.startswith('Swing') else 2
        first=True
        for verse in range(repeats):
            for p,d in notes:
                seconds=d*60/bpm
                if p!='-':
                    matches=[(h+1,a) for a in ('blow','draw') for h,n in enumerate(c['harmonica']['layout'][a]) if n==p]
                    assert matches, (title,p)
                    h,a=matches[0]
                    event={'id':f'note_{len(c["track"])+1:03}','time':round(cursor,6),'duration':round(seconds,6),'play_mode':'single','events':[{'hole':h,'action':a,'note':p}]}
                    if not c['track'] or first: event['phrase']=f'practice pass {verse+1}'
                    c['track'].append(event)
                first=False
                cursor+=seconds
            cursor+=2*60/bpm
            first=True
        dest=ROOT/artist/title/'song/chart.harpchart'
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
        print(title,len(c['track']),round(cursor,1),'seconds')

"""Rebuild the next public-domain melody exercises without network access."""
from pathlib import Path
from build_beginner_charts import build

if __name__ == '__main__':
    build(Path(__file__).with_name('next_songs.json'))

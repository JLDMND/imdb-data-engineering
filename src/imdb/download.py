import os
import urllib.request
from pathlib import Path

IMDB_BASE_URL = "https://datasets.imdbws.com/"

FILES = [
    "title.basics.tsv.gz",
    "title.ratings.tsv.gz",
    "title.akas.tsv.gz",
    "title.crew.tsv.gz",
    "title.principals.tsv.gz",
    "title.episode.tsv.gz",
    "name.basics.tsv.gz",
]

def download_imdb_files(output_dir="data/raw"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for filename in FILES:
        url = IMDB_BASE_URL + filename
        dest = output_path / filename

        print(f"Downloading {filename}...")

        urllib.request.urlretrieve(url, dest)

        print(f"Saved to {dest}")

if __name__ == "__main__":
    download_imdb_files()

import os
import urllib.request
import hashlib
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

def download_file(url, dest):
    """Download a file from URL to dest."""
    urllib.request.urlretrieve(url, dest)

def compute_md5(path):
    """Compute MD5 checksum for a file."""
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def verify_checksum(file_path, md5_path):
    """Compare local file MD5 with the .md5 file."""
    local_md5 = compute_md5(file_path)
    with open(md5_path, "r") as f:
        expected_md5 = f.read().strip().split()[0]

    if local_md5 == expected_md5:
        print(f"✔ OK: {file_path.name}")
    else:
        print(f"❌ CHECKSUM MISMATCH: {file_path.name}")
        print(f"Expected: {expected_md5}")
        print(f"Found:    {local_md5}")

def download_imdb_files(output_dir="data/raw"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for filename in FILES:
        # ---------- Download main file ----------
        file_url = IMDB_BASE_URL + filename
        dest_file = output_path / filename
        print(f"Downloading {filename}...")
        download_file(file_url, dest_file)

        # ---------- Download checksum file (.md5) ----------
        md5_url = file_url + ".md5"
        dest_md5 = output_path / (filename + ".md5")
        print(f"Downloading {filename}.md5...")
        download_file(md5_url, dest_md5)

        # ---------- Verify integrity ----------
        print(f"Verifying checksum for {filename}...")
        verify_checksum(dest_file, dest_md5)
        print()

if __name__ == "__main__":
    download_imdb_files()

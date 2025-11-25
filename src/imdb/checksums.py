import hashlib
from pathlib import Path

FILES = [
    "title.basics.tsv.gz",
    "title.ratings.tsv.gz",
    "title.akas.tsv.gz",
    "title.crew.tsv.gz",
    "title.principals.tsv.gz",
    "title.episode.tsv.gz",
    "name.basics.tsv.gz",
]

RAW_DIR = Path("data/raw")


def compute_md5(path: Path) -> str:
    """Compute MD5 checksum for a file in streaming fashion."""
    hash_md5 = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def write_md5_file(file_path: Path, md5_hash: str) -> None:
    """
    Write an .md5 file beside the data file.

    Format: '<hash>  filename'  (same as md5sum output)
    """
    md5_path = file_path.with_suffix(file_path.suffix + ".md5")
    content = f"{md5_hash}  {file_path.name}\n"
    md5_path.write_text(content, encoding="utf-8")
    print(f"  -> Wrote {md5_path.name}")


def generate_checksums() -> None:
    """Compute and store MD5 checksums for all expected IMDb raw files."""
    print("Generating MD5 checksums for IMDb raw files...\n")

    for filename in FILES:
        file_path = RAW_DIR / filename
        if not file_path.exists():
            print(f"SKIP: {filename} (file not found in {RAW_DIR})")
            continue

        print(f"Processing {filename}...")
        md5_hash = compute_md5(file_path)
        print(f"  MD5: {md5_hash}")
        write_md5_file(file_path, md5_hash)

    print("\nDone.")


def verify_checksums() -> None:
    """
    Recompute MD5 and compare with existing .md5 file.
    Useful later if you want to re-verify integrity.
    """
    print("Verifying MD5 checksums for IMDb raw files...\n")

    for filename in FILES:
        file_path = RAW_DIR / filename
        md5_path = file_path.with_suffix(file_path.suffix + ".md5")

        if not file_path.exists():
            print(f"SKIP: {filename} (data file missing)")
            continue

        if not md5_path.exists():
            print(f"SKIP: {filename} (.md5 file missing)")
            continue

        # Read expected hash from md5 file
        first_line = md5_path.read_text(encoding="utf-8").strip()
        expected_md5 = first_line.split()[0]

        # Recompute
        current_md5 = compute_md5(file_path)

        if current_md5 == expected_md5:
            print(f"✔ OK: {filename}")
        else:
            print(f"❌ MISMATCH: {filename}")
            print(f"   expected: {expected_md5}")
            print(f"   current : {current_md5}")

    print("\nVerification complete.")


if __name__ == "__main__":
    generate_checksums()
    verify_checksums()


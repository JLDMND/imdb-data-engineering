import pandas as pd
from pathlib import Path
from .utils import load_tsv

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")
PROC_DIR.mkdir(parents=True, exist_ok=True)

def clean_title_basics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply IMDb-specific cleaning rules to title.basics.
    """
    # Replace '\N' with None
    df = df.replace(r"\N", pd.NA)

    # Type casts
    df["startYear"] = pd.to_numeric(df["startYear"], errors="coerce")
    df["endYear"] = pd.to_numeric(df["endYear"], errors="coerce")
    df["runtimeMinutes"] = pd.to_numeric(df["runtimeMinutes"], errors="coerce")

    # Convert isAdult from string to int/bool
    df["isAdult"] = df["isAdult"].astype("Int64")

    # Split multi-valued genres → list
    df["genres"] = df["genres"].str.split(",")
    return df


def clean_title_ratings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace(r"\N", pd.NA)
    df["averageRating"] = pd.to_numeric(df["averageRating"], errors="coerce")
    df["numVotes"] = pd.to_numeric(df["numVotes"], errors="coerce")
    return df


def clean_name_basics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace(r"\N", pd.NA)
    df["birthYear"] = pd.to_numeric(df["birthYear"], errors="coerce")
    df["deathYear"] = pd.to_numeric(df["deathYear"], errors="coerce")
    df["primaryProfession"] = df["primaryProfession"].str.split(",")
    df["knownForTitles"] = df["knownForTitles"].str.split(",")
    return df


def clean_title_crew(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace(r"\N", pd.NA)
    df["directors"] = df["directors"].str.split(",")
    df["writers"] = df["writers"].str.split(",")
    return df

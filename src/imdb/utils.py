import pandas as pd
import duckdb
from pathlib import Path

RAW_DIR = Path("data/raw")


def load_tsv(filename: str, nrows=None):
    """
    Load an IMDb TSV.gz file into Pandas with standard settings.
    """
    return pd.read_csv(
        RAW_DIR / filename,
        sep="\t",
        na_values="\\N",
        compression="gzip",
        low_memory=False,
        nrows=nrows,
    )


def duckdb_scan(filename: str):
    """
    Lazily scan a TSV.gz file with DuckDB using SQL + read_csv_auto.
    This avoids all Python API signature issues.
    """
    path = RAW_DIR / filename
    query = f"""
        SELECT * 
        FROM read_csv_auto(
            '{path.as_posix()}',
            delim='\t',
            header=True,
            nullstr='\\N'
        )
    """
    return duckdb.query(query)


def get_row_count(filename: str) -> int:
    rel = duckdb_scan(filename)
    df = rel.aggregate("COUNT(*) AS row_count").df()

    if df.empty:
        raise ValueError("Row count query returned no rows — check file path or scan logic.")

    # Handle any possible column naming behavior
    col = df.columns[0]     # first (and only) column
    return int(df[col].iloc[0])

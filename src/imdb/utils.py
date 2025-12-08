import pandas as pd
import duckdb
from pathlib import Path

RAW_DIR = Path("data/raw")

def load_tsv(filename: str, nrows=None):
    return pd.read_csv(
        RAW_DIR / filename,
        sep="\t",
        na_values="\\N",
        compression="gzip",
        low_memory=False,
        nrows=nrows,
    )

def duckdb_scan(filename: str):
    path = RAW_DIR / filename
    query = f"""
        SELECT *
        FROM read_csv_auto(
            '{path.as_posix()}',
            delim='\\t',
            header=True,
            nullstr='\\N'
        )
    """
    return duckdb.query(query)

def get_row_count(filename: str) -> int:
    rel = duckdb_scan(filename)
    df = rel.aggregate("COUNT(*) AS row_count").df()
    col = df.columns[0]
    return int(df[col].iloc[0])

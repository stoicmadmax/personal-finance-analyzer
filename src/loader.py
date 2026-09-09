import pandas as pd
from pathlib import Path


REQUIRED_COLUMNS = {
    "date",
    "description",
    "amount",
    "type",
    "category",
    "account",
}


def load_transactions(file_path):
    """Load and validate transaction data from a CSV file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Transaction file not found: {path}")

    df = pd.read_csv(path)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    return df

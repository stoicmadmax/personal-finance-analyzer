import pandas as pd
from pathlib import Path


def load_transactions(file_path):
    """Load transaction data from a CSV file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Transaction file not found: {path}")

    return pd.read_csv(path)

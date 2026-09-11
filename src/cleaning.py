import pandas as pd


def clean_transactions(df):
    """Clean transaction data and validate required fields."""

    cleaned_df = df.copy()

    cleaned_df["amount"] = pd.to_numeric(
        cleaned_df["amount"],
        errors="coerce",
    )

    cleaned_df = cleaned_df.dropna(subset=["amount"])

    return cleaned_df

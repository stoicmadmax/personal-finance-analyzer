import pandas as pd


def monthly_spending(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    expenses = df[df["type"] == "expense"]

    return expenses.groupby("month")["amount"].sum()

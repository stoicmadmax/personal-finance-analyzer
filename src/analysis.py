def calculate_summary(df):
    """Calculate total income, expenses, and net cash flow."""

    total_income = df.loc[df["type"] == "income", "amount"].sum()
    total_expenses = df.loc[df["type"] == "expense", "amount"].sum()
    net_cash_flow = total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_cash_flow": net_cash_flow,
    }

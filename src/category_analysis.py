def spending_by_category(df):
    expenses = df[df["type"] == "expense"]
    
    return expenses.groupby("category")["amount"].sum()

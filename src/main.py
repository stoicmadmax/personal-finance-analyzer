from src.loader import load_transactions
from src.cleaning import clean_transactions
from src.analysis import calculate_summary
from src.category_analysis import spending_by_category
from src.monthly_analysis import monthly_spending


def main():
    file_path = "data/raw/transactions.csv"

    df = load_transactions(file_path)
    df = clean_transactions(df)

    summary = calculate_summary(df)
    category_summary = spending_by_category(df)
    monthly_summary = monthly_spending(df)

    print("\nPERSONAL FINANCE REPORT")
    print("-----------------------")

    print(f"Total income: ₹{summary['total_income']}")
    print(f"Total expenses: ₹{summary['total_expenses']}")
    print(f"Net cash flow: ₹{summary['net_cash_flow']}")

    print("\nSpending by category:")
    print(category_summary)

    print("\nMonthly spending:")
    print(monthly_summary)


if __name__ == "__main__":
    main()

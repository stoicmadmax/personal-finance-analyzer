import pandas as pd

from src.monthly_analysis import monthly_spending

def test_monthly_spending():
    df = pd.DataFrame(
        {
            "date": ["2026-09-02", "2026-09-10", "2026-10-03"],
            "amount": [1000, 500, 2000],
            "type": ["expense", "expense", "income"],
        }
    )

    result = monthly_spending(df)

    september = pd.Period("2026-09", freq="M")

    assert result[september] == 1500

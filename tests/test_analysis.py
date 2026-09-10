import pandas as pd

from src.analysis import calculate_summary


def test_calculate_summary():
    df = pd.DataFrame(
        {
            "amount": [5000, 2000, 1000],
            "type": ["income", "expense", "expense"],
        }
    )

    result = calculate_summary(df)

    assert result["total_income"] == 5000
    assert result["total_expenses"] == 3000
    assert result["net_cash_flow"] == 2000

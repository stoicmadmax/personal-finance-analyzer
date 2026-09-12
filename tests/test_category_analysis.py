import pandas as pd
from src.category_analysis import spending_by_category


def test_spending_by_category():
    df = pd.DataFrame(
        {
            "amount": [1000, 200, 300, 500],
            "type": ["income", "expense", "expense", "expense"],
            "category": ["salary", "food", "food", "transport"],
        }
    )

    result = spending_by_category(df)

    assert result["food"] == 500
    assert result["transport"] == 500


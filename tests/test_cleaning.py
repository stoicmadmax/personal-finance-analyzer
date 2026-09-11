import pandas as pd
from src.cleaning import clean_transactions

def test_clean_transactions_removes_invalid_amounts():
	    df = pd.DataFrame(
        {
            "amount": ["1000", "500.50", "invalid"],
            "type": ["income", "expense", "expense"],
        }
    )
	    cleaned = clean_transactions(df)

	    assert len(cleaned) == 2
	    assert cleaned["amount"].tolist() == [1000.0, 500.5]

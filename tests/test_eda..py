import pandas as pd
from sentiment import sentiment_analysis

def test_sentiment_analysis():
    test_df = pd.DataFrame({
        'headline': [
            "Stock rises after strong earnings",
            "Company hit by major scandal",
            "Market is neutral today"
        ],
        'date': pd.to_datetime(["2023-01-01", "2023-01-02", "2023-01-03"])
    })

    result = sentiment_analysis(test_df.copy())
    assert 'sentiment_compound' in result.columns
    assert 'sentiment_label' in result.columns
    assert result['sentiment_label'].isin(['positive', 'negative', 'neutral']).all()

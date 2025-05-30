import pandas as pd
from correlation import correlation_analysis

def test_correlation_analysis(monkeypatch):
    news_df = pd.DataFrame({
        'date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-02']),
        'sentiment_compound': [0.2, 0.4, -0.3]
    })

    stock_df = pd.DataFrame({
        'Close': [150, 152],
    }, index=pd.to_datetime(['2023-01-01', '2023-01-02']))

    # Test that correlation_analysis runs without error and returns float
    corr = correlation_analysis(news_df, stock_df, return_value=True)
    assert isinstance(corr, float)

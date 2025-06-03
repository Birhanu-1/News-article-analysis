import pandas as pd
import unittest

class TestCorrelationAnalysis(unittest.TestCase):

    def test_merge_sentiment_and_return(self):
        sentiment_df = pd.DataFrame({
            'date': pd.date_range(start="2024-06-01", periods=3),
            'sentiment': [0.2, -0.1, 0.3]
        })

        price_df = pd.DataFrame({
            'date': pd.date_range(start="2024-06-01", periods=3),
            'daily_return': [0.01, -0.02, 0.015]
        })

        merged = pd.merge(sentiment_df, price_df, on='date')
        self.assertEqual(len(merged), 3)
        self.assertIn('sentiment', merged.columns)
        self.assertIn('daily_return', merged.columns)

    def test_correlation_value(self):
        df = pd.DataFrame({
            'sentiment': [0.1, 0.2, 0.3, 0.4],
            'daily_return': [0.02, 0.03, 0.01, 0.04]
        })
        corr = df['sentiment'].corr(df['daily_return'])
        self.assertTrue(-1 <= corr <= 1)

if __name__ == '__main__':
    unittest.main()

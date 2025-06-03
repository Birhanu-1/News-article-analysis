import pandas as pd
from textblob import TextBlob
import unittest

class TestSentimentAnalysis(unittest.TestCase):

    def test_sentiment_scoring(self):
        text = "The stock price will rise significantly."
        polarity = TextBlob(text).sentiment.polarity
        self.assertTrue(-1 <= polarity <= 1)

    def test_sentiment_data_format(self):
        df = pd.DataFrame({
            'headline': ["Good news", "Bad market", "Neutral headline"],
            'date': ["2024-06-01", "2024-06-01", "2024-06-02"]
        })
        df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
        grouped = df.groupby('date')['sentiment'].mean()
        self.assertIn("2024-06-01", grouped.index)

if __name__ == '__main__':
    unittest.main()

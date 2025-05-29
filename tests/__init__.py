import unittest
import pandas as pd

class TestDataLoad(unittest.TestCase):
    def test_read(self):
        df = pd.read_csv("data/articles.csv")
        self.assertIn("headline", df.columns)

import pandas as pd
import talib
import unittest

class TestTechnicalIndicators(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Close': [100, 102, 101, 105, 110, 108, 107, 112, 115, 117]
        })

    def test_sma(self):
        sma = talib.SMA(self.df['Close'], timeperiod=3)
        self.assertEqual(len(sma), len(self.df))
        self.assertTrue(sma.isna().sum() > 0)

    def test_rsi(self):
        rsi = talib.RSI(self.df['Close'], timeperiod=5)
        self.assertTrue((rsi.dropna() >= 0).all() and (rsi.dropna() <= 100).all())

    def test_macd(self):
        macd, signal, hist = talib.MACD(self.df['Close'])
        self.assertEqual(len(macd), len(self.df))
        self.assertEqual(len(signal), len(self.df))

if __name__ == '__main__':
    unittest.main()

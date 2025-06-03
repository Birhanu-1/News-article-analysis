# 🧪 Notebooks Overview – Predicting Price Moves with News Sentiment

This folder contains Jupyter notebooks that implement the full pipeline for analyzing the relationship between financial news sentiment and stock price movements.

Each notebook corresponds to a specific task in the Week 1 assignment (B5W1) for 10 Academy.

---

## ✅ Notebook Index

### 📘 1. `Task_1_Sentiment_Analysis.ipynb`
- **Goal**: Perform sentiment analysis on financial news headlines.
- **Steps**:
  - Load and clean `raw_analyst_data.csv`
  - Apply `TextBlob` and/or `NLTK` VADER for sentiment scoring
  - Aggregate sentiment scores by date
  - Save output as `outputs/daily_sentiment.csv`

### 📘 2. `Task_2_Technical_Analysis.ipynb`
- **Goal**: Perform quantitative analysis on stock price data.
- **Steps**:
  - Load OHLCV data from `data/yfinance/`
  - Compute technical indicators using `TA-Lib`: SMA, RSI, MACD
  - Calculate daily returns using `PyNance` or `pandas`
  - Save enriched dataset to `outputs/price_with_indicators.csv`

### 📘 3. `Task_3_Correlation_Analysis.ipynb`
- **Goal**: Analyze correlation between sentiment and stock returns.
- **Steps**:
  - Align news sentiment and stock data by date
  - Merge sentiment scores and returns
  - Compute correlation coefficient (Pearson)
  - Visualize the relationship and save plot as `outputs/sentiment_vs_return.png`

---

## ⚙️ How to Use These Notebooks

### 1. Install requirements
```bash
pip install -r requirements.txt

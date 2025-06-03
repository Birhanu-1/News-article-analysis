# 📈 Predicting Price Moves with News Sentiment

This notebook-based project explores how news sentiment influences stock price movement by combining Natural Language Processing (NLP) with financial time series analysis. It is divided into three main tasks that analyze textual news data and financial market data to identify potential predictive patterns.

---

## 🧠 Project Objective

To quantify the impact of news sentiment on stock price movements by:
- Extracting sentiment scores from news headlines
- Performing technical analysis on stock price data
- Correlating sentiment with daily stock returns

---

## 📁 Project Structure

News-article-analysis/
│
├── data/
│ ├── raw_analyst_data.csv # Raw news headlines
│ └── yfinance/ # Historical stock price data
│
├── outputs/
│ ├── daily_sentiment.csv # Daily sentiment scores
│ ├── price_with_indicators.csv # Financial indicators + returns
│ └── sentiment_vs_return.png # Correlation plot
│
├── notebooks/
│ ├── Task_1_Sentiment_Analysis.ipynb
│ ├── Task_2_Technical_Analysis.ipynb
│ └── Task_3_Correlation_Analysis.ipynb
│
├── .github/workflows/ # GitHub Actions for CI (optional)
└── README.md

markdown
Copy
Edit

---

## ✅ Tasks Overview

### 🔹 Task 1: Sentiment Analysis of News Headlines

**Notebook**: `Task_1_Sentiment_Analysis.ipynb`

- **Objective**: Convert financial news headlines into sentiment scores.
- **Steps**:
  - Load and clean `raw_analyst_data.csv`
  - Apply `TextBlob` to compute sentiment polarity
  - Aggregate daily sentiment by stock symbol
  - Save results as `outputs/daily_sentiment.csv`

- **Libraries Used**: `pandas`, `TextBlob`, `nltk`

---

### 🔹 Task 2: Quantitative Analysis Using TA-Lib and PyNance

**Notebook**: `Task_2_Technical_Analysis.ipynb`

- **Objective**: Use financial indicators to analyze stock movement.
- **Steps**:
  - Load OHLCV stock data from `data/yfinance/`
  - Calculate:
    - Simple Moving Average (SMA)
    - Relative Strength Index (RSI)
    - Moving Average Convergence Divergence (MACD)
    - Daily returns
  - Save results as `outputs/price_with_indicators.csv`

- **Libraries Used**: `TA-Lib`, `PyNance`, `pandas`, `matplotlib`

---

### 🔹 Task 3: Correlation Between News and Stock Movement

**Notebook**: `Task_3_Correlation_Analysis.ipynb`

- **Objective**: Examine the relationship between sentiment and returns.
- **Steps**:
  - Merge sentiment and stock return data by date
  - Compute correlation (e.g., Pearson)
  - Visualize relationship using scatter plots

- **Libraries Used**: `pandas`, `seaborn`, `matplotlib`, `scipy`

---

## 📊 Sample Output

![image](https://github.com/user-attachments/assets/443ca0a2-bc12-4d97-bcc8-f36764b1757f)


![image](https://github.com/user-attachments/assets/bbfff7d3-decc-4016-8da6-3b39a901806d)

---

## 🚀 How to Run the Project

1. Clone this repo:
   ```bash
   git clone https://github.com/Birhanu-1/News-article-analysis.git
   cd News-article-analysis
Install the requirements:

bash
Copy
Edit
pip install -r requirements.txt
Launch the notebooks:

bash
Copy
Edit
jupyter notebook notebooks/
Open and run each of the following:

Task_1_Sentiment_Analysis.ipynb

Task_2_Technical_Analysis.ipynb

Task_3_Correlation_Analysis.ipynb

📌 Requirements
Python 3.8+

Jupyter Notebook

pandas, matplotlib, seaborn, TextBlob, nltk

TA-Lib (may require C dependencies)

PyNance

yfinance

🧪 Evaluation Context
This project was developed for 10 Academy - Week 1 as part of the assignment:

B5W1: Predicting Price Moves with News Sentiment – Final Submission

👤 Author
Birhanu Berihun

📄 License
MIT License – see LICENSE for details.

yaml
Copy
Edit

---

Let me know if you'd like me to also generate:
- A `requirements.txt` file
- A blog-style Medium post based on the final notebook
- An automated `notebook_runner.py` to run all tasks end-to-end








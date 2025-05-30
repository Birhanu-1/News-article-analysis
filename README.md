📈 News Sentiment Analysis and Correlation with Stock Prices
This project analyzes financial news headlines from analyst ratings and correlates the sentiment with stock price movements. It combines qualitative textual data (news headlines) and quantitative financial metrics (stock prices) for exploratory and statistical analysis.

🗂️ Project Structure
bash
Copy
Edit
.
├── data/
│   ├── raw_analyst_ratings.csv         # Raw dataset with news headlines and analyst ratings
│   └── stock_data/                     # Folder with pre-downloaded yfinance data (e.g., AAPL.csv)
├── scripts/
│   ├── eda.py                          # Functions for descriptive stats and topic modeling
│   ├── sentiment.py                    # Sentiment analysis using VADER
│   └── correlation.py                  # Sentiment-stock price correlation analysis
├── main.py                             # Main script to execute full pipeline
└── README.md                           # Project documentation
📌 Objective
Analyze textual news data for trends and topic patterns.

Perform sentiment analysis using VADER (from NLTK).

Download and process historical stock prices (or load from local CSV).

Merge both datasets on date and stock to perform correlation analysis.

Visualize insights (time series, word clouds, bar charts, heatmaps).

⚙️ Requirements
bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn nltk wordcloud yfinance
Also, download the VADER lexicon:

python
Copy
Edit
import nltk
nltk.download('vader_lexicon')
📥 Data Sources
Analyst Ratings Dataset: CSV containing columns like headline, publisher, date, stock.

Stock Data: Loaded from Yahoo Finance via yfinance or from local files.

🚀 How to Run
1. Clone this repo:
bash
Copy
Edit
git clone https://github.com/your_username/financial-news-sentiment.git
cd financial-news-sentiment
2. Run the analysis pipeline:
bash
Copy
Edit
python main.py
🔍 Functionality Overview
🧾 Descriptive Statistics & EDA
Word frequency, headline length

Articles per publisher and hour

Topic modeling using LDA

Daily publication trends

💬 Sentiment Analysis
VADER sentiment scoring per headline

Categorization into positive, negative, or neutral

📈 Stock Data Integration
Daily price aggregation from yfinance or CSV

Merge with news sentiment by date and stock

🔄 Correlation Analysis
Compute Pearson correlation between:

Daily average sentiment score

Daily closing stock prices

Dual-axis plots to visualize sentiment vs. price trends

📊 Example Output
📉 Time series plot of sentiment vs. stock price

☁️ Word clouds of common headline terms

🔥 Heatmap of publisher activity by weekday

📘 Bar charts of frequent terms per publisher

🛠️ Improvements Underway
✅ Your code showcases clear progress in intermediate functionalities, including loading datasets, calculating technical indicators using TA-Lib, and performing financial metric calculations.
⚠️ However, there is no evidence of actual sentiment analysis or correlation analysis between news sentiment and stock price movements, which are core tasks of the project.
💡 Improvements: Include sentiment scoring and correlation insights as implemented in this version.

🧱 Your repository shows the presence of organized notebooks dedicated to different stocks with modular functions for loading data, computing indicators, and plotting results.
📌 Suggestion: Improve separation between sentiment analysis and technical indicator computations for better modularity and maintainability.
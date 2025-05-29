# scripts/eda_statistics.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/articles.csv")
df['headline_length'] = df['headline'].str.len()

print(df['headline_length'].describe())
print(df['publisher'].value_counts().head())

df['date'] = pd.to_datetime(df['date'])
df['date'].dt.date.value_counts().sort_index().plot(title="Articles Per Day")
plt.tight_layout()
plt.savefig("notebooks/plots/articles_per_day.png")

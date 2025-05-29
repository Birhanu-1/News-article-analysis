# scripts/publisher_analysis.py
df['publisher_domain'] = df['publisher'].str.extract(r'@([\w\.-]+)')
print(df['publisher_domain'].value_counts().head())

# scripts/topic_modeling.py
from gensim import corpora, models
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

df = pd.read_csv("data/articles.csv")
texts = df['headline'].dropna().apply(lambda x: [w for w in word_tokenize(x.lower()) if w.isalpha() and w not in stopwords.words('english')])
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}")

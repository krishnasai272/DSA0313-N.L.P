from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "machine learning is interesting",
    "python is used for machine learning",
    "deep learning uses neural networks"
]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs)

print(tfidf.toarray())

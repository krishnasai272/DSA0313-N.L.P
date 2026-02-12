from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "The cat sits on the mat.",
    "It is sleeping peacefully."
]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(text)

similarity = cosine_similarity(tfidf[0], tfidf[1])
print("Coherence score:", similarity[0][0])

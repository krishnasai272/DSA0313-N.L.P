from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["running", "runs", "easily", "fairness"]
for word in words:
    print(word, "->", stemmer.stem(word))

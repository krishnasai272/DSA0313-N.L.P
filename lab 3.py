from nltk.stem import PorterStemmer
# Input sentence
sentence = "The children are playing happily"
# Tokenization
tokens = sentence.split()
# Create stemmer
stemmer = PorterStemmer()
print("Word\t\tStem")
print("----------------------")
for word in tokens:
    w = word.lower()          # convert to lowercase
    stem = stemmer.stem(w)    # apply stemming
    print(w, "\t\t", stem)

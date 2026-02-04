import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The quick brown fox jumps over the lazy dog"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)
+
print("POS Tagged Sentence:")
print(pos_tags)

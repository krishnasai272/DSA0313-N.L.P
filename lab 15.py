import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.5] | 'Mary' [0.5]
VP -> V NP [1.0]
V -> 'sees' [1.0]
""")

parser = ViterbiParser(grammar)

sentence = "John sees Mary".split()

for tree in parser.parse(sentence):
    print(tree)

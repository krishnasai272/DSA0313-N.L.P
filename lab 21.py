import nltk

sentence = "The smart boy solved the difficult problem"

tokens = nltk.word_tokenize(sentence)
pos = nltk.pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)

tree = cp.parse(pos)

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        print("Noun Phrase:", " ".join(word for word, tag in subtree.leaves()))

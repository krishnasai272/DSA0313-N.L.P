import nltk

text = "John went to the market. He bought apples."

sentences = nltk.sent_tokenize(text)

last_noun = None

for sent in sentences:
    words = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(words)

    for word, tag in tags:
        if tag.startswith('NN'):
            last_noun = word
        elif word.lower() in ['he','she','it'] and last_noun:
            print(word, "refers to", last_noun)

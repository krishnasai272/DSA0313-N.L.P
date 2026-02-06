import re

sentence = "Ravi is playing happily with friends"
words = sentence.split()

def regex_pos_tag(word):
    if re.match(r'.*ing$', word):
        return 'VBG'     # verb gerund
    elif re.match(r'.*ly$', word):
        return 'RB'      # adverb
    elif re.match(r'[A-Z][a-z]+$', word):
        return 'NNP'     # proper noun
    elif re.match(r'.*s$', word):
        return 'NNS'     # plural noun
    else:
        return 'NN'      # noun (default)

for w in words:
    print(w, "->", regex_pos_tag(w))

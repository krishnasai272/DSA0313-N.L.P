sentence = "Dogs bark loudly"
words = sentence.split()

# Initial tagging (default noun)
tags = {w: 'NN' for w in words}

# Transformation rule: words ending with "ly" → adverb
for w in words:
    if w.endswith("ly"):
        tags[w] = 'RB'

for w in words:
    print(w, "->", tags[w])

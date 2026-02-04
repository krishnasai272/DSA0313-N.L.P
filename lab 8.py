
prob_model = {
    "the": {"DT": 1.0},
    "dog": {"NN": 0.7, "VB": 0.3},
    "barks": {"VB": 0.9, "NN": 0.1},
    "cat": {"NN": 1.0},
    "runs": {"VB": 0.8, "NNS": 0.2}
}

sentence = "the dog barks"
words = sentence.split()

tagged_sentence = []

for word in words:
    word = word.lower()
    if word in prob_model:
        tag = max(prob_model[word], key=prob_model[word].get)
    else:
        tag = "NN"   # Default tag
    tagged_sentence.append((word, tag))

print("Stochastic POS Tagged Sentence:")
print(tagged_sentence)

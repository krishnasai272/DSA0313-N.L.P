import random

text = "I love natural language processing and I love machine learning"
words = text.split()

bigrams = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in bigrams:
        bigrams[word] = []
    bigrams[word].append(next_word)

current_word = "I"
generated_text = current_word

for _ in range(10):
    next_words = bigrams.get(current_word, [])
    if not next_words:
        break
    current_word = random.choice(next_words)
    generated_text += " " + current_word

print("Generated Text:")
print(generated_text)

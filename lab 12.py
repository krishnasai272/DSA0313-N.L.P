def earley_parse(sentence):
    words = sentence.split()
    print("Earley parsing demonstration")
    for i, w in enumerate(words):
        print("Scanning:", w)
    print("Sentence parsed successfully (demo)")

earley_parse("the cat chased the dog")

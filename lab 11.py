grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the']],
    'N': [['cat'], ['dog']],
    'V': [['chased']]
}

def parse(symbol, words):
    if not words:
        return False
    if symbol not in grammar:
        return words[0] == symbol, words[1:]

    for rule in grammar[symbol]:
        remaining = words[:]
        success = True
        for sym in rule:
            ok, remaining = parse(sym, remaining)
            if not ok:
                success = False
                break
        if success:
            return True, remaining
    return False, words

sentence = "the cat chased the dog".split()
result, rem = parse('S', sentence)

print("Accepted" if result and not rem else "Rejected")

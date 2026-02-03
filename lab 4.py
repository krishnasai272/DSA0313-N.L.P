def plural(noun):
    if noun[-1] == 'y':
        return noun[:-1] + 'ies'
    elif noun[-1] in ['s', 'x']:
        return noun + 'es'
    else:
        return noun + 's'
words = ["cat", "bus", "baby", "box", "boy"]

for w in words:
    print(w, "->", plural(w))

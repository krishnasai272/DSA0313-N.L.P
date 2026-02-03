def fsa_end_ab(string):
    state = 0

    for ch in string:
        if state == 0:
            state = 1 if ch == 'a' else 0
        elif state == 1:
            state = 2 if ch == 'b' else (1 if ch == 'a' else 0)
        elif state == 2:
            state = 1 if ch == 'a' else 0

    return state == 2

# Test
inputs = ["ab", "cab", "abc", "aab"]
for i in inputs:
    print(i, "->", fsa_end_ab(i))

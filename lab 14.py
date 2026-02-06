sentence = "He runs"
words = sentence.split()

subject = words[0]
verb = words[1]

if subject.lower() in ['he','she','it'] and not verb.endswith('s'):
    print("Agreement Error")
else:
    print("Agreement Correct")

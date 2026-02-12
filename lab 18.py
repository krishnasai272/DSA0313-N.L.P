import re

expr = "Loves(John,Mary)"

pattern = r'(\w+)\((\w+),(\w+)\)'
match = re.match(pattern, expr)

if match:
    predicate, arg1, arg2 = match.groups()
    print("Predicate:", predicate)
    print("Arguments:", arg1, arg2)

import re

with open('input.txt') as f:
    text = f.read()

pattern_p1 = 'mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)'
pattern_p2 = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)|do\(\s*\)|don't\(\s*\)"
matches = re.finditer(pattern_p2, text)

matches = [m.group(0) for m in list(matches)]

print(matches)

# part 1
"""total = 0
for m in matches:
    a, b = m[0], m[1]
    a, b = ''.join(c for c in a if c.isdigit()), ''.join(c for c in b if c.isdigit())
    a, b = int(a), int(b)

    total += a * b

print(total)"""

# part 2
print(matches.count('do()'))
print(matches.count("don't()"))
total = 0
do = True
for m in matches:
    if m == 'do()' or m == "don't()":
        if m == 'do()':
            do = True
        else:
            do = False
    else:
        a, b = m.split(',')[0], m.split(',')[1]
        a, b = ''.join(c for c in a if c.isdigit()), ''.join(c for c in b if c.isdigit())
        a, b = int(a), int(b)

        if do:
            total += (a * b)

print(total)

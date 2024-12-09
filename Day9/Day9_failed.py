""" MULTI DIGIT IDS NEED TO BE KEPT TOGETHER, THIS METHOD DOES NOT WORK"""

with open('example2.txt') as f:
    l = f.read()

literal = '' # string containing correct values w/ periods
index = 0
for i in range(len(l)): # assemble literal
    c = l[i]
    if i % 2 == 0:
        literal += (str(index) * int(c))
        index += 1
    else:
        literal += '.' * int(c)

print(literal)

literal = list(literal)
for i in reversed(range(len(literal))): # swap values around
    if literal[i] != '.':
        first = literal.index('.')
        if i < first:
            break
        literal[i], literal[first] = literal[first], literal[i]
        print(f'iter reversed: {i}')

literal = ''.join(l for l in literal)
print(literal)



total = 0
for i in range(len(literal)): # compute total
    c = literal[i]
    if not c.isnumeric():
        break

    total += i * int(c)

print(total)



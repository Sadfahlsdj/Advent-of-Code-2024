""" I THOUGHT I WAS SO GODDAMN SMART
regex fails due to very exorbitant runtime"""

import re

with open('input.txt') as f:
    lines = f.readlines()

    inputs = [w.strip() for w in lines[0].split(',')]
    towels = [w.strip() for w in lines[2:]]

str = '^('
for i in inputs:
    str += i
    if inputs.index(i) < (len(inputs) - 1):
        str += '|'

str += ')*$'
pattern = re.compile(str)

# doing manual way for logging
sum = 0
for t in towels:
    print(f'iteration {towels.index(t)} of {len(towels)}')
    sum += bool(pattern.match(t))

"""truths = [bool(pattern.match(t)) for t in towels] 
print(sum(truths))"""

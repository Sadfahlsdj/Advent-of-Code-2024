import re
from helper import extract_col, replace, max_all

swaps_file, molecule_file = 'swaps.txt', 'mol.txt'

with open(swaps_file) as f:
    lswaps = [l.strip() for l in f.readlines()]

with open(molecule_file) as f:
    final_mol = f.read().strip()

swaps_rev = set([(l.split('=>')[1].strip(),
                  l.split('=>')[0].strip()) for l in lswaps])

keys, values = extract_col(0, swaps_rev), extract_col(1, swaps_rev)

count = 0
curr = final_mol

while curr != 'e':
    valid = [k for k in keys if k in curr]
    if len(valid) == 0:
        print(curr)
        break

    """longest = str(max(valid, key=len))
    longest_swapped = values[keys.index(longest)]

    indexes = [m.start() for m in re.finditer(longest, curr)]
    for i in indexes:
        curr = replace(longest, longest_swapped, curr, i)
        print(f'key: {longest}, val: {longest_swapped}, idx: {i}, new: {curr}')
        count += 1"""

    longest = max_all(valid)
    longest_swapped = [values[keys.index(l)] for l in longest]

    indexes = [[[m.start() for m in re.finditer(l, curr)], l] for l in longest]
    indexes = sum(indexes, []) # flatten


    for i in indexes:
        idxs, val = indexes[0], indexes[1]
        for idx in idxs:
            curr = replace(val, longest_swapped[longest.index(val)], curr, idx)
            print(f'key: {longest}, val: {longest_swapped}, idx: {i}, new: {curr}')
            count += 1

print(count)





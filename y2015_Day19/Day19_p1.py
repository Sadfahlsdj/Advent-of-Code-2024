import re
from helper import replace, extract_col

swaps_file, molecule_file = 'swaps.txt', 'mol.txt'

with open(swaps_file) as f:
    lswaps = [l.strip() for l in f.readlines()]

with open(molecule_file) as f:
    str = f.read().strip()

swaps = [(l.split('=>')[0].strip(), l.split('=>')[1].strip()) for l in lswaps]

new_mols = set() # possible new molecules

keys, values = extract_col(0, swaps), extract_col(1, swaps)

for i in range(len(keys)):
    key = keys[i]
    if key in str:
        new = values[i]
        occs = [m.start() for m in re.finditer(key, str)]
        keylen = len(key)

        for idx in occs:
            new_mol = replace(key, new, str, idx)
            print(f'key: {key}, val: {new}, idx: {idx}, new: {new_mol}')
            new_mols.add(new_mol)

print(len(new_mols))


import math

with open('input.txt') as f:
    l = f.read().strip()

vals = []
dot_ranges = [] # each value = (starting index, length)
index = 0
for i in range(len(l)): # assemble blocks
    c = l[i]
    for j in range(int(c)):
        if i % 2 == 0:
            vals.append(str(index))
        else:
            vals.append('.')

    if i % 2 == 0: # doing this scuffed for dot ranges
        index += (i % 2 == 0)
    else:
        dot_ranges.append((len(vals) - int(c), int(c)))

"""# p1
for i in reversed(range(len(vals))): # swap values around
    if vals[i] != '.':
        first = vals.index('.')
        if i < first:
            break
        vals[i], vals[first] = vals[first], vals[i]
        # print(f'iter reversed: {i}')"""

def find_earliest_dots(arr, l, index):
    # index input is to make sure you aren't moving backwards, you're not supposed to
    for i in range(len(arr)):
        a = arr[i]
        if a[1] >= l and a[0] <= index:
            arr[i] = (a[0] + l, a[1] - l)
            return (True, a[0], arr)

    return (False, i, arr)

# p2
iter = 1
vals_numeric = [int(v) for v in vals if (v.isnumeric() and not v.isspace())]
for v in sorted(set(vals_numeric), reverse=True): # need to sort by number value, not by str value
    v = str(v)
    count = vals.count(v)
    idx = vals.index(v)
    truth, index, dot_ranges = find_earliest_dots(dot_ranges, count, idx)

    diagnostic = f'iter: {iter} of {len(set(vals_numeric))}'
    if truth:
        diagnostic += f' val = {v}, count = {count}'
        ind = vals.index(v)
        for i in range(count):
            vals[index + i], vals[ind + i] = vals[ind + i], vals[index + i]

    # diagnostics
    print(diagnostic)
    iter += 1

total = 0
for i in range(len(vals)): # compute total
    c = vals[i]
    if not c.isnumeric():
        continue

    total += i * int(c)

print(total)

# p2 wrong - 8554338581103


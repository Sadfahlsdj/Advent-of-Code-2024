import copy

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

nums = []
for l in lines:
    nums.append([int(n) for n in l.split()])

def safe(n):
    sortable, diffs = True, True

    if sorted(n) != n and sorted(n, reverse=True) != n:
        sortable = False

    for i in range(1, len(n)):
        if (n[i] == n[i - 1]) or abs(n[i] - n[i - 1]) > 3:
            diffs = False

    return int(sortable and diffs)

count = 0
for n in nums:
    if safe(n):
        count += 1
    else:
        for i in range(len(n)):
            if safe(n[:i] + n[i+1:]):
                count += 1
                break

print(count)

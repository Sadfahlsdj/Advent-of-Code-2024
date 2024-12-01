import math

with open('part1_input.txt') as f:
    lines = f.readlines()

l1, l2 = [], []
for l in lines:
    l = l.strip()
    n1, n2 = int(l.split('   ')[0]), int(l.split('   ')[1])

    l1.append(n1)
    l2.append(n2)

l1.sort()
l2.sort()

sum = 0
for l in range(len(l1)):
    sum += abs(l1[l] - l2[l])

print(sum)
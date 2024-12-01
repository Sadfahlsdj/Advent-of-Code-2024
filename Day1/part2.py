with open('part1_input.txt') as f:
    lines = f.readlines()

l1, l2 = [], []
for l in lines:
    l = l.strip()
    n1, n2 = int(l.split('   ')[0]), int(l.split('   ')[1])

    l1.append(n1)
    l2.append(n2)

sum = 0
for n in l1:
    val = l2.count(n)
    sum += n * val

print(sum)
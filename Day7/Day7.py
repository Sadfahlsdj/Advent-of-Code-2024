with open('input.txt') as f:
    lines = f.readlines()

d = {}
for l in lines:
    total = int(l.split(':')[0])
    vals = [int(n.strip()) for n in l.split(':')[1].strip().split()]
    d[total] = vals

total = 0
iter = 0
for k, v in d.items():
    current = set()
    current.add(v[0])
    v = list(v)

    for i in range(len(v) - 1):
        temp = set()
        for c in current:
            temp.add(c + v[i + 1])
            temp.add(c * v[i + 1])
            temp.add(int(str(c) + str(v[i + 1]))) # p2 only

        current = temp

    current = set(current)
    iter += 1
    print(f'iter: {iter}')
    if k in current:
        total += k

print(total)
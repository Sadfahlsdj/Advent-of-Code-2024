import copy

with open('input.txt') as f:
    ns = [int(n) for n in f.readline().split()]

loops = 25
memo = {} # dp
for i in range(loops):
    ns_new = []
    digit_lengths = []
    # if 0 store (0, 0), else store

    for n in ns:
        l = len(str(n))
        if n in memo.keys():
            for v in memo[n]:
                ns_new.append(v)
        elif n == 0:
            ns_new.append(1)
            memo[n] = (1,)
        elif l % 2 == 0:
            ns_new.append(int(str(n)[:int(l/2)]))
            ns_new.append(int(str(n)[int(l / 2):]))
            memo[n] = (int(str(n)[:int(l/2)]), int(str(n)[int(l / 2):]))
        else:
            ns_new.append(n * 2024)
            memo[n] = (n * 2024,)

    ns = copy.deepcopy(ns_new)

    print(f'iter: {i}, unique: {len(set(ns))}, len: {len(ns)}')

print(len(ns))

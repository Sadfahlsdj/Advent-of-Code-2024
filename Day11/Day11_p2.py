import copy
import time

# approx runtime w/ memo around 0.12s, w/o 0.165

start = time.time()

with open('input.txt') as f:
    ns = [int(n) for n in f.readline().split()]

ns = dict([(k, 1) for k in ns]) # store dict of {value: count} to avoid millions length array
print(ns)

loops = 75
memo = {} # dp
for i in range(loops):
    ns_new = dict()
    digit_lengths = []
    # if 0 store (0, 0), else store

    for val, iters in ns.items():
        l = len(str(val))

        if val in memo.keys(): # if memoized, skip rest
            for v in memo[val]:
                if v in ns_new.keys():
                    ns_new[v] += iters
                else:
                    ns_new[v] = iters

        elif val == 0: # if val == 0, add corresponding amount of 1s
            if 1 in ns_new.keys():
                ns_new[1] += iters
            else:
                ns_new[1] = iters
            memo[val] = (1,)
        elif l % 2 == 0: # add corresponding amount of 1st halves and 2nd halves
            first_half = int(str(val)[:int(l/2)])
            second_half = int(str(val)[int(l/2):])

            if first_half in ns_new.keys():
                ns_new[first_half] += iters
            else:
                ns_new[first_half] = iters

            if second_half in ns_new.keys():
                ns_new[second_half] += iters
            else:
                ns_new[second_half] = iters

            memo[val] = (first_half, second_half)
        else:
            if (val * 2024) in ns_new.keys():
                ns_new[val * 2024] += iters
            else:
                ns_new[val * 2024] = iters
            memo[val] = (val * 2024,)

    ns = copy.deepcopy(ns_new)

    print(f'iter: {i}, dict: {len(ns)}')

total = sum([l for l in ns.values()])
print(total)
print(f'time: {time.time() - start}')

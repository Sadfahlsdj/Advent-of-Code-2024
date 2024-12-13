import numpy as np

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

total = 0
for i in range(0, len(lines), 4):
    ls = [lines[i], lines[i+1], lines[i+2], lines[i+3]]
    strs = [''.join([s for s in l if s.isdigit() or s.isspace()]).strip() for l in ls if l]
    vals = [[int(c) for c in s.split()] for s in strs]

    Xs = np.array([[vals[0][0], vals[1][0]], [vals[0][1], vals[1][1]]])
    # Ys = np.array([[vals[2][0]], [vals[2][1]]]) # p1
    Ys = np.array([[vals[2][0] + 10000000000000], [vals[2][1] + 10000000000000]]) # p2

    sol = [round(float(n), 3) for n in np.matmul(np.linalg.inv(Xs), Ys).flatten()]
    ints = [i % 1 == 0 for i in sol]

    if all(ints):
        total += (3 * sol[0] + sol[1])

print(int(total))


""" despite "optimized" being in the filename, it still takes approx 10 seconds to run
best guess is that this is for the most part due to python being python"""

import networkx as nx # im on vacation, nx can do the pathfinding algo for me
import time # for diagnostics
def manh_dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

start_time = time.time()
with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

start, end = (0, 0), (0, 0)
obstacles = []
g = nx.Graph()

for i in range(len(lines)):
    for j in range(len(lines[0])):
        # add node & adjacent edges assuming no obstacles based on graph size
        g.add_node((i, j))

        adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for a in adj:
            if (0 <= a[0] < len(lines)) and (0 <= a[1] < len(lines)):
                g.add_edge((i, j), (a[0], a[1]))

        # check for start/end/obstacle
        if lines[i][j] == 'S':
            start = (i, j)
        elif lines[i][j] == 'E':
            end = (i, j)
        elif lines[i][j] == '#':
            obstacles.append((i, j))

# remove nodes with obstacles on them
for o in obstacles:
    g.remove_node((o[0], o[1]))

counts = {}
raw_path = nx.shortest_path(g, start, end) # used for the actual algo

print(f'initialization done, time: {time.time() - start_time}') # initial pathfinding & other

max_len = 20 # 2 for p1, 20 for p2
for i in range(len(raw_path)):
    for j in range(i, len(raw_path)):
        first, second = raw_path[i], raw_path[j]
        raw_len = j - i
        if 1 < manh_dist(first, second) <= max_len: # <= max_len apart means cheat can be used
            gain = raw_len - manh_dist(first, second)

            if gain in counts:
                counts[gain] += 1
            else:
                counts[gain] = 1

total = 0
for c in sorted([ch for ch in counts.keys() if ch >= 100]):
    total += counts[c]

print(total)
print(f'program done, time: {time.time() - start_time}')
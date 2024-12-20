import networkx as nx
from copy import deepcopy

def hash(x, y):
    return (1000 * x + y)

def add_node_and_edges(g, node):
    g.add_node(node)
    if (node - 1) in g.nodes:
        g.add_edge(node, (node - 1))
    if (node + 1) in g.nodes:
        g.add_edge(node, (node + 1))
    if (node - 1000) in g.nodes:
        g.add_edge(node, (node - 1000))
    if (node + 1000) in g.nodes:
        g.add_edge(node, (node + 1000))

with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

start, end = (0, 0), (0, 0)
obstacles = []
g = nx.Graph()

for i in range(len(lines)):
    for j in range(len(lines[0])):
        # add node & adjacent edges
        node_name = hash(i, j)
        g.add_node(node_name)

        adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for a in adj:
            if (0 <= a[0] < len(lines)) and (0 <= a[1] < len(lines)):
                g.add_edge(node_name, hash(a[0], a[1]))

        # check for start/end/obstacle
        if lines[i][j] == 'S':
            start = (i, j)
        elif lines[i][j] == 'E':
            end = (i, j)
        elif lines[i][j] == '#':
            obstacles.append((i, j))

for o in obstacles:
    g.remove_node(hash(o[0], o[1]))

raw_path_len = nx.shortest_path_length(g, hash(start[0], start[1]), hash(end[0], end[1]))
cheats = {}
used_cheats = set()
iter = 0 # diagnostics
for a in g.nodes:
    for b in g.nodes:
        if abs(a - b) == 2 or abs(a - b) == 1001 or abs(a - b) == 2000:
            if int((a + b) / 2) not in used_cheats:
                iter += 1
                print(f'going through cheat spot {int((a + b) / 2)} number {iter}')
                g_temp = deepcopy(g)
                add_node_and_edges(g_temp, int((a + b) / 2))
                timesave = (raw_path_len -
                            nx.shortest_path_length(g_temp, hash(start[0], start[1]), hash(end[0], end[1])))

                if timesave > 0:
                    if timesave in cheats:
                        cheats[timesave] += 1
                    else:
                        cheats[timesave] = 1

                used_cheats.add(int((a + b) / 2))

total = 0
for c in [ch for ch in cheats.keys() if ch >= 100]:
    total += cheats[c]

print(total)
import networkx as nx
import matplotlib.pyplot as plt

def hash(x, y):
    return 1000 * x + y

grid_limit = 71 # 7 for example, 71 for actual

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

lines = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in lines]
lines_first = lines[:1024] # 12 for ex, 1024 for input

g = nx.Graph()
for i in range(grid_limit):
    for j in range(grid_limit):
        node_name = hash(i, j)
        g.add_node(node_name)

        adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for a in adj:
            if (0 <= a[0] < grid_limit) and (0 <= a[1] < grid_limit):
                g.add_edge(node_name, hash(a[0], a[1]))

for l in lines_first:
    g.remove_node(hash(l[0], l[1]))

# p1
dij = nx.dijkstra_path_length(g, hash(0, 0),
                              hash(grid_limit - 1, grid_limit - 1))

for l in lines[1024:]:
    g.remove_node(hash(l[0], l[1]))
    try:
        dij = nx.dijkstra_path_length(g, hash(0, 0),
                                      hash(grid_limit - 1, grid_limit - 1))
        print(f'trying {l}')
    except:
        print(l)
        break







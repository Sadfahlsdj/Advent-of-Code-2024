import networkx as nx
import time

def sized_conn_comps(graph):
    ccs = set()
    nodes = list(graph.nodes)
    for n in nodes:
        for neighbor in graph[n]:
            for neighbor2 in graph[neighbor]:
                if g.has_edge(n, neighbor2):
                    ccs.add(tuple(sorted((n, neighbor, neighbor2))))

    return ccs

start = time.time()
with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

g = nx.Graph()
for l in lines:
    nodes = l.split('-')
    g.add_node(nodes[0])
    g.add_edge(nodes[0], nodes[1])

# p1
conn = sized_conn_comps(g)
total = 0

for a in conn:
    added = False
    for b in a:
        if b[0] == 't':
            if not added:
                total += 1
                added = True

print(f'p1: total - {total}, done in {time.time() - start}')

# p2
largest_cycle = max(nx.find_cliques(g), key=len)

str = ''
for c in sorted(largest_cycle):
    str += f'{c},'

print(f'p2: str - {str}, done in {time.time() - start}')

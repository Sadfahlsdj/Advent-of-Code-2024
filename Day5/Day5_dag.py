""" trying day 5 with a dag based solution instead of bruteforce"""
import networkx as nx

edges_filename, paths_filename = 'edges.txt', 'paths.txt'

with open(edges_filename) as f:
    e = list([l.strip() for l in f.readlines()])

with open(paths_filename) as f:
    p = list([l.strip() for l in f.readlines()])

dag = {}

for ed in e:
    n1, n2 = int(ed.split('|')[0]), int(ed.split('|')[1])
    if n1 in dag.keys():
        dag[n1].append(n2)
    else:
        dag[n1] = [n2]

dol = nx.from_dict_of_lists(dag, create_using=nx.DiGraph)

paths = []
for path in p:
    ns = [int(n) for n in path.split(',')]
    paths.append(ns)

total_p1, total_p2 = 0, 0

for path in paths:
    dag = dol.subgraph([p for p in path])
    l = list(nx.topological_sort(dag))

    # p1
    if l == path:
        total_p1 += path[int((len(path) - 1) / 2)]

    # p2
    if l != path:
        total_p2 += l[int((len(l) - 1) / 2)]

print(total_p1)
print(total_p2)
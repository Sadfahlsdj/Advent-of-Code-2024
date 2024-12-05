from graphlib import TopologicalSorter

edges, paths = 'edges.txt', 'paths.txt'

with open(edges) as f:
    e = list([l.strip() for l in f.readlines()])

with open(paths) as f:
    p = list([l.strip() for l in f.readlines()])

dag = {}

for ed in e:
    n1, n2 = int(ed.split('|')[0]), int(ed.split('|')[1])
    if n1 in dag.keys():
        dag[n1].append(n2)
    else:
        dag[n1] = [n2]

ps = []
for path in p:
    ns = [int(n) for n in path.split(',')]
    ps.append(ns)

total = 0

# p1
"""for pa in ps:
    valid = True
    for i in range(len(pa)):
        for j in range(i+1, len(pa)):
            if pa[i] in dag.keys():
                if pa[j] not in dag[pa[i]]:
                    valid = False
            else:
                valid = False

    if valid:
        print(pa)
        total += pa[int((len(pa) - 1) / 2)]"""

# p2
for pa in ps:
    # valid=False means that a swap had to be made, so we consider it
    valid = True
    for i in range(len(pa)):
        for j in range(i+1, len(pa)):
            if pa[i] in dag.keys():
                if pa[j] not in dag[pa[i]]:
                    if pa[i] in dag[pa[j]]:
                        pa[i], pa[j] = pa[j], pa[i]
                    valid = False
            else:
                valid = False
                if pa[i] in dag[pa[j]]:
                    pa[i], pa[j] = pa[j], pa[i]

    if not valid:
        print(pa)
        total += pa[int((len(pa) - 1) / 2)]

print(total)
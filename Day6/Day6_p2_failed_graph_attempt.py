import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

file_to_use = 'example.txt'
with open(file_to_use) as f:
    lines = [l.strip() for l in f.readlines()]

grid = [] # 0 = nothing, 1 = obstacle
guard_pos = np.array([0, 0])
guard_dir = np.array([-1, 0]) # direction guard is facing
for i in range(len(lines)):
    l = lines[i]
    row = []
    for j in range(len(l)):
        char = l[j]
        if char == '.':
            row.append(0)
        elif char == '#':
            row.append(1)
        else:
            row.append(0)
            guard_pos = [i, j]
    grid.append(row)

grid = np.array(grid)

dag = {}

while True:
    temp = guard_pos + guard_dir

    # if out of bounds, break
    if (temp[0] < 0 or temp[0] > (len(lines) - 1)
        or temp[1] < 0 or temp[1] > (len(lines[0]) - 1)):
        break
    if grid[tuple(temp)] == 1:
        # COULDN'T THINK OF A BETTER WAY TO CHANGE DIRECTION
        if np.array_equal(guard_dir, [-1, 0]):
            guard_dir = [0, 1]
        elif np.array_equal(guard_dir, [0, 1]):
            guard_dir = [1, 0]
        elif np.array_equal(guard_dir, [1, 0]):
            guard_dir = [0, -1]
        else:
            guard_dir = [-1, 0]

    new_loc = guard_pos + guard_dir
    gp_key, nl_val = tuple(guard_pos), tuple(new_loc) # list is unhashable
    if gp_key in dag.keys():
        dag[gp_key].append(nl_val)
    else:
        dag[gp_key] = [nl_val]
    guard_pos = new_loc

dol = nx.from_dict_of_lists(dag, create_using=nx.Graph)
cutsets = list(nx.all_node_cuts(dol))
print(cutsets)


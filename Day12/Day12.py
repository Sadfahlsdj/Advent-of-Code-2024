from itertools import chain

def get_neighbors(matrix, i, j, char):
    neighbors = []
    count = 0
    dirs = []

    # UP
    if (i > 0 and matrix[i - 1][j] == char):
        neighbors.append((i - 1, j))
        dirs.append((-1, 0))
        count += 1

    # LEFT
    if (j > 0 and matrix[i][j - 1] == char):
        neighbors.append((i, j - 1))
        dirs.append((0, -1))
        count += 1

    # DOWN
    if (i < len(matrix) - 1 and matrix[i + 1][j] == char):
        neighbors.append((i + 1, j))
        dirs.append((1, 0))
        count += 1

    # RIGHT
    if (j < len(matrix[0]) - 1 and matrix[i][j + 1] == char):
        neighbors.append((i, j + 1))
        dirs.append((0, 1))
        count += 1

    return (neighbors, count, dirs)


with open('example.txt') as f:
    lines = [[c for c in l.strip()] for l in f.readlines()]

unique = list(set(chain(*lines))) # unique values
groups = dict((k, []) for k in unique)
visited = set()
total_p1, total_p2 = 0, 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        discovered = False
        char = lines[i][j]

        if (i, j) in visited:
            # print(f'({i}, {j}) in {visited}')
            discovered = True

        if not discovered:
            group, neighbors = {(i, j)}, {(i, j)}
            count = (4 - get_neighbors(lines, i, j, char)[1])
            corners = 0
            visited_neighbors = set()

            while len(neighbors) > 0:
                curr = neighbors.pop()
                group.add(curr)
                visited.add(curr)

                for t in get_neighbors(lines, curr[0], curr[1], char)[0]:
                    if t not in group and t not in visited_neighbors:
                        neighbors.add(t)
                        visited_neighbors.add(t)
                        c = 4 - get_neighbors(lines, t[0], t[1], char)[1]
                        count += (c)
                        # print(f'char {lines[t[0]][t[1]]} with curr {curr} at position {t} has {c} perim')

            total_p1 += len(group) * count
            total_p2 += len(group) * corners
            groups[char].append(sorted(group))

print(groups)
print(total_p1)
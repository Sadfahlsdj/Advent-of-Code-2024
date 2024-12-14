from itertools import chain

def get_neighbors(m, i, j, char):
    """ m = input matrix, i,j are coords, char is char to search for"""
    neighbors = []
    count = 0
    dirs = []

    # UP
    if (i > 0 and m[i - 1][j] == char):
        neighbors.append((i - 1, j))
        dirs.append((-1, 0))
        count += 1

    # LEFT
    if (j > 0 and m[i][j - 1] == char):
        neighbors.append((i, j - 1))
        dirs.append((0, -1))
        count += 1

    # DOWN
    if (i < len(m) - 1 and m[i + 1][j] == char):
        neighbors.append((i + 1, j))
        dirs.append((1, 0))
        count += 1

    # RIGHT
    if (j < len(m[0]) - 1 and m[i][j + 1] == char):
        neighbors.append((i, j + 1))
        dirs.append((0, 1))
        count += 1

    surrounding = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (0 <= x < len(m)) and (0 <= y < len(m[0])):
                if (x == i and y == j):
                    continue
                surrounding.append(m[x][y])
            else:
                surrounding.append('-') # filler char to denote not valid

    # topleft, top, topright, left, right, botleft, bot, botright

    surr_truth = [c == char for c in surrounding]

    return (neighbors, count, surr_truth)

def get_corners(surr, count):
    """
    surr - array detailing which of surrounding 8 chars have the same value
    in order: 0: tl, 1: top, 2: tr, 3: left, 4: right, 5: bl, 6: bot, 7: br
    count - # of neighbors (not counting corners)
    """
    if count == 0: # no surrounding
        return 4
    elif sum(surr) == 8: # completely surrounded
        return 0
    elif sum(surr) == 1 and count == 1: # only surrounding is a singular neighbor
        return 2
    elif ((surr[1] and surr[6]) or (surr[3] and surr[4])) and sum(surr) == 2:
        # 2 opposite ones, no other surrounding
        return 0
    else:
        corners = 0
        # DISGUSTING CHUNGUS HARDCODE

        # 2 "adjacent" vertical/horizontal sides are not same char, this makes an inner corner
        if not surr[1] and not surr[3]:
            corners += 1
        if not surr[1] and not surr[4]:
            corners += 1
        if not surr[6] and not surr[3]:
            corners += 1
        if not surr[6] and not surr[4]:
            corners += 1

        # 2 "adjacent" vertical/horizontal sides are same char, corresponding corner is not
        if surr[1] and surr[3] and not surr[0]:  # top left
            corners += 1
        if surr[3] and surr[6] and not surr[5]:  # bot left
            corners += 1
        if surr[4] and surr[6] and not surr[7]:  # bot right
            corners += 1
        if surr[1] and surr[4] and not surr[2]:  # top right
            corners += 1

        if count == 1:
            # 1 adjacent vertical/horizontal and no connected corners
            # this means there are always just 2 corners, can return here
            if surr[1] and not surr[0] and not surr[2]:
                return 2
            if surr[6] and not surr[5] and not surr[7]:
                return 2
            if surr[3] and not surr[0] and not surr[5]:
                return 2
            if surr[4] and not surr[2] and not surr[7]:
                return 2

        if corners == 5: # sometimes corners = 5?? hacky time
            return 4
        return corners


with open('input.txt') as f:
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
            count = (4 - get_neighbors(lines, i, j, char)[1]) # p1
            corners = get_corners(get_neighbors(lines, i, j, char)[2], count)
            print(f'first corner {char} at {i}, {j} has {corners} corners')
            visited_neighbors = set()

            while len(neighbors) > 0:
                curr = neighbors.pop()
                group.add(curr)
                visited.add(curr)

                for t in get_neighbors(lines, curr[0], curr[1], char)[0]:
                    if t not in group and t not in visited_neighbors:
                        neighbors.add(t)
                        visited_neighbors.add(t)
                        neighbor_count = get_neighbors(lines, t[0], t[1], char)[1]
                        c = 4 - neighbor_count

                        # p1
                        count += (c)

                        # p2
                        surr = get_neighbors(lines, t[0], t[1], char)[2]
                        print(f'char {lines[t[0]][t[1]]} with curr {curr} at position {t} has {surr} '
                              f'surrounding with {get_corners(surr, neighbor_count)} corners '
                              f'and count {neighbor_count}')
                        corners += get_corners(surr, neighbor_count)

                        # print(f'char {lines[t[0]][t[1]]} with curr {curr} at position {t} has {c} perim')

            total_p1 += len(group) * count
            total_p2 += len(group) * corners
            print(f'char {char} has {corners} corners')
            groups[char].append(sorted(group))

print(total_p2)
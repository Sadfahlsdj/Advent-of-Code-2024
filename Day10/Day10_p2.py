with open('input.txt') as f:
    lines = [[int(c) for c in l.strip()] for l in f.readlines()]

trailheads = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 0:
            trailheads.append((i, j))

total = 0
for t in trailheads:
    count = 0
    current, current_val = [t], 0
    paths = []
    paths.append([t]) # initialize paths

    while current_val < 9:
        for c in paths:
            print(f'initial c: {c}')
            # up, down, left, right in order of c[-1] (most recent entry in path)
            initial = ((c[-1][0] - 1, c[-1][1]), (c[-1][0] + 1, c[-1][1]),
                       (c[-1][0], c[-1][1] - 1), (c[-1][0], c[-1][1] + 1))

            avail = set(initial)
            print(f'step 1 - c: {c}, avail: {avail}')

            # remove entries outside bounds of graph
            avail = [a for a in avail if (not a[0] < 0 and a[0] < len(lines)
                                          and not a[1] < 0 and a[1] < len(lines[0]))]
            print(f'step 2 - c: {c}, avail: {avail}')

            # repopulate array with entries that correspond to the correct value in graph
            avail = [a for a in avail if lines[a[0]][a[1]] == current_val + 1]
            print(f'step 3 - c: {c}, avail: {avail}')

            # remove current value from paths, add all new ones
            paths = [cu for cu in paths if cu != c]
            for a in avail:
                temp = [pair for pair in c]
                temp.append(a)
                paths.append(tuple(temp))

            paths = list(set(paths)) # remove dupes

        if current_val + 1 == 9:
            total += len(set(paths)) # if new path heads correspond to 9, add 1 for every path

        print(f'paths: {paths}, current_val: {current_val}')
        current_val += 1

print(total)



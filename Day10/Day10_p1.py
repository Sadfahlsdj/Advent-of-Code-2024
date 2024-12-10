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
    endpoints = set() # list of endpoints from current trailhead

    while current_val < 9:
        for c in current:
            # up, down, left, right in order
            initial = (c[0] - 1, c[1]), (c[0] + 1, c[1]), (c[0], c[1] - 1), (c[0], c[1] + 1)
            avail = set(initial) # use set for runtime
            print(f'step 1 - c: {c}, avail: {avail}')

            # remove ones that go beyond graph boundaries
            avail = [a for a in avail if (not a[0] < 0 and a[0] < len(lines)
                                          and not a[1] < 0 and a[1] < len(lines[0]))]
            print(f'step 2 - c: {c}, avail: {avail}')

            # remove ones that do not correspond to the correct value in graph
            avail = [a for a in avail if lines[a[0]][a[1]] == current_val + 1]
            print(f'step 3 - c: {c}, avail: {avail}')

            # update current array by removing value being iterated over and adding all of avail
            current = [cu for cu in current if cu != c] #
            for a in avail:
                current.append(a)

            current = list(set(current)) # remove dupes
            print(f'current: {current}, current_val: {current_val}')

            if current_val + 1 == 9:
                for a in avail:
                    endpoints.add(a) # if "avail" values correspond to 9, add avail values to set
                print(f'at endpoints, adding avail = {avail}')

        current_val += 1
    total += len(endpoints)

print(total)



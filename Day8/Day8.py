with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

chars = set()
for l in lines:
    unique = set(l)
    for u in unique:
        chars.add(u)

chars.remove('.')
locs = {c: set() for c in chars}

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            locs[lines[i][j]].add((i, j))

antinodes = set()
for c in chars:
    loc = list(locs[c])
    for i in range(len(loc)):
        for j in range(i+1, len(loc)):
            # print(f'{loc[i]} {loc[j]}')
            diff_x, diff_y = loc[i][0] - loc[j][0], loc[i][1] - loc[j][1]

            # p1
            """antinodes.add((loc[i][0] + diff_x, loc[i][1] + diff_y))
            antinodes.add((loc[j][0] - diff_x, loc[j][1] - diff_y))"""

            # p2
            new_x, new_y = loc[i][0], loc[i][1]

            while (0 <= new_x < len(lines)) and (0 <= new_y < len(lines[0])):
                print(f'positive - current: {new_x}, {new_y} direction - {diff_x}, {diff_y}')
                antinodes.add((new_x, new_y))
                new_x += diff_x
                new_y += diff_y

            new_x, new_y = loc[i][0], loc[i][1]
            while (0 <= new_x < len(lines)) and (0 <= new_y < len(lines[0])):
                print(f'negative - current: {new_x}, {new_y} direction - {diff_x}, {diff_y}')
                antinodes.add((new_x, new_y))
                new_x -= diff_x
                new_y -= diff_y

# remove ones outside grid
antinodes = [a for a in antinodes if not (a[0] < 0 or a[0] >= len(lines)
                                          or a[1] < 0 or a[1] >= len(lines[0]))]

print(len(antinodes))
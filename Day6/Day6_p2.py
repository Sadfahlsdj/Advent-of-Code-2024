file_to_use = 'input.txt'
with open(file_to_use) as f:
    lines = [l.strip() for l in f.readlines()]

grid = [] # 0 = nothing, 1 = obstacle
grid_chars = [list(l) for l in lines]

guard_pos = [0, 0]
guard_dir = [-1, 0] # direction guard is facing
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

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def cycle(guard_pos, grid):
    visited_directed = set()  # list of tuples from source -> target positions
    dir_index = 0

    while True:
        visited_key = tuple([tuple(guard_pos), dir_index])
        if visited_key in visited_directed:
            return True
        guard_dir = DIRS[dir_index]
        temp = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        # if out of bounds, break
        if (temp[0] < 0 or temp[0] > (len(lines) - 1)
            or temp[1] < 0 or temp[1] > (len(lines[0]) - 1)):
            return False
        if grid[temp[0]][temp[1]] == '#':
            dir_index = (dir_index + 1) % len(DIRS)
        else:
            guard_pos = temp
            visited_directed.add(visited_key)

looping = 0

guard_pos_og = guard_pos
iteration = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid_chars[i][j] == '.':
            grid_chars[i][j] = '#'
            looping += cycle(guard_pos_og, grid_chars)
            grid_chars[i][j] = '.'

        iteration += 1
        print(f'iteration: {iteration} looping: {looping}')

print(looping)
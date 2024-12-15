import copy

grid_file, moves_file = 'input_grid.txt', 'input_moves.txt'

with open(grid_file) as f:
    grid = [list(l.strip()) for l in f.readlines()]

with open(moves_file) as f:
    moves = f.read().replace('\n', '').strip()

def move(x, y, dir, grid):
    og_grid = copy.deepcopy(grid)
    if dir == '<':
        newx, newy = x, y - 1
    elif dir == '>':
        newx, newy = x, y + 1
    elif dir == '^':
        newx, newy = x - 1, y
    else:
        newx, newy = x + 1, y

    if grid[newx][newy] == '.': # empty tile
        grid[newx][newy] = '@'
        grid[x][y] = '.'
        return (newx, newy)

    elif grid[newx][newy] == '#': # wall tile
        return (x, y)

    else: # obstacle
        d = (newx - x, newy - y)
        box_count = 1

        iterx, itery = newx + d[0], newy + d[1]
        while grid[iterx][itery] == 'O':
            box_count += 1
            iterx, itery = iterx + d[0], itery + d[1]

        if grid[iterx][itery] == '#':
            return (x, y)

        grid[x][y] = '.'
        grid[newx][newy] = '@'
        for i in range(1, box_count + 1):
            grid[newx + i * d[0]][newy + i * d[1]] = 'O'

        return (newx, newy)

def diagnostic_print(grid, bot_pos):
    d = '-' * (len(grid[0]) * 10)
    print(d)
    for g in grid:
        print(g)
    print(f'bot_pos: {bot_pos}')
    print(d)

start_pos = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            start_pos = (i, j)

iter = 0
bot_pos = copy.deepcopy(start_pos)
for m in moves:
    # diagnostic_print(grid, bot_pos)
    bot_pos = move(bot_pos[0], bot_pos[1], m, grid)
    print(f'iter {iter} of {len(moves)}')
    iter += 1

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            total += (100 * i) + j

print(total)
"""NOTE - EVERYTHING IS FLIPPED FOR X AND Y VALUES, JUST ROLL WITH IT"""

def draw_pos(dim_x, dim_y, pos):
    pos = sorted(pos)
    for i in range(dim_x):
        s = ''
        for j in range(dim_y):
            if (i, j) in pos:
                s += 'X'
            else:
                s += '*'

        print(s)


with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

dim_x, dim_y = 101, 103 # (101, 103) for actual, (11, 7) for example

pos, vel = [], []

for l in lines:
    p, v = l.split('=')[1].strip(), l.split('=')[2].strip()
    vels = tuple([int(a) for a in v.split(',')])

    poss = tuple([int(p.split(',')[0]), int(p.split(',')[1].split()[0])])
    """poss.append(int(p.split(',')[0]))
    poss.append(int(p.split(',')[1].split()[0]))"""

    pos.append(poss)
    vel.append(vels)

for i in range(1, 30000):
    for j in range(len(pos)):
        x_pos, y_pos = pos[j][0] + vel[j][0], pos[j][1] + vel[j][1]
        if x_pos < 0:
            x_pos = dim_x + x_pos
        elif x_pos >= dim_x:
            x_pos = x_pos % dim_x
        if y_pos < 0:
            y_pos = dim_y + y_pos
        elif y_pos >= dim_y:
            y_pos = y_pos % dim_y

        pos[j] = (x_pos, y_pos)

    if len(set(pos)) == len(pos):
        print(i)
        draw_pos(dim_x, dim_y, set(pos))

tl, tr, bl, br = 0, 0, 0, 0
x_mid, y_mid = int(dim_x / 2), int(dim_y / 2)
for p in pos:
    x, y = p[0], p[1]
    if x < x_mid and y < y_mid:
        tl += 1
    elif x > x_mid and y < y_mid:
        tr += 1
    elif x > x_mid and y > y_mid:
        br += 1
    elif x < x_mid and y > y_mid:
        bl += 1

print(tl * tr * bl * br)








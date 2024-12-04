with open('input.txt') as f:
    rows = [r.strip() for r in f.readlines()]

total = 0
for x in range(len(rows)):
    for y in range(len(rows[0])):
        if rows[x][y] == 'X':
            up, down, left, right = 'X', 'X', 'X', 'X'
            ul, ur, dl, dr = 'X', 'X', 'X', 'X'

            try:
                if (y - 3) >= 0:
                    left += rows[x][y-1]
                    left += rows[x][y - 2]
                    left += rows[x][y - 3]
            except:
                pass

            try:
                right += rows[x][y+1]
                right += rows[x][y+2]
                right += rows[x][y+3]
            except:
                pass

            try:
                if (x - 3) >= 0:
                    up += rows[x-1][y]
                    up += rows[x-2][y]
                    up += rows[x-3][y]
            except:
                pass

            try:
                down += rows[x+1][y]
                down += rows[x+2][y]
                down += rows[x+3][y]
            except:
                pass

            try:
                if (y - 3) >= 0 and (x - 3) >= 0:
                    ul += rows[x-1][y-1]
                    ul += rows[x-2][y-2]
                    ul += rows[x-3][y-3]
            except:
                pass

            try:
                if (x - 3) >= 0:
                    ur += rows[x - 1][y + 1]
                    ur += rows[x - 2][y + 2]
                    ur += rows[x - 3][y + 3]
            except:
                pass

            try:
                dr += rows[x+1][y + 1]
                dr += rows[x+2][y + 2]
                dr += rows[x+3][y + 3]
            except:
                pass

            try:
                if (y - 3) >= 0:
                    dl += rows[x + 1][y-1]
                    dl += rows[x + 2][y-2]
                    dl += rows[x + 3][y-3]
            except:
                pass

            """print(f'{x} {y}')
            print(f'up: {up} down: {down} left: {left} right: {right} '
                  f'dr: {dr} dl: {dl} ur: {ur} ul: {ul}')"""
            words = [up, down, left, right, dr, dl, ur, ul]
            total += words.count('XMAS')
            total += words.count('SAMX')

print(total)



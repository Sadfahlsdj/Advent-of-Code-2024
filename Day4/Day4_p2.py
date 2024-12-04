with open('input.txt') as f:
    rows = [r.strip() for r in f.readlines()]

total = 0
for x in range(len(rows)):
    for y in range(len(rows[0])):
        if rows[x][y] == 'A':
            dr, ul = '', ''
            try:
                if (y - 1) >= 0 and (x - 1) >= 0:
                    dr += rows[x-1][y-1]
                    dr += rows[x][y]
                    dr += rows[x+1][y+1]
            except:
                pass

            try:
                if (y - 1) >= 0 and (x - 1) >= 0:
                    ul += rows[x - 1][y + 1]
                    ul += rows[x][y]
                    ul += rows[x + 1][y - 1]
            except:
                pass


            """print(f'{x} {y}')
            print(f'dr: {dr}, ul: {ul}')"""

            if (dr == 'MAS' or dr == 'SAM') and (ul == 'MAS' or ul == 'SAM'):
                total += 1

print(total)



with open('example2.txt') as f:
    rows = [r.strip() for r in f.readlines()]

cols = []
for i in range(len(rows[0])):
    # each column as a single string
    cols.append(''.join(list(r[i] for r in rows)))

with open('example_cols', 'w') as f:
    for c in cols:
        f.write(c + '\n')

def remove_reversed_strings(lst):
    """Removes strings from the list that are the reverse of another string."""

    result = []
    seen = set()

    for string in lst:
        reversed_string = string[::-1]
        if reversed_string not in seen:
            result.append(string)
            seen.add(string)

    return result
def get_diag(arr, offset, dir):
    """ dir should be dr for downright facing or ul for upleft facing"""
    str1, str2 = '', ''

    if dir == 'dr':
        for i in range(len(arr)):
            if (offset + i) < 0:
                break
            try:
                str1 += arr[offset + i][i]
                str2 += arr[i][offset + i]
            except:
                pass


    elif dir == 'ul':
        for i in reversed(range(len(arr))):
            if (i - offset) < 0: # going to negative indices screws it up
                break
            try:
                str1 += arr[i - offset][len(arr[0]) - 1 - i]
                str2 += arr[len(arr[0]) - 1 - i][i - offset]
            except:
                pass

    return (str1, str2)

diags = []
for i in range(len(rows)):
    diags.append(get_diag(rows, i, 'dr')[0])
    diags.append(get_diag(rows, i, 'dr')[1])
    diags.append(get_diag(rows, i, 'ul')[0])
    diags.append(get_diag(rows, i, 'ul')[1])

# diags = remove_reversed_strings(diags)
diags = list(set(diags))

count = 0
words = cols + rows + diags

for w in words:
    xmas, samx = w.count('XMAS'), w.count('SAMX')
    count += xmas
    count += samx

    print(f'{w}: {xmas} {samx}')

print(len(words))
print(count)



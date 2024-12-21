import copy

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def find_char(c, l):
    for i, sublist in enumerate(l):
        for j, ch in enumerate(sublist):
            if ch == c:
                return (i, j)

    return 'not found'

def generate_path(target_grid, input_list, curr, dtype):
    """

    :param target_grid: grid to search for chars on
    :param input_list: sequence to search on
    :param curr: starting position
    :param dtype: int or str to decide whether to cast or not
    :return:
    """
    seq = []
    for i, char in enumerate(input_list):
        if dtype == 'int':
            target_pos = find_char(int(char), target_grid)
        else:
            target_pos = find_char(char, target_grid)

        if i < len(input_list) - 1:
            print(f'current = {curr}, next = {target_pos}')

        while curr != target_pos:
            if curr[0] != target_pos[0]:
                if curr[0] > target_pos[0]:
                    curr = (curr[0] - 1, curr[1])
                    seq.append('^')
                else:
                    curr = (curr[0] + 1, curr[1])
                    seq.append('v')

            elif curr[1] != target_pos[1]:
                if curr[1] > target_pos[1]:
                    curr = (curr[0], curr[1] - 1)
                    seq.append('<')
                else:
                    curr = (curr[0], curr[1] + 1)
                    seq.append('>')
        seq.append('A')

    return seq


g_numbers = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, 1000]]
g_dir = [['-', '^', 'A'], ['<', 'v', '>']]

total = 0
for i, l in enumerate(lines):
    initial_n, initial_g = (3, 2), (0, 2)
    seq_n = list(l)
    seq_n[seq_n.index('A')] = 1000
    curr_n, curr_g = initial_n, initial_g

    seq_g1 = generate_path(g_numbers, seq_n, curr_n, 'int')
    seq_g2 = generate_path(g_dir, seq_g1, copy.deepcopy(curr_g), 'str')
    print(f'starting g3 on index {i}')
    seq_g3 = generate_path(g_dir, seq_g2, copy.deepcopy(curr_g), 'str')

    print((''.join([c for c in seq_g3])))

    value = int(''.join([ch for ch in l if ch.isnumeric()]))
    total += len(seq_g3) * value
    print(f'for input {l} value is {value} and len is {len(seq_g3)}')

print('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A') # correct 5th
print(total)

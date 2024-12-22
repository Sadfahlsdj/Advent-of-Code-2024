import copy
import itertools

with open('example.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def find_char(c, l):
    for i, sublist in enumerate(l):
        for j, ch in enumerate(sublist):
            if ch == c:
                return (i, j)

    return 'not found'

def find_all_paths(src, targ):
    """

    :param src: source coords as tuple(x, y)
    :param targ: target coords as tuple(x, y)
    :return: list of all possible moves - etc ['<^', '^<']
    """

    moves = ''
    diff = (targ[0] - src[0], targ[1] - src[1])

    if diff[0] > 0:
        moves += diff[0] * 'v'
    elif diff[0] < 0:
        moves += abs(diff[0]) * '^'

    if diff[1] > 0:
        moves += diff[1] * '>'
    elif diff[1] < 0:
        moves += abs(diff[1]) * '<'

    return [list(l) for l in list(set(itertools.permutations(moves)))]

def generate_path(target_grid, input_list, curr, dtype, memo):
    """

    :param target_grid: grid to search for chars on
    :param l: list of possible input sequences to search on
    :param curr: starting position
    :param dtype: int or str to decide whether to cast or not
    :return: all possible output strings given all possible input strings
    """
    seq = []
    for ind, l in enumerate(input_list):
        if tuple(l) in memo:
            seq += memo[l]
        else:
            temp = [[]]
            for i, char in enumerate(l):
                temp2 = []
                if dtype == 'int':
                    target_pos = find_char(int(char), target_grid)
                else:
                    target_pos = find_char(char, target_grid)

                if curr == target_pos:
                    possible = [['A']]
                else:
                    possible = find_all_paths(curr, target_pos)
                    possible = [p + ['A'] for p in possible]

                for t in temp:
                    for p in possible:
                        temp2.append(t + p)


                temp = temp2
                curr = target_pos

            memo[tuple(l)] = temp
            seq += temp
        """min_len = min([len(x) for x in seq])
        seq = [s for s in seq if len(s) == min_len]"""
        print(f'iteration {ind} of {len(input_list)}, seq has len {len(seq)}')

    min_len = min([len(x) for x in seq])
    seq = [s for s in seq if len(s) == min_len]
    return seq

def main():
    g_numbers = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, 1000]]
    g_dir = [['-', '^', 'A'], ['<', 'v', '>']]
    memo = {}

    total = 0
    for i, l in enumerate(lines):
        initial_n, initial_g = (3, 2), (0, 2)
        seq_n = list(l)
        seq_n[seq_n.index('A')] = 1000
        seq_n = [seq_n]
        curr_n, curr_g = initial_n, initial_g

        seq_g1 = generate_path(g_numbers, seq_n, curr_n, 'int', memo)
        print('g1 done')
        seq_g2 = generate_path(g_dir, seq_g1, copy.deepcopy(curr_g), 'str', memo)
        print('g2 done')
        seq_g3 = generate_path(g_dir, seq_g2, copy.deepcopy(curr_g), 'str', memo)

        shortest_sublist = min(seq_g3, key=len)
        # print((''.join([c for c in longest_sublist])))

        value = int(''.join([ch for ch in l if ch.isnumeric()]))
        total += len(shortest_sublist) * value
        print(f'for input {l} value is {value} and len is {len(shortest_sublist)}')

    print(total)

if __name__ == '__main__':
    main()
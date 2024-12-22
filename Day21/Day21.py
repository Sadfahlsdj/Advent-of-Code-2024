import copy
import itertools
import networkx as nx

with open('example.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def find_all_paths(src, targ, grid):
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

def generate_path(target_map, target_grid, input_list, curr, possible):
    """

    :param target_map: map listing which chars are in which position in a grid
    :param l: list of possible input sequences to search on
    :param curr: starting position
    :param possible: possible outcomes at this stage
    :param iter: crap for diagnostics
    :return: all possible output strings given all possible input strings
    """
    if len(input_list) == 0:
        return possible

    temp, temp2 = [], []
    target_pos = target_map[input_list[0]]
    if curr == target_pos:
        temp = [['A']]
    else:
        po = find_all_paths(curr, target_pos, target_grid)
        temp = [p + ['A'] for p in po]

    for t in temp:
        for p in possible:
            temp2.append(p + t)

    return generate_path(target_map, target_grid, input_list[1:], target_pos, temp2)


def main():
    n_map = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2),
             '1': (2, 0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
    d_map = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
    g_numbers = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [-1, 0, 1000]]
    g_dir = [['-', '^', 'A'], ['<', 'v', '>']]

    # NETWORKX GRAPH CREATION IGNORE IGNORE IGNORE
    memo = {}

    total = 0
    for i, l in enumerate(lines):
        initial_n, initial_g = (3, 2), (0, 2)
        seq_n = list(l)
        seq_n = [seq_n]
        curr_n, curr_g = initial_n, initial_g

        # returns a list nested 3 times instead of 2 times, so take 0th ind in each step
        seq_g1 = [generate_path(n_map, g_numbers, s, curr_n, [[]]) for s in seq_n][0]
        seq_g2 = [generate_path(d_map, g_dir, s, copy.deepcopy(curr_g), [[]])
                  for s in seq_g1][0]
        seq_g3 = [generate_path(d_map, g_dir, s, copy.deepcopy(curr_g), [[]],
                    ) for s in seq_g2][0]

        shortest_sublist = min(seq_g3, key=len)
        # print((''.join([c for c in longest_sublist])))

        value = int(''.join([ch for ch in l if ch.isnumeric()]))
        total += len(shortest_sublist) * value
        print(f'for input {l} value is {value} and len is {len(shortest_sublist)}')

    print(total)

if __name__ == '__main__':
    main()
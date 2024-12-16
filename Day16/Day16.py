import copy

with open('example.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

start_pos, end_pos = [0, 0], [0, 0]

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'S':
            start_pos = [i, j]
        if lines[i][j] == 'E':
            end_pos = [i, j]

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dir = 0 # starting dir is east

pos = copy.deepcopy(start_pos)

sequences = [[]]
positions = [(pos)] # will sync with sequences
seq_dirs = [dir]

found = False

while not found:
    seqs_to_remove = []
    seqs_to_append, pos_to_append, dirs_to_append = [], [], []
    for i in range(len(sequences)):
        curr_pos = positions[i]
        d = dirs[seq_dirs[i]]
        left_dir = dirs[(seq_dirs[i] + 1) % 4]
        right_dir = dirs[(seq_dirs[i] - 1) % 4]

        if lines[curr_pos[0] + d[0]][curr_pos[1] + d[1]] == '.':
            sequences[i].append('f')
            positions[i] = [positions[i][0] + dirs[dir][0], positions[i][1] + dirs[dir][1]]

        if lines[curr_pos[0] + left_dir[0]][curr_pos[1] + left_dir[1]] == '.':
            temp_seq = copy.deepcopy(sequences[i])
            temp_seq.append('l')
            seqs_to_append.append(temp_seq)
            pos_to_append.append([curr_pos[0] + left_dir[0], curr_pos[1] + left_dir[1]])
            dirs_to_append.append((dir + 1) % 4)

        if lines[curr_pos[0] + right_dir[0]][curr_pos[1] + right_dir[1]] == '.':
            temp_seq = copy.deepcopy(sequences[i])
            temp_seq.append('r')
            seqs_to_append.append(temp_seq)
            pos_to_append.append([curr_pos[0] + right_dir[0], curr_pos[1] + right_dir[1]])
            dirs_to_append.append((dir - 1) % 4)

    sequences = [s for s in sequences if s not in seqs_to_remove]
    for s in zip(seqs_to_append, pos_to_append, dirs_to_append):
        print(f'a: {s}')



print(sequences)
print(positions)
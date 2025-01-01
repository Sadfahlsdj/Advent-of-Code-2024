initial_filename, conns_filename = 'input_initial.txt', 'input_connections.txt'

with open(initial_filename) as f:
    vals = dict([(l.split(':')[0], int(l.split(':')[1].strip())) for l in f.readlines()])

with open(conns_filename) as f:
    connections_raw = [l.strip() for l in f.readlines()]

conns = {}
for c in connections_raw:
    op = ''.join([ch for ch in c if ch.isupper()])
    inp1, inp2 = c.split(op)[0].strip(), c.split(op)[1].strip()[:3]
    out = c[-3:]
    conns[out] = (inp1, inp2, op) # input parsing

    if inp1 not in vals:
        vals[inp1] = -1
    if inp2 not in vals:
        vals[inp2] = -1
    if out not in vals:
        vals[out] = -1

    # print(f'{inp1} {op} {inp2}: {out}')

while -1 in vals.values():
    for k, v in conns.items(): # v is (input1, input2, operation)
        v1, v2, op, o = vals[v[0]], vals[v[1]], v[2], vals[k]
        if v1 != -1 and v2 != -1 and o == -1:
            if op == 'AND':
                vals[k] = v1 & v2
            elif op == 'OR':
                vals[k] = v1 | v2
            elif op == 'XOR':
                vals[k] = v1 ^ v2

final = []
for k, v in sorted(vals.items()):
    if 'z' in k:
        final.insert(0, v)

print(int(''.join([str(c) for c in final]), 2))

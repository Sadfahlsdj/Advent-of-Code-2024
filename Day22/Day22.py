""" expect runtime of ~5 minutes on the input it's not pretty"""

with open('input.txt') as f:
    lines = [int(l.strip()) for l in f.readlines()]

def find_common_sublists(inputs):
    """ ignore, misread problem statement :D"""
    # only care about length 4
    ret = []

    for i in range(len(inputs[0]) - 3):
        sublist = inputs[0][i:i + 4]

        all_has = True
        for inp in inputs:
            if (not any(inp[idx: idx + len(sublist)] == sublist
          for idx in range(len(inp) - 3))):
                all_has = False

        if all_has:
            ret += sublist

    return ret

def find_first_sublist(sublist, l):
    sll = len(sublist)
    for ind in (i for i,e in enumerate(l) if e == sublist[0]):
        if l[ind:ind + sll] == sublist:
            return ind

    return 'not found'
def try_all_sublists(ones, changes):
    """ will only work under the assumption that the best sublist is in the first list of changes
    DISGUSTING CHUNGUS HARDCODE"""
    vals = []
    for i in range(len(changes[0]) - 3):
        sublist = changes[0][i:i + 4]
        temp = 0

        for ind, o in enumerate(ones):
            first_sl_ind = find_first_sublist(sublist, changes[ind])
            if first_sl_ind != 'not found':
                temp += o[first_sl_ind + 4]

        vals.append(temp)
        print(f'iter {i} of {len(changes[0]) - 3}')

    return max(vals)
def mix(n, inp):
    return n ^ inp

def prune(inp):
    return inp % 16777216
def secret_number(inp, loops):
    nums = [inp]
    ones = [inp % 10]
    changes = []
    for i in range(loops):
        n1 = prune(mix(64 * inp, inp))
        n2 = prune(mix(int(n1 / 32), n1))
        n3 = prune(mix(2048 * n2, n2))
        inp = n3

        nums.append(inp)
        if i < loops - 1: # ignore last one
            changes.append((inp % 10) - ones[-1])
        ones.append(inp % 10)

    return nums, ones, changes

def main():
    total = 0 # p1
    vals, ones, changes = [], [], []
    for l in lines:
        n, o, c = secret_number(l, 2000)
        vals.append(n)
        ones.append(o)
        changes.append(c)

    # p1 answer will just be vals[-1]

    print(try_all_sublists(ones, changes))


if __name__ == '__main__':
    main()




import copy

def recurse(total_str, ipts, memo):
    """
    :param total_str: input string
    :param ipts: input substrings
    :param memo: dict for memoization
    :return: # of substrings that are in the input
    """

    total = 0
    if total_str == '':
        return 0

    if total_str in ipts:
        total += 1

    if total_str in memo.keys():
        # print(f'string {str} has cached value {memo[str]}')
        return memo[total_str]

    for i in ipts:
        if total_str.startswith(i):
            total += recurse(total_str[len(i):], ipts, memo)

    memo[total_str] = total
    return total

with open('input.txt') as f:
    lines = f.readlines()

    inputs = [w.strip() for w in lines[0].split(',')]
    towels = [w.strip() for w in lines[2:]]

total_p1 = 0
total_p2 = 0
memo = {}
for t in towels:
    r = recurse(t, inputs, memo)
    print(f'input: {t}, recursion output: {r}')
    if r > 0:
        total_p1 += 1

    total_p2 += r

print(total_p1)
print(total_p2)
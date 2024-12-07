def extract_col(idx, l):
    return [s[idx] for s in l]

def replace(old, new, string, idx):
    keylen = len(old)
    if idx == 0:
        new_mol = new + string[idx + keylen:]
    elif len(string) > idx + keylen:
        new_mol = string[0:idx] + new + string[idx + keylen:]
    else:
        new_mol = string[0:idx] + new

    return new_mol

def max_all(list):
    output = []
    max_len = 0

    for s in list:
        if len(s) > max_len:
            if len(output) == 0:
                output.append(s)
                continue

            prev_max = len(max(output, key=len))
            if len(s) > prev_max:
                output = [s]
            elif len(s) == prev_max:
                output.append(s)

    return output

def main():
    a = ['a', 'b', 'cd', 'def']
    b = ['a', 'ab', 'ba', 'cdd', 'def']

    print(max_all(a))
    print(max_all(b))

if __name__ == '__main__':
    main()
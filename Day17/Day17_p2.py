def extract_operand_value(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c

with open('example.txt') as f:
    lines = f.readlines()
    a = int(''.join([char for char in lines[0] if char.isnumeric()]))
    b = int(''.join([char for char in lines[1] if char.isnumeric()]))
    c = int(''.join([char for char in lines[2] if char.isnumeric()]))

    ops = [int(sp[-1]) for sp in lines[4].split(',')]

ind = 0
outputs = []

while ind < (len(ops) - 1):
    opcode, lit_op = ops[ind], ops[ind + 1]
    combo_op = extract_operand_value(lit_op)

    print(f'opcode = {opcode}, lit = {lit_op}, combo = {combo_op}')
    if opcode == 0:
        print(f'changing a from {a} to {int(a / (2 ** combo_op))}')
        a = int(a / (2 ** combo_op))
    elif opcode == 1:
        print(f'changing b from {b} to {b ^ lit_op}')
        b = b ^ lit_op
    elif opcode == 2:
        print(f'changing {b} from {b} to {combo_op % 8}')
        b = combo_op % 8
    elif opcode == 3:
        if a == 0:
            print(f'value 3 and a=0, skipping')
            pass
        else:
            print(f'changing index to {lit_op}')
            ind = lit_op - 2 # to offset it increasing by 2 always
    elif opcode == 4:
        print(f'changing {b} to {b ^ c}')
        b = b ^ c
    elif opcode == 5:
        print(f'outputting {combo_op % 8}')
        outputs.append(combo_op % 8)
    elif opcode == 6:
        print(f'changing {b} to {int(a / (2 ** combo_op))}')
        b = int(a / (2 ** combo_op))
    elif opcode == 7:
        print(f'changing {c} to {int(a / (2 ** combo_op))}')
        c = int(a / (2 ** combo_op))

    ind += 2

s = ''
for o in outputs:
    s += f'{o},'

print(s)


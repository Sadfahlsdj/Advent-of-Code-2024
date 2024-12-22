with open('input.txt') as f:
    lines = f.readlines()
    a = int(''.join([char for char in lines[0] if char.isnumeric()]))
    b = int(''.join([char for char in lines[1] if char.isnumeric()]))
    c = int(''.join([char for char in lines[2] if char.isnumeric()]))

    ops = [int(sp[-1]) for sp in lines[4].split(',')]



def extract_operand_value(operand):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c

ind = 0
outputs = []

while ind < (len(ops) - 1):
    opcode, lit_operand = ops[ind], ops[ind + 1]
    combo_op = extract_operand_value(lit_operand)

    print(f'opcode = {opcode}, lit = {lit_operand}, combo = {combo_op}')
    if opcode == 0:
        a = int(a / (2 ** combo_op))
    elif opcode == 1:
        b = b ^ lit_operand
    elif opcode == 2:
        b = combo_op % 8
    elif opcode == 3:
        if a == 0:
            pass
        else:
            ind = lit_operand - 2 # to offset it increasing by 2 always
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        outputs.append(combo_op % 8)
    elif opcode == 6:
        b = int(a / (2 ** combo_op))
    elif opcode == 7:
        c = int(a / (2 ** combo_op))

    ind += 2
    print(ind)

s = ''
for o in outputs:
    s += f'{o},'

print(s)


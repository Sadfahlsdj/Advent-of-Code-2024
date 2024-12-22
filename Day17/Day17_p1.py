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

looping = False

while ind < (len(ops) - 1):
    opcode, lit_operand = ops[ind], ops[ind + 1]
    combo_op = extract_operand_value(lit_operand)

    if opcode == 0:
        a = int(a / (2 ** combo_op))
        if not looping:
            print(f'setting a to a divided by 2 to the power of {combo_op}')
    elif opcode == 1:
        b = b ^ lit_operand
        if not looping:
            print(f'setting b to b xor {lit_operand}')
    elif opcode == 2:
        b = combo_op % 8
        if not looping:
            print(f'setting b to {combo_op} modulo 8')
    elif opcode == 3:
        if a == 0:
            print(f'skipping')
            looping = False
        else:
            ind = lit_operand - 2 # to offset it increasing by 2 always
            looping = True
            print(f'changing index to {lit_operand}')
    elif opcode == 4:
        b = b ^ c
        if not looping:
            print('changing b to b xor c')
    elif opcode == 5:
        outputs.append(combo_op % 8)
        print(f'outputting {combo_op} % 8, looping is {looping}')
    elif opcode == 6:
        b = int(a / (2 ** combo_op))
        if not looping:
            print(f'setting b to a divided by 2 to the power of {combo_op}')
    elif opcode == 7:
        if not looping:
            print(f'setting c to a divided by 2 to the power of {combo_op}')

    ind += 2

s = ''
for o in outputs:
    s += f'{o},'

print(s)


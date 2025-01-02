with open("inputs/input17.txt") as ifile:
    REGS, PROG = ifile.read().split("\n\n")
    REGS = {r.split(':')[0].split(" ")[1]: int(r.split(':')[1])
            for r in REGS.split("\n")}
    PROG = list(map(int, PROG.split(":")[1].strip().split(',')))


def get_combo(o: int, regs: dict) -> int:
    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: 'A', 5: 'B', 6: 'C', 7: None}
    v = combo[o]
    if isinstance(v, str):
        v = regs[v]
    return v


def adv(operand: int, regs: dict):
    v = get_combo(operand, regs)
    regs['A'] = int(regs['A']/(2**v))


def bxl(operand: int, regs: dict):
    regs['B'] = regs['B'] ^ operand


def bst(operand: int, regs: dict):
    v = get_combo(operand, regs)
    regs['B'] = v % 8


def jnz(pointer: int, operand: int,  regs: dict):
    if regs['A'] != 0:
        return operand
    return pointer + 2


def bxc(operand: int, regs: dict):
    regs['B'] = regs['B'] ^ regs['C']


def out(operand: int, regs: dict):
    return get_combo(operand, regs) % 8


def bdv(operand: int, regs: dict):
    v = get_combo(operand, regs)
    regs['B'] = int(regs['A']/(2**v))


def cdv(operand: int, regs: dict):
    v = get_combo(operand, regs)
    regs['C'] = int(regs['A']/(2**v))


def execute(prog: list, regs: dict):
    p = 0
    outs = []
    while p < len(prog):
        match prog[p]:
            case 0:
                adv(prog[p+1], regs)
                p += 2
            case 1:
                bxl(prog[p+1], regs)
                p += 2
            case 2:
                bst(prog[p+1], regs)
                p += 2
            case 3:
                p = jnz(p, prog[p+1], regs)
            case 4:
                bxc(prog[p+1], regs)
                p += 2
            case 5:
                outs.append(out(prog[p+1], regs))
                p += 2
            case 6:
                bdv(prog[p+1], regs)
                p += 2
            case 7:
                cdv(prog[p+1], regs)
                p += 2
            case _:
                print("no match")
    return ",".join([str(o) for o in outs])


def p1():
    return execute(PROG, REGS)

def p2():
    cursor = -1
    a_val = 8**(len(PROG) + cursor)
    while abs(cursor) <= len(PROG):
        out = execute(PROG, {'A': a_val, 'B': 0, 'C': 0}).split(",")
        if all(int(out[i]) == PROG[i] for i in range(-1, cursor-1, -1)):
            cursor -= 1
            continue

        a_val += 8**(len(PROG) + cursor)

    return a_val

print(p1())
print(p2())

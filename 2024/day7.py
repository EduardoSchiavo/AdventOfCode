import itertools
with open("inputs/input7.txt") as ifile:

    INP = [(int(k), [int(n) for n in v.split()])
           for line in ifile.read().splitlines() for k, v in [line.split(":")]]


def is_valid(target: int, vs: list[int], ops: tuple[str]) -> bool:
    ops = list(ops)
    test_val = vs[0]
    for i, op in enumerate(ops):
        if op == '+':
            test_val += vs[i+1]
        elif op == "*":
            test_val *= vs[i+1]
        else:
            test_val = int(str(test_val)+str(vs[i+1]))
    return test_val == target


def sum_valid(eqs: list, ops: str):
    tot = 0
    for k, v in eqs:
        comb = itertools.product(ops, repeat=len(v)-1)
        for c in comb:
            if is_valid(k, v, c):
                tot += k
                break
    return tot

def p1():
    return sum_valid(INP, "+*")

def p2():
    return sum_valid(INP, "+*|")

print(p1())
print(p2())

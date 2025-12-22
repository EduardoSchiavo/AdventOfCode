from itertools import product
from z3 import Optimize, Int, Sum, sat

with open("inputs/input10.txt") as ifile:
    SCHEMAS = ifile.read().splitlines()
    TARGETS = [[0 if i == '.' else 1 for i in s.split()[0].strip("][")]
               for s in SCHEMAS]
    BUTTONS = [[tuple(int(i) for i in b.strip(")(").split(","))
                for b in s.split()[1:-1]] for s in SCHEMAS]
    JOLTAGES = [list(map(int, s.split()[-1].strip("}{").split(","))) for s in SCHEMAS]



def p1():
    return sum(get_number_of_presses(TARGETS[i], BUTTONS[i]) for i in range(len(TARGETS)))


def press(button: tuple, machine: list):
    for i in button:
        machine[i] ^= 1


def generate_combinations(n):
    return sorted(list(product([0, 1], repeat=n)), key=sum)


def apply_combination(combination: tuple, buttons: list[tuple], size: int):
    machine = [0 for _ in range(size)]
    for button, times in enumerate(combination):
        for t in range(times):
            press(buttons[button], machine)
    return machine


def get_number_of_presses(target: list, buttons: tuple):
    combs = generate_combinations(len(buttons))
    for c in combs:
        m = apply_combination(c, buttons, len(target))
        if m == target:
            return sum(c)



def minimize_presses(buttons: list, target: list):
    opt = Optimize()
    x = [Int(f'x{i}') for i in range(len(buttons))]

    for xi in x:
        opt.add(xi >=0)

    for i, t in enumerate(target):
        coefficients = [int(i in bt) for bt in buttons] #1 if in button else 0
        opt.add(Sum(c*xi for c,xi in zip(coefficients, x)) == t)

    opt.minimize(Sum(x))

    if opt.check() == sat:
        m = opt.model()
        return sum(m[xi].as_long() for xi in x)

def p2():
    return sum(minimize_presses(bs, ts) for bs, ts in zip(BUTTONS, JOLTAGES))


assert p1() == 415
assert p2() == 16663


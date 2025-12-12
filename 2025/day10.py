from itertools import product

with open("inputs/input10.txt") as ifile:
    SCHEMAS = ifile.read().splitlines()
    TARGETS = [[0 if i == '.' else 1 for i in s.split()[0].strip("][")]
               for s in SCHEMAS]
    BUTTONS = [[tuple(int(i) for i in b.strip(")(").split(","))
                for b in s.split()[1:-1]] for s in SCHEMAS]
    JOLTAGES = [s.split() for s in SCHEMAS]

print(TARGETS)
print(BUTTONS)
# print(JOLTAGES)


def p1():
    return sum(get_number_of_presses(TARGETS[i], BUTTONS[i]) for i in range(len(TARGETS)))


def press(button: tuple, machine: list):
    for i in button:
        machine[i] ^= 1


def generate_combinations(n):
    return sorted(list(product([0, 1, 2], repeat=n)), key=sum)


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


print(f"p1: {p1()}")

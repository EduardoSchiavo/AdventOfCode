from itertools import combinations
from functools import cmp_to_key
with (open("inputs/input9.txt")) as ifile:
    inp = [tuple([int(n) for n in l.split(',')])
           for l in ifile.read().splitlines()]

print(inp)

RED_TILES = inp


def compute_square(a: tuple, b: tuple) -> int:
    return (max(a[0], b[0]) + 1 - min(a[0], b[0])) * (max(a[1], b[1]) + 1 - min(a[1], b[1]))


def precompute_pairs(coords: list[tuple]):
    return list(combinations(RED_TILES, 2))


def p1():
    all_pairs = precompute_pairs(RED_TILES)
    return max(compute_square(*pair) for pair in all_pairs)


print(p1())


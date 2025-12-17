from itertools import combinations
from functools import cache
with (open("inputs/input9.txt")) as ifile:
    inp = [tuple([int(n) for n in l.split(',')])
           for l in ifile.read().splitlines()]


RED_TILES = inp


def p1():
    all_pairs = precompute_pairs(RED_TILES)
    return max(compute_square(*pair) for pair in all_pairs)


def compute_square(a: tuple, b: tuple) -> int:
    return (max(a[0], b[0]) + 1 - min(a[0], b[0])) * (max(a[1], b[1]) + 1 - min(a[1], b[1]))


def precompute_pairs(coords: list[tuple]):
    return list(combinations(RED_TILES, 2))


def p2():
    all_pairs = precompute_pairs(RED_TILES)
    max_area = 0
    for pair in all_pairs:
        area = compute_square(*pair)
        if area > max_area and is_valid(pair):
            max_area = area
    return max_area


@cache
def point_in_polygon(x: int, y: int) -> bool:
    inside = False

    for (x1, y1), (x2, y2) in zip(RED_TILES, RED_TILES[1:] + RED_TILES[:1]):
        if (x == x1 == x2 and min(y1, y2) <= y <= max(y1, y2) or
                y == y1 == y2 and min(x1, x2) <= x <= max(x1, x2)):
            return True
        if ((y1 > y) != (y2 > y) and (x < (x2-x1)*(y-y1)/(y2-y1) + x1)):
            inside = not inside
    return inside


def edge_intersects_rect(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    if y1 == y2:
        if ry1 < y1 < ry2:
            if max(x1, x2) > rx1 and min(x1, x2) < rx2:
                return True
    else:
        if rx1 < x1 < rx2:
            if max(y1, y2) > ry1 and min(y1, y2) < ry2:
                return True
    return False


def is_valid(pair) -> bool:
    x1, x2 = sorted([pair[0][0], pair[1][0]])
    y1, y2 = sorted([pair[0][1], pair[1][1]])

    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        if not point_in_polygon(x, y):
            return False
    for (ex1, ey1), (ex2, ey2) in zip(RED_TILES, RED_TILES[1:] + RED_TILES[:1]):
        if edge_intersects_rect(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
            return False

    return True


assert p1() == 4763509452
assert p2() == 1516897893

from math import floor
from itertools import combinations
from functools import cmp_to_key
with (open("examples/example9.txt")) as ifile:
    inp = [tuple([int(n) for n in l.split(',')])
           for l in ifile.read().splitlines()]


RED_TILES = inp
MAX_X = max(p[0] for p in RED_TILES)
MAX_Y = max(p[1] for p in RED_TILES)


def p1():
    all_pairs = precompute_pairs(RED_TILES)
    return max(compute_square(*pair) for pair in all_pairs)


def compute_square(a: tuple, b: tuple) -> int:
    return (max(a[0], b[0]) + 1 - min(a[0], b[0])) * (max(a[1], b[1]) + 1 - min(a[1], b[1]))


def precompute_pairs(coords: list[tuple]):
    return list(combinations(RED_TILES, 2))


def p2():
    all_pairs = precompute_pairs(RED_TILES)
    
    def compare(a, b):
        return compute_square(*a) - compute_square(*b)

    all_pairs = sorted(all_pairs, key=cmp_to_key(compare), reverse=True)
    print(all_pairs)
    polygon_sides = get_sides(RED_TILES)
    lo = 0
    hi = len(all_pairs)

    while (lo < hi):
        mid = floor(lo + (hi - lo)/2)
        if is_contained(all_pairs[mid], polygon_sides):
            hi = mid
        else:
            lo = mid + 1

    # print(all_pairs)
    print(f"low {lo}, hi {hi}")
    return compute_square(*all_pairs[lo-1])


def get_sides(pairs: list):
    return [(pairs[i-1], pairs[i]) for i in range(1, len(pairs))]


def get_box(pair: tuple):
    a, b = pair
    return {(a, (a[0], b[1])), (a, (b[0], a[1])), (b, (a[0], b[1])), (b, (b[0], a[1]))}


def intersects(segment: tuple, perimeter: list):
    if segment[0][0] == segment[1][0]: #perpendicular to x
        for side in perimeter:
            if side[0][0] == side[1][0]: # also perpendicular, ignore
                continue
            if segment[0][1] < side[0][1] < segment[1][1]:
                print(f"intersecting at {segment[0][0], side[0][1]}")
                intersection = (segment[0][0], side[0][1])
                if intersection in RED_TILES:
                    print("ignore")
                    continue
                return True
    else: #perpendicular to y 
        for side in perimeter:
            if side[0][1] == side[1][1]:
                continue
            if segment[0][0] < side[0][0] < segment[1][0]:
                intersection = (side[0][0], segment[0][1])
                print(f"intersecting at {intersection}")
                if intersection in RED_TILES:
                    print("ignore")
                    continue
                return True
    return False


def is_contained(pair: tuple, perimeter: list) -> int:
    print(f"checking box: {pair}")
    box_sides = get_box(pair)
    for side in box_sides:
        print(f"side : {side}")
        if intersects(side, perimeter):
            print(f"side {side} intersects perimeter")
            return False
    return True


# print(p1())
print(p2())

# print(f"polygon sides: {get_sides(RED_TILES)}")

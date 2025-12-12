from itertools import combinations
from functools import cmp_to_key
with (open("inputs/input9.txt")) as ifile:
    inp = [tuple([int(n) for n in l.split(',')])
           for l in ifile.read().splitlines()]


RED_TILES = inp
MAX_X = max(p[0] for p in RED_TILES)
MAX_Y = max(p[1] for p in RED_TILES)


def compute_square(a: tuple, b: tuple) -> int:
    return (max(a[0], b[0]) + 1 - min(a[0], b[0])) * (max(a[1], b[1]) + 1 - min(a[1], b[1]))

#VIBECODED XD
def compute_box_perimeter(a: tuple, b: tuple):
    """
    Return the perimeter of the axis-aligned rectangle defined
    by opposite corners a and b, as a list of (x, y) points.
    """

    x1, y1 = a
    x2, y2 = b

    # Get min/max corners
    left, right = min(x1, x2), max(x1, x2)
    bottom, top = min(y1, y2), max(y1, y2)

    perimeter = []

    # Bottom edge (left to right)
    for x in range(left, right + 1):
        perimeter.append((x, bottom))

    # Right edge (bottom+1 to top-1)
    for y in range(bottom + 1, top):
        perimeter.append((right, y))

    # Top edge (right to left)
    if top != bottom:   # avoid duplicating if zero height
        for x in range(right, left - 1, -1):
            perimeter.append((x, top))

    # Left edge (top-1 to bottom+1)
    if left != right:   # avoid duplicating if zero width
        for y in range(top - 1, bottom, -1):
            perimeter.append((left, y))

    return perimeter


def precompute_pairs(coords: list[tuple]):
    return list(combinations(RED_TILES, 2))


def p1():
    all_pairs = precompute_pairs(RED_TILES)
    return max(compute_square(*pair) for pair in all_pairs)

def compute_perimeter(tile_pairs: list[tuple]) -> set:
    perimeter = set()
    for pair in tile_pairs:
        if pair[0][0] == pair[1][0]:
            for i in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1])+1):
                perimeter.add((pair[0][0], i))
        elif pair[0][1] == pair[1][1]:
            for i in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])+1):
                perimeter.add((i, pair[0][1]))
    return perimeter


def get_corners(a: tuple, b: tuple) -> set:
    return {a, b, (a[0], b[1]), (b[0], a[1])}


def is_point_in_polygon(point: tuple, polygon: set[tuple]) -> bool:
    if point in polygon:
        return True

    crossed = 0
    dir = 0
    dirs = [(1, 0, MAX_X), (0, 1, MAX_Y), (-1, 0, MAX_X), (0, -1, MAX_Y)]
    curr = point
    edge = False
    first = True
    for dir in dirs:
        if not edge and not first:
            return crossed %2 != 0
        first = False
        edge = False
        for i in range(0, dir[2]):
            prev = curr
            curr = (curr[0]+dir[0], curr[1]+dir[1])
            if curr in polygon:
                crossed +=1
            # print(f"curr: {curr} prev: {prev}")
            if curr in polygon and prev in polygon:
                # print(f"{curr} caught an edge! reset and change direction")
                curr = point
                crossed = 0
                edge = True
                break
    return crossed %2 != 0

def p2():
    all_pairs = precompute_pairs(RED_TILES)
    perimeter = compute_perimeter(all_pairs)
    # print(f"perimeter: {perimeter}")

    def compare(a, b):
        return compute_square(*a) - compute_square(*b)

    all_pairs = sorted(all_pairs, key=cmp_to_key(compare), reverse=True)
    # print(f"sorted pairs: {all_pairs}")
    for p in all_pairs:
        print(f"evaluating: {p}")
        # corners = list(get_corners(*p))
        box_perimeter = compute_box_perimeter(*p)
        skip = False
        # print(f"corners: {corners}")
        # for c in corners:
        for c in box_perimeter:
            if not is_point_in_polygon(c, perimeter):
                # print(f"out: {c}")
                skip=True
                break
        if skip:
            continue
        else:
            print(f"returning area of {p}")
            return compute_square(*p) 


# print(p1())
print(p2())



# all_pairs = precompute_pairs(RED_TILES)
# perimeter = compute_perimeter(all_pairs)
# test = {(84038, 16393), (15740, 83824), (84038, 83824), (15740, 16393)}
# for t in test:
#     is_point_in_polygon(t, perimeter)
# print(f"polygon: {perimeter}")

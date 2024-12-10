with open("inputs/input10.txt") as ifile:
    INP = {(i, j): int(v) for i, row in enumerate(ifile.read().splitlines())
           for j, v in enumerate(row)}

HEADS = [p for p, v in INP.items() if v == 0]
BOUNDS = list(INP.keys())[-1]

DIRS = ((0, 1), (1, 0), (-1, 0), (0, -1))


def hike(land: dict, pos: tuple, target: int, prev: int, seen: list, counting_paths: bool):
    nines = 0
    if pos[0] < 0 or pos[0] > BOUNDS[0] or pos[1] < 0 or pos[1] > BOUNDS[1]:
        return 0

    curr_val = land[pos]
    if curr_val - prev != 1:
        return 0

    if pos in seen:
        return 0

    if not counting_paths:
        seen.append(pos)

    if curr_val == target:
        return 1

    for dir in DIRS:
        next = tuple([sum(x) for x in zip(pos, dir)])
        nines += hike(land, next, target, curr_val, seen, counting_paths)

    return nines


def p1():
    return sum(hike(INP, head, 9, -1, [], False) for head in HEADS)


def p2():
    return sum(hike(INP, head, 9, -1, [], True) for head in HEADS)


print(p1())
print(p2())

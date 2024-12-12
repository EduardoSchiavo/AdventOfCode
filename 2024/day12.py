with open("inputs/input12.txt") as ifile:
    INP = {(i, j): v for i, row in enumerate(ifile.read().splitlines())
           for j, v in enumerate(row)}


BOUNDS = list(INP.keys())[-1]
DIRS = ((0, 1), (1, 0), (-1, 0), (0, -1))


def get_bounds(region: list[tuple]) -> tuple:
    return (min(t[0] for t in region),
            max(t[0] for t in region),
            min(t[1] for t in region),
            max(t[1] for t in region))


def is_edge(pos: tuple, dir: tuple, land: dict) -> bool:
    next = tuple([sum(x) for x in zip(pos, dir)])
    try:
        if land[next] != land[pos]:
            return True
    except KeyError:
        return True
    return False


def get_edges(region: list[tuple], land: dict):
    bounds = get_bounds(region)
    count = 0
    for x in range(bounds[0], bounds[1]+1):
        line = [y for y in range(
            bounds[2], bounds[3]+1) if (x, y) in region and is_edge((x, y), (-1, 0), land)]
        if line:
            count += 1
        count += sum(1 for i in range(len(line) - 1)
                     if line[i + 1] - line[i] != 1)

        line = [y for y in range(
            bounds[2], bounds[3]+1) if (x, y) in region and is_edge((x, y), (1, 0), land)]
        if line:
            count += 1

        count += sum(1 for i in range(len(line) - 1)
                     if line[i + 1] - line[i] != 1)
    for y in range(bounds[2], bounds[3]+1):
        line = [x for x in range(
            bounds[0], bounds[1]+1) if (x, y) in region and is_edge((x, y), (0, -1), land)]
        if line:
            count += 1
        count += sum(1 for i in range(len(line) - 1)
                     if line[i + 1] - line[i] != 1)
        line = [x for x in range(
            bounds[0], bounds[1]+1) if (x, y) in region and is_edge((x, y), (0, +1), land)]
        if line:
            count += 1
        count += sum(1 for i in range(len(line) - 1)
                     if line[i + 1] - line[i] != 1)

    return count


def explore_region(land: dict, pos: tuple, prev: tuple, visited: list) -> list:
    area = []
    if pos[0] < 0 or pos[0] > BOUNDS[0] or pos[1] < 0 or pos[1] > BOUNDS[1]:
        return area

    if pos in visited:
        return area

    if prev and land[pos] != land[prev]:
        return area

    visited.append(pos)
    area.append(pos)
    for dir in DIRS:
        next = tuple([sum(x) for x in zip(pos, dir)])
        area.extend(explore_region(land, next, pos,  visited))

    return area

# swap dirs and j to make more efficiest: check dirs and see if point is in region


def count_contacts(region: list[tuple]) -> int:
    tot = 0
    for i in range(len(region)):
        for j in range(i, len(region)):
            delta = tuple(x-y for x, y in zip(region[i], region[j]))
            tot += delta in DIRS
    return tot


def score(part: int):
    regions = []
    visited = []
    price = 0
    for point in INP.keys():
        if point in visited:
            continue
        region = explore_region(INP, point, None, [])
        if part == 1:
            price += len(region)*(len(region)*4-count_contacts(region)*2)
        else:
            price += len(region)*get_edges(region, INP)
        regions.append(region)
        visited.extend(region)
    return price


def p1():
    return score(1)


def p2():
    return score(2)


print(p1())
print(p2())

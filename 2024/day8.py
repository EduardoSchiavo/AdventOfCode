import math
with open("inputs/input8.txt") as ifile:
    INP = {(i, j): v for i, row in enumerate(ifile.read().splitlines())
           for j, v in enumerate(row)}


BOUNDS = list(INP.keys())[-1]
ANTENNA_POINTS = [p for p, v in INP.items() if v != "."]
ANTENNAS = {v: [] for v in INP.values() if v != "."}

for a in ANTENNAS.keys():
    ANTENNAS[a] = [k for k, v in INP.items() if v == a]


def midpoint(a: tuple, b: tuple) -> tuple:
    return (a[0]+b[0])/2, (a[1]+b[1])/2


def p1():
    tot = 0
    for point in INP.keys():
        for ant in ANTENNA_POINTS:
            mp = midpoint(point, ant)
            try:
                if INP[ant] == INP[mp] and mp != ant and mp != point:
                    tot += 1
                    break
            except KeyError:
                pass
    return tot


def compute_points(bounds: tuple, a: tuple, b: tuple) -> list[tuple]:
    return [(x, y) for x in range(bounds[0] + 1) if (y := ((x-a[0])/(b[0]-a[0]))*(b[1]-a[1]) + a[1]).is_integer() and 0 <= y <= bounds[1]]


def p2():
    return len(set([
        point for k, v in ANTENNAS.items()
        for i, num in enumerate(v[:-1])
        for j in v[i+1:]
        for point in compute_points(BOUNDS, num, j)
    ]))


print(p1())
print(p2())

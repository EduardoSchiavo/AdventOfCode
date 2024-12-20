with open("inputs/input20.txt") as ifile:
    MAP = {(x, y): v for x, row in enumerate(ifile.read().splitlines())
           for y, v in enumerate(row)}

START = [pos for pos in MAP.keys() if MAP[pos] == 'S'][0]
END = [pos for pos in MAP.keys() if MAP[pos] == 'E'][0]
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R, D, L, U


def find_path(s: tuple, e: tuple, track: dict):
    pos = s
    prev = None
    path = {s: 0}
    while pos != e:
        for dir in DIRS:
            n = tuple(sum(x) for x in zip(pos, dir))
            if n == e:
                path[n] = path[pos]+1
                pos = n
                break

            if track.get(n) == '.' and n != prev:
                path[n] = path[pos]+1
                prev = pos
                pos = n
                break
    return path


def manhattan(a: tuple, b: tuple) -> int:
    return abs(b[0]-a[0]) + abs(b[1]-a[1])


def get_pairs(path: dict[tuple, int]):
    pairs = []
    keys = list(path.keys())
    for i in range(len(keys)):
        for j in range(i, len(keys)-4):
            pairs.append((keys[i], keys[j+4]))
    return pairs


def get_cheats(allowed: int):
    path = find_path(START, END, MAP)
    cheats = get_pairs(path)
    tot = 0
    for c in cheats:
        m = manhattan(*c)
        if not 2 <= m <= allowed:
            continue
        saved = abs(path[c[0]] - path[c[1]]) - manhattan(*c)
        if saved >= 100:
            tot += 1
    return tot


def p1():
    return get_cheats(2)


def p2():
    return get_cheats(20)


print(p1())
print(p2())

with open("inputs/input20.txt") as ifile:
    MAP = {(x, y): v for x, row in enumerate(ifile.read().splitlines())
           for y, v in enumerate(row)}

START = [pos for pos in MAP.keys() if MAP[pos] == 'S'][0]
END = [pos for pos in MAP.keys() if MAP[pos] == 'E'][0]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R, D, L, U
print(START, END)

MAXCHEATS = 20


def get_adjacents(p: tuple, track: dict) -> list:
    bounds = list(track.keys())[-1]
    adj_pts = [tuple(sum(x) for x in zip(p, dir)) for dir in DIRS]
    return [pt for pt in adj_pts if track.get(pt) != '#'
            and 0 < pt[0] < bounds[0] and 0 < pt[1] < bounds[1]]


def get_cheats(track: dict):
    walls = []
    for p in track.keys():
        if track.get(p) == '#':
            adj = [tuple(sum(x) for x in zip(p, dir)) for dir in DIRS]
            if (track.get(adj[0], '_') in 'SE.' and track.get(adj[2], '_') in 'SE.') or (track.get(adj[1], '_') in 'SE.' and track.get(adj[3], '_') in 'SE.'):
                walls.append(p)
    return walls


def find_path(s: tuple, e: tuple, track: dict):
    pos = s
    prev = None
    path = [s]
    while pos != e:
        for dir in DIRS:
            n = tuple(sum(x) for x in zip(pos, dir))
            if n == e:
                path.append(n)
                pos = n
                break

            if track.get(n) == '.' and n != prev:
                path.append(n)
                prev = pos
                pos = n
                break
    return path


print(len(find_path(START, END, MAP)))

def manhattan(a: tuple, b:tuple)-> int:
    return abs(b[0]-a[0]) + abs(b[1]-a[1])

def get_pairs(path: list[tuple]):
    pairs = []
    for i in range(len(path)):
        for j in range(i, len(path)-4):
            pairs.append((path[i], path[j+4]))
    return pairs

def p1():
    path = find_path(START, END, MAP)
    cheats = get_pairs(path)
    tot = 0
    for c in cheats:
        # print(manhattan(*c))
        m = manhattan(*c)
        # if m != 2:
        #     continue
        if not 2 <= m <= 20:
            continue
        saved = abs(path.index(c[0]) - path.index(c[1])) - manhattan(*c)
        if saved >= 100:
            tot += 1
    return tot


print(p1())
# def p1():
#     # track_len = dijkstra(START, END, MAP)
#     track = find_path(START, END, MAP)
#     print(track)
#     track_len = len(track)
#     cheats = get_cheats(MAP)
#     # save = {c: 0 for c in cheats}
#     tot = 0
#     for c in cheats:
#         MAP[c] = '.'
#         # save[c] += track_len - dijkstra(START, END, MAP)
#         if (track_len - dijkstra(START, END, MAP)) >= 100:
#             tot += 1
#         MAP[c] = '#'
#     return tot
#

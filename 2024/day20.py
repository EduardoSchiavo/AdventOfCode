import math
from heapq import heapify, heappop, heappush

with open("inputs/input20.txt") as ifile:
    MAP = {(x, y): v for x, row in enumerate(ifile.read().splitlines())
           for y, v in enumerate(row)}

START = [pos for pos in MAP.keys() if MAP[pos] == 'S'][0]
END = [pos for pos in MAP.keys() if MAP[pos] == 'E'][0]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R, D, L, U
print(START, END)


def get_adjacents(p: tuple, track: dict) -> list:
    bounds = list(track.keys())[-1]
    adj_pts = [tuple(sum(x) for x in zip(p, dir)) for dir in DIRS]
    return [pt for pt in adj_pts if track.get(pt) != '#'
            and 0 < pt[0] < bounds[0] and 0 < pt[1] < bounds[1]]


def dijkstra(start: tuple, end: tuple,  track: dict):
    dist = {k: math.inf for k in track.keys()}
    dist[start] = 0
    prev = {}
    pq = [(0, start)]
    heapify(pq)
    while (pq):
        _, curr = heappop(pq)
        if curr == end:
            return dist[end]
        for adj in get_adjacents(curr, track):
            d = dist[curr] + 1
            if d < dist[adj]:
                dist[adj] = d
                prev[adj] = curr
                heappush(pq, (0, adj))


def get_cheats(track: dict):
    walls = []
    for p in track.keys():
        if track.get(p) == '#':
            adj = [tuple(sum(x) for x in zip(p, dir)) for dir in DIRS]
            # print(p, list(track.get(a) for a in adj))
            if (track.get(adj[0], '_') in 'SE.' and track.get(adj[2], '_') in 'SE.') or (track.get(adj[1], '_') in 'SE.' and track.get(adj[3], '_') in 'SE.'):
                walls.append(p)
    return walls


print(get_adjacents(END, MAP))
print(dijkstra(START, END, MAP))
print(len(get_cheats(MAP)))


def p1():
    track_len = dijkstra(START, END, MAP)
    cheats = get_cheats(MAP)
    # save = {c: 0 for c in cheats}
    tot = 0
    for c in cheats:
        MAP[c] = '.'
        # save[c] += track_len - dijkstra(START, END, MAP)
        if (track_len - dijkstra(START, END, MAP)) >= 100:
            tot += 1
        MAP[c] = '#'
    return tot


print(p1())

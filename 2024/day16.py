from heapq import heapify, heappush, heappop
import math
with open("inputs/input16.txt") as ifile:
    MAP = {(x, y): v for x, row in enumerate(ifile.read().splitlines())
           for y, v in enumerate(row)}


START = [k for k in MAP.keys() if MAP[k] == 'S'][0]
END = [k for k in MAP.keys() if MAP[k] == 'E'][0]
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TURNS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def get_adjacents(pos: tuple):
    return [(tuple([sum(x) for x in zip(pos, dir)]), dir) for dir in DIRS]


def are_orthogonal(dir1: tuple, dir2: tuple):
    return dir1[0]*dir2[0] + dir1[1]*dir2[1] == 0


def dijkstra(s: tuple, e: tuple, maze: dict) -> list:
    queue = [(0, (s, (0, 1)))]
    prev = {(s, (0, 1)): None}
    dists = {(k, dir): math.inf for k in maze.keys() for dir in DIRS}
    dists[(s, (0, 1))] = 0
    heapify(queue)
    while (queue):
        v, curr = heappop(queue)
        adjacents = get_adjacents(curr[0])
        if curr[0] == END:
            break
        for adj in adjacents:
            if maze[adj[0]] == '#':
                continue
            if are_orthogonal(curr[1], adj[1]):
                dist = dists[curr] + 1001
            else:
                dist = dists[curr] + 1
            if dist < dists[adj]:
                dists[adj] = dist
                heappush(queue, (dist, adj))
                prev[adj] = {curr}
            elif dist == dists[adj]:
                prev[adj].add(curr)
    return min([dists[(e, dir)] for dir in DIRS]), prev


def traverse(pos: tuple, prev: dict, visited=None):
    if visited is None:
        visited = set()
    seats = set()

    if pos[0] == START:
        seats.add(pos)
        return seats

    if pos in visited:
        return set()

    if prev.get(pos) is None:
        # print(f" dead end: {pos}")
        seats.add(pos)
        return seats

    for child in prev.get(pos):
        seats.update(traverse(child, prev, visited))

    seats.add(pos)
    visited.add(pos)
    return seats


def get_paths(prev: dict, end: tuple):
    seats = set()
    for end in [(end, dir) for dir in DIRS]:
        seats.update([s[0] for s in traverse(end, prev)])
    return seats


def p1():
    return dijkstra(START, END, MAP)[0]

def p2():
    _, prev = dijkstra(START, END, MAP)
    os = get_paths(prev, END)
    return len(os)

print(p1())
print(p2())

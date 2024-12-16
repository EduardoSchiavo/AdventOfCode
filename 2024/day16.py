from heapq import heapify, heappush, heappop
import math
with open("examples/example16.txt") as ifile:
    MAP = {(x, y): v for x, row in enumerate(ifile.read().splitlines())
           for y, v in enumerate(row)}

print(MAP)

START = [k for k in MAP.keys() if MAP[k] == 'S'][0]
END = [k for k in MAP.keys() if MAP[k] == 'E'][0]
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TURNS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def get_adjacents(pos: tuple):
    return [tuple([sum(x) for x in zip(pos, dir)]) for dir in DIRS]


def dijkstra(s: tuple, e: tuple, maze: dict) -> list:
    queue = [(0, s)]
    prev = {s: None}
    dists = {k: math.inf for k in maze.keys()}
    dists[s] = 0
    visited = set()
    heapify(queue)
    while (queue):
        v, curr = heappop(queue)
        if curr in visited:
            continue
        print(f"curr: {curr}, v: {v}")
        visited.add(curr)
        adjacents = get_adjacents(curr)
        for adj in adjacents:
            print(f" adj: {adj, maze[adj]}")
            if maze[adj] == '#':
                continue
            if prev.get(curr) and tuple(x - y for x, y in zip(prev[curr], adj)) in TURNS:
                print(f"pushing corner: {adj}")
                dist = dists[curr] + 1
            else:
                dist = dists[curr] + 10
            if dist < dists[adj]:
                dists[adj] = dist
                prev[adj] = curr
                heappush(queue, (dist, adj))

    print(f"prev array: {prev}")

    curr = e
    path = []
    while (prev[curr] is not None):
        path.append(curr)
        curr = prev[curr]
    path.append(curr)
    path.reverse()
    
    print(f"dist: {dist}")

    return path


print(dijkstra(START, END, MAP))

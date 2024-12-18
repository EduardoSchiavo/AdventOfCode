import math
from heapq import heapify
from heapq import heappop
from math import dist
from heapq import heappush
from math import floor
with open("inputs/input18.txt") as ifile:
    BYTES = [tuple(map(int, b.split(","))) for b in ifile.read().splitlines()]

# print(BYTES)

START = (0, 0)
# END = (6, 6)  # 70, 70
END = (70, 70)


def get_graph(s: tuple, b: list[tuple]) -> dict:
    graph = {}
    dirs = ((0, 1), (0, -1), (-1, 0), (1, 0))
    for x in range(s[0]+1):
        for y in range(s[1]+1):
            if (x, y) in b:
                continue
            graph[(x, y)] = []
            for dir in dirs:
                ad = tuple(sum(x) for x in zip((x, y), dir))
                if 0 <= ad[0] <= s[0] and 0 <= ad[1] <= s[1] and ad not in b:
                    graph[(x, y)].append(ad)
    return graph




def dijkstra(start: tuple, end: tuple,  graph: dict):
    dist = {k: math.inf for k in graph.keys()}
    dist[start] = 0
    prev = {}
    pq = [(0, start)]
    heapify(pq)
    while(pq):
        _, curr = heappop(pq)
        if curr == end:
            return dist[end] 
        for adj in graph[curr]:
            d = dist[curr] + 1
            if d < dist[adj]:
                dist[adj] = d
                prev[adj] = curr
                heappush(pq, (0, adj))


def p1(n: int):
    g = get_graph(END, BYTES[:n])
    return dijkstra(START, END, g)


def bs(b: list):
    lo = 0
    hi = len(b)
    while (lo < hi):
        m = floor(lo + (hi -lo)/2)
        res = p1(m)
        if res == None:
            hi = m
        else:
            lo = m+1
    return b[lo-1] 
        


print(bs(BYTES))

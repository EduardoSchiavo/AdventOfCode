import math
from itertools import combinations
from functools import cmp_to_key

with (open("inputs/input8.txt")) as ifile:
    BOXES = [tuple(int(i) for i in l.split(","))
             for l in ifile.read().splitlines()]


def get_distance(a: tuple, b: tuple) -> float:
    return math.sqrt(sum((i-j)**2 for i, j in zip(a, b)))


def compare(a: tuple, b: tuple):
    return get_distance(*a) - get_distance(*b)


def precompute_pairs(coords: list[tuple]):
    return sorted(list(combinations(coords, 2)), key=cmp_to_key(compare))


class UnionFind:

    def __init__(self):
        self.parent_map = {}
        self.size_map = {}

    def find(self, a: tuple):
        if a not in self.parent_map:
            self.parent_map[a] = a
        if a != self.parent_map[a]:
            self.parent_map[a] = self.find(self.parent_map[a])
        return self.parent_map[a]

    def union(self, a: tuple, b: tuple):
        root_i = self.find(a)
        root_c = self.find(b)
        size_i = self.size_map[root_i] if root_i in self.size_map else 1
        size_c = self.size_map[root_c] if root_c in self.size_map else 1

        if size_i < size_c:
            self.parent_map[root_i] = root_c
            self.size_map[root_c] = size_i + size_c
        else:
            self.parent_map[root_c] = root_i
            self.size_map[root_i] = size_i + size_c




def p1():
    uf = UnionFind()

    sorted_pairs = precompute_pairs(BOXES)

    TO_CONNECT = 1000

    for closest in sorted_pairs[:TO_CONNECT]:
        uf.union(*closest)

    for b in BOXES:
        uf.find(b)

    counts = {}
    for k, v in uf.parent_map.items():
        if uf.find(k) not in counts:
            counts[uf.find(k)] = 1
        else:
            counts[uf.find(k)] += 1

    vals = list(counts.values())
    vals.sort(reverse=True)
    return math.prod(vals[:3])


def p2():

    parent_map = {}
    size_map = {}

    boxes = BOXES.copy()

    already_paired = set()

    def find(a: tuple):
        if a not in parent_map:
            parent_map[a] = a
        if a != parent_map[a]:
            parent_map[a] = find(parent_map[a])
        return parent_map[a]

    sorted_pairs = precompute_pairs(boxes)

    for closest in sorted_pairs:
        # closest = get_closest_pair(boxes, already_paired)
        already_paired.add(closest)
        root_i = find(closest[0])
        root_c = find(closest[1])
        size_i = size_map[root_i] if root_i in size_map else 1
        size_c = size_map[root_c] if root_c in size_map else 1

        if size_i < size_c:
            parent_map[root_i] = root_c
            size_map[root_c] = size_i + size_c
        else:
            parent_map[root_c] = root_i
            size_map[root_i] = size_i + size_c

        for b in BOXES:
            find(b)

        counts = {}
        for k, v in parent_map.items():
            if find(k) not in counts:
                counts[find(k)] = 1
            else:
                counts[find(k)] += 1

        if len(counts.keys()) == 1:
            return closest[0][0]*closest[1][0]


print("-----")

assert p1() == 103488
assert p2() == 8759985540

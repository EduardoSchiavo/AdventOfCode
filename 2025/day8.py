import math
from itertools import combinations
from functools import cmp_to_key

with (open("inputs/input8.txt")) as ifile:
    BOXES = [tuple(int(i) for i in l.split(","))
             for l in ifile.read().splitlines()]


# print(BOXES)


def get_distance(a: tuple, b: tuple)-> float:
    return math.sqrt(sum((i-j)**2 for i, j in zip(a, b)))

def compare(a: tuple, b: tuple):
    return get_distance(*a) - get_distance(*b)

def precompute_pairs(coords: list[tuple]):
    return sorted(list(combinations(coords, 2)), key=cmp_to_key(compare))


# print(f"all pairs: {precompute_pairs(BOXES)}")

def get_closest_pair(coords: list[tuple], ignore: set[tuple]):
    #refactor later
    dist = math.inf
    pair = None
    for a in coords:
        for b in coords:
            if a == b or (a,b) in ignore or (b, a) in ignore:
                continue
            d = get_distance(a,b)
            if d < dist:
                dist = d
                pair = (a,b)
    return pair

def p1():

    parent_map = {}
    size_map = {}
    
    boxes = BOXES.copy()
    
    already_paired = set()

    def find(a: tuple):
        if a not in parent_map:
            parent_map[a]=a
        if a != parent_map[a]:
            parent_map[a] = find(parent_map[a])
        return parent_map[a]
   
    sorted_pairs = precompute_pairs(boxes)

    for closest in sorted_pairs[:1000]:
        # closest = get_closest_pair(boxes, already_paired)
        already_paired.add(closest)
        root_i = find(closest[0])
        root_c = find(closest[1])
        size_i = size_map[closest[0]] if closest[0] in size_map else 1
        size_c = size_map[closest[1]] if closest[1] in size_map else 1

        if size_i < size_c:
            parent_map[root_i] = root_c
            size_map[root_c] = size_i + size_c
        else:
            parent_map[root_c] = root_i
            size_map[root_i] = size_i + size_c

    # print(f"parent map { parent_map}")
    # print(f"parent map size{len(parent_map.keys())}")
   

    counts= {}
    roots = set()
    for k, v in parent_map.items():
        # print(f"root of {k} is {find(k)}")
        if find(k) not in counts:
            counts[find(k)] = 1
        else: 
            counts[find(k)] += 1
    # print(f"counts: {counts}")
    # print(f"roots: {roots}, tot: {len(roots)}")
    
    vals = []
    for _, v in counts.items():
        vals.append(v)
    vals.sort(reverse=True)
    prd = 1
    for i in vals[:3]:
        prd *= i
    return prd
            
print("-----")
print(p1())

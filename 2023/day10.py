
from dataclasses import dataclass
from operator import length_hint
from unittest import result
from urllib.request import ProxyDigestAuthHandler


EXAMPLE = "examples/example10p4.txt"
INPUT = "inputs/input10.txt"


with open(EXAMPLE) as ifile:
    INP = [ list(line) for line in ifile.read().splitlines()]

# print(INP)

@dataclass
class Pipe:
    pos: tuple
    kind: str

def find_source(pipe_map: list[list]):
    for r, row in enumerate(pipe_map):
        for c, elem in enumerate(row):
            # print(elem)
            if elem == 'S':
                return (r, c)





def get_connections(source: tuple, kind: str, pipe_map: list[list]):

    openings = {
        '|': ((-1, 0), (+1, 0)), #above, below
        '-': ((0, -1), (0, +1)), #left, right
        'L': ((-1, 0), (0, +1)), #above, right
        'J': ((-1, 0), (0, -1)), #above, left
        '7': ((0, -1), (+1, 0)), #left, below
        'F': ((0, +1), (+1, 0)), #right, below
        '.': (), #none
        'S': ((-1, 0), (+1, 0),(0, -1), (0, +1) ) #all
    }
    if kind == 'S':  #TODO: remove custom logic
        conn = []
        if pipe_map[source[0]-1][source[1]] in ["|", "F", "7"]:
            conn.append(Pipe((source[0]-1, source[1]), pipe_map[source[0]-1][source[1]]))
        if pipe_map[source[0]][source[1]+1] in ["-", "J", "7"]:
            conn.append(Pipe((source[0],source[1]+1), pipe_map[source[0]][source[1]+1]))
        if pipe_map[source[0]+1][source[1]] in ["|", "J", "L"]:
            conn.append(Pipe((source[0]+1,source[1]), pipe_map[source[0]+1][source[1]]))
        if pipe_map[source[0]][source[1]-1] in ["-", "F", "L"]:
            conn.append(Pipe((source[0],source[1]-1), pipe_map[source[0]][source[1]-1]))
        return conn

    return [Pipe((source[0]+op[0], source[1]+op[1]), pipe_map[source[0]+op[0]][source[1]+op[1]]) for op in openings[kind]]




# print(get_connections((1,1), 'S', INP))

def explore_paths_from_source():
    source = Pipe(find_source(INP), 'S')
    source_connections = get_connections(find_source(INP), 'S', INP)
    pathA = [source, source_connections[0]]
    pathB = [source, source_connections[1]]
    # print('a', pathA)
    # print('b', pathB)
    exploring = True
    count = 1
    while exploring :
        # print('last elem:', pathA[-1])
        pathA.extend([pipe for pipe in get_connections(pathA[-1].pos, pathA[-1].kind, INP) if pipe not in pathA])
        pathB.extend([pipe for pipe in get_connections(pathB[-1].pos, pathB[-1].kind, INP) if pipe not in pathB])
        count +=1
        if pathA[-1]==pathB[-1]:
            exploring = False
    pathA.extend(pathB[::-1])
    return pathA, count

def p1():
    return explore_paths_from_source()[1]








def get_indices(intersections: list, edges: list[tuple]):
    return sorted([edges.index(num) for num in intersections])
    
def clean(indices: list):
    # print(indices)

    if len(indices) < 2:
        return indices # FIXME: maybe return list of len 1
    ret =[]
    block = [indices[0]]
    for i in range(len(indices)-1):
        if indices[i+1]-indices[i] == 1:
            block.append(indices[i+1])
        else:
            if len(block) == 1:
                ret.extend(block)
            block = [indices[i+1]]
    if len(block) == 1:
        ret.extend(block)
    return ret


def count_valid(intersections: list, edges: list[tuple]):
    return len(clean(get_indices(intersections, edges)))

def cast_rays(point: tuple, edges: list[tuple]):
    height = len(INP)
    width = len(INP[0])
    int_count = []
    intersections = []
    for i in range(point[0]+1, height):
        if (i, point[1]) in edges:
            intersections.append((i, point[1]))
    count_a = count_valid(intersections, edges)
    int_count.append(len(intersections))
    # print(intersections) 
    # if count_valid(intersections, edges) %2 != 0:
    #     print('aaaa')
    #     return True
    intersections = []
    for i in range(0, point[0]):
        if (i, point[1]) in edges:
            intersections.append((i, point[1]))
    # print(intersections)
    count_b = count_valid(intersections, edges)
    int_count.append(len(intersections))

    # if count_valid(intersections, edges) %2 != 0:
    #     print('bbbb')
    #     return True
    intersections = []
    for i in range(0, point[1]):
        if (point[0], i) in edges :
            intersections.append((point[0], i))
    count_c = count_valid(intersections, edges)
    int_count.append(len(intersections))


    # print(intersections)
    # if count_valid(intersections, edges) %2 != 0:
    #     print('ccc')
    #     return True
    intersections = []
    for i in range(point[1]+1, width):
        if (point[0], i) in edges:
            intersections.append((point[0], i))
    # print(intersections)
    count_d = count_valid(intersections, edges)
    int_count.append(len(intersections))

    print('counts', [count_a, count_b, count_c, count_d])

    # if any(c == 0 for c in [count_a, count_b, count_c, count_d]):
    #     return False
    if any(c % 2 == 0 for c in [count_a, count_b, count_c, count_d]):
        return True
    
    # if count_valid(intersections, edges) %2 != 0:
    #     print('ddd')
    #     return True
    return False

    
LOOP = explore_paths_from_source()[0]
EDGES = [l.pos for l in LOOP]

# print(cast_rays((2,3), EDGES))
# print([l.pos for l in loop])
# print(count_valid([(2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15)], EDGES))

points_in_poligon = []
for r in range(1, len(INP)-1):
    for c in range(1, len(INP[0])-1):
        if cast_rays((r, c), EDGES):
            points_in_poligon.append((r, c))

print('res', [point for point in points_in_poligon if point not in EDGES])

# print('test', count_valid([(1, 4), (2, 4)], EDGES))
# print('test edge', count_valid([(5, 4), (6, 4), (7, 4)],EDGES ))

# print(get_indices([(5, 4), (6, 4), (7, 4)], EDGES))
# print(get_indices([(1, 4), (2, 4)], EDGES))

# print(clean([36, 37, 38]))
# print(clean([3, 29]))

# print(get_indices([(3, 1), (3, 2)], EDGES))
# print(clean([45, 32]))

print(cast_rays((4, 7), EDGES))



from itertools import combinations

EXAMPLE = "examples/example11.txt"
INPUT = "inputs/input11.txt"


with open(EXAMPLE) as ifile:
    INP = [ list(line) for line in ifile.read().splitlines()]

# print(INP)


def get_galaxies(points: list[list])-> dict:
    galaxies = {}
    down_shift=0
    for ridx, row in enumerate(points):
        if all(val == '.' for val in row):
            down_shift+=1
        for cidx, value in enumerate(row):
            if value == '#':
                galaxies[(ridx+down_shift, cidx)]=value
    return galaxies


def get_empty_columns(galaxies: dict)-> list[int]:
    return [i for i in range(len(INP)) if i not in [key[1] for key in galaxies.keys()]]
        
def shift_galaxies(galaxies: dict):
    empty = get_empty_columns(galaxies)
    shifted_galaxies = {}
    for key in galaxies.keys():
        new_coord = key[1] + sum([i<key[1] for i in empty])
        shifted_galaxies[(key[0], new_coord)] = galaxies[key]
    return shifted_galaxies
        

def manhattan_distance(pointA: tuple, pointB: tuple):
    return abs(pointB[0]-pointA[0]) + abs(pointB[1]-pointA[1]) 


def p1():
    galaxies = shift_galaxies(get_galaxies(INP))
    return sum([manhattan_distance(*pair) for pair in list(combinations(galaxies.keys(), 2))])

# G= get_galaxies(INP)
# # print((G))
# G= shift_galaxies(G)
# print([pair for pair in list(combinations(G.keys(), 2))])
# print([manhattan_distance(*pair) for pair in list(combinations(G.keys(), 2))])
# print(sum([manhattan_distance(*pair) for pair in list(combinations(G.keys(), 2))]))

print(p1())

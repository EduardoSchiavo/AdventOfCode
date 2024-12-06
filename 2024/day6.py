import sys
with open("inputs/input6.txt") as ifile:
    MAP = {(lidx, ridx): char for lidx,  line in enumerate(
        ifile.read().splitlines()) for ridx, char in enumerate(line)}
    START = [k for k in MAP.keys() if MAP[k] == '^'][0]

# print(MAP)
# print(START)

sys.setrecursionlimit(10000)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_next(start: tuple, map: dict, turns: int) -> str:
    return (start[0] + DIRS[turns%4][0], start[1] + DIRS[turns%4][1])


def has_next(start: tuple, map: dict, turns: int) -> bool:
    try:
        map[get_next(start, map, turns)]
        return True
    except KeyError:
        return False


def find_path(start: tuple, map: dict, turns: int) -> list:
    seen = [start]
    
    if not has_next(start, map, turns):
        return seen

    next = get_next(start, map, turns) 
    while map[next] == "#":
        turns += 1
        next = get_next(start, map, turns) 
    
    seen.extend(find_path(next, map, turns))
    return seen


def p1():
    visited = find_path(START, MAP, 0)
    return len(set(visited))



#BRUTEFORE
def p2(path: list[tuple]):
    tot =0
    for pos in path:
        copy = MAP.copy()
        copy[pos] = '#'
        try:
            find_path(START, copy, 0)
        except RecursionError:
            tot +=1
    return tot


    



print(p1())
print(p2(list(set(find_path(START, MAP, 0)))))

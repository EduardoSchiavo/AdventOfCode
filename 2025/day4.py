with open('inputs/input4.txt') as ifile:
    inp = ifile.read().splitlines()


GRID = {(i, j): inp[i][j]
        for i in range(len(inp))
        for j in range(len(inp[0]))}

ADJ = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def add_up(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


def p1():
    tot = 0
    for k, v in GRID.items():
        if v != '@':
            continue
        if is_accessible(k, v, GRID):
            tot += 1
    return tot

def p2():
    tot = 0
    g = GRID
    while (True):
        g, removed = remove_rolls(g)
        tot += removed
        if (removed == 0):
            return tot

def is_accessible(k: tuple, v: str, grid: dict) -> bool:
    n = 0
    for tup in ADJ:
        check = add_up(tup, k)
        if check in grid.keys() and grid[check] == '@':
            n += 1
    if n < 4:
        return True
    return False


def remove_rolls(grid: dict):
    old_grid = grid.copy()
    new_grid = grid.copy()
    tot = 0
    for k, v in old_grid.items():
        if v != '@':
            continue
        if is_accessible(k, v, old_grid):
            tot +=1
            new_grid[k] = '.'
    return new_grid, tot


assert p1() == 1389
assert p2() == 9000

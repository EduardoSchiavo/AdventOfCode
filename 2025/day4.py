with open('inputs/input4.txt') as ifile:
    inp = ifile.read().splitlines()


GRID = {}
for i in range(len(inp)):
    for j in range(len(inp[0])):
        GRID[i, j] = inp[i][j]

print(inp)
print(GRID)

ADJ = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def add_up(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


def p1():
    tot = 0
    for k, v in GRID.items():
        if v != '@':
            continue
        n = 0
        for tup in ADJ:
            check = add_up(tup, k)
            if check in GRID.keys() and GRID[check] == '@':
                n += 1
        if n < 4:
            tot += 1
            print(k)
    return tot

def remove_rolls(grid: dict):
    old_grid = grid.copy()
    new_grid = grid.copy()
    tot = 0
    for k, v in old_grid.items():
        if v != '@':
            continue
        n = 0
        for tup in ADJ:
            check = add_up(tup, k)
            if check in old_grid.keys() and old_grid[check] == '@':
                n += 1
        if n < 4:
            tot += 1
            new_grid[k]='.'
    return new_grid, tot


def p2():
    tot=0
    g = GRID
    while(True):
        g, removed = remove_rolls(g)
        tot += removed
        if (removed == 0):
            return tot




# print(p1())
print(p2())

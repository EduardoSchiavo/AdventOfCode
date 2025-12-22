from functools import cache
with open('inputs/input7.txt') as ifile:
    inp = ifile.read().splitlines()

DIAGRAM = {(i, j): inp[i][j] for i in range(len(inp))
           for j in range(len(inp[0])) if inp[i][j] != '.'}


for k in DIAGRAM.keys():
    if DIAGRAM[k] == 'S':
        START = k

OUT = len(inp)


def p1():
    return len(explore_paths(START))

def p2():
    return explore_rec(START)

#probably don't need two separate DFS implementations... but I can't be bother to refactor it
def explore_paths(start: tuple):
    stack = [start]
    splitted = set()

    while (stack):
        curr = stack.pop()
        is_out = False
        while curr not in DIAGRAM or curr == start:
            curr = (curr[0]+2, curr[1])
            if curr[0]+2 >= OUT:
                splitted.add(curr)
                is_out = True
                break
        if is_out or curr in splitted:
            continue
        else:
            stack.append((curr[0]+2, curr[1]-1))
            stack.append((curr[0]+2, curr[1]+1))
            splitted.add(curr)
    return set([s for s in splitted if s in DIAGRAM])


@cache
def explore_rec(start: tuple):
    n = 0 
    
    if start[0] >= OUT:
        return 1

    if start not in DIAGRAM:
        n  += explore_rec((start[0]+2, start[1]))
    else:
        n += explore_rec((start[0]+2, start[1]-1))
        n += explore_rec((start[0]+2, start[1]+1))
    
    return n




assert p1() == 1630
assert p2() == 47857642990160

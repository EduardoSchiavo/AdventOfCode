from functools import cache
with open('inputs/input7.txt') as ifile:
    inp = ifile.read().splitlines()

DIAGRAM = {(i, j): inp[i][j] for i in range(len(inp))
           for j in range(len(inp[0])) if inp[i][j] != '.'}


for k in DIAGRAM.keys():
    if DIAGRAM[k] == 'S':
        START = k

OUT = len(inp)
print(f"max size is : {len(inp)}")


def p1():
    return len(explore_paths(START))


def explore_paths(start: tuple):
    stack = [start]
    splitted = set()

    while (stack):
        curr = stack.pop()
        # print(f"curr: {curr}")
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
    print(f"splitted: {set([s for s in splitted if s in DIAGRAM])}")
    print(f"--- {len([s for s in splitted if s in DIAGRAM])}")
    return set([s for s in splitted if s in DIAGRAM])



print(f"p1: {p1()}")

print("-------")
# print(count_paths(START))




def explore_paths2(start: tuple):
    q = [start]
    tot = 0

    while q:
        curr = q.pop(0)
        # print(f"curr: {curr}")
        if curr[0] >= OUT:
            tot +=1
        if curr in DIAGRAM:
            q.append((curr[0]+2, curr[1]-1))
            q.append((curr[0]+2, curr[1]+1))
        elif curr[0]+2 <= OUT:
            q.append((curr[0]+2, curr[1]))
    return tot

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


# print(f"p2: {explore_paths2(START)}")
print(f"p2: {explore_rec(START)}")

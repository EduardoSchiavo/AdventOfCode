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


def count_paths(start: tuple):
    stack = [[start]]
    splitted = set()
    visited = []
    count = 0
    while (stack):
        curr_path = stack.pop()
        curr = curr_path[-1]
        is_out = False
        while curr not in DIAGRAM or curr == start:
            curr = (curr[0]+2, curr[1])
            if curr[0] >= OUT:
                if curr in DIAGRAM:
                    splitted.add(curr)
                # visited.append(curr_path)
                is_out = True
                count +=1
                break
        if is_out:
            continue
        else:
            stack.append([curr_path, (curr[0]+2, curr[1]-1)])
            stack.append([curr_path, (curr[0]+2, curr[1]+1)])
            splitted.add(curr)
            # visited.append(curr_path)
    return count

print(f"p1: {p1()}")

print("-------")
# print(count_paths(START))

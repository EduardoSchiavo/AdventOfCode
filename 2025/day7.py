with open('inputs/input7.txt') as ifile:
    inp = ifile.read().splitlines()

print(inp)
DIAGRAM = {(i, j): inp[i][j] for i in range(len(inp))
           for j in range(len(inp[0])) if inp[i][j] != '.'}


for k in DIAGRAM.keys():
    if DIAGRAM[k] == 'S':
        START = k


print(f"start: {START}")
# # refactor later
# SPLITTER_MAP = {}
# for i in range(len(inp)):
#     if i % 2 == 0:
#         SPLITTER_MAP[i] = []
#     for j in range(len(inp[0])):
#         if inp[i][j] not in ('.', 'S'):
#             SPLITTER_MAP[i].append(j)


print(DIAGRAM)
OUT = len(inp)
print(f"max size is : {len(inp)}")


def propagate_beam(start: tuple):
    splitted = set()

    # base case
    if start[0] == OUT:
        return splitted

    if start in splitted:
        return splitted

    if start not in DIAGRAM:
        splitted.update(propagate_beam((start[0]+2, start[1])))
    else:
        splitted.add(start)
        # probably could start from next row
        splitted.update(propagate_beam((start[0]+2, start[1]-1)))
        splitted.update(propagate_beam((start[0]+2, start[1]+1)))

    return splitted



def explore_paths(start: tuple):
    stack = [start]
    splitted = set()

    while (stack):
        curr = stack.pop()
        # print(f"curr: {curr}")
        is_out = False
        while curr not in DIAGRAM or curr==start:
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
        

print(explore_paths(START))
print("-----")
print(len(explore_paths(START)))



for k, val in DIAGRAM.items():
    if k in explore_paths(START):
        pass
    else:
        print(k, val)

#

# print(SPLITTER_MAP)







# def compare_rows(rowA: list, rowB: list)-> int:
#     staggered = 0
#     for b in rowB:
#         for a in rowA:
#             if abs(a-b) ==1:
#                 staggered +=1
#                 break
#     return staggered
#
#
# def p1():
#     tot =1
#     for i in range(2, len(SPLITTER_MAP.keys())*2-2, 2):
#         print(f"comparing {SPLITTER_MAP[i]} AND {SPLITTER_MAP[i+2]}")
#         tot += compare_rows(SPLITTER_MAP[i], SPLITTER_MAP[i+2])
#     return tot
#
# print(compare_rows(SPLITTER_MAP[8], SPLITTER_MAP[10]))
# print(compare_rows(SPLITTER_MAP[12], SPLITTER_MAP[14]))
# print(p1())

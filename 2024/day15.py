with open("inputs/input15.txt") as ifile:
    MAP, INSTRUCTIONS = ifile.read().split("\n\n")
    MAP = {(x, y): val for x, row in enumerate(MAP.split("\n"))
           for y, val in enumerate(row)}
INSTRUCTIONS = INSTRUCTIONS.replace('\n', '')

DIRS = {'<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)}

BOUNDS = tuple(map(max, zip(*MAP.keys())))

START = [pos for pos in MAP.keys() if MAP[pos] == '@'][0]


def step(start: tuple, dir: str, space: dict):

    bounds = tuple(map(max, zip(*space.keys())))
    pos = start
    robot = pos
    checked = []
    while (0 < pos[0] < bounds[0] and 0 < pos[1] < bounds[1]):
        next = tuple(map(sum, zip(pos, DIRS[dir])))
        checked.append(next)
        if space.get(next, '.') == '.':
            space[start] = '.'
            for i in range(1, len(checked)):
                space[checked[len(checked)-i]] = space[checked[len(checked)-i-1]]
                del space[checked[len(checked)-i-1]]
            space[checked[0]] = '@'
            robot = tuple(map(sum, zip(start, DIRS[dir])))
            break
        if space.get(next) == '#':
            break
        pos = next
    return robot


def walk(start: tuple, space: dict, moves: str):
    pos = start
    for move in moves:
        pos = step(pos, move, space)


def enlarge(space: dict):
    warehouse = {}
    increments = {p[0]: 0 for p in space.keys()}
    new_vals = {".": "..", "#": "##", "O": "[]", "@": "@."}
    for i, p in enumerate(space.keys()):
        v = new_vals[space[p]]
        warehouse[(p[0], p[1]+increments[p[0]])] = v[0]
        warehouse[(p[0], p[1]+1+increments[p[0]])] = v[1]
        increments[p[0]] += 1
    return warehouse


def step2(start: tuple, dir: str, space: dict):
    if dir in "<>":
        return step(start, dir, space)
    robot = start
    stack = [start]
    checked = set()

    while (stack):
        pos = stack.pop()
        checked.add(pos)
        n = tuple(map(sum, zip(pos, DIRS[dir])))
        if space.get(n) == "[":
            stack.extend([n, (n[0], n[1]+1)])
        elif space.get(n) == "]":
            stack.extend([n, (n[0], n[1]-1)])
        elif space.get(n) == "#":
            return robot
    checked = sorted(checked, key=lambda t: t[0])
    if dir == "v":
        checked = reversed(checked)
    for p in checked:
        space[tuple(map(sum, zip(p, DIRS[dir])))] = space.get(p)
        if space.get(p):
            del space[p]
        

    robot = tuple(map(sum, zip(robot, DIRS[dir])))
    space[robot] = "@"
    return robot


def p1():
    wh = MAP.copy()
    walk(START, wh, INSTRUCTIONS)
    boxes = [p for p in wh.keys() if wh[p] == 'O']
    return sum(100*box[0]+box[1] for box in boxes)



def p2():
    nw = enlarge(MAP)
    new_start = [pos for pos in nw.keys() if nw[pos] == '@'][0]
    pos = new_start
    for m in INSTRUCTIONS:
        pos = step2(pos, m, nw)
    boxes = [p for p in nw.keys() if nw[p] == '[']
    return sum(100*box[0]+box[1] for box in boxes)


print(p1())

print(p2())

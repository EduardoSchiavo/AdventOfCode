with open("examples/example15.txt") as ifile:
    MAP, INSTRUCTIONS = ifile.read().split("\n\n")
    MAP = {(x, y): val for x, row in enumerate(MAP.split("\n"))
           for y, val in enumerate(row)}
INSTRUCTIONS = INSTRUCTIONS.replace('\n', '')
print(MAP)
print(INSTRUCTIONS)

DIRS = {'<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)}

BOUNDS = tuple(map(max, zip(*MAP.keys())))

START = [pos for pos in MAP.keys() if MAP[pos] == '@'][0]


def step(start: tuple, dir: str, space: dict):
    pos = start
    robot = pos
    checked = []
    while (0 < pos[0] < BOUNDS[0] and 0 < pos[1] < BOUNDS[1]):
        next = tuple(map(sum, zip(pos, DIRS[dir])))
        checked.append(next)
        if space[next] == '.':
            # shift_everything
            space[start] = '.'
            for i in range(1, len(checked)):
                space[checked[i]] = space[checked[i-1]]
            space[checked[0]] = '@'
            robot = tuple(map(sum, zip(start, DIRS[dir])))
            break
        if space[next] == '#':
            break
        pos = next
    return robot


def walk(start: tuple, space: dict, moves: str):
    pos = start
    for move in moves:
        pos = step(pos, move, space)
        # print(MAP)


def p1():
    walk(START, MAP, INSTRUCTIONS)

    boxes = [p for p in MAP.keys() if MAP[p] == 'O']
    print("boxes", boxes)
    tot = 0
    for box in boxes:
        tot += 100*box[0]+box[1]

    return tot
# print(step(START, '<', MAP))


# print(MAP)
print(p1())

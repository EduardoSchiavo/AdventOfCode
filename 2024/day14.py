import math
with open("inputs/input14.txt") as ifile:
    INP = [[tuple(int(x) for x in a.split("=")[1].split(","))
            for a in r.split(" ")] for r in ifile.read().splitlines()]

BOUNDS = (101, 103)  # 101, 103


def display(occupied: set):
    for y in range(BOUNDS[1]):
        line = ""
        for x in range(BOUNDS[0]):
            if (x,y) in occupied:
                line += "#"
            else:
                line += "."
        print(line)


def step(robot: list[tuple], n: int) -> tuple:
    new_x = robot[0][0]+robot[1][0]*n
    new_x = new_x % BOUNDS[0]
    new_y = robot[0][1]+robot[1][1]*n
    new_y = new_y % BOUNDS[1]
    return new_x, new_y


def p1():
    quads = [0]*4
    for robot in INP:
        pos = step(robot, 100)
        if pos[0] < BOUNDS[0]//2 and pos[1] < BOUNDS[1]//2:
            quads[0] += 1
        elif pos[0] < BOUNDS[0]//2 and pos[1] > BOUNDS[1]//2:
            quads[1] += 1

        elif pos[0] > BOUNDS[0]//2 and pos[1] < BOUNDS[1]//2:
            quads[2] += 1
        elif pos[0] > BOUNDS[0]//2 and pos[1] > BOUNDS[1]//2:
            quads[3] += 1
    return math.prod(quads)


def p2():
    for s in range(0, 6517):
        occupied = set()
        for robot in INP:
            pos = step(robot, s)
            occupied.add(pos)
        max_y = max([o[1] for o in occupied])
        for y in range(max_y):
            x_coords = sorted([o[0] for o in occupied if o[1] == y])
            consecutive = 0
            for i in range(1, len(x_coords)):
                if x_coords[i] -x_coords[i-1] == 1:
                    consecutive += 1
                if consecutive >= 20:
                    return s

print(p1())
print(p2())

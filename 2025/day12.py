with open("inputs/input12.txt") as ifile:
    inp = ifile.read()


*presents_s, spaces = inp.split("\n\n")


PRESENTS = {}
for p in presents_s:
    lines = p.split('\n')
    PRESENTS[int(lines[0].strip(':'))] = sum(c == '#' for row in lines[1:] for c in row)


REGIONS = []
for s in spaces.strip('\n').split('\n'):
    size, boxes = s.split(': ')
    size = tuple(map(int, size.split('x')))
    boxes = tuple(map(int, boxes.split(' ')))
    REGIONS.append((size, boxes))


def p1():
    tot = 0
    for reg in REGIONS:
        max_size = reg[0][0] * reg[0][1]
        occupied = 0
        for idx, qty in enumerate(reg[1]):
            occupied += qty * PRESENTS[idx]
        if max_size >= occupied:
            tot += 1
    return tot


assert p1() == 403

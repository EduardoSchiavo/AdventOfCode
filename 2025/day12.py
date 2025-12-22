with open("inputs/input12.txt") as ifile:
    inp = ifile.read()



*presents_s, spaces = inp.split("\n\n")

PRESENTS = {}
for p in presents_s:
    lines = p.split('\n')
    PRESENTS[int(lines[0].strip(':'))] = lines[1:]

print(PRESENTS)

print(spaces)

REGIONS = []
for s in spaces.strip('\n').split('\n'):
    size, boxes = s.split(': ')
    size = tuple(map(int, size.split('x')))
    boxes = tuple(map(int, boxes.split(' ')))
    print(size, boxes)
    REGIONS.append((size, boxes))


def occupies(box: list[str]):
    tot = 0
    for l in box:
        for c in l:
            if c == '#':
                tot +=1
    return tot


def p1():
    tot = 0
    for reg in REGIONS:
        max_size = reg[0][0] * reg[0][1]
        occupied = 0
        for idx, qty in enumerate(reg[1]):
            # print(idx, qty)
            occupied += qty * occupies(PRESENTS[idx])
        if max_size >= occupied:
            print(occupied)
            tot += 1
    return tot



def p2():
    pass


print(f" p1: {p1()}")

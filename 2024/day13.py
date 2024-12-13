with open("inputs/input13.txt") as ifile:
    INP = [[a.split(":")[1].strip() for a in block.split("\n")]
           for block in ifile.read().rstrip("\n").split("\n\n")]


def extract_coordinates(block: list[str], offset: int):
    a = tuple(int(num.split("+")[1]) for num in block[0].split(","))
    b = tuple(int(num.split("+")[1]) for num in block[1].split(","))

    t = tuple(int(num.split("=")[1]) +
              offset for num in block[2].split(","))
    return a, b, t


def solve(rules: tuple):
    a, b, t = rules

    y = round((t[1] - a[1]*t[0]/a[0])/(b[1]-(a[1]*b[0])/a[0]), 3)
    x = round((t[0] - b[0]*y)/a[0], 3)

    if not x.is_integer() or not y.is_integer():
        return 0, 0

    return int(x), int(y)


def score(offset: int):
    tot = 0
    for game in INP:
        rules = extract_coordinates(game, offset)
        a, b = solve(rules)
        tot += a*3+b
    return int(tot)

def p1():
    return score(0)

def p2():
    return score(10000000000000)

print(p1())
print(p2())

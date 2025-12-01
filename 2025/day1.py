with open('inputs/input1.txt') as ifile:
    inp = ifile.read().splitlines()


def p1():
    tot = 0
    curr = 50
    for dial in inp:
        # print(curr)
        if dial[0] == 'R':
            curr = (curr + int(dial[1:])) % 100
        else:
            curr = (curr - int(dial[1:])) % 100

        if curr == 0:
            tot += 1

    return tot


def p2():
    tot = 0
    curr = 50
    for dial in inp:
        val = int(dial[1:])
        prev = curr
        if dial[0] == 'R':
            curr = (curr + val) % 100
            if (curr < prev or curr == 0) and prev != 0:
                tot += 1
        else:
            curr = (curr - val) % 100
            if (curr > prev or curr == 0) and prev!= 0:
                tot += 1
        tot += val //100 
    return tot


print(f"p1: {p1()}")
print(f"p2: {p2()}")

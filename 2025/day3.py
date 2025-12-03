with open('inputs/input3.txt') as ifile:
    inp = ifile.read().splitlines()

print(inp)


def get_joltage(bank: str):

    l = "0"
    stop = 0
    for i in range(len(bank)-1):
        if int(bank[i]) > int(l):
            l = bank[i]
            stop = i
    r = bank[-1]
    for i in bank[-1:stop:-1]:
        # print(f"eeee {i}")
        if int(i) > int(r):
            r = i
    return int(l+r)


def p1():
    tot = 0
    for bank in inp:
        tot += get_joltage(bank)
    return tot


def get_joltage_2(bank: str, l: int):  # parametrize the num later
    num = ''
    stop = 0

    for i in range(1,l+1):
        curr = "0"
        # print(f"from {stop} up to {len(bank)-l+i}")
        for idx, val in enumerate(bank[stop:len(bank)-l+i]):
            # print(f"iteration: {i}, value: {val}, idx: {idx}, print: {stop}, curr: {curr}")
            if int(val) > int(curr):
                curr = val
                stopped_at=idx+1
        stop +=stopped_at 
        num += curr
    print(f"returning {num}")
    return int(num)

def p2():
    tot = 0
    for bank in inp:
        tot += get_joltage_2(bank, 2)
    return tot

# print(f"p1: {p1()}")
print(f"p2: {p2()}")

# print(get_joltage_2("811111111111119", 12))
# print(get_joltage_2("234234234234278", 12))

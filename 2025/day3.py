with open('inputs/input3.txt') as ifile:
    inp = ifile.read().splitlines()


def p1():
    return add_up_joltage(2)


def p2():
    return add_up_joltage(12)


def add_up_joltage(batteries_num: int) -> int:
    return sum(get_joltage(bank, batteries_num) for bank in inp)


def get_joltage(bank: str, batteries_num: int) -> int:
    joltage = ''
    start = 0
    for i in range(1, batteries_num+1):
        curr = "0"
        for idx, val in enumerate(bank[start:len(bank)-batteries_num+i]):
            if int(val) > int(curr):
                curr = val
                stopped_at = idx+1
        start += stopped_at
        joltage += curr
    return int(joltage)


assert p1() == 17412
assert p2() == 172681562473501

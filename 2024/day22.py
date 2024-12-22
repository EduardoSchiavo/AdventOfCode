with open("inputs/input22.txt") as ifile:
    SNS = list(map(int, ifile.read().splitlines()))


def generate_next(sn: int) -> int:
    s1 = ((sn*64) ^ sn) % 16777216
    s2 = ((s1//32) ^ s1) % 16777216
    s3 = ((s2*2048) ^ s2) % 16777216
    return s3


def p1():
    tot = 0
    for num in SNS:
        sn = num
        for i in range(2000):
            sn = generate_next(sn)
        tot += sn
    return tot


print(p1())

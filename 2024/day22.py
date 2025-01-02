import itertools
with open("inputs/input22.txt") as ifile:
    SNS = list(map(int, ifile.read().splitlines()))


def generate_next(sn: int) -> int:
    s1 = ((sn*64) ^ sn) % 16777216
    s2 = ((s1//32) ^ s1) % 16777216
    s3 = ((s2*2048) ^ s2) % 16777216
    return s3


def get_best_seq(sn: int) -> list[int]:
    best = {}
    prices = [sn % 10]
    for i in range(1, 2001):
        key = []
        sn = generate_next(sn)
        prices.append(sn % 10)
        if i < 4:
            continue
        for j in range(4):
            key.append(prices[i-j]-prices[i-j-1])
        if tuple(key) not in best:
            best[tuple(key)] = sn % 10
    return best


def p1():
    tot = 0
    for num in SNS:
        sn = num
        for i in range(2000):
            sn = generate_next(sn)
        tot += sn
    return tot


def get_all_keys():
    return tuple(itertools.product(range(-9, 10), repeat=4))


def p2():
    seqs = []
    for num in SNS:
        seqs.append(get_best_seq(num))
    keys = get_all_keys()
    bv = 0
    for k in keys:
        val = sum(s.get(k, 0) for s in seqs)
        if val > bv:
            bv = val

    return bv


print(p1())
print(p2())

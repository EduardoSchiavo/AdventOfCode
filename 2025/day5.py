with open('inputs/input5.txt') as ifile:
    RANGES, IDS = ifile.read().split('\n\n')
    RANGES = set([tuple(int(n) for n in r.split("-"))
                 for r in RANGES.splitlines()])
    IDS = set(int(n) for n in IDS.splitlines())


def p1():
    # tot = 0
    ranges = to_ranges(RANGES)
    # for id in IDS:
    #     for rng in ranges:
    #         if id in rng:
    #             tot += 1
    #             break
    # return tot
    return sum([any(id in rng for rng in ranges) for id in IDS])


def to_ranges(rngs: set[tuple]) -> set[range]:
    return set([range(t[0], t[1]+1) for t in rngs])


def p2():
    rngs = RANGES
    new_rngs = set()
    while (True):
        for g in rngs:
            for r in rngs:
                if max(g[0], r[0]) <= min(g[1], r[1]):  # intersection exists
                    if g in new_rngs:
                        new_rngs.remove(g)
                    g = tuple([min(g[0], r[0]), max(g[1], r[1])])
            new_rngs.add(g)

        if (new_rngs == rngs):
            break
        rngs = new_rngs.copy()

    return sum(r[1]-r[0]+1 for r in new_rngs)


assert p1() == 744
assert p2() == 347468726696961

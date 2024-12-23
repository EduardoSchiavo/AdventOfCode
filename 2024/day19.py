from functools import cache
with open("inputs/input19.txt") as ifile:
    T, P = ifile.read().split("\n\n")
    T = [t.strip() for t in T.split(",")]
    P = P.splitlines()


def get_candidates(c: str, avail: list[str]):
    candidates = []
    for a in avail:
        if a.startswith(c):
            candidates.append(a)
    return candidates


CAND = {}


@cache
def is_possible(p: int, word: str, avail: tuple[str], c: str = None):
    tot = 0
    if p > len(word):
        return False

    if c and p == len(word)-len(c) and is_valid(c, p, word):
        return True

    if c and not is_valid(c, p, word):
        return False

    if c and is_valid(c, p, word):
        p += len(c)

    if p > len(word)-1:
        return False

    if word[p] not in CAND:
        CAND[word[p]] = get_candidates(word[p], avail)

    for c in CAND[word[p]]:
        tot += is_possible(p, word, avail, c)

    return tot


def is_valid(c, p, word):
    if len(c) == 1:
        if c == word[p]:
            return True
        return False

    for i in range(len(c)):
        try:
            if c[i] != word[p+i]:
                return False
        except IndexError:
            return False
    return True


def p1():
    tot = 0
    for pat in P:
        if is_possible(0, pat, tuple(T)):
            tot += 1
    return tot


def p2():
    tot = 0
    for pat in P:
        tot += is_possible(0, pat, tuple(T))
    return tot


print(p1())
print(p2())

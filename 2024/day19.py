with open("inputs/input19.txt") as ifile:
    T, P = ifile.read().split("\n\n")
    T = [t.strip() for t in T.split(",")]
    P = P.splitlines()

# print(T)


def get_candidates(c: str, avail: list[str]):
    candidates = []
    for a in avail:
        # print(f"a: {a}")
        if a.startswith(c):
            candidates.append(a)
    return candidates



def is_possible(p: int, word: str, avail: list[str], seen: list, c: str = None):
    if (p, c) in seen:
        return False
    seen.append((p, c))

    if p > len(word):
        return False

    if c and p == len(word)-len(c) and is_valid(c, p, word):
        return True
    # print(f"p: {p}, c: {c}, word: {word}")

    if c and not is_valid(c, p, word):
        return False

    if c and is_valid(c, p, word):
        p += len(c)

    if p > len(word)-1:
        return False

    cand = get_candidates(word[p], avail)

    for c in cand:
        if is_possible(p, word, avail, seen, c):
            return True

    return False

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
        if is_possible(0, pat, T, []):
            tot +=1
            print(pat)
    return tot


print(p1())
# print(is_possible(0, "bwurrg", T, []))

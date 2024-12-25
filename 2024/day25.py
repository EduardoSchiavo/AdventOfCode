import itertools
with open("inputs/input25.txt") as ifile:
    SCHEM = [tuple(s.splitlines()) for s in ifile.read().split("\n\n")]


SWIDTH = 5

def convert_to_heights(scheme: tuple)-> list[int]:
    heights = []
    for i in range(SWIDTH):
        for j in range(len(scheme)):
            if scheme[j][i] == '.':
                heights.append(j-1)
                break
    return tuple(heights)


def separate_locks_and_keys(schemes: list):
    locks = []
    keys = []
    for s in schemes:
        if s[0] == '#####':
            locks.append(convert_to_heights(s))
        else:
            keys.append(convert_to_heights(s[::-1]))
    return tuple(locks), tuple(keys)



def is_match(lock: tuple, key: tuple):
    for i in range(SWIDTH):
        if lock[i] + key[i] > 5:
            return False
    return True

def  p1():
    ls, ks = separate_locks_and_keys(SCHEM)
    tot = 0
    for l in ls:
        for k in ks:
            tot += is_match(l, k)
    return tot



print(p1())

with open("inputs/input9.txt") as ifile:
    INP = ifile.read().strip('\n')


DISKS = [int(INP[i]) for i in range(0, len(INP), 2)]
MEM = [int(INP[i]) for i in range(1, len(INP), 2)]

# print(MEM)
#
#


def reallocate(disks: list, mem: list) -> list:
    repositioned = ["" for i in range(len(mem))]
    p = 0
    while (len(disks)-1 > p+2):
        curr_idx = len(disks)-1
        quantity = disks.pop()
        print(f"curr_idx: {curr_idx}, quantity {quantity}, p:{p}")

        while (quantity):
            diff = mem[p] - quantity
            if diff > 0:
                repositioned[p] += str(curr_idx)*quantity
                mem[p] = diff
                quantity = 0
            else:
                repositioned[p] += str(curr_idx)*mem[p]
                quantity = -diff
                p += 1
            if (curr_idx == p+1):
                repositioned[p] += str(curr_idx)*quantity
                break
            # print(f" c: {curr_idx}, p: {p}")
    return repositioned


def compute_str(disks: list, repos: list) -> str:
    res = ""
    for i in range(len(disks)):
        res += str(i)*disks[i]
        res += repos[i]
    return res


def score(to_score: str):
    res = 0
    for i in range(len(to_score)):
        res += i*int(to_score[i])
    return res


repos = reallocate(DISKS, MEM)
print(repos)
a = compute_str(DISKS, repos)
print(score(a))

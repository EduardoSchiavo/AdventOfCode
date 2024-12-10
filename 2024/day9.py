with open("inputs/input9.txt") as ifile:
    INP = ifile.read().strip('\n')


DISKS = [int(INP[i]) for i in range(0, len(INP), 2)]
MEM = [int(INP[i]) for i in range(1, len(INP), 2)]


def reallocate_blocks(disks: list, mem: list) -> list:
    repositioned = [[0]*mem[i] for i in range(len(mem))]
    for i, q in reversed(list(enumerate(disks))):
        for j in range(len(mem)):
            if i<=j:
                break
            if mem[j] >= q:
                taken = sum(x != 0 for x in repositioned[j])
                for k in range(q):
                    repositioned[j][k+taken] = i
                disks[i] = str(q)
                mem[j] -= q
                break
    return repositioned


def checksum_p2(disks: list, repos: list) -> int:
    tot = 0
    offset = 0
    for i in range(len(disks)):
        if isinstance(disks[i], str):
            offset += int(disks[i])
        else:
            for j in range(disks[i]):
                tot += (j+offset)*i
            offset += disks[i]
        try:
            for k in range(len(repos[i])):
                tot += (k+offset)*repos[i][k]
            offset += len(repos[i])
        except IndexError:
            pass
    return tot


def reallocate(disks: list, mem: list) -> list:
    repositioned = [[] for i in range(len(mem))]
    p = 0
    done = False
    while (not done):
        curr_idx = len(disks)-1
        quantity = disks.pop()
        while (quantity):
            diff = mem[p] - quantity
            if diff > 0:
                repositioned[p].extend([curr_idx]*quantity)
                mem[p] = diff
                quantity = 0
            else:
                repositioned[p].extend([curr_idx]*mem[p])
                quantity = -diff
                p += 1
            if (curr_idx <= p+1):
                repositioned[p].extend([curr_idx]*quantity)
                done = True
                break

    return repositioned


def checksum_p1(disks: list, repos: list) -> str:
    tot = 0
    offset = 0
    for i in range(len(disks)):
        for j in range(disks[i]):
            tot += (j+offset)*i
        offset += disks[i]
        for k in range(len(repos[i])):
            tot += (k+offset)*repos[i][k]
        offset += len(repos[i])

    return tot




def p1():
    disks = DISKS[:]
    mem = MEM[:]
    repos = reallocate(disks, mem)
    return checksum_p1(disks, repos)


def p2():
    repos = reallocate_blocks(DISKS, MEM)
    return checksum_p2(DISKS, repos)

print(p1())
print(p2())

with open('examples/example1.txt') as ifile:
    inp=ifile.read().split('\n\n')

elves=[elf.split() for elf in inp]
loads_per_elf=[sum([int(e) for e in elf]) for elf in elves]

# P1
print("part 1: ", max(loads_per_elf))

loads_per_elf.sort()
# P2
print("part 2: ", sum(loads_per_elf[-3:]))
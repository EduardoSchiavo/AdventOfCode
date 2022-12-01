with open('examples/example1.txt') as ifile:
    inp=ifile.read().split('\n\n')

load_per_elf=[sum([int(e) for e in elf]) for elf in [x.split() for x in inp]]

# P1
print("part 1: ", max(load_per_elf))

load_per_elf.sort()
# P2
print("part 2: ", sum(load_per_elf[-3:]))
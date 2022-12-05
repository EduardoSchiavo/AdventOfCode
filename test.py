import regex as re

with open("examples/example5.txt") as ifile:
    PILES, MOVES = ifile.read().split('\n\n')


# PILES=PILES.split('\n')
# PILES.reverse()
# MOVES=MOVES.split('\n')

print(PILES)

exp=re.compile(r"\[\w\]")

print(exp.findall(PILES))
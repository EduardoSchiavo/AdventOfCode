import regex as re

with open("examples/example5.txt") as ifile:
    PILES, MOVES = ifile.read().split('\n\n')


PILES=PILES.split('\n')
PILES.reverse()
MOVES=MOVES.split('\n')


# assign values based on string indices
crates=[[] for col in range(len(PILES[0]))]
for level in PILES:
    for col in range(len(PILES[0])):
       crates[col].append(level[col])

#filter out useless columns
crates = [crate for crate in crates if crate[0] != ' ']
#convert to dict
keys = [crate[0] for crate in crates]
vals = [[val for val in crate[1:] if val != ' '] for crate in crates]
crates_dict = {k:v for k,v in zip(keys, vals)}

print(crates_dict)


print(MOVES)

def parse_move(move: str)-> tuple:
    exp=re.compile(r"move (\d*) from (\d*) to (\d*)")
    return exp.search(move).group(1, 2, 3)

def execute_move(piles_of_crates: dict, quantity: str, starting_pile: str, destination: str, element_wise=False)-> None:
    if element_wise:
        piles_of_crates[destination].extend(reversed(piles_of_crates[starting_pile][-int(quantity):]))
    else:
        piles_of_crates[destination].extend(piles_of_crates[starting_pile][-int(quantity):])
    piles_of_crates[starting_pile]=piles_of_crates[starting_pile][:-int(quantity)]
    return piles_of_crates

def shift_crates(list_of_instructions:list, piles_of_crates: dict, element_wise=False)-> dict:
    for instruction in list_of_instructions:
        piles_of_crates = execute_move(
            piles_of_crates, *parse_move(instruction), element_wise
        )
    return piles_of_crates

def solution(piles_of_crate: dict)-> str:
    return ''.join([val[-1] for val in piles_of_crate.values()])


# print(solution(shift_crates(MOVES, crates_dict, element_wise=True)))


print(solution(shift_crates(MOVES, crates_dict)))




import regex as re

with open("examples/example5.txt") as ifile:
    PILES, MOVES = ifile.read().split("\n\n")

PILES = PILES.split("\n")
PILES.reverse()
MOVES = MOVES.split("\n")

def parse_piles(piles: list) -> dict:
    crates = [[] for col in range(len(piles[0]))]
    for level in piles:
        for col in range(len(piles[0])):
            crates[col].append(level[col])
    crates = [crate for crate in crates if crate[0] != " "]
    return {
        k: v
        for k, v in zip(
            [crate[0] for crate in crates],
            [[val for val in crate[1:] if val != " "] for crate in crates],
        )
    }

def parse_move(move: str) -> tuple:
    exp = re.compile(r"move (\d*) from (\d*) to (\d*)")
    return exp.search(move).group(1, 2, 3)

def execute_move(
    piles_of_crates: dict,
    quantity: str,
    starting_pile: str,
    destination: str,
    direction=1,
) -> None:
    piles_of_crates[destination].extend(
        piles_of_crates[starting_pile][-int(quantity) :][:: -1 * direction]
    )
    piles_of_crates[starting_pile] = piles_of_crates[starting_pile][: -int(quantity)]
    return piles_of_crates

def shift_crates(
    list_of_instructions: list, piles_of_crates: dict, direction=1
) -> dict:
    for instruction in list_of_instructions:
        piles_of_crates = execute_move(
            piles_of_crates, *parse_move(instruction), direction
        )
    return piles_of_crates

def solution(piles_of_crate: dict) -> str:
    return "".join([val[-1] for val in piles_of_crate.values()])

def part_1(piles, moves):
    return solution(shift_crates(moves, parse_piles(piles)))

def part_2(piles, moves):
    return solution(shift_crates(moves, parse_piles(piles), direction=-1))

print(part_1(PILES, MOVES))
print(part_2(PILES, MOVES))

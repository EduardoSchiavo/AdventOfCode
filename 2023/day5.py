from dataclasses import dataclass


with open('inputs/input5.txt') as ifile:
    inp=ifile.read()

print(inp.split('\n\n'))

STARTING_SEEDS=inp.splitlines()[0].split(': ')[1].split(' ')

print(STARTING_SEEDS)

LINE_SEPARATED_INP =inp.split('\n\n')



class Instruction:

    def __init__(self,     destination_start: int,
    source_start: int,
    span: int) -> None:
        self.destination_start= int(destination_start)
        self.source_start= int(source_start)
        self.span= int(span)

    def get_matching(self, source_element: int):
        updated = False
        if self.source_start <= source_element < self.source_start + self.span:
            updated=True
            return self.destination_start + (source_element - self.source_start), updated
        return source_element, updated


        
def parse_mapper(map_string: str):
    return [Instruction(*entry.split(' ')) for entry in map_string.split("\n")[1:]]


MAPS = [parse_mapper(LINE_SEPARATED_INP[i]) for i in range(1, 8)]


def seed_path(seed: int)-> int:
    current = seed
    for map in MAPS:
        for instruction in map:
            current, updated=instruction.get_matching(current)
            if updated: 
                break
    return current


def p1():
    return min([seed_path(int(seed)) for seed in STARTING_SEEDS])


print(p1()) #282277027

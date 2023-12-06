from dataclasses import dataclass
from random import seed
import time


# with open('examples/example5.txt') as ifile:
#     inp=ifile.read()


with open('input5.txt') as ifile:
    inp=ifile.read()

# print(inp.split('\n\n'))

STARTING_SEEDS=inp.splitlines()[0].split(': ')[1].split(' ')

# print(STARTING_SEEDS)

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

    #test for p2
    def reverse_get_matching(self, destination_element: int):
        updated = False
        if self.destination_start <= destination_element < self.destination_start + self.span:
            updated=True
            return self.source_start + (destination_element - self.destination_start), updated
        return destination_element, updated
        
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
# print(p1()) #282277027


# ##p2

def update_seeds(seeds:list)-> list:
    updated_seeds=[]
    for i in range(0, int(len(seeds)), 2):
        updated_seeds.extend([(int(seeds[i]), int(seeds[i])+int(seeds[i+1]))])
    return updated_seeds

def is_starting_seed(seed: int, starting_seeds: list[tuple]):
    return any(lower<= seed < upper for (lower, upper) in starting_seeds)



def sort_by_destination(map: list[Instruction]):
    return sorted( map, key=lambda x: x.destination_start)

def location_path(location: int, maps: list[list[Instruction]])-> int:
    current = location
    for map in maps:
        for instruction in map:
            current, updated=instruction.reverse_get_matching(current)
            if updated: 
                break
    return current


NEW_MAPS = reversed(MAPS)
print('maps reversed')

def compute_locations(last_map):
    locations = []
    for inst in last_map:
        locations.extend([(inst.destination_start, inst.destination_start+inst.span)])
    return sorted(locations, key=lambda x:x[0])
                         


LOCATIONS = compute_locations(MAPS[-1])
SEED_RANGES = update_seeds(STARTING_SEEDS)
print(LOCATIONS)
print(SEED_RANGES)

def p2():
    a = time.time()
    for loc in range(0, LOCATIONS[-1][-1]):
        seed = location_path(loc, MAPS[::-1])
        if is_starting_seed(seed, SEED_RANGES):
            print(time.time()-a)
            return loc
    return None

print(p2())






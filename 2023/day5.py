from dataclasses import dataclass
from random import seed


with open('examples/example5.txt') as ifile:
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

# ##p2

def update_seeds(seeds:list)-> list:
    updated_seeds=[]
    for i in range(0, int(len(seeds)), 2):
        # print([*range(int(seeds[i]), int(seeds[i])+int(seeds[i+1]))])
        updated_seeds.extend([(int(seeds[i]), int(seeds[i])+int(seeds[i+1]))])
    return updated_seeds

def is_starting_seed(seed: int, starting_seeds: list[tuple]):
    return any(lower<= seed < upper for (lower, upper) in starting_seeds)

# def generate_map(instructions: list[Instruction])-> dict:
#     source_to_destination_map={}
#     for inst in instructions:
#         for source_elem, destination_elem in zip(range(inst.source_start, inst.source_start+inst.span), range(inst.destination_start, inst.destination_start+inst.span)):
#             source_to_destination_map[source_elem]= destination_elem
#     return source_to_destination_map

# def generate_maps(map_list: list):
#     return [generate_map(insts) for insts in map_list]

# def lookup_path(seed: str, maps: list[dict]):
#     current=seed
#     for map in maps: #7
#         current=map.get(current, current)
#     return current

# def p2():
#     new_maps=generate_maps(MAPS)
#     print('maps created')
#     new_seeds=update_seeds(STARTING_SEEDS)
#     return [lookup_path(seed, new_maps) for seed in new_seeds]




# print(min(p2()))





# print(p1()) #282277027

# print(update_seeds(STARTING_SEEDS))

# print(generate_map(MAPS[0]))

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



# print(sort_by_destination(MAPS[-1]))

# NEW_SEEDS = update_seeds(STARTING_SEEDS)
# print('seeds_computed')

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

def test():
    for chunk in LOCATIONS:
        for loc in chunk:
            seed = location_path(loc, MAPS[::-1])
            if is_starting_seed(seed, SEED_RANGES):
                return seed
    return None
print(test())




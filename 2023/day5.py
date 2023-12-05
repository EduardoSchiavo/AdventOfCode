from dataclasses import dataclass


with open('examples/example5.txt') as ifile:
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



#TODO refactor this shit
SEED_TO_SOIL=parse_mapper(LINE_SEPARATED_INP[1])
print(SEED_TO_SOIL)
SOIL_TO_FERTILIZER=parse_mapper(LINE_SEPARATED_INP[2])
print(SOIL_TO_FERTILIZER)
FERTILIZER_TO_WATER=parse_mapper(LINE_SEPARATED_INP[3])
print(FERTILIZER_TO_WATER)
WATER_TO_LIGHT=parse_mapper(LINE_SEPARATED_INP[4])
print(WATER_TO_LIGHT)
LIGHT_TO_TEMPERATURE=parse_mapper(LINE_SEPARATED_INP[5])
print(LIGHT_TO_TEMPERATURE)
TEMPERATURE_TO_HUMIDITY=parse_mapper(LINE_SEPARATED_INP[6])
print(TEMPERATURE_TO_HUMIDITY)
HUMIDITY_TO_LOCATION=parse_mapper(LINE_SEPARATED_INP[7])
print(HUMIDITY_TO_LOCATION)


def seed_path(seed: int)-> int:
    current = seed
    for instruction in SEED_TO_SOIL:
        current, updated=instruction.get_matching(current)
        if updated: 
            break
    # print(current)
    for instruction in SOIL_TO_FERTILIZER:
        current, updated=instruction.get_matching(current)
        if updated: 
            break    
    # print(current)
    for instruction in FERTILIZER_TO_WATER:
        current, updated=instruction.get_matching(current)
        if updated: 
            break
    # print(current)
    for instruction in WATER_TO_LIGHT:
        current, updated=instruction.get_matching(current)
        if updated: 
            break    
    for instruction in LIGHT_TO_TEMPERATURE:
        current, updated=instruction.get_matching(current)
        if updated: 
            break    
    for instruction in TEMPERATURE_TO_HUMIDITY:
        current, updated=instruction.get_matching(current)
        if updated: 
            break
    for instruction in HUMIDITY_TO_LOCATION:
        current, updated=instruction.get_matching(current)
        if updated: 
            break    
    return current

# print(seed_path(79)) #82
# print(seed_path(14)) #43
# print(seed_path(55)) #86
# print(seed_path(13)) #35


def p1():
    return min([seed_path(int(seed)) for seed in STARTING_SEEDS])


print(p1())
# print(FERTILIZER_TO_WATER[0].__dict__)
# print(FERTILIZER_TO_WATER[1].get_matching(49))
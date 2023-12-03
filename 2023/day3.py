with open('inputs/input3.txt') as ifile:
    INP=[list(line) for line in ifile.read().splitlines()]

print(INP)

UNALLOWED_SYMBOLS = ".1234567890"

BLACKLIST: list[tuple] = []

def get_symbol_indices(schematic: list[list])-> list:
    symbol_indices=[]
    for r_idx, row in enumerate(schematic):
        for c_idx, element in enumerate(row):
            if element not in  UNALLOWED_SYMBOLS:
                print(element, (r_idx, c_idx))
                symbol_indices.append((r_idx, c_idx))
    return symbol_indices

def blacklist_coordinates(coords: tuple)-> None:
    BLACKLIST.append(coords)

def is_blacklisted(coords: tuple)-> bool:
    return coords in BLACKLIST

def collect_number_and_blacklist_indices(num_coordinates: tuple, schematic: list[list]):
    x, y = num_coordinates
    part_number = schematic[x][y]
    blacklist_coordinates(num_coordinates)
    i = 1

    while schematic[x][y-i].isnumeric() and y-1 >= 0:
        part_number = schematic[x][y-i] + part_number
        blacklist_coordinates((x, y-i))
        i += 1
    i = 1
    try:
        while schematic[x][y+i].isnumeric():
            part_number = part_number + schematic[x][y+i]
            blacklist_coordinates((x, y+i))
            i += 1
    except IndexError:
        print("reaching array edge")
    return part_number


def search_symbol_surroundings(symbol_coordinates: tuple, schematic: list[list]):
    x, y = symbol_coordinates
    modifiers = [(1,0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    part_numbers = []
    for mod in modifiers:
        print(mod)
        a = x+mod[0]
        b = y+mod[1]        
        if schematic[a][b].isnumeric():  #TODO turn ifs into a loop
            print(schematic[a][b])
            if not is_blacklisted((a, b)):
                part_numbers.append(collect_number_and_blacklist_indices((a, b), schematic))
    return part_numbers

def collect_all_part_numbers(schematic: list[list]):
    indices = get_symbol_indices(schematic)
    part_nums = []
    for index in indices:
        part_nums.extend(search_symbol_surroundings(index, schematic))
    print(BLACKLIST)
    return part_nums

def p1():
    return sum([int(num) for num in collect_all_part_numbers(INP)])




# indices = get_symbol_indices(INP)

# print(search_symbol_surroundings(indices[5], INP))
# print(BLACKLIST)

# print(collect_number_and_blacklist_indices((0, 1), INP))

print(p1()) #543867


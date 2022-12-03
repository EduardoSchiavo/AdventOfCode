with open('examples/example3.txt') as ifile:
    inp=ifile.read().splitlines()

# strings to lists
RUCKSACKS=[list(rucksack) for rucksack in inp]

def get_common_types(rucksacks: list)-> list:
    letters_in_common=[]
    for rucksack in rucksacks:        
        mid_point=len(rucksack)//2
        letters_in_common.append([letter for letter in rucksack[:mid_point] if letter in rucksack[mid_point:]][0])
    return letters_in_common

def part_1(rucksacks):
    common = get_common_types(rucksacks)
    return calculate_score(common)

def calculate_score(common):
    return sum([ord(letter)-(96-58*letter.isupper()) for letter in common])

def get_intersection(group_of_elves: list[list])-> list:
    return [letter for letter in group_of_elves[0] if letter in group_of_elves[1] and letter in group_of_elves[2]][0]

def part_2(rucksacks):
    common=[]
    for i in range(0, len(rucksacks), 3):
        common.append(get_intersection(rucksacks[i:i+3]))
    return calculate_score(common)

print("part one: ", part_1(RUCKSACKS))

print("part two:", part_2(RUCKSACKS))
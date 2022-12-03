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

COMMON = get_common_types(RUCKSACKS)

def part_1(common):
    return sum([ord(letter)-(96-58*letter.isupper()) for letter in common])

intersection_a_b = get_common_types(RUCKSACKS[:2])
print(intersection_a_b)

intesection_b_c= get_common_types(RUCKSACKS[1:2])

result=get_common_types([intersection_a_b, intesection_b_c])

print(intesection_b_c)

# print(part_1(COMMON))



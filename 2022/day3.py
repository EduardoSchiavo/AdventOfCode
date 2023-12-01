with open("examples/example3.txt") as ifile:
    inp = ifile.read().splitlines()

# strings to lists
RUCKSACKS = [list(rucksack) for rucksack in inp]


def get_common_types(rucksacks: list) -> list:
    return [
        [
            letter
            for letter in rucksack[: len(rucksack) // 2]
            if letter in rucksack[len(rucksack) // 2 :]
        ][0]
        for rucksack in rucksacks
    ]


def part_1(rucksacks):
    common = get_common_types(rucksacks)
    return calculate_score(common)


def calculate_score(common):
    return sum([ord(letter) - (96 - 58 * letter.isupper()) for letter in common])


def get_intersection(group_of_elves: list[list]) -> list:
    return list(
        set(group_of_elves[0]) & set(group_of_elves[1]) & set(group_of_elves[2])
    )[0]


def part_2(rucksacks):
    common = []
    for i in range(0, len(rucksacks), 3):
        common.append(get_intersection(rucksacks[i : i + 3]))
    return calculate_score(common)


print("part one: ", part_1(RUCKSACKS))

print("part two:", part_2(RUCKSACKS))

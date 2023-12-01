with open("inputs/input4.txt") as ifile:
    inp = ifile.read().splitlines()

PAIRS = [line.split(",") for line in inp]

def is_contained(range1: str, range2: str) -> bool:
    return int(range1.split("-")[0]) <= int(range2.split("-")[0]) and int(
        range1.split("-")[1]
    ) >= int(range2.split("-")[1])

def do_overlap(range1: str, range2: str) -> bool:
    if int(range1.split("-")[0]) > int(range2.split("-")[1]) or int(
        range2.split("-")[0]
    ) > int(range1.split("-")[1]):
        return False
    return True

def compute_solution(func, pairs):
    count = 0
    for pair in pairs:
        if func(pair[0], pair[1]):
            count += 1
        elif func(pair[1], pair[0]):
            count += 1
    return count

def part_1(pairs):
    return compute_solution(is_contained, pairs)

def part_2(pairs):
    return compute_solution(do_overlap, pairs)

print(part_1(PAIRS))
print(part_2(PAIRS))
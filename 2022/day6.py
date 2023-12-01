with open("inputs/input6.txt") as ifile:
    INPUT = ifile.read()

example6="mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def is_marker(characters:str)-> bool:
    return  len(characters) == len(set(characters))

def get_position_after_marker(datastream: str, marker_size: int)-> int:
    for i in range(len(datastream)-marker_size):
        if is_marker(datastream[i:i+marker_size]):
            return i+marker_size

def part_1(datastream: str):
    return get_position_after_marker(datastream, 4)

def part_2(datastream: str):
    return get_position_after_marker(datastream, 14)

print("Solution to p1: ", part_1(INPUT))
print("Solution to p2: ", part_2(INPUT))

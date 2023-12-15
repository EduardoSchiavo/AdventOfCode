

EXAMPLE = "examples/example15.txt"
INPUT = "inputs/input15.txt"

with open(INPUT) as ifile:
    INP = ifile.read().split(',')


def score_string(chars: str):
    value = 0
    for char in chars:
        value += ord(char)
        value = value*17
        value = value % 256
    return value


def get_boxes_map(instructions: list[str]) -> dict:
    boxes = {}
    for entry in instructions:
        if '=' in entry:
            label, focal_length = entry.split('=')
            box_number = score_string(label)
            if not boxes.get(box_number):
                boxes[box_number] = {label: focal_length}
            else:
                boxes[box_number][label] = focal_length
        if '-' in entry:
            label = entry[:-1]
            box_number = score_string(label)
            if boxes.get(box_number):
                if label in boxes[box_number]:
                    boxes[box_number].pop(label)
    return boxes


def score(boxes: dict) -> int:
    tot = 0
    for key, box in boxes.items():
        for lab, lens in box.items():
            tot += int(lens)*(list(box).index(lab)+1)*(int(key)+1)
    return tot


def p1():
    return sum([score_string(i) for i in INP])


def p2():
    return score(get_boxes_map(INP))


# print(p1())

print(p2())  # 279116

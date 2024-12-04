with open("inputs/input4.txt") as ifile:
    inp = [list(line) for line in ifile.read().splitlines()]

print(inp)

# TODO: turn into comprehension
character_map = {}
for i in range(len(inp)):
    for j in range(len(inp[i])):
        character_map[(i, j)] = inp[i][j]

directions = [(1, 0), (1, 1), (0, 1), (-1, -1),
              (-1, 0), (0, -1), (-1, 1), (1, -1)]


# def find_xmas(pos: tuple):
#     xmases = []


def find_xmas(pos: tuple, target: str, selected_dir: tuple = None):
    target_order = "XMAS"
    total_xmases = 0
    try:
        if character_map[pos] != target:
            return 0
        if target == "S":
            # print(f"t: {target}, p: {pos}, selected: {selected_dir}")
            if character_map[pos] != target:
                return 0
            print("got it!")
            return 1
    except KeyError:
        return 0
    # print(f"t: {target}, p: {pos}, selected: {selected_dir}")
    next_target = target_order[target_order.index(target)+1]
    if selected_dir is not None:
        next_pos = tuple(map(sum, zip(pos, selected_dir)))
        total_xmases += find_xmas(next_pos, next_target, selected_dir)
    else:
        for dir in directions:
            next_pos = tuple(map(sum, zip(pos, dir)))
            total_xmases += find_xmas(next_pos, next_target, selected_dir=dir)

    return total_xmases


def p1():
    total = 0
    for key in character_map.keys():
        if character_map[key] == "X":
            total += find_xmas(key, "X")

    return total


print(p1())

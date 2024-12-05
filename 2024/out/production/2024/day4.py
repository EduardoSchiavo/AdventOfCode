with open("inputs/input4.txt") as ifile:
    inp = [list(line) for line in ifile.read().splitlines()]


character_map = {(i, j): inp[i][j] for i in range(len(inp)) for j in range(len(inp[i]))}


def is_cross(pos: tuple, word_search: dict):
    tl = tuple(map(sum, zip(pos, (-1, -1))))
    br = tuple(map(sum, zip(pos, (1, 1))))
    tr = tuple(map(sum, zip(pos, (-1, 1))))
    bl = tuple(map(sum, zip(pos, (1, -1))))
    valid_chars = ("M", "S")
    try:
        if (word_search[tl] == word_search[br] or word_search[tr] == word_search[bl]):
            return False
    except KeyError:
        return False
    return all(char in valid_chars for i in (tl, br, tr, bl) for char in word_search[i]) 
    


def find_xmas(pos: tuple, target: str, wordsearch, selected_dir: tuple=None):
    target_order="XMAS"
    total_xmases=0
    directions=[(1, 0), (1, 1), (0, 1), (-1, -1),
                  (-1, 0), (0, -1), (-1, 1), (1, -1)]

    try:
        if wordsearch[pos] != target:
            return 0
        if target == "S":
            if wordsearch[pos] != target:
                return 0
            return 1
    except KeyError:
        return 0
    next_target=target_order[target_order.index(target)+1]
    if selected_dir is not None:
        next_pos=tuple(map(sum, zip(pos, selected_dir)))
        total_xmases += find_xmas(next_pos, next_target, wordsearch, selected_dir)
    else:
        for dir in directions:
            next_pos=tuple(map(sum, zip(pos, dir)))
            total_xmases += find_xmas(next_pos, next_target, wordsearch, selected_dir=dir)

    return total_xmases


def p1():
    return sum([find_xmas(key, "X", character_map) for key in character_map.keys() if character_map[key] == "X"])

def p2():
    return sum([1 for key in character_map.keys() if character_map[key] =="A" and is_cross(key, character_map)])


print(p1())  #2603
print(p2())  #1965

EXAMPLE = "examples/example13.txt"
INPUT = "inputs/input13.txt"


with open(INPUT) as ifile:
    # INP = [ list(line) for line in ifile.read().splitlines()]
    INP_ROWWISE =  [pattern.split('\n') for pattern in ifile.read().split('\n\n')]

def get_columns(input_as_rows):
    rotated_patterns = []
    for pattern in input_as_rows:
        pattern_by_col = []
        for col in range(len(pattern[0])):
            pattern_by_col.append("".join(pattern[row][col] for row in range(len(pattern))))
        rotated_patterns.append(pattern_by_col)
    return rotated_patterns

INP_COLUMNWISE = get_columns(INP_ROWWISE)

# print(INP_ROWWISE)
# print(INP_COLUMNWISE)


def get_reflections(input_strings: list[str]):
    span = len(input_strings[0])+1
    # reflections = []
    for i in range(1, len(input_strings)):
        if input_strings[i]==input_strings[i-1]:
            # print(i, i-1)
            # print(input_strings[i], input_strings[i-1])

            for j in range(1, span+1):
                try:
                    # print(j, span+1)
                    # print(input_strings[i+j],input_strings[i-1-j])
                    if j==i:
                        return i
                    if not input_strings[i+j]==input_strings[i-1-j]:
                        break
                except IndexError:
                    return i 
    return 0



print(INP_COLUMNWISE[0])
print(get_reflections(INP_COLUMNWISE[0]))
# assert get_reflections(INP_COLUMNWISE[0]), 5

# print(INP_ROWWISE[0])
# print(get_reflections(INP_ROWWISE[0]))
# # assert get_reflections(INP_ROWWISE[0]), 0

# print(INP_ROWWISE[1])
# print(get_reflections(INP_ROWWISE[1]))

# print(fold_horizontally(sample_map, 6))

def p1():
    total = 0
    for pattern in range(len(INP_ROWWISE)):
        v = get_reflections(INP_COLUMNWISE[pattern])
        h = get_reflections(INP_ROWWISE[pattern])*100
        print(v, h)
        total += v + h
    return total

print(p1())

EXAMPLE = "examples/example15.txt"
INPUT = "inputs/input15.txt"

with open(INPUT) as ifile:
    INP = ifile.read().split(',')

print(INP)

def score_string(chars: str):
    value =0
    for char in chars:
        value += ord(char)
        value = value*17
        value = value % 256
    return value

def p1():
    return sum([score_string(i) for i in INP ])

print(p1())

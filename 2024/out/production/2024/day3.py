import re

with open("inputs/input3.txt") as ifile:
    inp = ifile.read()



def p1(instructions: str) -> int:
    matches = re.findall("mul\((\d{1,3},\d{1,3})\)", instructions)
    matches = [tuple(m.split(",")) for m in matches]
    return sum(int(m[0])*int(m[1]) for m in matches)


def p2(instructions: str) -> int:
    instructions = re.sub("(?s)don't\(\).*?do\(\)", "", instructions)
    instructions = re.sub("(?s)don't\(\).*", "", instructions)
    return p1(instructions)


print(p1(inp)) #160672468
print(p2(inp)) #84893551

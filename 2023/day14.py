EXAMPLE = "examples/example14.txt"
INPUT = "inputs/input14.txt"

with open(INPUT) as ifile:
    INP_BY_LINE = ifile.read().split('\n')
    INP=[ "".join([INP_BY_LINE[row][col] for row in range(len(INP_BY_LINE))])   for col in range(len(INP_BY_LINE[0]))]

print(INP)


def score_line(line: str)-> int:
    score=0
    max_weight=len(line)
    for block in line.split('#'):
        max_weight -= block.count('#')
        score += sum(range(max_weight-block.count('O')+1, max_weight+1))
        max_weight = max_weight - (len(block)+1)
    return score


def p1():
    return sum([score_line(line) for line in INP])

print(p1()) #106186

import plotly.express as px
from itertools import pairwise
from functools import reduce


EXAMPLE = "examples/example9.txt"
INPUT = "inputs/input9.txt"

with open(INPUT) as ifile:
    INP = [[int(n) for n in line.split()]
           for line in ifile.read().splitlines()]


def extrapolate(series, direction=-1):
    completed = False
    steps = [series[direction]]
    step = series
    while not completed:
        step = [y - x for x, y in pairwise(step)]
        if all(n == step[0] for n in step):
            completed = True
            steps.append(step[direction])
        else:
            steps.append(step[direction])
    if direction == 0:
        return reduce(lambda a, b: b-a, steps[::-1])
    return sum(steps)


def compute_result(direction: int):
    return sum(extrapolate(line, direction) for line in INP)


def p1():
    return compute_result(-1)


def p2():
    return compute_result(0)


print(p1())  # 2075724761
print(p2())  # 1072

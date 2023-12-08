
from enum import Enum
from math import lcm

EXAMPLE = "examples/example8p3.txt"
INPUT = "inputs/input8.txt"

with open(INPUT) as ifile:
    INP = ifile.read().splitlines()


class Instruction(Enum):
    L = 0
    R = 1


def parse_instructions_and_tree(input: list):
    instructions = [Instruction[inst] for inst in input[0]]
    nodes = {k: tuple(v.strip('()').split(', '))
             for (k, v) in [entry.split(' = ') for entry in input[2::]]}
    return instructions, nodes


INSTRUCTIONS, NODES = parse_instructions_and_tree(INP)


def execute_instructions(current, count: int):
    for inst in INSTRUCTIONS:
        count += 1
        current = NODES[current][inst.value]
        if current[-1] == 'Z':
            return count
    return execute_instructions(current, count)


def p1():
    print(execute_instructions('AAA', 0))


def p2():
    print(lcm(*[execute_instructions(starter, 0)
          for starter in [key for key in NODES.keys() if key[-1] == 'A']]))


p1()  # 20093
p2()  # 22103062509257

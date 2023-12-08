
from enum import Enum


EXAMPLE = "examples/example8p2.txt"
INPUT = "inputs/input8.txt"

with open(INPUT) as ifile:
    INP = ifile.read().splitlines()

# print(INP)

class Instruction(Enum):
    L = 0
    R = 1

def parse_instructions_and_tree(input:list):
    instructions = [Instruction[inst] for inst in input[0]]
    nodes = {k: tuple(v.strip('()').split(', ')) for (k, v) in [entry.split(' = ') for entry in input[2::]]}
    return instructions, nodes


def execute_instructions(current, nodes, instructions, count: int):
    for inst in instructions:
        count +=1
        current = nodes[current][inst.value]
        if current == 'ZZZ': 
            return count
    return execute_instructions(current, nodes, instructions, count)

def transverse(start_from, nodes, instructions):
    current = start_from
    count = 0 
    return execute_instructions(current, nodes, instructions, count)

def p1():
    instr, nodes = parse_instructions_and_tree(INP)
    print(transverse('AAA', nodes, instr))

p1() #20093


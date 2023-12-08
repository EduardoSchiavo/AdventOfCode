
from enum import Enum
from math import lcm

EXAMPLE = "examples/example8p3.txt"
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
        if current[-1]=='Z': 
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

def get_starting_nodes(nodes):
    return [key for key in nodes.keys() if key[-1]=='A']

def p2():
    instr, nodes = parse_instructions_and_tree(INP)
    starting = get_starting_nodes(nodes)
    print(lcm(*[transverse(starter, nodes, instr) for starter in starting ]))

p2() #22103062509257


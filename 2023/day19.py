from dataclasses import dataclass
import json
import re

EXAMPLE = "examples/example19.txt"
INPUT = "inputs/input19.txt"

with open(INPUT) as ifile:
    W, PARTS = [block.split('\n') for block in ifile.read().split("\n\n")]
    WORKFLOWS = {k: v[:-1] for (k, v) in [w.split('{') for w in  W]}




@dataclass
class MetalPart():
    x: int
    m: int
    a: int
    s: int

    def evaluate_workflow(self, wf_key: str= 'in'):
        if wf_key in ['R', 'A']:
            return wf_key
        workflow =  WORKFLOWS.get(wf_key).split(',')

        temp_map ={'x': self.x, 'm': self.m , 'a': self.a, 's': self.s}

        for instruction in workflow[:-1]:
            operation, destination = instruction.split(':')
            if eval(temp_map[operation[0]] + operation[1:]) == True:
                return self.evaluate_workflow(destination)
        return self.evaluate_workflow(workflow[-1])

    def get_value(self):
        return int(self.a) + int(self.m) + int(self.s) + int(self.x)
    



digits = re.compile(r"\d+")
PARTS = [MetalPart(*re.findall(digits, part)) for part in PARTS]



def p1():
    return sum([part.get_value() for part in PARTS if part.evaluate_workflow()=='A'])

print(p1()) #509597

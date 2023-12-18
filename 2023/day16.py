
from dataclasses import dataclass


EXAMPLE = "examples/example16.txt"
INPUT = "inputs/input16.txt"

with open(EXAMPLE) as ifile:
    ROWS =  [line for line in ifile.read().splitlines()]
    INP = {}
    for r_idx, row in enumerate(ROWS):
        for c_idx, elem in enumerate(row):
            INP[(r_idx, c_idx)]=elem

print(INP)

@dataclass
class Beam:
    pos: tuple #current position
    direction: tuple 
    moving: bool

    def step(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
        

def propagate_beam(layout: dict):
    beams = [Beam(pos=(0,0), direction=(0,1), moving=True)]
    energized = []
    for beam in beams:
        energized.append(beam.pos)
        if layout[beam.pos] == '.':
            beam.step()
        elif layout[beam.pos] == '\\' :
            beam.direction = beam.direction[::-1]
            beam.step()
        elif layout[beam.pos] == '/' :
            beam.direction = tuple(-i for i in beam.direction[::-1])
            beam.step()
        elif layout[beam.pos] == '|':
            if beam.direction[1]==0:
                beam.step()
            else:
                #send beam upward  01   10       0-1   10
                beam.direction = (1, 0)
                #create new downward beam
                beams.append(Beam(pos=beam.pos, direction=(-1, 0), moving=True))
                

        

        





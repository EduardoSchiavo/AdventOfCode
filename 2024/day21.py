import itertools
from functools import cache
import math
with open("inputs/input21.txt") as ifile:
    CODES = ifile.read().splitlines()

NUMPAD = {'7': (0, 0), '8': (0, 1), '9': (0, 2),
          '4': (1, 0), '5': (1, 1), '6': (1, 2),
          '1': (2, 0), '2': (2, 1), '3': (2, 2),
          '0': (3, 1), 'A': (3, 2)}

# move: pos on keypad
KEYPAD = {'^': (0, 1),  # ^
          'A': (0, 2),
          '<': (1, 0),  # <
          'v': (1, 1),  # v
          '>': (1, 2)}  # >

ARROWS = {(-1, 0): '^',
          (0, -1): '<',
          (1, 0):  'v',
          (0, 1):  '>'}


def precompute_best_sequences(keypad: dict, exclude: dict)-> dict:
    bs = {}
    moves = tuple(m for m in itertools.product(
        keypad.keys(), repeat=2) if m[0] != m[1])

    for m in moves:
        delta = (keypad[m[1]][0] - keypad[m[0]][0],
                 keypad[m[1]][1] - keypad[m[0]][1])
        arr = ""
        for x in range(abs(delta[0])):
            arr += ARROWS[(delta[0]/abs(delta[0]), 0)]
        for y in range(abs(delta[1])):
            arr += ARROWS[0, (delta[1]/abs(delta[1]))]
        bs["".join(m)] = {"".join(s) + 'A' for s in itertools.permutations(arr)
                          if not "".join(s).startswith(exclude.get(m[0], "@"))}
    for a in "<>^vA":
        bs[a*2] = 'A'
    return bs


BS_KEY = precompute_best_sequences(KEYPAD,{'A': "<<", '^': "<", '<': "^"} )
BS_NUM = precompute_best_sequences(NUMPAD,{'A': "<<", '0': "<", '7': "vvv", '4': "vv", '1': "v"} )

@cache
def get_len(code: str, depth: int)-> int:
    if depth == 0:
        return len(code)
    length = 0
    code = 'A' + code
    for i in range(len(code)-1):
        length += min(get_len(seq, depth-1) for seq in BS_KEY[code[i:i+2]])
    return length

def nums_to_keys(code: str)-> list[str]:
    ways = {''}
    code = 'A' + code
    for i in range(len(code)-1):
        new = set()
        for w in ways:
            new.update([w + comb for comb in  BS_NUM[code[i] + code[i+1]]])
        ways = new
    return ways

def score(depth: int):
    tot = 0
    for code in CODES:
        opts = nums_to_keys(code)
        best_len = math.inf
        for op in opts:
            op_len = 0
            op_len = get_len(op, depth)
            if op_len < best_len:
                best_len = op_len
        tot += best_len*int(code.rstrip('A'))
    return tot

def p1():
    return score(2)

def p2():
    return score(25)


print(p1())
print(p2())


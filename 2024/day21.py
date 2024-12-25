import itertools
from functools import cache
with open("examples/example21.txt") as ifile:
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

SUBPATHS = {}
PERMS = {}


def get_sequence(code: str):
    pos = NUMPAD['A']
    keys = []
    for d in code:
        delta = (NUMPAD[d][0] - pos[0], NUMPAD[d][1] - pos[1])
        keys.append(delta)
        pos = NUMPAD[d]
    return keys


def precompute_best_arrow_sequences():
    # moves = itertools.product(KEYPAD.keys(), repeat=2)
    bs = {}
    moves = tuple(m for m in itertools.product(KEYPAD.keys(), repeat=2) if m[0] != m[1])
    print(f"moves = {moves}")
    # for k in KEYPAD:
    #     delta = (KEYPAD[k][0] - pos[0], KEYPAD[k][1] - pos[1])
    #     print(f"key: {KEYPAD[k]}

print(get_sequence('379A'))
print(precompute_best_arrow_sequences())

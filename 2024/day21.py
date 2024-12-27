import itertools
import math
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
    # print(keys)
    return keys


def precompute_best_arrow_sequences():
    bs = {}
    moves = tuple(m for m in itertools.product(
        KEYPAD.keys(), repeat=2) if m[0] != m[1])
    for m in moves:
        delta = (KEYPAD[m[1]][0] - KEYPAD[m[0]][0],
                 KEYPAD[m[1]][1] - KEYPAD[m[0]][1])
        arr = ""
        for x in range(abs(delta[0])):
            arr += ARROWS[(delta[0]/abs(delta[0]), 0)]
        for y in range(abs(delta[1])):
            arr += ARROWS[0, (delta[1]/abs(delta[1]))]
        # avoid gap
        if delta[0] < 0:
            arr = arr[::-1]
        bs["".join(m)] = arr + 'A'
    for a in "<>^vA":
        bs[a*2] = 'AA'
    return bs


# try computing all possiblities just for this first step
def get_arr_seq(seq: list[tuple]) -> set:
    pos = NUMPAD['A']
    arr_seq = {""}
    for delta in seq:
        arr = ""
        for x in range(abs(delta[0])):
            arr += ARROWS[(delta[0]/abs(delta[0]), 0)]
        for y in range(abs(delta[1])):
            arr += ARROWS[0, (delta[1]/abs(delta[1]))]

        to_add = set()
        if (pos[0] == 3 and tuple([sum(x) for x in zip(pos, delta)])[1] == 0) or (pos[1] == 0 and tuple([sum(x) for x in zip(pos, delta)])[0] == 3):
            for a in arr_seq:
                if delta[0] < 0 ^ delta[1] > 0:
                    to_add.add(a + arr[::-1] + 'A')
                else:
                    to_add.add(a + arr + 'A')
        else:
            for a in arr_seq:
                to_add.add(a + arr + 'A')
                to_add.add(a + arr[::-1] + 'A')
        arr_seq = to_add
        pos = tuple([sum(x) for x in zip(pos, delta)])
    return arr_seq


# def propagate(arr_seq: str, bs: dict):
#     arr = ""
#     arr_seq = 'A' + arr_seq
#     for i in range(len(arr_seq)-1):
#         if arr_seq[i] != arr_seq[i+1]:
#             arr += bs[arr_seq[i] + arr_seq[i+1]]
#         arr += 'A'
#     return arr

def init_state(arr_seq: str, bs: dict):
    state = {}
    for i in arr_seq.rstrip('A').split('A'):
        if i == '':
            continue
        if i not in state:
            state[i] = 0
        state[i] += 1
    return state


def propagate(state: dict, bs: dict):
    new_state = {}
    for move in state:
        p_move = 'A' + move + 'A'
        for i in range(len(p_move)-1):
            pair = p_move[i] +p_move[i+1]
            # print(f"p: {pair}")
            if bs[pair].rstrip('A') not in new_state:
                new_state[bs[pair].rstrip('A')] = 0
            new_state[bs[pair].rstrip('A')] += state[move]
    return new_state

def get_len(state:dict):
    tot = 0
    for k, v in state.items():
        tot += (len(k)+1)*v
    return tot

def p1():
    bs = precompute_best_arrow_sequences()
    print(bs)
    tot = 0
    for code in CODES:
        print(f"code: {code}")
        s1 = get_arr_seq(get_sequence(code))
        min_len = min(len(s) for s in s1)
        opts = [s for s in s1 if len(s) == min_len]
        final = set()
        for op in opts:
            s = op
            state = init_state(s, bs)
            for i in range(2):
                state = propagate(state, bs)
                print(f"state: {state}, len: {get_len(state)}")
            final.add(get_len(state))
        # print(f" final: {final} len {min(len(s) for s in final) }")
        tot += min(s for s in final) * int(code.strip('A'))
    return tot


print(p1())

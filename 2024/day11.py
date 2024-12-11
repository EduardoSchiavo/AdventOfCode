with open("inputs/input11.txt") as ifile:
    STONES = [int(s) for s in ifile.read().split()]


def get_initial_state(stones: list) -> dict:
    return {s: 1 for s in stones}


def step(state: dict) -> dict:
    new_state = {}
    for s in state.keys():
        if s == 0:
            if 1 not in new_state:
                new_state[1] = 0
            new_state[1] += state[s]
        elif len(str(s)) % 2 == 0:
            ss = str(s)
            for a in [int(ss[:len(ss)//2]), int(ss[len(ss)//2:])]:
                if a not in new_state:
                    new_state[a] = 0
                new_state[a] += state[s]
        else:
            if s*2024 not in new_state:
                new_state[s*2024] = 0
            new_state[s*2024] += state[s]
    return new_state


def score(n_steps: int) -> int:
    curr = get_initial_state(STONES)
    for i in range(n_steps):
        new = step(curr)
        curr = new
    return sum(curr.values())


def p1():
    return score(25)


def p2():
    return score(75)


print(p1())
print(p2())

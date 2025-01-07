import operator

with open("inputs/input24.txt") as ifile:
    W, G = ifile.read().split("\n\n")
    W = {w.split(":")[0]: int(w.split(":")[1]) for w in W.splitlines()}
    G = [tuple(g.split()) for g in G.splitlines()]


OPS = {'AND': operator.and_, 'OR': operator.or_, 'XOR': operator.xor}


def propagate(wires: dict, gates: list):
    for gate in gates:
        if gate[0] in wires and gate[2] in wires:
            result = OPS[gate[1]](wires[gate[0]], wires[gate[2]])
            wires[gate[4]] = result


def p1(wires: dict):
    zeds = [g[4] for g in G if g[4].startswith('z')]
    while not all(z in W for z in zeds):
        propagate(wires, G)
    return int("".join([str(p[1]) for p in sorted({z: wires[z] for z in wires.keys() if z in zeds}.items())])[::-1], base=2)

# solved by manually checking the circuit :D
def p2():
    res = ['z09', 'nnf', 'z20', 'nhs', 'z34', 'wrc', 'ddn', 'kqh']
    res.sort()
    return ",".join(res)


print(p1(W))
print(p2())

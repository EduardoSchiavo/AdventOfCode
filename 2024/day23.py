with open("inputs/input23.txt") as ifile:
    NETMAP = ifile.read().splitlines()


def get_connections(netmap: list[str]) -> dict:
    conn = {}
    for link in netmap:
        c1, c2 = link.split('-')
        if c1 not in conn:
            conn[c1] = list()
        conn[c1].append(c2)
        if c2 not in conn:
            conn[c2] = list()
        conn[c2].append(c1)
    return conn


def get_groups(conn: dict)-> set:
    groups = list()
    for comp in conn.keys():
        for i in range(len(conn[comp])-1):
            for j in range(i, len(conn[comp])):
                if conn[comp][i] in conn[conn[comp][j]] or conn[comp][j] in conn[conn[comp][i]]:            
                    g = {comp, conn[comp][i], conn[comp][j]}
                    if g not in groups:
                        groups.append(g)
                    continue
    return groups
    # return [",".join(g) for g in groups]


def p1():
    comps = get_connections(NETMAP)
    groups = get_groups(comps)
    print(groups)
    return sum(1 for g in groups if any(c.startswith('t') for c in g))

print(p1())


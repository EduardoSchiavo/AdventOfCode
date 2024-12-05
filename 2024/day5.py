with open("inputs/input5.txt") as ifile:
    blocks = ifile.read().split("\n\n")
    RULES = blocks[0].splitlines()
    UPDATES = [u.split(",") for u in blocks[1].splitlines()]


def get_children_map(rules: list):
    map = {p: [] for p in [r.split("|")[0] for r in rules]}
    for rule in rules:
        p, c = rule.split("|")
        map[p].append(c)
    return map



def is_sorted(update: list, index_map: dict) -> bool:
    for idx, num in enumerate(update[1:]):
        for prev in update[:idx+1]:
            try:
                if num not in index_map[prev]:
                    return False
            except KeyError:
                return False
    return True


def fix(update: list, index_map: dict) -> list:
    for idx, num in enumerate(update[1:]):
        for pidx, prev in enumerate(update[:idx+1]):
            try:
                if num not in index_map[prev]:
                    update[idx+1] = prev
                    update[pidx] = num
                    break
            except KeyError:
                update[idx+1] = prev
                update[pidx] = num
    if not is_sorted(update, index_map):
        return fix(update, index_map)
    return update

def get_value(updates: list, rules: list )-> int:
    tot = 0
    for update in updates:
        if (is_sorted(update, get_children_map(rules))):
            tot += int(update[len(update)//2])
    return tot



def p1():
    return get_value(UPDATES, RULES)

def p2():
    children_map = get_children_map(RULES)
    fixed_updates= [fix(update,children_map) for update in UPDATES if not is_sorted(update, children_map)]
    return get_value(fixed_updates, RULES)


print(p1())
print(p2())

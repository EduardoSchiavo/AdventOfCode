with open('inputs/input6.txt') as ifile:
    inp = ifile.read().splitlines()

print(inp)
# ROWS = [c.split(" ") for c in inp]


def p1():

    rows = [[n for n in c.strip().split(" ") if n != ''] for c in inp]
    tot = 0
    for c in range(len(rows[0])):
        op = rows[-1][c]
        if op == '+':
            sm = sum(int(rows[r][c]) for r in range(len(rows)-1))
            tot += sm
        else:
            prd = 1
            for r in range(len(rows)-1):
                prd *= int(rows[r][c])
            tot += prd
    return tot




print(p1())


def parse_worksheet():
    for line in inp:
        print(line)

    problems = []
    curr_prob = []

    for i in reversed(range(len(inp[0]))):
        curr_num = ''
        for j in range(len(inp)-1):
            # print(f"idxs: {i} {j} -- {inp[j][i]}")
            curr_num += inp[j][i]
        if not curr_num.isspace():
            curr_prob.append(curr_num)
        if inp[-1][i] in ('+', '*'):
            # print(f" op: {inp[-1][i]})")
            curr_prob.append(inp[-1][i])
            # reset
            problems.append(curr_prob)
            curr_prob = []
    return problems


def compute_problem(problem: list[str]) -> int:

    if problem[-1] == "+":
        return sum(int(n) for n in problem[:-1] if n != '')
    prd = 1
    for n in problem[:-1]:
        if n == '':
            continue
        prd *= int(n)
    return prd

def p2():
    problems = parse_worksheet()
    tot = 0 
    for prob in problems:
        tot += compute_problem(prob)
    return tot



print(parse_worksheet())
print(p2())

from functools import reduce
import operator

with open('inputs/input6.txt') as ifile:
    inp = ifile.read().splitlines()



def p1():
    return sum(compute_problem(p) for p in parse_worksheet_h())

def parse_worksheet_h():
    rows = [[n for n in c.strip().split(" ") if n != ''] for c in inp]
    problems = []
    curr_prob = []
    for c in range(len(rows[0])):
        op = rows[-1][c]
        curr_prob = [int(rows[r][c]) for r in range(len(rows)-1)]
        curr_prob.append(op)
        problems.append(curr_prob)
        curr_prob= []
    return problems

def parse_worksheet():
    problems= []
    curr_prob= []
    for i in reversed(range(len(inp[0]))):
        curr_num= ''
        for j in range(len(inp)-1):
            curr_num += inp[j][i]
        if not curr_num.isspace():
            curr_prob.append(int(curr_num))
        if inp[-1][i] in ('+', '*'):
            curr_prob.append(inp[-1][i])
            problems.append(curr_prob)
            curr_prob= []
    return problems


def compute_problem(problem: list[str]) -> int:
    if problem[-1] == "+":
        return sum(problem[:-1])
    return reduce(operator.mul, problem[:-1], 1)

def p2():
    return sum(compute_problem(p) for p in parse_worksheet())




assert p1() == 4719804927602
assert p2() == 9608327000261

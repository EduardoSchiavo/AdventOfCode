from logging import exception
with open("inputs/input2.txt") as ifile:
    inp = [[int(i) for i in l.split()] for l in ifile.read().splitlines()]


def is_safe(report: list) -> bool:
    try:
        sign = (report[1]-report[0])/abs(report[1] -
                                         report[0]) 
    except (ZeroDivisionError):
        return False
    for i in range(1, len(report)):
        if not (1 <= abs(report[i]-report[i-1]) <= 3) or (report[i]-report[i-1])/abs(report[i]-report[i-1]) != sign:
            return False
    return True

def is_safe_w_dampener(report: list) -> bool:
    if is_safe(report):
        return True
    for i in range(len(report)):
        copy = report.copy()
        copy.pop(i)
        if is_safe(copy):
            return True
    return False



def p1():
    return sum(1 for report in inp if is_safe(report))


def p2():
    return sum(1 for report in inp if is_safe_w_dampener(report))

print(p1())
print(p2())


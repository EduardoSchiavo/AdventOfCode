with open("examples/example10.txt") as ifile:
    INSTRUCTIONS = [ tuple(line.split(' ')) for line in ifile.read().splitlines()]


def p1(input):
    cycle = 0
    for idx, command in enumerate(input):
        adjust = 0
        if command[0] == 'noop':
            adjust = 1
            cycle +=1
        else:
            cycle +=2
        if cycle == 21:
            ret = (1 + sum([int(command[1]) for command in input[:idx-adjust] if command[0] == 'addx']))*20
        if cycle == 61:
            ret += (1 + sum([int(command[1]) for command in input[:idx-adjust] if command[0] == 'addx']))*60
        if cycle == 101:
            ret += (1 + sum([int(command[1]) for command in input[:idx-adjust] if command[0] == 'addx']))*100
        if cycle == 141:
            ret += (1 + sum([int(command[1]) for command in input[:idx-adjust] if command[0] == 'addx']))*140
        if cycle == 181:
            ret += (1 + sum([int(command[1]) for command in input[:idx-adjust] if command[0] == 'addx']))*180
        if cycle == 221:
            ret += (1 + sum([int(command[1]) for command in input[:idx-adjust] if command[0] == 'addx']))*220
            return ret


def evaluate_x(commands: list):
    cycles_dict = {0: 1}
    for command in commands:
        if command[0] == 'noop':
            cycles_dict[list(cycles_dict)[-1]+1]=cycles_dict[list(cycles_dict)[-1]]
        else:
            cycles_dict[list(cycles_dict)[-1]+1]=cycles_dict[list(cycles_dict)[-1]]
            cycles_dict[list(cycles_dict)[-1]+1]=int(command[1])+cycles_dict[list(cycles_dict)[-1]]
    return cycles_dict


def draw_lines(cycle_dict: dict):
    lines=[]
    for row in range(6):
        line = ""
        for i in range(40):
            if i in [cycle_dict[i+row*40]-1, cycle_dict[i+row*40], cycle_dict[i+row*40]+1]:
                line += "#"
            else:
                line += "."
        lines.append(line)
    return lines

def render(strings: list) -> None:
    for string in strings:
        print(string)


def p2(input):
    render(draw_lines(evaluate_x(input)))

print(p1(INSTRUCTIONS))
p2(INSTRUCTIONS)

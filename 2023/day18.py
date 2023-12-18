EXAMPLE = "examples/example18.txt"
INPUT = "inputs/input18.txt"


with open(INPUT) as ifile:
    INP = [tuple(instr.split(' ')) for instr in ifile.read().splitlines()]

# print(INP)

def create_path(instructions: list[tuple]):
    direction_map = { 
        'R' : (0, 1),
        'L' : (0, -1),
        'U' : (1, 0),
        'D' : (-1, 0)
    }
    path = [(0,0)]
    length = 1
    for instr in instructions:
        step = tuple([i*int(instr[1]) for i in  direction_map.get(instr[0])])
        path.append((path[-1][0]+step[0], path[-1][1]+step[1]))
        length += int(instr[1])

    return path, length

def polygon_area(vertices: list[tuple], perimeter):
    n=len(vertices)

    area = 0

    for i in range(1, n):
        x1, y1 = vertices[i-1]
        x2, y2 = vertices[(i)]  
        area += (x1 * y2 - x2 * y1)

    # Take the absolute value and divide by 2
    area = abs(area) // 2.0 + abs(perimeter) // 2.0 +1

    print(area)
    return int(area)

def parse_instructions_for_p2(instructions: list[tuple]):
    directions=['R', 'D', 'L', 'U']
    return [(directions[int(inst[-1][-2])], int(inst[-1][2:7], 16) )  for inst in instructions]
    

parse_instructions_for_p2(INP)

def p1(instructions):
    path, length = create_path(instructions)
    polygon_area(path, length)

# p1(INP)

def p2():
    new_instructions = parse_instructions_for_p2(INP)
    print(new_instructions)
    p1(new_instructions)
p2()
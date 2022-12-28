with open("inputs/input9.txt") as ifile:
    MOVES = [(move.split()[0], int(move.split()[1])) for move in ifile.read().splitlines()]

def move_head(move: tuple, pos=[0,0]):
    match move[0]:
        case 'R':
            pos[0]+=1
        case 'L':
            pos[0]-=1
        case 'U':
            pos[1]+=1
        case 'D':
            pos[1]-=1
    return pos

def sign(n: int):
    return n/abs(n)

def move_tail(tail, head):
    if tail[0] == head[0]:
        tail[1]+=sign(head[1]-tail[1])
    elif tail[1] == head[1]:
        tail[0]+=sign(head[0]-tail[0])
    else:
        tail[0]+=sign(head[0]-tail[0])
        tail[1]+=sign(head[1]-tail[1])
    return tail

def is_distant(t, h)-> bool:
    return not (abs(t[0]-h[0]) + abs(t[1]-h[1]) <= 1 or abs(t[0]-h[0])<= 1 and abs(t[1]-h[1]) <= 1)

def head_path(moves: list):
    step = [0,0]
    steps = []
    for move in moves:
        for i in range(move[1]):
            step = move_head(move, step)
            steps.append(step.copy())
    return steps

def tail_path(head_path: list):
    step =[0,0]
    steps=[step.copy()]
    for hs in head_path:
        if is_distant(step, hs):
            step = move_tail(step, hs)
            steps.append(step.copy())
    return steps


def filter_duplicates(path: list)-> list:
    filtered=[]
    [filtered.append(step) for step in path if step not in filtered]
    return filtered



def p1(head_path: list) -> int:
    return len(filter_duplicates(tail_path(head_path)))


def p2(head_path: list) -> int:
    leading=head_path
    for i in range(9):
        tp=tail_path(leading)
        leading=tp
    return len(filter_duplicates(tp))

H_PATH=head_path(MOVES)

print(p1(H_PATH))
print(p2(H_PATH))

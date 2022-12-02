import enum

with open('inputs/input2.txt') as ifile:
    inp=ifile.read().splitlines()

# print(inp)

# unify or convert to enum
def opponent(letter: str)-> str:
    match letter:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3

def me(letter: str)-> str:
    match letter:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3

def calculate_score(game: str)-> int:    

    opponents_hand=opponent(game[0])
    my_hand=me(game[2])

    result = (opponents_hand, my_hand)
    print(opponents_hand, my_hand)
    # restructure 
    if result[0]==result[1]:
            # print("DRAW")
            return result[1] + 3
    elif result[0]==1 and result[1]==3:
            # print("opponent wins")
            return result[1]
    elif result[0]==3 and result[1]==1:
            # print("I win")
            return result[1] + 6
    elif result[0] > result[1]:
            # print("opponent wins")
            return result[1]
    else:
        print("i win")
        return result[1] + 6

    

def compute_total_score(games: list)-> int:
    total=0
    for game in games:
        total+=calculate_score(game)

    return total


# print(inp[0])
# print(calculate_score(inp[2]))

print(compute_total_score(inp))



    
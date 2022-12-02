with open('inputs/input2.txt') as ifile:
    inp=ifile.read().splitlines()


def parse_hand(letter: str)-> str:
    match letter:
        case "A" | "X":
            return 1
        case "B" | "Y":
            return 2
        case "C" | "Z":
            return 3


def calculate_score(game: str)-> int:    
    result = (parse_hand(game[0]), parse_hand(game[2]))    
    # restructure 
    if result[0]==result[1]:     #DRAW
            return result[1] + 3
    elif result[0]==1 and result[1]==3:  #LOOSE
            return result[1]
    elif result[0]==3 and result[1]==1:  #WIN
            return result[1] + 6
    elif result[0] > result[1]:          #LOOSE
            return result[1]
    return result[1] + 6    # WIN
    

def calculate_score_p2(game: str)-> int:    
    result = (parse_hand(game[0]), parse_hand(game[2]))    
    match result[1]:
        case 1:
            if result[0] == 1:
                return 3
            elif result[0] == 2:
                return 1
            return 2
        case 2:
            return 3 + result[0]
        case 3:
            score = 6
            if result[0] == 1:
                return score + 2
            elif result[0] == 2:
                return score + 3
            return score +1

    

# P1
print("Part one: ", sum([calculate_score(game) for game in inp]))


# P2
print("Part one: ", sum([calculate_score_p2(game) for game in inp]))




    
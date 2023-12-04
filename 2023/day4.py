from ast import parse


with open('inputs/input4.txt') as ifile:
    INP= [line.split(':')[1] for line in ifile.read().splitlines()]


def parse_number_sequence(numbers: str):
    return [int(num) for num in numbers if num != '']

def compute_score(matched_numbers: list)-> int:
    return 2**(len(matched_numbers)-1) if len(matched_numbers) else 0


def evaluate_card(card: str)-> list:
    winning_numbers = parse_number_sequence(card.split('|')[0].split(' '))
    scratched_numbers = parse_number_sequence(card.split('|')[1].split(' '))
    return [num for num in scratched_numbers if num in winning_numbers]

def to_dict(cards: list)-> dict:
    return {idx+1: [card, 1] for (idx, card) in enumerate(cards)}


cards_dict = to_dict(INP)

for idx, value in cards_dict.items():
    index_span = len(evaluate_card(value[0]))
    quantity = value[1]
    for i in range(idx+1, idx+index_span+1):
        print(idx, i)
        try:
            cards_dict[i][1]+=quantity
        except KeyError:
            pass


tot = 0
for k, v in cards_dict.items():
    print(k, v)
    tot += v[1]
print(tot)






def p1():
    total =0
    for card in INP:
        total += compute_score(evaluate_card(card))
    return total



# print(p1())
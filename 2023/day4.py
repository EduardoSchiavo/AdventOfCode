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

def p1():
    total =0
    for card in INP:
        total += compute_score(evaluate_card(card))

    return total

print(p1())
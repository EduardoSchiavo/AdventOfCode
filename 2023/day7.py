import copy
from dataclasses import dataclass
from functools import cmp_to_key



with open('inputs/input7.txt') as ifile:
    INP = ifile.read().splitlines()

print(INP)

@dataclass
class Hand:
    cards: str
    bid: int
    # rank: int = None

SCORE_MAP = { '11111': [], '2111': [],  '221': [], '311': [],'32': [],'41': [], '5': []  }
CARD_VALUES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] #p1
# CARD_VALUES = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'] #p2

def parse_hands(hands: list):
    return [Hand(card, int(bid)) for card, bid in [hand.split() for hand in hands]]


def get_hand_type(hand: Hand, score_map: dict, include_jolly=False):
    counts={char: str(hand.cards.count(char)) for char in hand.cards}
    hand_type=''.join(sorted(counts.values(), reverse=True))
    # score_map[hand_type].append(hand)
    if include_jolly:
        match counts.get('J'):
            case '1':
                match hand_type:
                    case '41':
                        score_map['5'].append(hand)
                    case '311':
                        score_map['41'].append(hand)
                    case '221':
                        score_map['32'].append(hand)
                    case '2111':
                        score_map['311'].append(hand)
                    case '11111':
                        score_map['2111'].append(hand)    
            case '2':
                match hand_type:
                    case '32':
                        score_map['5'].append(hand)
                    case '221':
                        score_map['41'].append(hand)
                    case '2111':
                        score_map['311'].append(hand)
            case '3':
                match hand_type:
                    case '32':
                        score_map['5'].append(hand)
                    case '311':
                        score_map['41'].append(hand)
            case None :
                score_map[hand_type].append(hand)
            case _ :
                print(counts.get('J'))
                score_map['5'].append(hand)
    else:
        score_map[hand_type].append(hand)
    return score_map

def get_winning(hand1: str, hand2: str): #only for cards of same type
    # print(f'comparing {hand2.cards[0]} and {hand1.cards[0]} ')
    hand1_copy=copy.deepcopy(hand1)
    hand2_copy=copy.deepcopy(hand2)
    diff = CARD_VALUES.index(hand2_copy.cards[0])-CARD_VALUES.index(hand1_copy.cards[0])
    if diff < 0:
        return 1
    if diff > 0:
        return -1
    hand1_copy.cards=hand1_copy.cards[1::]
    hand2_copy.cards=hand2_copy.cards[1::]
    return get_winning(hand1_copy, hand2_copy)



def sort_by_hand_type(hands: list[Hand], score_map: dict, include_jolly=False):
    for hand in hands:
        score_map=get_hand_type(hand, score_map, include_jolly)
    return score_map


def sort_hands_of_same_type(hands: list[Hand]):
    cmp=cmp_to_key(get_winning)
    return sorted(hands, key=cmp, reverse=True)

def sort_same_type_blocks(hand_types_dict: dict):
    for k, val in hand_types_dict.items():   #TODO: turn into comprehension???
        hand_types_dict[k] = sort_hands_of_same_type(val)
    return hand_types_dict

def p1():
    hands= parse_hands(INP)
    hand_types_dict = sort_by_hand_type(hands, SCORE_MAP)
    hand_types_dict = sort_same_type_blocks(hand_types_dict)
    # print(hand_types_dict)
    shift_by=0
    score=0
    for _, hands in hand_types_dict.items():
        for idx, hand in enumerate(hands):
            print("scoring", hand, idx+1, shift_by)
            score+=hand.bid*(idx+1+shift_by)
        shift_by+=len(hands)
    return score


def p2():
    
    hands= parse_hands(INP)
    hand_types_dict = sort_by_hand_type(hands, SCORE_MAP, include_jolly=True)
    hand_types_dict = sort_same_type_blocks(hand_types_dict)
    # print(hand_types_dict)

    shift_by=0
    score=0
    for _, hands in hand_types_dict.items():
        for idx, hand in enumerate(hands):
            # print("scoring", hand, idx+1, shift_by)
            score+=hand.bid*(idx+1+shift_by)
        shift_by+=len(hands)
    return score




# hands= parse_hands(INP)
# print(hands)
# hand_types_dict = sort_by_hand_type(hands, SCORE_MAP)
# hand_types_dict = sort_same_type_blocks(hand_types_dict)
# sorted_hands=sort_hands_of_same_type(hand_types_dict['221'])
# print(sorted_hands)


# print(p2())



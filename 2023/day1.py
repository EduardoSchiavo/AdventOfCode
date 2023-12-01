import re

with open('inputs/input1.txt') as ifile:
    inp=ifile.read().splitlines()

SPELLED_OUT_DIGITS = {
                    'one': 1, 
                    'two':2 , 
                    'three': 3, 
                    'four': 4, 
                    'five': 5, 
                    'six': 6, 
                    'seven': 7, 
                    'eight': 8,
                    'nine': 9, 
                    'zero': 0
}
    

def extract_digits(line: str)-> int:
    digits = []
    for char in list(line):
        if char.isnumeric():
            digits.append(char)
            break
    for char in list(line)[::-1]:
        if char.isnumeric():
            digits.append(char)
            break
    return int("".join(digits))

def convert_spelled_out_digits_to_ints(line: str):
    to_insert={}
    for spelled_digit, digit in SPELLED_OUT_DIGITS.items():
        matches = re.finditer(spelled_digit, line)
        for m in matches:
            to_insert[m.start()] = digit
    line = list(line)
    for idx, d in to_insert.items():
        line[idx]=str(d)
    return ''.join(line)


def p1(inp):    
    print(sum([extract_digits(line) for line in inp]))

def p2(inp):
    p1([convert_spelled_out_digits_to_ints(line) for line in inp])


p1(inp) #53386

p2(inp) #53312



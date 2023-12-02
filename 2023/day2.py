import math
import re


with open('inputs/input2.txt') as ifile:
    INP=ifile.read().splitlines()


BAG_CONTENT={
    'red': 12,
    'green': 13,
    'blue': 14
}

def get_cube_values(game: str)-> dict:
    vals = {}
    for color in BAG_CONTENT.keys():
        matches = re.findall(fr'(\d+) ({color})', game)
        vals[color]= max([int(match[0]) for match in matches])
    return vals

def is_possible(game_values: dict)-> bool:
    if any(game_values.get(color) > BAG_CONTENT.get(color) for color in BAG_CONTENT.keys()):
        return False
    return True

def parse_games(games: list)-> dict:
    parsed_games={}
    for idx, game in enumerate(games):
        parsed_games[idx+1]=get_cube_values(game)
    return parsed_games

def p1(input: list)-> int:
    return sum( {idx: game for idx, game in parse_games(input).items() if is_possible(game)}.keys())

def p2(input: list)-> int:
    return sum([math.prod([value for value in game.values()]) for game in parse_games(input).values()])
        

print(p1(INP)) #3099
print(p2(INP))  #72970
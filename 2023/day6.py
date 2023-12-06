import math


with open('inputs/input6.txt') as ifile:
    INP=ifile.read().splitlines()

print(INP)

def parse_races(times_and_distances: list[str]):
    times = times_and_distances[0].split(': ')[1].split( )
    distances = times_and_distances[1].split(': ')[1].split( )
    return [(int(t), int(d)) for t, d in zip(times, distances)]


def compute_ways_to_win(game: tuple)-> int:
    ways_to_win = 0
    for hold_time in range(game[0]+1):
        velocity = hold_time      #TODO: shorten 
        distance = (game[0]-hold_time)*velocity
        if distance > game[1]:
            ways_to_win+=1
    return ways_to_win

def parse_races_as_single_race(times_and_distances: list[str])-> tuple:
    time = int(times_and_distances[0].split(': ')[1].replace(" ", ""))
    distance = int(times_and_distances[1].split(': ')[1].replace(" ", ""))
    return time, distance




def p1():
    return math.prod([compute_ways_to_win(game) for game in parse_races(INP)])



# print(p1())

print(parse_races_as_single_race(INP))

def p2():
    return compute_ways_to_win(parse_races_as_single_race(INP))

print(p2())
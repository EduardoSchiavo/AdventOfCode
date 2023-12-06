import math

with open('inputs/input6.txt') as ifile:
    INP=ifile.read().splitlines()

print(INP)

def parse_races(times_and_distances: list[str]):
    times = times_and_distances[0].split(': ')[1].split( )
    distances = times_and_distances[1].split(': ')[1].split( )
    return [(int(t), int(d)) for t, d in zip(times, distances)]

def is_winning_time(time: int, game: tuple)-> bool:
    return (game[0]-time)*time > game[1]

def compute_ways_to_win(game: tuple)-> int:
    ways_to_win_range = []
    for hold_time in range(game[0]+1):
        if is_winning_time(hold_time, game):
            ways_to_win_range.append(hold_time)
            break
    for hold_time in range(game[0]+1, 0, -1):
        if is_winning_time(hold_time, game):
            ways_to_win_range.append(hold_time)
            return ways_to_win_range[1]-ways_to_win_range[0]+1

def parse_races_as_single_race(times_and_distances: list[str])-> tuple:
    time = int(times_and_distances[0].split(': ')[1].replace(" ", ""))
    distance = int(times_and_distances[1].split(': ')[1].replace(" ", ""))
    return time, distance


def p1():
    return math.prod([compute_ways_to_win(game) for game in parse_races(INP)])

def p2():
    return compute_ways_to_win(parse_races_as_single_race(INP))

print(p1())   #625968
print(p2())   #43663323

import regex as re
with open('input.txt') as ifile:
    MAP = ifile.read().splitlines()

# print(MAP)



def parse_sensors_and_beacons(input: list) -> list:
    sensors_and_beacons=[]
    exp=re.compile(r"Sensor at x=([-]?\d*), y=([-]?\d*): closest beacon is at x=([-]?\d*), y=([-]?\d*)")
    for entry in input:
        sensors_and_beacons.append(tuple(map(int,exp.search(entry).group(1,2,3,4))))
    return sensors_and_beacons

# print(parse_sensors_and_beacons(MAP))



def get_distance(point_a: tuple, point_b: tuple) -> int:
    return abs(point_b[0]-point_a[0])+abs(point_b[1]-point_a[1])


def get_sensors_and_distances(map):
    return [((s_and_b[0], s_and_b[1]), get_distance((s_and_b[0], s_and_b[1]), (s_and_b[2], s_and_b[3]))) for s_and_b in parse_sensors_and_beacons(map)]


beacon_list = list(set([(s_and_b[2], s_and_b[3]) for s_and_b in parse_sensors_and_beacons(MAP)]))
print(beacon_list)
sensors_and_distances = get_sensors_and_distances(MAP)
y=2000000
count=0
for x in range(-10000000, 10000000):
    for sensor in sensors_and_distances:
        if (x,y) in beacon_list:
            continue
        if get_distance((x, y), sensor[0]) <= sensor[1]:
            count+=1
            break

print(count)




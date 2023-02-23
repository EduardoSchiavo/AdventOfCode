import regex as re
with open('input.txt') as ifile:
    MAP = ifile.read().splitlines()

# print(MAP)

class Sensor():
    def __init__(self, position: tuple, beacon: tuple):
        self.position=position
        self.beacon=beacon
        self.span=self.get_distance(position, beacon)

    def __repr__(self):
        return f"S: {self.position}, B: {self.beacon}, span: {self.span}"


    def get_distance(self, point_a: tuple, point_b: tuple) -> int:
        return abs(point_b[0]-point_a[0])+abs(point_b[1]-point_a[1])

    def get_distance_from_point(self, point_b):
        return self.get_distance(self.position, point_b)


def convert_to_beacon_list(sensor_list):
    return [sensor.beacon for sensor in sensor_list]


def parse_sensors_and_beacons(input: list) -> list:
    sensor_list=[]
    exp=re.compile(r"Sensor at x=([-]?\d*), y=([-]?\d*): closest beacon is at x=([-]?\d*), y=([-]?\d*)")
    for entry in input:
        s=tuple(map(int,exp.search(entry).group(1,2)))
        b=tuple(map(int,exp.search(entry).group(3,4)))
        sensor_list.append(Sensor(s,b))
    return sensor_list

y=10

sensor_list = parse_sensors_and_beacons(MAP)
removed_beacons = []

count=0
for sensor in sensor_list:
    projection = sensor.get_distance_from_point((sensor.position[0], y))
    if sensor.beacon[1] == y and sensor.beacon not in removed_beacons:
        removed_beacons.append(sensor.beacon)
        count += -2
    if  projection <= sensor.span:
        count+=2 * (sensor.span - projection)

print(count)







# # print(parse_sensors_and_beacons(MAP))



# def get_distance(point_a: tuple, point_b: tuple) -> int:
#     return abs(point_b[0]-point_a[0])+abs(point_b[1]-point_a[1])


# def get_sensors_and_distances(map):
#     return [((s_and_b[0], s_and_b[1]), get_distance((s_and_b[0], s_and_b[1]), (s_and_b[2], s_and_b[3]))) for s_and_b in parse_sensors_and_beacons(map)]


# beacon_list = list(set([(s_and_b[2], s_and_b[3]) for s_and_b in parse_sensors_and_beacons(MAP)]))
# print(beacon_list)
# sensors_and_distances = get_sensors_and_distances(MAP)
# y=2000000
# count=0
# for x in range(-10000000, 10000000):
#     for sensor in sensors_and_distances:
#         if (x,y) in beacon_list:
#             continue
#         if get_distance((x, y), sensor[0]) <= sensor[1]:
#             count+=1
#             break

# print(count)




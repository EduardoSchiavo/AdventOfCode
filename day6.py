with open("inputs/input6.txt") as ifile:
    INPUT = ifile.read()

example6="mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# print(INPUT)

def is_packet_marker(charachters: str)-> bool:
    return charachters[0] not in charachters[1:] and charachters[1] not in charachters[2:] and charachters[2] != charachters[3]

def is_message_marker(charachters: str)-> bool:
    return all([charachters[i] not in charachters[i+1:] for i in range(len(charachters))])


def get_position_after_marker(datastream: str)-> int:
    for i in range(len(datastream)-4):
        if is_packet_marker(datastream[i:i+4]):
            return i+4

def get_position_after_message_marker(datastream: str)-> int:
    for i in range(len(datastream)-14):
        # print(datastream[i:i+14])
        if is_message_marker(datastream[i:i+14]):
            return i+14




print(get_position_after_message_marker(INPUT))
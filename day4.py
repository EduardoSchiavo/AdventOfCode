with open('inputs/input4.txt') as ifile:
    inp=ifile.read().splitlines()


pairs=[line.split(',') for line in inp]


def is_contained(range1:str , range2:str)-> bool:
    return (int(range1.split('-')[0]) <=  int(range2.split('-')[0]) and int(range1.split('-')[1]) >=  int(range2.split('-')[1]))


def do_overlap(range1:str , range2:str)-> bool:
    if int(range1.split('-')[0]) > int(range2.split('-')[1]) or int(range2.split('-')[0]) > int(range1.split('-')[1]):
        return False
    return True



def part_1():
    count=0
    for pair in pairs:
        if is_contained(pair[0], pair[1]):
            count+=1
        elif is_contained(pair[1], pair[0]):
            count+=1
    return count

def part_2():
    count=0
    for pair in pairs:
        if do_overlap(pair[0], pair[1]):
            count+=1
        elif do_overlap(pair[1], pair[0]):
            count+=1
    return count




print(part_1())

print(part_2())


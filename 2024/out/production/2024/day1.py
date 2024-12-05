with open('inputs/input1.txt') as ifile:
    inp=ifile.read().splitlines()


first_list = []
second_list = []
for i in inp:
    first_list.append(int(i.split()[0]))
    second_list.append(int(i.split()[1]))


first_list.sort()
second_list.sort()

def p1():
    total_distance = 0
    for i in range(len(first_list)):
        total_distance += abs(second_list[i]-first_list[i])
    return total_distance

def p2():
    similarity_score = 0
    for i in first_list:
        similarity_score += i*second_list.count(i)
    return similarity_score


print(p1())
print(p2())





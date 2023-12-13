EXAMPLE = "examples/example13.txt"
INPUT = "inputs/input13.txt"


with open(EXAMPLE) as ifile:
    # INP = [ list(line) for line in ifile.read().splitlines()]
    INP =  [pattern.split('\n') for pattern in ifile.read().split('\n\n')]

print(INP)



def parse_patterns(patterns):  #TODO include in initial parsing
    ground_maps = []
    for pattern_idx, pattern in enumerate(patterns):
        ground_maps.append({})
        for r_idx, row in enumerate(pattern):
            for c_idx, element in enumerate(list(row)):
                ground_maps[pattern_idx][(r_idx, c_idx)]=(element)
    return ground_maps


def fold_horizontally(pattern_map: dict, axis: int): 
    
    for i in range(axis):
        for j in range(len(pattern_map)): #FIXME
            try:
                # print(i, j)
                if pattern_map[(j, i)]!=pattern_map[(j, i+(axis+1)*2-1)]:
                    return False
            except KeyError:
                continue
    return True




sample_map = parse_patterns(INP)[0]
print(sample_map)
print(fold_horizontally(sample_map, 6))
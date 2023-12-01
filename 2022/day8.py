import numpy as np
from functools import reduce

with open("inputs/input8.txt") as ifile:
    INP=[[int(n) for n in line] for line in ifile.read().splitlines()]


def is_visible(row, index):
    return all(i < row[index] for i in row[:index])

def count_visible(trees: list):
    count=0
    for i in range(1, len(trees)-1):
        if is_visible(trees, i) and not isinstance(trees[i], float):
            count += 1
            trees[i]=float(trees[i])
    trees.reverse()
    for i in range(1, len(trees)-1):
        if is_visible(trees, i) and not isinstance(trees[i], float):
            count += 1
            trees[i]=float(trees[i])
    trees.reverse()
    return count, trees


def visible(forest: list):
    count=0
    to_rotate=[forest[0]]
    for tree_row in forest[1:-1]:
        visible_count, tree_row = count_visible(tree_row)
        count += visible_count
        to_rotate.append(tree_row)
    to_rotate.append(forest[-1])
    rotated_forest=rotate_array(to_rotate)
    output_forest=[rotated_forest[0]]
    for tree_row in rotated_forest[1:-1]:
        visible, tree_row = count_visible(tree_row)
        count += visible
        output_forest.append(tree_row)
    output_forest.append(rotated_forest[-1])
    return count, rotate_array(rotate_array(rotate_array(output_forest)))

def rotate_array(array):
    return list(map(list, zip(*array[::-1])))

def p1(array):
    return len(array)*4-4 + visible(array)[0]

def get_positions(array):
    positions=[]
    for i, row in enumerate(array):
        for j, _ in enumerate(row):
            if isinstance(array[i][j], float):
                positions.append((i,j))
    return positions

def compute_view(array: list[list], point: tuple)-> int:
    row, col= point
    array = np.array(array)
    views=[0, 0, 0, 0]
    for tree in array[row,col+1:]:
        views[0]+=1
        if tree>=array[row,col]:
            break
    for tree in array[row,col-1::-1]:
        views[1]+=1
        if tree>=array[row,col]:
            break
    for tree in array[row+1:,col]:
        views[2]+=1
        if tree>=array[row,col]:
            break
    for tree in array[row-1::-1,col]:
        views[3]+=1
        if tree>=array[row,col]:
            break
    return reduce(lambda x, y: x*y, views)

def compute_views(marked_array: list[list]) -> int:
    return max([compute_view(marked_array, point) for point in get_positions(marked_array)])

def p2(array):
    _, marked=visible(array)
    return compute_views(marked)

print(p1(INP))
print(p2(INP))


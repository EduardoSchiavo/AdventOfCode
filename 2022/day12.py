import heapq
import math



def parse_input(file_path: str)-> list[list]:
    with open(file_path) as ifile:
        return [[compute_height(letter) for letter in line] for line in ifile.read().splitlines()]


def compute_height(letter: str)-> int:
    if letter == "S":
        return 0
    elif letter == "E":
        return 27
    return ord(letter) - 96


def is_accessible(starting_square: int, landing_square: int)-> bool:
    if landing_square - starting_square > 1:
        return False
    return True

def generate_graph(heightmap: list[list])-> dict:
    graph = {}
    for row_idx, row in enumerate(heightmap):
        for col_idx, vertex in enumerate(row):
            graph[vertex]=[]
            if is_accessible(vertex, heightmap[row_idx, col_idx+1]):
                graph[vertex].append(heightmap[row_idx, col_idx+1])


            

def djikstra(graph, source_node):

    #current distances from source 
    distances = {
        source_node: 0
    }

    previous_hops = {}

    for vertex in graph: 
        if vertex != source_node:
            distances[vertex] = math.inf
            previous_hops[vertex] = None


if __name__ == '__main__':
    GRID = parse_input("examples/example12.txt")
    print(GRID)


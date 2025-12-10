import math
import operator
from functools import reduce

from open_input import *
from math import hypot

def get_dist(coord1: tuple[int,...], coord2: tuple[int,...]) -> float:
    return (coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2 + (coord1[2] - coord2[2])**2

def sort_junction_boxes(junction_boxes) -> list:
    distances = []

    for j in range(len(junction_boxes)):
        for o in range(j + 1, len(junction_boxes)):
            # print(junction_box, other_box)
            distances.append((get_dist(junction_boxes[j], junction_boxes[o]), j, o))

    return sorted(distances)

def get_root(x:int) -> int:
    if parent[x] == x:
        return x
    parent[x] = get_root(parent[x])
    return parent[x]

def merge(a:int, b:int) -> None:
    parent[get_root(a)] = get_root(b)

def main_part_one(max_connections:int) -> int:
    for _,a,b in sorted_junction_boxes[:max_connections]:
        merge(a, b)

    # print(parent)
    sizes = [0 for _ in range(len(junction_boxes))]
    for i in range(len(junction_boxes)):
        sizes[get_root(i)] += 1
    print(sizes)
    return reduce(operator.mul, sorted(sizes, reverse=True)[:3])

def main_part_two() -> int:
    circuits = len(junction_boxes)
    for _,a,b in sorted_junction_boxes:
        if get_root(a) == get_root(b):
            continue
        merge(a, b)
        circuits -= 1
        if circuits == 1:
            return junction_boxes[a][0] * junction_boxes[b][0]
    return 0

test = 1
junction_boxes = open_as_list('day8sample.txt') if test else open_as_list('day8.txt')
junction_boxes = [tuple(map(int, line.split(','))) for line in junction_boxes]
sorted_junction_boxes = sort_junction_boxes(junction_boxes)
parent = list(range(len(junction_boxes)))
print(f"the answer to part one is {main_part_one(1000) if not test else main_part_one(10)}")

test = 0
junction_boxes = open_as_list('day8sample.txt') if test else open_as_list('day8.txt')
junction_boxes = [tuple(map(int, line.split(','))) for line in junction_boxes]
sorted_junction_boxes = sort_junction_boxes(junction_boxes)
parent = list(range(len(junction_boxes)))
print(f"the answer to part two is {main_part_two()}")
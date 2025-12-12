from open_input import *

def get_area(x1, y1, x2, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) # since inclusive numbers

def main_part_one():
    test = 0
    r = open_as_list("day9sample.txt") if test else open_as_list("day9.txt")
    r = [tuple(map(int, line.split(','))) for line in r]


    res = [0, (0,0), (0,0)]
    for i in range(len(r)):
        for j in range(i + 1, len(r)):
            curr_area = get_area(r[i][0], r[i][1], r[j][0], r[j][1])
            if curr_area > res[0]: res = curr_area, r[i], r[j]

    print(f"the ans to part one is {res}")

def find_allowed_tiles(tiles):
    allowed = set()

    for k in range(len(tiles)):
        p1 = tiles[k]
        p2 = tiles[(k + 1) % len(tiles)]
        if p1[0] == p2[0]:  # vertical edge
            x = p1[0]
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                allowed.add((x, y))
        else:  # horizontal edge
            y = p1[1]
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                allowed.add((x, y))

    return allowed

def main_part_two():
    test = 1
    r = open_as_list("day9sample.txt") if test else open_as_list("day9.txt")
    r = [tuple(map(int, line.split(','))) for line in r]
    print(r)
    valid_tiles = find_allowed_tiles(r)
    print(valid_tiles)

main_part_two()
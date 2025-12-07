import re
from open_input import *

def split_beam(coord:tuple[int, int]) -> None:
    global grid
    beam_down(tuple((coord[0], coord[1] - 1)))
    beam_down(tuple((coord[0], coord[1] + 1)))
    return


def beam_down(coord:tuple[int, int]) -> None:
    global res
    global grid
    if coord in res:
        return
    coord_y, coord_x = coord[0], coord[1]
    try:
        while True:
            if grid[coord_y][coord_x] == '^':
                res.append((coord_y, coord_x))
                # print(f"splitting at y:{coord_y}, x:{coord_x}")
                split_beam(tuple((coord_y, coord_x)))
                return
            elif grid[coord_y][coord_x] == '|':
                return
            else:
                grid[coord_y][coord_x] = '|'
                coord_y += 1
                # nice_print_grid(grid)
                # print(res, "y", coord_y, "x", coord_x)
                # print("\n")

    except IndexError:
        return

def get_starting_index() -> tuple[int, int]:
    global grid
    for i, row in enumerate(grid):
        if 'S' in row:
            return i, row.index('S')
    return -1, -1

test = 0
res = []
grid = open_as_grid("day7sample.txt") if test else open_as_grid("day7.txt")
start_coord = get_starting_index()
beam_down(start_coord)
print(f"the answer to part one is {len(res)}")

print((sum(line.count('|') for line in grid) - 2) / 2)

# orig_grid = open_as_grid("day7sample.txt") if test else open_as_grid("day7.txt")
# overlaps = [[match.group(1) for match in re.finditer(r'(?=(\^\.\^))', ''.join(line))] for line in orig_grid]
# print(len(overlaps))
# print(f"the answer to part two is {len(res)}")


# def main_part_two():
#     test = 1
#     grid = open_as_grid("day7sample.txt") if test else open_as_grid("day7.txt")
#     res = 0
#     for row in grid:
#         if row.count('^') > 1:
#             res += row.count('^')
#     print(f"the answer to part two is {res}")
#
# main_part_two()
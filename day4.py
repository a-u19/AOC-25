from open_input import *

def valid_roll(orig_x: int, orig_y: int, grid: list[list]) -> bool:
    paper_rolls = 0
    if grid[orig_y][orig_x] == '@':
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                try:
                    if (not (x == 0 and y == 0) and grid[orig_y + y][orig_x + x] == '@'
                            and 0 <= orig_y + y < len(grid) and 0 <= orig_x + x < len(grid[0])):
                        paper_rolls += 1
                        # print(orig_y + y, orig_x + x, grid[orig_y + y][orig_x + x])
                except IndexError:
                    pass
        return True if paper_rolls < 4 else False

    else:
        return False


def main_part_one():
    res = 0
    grid = open_as_grid("day4.txt")
    copy_grid = [row[:] for row in grid]
    nice_print_grid(grid)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # print(x,y,cell)
            if valid_roll(x, y, grid):
                copy_grid[y][x] = 'X'
                res += 1
    # print(nice_print_grid(copy_grid))

    print(f"the ans to part one is {res}")

def main_part_two():

    total = 0

    def remove_rolls(grid:list[list]) -> tuple[int, list[list]]:
        res = 0
        nice_print_grid(grid)
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                # print(x, y, cell)
                if valid_roll(x, y, grid):
                    grid[y][x] = '.'
                    res += 1
        # print(nice_print_grid(copy_grid))
        return res, grid

    grid = open_as_grid("day4.txt")
    res, grid = remove_rolls(grid)
    total += res
    while res != 0:
        res, grid = remove_rolls(grid)
        total += res

    print(f"the ans to part two is {total}")

main_part_two()

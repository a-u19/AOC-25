from pprint import pprint


def open_as_list(input_file:str) -> list:
    return [line.strip() for line in open(input_file).readlines()]

def open_as_string(input_file:str) -> str:
    return open(input_file).read().strip()

def open_as_grid(input_file:str) -> list[list]:
    return [list(line.strip()) for line in open(input_file)]

def nice_print_grid(grid:list[list]) -> None:
    pprint(grid)


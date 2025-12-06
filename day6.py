from open_input import *
import re, pandas as pd
from functools import reduce

def apply_operator(sign: str):
    if sign == "+":
        return lambda items: reduce(lambda x, y: x + y, items)
    elif sign == "-":
        return lambda items: reduce(lambda x, y: x - y, items)
    elif sign == "*":
        return lambda items: reduce(lambda x, y: x * y, items)
    elif sign == "/":
        return lambda items: reduce(lambda x, y: x / y, items)
    else:
        raise ValueError("invalid sign")

def apply_to_cols(df:pd.DataFrame) -> int:
    res = {}

    for column in df.columns:
        values = df[column].iloc[:-1].astype(float)
        operator_str = df[column].iloc[-1]

        operator_func = apply_operator(operator_str)
        res[column] = operator_func(values)

    return int(sum(res.values()))

def main_part_one():
    test = False
    inp = open_as_string("day6sample.txt") if test else open_as_string("day6.txt")
    calcs = []
    for line in inp.split("\n"):
        calcs.append(re.split(r"\s+", line.strip()))
    df = pd.DataFrame(calcs)
    # print(df)
    print(f"the answer to part one is {apply_to_cols(df)}")

def process_inp(inp:str) -> (list, list):
    content = inp.split("\n")
    grid_lines = content[:-1]
    max_len = max(len(line) for line in grid_lines)

    # Pad and transpose
    padded = [list(line.ljust(max_len)) for line in grid_lines]
    columns = [''.join(padded[row][col] for row in range(len(padded))).strip()
               for col in range(max_len)]

    groups = []
    current = []
    for item in columns:
        if item:
            current.append(int(item))
        elif current:
            groups.append(current)
            current = []
    if current:
        groups.append(current)

    # Extract symbols
    symbols = [c for c in content[-1] if c != ' ']
    return groups, symbols

def main_part_two():
    test = False
    inp = open_as_string("day6sample.txt") if test else open_as_string("day6.txt")

    grouped_nums, symbols = process_inp(inp)

    # Calculate result
    result = sum(apply_operator(sym)(nums) for sym, nums in zip(symbols, grouped_nums))

    print(f"The answer to part two is {result}")

main_part_one()
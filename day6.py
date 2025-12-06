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

        # Get the operator function
        operator_func = apply_operator(operator_str)

        # Apply the operator cumulatively (e.g., for +: 5 + 3 = 8)
        if len(values) >= 2:
            # Start with first value
            cumulative_result = values.iloc[0]

            # Apply operator to remaining values
            for i in range(1, len(values)):
                cumulative_result = operator_func(cumulative_result, values.iloc[i])

            res[column] = cumulative_result
        else:
            res[column] = values.iloc[0] if len(values) == 1 else 0

    return int(sum(res.values()))

def convert_col_r_to_l(df_col:pd.DataFrame) -> dict:
    new_nums = {}
    for word in list(df_col.iloc):
        for i, char in enumerate(word[::-1]):
            if i not in new_nums.keys():
                new_nums[i] = char
            else:
                new_nums[i] += char
    print(new_nums)
    return new_nums

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

main_part_two()
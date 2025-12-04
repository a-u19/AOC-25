from open_input import *

def get_max_voltage(row:str) -> int:
    row_list = [int(char) for char in row]
    highest_to_lowest = sorted(list(set(row_list)), reverse=True)
    curr_max = 0
    for digit in highest_to_lowest:
        try:
            temp_max = str(digit) + str(max(row_list[row_list.index(digit) + 1:]))
            # print(temp_max, curr_max)
            curr_max = max(curr_max, int(temp_max))
        except ValueError:
            pass
    return curr_max


def main_part_one():
    inp = open_as_list("day3.txt")
    res = 0
    for row in inp:
        max_voltage = get_max_voltage(row)
        res += max_voltage
    print(f"the answer to part one is {res}")

def get_max_voltage_v2(row:str) -> int:
    row_list = [int(char) for char in row]
    res = ""
    starting_i = 0
    for max_digits in range(12):
        ending_i = len(row) + max_digits - 12 + 1
        if ending_i <= starting_i:
            res += row_list[starting_i:]
            starting_i += 1

        temp_max = max(row_list[starting_i:ending_i])
        starting_i += row_list[starting_i:ending_i].index(temp_max) + 1
        res += str(temp_max)

    print(res)

    return int(res)

def main_part_two():
    inp = open_as_list("day3.txt")
    res = 0
    for row in inp:
        max_voltage = get_max_voltage_v2(row)
        res += max_voltage
    print(f"the answer to part two is {res}")

main_part_two()
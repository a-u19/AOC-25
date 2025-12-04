from open_input import *
from functools import reduce

def invalid_num(num:int) -> bool:
    str_num = str(num)
    if str_num[:len(str_num) // 2] == str_num[len(str_num) // 2:]:
        return True
    else:
        return False

def factors(n):
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def invalid_num_v2(num:int) -> bool:
    for factor in factors(len(str(num))):
        if factor < len(str(num)):
            sub_lists = list(chunks([char for char in str(num)], factor))
            if sub_lists.count(sub_lists[0]) == len(sub_lists):
                return True
    else:
        return False


def main_part_1():
    inp = open_as_string("day2sample.txt")
    res = 0
    for pair in inp.split(","):
        start, end = pair.split("-")
        for nums in range(int(start), int(end) + 1):
            if invalid_num(nums):
                print(nums)
                res += nums

    print(f"part 1 total is {res}")

def main_part_2():
    inp = open_as_string("day2.txt")
    res = 0
    for pair in inp.split(","):
        start, end = pair.split("-")
        for nums in range(int(start), int(end) + 1):
            if invalid_num_v2(nums):
                print(nums)
                res += nums

    print(f"part 2 total is {res}")

main_part_2()
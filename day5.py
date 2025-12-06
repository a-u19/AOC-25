from open_input import *
def is_fresh(ingr_id:int, range_list) -> bool:
    index = binary_search(ingr_id, range_list)
    if index != -1 and ingr_id <= range_list[index][1]:
        return True
    else:
        return False

def binary_search(search_val:int, target_ranges:list) -> int:
    left, right = 0, len(target_ranges)-1

    if not target_ranges or search_val < target_ranges[0][0]:
        return -1

    index = -1
    while left <= right:
        # print(f"left: {left}, right: {right}")
        mid = (left+right)//2
        start, end = target_ranges[mid]
        if start <= search_val:
            index = mid
            left = mid+1
        else:
            right = mid-1

    return index

def merge_ranges(fresh_id_range:list[list[int]]) -> list[list[int]]:
    sorted_ranges = sorted(fresh_id_range, key=lambda x: x[0])
    merged = []

    for start, end in sorted_ranges:
        if not merged:
            # First range
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]

            if start <= last_end + 1:
                # Ranges overlap or are adjacent
                merged[-1] = [last_start, max(last_end, end)]
            else:
                # No overlap
                merged.append([start, end])

    return merged

def main_part_one():

    res = 0

    for ingr in ingr_id:
        if is_fresh(int(ingr), merged_fresh_id_range):
            res += 1
            # print(f"ingr is fresh: {ingr}")

    print(f"the answer to part one is {res}")

def main_part_two():
    res = 0
    for start,end in merged_fresh_id_range:
        res += (end - start) + 1
    print(f"the answer to part two is {res}")

test = False
fresh_id_range, ingr_id = open_as_string("day5sample.txt").split("\n\n") if test else open_as_string("day5.txt").split("\n\n")
ingr_id = [int(x) for x in ingr_id.split("\n")]
fresh_id_range = [[int(y) for y in x.split("-")] for x in fresh_id_range.split("\n")]

merged_fresh_id_range = merge_ranges(fresh_id_range)
main_part_one()
main_part_two()
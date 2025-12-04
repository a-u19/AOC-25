from open_input import *

def spin(dir:str, num:int, curr_num:int) -> int:
    return (curr_num + num) % 100 if dir == "R" else (curr_num - num) % 100

# def spin_v2(dir:str, add_num:int, old_num:int) -> tuple[int, int]:
#     if dir == "R":
#         return (old_num + add_num) % 100, abs((old_num + add_num) // 100) - 1 if old_num == 0 and abs((old_num + add_num) // 100) > 0 else abs((old_num + add_num) // 100)
#     else:
#         return (old_num - add_num) % 100, abs((old_num - add_num) // 100) - 1 if old_num == 0 and abs((old_num + add_num) // 100) > 0 else abs((old_num - add_num) // 100)

def part_1_main():
    inp_list = open_as_list("day1.txt")
    ans = 0
    num = 50
    for line in inp_list:
        old_num = num
        num = spin(line[0], int(line[1:]), num)
        # print(f"line is {line}, old_num is {old_num}, curr num is {num}")
        if num == 0:
            ans += 1
    print(f"ans to part 1 is {ans}")

def part_2_main():
    inp_list = open_as_list("day1.txt")
    ans = 0
    num = 50
    for line in inp_list:
        direction = line[0]
        distance = int(line[1:])

        if direction == "R":
            start = num
            for _ in range(distance):
                start = (start + 1) % 100
                if start == 0:
                    ans += 1
            num = (num + distance) % 100
        else:
            start = num
            for _ in range(distance):
                start = (start - 1) % 100
                if start == 0:
                    ans += 1
            num = (num - distance) % 100

    print(f"ans to part 2 is {ans}")

if __name__ == "__main__":
    part_1_main()
    part_2_main()

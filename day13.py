from random import sample
from typing import List

from utils import read_input


def find_mirror_summary(grid: List[str]):
    result = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows - 1):
        before = i
        after = i+1
        mirror = True

        while before >= 0 and after < rows:
            loop_break_flag = False
            for col in range(cols):
                if grid[before][col] != grid[after][col]:
                    loop_break_flag = True
                    break
            if loop_break_flag:
                mirror =False
                break

            before -= 1
            after += 1

        if mirror :
            result = 100 * (i + 1)

    for i in range(cols - 1):
        before = i
        after = i+1
        mirror = True

        while before >= 0 and after < cols:
            loop_break_flag = False
            for row in range(rows):
                if grid[row][before] != grid[row][after]:
                    loop_break_flag = True
                    break
            if loop_break_flag:
                mirror = False
                break

            before -= 1
            after += 1

        if mirror :
            result = i + 1

    return result


def part1(input_data: List[str])-> int:
    result = 0
    start = 0
    while start < len(input_data):
        try:
            end = input_data.index("", start)
        except ValueError:
            end = len(input_data)

        # print(start, end)
        result += find_mirror_summary(input_data[start: end])
        start = end + 1
        # break
    return result

def find_mirror_summary2(grid: List[str]):
    result = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows - 1):
        before = i
        after = i+1
        mirror = True

        fixed = False
        while before >= 0 and after < rows:
            loop_break_flag = False
            for col in range(cols):
                if grid[before][col] != grid[after][col]:
                    if not fixed:
                        fixed = True
                    else:
                        loop_break_flag = True
                        break
            if loop_break_flag:
                mirror =False
                break

            before -= 1
            after += 1

        if mirror and fixed:
            result = 100 * (i + 1)
            break

    for i in range(cols - 1):
        before = i
        after = i+1
        mirror = True
        fixed = False
        while before >= 0 and after < cols:
            loop_break_flag = False
            for row in range(rows):
                if grid[row][before] != grid[row][after]:
                    if not fixed:
                        fixed = True
                    else:
                        loop_break_flag = True
                        break
            if loop_break_flag:
                mirror = False
                break

            before -= 1
            after += 1

        if mirror and fixed :
            result = i + 1
            break

    return result


def part2(input_data: List[str])-> int:
    result = 0
    start = 0
    while start < len(input_data):
        try:
            end = input_data.index("", start)
        except ValueError:
            end = len(input_data)

        # print(start, end)
        result += find_mirror_summary2(input_data[start: end])
        start = end + 1
        # break
    return result


test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip().splitlines()

assert 405 == part1(test_input)
print(part1(read_input("day13")))

assert 400 == part2(test_input)
print(part2(read_input("day13")))
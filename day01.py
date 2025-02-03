from turtledemo.penrose import start
from typing import List

from utils import read_input

def part1(input_list: List[str]) -> int:
    calibration_value_sum = 0
    for input_str in input_list:
        first_digit = None
        last_digit = None
        for letter in input_str:
            if not letter.isdigit():
                continue

            if not first_digit:
                first_digit = letter
            last_digit = letter

        calibration_value = int(first_digit + last_digit)
        calibration_value_sum += calibration_value

    return calibration_value_sum


def find_digit_str(start_index: int, input_str: str)-> int | None:
    digit_str_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for dsi in range(len(digit_str_list)):
        flag = True
        for i in range(len(digit_str_list[dsi])):
            if start_index + i >= len(input_str) or digit_str_list[dsi][i] != input_str[i + start_index]:
                flag = False
                break

        if flag:
            return dsi + 1

    return None


def part2(input_list: List[str]) -> int:
    calibration_value_sum = 0
    for input_str in input_list:
        first_digit = None
        last_digit = None
        for i in range(len(input_str)):
            if input_str[i].isdigit():
                if not first_digit:
                    first_digit = int(input_str[i])
                last_digit = int(input_str[i])
            else:
                digit = find_digit_str(i, input_str)
                if digit is not None:
                    if not first_digit:
                        first_digit = digit
                    last_digit = digit

        calibration_value = first_digit * 10 + last_digit
        calibration_value_sum += calibration_value

    return calibration_value_sum


input_lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

assert part1(input_lines) == 142

print(part1(read_input("day01")))

input_lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

# print(find_digit_str(0, input_lines[0]))
assert part2(input_lines) == 281

print(part2(read_input("day01")))
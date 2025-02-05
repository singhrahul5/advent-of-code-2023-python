from typing import List

from utils import read_input

none_symbol = set("0123456789.")


def part1(input_data: List[str]) -> int:
    row_count = len(input_data)
    col_count = len(input_data[0])

    part_number_sum = 0
    for row in range(row_count):
        col = 0
        while col < col_count:
            if input_data[row][col].isdigit():
                end_col = col
                while end_col < col_count and input_data[row][end_col].isdigit():
                    end_col += 1

                valid_part = False
                if col > 0 and input_data[row][col - 1] not in none_symbol \
                        or end_col < col_count and input_data[row][end_col] not in none_symbol:
                    valid_part = True

                if not valid_part:
                    for i in range(max(0, col - 1), min(col_count, end_col + 1)):
                        if row != 0 and input_data[row - 1][i] not in none_symbol:
                            # print(row - 1, i)
                            valid_part = True
                            break

                        if row + 1 != row_count and input_data[row + 1][i] not in none_symbol:
                            # print(row + 1, i)
                            valid_part = True
                            break

                if valid_part:
                    part_number = int(input_data[row][col:end_col])
                    # print(part_number)
                    part_number_sum += part_number

                col = end_col
            else:
                col += 1
    return part_number_sum


def part2(input_data: List[str]) -> int:
    row_count = len(input_data)
    col_count = len(input_data[0])

    gear_to_part_dict: dict[tuple[int, int], List[int]] = {}

    for row in range(row_count):
        col = 0
        while col < col_count:
            if input_data[row][col].isdigit():
                end_col = col
                while end_col < col_count and input_data[row][end_col].isdigit():
                    end_col += 1

                part_number = int(input_data[row][col:end_col])

                if col > 0 and input_data[row][col - 1] == '*':
                    if (row, col-1) not in gear_to_part_dict:
                        gear_to_part_dict[(row, col-1)] = []
                    gear_to_part_dict[(row, col-1)].append(part_number)

                if end_col < col_count and input_data[row][end_col] == '*':
                    if (row, end_col) not in gear_to_part_dict:
                        gear_to_part_dict[(row, end_col)] = []
                    gear_to_part_dict[(row, end_col)].append(part_number)

                for i in range(max(0, col - 1), min(col_count, end_col + 1)):
                    if row != 0 and input_data[row - 1][i] == '*':
                        if (row - 1, i) not in gear_to_part_dict:
                            gear_to_part_dict[(row - 1, i)] = []
                        gear_to_part_dict[(row - 1, i)].append(part_number)

                    if row + 1 != row_count and input_data[row + 1][i] == '*':
                        if (row + 1, i) not in gear_to_part_dict:
                            gear_to_part_dict[(row + 1, i)] = []
                        gear_to_part_dict[(row + 1, i)].append(part_number)

                col = end_col
            else:
                col += 1

    gear_ratio_sum = 0

    for part_number_list in gear_to_part_dict.values():
        if len(part_number_list) == 2:
            gear_ratio_sum += (part_number_list[0] * part_number_list[1])

    return gear_ratio_sum


_input_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().splitlines()

# print(part1(_input_lines))
assert part1(_input_data) == 4361
print(part1(read_input("day03")))

assert 467835 == part2(_input_data)
print(part2(read_input("day03")))

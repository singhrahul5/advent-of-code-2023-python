from typing import List

from utils import read_input


def part1(input_data: List[str]):
    sensor_data = [[int(data) for data in input_line.split()] for input_line in input_data]

    extrapolated_value_sum = 0
    for data in sensor_data:
        length = len(data)
        arr = [data + [0]] + [[0] * (length + 1) for _ in range(length)]
        # print(data)
        for row in range(length - 1):
            size = length - row - 1
            for col in range(size):
                arr[row + 1][col] = arr[row][col + 1] - arr[row][col]

        for row in range(length - 1, 0, -1):
            last_col = length - row
            arr[row - 1][last_col + 1] = arr[row - 1][last_col] + arr[row][last_col]

        # print(arr)
        extrapolated_value_sum += arr[0][length]

    return extrapolated_value_sum


def part2(input_data: List[str]):
    sensor_data = [[int(data) for data in input_line.split()] for input_line in input_data]

    extrapolated_value_sum = 0
    for data in sensor_data:
        length = len(data)
        arr = [[0] + data] + [[0] * (length + 1) for _ in range(length)]

        for row in range(length - 1):
            size = length - row
            for col in range(1, size):
                arr[row + 1][col] = arr[row][col + 1] - arr[row][col]

        for row in range(length - 1, 0, -1):
            arr[row - 1][0] = arr[row - 1][1] - arr[row][0]

        # print(arr)
        extrapolated_value_sum += arr[0][0]

    return extrapolated_value_sum


_input_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().splitlines()

assert 114 == part1(_input_data)
print(part1(read_input("day09")))

assert 2 == part2(_input_data)
print(part2(read_input("day09")))


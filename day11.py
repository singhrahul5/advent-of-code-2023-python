from typing import List

from utils import read_input


def part1(input_data: List[str]) -> int:

    rows = len(input_data)
    cols = len(input_data[0])

    galaxy_rows = {}
    galaxy_cols = {}

    # calculating galaxy row after expending of empty rows
    exp_row_count = 0
    for act_row in range(rows):
        galaxy_absent = True
        for act_col in range(cols):
            if input_data[act_row][act_col] == '#':
                galaxy_rows[(act_row, act_col)] = exp_row_count + act_row
                galaxy_absent = False

        if galaxy_absent:
            exp_row_count += 1

    # calculating galaxy col after expending of empty cols
    exp_col_count = 0
    for act_col in range(cols):
        galaxy_absent = True
        for act_row in range(rows):
            if input_data[act_row][act_col] == '#':
                galaxy_cols[(act_row, act_col)] = exp_col_count + act_col
                galaxy_absent = False

        if galaxy_absent:
            exp_col_count += 1

    # print(galaxy_rows)
    # print(galaxy_cols)
    galaxy_idx = []
    for pos in galaxy_rows.keys():
        galaxy_idx.append((galaxy_rows[pos], galaxy_cols[pos]))

    shortest_dist_sum = 0

    for g1 in range(len(galaxy_idx)):
        g1_row, g1_col = galaxy_idx[g1]
        for g2 in range(g1+1, len(galaxy_idx)):
            g2_row, g2_col = galaxy_idx[g2]

            dist = abs(g2_row - g1_row) + abs(g2_col - g1_col)
            shortest_dist_sum += dist

    return shortest_dist_sum


def part2(input_data: List[str]) -> int:
    expending_rate = 1_000_000 - 1
    rows = len(input_data)
    cols = len(input_data[0])

    galaxy_rows = {}
    galaxy_cols = {}

    # calculating galaxy row after expending of empty rows
    exp_row_count = 0
    for act_row in range(rows):
        galaxy_absent = True
        for act_col in range(cols):
            if input_data[act_row][act_col] == '#':
                galaxy_rows[(act_row, act_col)] = exp_row_count + act_row
                galaxy_absent = False

        if galaxy_absent:
            exp_row_count += expending_rate

    # calculating galaxy col after expending of empty cols
    exp_col_count = 0
    for act_col in range(cols):
        galaxy_absent = True
        for act_row in range(rows):
            if input_data[act_row][act_col] == '#':
                galaxy_cols[(act_row, act_col)] = exp_col_count + act_col
                galaxy_absent = False

        if galaxy_absent:
            exp_col_count += expending_rate

    # print(galaxy_rows)
    # print(galaxy_cols)
    galaxy_idx = []
    for pos in galaxy_rows.keys():
        galaxy_idx.append((galaxy_rows[pos], galaxy_cols[pos]))

    shortest_dist_sum = 0

    for g1 in range(len(galaxy_idx)):
        g1_row, g1_col = galaxy_idx[g1]
        for g2 in range(g1 + 1, len(galaxy_idx)):
            g2_row, g2_col = galaxy_idx[g2]

            dist = abs(g2_row - g1_row) + abs(g2_col - g1_col)
            shortest_dist_sum += dist

    return shortest_dist_sum


test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip().splitlines()

assert 374 == part1(test_input)
print(part1(read_input("day11")))

assert 82000210 == part2(test_input)
print(part2(read_input("day11")))
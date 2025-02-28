from sys import flags
from typing import List

from utils import read_input


# def pp(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     for i in range(rows):
#         for j in range(cols):
#             print(grid[i][j], end=" ")
#         print()


def part1(input_data: List[str]) -> int:
    rows = len(input_data)
    cols = len(input_data[0])

    pipe_ends = {"J": (-1, 0, 0, -1),
                 "F": (1, 0, 0, 1),
                 "7": (0, -1, 1, 0),
                 "L": (-1, 0, 0, 1),
                 "|": (-1, 0, 1, 0),
                 "-": (0, -1, 0, 1)}

    def solve(row, col, prev_row, prev_col):
        steps = 1
        flag = True
        while True:
            if not (0 <= row < rows and 0 <= col < cols) or input_data[row][col] == '.':
                flag = False
                break

            if input_data[row][col] == 'S':
                break

            # print(input_data[row][col])
            mr1, mc1, mr2, mc2 = pipe_ends[input_data[row][col]]

            if row + mr1 == prev_row and col + mc1 == prev_col:
                row, col, prev_row, prev_col = row + mr2, col + mc2, row, col
            elif row + mr2 == prev_row and col + mc2 == prev_col:
                row, col, prev_row, prev_col = row + mr1, col + mc1, row, col
            else:
                flag = False
                break

            steps += 1
        # print(steps)
        return flag, steps // 2

    for i in range(rows):
        for j in range(cols):
            if input_data[i][j] != 'S':
                continue

            for mr, mc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                valid, ans = solve(i + mr, j + mc, i, j)
                if valid:
                    return ans

    return -1


def part2(input_data: List[str]) -> int:
    grid = [list(s) for s in input_data]
    # print(grid)
    rows = len(grid)
    cols = len(grid[0])

    pipe_ends = {"J": (-1, 0, 0, -1),
                 "F": (1, 0, 0, 1),
                 "7": (0, -1, 1, 0),
                 "L": (-1, 0, 0, 1),
                 "|": (-1, 0, 1, 0),
                 "-": (0, -1, 0, 1)}

    def find_loop(start_row, start_col):
        loop = set()
        flag = False
        row, col = start_row, start_col
        mr1, mc1, _, _ = pipe_ends[grid[row][col]]
        prev_row = row
        prev_col = col
        row += mr1
        col += mc1

        while True:
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] == '.':
                break

            loop.add((row, col))
            # print(row, col)

            # print(grid[row][col])
            mr1, mc1, mr2, mc2 = pipe_ends[grid[row][col]]

            two_ends = [(row + mr1, col + mc1), (row + mr2, col + mc2)]
            if (start_row, start_col) == (row ,col):
                flag = True
                break


            if (prev_row, prev_col) == two_ends[0] :
                prev_row, prev_col = row, col
                row, col = two_ends[1]
            elif (prev_row, prev_col) == two_ends[1] :
                prev_row, prev_col = row, col
                row, col = two_ends[0]
            else:
                break

        # print(flag)

        return flag, loop

    # find loop and replace the 'S'
    loop_tiles = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                for s_repl in "|-F7LJ":
                    # print(s_repl)
                    grid[i][j] = s_repl
                    valid, loop = find_loop(i , j)
                    if valid:
                        loop_tiles = loop
                        break
                break

    # pp(grid)


    # find tiles within loop
    enclosed_count = 0

    for r in range(rows):
        crossings = 0
        c = 0
        while c <cols:
            if (r, c) in loop_tiles:
                if grid[r][c] == "|":  # Count border crossings
                    crossings += 1
                else:
                    start = c
                    end = c+1

                    while end < cols and grid[r][end] == "-":
                        end +=1

                    if (grid[r][start] == 'F' and grid[r][end] == 'J') or (grid[r][start] == 'L' and grid[r][end] == '7'):
                        crossings += 1

                    # print(r, start, end, crossings)
                    c = end
            elif crossings % 2 == 1:  # If inside the loop (odd crossings)
                # print(r, c)
                enclosed_count += 1

            c += 1

    return enclosed_count


test_input_data = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip().splitlines()

assert 8 == part1(test_input_data)

print(part1(read_input("day10")))

test_input_data = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip().splitlines()
print(part2(test_input_data))

test_input_data = """
...F--7...
.S-J..L-7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
""".strip().splitlines()
print(part2(test_input_data))

print(part2(read_input("day10")))

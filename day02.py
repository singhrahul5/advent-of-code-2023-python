from typing import List

from utils import read_input


def part1(input_lines: List[str]) -> int:
    result = 0

    for game in input_lines:
        game_id_str, cube_reveled_list_str = game.split(": ")
        game_id = int(game_id_str[5:])

        cube_reveled_list = cube_reveled_list_str.replace("; ", ", ").split(", ")

        flag = True
        for cube_reveled in cube_reveled_list:
            cube_count_str, cube_color = cube_reveled.split(" ")
            cube_count = int(cube_count_str)
            if cube_color == "red" and cube_count > 12 \
                    or cube_color == "green" and cube_count > 13 \
                    or cube_color == "blue" and cube_count > 14:
                flag = False
                break

        if flag:
            result += game_id

    return result


def part2(input_lines: List[str]) -> int:
    result = 0

    for game in input_lines:
        _, cube_reveled_list_str = game.split(": ")
        cube_reveled_list = cube_reveled_list_str.replace("; ", ", ").split(", ")

        max_red_cubes = 0
        max_blue_cubes = 0
        max_green_cubes = 0

        for cube_reveled in cube_reveled_list:
            cube_count_str, cube_color = cube_reveled.split(" ")
            cube_count = int(cube_count_str)
            if cube_color == "red":
                max_red_cubes = max(max_red_cubes, cube_count)

            if cube_color == "green":
                max_green_cubes = max(max_green_cubes, cube_count)

            if cube_color == "blue":
                max_blue_cubes = max(max_blue_cubes, cube_count)

        result += (max_red_cubes * max_blue_cubes * max_green_cubes)

    return result


_input_lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

assert part1(_input_lines) == 8

print(part1(read_input("day02")))

assert part2(_input_lines) == 2286

print(part2(read_input("day02")))
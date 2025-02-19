import re
from typing import List, Tuple

from utils import read_input


def extract_data(input_data: List[str]) -> Tuple[str, dict[str, Tuple[str, str]]]:
    navigation = input_data[0]
    network = {}
    for ins in input_data[2:]:
        src, left, right = re.findall(r"\w{3}", ins)
        # print(src, left, right)
        network[src] = (left, right)

    return navigation, network


def part1(input_data: List[str]) -> int:
    navigation, network = extract_data(input_data)

    pos = 'AAA'
    steps = 0
    while pos != 'ZZZ':
        nav_idx = steps % len(navigation)
        turn_idx = 0 if navigation[nav_idx] == 'L' else 1
        pos = network[pos][turn_idx]
        steps += 1

    return steps


# [START] PART 2
def gcd(a: int, b: int) -> int:
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def part2(input_data: List[str]) -> int:
    navigation, network = extract_data(input_data)

    def count_steps_to_end(pos: str) -> Tuple[int, int]:
        visited = set()

        steps = 0
        nav_idx = 0
        # find loop
        while pos[-1] != 'Z':
            visited.add(pos)
            turn_idx = 0 if navigation[nav_idx] == 'L' else 1
            pos = network[pos][turn_idx]
            steps += 1
            nav_idx = (nav_idx + 1) % len(navigation)


        # after loop find next end
        loop_size = 0
        in_loop = False
        while not in_loop or pos[-1] != 'Z':
            turn_idx = 0 if navigation[nav_idx] == 'L' else 1
            pos = network[pos][turn_idx]
            loop_size += 1
            nav_idx = (nav_idx + 1) % len(navigation)

            if not in_loop and pos in visited:
                in_loop = True

            visited.add(pos)

        return steps, loop_size

    positions = [pos for pos in network.keys() if pos[-1] == 'A']

    # result = count_steps_to_end(positions[0])
    # print(result)
    step_list = []
    loop_size_list = []
    for _pos in positions:
        _steps, _loop_size = count_steps_to_end(_pos)
        # print(_steps, _loop_size)
        step_list.append(_steps)
        loop_size_list.append(_loop_size)
        # result = result * _steps // gcd(result, _steps)

    # print(step_list)
    # print(loop_size_list)
    assert step_list == loop_size_list

    result = step_list[0]

    for _steps in step_list:
        result = result * _steps // gcd(result, _steps)

    return result
    # while True:
    #
    #     flag = True
    #     for i in range(1, len(step_list)):
    #         if step_list[i-1] != step_list[i]:
    #             flag = False
    #             break
    #
    #     if flag:
    #         return step_list[0]
    #
    #     max_step = 0
    #     for _steps in step_list:
    #         max_step = max(max_step, _steps)
    #
    #     print(max_step)
    #     for i in range(len(step_list)):
    #         diff = max_step - step_list[i]
    #
    #         step_list[i] += (diff // loop_size_list[i] + (1 if diff % loop_size_list[i] != 0 else 0)) * loop_size_list[i]




# [END] PART 2

_input_data = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()

assert 2 == part1(_input_data)

_input_data = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip().splitlines()

assert 6 == part1(_input_data)

print(part1(read_input("day08")))

_input_data = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip().splitlines()

assert 6 == part2(_input_data)

print(part2(read_input("day08")))

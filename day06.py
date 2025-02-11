from typing import List
import re

from utils import read_input


def part1(input_data: List[str]) -> int:
    time_list = [int(d) for d in re.findall(r"\d+", input_data[0])]
    distance_list = [int(d) for d in re.findall(r"\d+", input_data[1])]

    ans = 1
    for i in range(len(time_list)):
        speed = 1
        remaining_time = time_list[i] - 1
        curr_wining_ways = 0
        while speed < time_list[i]:
            curr_traveled_dist = remaining_time * speed
            if curr_traveled_dist > distance_list[i]:
                curr_wining_ways +=1
            speed +=1
            remaining_time -= 1

        ans *= curr_wining_ways

    return ans



def part2(input_data: List[str]) -> int:
    time = int("".join(re.findall(r"\d+", input_data[0])))
    distance = int("".join(re.findall(r"\d+", input_data[1])))

    speed = 1
    while speed <= time//2 and speed * (time - speed) <= distance:
        speed +=1

    if speed > time//2:
        return 0

    return (time//2 - speed + 1) * 2 - (1 if time % 2 == 0 else 0)


_input_data = """
Time:      7  15   30
Distance:  9  40  200
""".strip().splitlines()

assert 288 == part1(_input_data)
print(part1(read_input("day06")))

assert 71503 == part2(_input_data)
print(part2(read_input("day06")))


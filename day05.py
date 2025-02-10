from mimetypes import inited
from typing import List, Tuple

from utils import read_input


def convert_category(src: int, src_dest_map: List[Tuple[int, int, int]]):
    for src_range_start, dest_range_start, range_len in src_dest_map:
        if src_range_start <= src < (src_range_start + range_len):
            return dest_range_start + src - src_range_start
        if src < src_range_start:
            break
    return src


def part1(input_data: List[str]) -> int:
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    seeds = [int(d) for d in input_data[0][7:].split()]
    index = 2
    while index < len(input_data):
        curr_map = None
        if input_data[index].startswith("seed-to-soil"):
            curr_map = seed_to_soil_map
        if input_data[index].startswith("soil-to-fertilizer"):
            curr_map = soil_to_fertilizer_map
        if input_data[index].startswith("fertilizer-to-water"):
            curr_map = fertilizer_to_water_map
        if input_data[index].startswith("water-to-light"):
            curr_map = water_to_light_map
        if input_data[index].startswith("light-to-temperature"):
            curr_map = light_to_temperature_map
        if input_data[index].startswith("temperature-to-humidity"):
            curr_map = temperature_to_humidity_map
        if input_data[index].startswith("humidity-to-location"):
            curr_map = humidity_to_location_map

        index += 1
        while index < len(input_data) and input_data[index] != "":
            dest_range_start, src_range_start, range_len = [int(d) for d in input_data[index].split()]
            curr_map.append((src_range_start, dest_range_start, range_len))
            index += 1

        curr_map.sort()
        index += 1

    lowest_location = int(1e10)
    for seed in seeds:
        soil = convert_category(seed, seed_to_soil_map)
        fertilizer = convert_category(soil, soil_to_fertilizer_map)
        water = convert_category(fertilizer, fertilizer_to_water_map)
        light = convert_category(water, water_to_light_map)
        temp = convert_category(light, light_to_temperature_map)
        humidity = convert_category(temp, temperature_to_humidity_map)
        location = convert_category(humidity, humidity_to_location_map)
        # print(seed, soil, fertilizer, water, light, temp, humidity, location)
        lowest_location = min(lowest_location, location)

    return lowest_location


def part2(input_data: List[str]) -> int:
    conversion_map_list: List[List[Tuple[int, int, int]]] = []

    # init
    seeds = [int(d) for d in input_data[0][7:].split()]
    index = 2
    while index < len(input_data):
        curr_map = []

        index += 1
        while index < len(input_data) and input_data[index] != "":
            dest_range_start, src_range_start, range_len = [int(d) for d in input_data[index].split()]
            curr_map.append((src_range_start, dest_range_start, range_len))
            index += 1

        curr_map.sort()
        conversion_map_list.append(curr_map)
        index += 1

    def solve(curr_src_start, curr_range_len, map_index):
        # print(curr_src_start, curr_range_len, map_index)
        if map_index == 7:
            return curr_src_start

        result = int(1e10)
        for src_range_start, dest_range_start, range_len in conversion_map_list[map_index]:
            if curr_range_len == 0: break
            # print(result)
            if curr_src_start < src_range_start:
                next_src_start = curr_src_start
                next_range_length = min(curr_range_len, src_range_start - curr_src_start)
                result = min(result, solve(next_src_start, next_range_length, map_index + 1))
                # print(result)
                # remove the range which is already calculated
                curr_src_start += next_range_length
                curr_range_len -= next_range_length

            if curr_src_start < src_range_start + range_len:
                next_src_start = dest_range_start + curr_src_start - src_range_start
                next_range_length = min(curr_range_len, src_range_start + range_len - curr_src_start)
                result = min(result, solve(next_src_start, next_range_length, map_index + 1))
                # print(result)
                # remove the range which is already calculated
                curr_src_start += next_range_length
                curr_range_len -= next_range_length

        if curr_range_len > 0:
            result = min(result, solve(curr_src_start, curr_range_len, map_index+1))

        # print(result)
        return result

    lowest_location = int(1e10)

    for index in range(0, len(seeds), 2):
        lowest_location = min(lowest_location, solve(seeds[index], seeds[index +1], 0))
    # print(lowest_location)
    return lowest_location


_input_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().splitlines()
# print(_input_data)
assert 35 == part1(_input_data)

print(part1(read_input("day05")))

assert 46 == part2(_input_data)

print(part2(read_input("day05")))

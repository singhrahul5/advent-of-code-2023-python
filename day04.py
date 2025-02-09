from typing import List

from utils import read_input


def part1(input_data: List[str]) -> int:
    result = 0
    for line in input_data:
        winning_number_list_str, my_number_list_str = line[line.index(":") + 1:].split(" | ")
        winning_numbers = set(winning_number_list_str.split())
        my_numbers = my_number_list_str.split()
        point = 1
        for num in my_numbers:
            if num in winning_numbers:
                point <<= 1
        point >>= 1
        result += point
    # print(result)
    return result

def part2(input_data: List[str]) -> int:
    card_freq_list = [1 for _ in range(len(input_data) + 1)]

    total_won_cards = 0
    for line in input_data:
        card_num = int(line[5: line.index(": ")])
        winning_number_list_str, my_number_list_str = line[line.index(": "):].split(" | ")
        winning_numbers = set( winning_number_list_str.split())
        my_numbers = my_number_list_str.split()
        winning_card_num = card_num
        for num in my_numbers:
            if num in winning_numbers:
                winning_card_num += 1
                card_freq_list[winning_card_num] += card_freq_list[card_num]

        total_won_cards += card_freq_list[card_num]

    # print(total_won_cards)
    return total_won_cards


_input_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip().splitlines()

assert 13 == part1(_input_data)
print(part1(read_input("day04")))

assert 30 == part2(_input_data)
print(part2(read_input("day04")))
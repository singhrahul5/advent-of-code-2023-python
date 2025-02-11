import functools
from typing import List, Tuple

from utils import read_input


def compare_card_hand1(hand_bid1: Tuple[str, int], hand_bid2: Tuple[str, int]) -> int:
    hand1 = hand_bid1[0]
    hand2 = hand_bid2[0]
    card_rank_map = {"A": 13, "K": 12, "Q": 11, "J": 10, "T":9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4":3, "3": 2, "2": 1}

    def find_hand_type(hand):
        card_count_map = {}
        for card in hand:
            card_count_map[card] = card_count_map.get(card, 0) + 1

        card_freq_list = list(card_count_map.values())
        card_freq_list.sort()
        # print(card_count_map)

        if len(card_freq_list) == 1:
            return 7 # five of a kind
        elif len(card_freq_list) == 2 and card_freq_list[1] == 4:
            return 6 # four of a kind
        elif len(card_freq_list) == 2 and card_freq_list[1] == 3:
            return 5 # full house
        elif len(card_freq_list) == 3 and card_freq_list[2] == 3:
            return 4 # three of a kind
        elif len(card_freq_list) == 3 and card_freq_list[2] == 2:
            return 3 # two pair
        elif len(card_freq_list) == 4 and card_freq_list[3] == 2:
            return 2 # one pair
        else:
            return 1 # high card

    hand1_type = find_hand_type(hand1)
    hand2_type = find_hand_type(hand2)

    # print(hand1_type, hand2_type)

    if hand1_type != hand2_type:
        return hand1_type - hand2_type

    for i in range(len(hand2)):
        if hand1[i] != hand2[i]:
            return card_rank_map[hand1[i]] - card_rank_map[hand2[i]]

    return 0


# print(compare_card_hand(('T55J5', 684), ('QQQJA', 483)))
# exit(1)
def part1(input_data: List[str]) -> int:
    hand_bid_list = []
    for data in input_data:
        hand, bid = data.split()
        hand_bid_list.append((hand, int(bid)))

    # print(hand_bid_list)

    hand_bid_list.sort(key= functools.cmp_to_key(compare_card_hand1))

    # print(hand_bid_list)
    ans = 0
    for rank in range(len(hand_bid_list)):
        ans += (rank+1) * hand_bid_list[rank][1]
        # print(ans)

    return ans




def compare_card_hand2(hand_bid1: Tuple[str, int], hand_bid2: Tuple[str, int]) -> int:
    hand1 = hand_bid1[0]
    hand2 = hand_bid2[0]
    card_rank_map = {"A": 13, "K": 12, "Q": 11, "T": 10, "9":9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3":3, "2": 2, "J": 1}

    def find_hand_type(hand):
        card_count_map = {'J': 0}
        for card in hand:
            card_count_map[card] = card_count_map.get(card, 0) + 1

        jokers = card_count_map["J"]
        card_count_map.pop("J")

        card_freq_list = list(card_count_map.values())
        card_freq_list.sort()

        if len(card_freq_list) == 0:
            card_freq_list.append(0)

        card_freq_list[-1] += jokers

        # print(card_count_map)

        if len(card_freq_list) == 1:
            return 7 # five of a kind
        elif len(card_freq_list) == 2 and card_freq_list[1] == 4:
            return 6 # four of a kind
        elif len(card_freq_list) == 2 and card_freq_list[1] == 3:
            return 5 # full house
        elif len(card_freq_list) == 3 and card_freq_list[2] == 3:
            return 4 # three of a kind
        elif len(card_freq_list) == 3 and card_freq_list[2] == 2:
            return 3 # two pair
        elif len(card_freq_list) == 4 and card_freq_list[3] == 2:
            return 2 # one pair
        else:
            return 1 # high card

    hand1_type = find_hand_type(hand1)
    hand2_type = find_hand_type(hand2)

    # print(hand1_type, hand2_type)

    if hand1_type != hand2_type:
        return hand1_type - hand2_type

    for i in range(len(hand2)):
        if hand1[i] != hand2[i]:
            return card_rank_map[hand1[i]] - card_rank_map[hand2[i]]

    return 0


def part2(input_data: List[str]) -> int:
    hand_bid_list = []
    for data in input_data:
        hand, bid = data.split()
        hand_bid_list.append((hand, int(bid)))

    # print(hand_bid_list)

    hand_bid_list.sort(key=functools.cmp_to_key(compare_card_hand2))

    # print(hand_bid_list)
    ans = 0
    for rank in range(len(hand_bid_list)):
        ans += (rank + 1) * hand_bid_list[rank][1]
        # print(ans)

    return ans



_input_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().splitlines()

assert 6440 == part1(_input_data)
print(part1(read_input("day07")))

assert 5905 == part2(_input_data)
print(part2(read_input("day07")))
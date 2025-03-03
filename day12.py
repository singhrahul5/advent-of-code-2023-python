import time
from typing import List

from utils import read_input


def extract_data(input_data: List[str]):
    # print(input_data)
    damaged_group_size_list = []
    condition_record_list = []

    for line in input_data:
        condition_record, group_size_str = line.split()
        dg_size = [int(d) for d in group_size_str.split(",")]
        condition_record_list.append(condition_record)
        damaged_group_size_list.append(dg_size)

    return condition_record_list, damaged_group_size_list


def solve_rec(curr_dgs: int, cr_index: int, dgs_index: int, cr: str, dgs: List[int]):
    if dgs_index == len(dgs):
        return 1 if cr.find('#', cr_index) == -1 else 0

    if cr_index == len(cr):
        return 0

    ans = 0
    if cr[cr_index] == '#':
        if curr_dgs == -1:
            ans = 0
        elif curr_dgs + 1 == dgs[dgs_index]:
            ans = solve_rec(-1, cr_index + 1, dgs_index+1, cr, dgs)
        elif curr_dgs + 1 < dgs[dgs_index]:
            ans = solve_rec(curr_dgs + 1, cr_index + 1, dgs_index, cr, dgs)
    elif cr[cr_index] == '?':
        if curr_dgs == -1:
            ans = solve_rec(0, cr_index+1, dgs_index, cr, dgs)
        elif curr_dgs == 0 :
            ans = solve_rec(0, cr_index+1, dgs_index, cr, dgs)
            if curr_dgs + 1 == dgs[dgs_index]:
                ans += solve_rec(-1, cr_index + 1, dgs_index + 1, cr, dgs)
            elif curr_dgs + 1 < dgs[dgs_index]:
                ans += solve_rec(curr_dgs + 1, cr_index + 1, dgs_index, cr, dgs)
            else:
                print("did not expected")
        else:
            if curr_dgs + 1 == dgs[dgs_index]:
                ans = solve_rec(-1, cr_index + 1, dgs_index + 1, cr, dgs)
            elif curr_dgs + 1 < dgs[dgs_index]:
                ans = solve_rec(curr_dgs + 1, cr_index + 1, dgs_index, cr, dgs)
            else:
                print("did not expected")
    else:
        if curr_dgs == -1 or curr_dgs == 0:
            ans = solve_rec(0, cr_index + 1, dgs_index, cr, dgs)

    return ans


def part1(input_data: List[str]) -> int:
    cr_list, dgs_list = extract_data(input_data)

    result = 0
    for i in range(len(cr_list)):
        result += solve_rec(0, 0, 0, cr_list[i], dgs_list[i])

    return result

def solve_memo(curr_dgs: int, cr_index: int, dgs_index: int, cr: str, dgs: List[int], memo):
    if dgs_index == len(dgs):
        return 1 if cr.find('#', cr_index) == -1 else 0

    if cr_index == len(cr):
        return 0

    if memo[curr_dgs + 1][cr_index][dgs_index] != -1:
        return memo[curr_dgs + 1][cr_index][dgs_index]

    ans = 0
    if cr[cr_index] == '#':
        if curr_dgs == -1:
            ans = 0
        elif curr_dgs + 1 == dgs[dgs_index]:
            ans = solve_memo(-1, cr_index + 1, dgs_index + 1, cr, dgs, memo)
        elif curr_dgs + 1 < dgs[dgs_index]:
            ans = solve_memo(curr_dgs + 1, cr_index + 1, dgs_index, cr, dgs, memo)
    elif cr[cr_index] == '?':
        if curr_dgs == -1:
            ans = solve_memo(0, cr_index + 1, dgs_index, cr, dgs, memo)
        elif curr_dgs == 0 :
            ans = solve_memo(0, cr_index + 1, dgs_index, cr, dgs, memo)
            if curr_dgs + 1 == dgs[dgs_index]:
                ans += solve_memo(-1, cr_index + 1, dgs_index + 1, cr, dgs, memo)
            elif curr_dgs + 1 < dgs[dgs_index]:
                ans += solve_memo(curr_dgs + 1, cr_index + 1, dgs_index, cr, dgs, memo)
            else:
                print("did not expected")
        else:
            if curr_dgs + 1 == dgs[dgs_index]:
                ans = solve_memo(-1, cr_index + 1, dgs_index + 1, cr, dgs, memo)
            elif curr_dgs + 1 < dgs[dgs_index]:
                ans = solve_memo(curr_dgs + 1, cr_index + 1, dgs_index, cr, dgs, memo)
            else:
                print("did not expected")
    else:
        if curr_dgs == -1 or curr_dgs == 0:
            ans = solve_memo(0, cr_index + 1, dgs_index, cr, dgs, memo)

    memo[curr_dgs + 1][cr_index][dgs_index] = ans
    return ans


def part2(input_data: List[str]) -> int:
    cr_list, dgs_list = extract_data(input_data)

    result = 0
    for i in range(len(cr_list)):
        n = len(cr_list[i])*5 + 7

        _memo = [[[-1] * n for _ in range(n)] for _ in range(n)]
        _cr =  "?".join([cr_list[i] for _ in range(5)])
        _dgs = dgs_list[i]*5
        result += solve_memo(0, 0, 0,_cr, _dgs, _memo)

    # print(result)
    return result

test_input= """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip().splitlines()

# print(extract_data(test_data))
assert 21 == part1(test_input)

print(part1(read_input("day12")))

assert 525152 == part2(test_input)

print(part2(read_input("day12")))
import string
from itertools import islice


def calc_value_for_char(char):
    if char in string.ascii_lowercase:
        o = ord(char) - 96
    if char in string.ascii_uppercase:
        o = ord(char) - 64 + 26
    return o


def part1():
    s = 0
    with open("input.txt") as input_file:
        for line in input_file:
            line = line.strip()
            half_index = len(line.strip())//2
            first_half, last_half = line[:half_index], line[half_index:]
            in_common = set(first_half).intersection(set(last_half))
            char_in_common = in_common.pop()
            value_for_in_common = calc_value_for_char(char_in_common)
            s += value_for_in_common
    print(s)


def part2():
    N_LINES_IN_BATCH = 3
    s = 0
    with open("input.txt") as input_file:
        while True:
            lines = islice(input_file, N_LINES_IN_BATCH)
            l_lines = list(lines)
            if not l_lines:
                break
            first_line, second_line, third_line = l_lines
            first_set, second_set, third_set = set(first_line.strip()), set(
                second_line.strip()), set(third_line.strip())
            in_common = first_set.intersection(
                second_set).intersection(third_set)
            char_in_common = in_common.pop()
            value_for_in_common = calc_value_for_char(char_in_common)
            s += value_for_in_common
    print(s)


part2()

import string
from itertools import islice


def calc_value_for_char(char):
    if char in string.ascii_lowercase:
        o = ord(char) - 96
    if char in string.ascii_uppercase:
        o = ord(char) - 64 + 26
    return o


def part1():
    file1 = open("input.txt", 'r')
    lines = file1.readlines()
    s = 0
    for line in lines:
        line = line.strip()
        l = len(line)
        half_index = int(l/2)
        first_half, last_half = line[:half_index], line[half_index:]
        first_set = set(first_half)
        last_set = set(last_half)
        in_common = first_set.intersection(last_set)
        char_in_common = in_common.pop()
        value_for_in_common = calc_value_for_char(char_in_common)
        s += value_for_in_common
    print(s)


def part2():
    N_LINES_IN_BATCH = 3
    s = 0
    with open("input.txt") as f:
        while True:
            lines = islice(f, N_LINES_IN_BATCH)

            l_lines = list(lines)
            if not l_lines:
                break
            first_line, second_line, third_line = l_lines[0], l_lines[1], l_lines[2]
            print(first_line)
            first_set, second_set, third_set = set(first_line.strip()), set(
                second_line.strip()), set(third_line.strip())
            in_common = first_set.intersection(
                second_set).intersection(third_set)
            char_in_common = in_common.pop()
            value_for_in_common = calc_value_for_char(char_in_common)
            print(char_in_common)
            print(value_for_in_common)
            s += value_for_in_common
    print(s)


def main():
    part2()


if __name__ == "__main__":
    main()

import string
from itertools import islice


def part1():
    s = 0
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            fst_range_with_dash, scd_range_with_dash = line.split(",")
            fst_lower, fst_upper = fst_range_with_dash.split('-')
            scd_lower, scd_upper = scd_range_with_dash.split('-')
            fst_lower, fst_upper = int(fst_lower), int(fst_upper)
            scd_lower, scd_upper = int(scd_lower), int(scd_upper)
            a_in_b = set(range(fst_lower, fst_upper+1)).issubset(
                range(scd_lower, scd_upper+1))
            b_in_a = set(range(scd_lower, scd_upper+1)).issubset(
                range(fst_lower, fst_upper+1))
            if a_in_b or b_in_a:
                s += 1

    print(s)


def part2():

    s = 0
    with open("input.txt", "r") as input_file:
        for line in input_file:
            line = line.strip()
            fst_range_with_dash, scd_range_with_dash = line.split(",")
            fst_lower, fst_upper = fst_range_with_dash.split('-')
            scd_lower, scd_upper = scd_range_with_dash.split('-')
            fst_lower, fst_upper = int(fst_lower), int(fst_upper)
            scd_lower, scd_upper = int(scd_lower), int(scd_upper)
            a_in_b = set(range(fst_lower, fst_upper+1)).intersection(
                range(scd_lower, scd_upper+1))
            b_in_a = set(range(scd_lower, scd_upper+1)).intersection(
                range(fst_lower, fst_upper+1))
            if a_in_b or b_in_a:
                s += 1
    print(s)


part2()

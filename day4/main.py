import string
from itertools import islice


def part1():
    file1 = open("input.txt", 'r')
    lines = file1.readlines()
    s = 0
    for line in lines:
        line = line.strip()
        fst_range_with_dash, scd_range_with_dash = line.split(",")
        fst_lower, fst_upper = fst_range_with_dash.split('-')
        scd_lower, scd_upper = scd_range_with_dash.split('-')
        fst_lower, fst_upper = int(fst_lower), int(fst_upper)
        scd_lower, scd_upper = int(scd_lower), int(scd_upper)
        print(fst_lower)
        print(fst_upper)
        print(scd_lower)
        print(scd_upper)
        a_in_b = set((range(fst_lower, fst_upper+1))).issubset(
            range(scd_lower, scd_upper+1))
        print(a_in_b)
        b_in_a = set((range(scd_lower, scd_upper+1))).issubset(
            range(fst_lower, fst_upper+1))
        print(b_in_a)
        if a_in_b or b_in_a:
            s += 1

    print(s)


def part2():
    file1 = open("input.txt", 'r')
    lines = file1.readlines()
    s = 0
    for line in lines:
        line = line.strip()
        fst_range_with_dash, scd_range_with_dash = line.split(",")
        fst_lower, fst_upper = fst_range_with_dash.split('-')
        scd_lower, scd_upper = scd_range_with_dash.split('-')
        fst_lower, fst_upper = int(fst_lower), int(fst_upper)
        scd_lower, scd_upper = int(scd_lower), int(scd_upper)
        a_in_b = set((range(fst_lower, fst_upper+1))).intersection(
            range(scd_lower, scd_upper+1))
        print(a_in_b)
        b_in_a = set((range(scd_lower, scd_upper+1))).intersection(
            range(fst_lower, fst_upper+1))
        print(b_in_a)
        if a_in_b or b_in_a:
            s += 1

    print(s)


def main():
    part2()


if __name__ == "__main__":
    main()

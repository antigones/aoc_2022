
def part1():
    with open("input.txt") as input_file:
        for line in input_file:
            datastream = line.strip().split()[0]
            for candidate_marker_position in range(4, len(datastream)):
                candidate_marker = datastream[candidate_marker_position -
                                              4:candidate_marker_position]
                if len(set(candidate_marker)) == 4:
                    print('marker_position')
                    print(candidate_marker_position)
                    break


def part2():
    with open("input.txt") as input_file:
        for line in input_file:
            datastream = line.strip().split()[0]
            for candidate_marker_position in range(14, len(datastream)):
                candidate_marker = datastream[candidate_marker_position -
                                              14:candidate_marker_position]
                if len(set(candidate_marker)) == 14:
                    print('marker_position')
                    print(candidate_marker_position)
                    break


part2()

from collections import deque

"""

"""

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

containers = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P'],
]


def part1():
    with open("input.txt") as input_file:
        for line in input_file:
            parts = line.strip().split()
            how_many, from_rig, to_rig = int(
                parts[1]), int(parts[3]), int(parts[5])
            elements_to_move = containers[from_rig-1][-how_many:]
            containers[from_rig-1] = containers[from_rig-1][:-how_many]
            elements_to_move.reverse()
            for element in elements_to_move:
                containers[to_rig-1].append(element)
    print(containers)


def part2():
    with open("input.txt") as input_file:
        for line in input_file:
            parts = line.strip().split()
            how_many, from_rig, to_rig = int(
                parts[1]), int(parts[3]), int(parts[5])
            elements_to_move = containers[from_rig-1][-how_many:]
            containers[from_rig-1] = containers[from_rig-1][:-how_many]
            for element in elements_to_move:
                containers[to_rig-1].append(element)
    print(containers)


part2()

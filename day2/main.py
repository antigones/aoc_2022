def part1():
    # X,A rock
    # Y,B paper
    # Z,C scissor
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    encoded_score_dict = {
        # draw
        'XA': 3,
        'YB': 3,
        'ZC': 3,

        # win
        'XC': 6,
        'ZB': 6,
        'YA': 6,

        # lose
        'XB': 0,
        'YC': 0,
        'ZA': 0


    }
    score_shape = {'X': 1, 'Y': 2, 'Z': 3}

    file1 = open("input.txt", 'r')
    lines = file1.readlines()
    my_tot_score = 0
    for line in lines:
        opponent_move, my_move = line.strip().split(" ")
        key = my_move+""+opponent_move
        round_score = encoded_score_dict[key]
        my_tot_score += score_shape[my_move] + round_score

    print(my_tot_score)


def part2():
    # X,A rock
    # Y,B paper
    # Z,C scissor
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    # ...but now you need to figure out what shape to choose so the round ends as indicated
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    encoded_score_dict = {
        # draw
        'XA': 3,
        'YB': 3,
        'ZC': 3,

        # win
        'XC': 6,
        'ZB': 6,
        'YA': 6,

        # lose
        'XB': 0,
        'YC': 0,
        'ZA': 0
    }

    # X, need to lose
    # Y, need to draw
    # Z, need to win

    # X,A rock
    # Y,B paper
    # Z,C scissor
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    move_should_i_play = {
        # Y, need to draw
        'YA': 'X',
        'YB': 'Y',
        'YC': 'Z',

        # X, need to lose
        'XB': 'X',
        'XA': 'Z',
        'XC': 'Y',

        # Z, you need to win
        'ZA': 'Y',
        'ZB': 'Z',
        'ZC': 'X',

    }

    score_shape = {'X': 1, 'Y': 2, 'Z': 3}

    file1 = open("input.txt", 'r')
    lines = file1.readlines()
    my_tot_score = 0
    # A Y
    # B X
    # C Z
    for line in lines:
        opponent_move, how_should_it_end = line.strip().split(" ")
        my_move = move_should_i_play[how_should_it_end+opponent_move]
        key = my_move+""+opponent_move
        round_score = encoded_score_dict[key]
        my_tot_score += score_shape[my_move] + round_score

    print(my_tot_score)


def main():
    part2()


if __name__ == "__main__":
    main()

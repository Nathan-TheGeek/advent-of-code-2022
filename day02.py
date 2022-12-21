from common.inputfile import InputFile

OPPONENT_ROCK = 'A'
OPPONENT_PAPER = 'B'
OPPONENT_SCISSORS = 'C'
PLAYER_ROCK = 'X'
PLAYER_PAPER = 'Y'
PLAYER_SCISSORS = 'Z'
OUTCOME_LOSE = 'X'
OUTCOME_DRAW = 'Y'
OUTCOME_WIN = 'Z'
GAME_WON = 6
GAME_LOST = 0
GAME_DRAW = 3
POINTS_ROCK = 1
POINTS_PAPER = 2
POINTS_SCISSORS = 3

def part1(lines):
    totalPoints = 0
    for line in lines:
        values = line.split(' ')
        totalPoints += get_round_point_values(values[0], values[1])
    return str(totalPoints);


def part2(lines) :
    totalPoints = 0
    for line in lines:
        values = line.split(' ')
        playerValue = get_player_move(values[0], values[1])
        totalPoints += get_round_point_values(values[0], playerValue)
    return str(totalPoints)

def ensure_known_states(opponent, player):
    # check the player and opponent moves to make sure they are valid.
    if opponent != OPPONENT_PAPER and opponent != OPPONENT_ROCK and opponent != OPPONENT_SCISSORS:
        raise Exception('Unknown opponent state. ' + opponent)
    if player != PLAYER_PAPER and player != PLAYER_ROCK and player != PLAYER_SCISSORS:
        raise Exception("Unknown player option. " + player)

def get_round_point_values(opponent, player):
    ensure_known_states(opponent, player)
    if player == PLAYER_ROCK:
        if opponent == OPPONENT_ROCK:
            return POINTS_ROCK + GAME_DRAW
        elif opponent == OPPONENT_PAPER:
            return POINTS_ROCK + GAME_LOST
        elif opponent == OPPONENT_SCISSORS:
            return POINTS_ROCK + GAME_WON
    elif player == PLAYER_PAPER:
        if opponent == OPPONENT_ROCK:
            return POINTS_PAPER + GAME_WON
        elif opponent == OPPONENT_PAPER:
            return POINTS_PAPER + GAME_DRAW
        elif opponent == OPPONENT_SCISSORS:
            return POINTS_PAPER + GAME_LOST
    elif (player == PLAYER_SCISSORS):
        if opponent == OPPONENT_ROCK:
            return POINTS_SCISSORS + GAME_LOST
        elif opponent == OPPONENT_PAPER:
            return POINTS_SCISSORS + GAME_WON
        elif opponent == OPPONENT_SCISSORS:
            return POINTS_SCISSORS + GAME_DRAW

def get_player_move(opponent, outcome):
    ensure_known_states(opponent, outcome)
    if (outcome == OUTCOME_WIN):
        if opponent == OPPONENT_ROCK:
            return PLAYER_PAPER
        elif opponent == OPPONENT_PAPER:
            return PLAYER_SCISSORS
        elif opponent == OPPONENT_SCISSORS:
            return PLAYER_ROCK
    elif (outcome == OUTCOME_DRAW): 
        if opponent == OPPONENT_ROCK:
            return PLAYER_ROCK
        elif opponent == OPPONENT_PAPER:
            return PLAYER_PAPER
        elif opponent == OPPONENT_SCISSORS:
            return PLAYER_SCISSORS
    elif (outcome == OUTCOME_LOSE):
        if opponent == OPPONENT_ROCK:
            return PLAYER_SCISSORS
        elif opponent == OPPONENT_PAPER:
            return PLAYER_ROCK
        elif opponent == OPPONENT_SCISSORS:
            return PLAYER_PAPER

if __name__ == '__main__':
    # input = InputFile('input-files/day02-sample.txt')
    input = InputFile('input-files/day02.txt')
    lines = input.get_contents_by_line()
    part1 = part1(lines)
    part2 = part2(lines)
    print("part 1:" + part1)
    print("part 2:" + part2)
from copy import deepcopy
from itertools import product
from collections import deque, defaultdict
from typing import List


def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line.split(": ")[-1] for line in f.readlines()]
        lines = [int(line.strip()) for line in lines]
        return lines


def roll_100_die():
    while True:
        for i in range(1, 101):
            yield i


def print_score(game):
    s = f"""
    Player 1: {game['player_1']['position'][0]}
    Player 1: {game['player_1']['score']}
    Player 2: {game['player_2']['position'][0]}
    Player 2: {game['player_2']['score']}
    Rolls   : {num_die_rolls}
"""
    print(s)


def solve_1(path: str):
    data = read_lines(path)
    num_die_rolls = 0
    die = roll_100_die()

    game = {
        "player_1": {
            "position": data[0],
            "score": 0
        },

        "player_2": {
            "position": data[1],
            "score": 0
        }
    }

    loosing_player = None
    while True:
        # Player 1
        die_roll = sum(next(die) for _ in range(3))
        num_die_rolls += 3
        game["player_1"]["position"] = ((game["player_1"]["position"] - 1) + die_roll) % 10 + 1
        game["player_1"]["score"] += game["player_1"]["position"]
        if game["player_1"]["score"] >= 1000:
            loosing_player = game["player_2"]
            break

        # Player 2
        die_roll = sum(next(die) for _ in range(3))
        num_die_rolls += 3
        game["player_2"]["position"] = ((game["player_2"]["position"] - 1) + die_roll) % 10 + 1
        game["player_2"]["score"] += game["player_2"]["position"]

        if game["player_2"]["score"] >= 1000:
            loosing_player = game["player_1"]
            break

    return loosing_player["score"] * num_die_rolls


def solve_2(path: str):
    data = read_lines(path)
    print(data)
    
    possible_dirac_outcomes = list(map(sum, product([1, 2, 3], repeat=3)))

    # Create score map where;
    # key = sum of three rolls
    # value = number of combination with sum == key
    score_map = defaultdict(int)
    for outcome in possible_dirac_outcomes:
        score_map[outcome] += 1
    

    def play_round(p1_pos, p1_score, p2_pos, p2_score, dimension_count):
        p1_wins = 0
        p2_wins = 0

        for roll_sum_1, count_1 in score_map.items():
            _dimension_count_1 = dimension_count * count_1
            _p1_pos = ((p1_pos - 1) + roll_sum_1) % 10 + 1
            _p1_score = _p1_pos + p1_score
            if _p1_score >= 21:
                p1_wins += _dimension_count_1
                continue

            for roll_sum_2, count_2 in score_map.items():
                _dimension_count_2 = _dimension_count_1 * count_2
                _p2_pos = ((p2_pos - 1) + roll_sum_2) % 10 + 1
                _p2_score = _p2_pos + p2_score
                if _p2_score >= 21:
                    p2_wins += _dimension_count_2
                    continue

                _p1_wins, _p2_wins = play_round(_p1_pos, _p1_score, _p2_pos, _p2_score, _dimension_count_2)

                p1_wins += _p1_wins
                p2_wins += _p2_wins
            
        return (p1_wins, p2_wins)

    return max(play_round(data[0], 0, data[1], 0, 1))



if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")

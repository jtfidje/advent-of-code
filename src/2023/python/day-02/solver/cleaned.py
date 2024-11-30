# flake8: noqa: F841
import re
from functools import reduce
from pathlib import Path
from typing import Any

data_path = Path(__file__).parent.parent.absolute() / "data"


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        lines = [line.split(": ")[1] for line in lines]
        return lines


def solve_1(path: str) -> int:
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    possible_games = []
    for game_number, line in enumerate(read_lines(path), start=1):
        for game in line.split("; "):
            cube_sets = list(map(lambda g: g.split(), game.split(", ")))
            for num, color in cube_sets:
                if max_cubes[color] < int(num):
                    break
            else:
                continue
            break
        else:
            # If we didn't break out of the loop, we have a valid game
            possible_games.append(game_number)
    
    return sum(possible_games)
    

def solve_2(path: str) -> int:
    powers = []
    for line in read_lines(path):
        max_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for game in line.split("; "):
            cube_sets = list(map(lambda g: g.split(), game.split(", ")))
            for num, color in cube_sets:
                max_cubes[color] = max(max_cubes[color], int(num))
    
        powers.append(reduce(lambda x, y: x * y, max_cubes.values()))
    return sum(powers)


if __name__ == "__main__":
    example_1 = solve_1(Path(data_path, "example_1.txt"))
    if example_1 is not None:
        print(f"Example 1: {example_1}")

    example_2 = solve_2(Path(data_path, "example_2.txt"))
    if example_2 is not None:
        print(f"Example 2: {example_2}")

    print("\n- - -\n")

    problem_1 = solve_1(Path(data_path, "input.txt"))
    if problem_1 is not None:
        print(f"Problem 1: {problem_1}")

    problem_2 = solve_2(Path(data_path, "input.txt"))
    if problem_2 is not None:
        print(f"Problem 2: {problem_2}")

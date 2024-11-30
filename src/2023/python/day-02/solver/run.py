# flake8: noqa: F841
import re
from functools import reduce  # noqa: F401
from pathlib import Path
from typing import Any

data_path = Path(__file__).parent.parent.absolute() / "data"


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        lines = [line.split(": ")[1] for line in lines]
        return lines


def solve_1(path: str) -> Any:
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    pattern = r"((\d+) (blue|green|red)(?:, )?)"
    possible_games = []

    data = read_lines(path)
    for game_number, game in enumerate(data, start=1):
        for turn in game.split("; "):
            res = re.findall(pattern, turn)
            is_possible = True
            for match in res:
                num, color = match[1], match[2]
                if max_cubes[color] < int(num):
                    is_possible = False
                    break
            if not is_possible:
                break
        else:
            possible_games.append(game_number)
    return sum(possible_games)
    

def solve_2(path: str) -> Any:
    pattern = r"((\d+) (blue|green|red)(?:, )?)"
    possible_games = []
    result = 0
    data = read_lines(path)
    for game_number, game in enumerate(data, start=1):
        max_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for turn in game.split("; "):
            res = re.findall(pattern, turn)
            for match in res:
                num, color = match[1], match[2]
                max_cubes[color] = max(max_cubes[color], int(num))
        power = reduce(lambda x, y: x * y, max_cubes.values())
        result += power
    return result


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

# flake8: noqa: F401

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from advent_of_code import utils
from aoc_2015_14 import DATA_PATH


@dataclass
class Deer:
    points: int
    state: Literal["RUN", "REST"]
    counter: int
    distance: int

    speed: int
    stamina: int
    rest: int


def solve(path: str | Path, travel_time: int):
    data = utils.read_lines(path)
    leaderboard: list[Deer] = []

    for line in data:
        leaderboard.append(Deer(0, "REST", 0, 0, *map(int, re.findall(r"(\d+)", line))))

    for _ in range(travel_time):
        for deer in leaderboard:
            if deer.counter == 0:
                match deer.state:
                    case "RUN":
                        deer.state = "REST"
                        deer.counter = deer.rest
                    case "REST":
                        deer.state = "RUN"
                        deer.counter = deer.stamina

            deer.counter -= 1
            if deer.state == "REST":
                continue

            deer.distance += deer.speed

        best_distance = max(deer.distance for deer in leaderboard)
        for deer in leaderboard:
            if deer.distance == best_distance:
                deer.points += 1

    return max(deer.points for deer in leaderboard)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt", travel_time=2503)
    if answer is not None:
        print(f"Problem 2: {answer}")

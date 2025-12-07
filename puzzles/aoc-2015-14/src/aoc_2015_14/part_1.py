# flake8: noqa: F401
import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_14 import DATA_PATH


def solve(path: str | Path, travel_time: int):
    data = utils.read_lines(path)

    lead = 0
    for line in data:
        speed, stamina, rest = map(int, re.findall(r"(\d+)", line))
        seconds = 0
        distance = 0
        while seconds < travel_time:
            new_time = seconds + stamina
            distance += (min(new_time, travel_time) - seconds) * speed
            seconds = new_time
            seconds += rest

        lead = max(distance, lead)

    return lead


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt", travel_time=2503)
    print(f"Problem 1: {answer}")

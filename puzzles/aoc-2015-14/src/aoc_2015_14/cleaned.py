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


def parse_data(path: Path) -> list[Deer]:
    data = utils.read_lines(path)
    deer: list[Deer] = [
        Deer(
            points=0,
            state="REST",
            counter=0,
            distance=0,
            speed=int(speed),
            stamina=int(stamina),
            rest=int(rest),
        )
        for line in data
        for speed, stamina, rest in re.findall(r"(\d+)", line)
    ]

    return deer


def solve_1(path: Path, travel_time: int):
    data = utils.read_lines(path)

    lead = 0
    for line in data:
        speed, stamina, rest = map(int, re.findall(r"(\d+)", line))
        seconds = 0
        distance = 0
        while seconds < travel_time:
            new_time = seconds + stamina
            distance += (min(new_time, travel_time) - seconds) * speed
            seconds = new_time + rest

        lead = max(distance, lead)

    return lead


def solve_2(path: Path, travel_time: int):
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
    answer = solve_1(DATA_PATH / "input.txt", travel_time=2503)
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt", travel_time=2503)
    print(f"Problem 2: {answer}")

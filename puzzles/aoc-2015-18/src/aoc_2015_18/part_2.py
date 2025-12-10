# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_18 import DATA_PATH


def solve(path: str | Path, steps: int):
    data = [list(line) for line in utils.read_lines(path)]

    CORNERS = {
        (0, 0),
        (0, len(data[0]) - 1),
        (len(data) - 1, 0),
        (len(data) - 1, len(data[0]) - 1),
    }

    for _ in range(steps):
        new_states: list[tuple[int, int, str]] = []
        for x, line in enumerate(data):
            for y, char in enumerate(line):
                if (x, y) in CORNERS:
                    continue

                num_on = utils.get_adjacent(
                    x, y, matrix=data, include_corners=True, return_values=True
                ).count("#")

                if char == "#":
                    if 2 <= num_on <= 3:
                        state = (x, y, "#")
                    else:
                        state = (x, y, ".")
                else:
                    if num_on == 3:
                        state = (x, y, "#")
                    else:
                        state = (x, y, ".")

                new_states.append(state)
        for x, y, char in new_states:
            data[x][y] = char

    return sum(line.count("#") for line in data)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt", steps=100)
    if answer is not None:
        print(f"Problem 2: {answer}")

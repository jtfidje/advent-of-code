# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2025_07 import DATA_PATH


def solve(path: str | Path):
    data = utils.read_lines(path)
    data[0] = data[0].replace("S", "|")
    beam_pos = (0, data[0].index("|"))

    beam_positions: list[tuple[int, int]] = [beam_pos]

    splits = 0
    while beam_positions:
        pos = beam_positions.pop(0)
        x, y = (pos[0] + 1, pos[1])

        if x >= len(data):
            continue

        if data[x][y] == "^":
            splits += 1

            y_right = y + 1
            if y_right < len(data[0]):
                new_pos = (x, y_right)
                if new_pos not in beam_positions:
                    beam_positions.append(new_pos)

            y_left = y - 1
            if y_left >= 0:
                new_pos = (x, y_left)
                if new_pos not in beam_positions:
                    beam_positions.append(new_pos)

        elif data[x][y] == ".":
            new_pos = (x, y)
            if new_pos not in beam_positions:
                beam_positions.append(new_pos)

    return splits


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

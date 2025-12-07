# flake8: noqa: F401

from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2025_07 import DATA_PATH


def worker(
    matrix: list[str], splitters: dict[tuple[int, int], int], pos: tuple[int, int]
) -> int:
    while True:
        x, y = pos[0] + 1, pos[1]

        if x >= len(matrix):
            return 1

        if matrix[x][y] == ".":
            pos = (x, y)
            continue

        if (n := splitters.get((x, y), 0)) > 0:
            return n

        for dir_ in (-1, 1):
            new_pos = (x, y + dir_)

            if new_pos[1] < 0 or new_pos[1] >= len(matrix[0]):
                continue

            splitters[(x, y)] += worker(matrix, splitters, new_pos)

        return splitters[(x, y)]


def solve(path: str | Path):
    data = utils.read_lines(path)
    data[0] = data[0].replace("S", "|")
    beam_pos = (0, data[0].index("|"))

    return worker(matrix=data, splitters=defaultdict(int), pos=beam_pos)


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")

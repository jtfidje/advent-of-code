from collections import defaultdict
from pathlib import Path

from advent_of_code import utils
from aoc_2025_07 import DATA_PATH


def solve_1(path: Path):
    data = utils.read_lines(path)
    beam_positions: list[tuple[int, int]] = [(0, data[0].index("S"))]
    max_x, max_y = len(data), len(data[0])

    splits = 0
    while beam_positions:
        pos = beam_positions.pop(0)
        x, y = pos[0] + 1, pos[1]

        if x >= max_x:
            continue

        if data[x][y] == ".":
            new_pos = (x, y)
            if new_pos not in beam_positions:
                beam_positions.append(new_pos)
            continue

        splits += 1
        for new_pos in ((x, y + 1), (x, y - 1)):
            if new_pos[1] < 0 or new_pos[1] == max_y:
                continue

            if new_pos in beam_positions:
                continue

            beam_positions.append(new_pos)

    return splits


def solve_2(path: Path):
    data = utils.read_lines(path)
    beam_pos = (0, data[0].index("S"))
    MAX_X, MAX_Y = len(data), len(data[0])

    def worker(
        matrix: list[str], splitters: dict[tuple[int, int], int], pos: tuple[int, int]
    ) -> int:
        while True:
            x, y = pos[0] + 1, pos[1]

            if x >= MAX_X:
                return 1

            if matrix[x][y] == ".":
                pos = (x, y)
                continue

            if (n := splitters.get((x, y), 0)) > 0:
                return n

            for new_pos in ((x, y + 1), (x, y - 1)):
                if new_pos[1] < 0 or new_pos[1] == MAX_Y:
                    continue

                splitters[(x, y)] += worker(matrix, splitters, new_pos)

            return splitters[(x, y)]

    return worker(matrix=data, splitters=defaultdict(int), pos=beam_pos)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")

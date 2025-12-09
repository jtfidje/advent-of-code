# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2025_09 import DATA_PATH


def print_grid(grid: list[list[str]]):
    print()
    print()
    for row in grid:
        print("".join(row))
    print()


def solve(path: str | Path):
    data = utils.read_line_numbers(path)
    data.append(data[0])
    data = [(x, y) for x, y in data]

    ranges = []
    for a, b in utils.sliding_window(data, window_size=2, step=1):
        r = (
            range(min(a[0], b[0]), max(a[0], b[0]) + 1),
            range(min(a[1], b[1]), max(a[1], b[1]) + 1),
        )
        ranges.append(r)

    data.append(data[1])

    ranges = sorted(ranges, key=lambda x: (x[0].start, x[1].start))

    corner_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []
    best = 0
    for a, point, b in utils.sliding_window(data, window_size=3, step=1):
        # Check left, down
        for x in range(a[0], b[0]):
            p = (x, b[1])
            if p in data:
                corner_pairs.append((point, p))
                best = max(
                    best, ((abs(point[0] - p[0]) + 1) * (abs(point[1] - p[1]) + 1))
                )
                break

        # Check right, down
        for i in range(a[0] + 1, b[0] + 1):
            p = (i, a[1])
            if p in data:
                corner_pairs.append((point, p))
                best = max(
                    best, ((abs(point[0] - p[0]) + 1) * (abs(point[1] - p[1]) + 1))
                )
                break

        # Check left, up
        min_y = min(point[1], a[1])
        min_x = min(point[0], a[0])

        for x in range(point[0] - 1, min_x + 1, -1):
            p = (x, min_y)
            if p in data:
                corner_pairs.append((point, p))
                best = max(
                    best, ((abs(point[0] - p[0]) + 1) * (abs(point[1] - p[1]) + 1))
                )
                break

    # print()
    # for pair in corner_pairs:
    #     print(*pair)
    return best


"""
..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
"""


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")

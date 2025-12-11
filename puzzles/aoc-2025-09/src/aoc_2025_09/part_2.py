# flake8: noqa: F401

import itertools
from pathlib import Path

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from advent_of_code import utils
from aoc_2025_09 import DATA_PATH


def print_grid(grid: list[list[str]]):
    print()
    print()
    for row in grid:
        print("".join(row))
    print()


def solve_backup(path: str | Path):
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

    ranges = sorted(ranges, key=lambda x: (x[0].start, x[1].start))
    best = 0
    polygon = Polygon(data[:-1])
    for X, A in itertools.combinations(data[:-1], 2):
        x, y = X
        a, b = A

        area = (abs(a - x) + 1) * (abs(b - y) + 1)

        if area <= best:
            continue

        for i in range(min(x, a), max(x, a) + 1):
            for j in range(min(y, b), max(y, b) + 1):
                if not polygon.covers(Point(i, j)):
                    break
            else:
                continue

            break
        else:
            best = max(best, area)

    return best


@utils.performance_timer
def solve(path: str | Path):
    data = utils.read_line_numbers(path)
    data.append(data[0])
    data = [(x, y) for x, y in data]

    boundary = set()
    max_x = 0
    max_y = 0
    for a, b in utils.sliding_window(data, window_size=2, step=1):
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                boundary.add((x, y))

    best = 0
    seen_outside = set()
    seen_inside = set()
    for X, A in itertools.combinations(data[:-1], 2):
        x, y = X
        a, b = A
        if x == a or y == b:
            continue

        area = (abs(a - x) + 1) * (abs(b - y) + 1)

        if area <= best:
            continue
        min_x_, max_x_ = min(x, a), max(x, a)
        min_y_, max_y_ = min(y, b), max(y, b)
        border_ = []
        for x_ in range(min_x_, max_x_ + 1):
            border_.append((x_, min_y_))
            border_.append((x_, max_y_))
        for y_ in range(min_y_, max_y_ + 1):
            border_.append((min_x_, y_))
            border_.append((max_x_, y_))

        for point in border_:
            if point in seen_outside:
                break

            if point in boundary or point in seen_inside:
                continue

            crossings = sum(
                (x_, point[1]) in boundary for x_ in range(point[0] + 1, max_x + 1)
            )

            if crossings % 2 == 0:
                seen_outside.add(point)
                break
            else:
                seen_inside.add(point)

        else:
            best = max(best, area)
            print(best)

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
    # answer = solve(DATA_PATH / "example_1_1.txt")
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")

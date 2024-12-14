# flake8: noqa: F401

import re
from functools import reduce
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_lines(path)
    robots = [
        list(map(int, re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line).groups()))  # type: ignore
        for line in data
    ]

    grid = []

    if "example" in (path if isinstance(path, str) else path.as_posix()):
        height = 7
        width = 11
    else:
        height = 103
        width = 101

    for _ in range(height):
        grid.append(["."] * width)

    positions = {(pr, pc): (vr, vc) for pc, pr, vc, vr in robots}

    for pos, vel in positions.items():
        vr = abs(vel[0] * 100)
        vc = abs(vel[1] * 100)

        if vel[0] < 0:
            vr *= -1
        if vel[1] < 0:
            vc *= -1

        pr = (pos[0] + vr) % height
        pc = (pos[1] + vc) % width

        if grid[pr][pc] == ".":
            grid[pr][pc] = 1
        else:
            grid[pr][pc] += 1

    quadrants = [
        ((r, c) for r in range(0, height // 2) for c in range(0, width // 2)),
        ((r, c) for r in range(0, height // 2) for c in range((width // 2) + 1, width)),
        (
            (r, c)
            for r in range((height // 2) + 1, height)
            for c in range(0, width // 2)
        ),
        (
            (r, c)
            for r in range((height // 2) + 1, height)
            for c in range((width // 2) + 1, width)
        ),
    ]

    results = [
        sum(grid[r][c] if grid[r][c] != "." else 0 for r, c in _range)
        for _range in quadrants
    ]

    r, c = height // 2, width // 2
    for i in range(width):
        grid[r][i] = " "
    for i in range(height):
        grid[i][c] = " "

    for line in grid:
        print("".join(map(str, line)))
    return reduce(lambda x, y: x * y, results)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")


"""
  .  .  .  .  
  .  .  .  .  
  .  .  .  .  
  .  .  .  .  
  .  .  .  .  

"""

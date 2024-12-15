# flake8: noqa: F401
import re
import time
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

    height = 103
    width = 101

    for i in range(10403):
        for robot in robots:
            pc, pr, vc, vr = robot
            pr += vr
            pc += vc

            if pr >= height:
                pr = pr % height
            elif pr < 0:
                pr = height + pr

            if pc >= width:
                pc = pc % width
            elif pc < 0:
                pc = width + pc

            robot[0] = pc
            robot[1] = pr

        grid = []
        for _ in range(height):
            grid.append(["."] * width)

        for pc, pr, vc, vr in robots:
            grid[pr][pc] = "#"

        # quadrants = [
        #     ((r, c) for r in range(0, height // 2) for c in range(0, width // 2)),
        #     ((r, c) for r in range(0, height // 2) for c in range((width // 2) + 1, width)),
        #     (
        #         (r, c)
        #         for r in range((height // 2) + 1, height)
        #         for c in range(0, width // 2)
        #     ),
        #     (
        #         (r, c)
        #         for r in range((height // 2) + 1, height)
        #         for c in range((width // 2) + 1, width)
        #     ),
        # ]

        # results = [sum(grid[r][c] for r, c in _range) for _range in quadrants]

        # r, c = height // 2, width // 2
        # for i in range(width):
        #     grid[r][i] = " "
        # for i in range(height):
        #     grid[i][c] = " "

        # grid_string = "".join("".join(row) for row in grid)
        # if i == 0:
        #     first_grid = grid_string
        # else:
        #     if grid_string == first_grid:
        #         print("Repeat after:", i)
        #         break

        grid_string = "\n".join("".join(row) for row in grid)
        if re.search(r"####################", grid_string):
            print(grid_string)
            print(i)
            break

        # for row in grid:
        #     line = "".join(row)
        #     if line.count("#") >= width - 5:
        #         print(i)
        #         break
    return None


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")

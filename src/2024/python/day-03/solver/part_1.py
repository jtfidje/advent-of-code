# flake8: noqa: F401

import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_data(path)
    points = re.findall(r"mul\((\d+,\d+)\)", data)
    
    _sum = 0
    for point in points:
        x, y = point.split(",")
        _sum += int(x) * int(y)

    return _sum
if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

# flake8: noqa: F401
import math
from copy import deepcopy
from functools import cache
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data_raw = [list(line) for line in utils.read_lines(path)]
    data = deepcopy(data_raw)
    _total_size = len(data) * len(data[0])

    visited = set()

    nodes = []
    regions = []
    current_region = {}
    while len(visited) != _total_size:
        if not nodes:
            if current_region:
                regions.extend(current_region.values())

            try:
                node = next(
                    (row_i, col_i)
                    for row_i, row in enumerate(data)
                    for col_i, col in enumerate(row)
                    if col != "."
                )
            except StopIteration:
                ...

            nodes = [node]
            current_region = {data[node[0]][node[1]]: set()}

        current = nodes.pop()
        row_i, col_i = current
        value = data[row_i][col_i]

        if current in visited:
            continue
        else:
            visited.add(current)
            current_region[value].add(current)
            data[row_i][col_i] = "."

        for n in utils.get_adjacent(*current, data, include_corners=False):
            # Only add new values from the current region
            if value == data[n[0]][n[1]] and n not in visited:
                nodes.append(n)

    regions.extend(current_region.values())
    region_map = {tuple(region): 0 for region in regions}
    # Calculate perimiters
    for region in region_map:
        target_value = data_raw[region[0][0]][region[0][1]]

        for row_i, col_i in region:
            # Top and bottom row counts as 1
            if row_i in [0, len(data) - 1]:
                region_map[region] += 1

            # Left and right sides counts as 1
            if col_i in [0, len(data[0]) - 1]:
                region_map[region] += 1

            for r_i, c_i in utils.get_adjacent(
                row_i, col_i, matrix=data_raw, include_corners=False
            ):
                if data_raw[r_i][c_i] != target_value:
                    region_map[region] += 1

    _sum = 0
    for region, perimiter in region_map.items():
        _sum += len(region) * perimiter

    return _sum


if __name__ == "__main__":
    # answer = solve(Path(data_path, "input.txt"))
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

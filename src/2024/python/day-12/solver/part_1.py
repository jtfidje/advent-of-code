# flake8: noqa: F401
import math
from functools import cache
from pathlib import Path

import matplotlib.path as pltPath
import shapely.geometry
import shapely.geometry.polygon
import sympy

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = [list(line) for line in utils.read_lines(path)]
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
        # We need to check if a region is _inside_ another region

        min_row = min_col = math.inf
        max_row = max_col = -math.inf
        for row_i, col_i in region:
            min_row = min(min_row, row_i)
            min_col = min(min_col, col_i)
            max_row = max(max_row, row_i)
            max_col = max(max_col, col_i)

        region_map[region] += _calculate_permiter(region)

        for _region in region_map:
            if _region == region:
                continue

            if len(_region) < 8:
                continue

            polygon = _create_polygon(_region)
            breakpoint()
            res = [polygon.encloses_point(sympy.Point(*point)) for point in region]
            print(_region)
            print(region)
            print(res)
            print()
            if all(res):
                region_map[_region] += _calculate_permiter(region)

    for region, perimiter in region_map.items():
        print(len(region), perimiter)

    return sum(len(region) * perimiter for region, perimiter in region_map.items())


@cache
def _create_polygon(points):
    return sympy.Polygon(*points)


@cache
def _calculate_permiter(points):
    min_row = min_col = math.inf
    max_row = max_col = -math.inf
    for row_i, col_i in points:
        min_row = min(min_row, row_i)
        min_col = min(min_col, col_i)
        max_row = max(max_row, row_i)
        max_col = max(max_col, col_i)

    return int(((max_col - min_col + 1) * 2) + ((max_row - min_row + 1) * 2))


if __name__ == "__main__":
    # answer = solve(Path(data_path, "input.txt"))
    answer = solve(Path(data_path, "example_1_3.txt"))
    print(f"Problem 1: {answer}")

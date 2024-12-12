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
        # We need to check if a region is _inside_ another region

        # min_row = min_col = math.inf
        # max_row = max_col = -math.inf
        # for row_i, col_i in region:
        #     min_row = min(min_row, row_i)
        #     min_col = min(min_col, col_i)
        #     max_row = max(max_row, row_i)
        #     max_col = max(max_col, col_i)

        target_value = data_raw[region[0][0]][region[0][1]]
        for row_i, col_i in region:
            if row_i in [0, len(data) - 1]:
                region_map[region] += 1
            if col_i in [0, len(data[0]) - 1]:
                region_map[region] += 1

            for r_i, c_i in utils.get_adjacent(
                row_i, col_i, matrix=data_raw, include_corners=False
            ):
                if data_raw[r_i][c_i] != target_value:
                    region_map[region] += 1

        # Create matrix to fit the polygon, then flood-fill the perimiter!

        # num_rows = int(max_row - min_row + 1)
        # num_cols = int(max_col - min_col + 1)

        # matrix = [["."] * num_cols for _ in range(num_rows)]

        # for row_i, col_i in region:
        #     matrix[row_i - min_row][col_i - min_col] = "#"

        # flood_fill(matrix)

        # # Now, any remaining "." are other regions!!
        # other_region_points = []
        # for row_i, row in enumerate(matrix):
        #     for col_i, col in enumerate(row):
        #         if col == ".":
        #             other_region_points.append((row_i, col_i))

        # # Find the other regions and add their perimiter to the current
        # counted_regions = []
        # for point in other_region_points:
        #     for _region in counted_regions:
        #         if point in _region:
        #             break
        #     else:
        #         # find the region it is actually in
        #         for _region in region_map:
        #             if point not in _region:
        #                 continue

        #             for row_i, col_i in _region:
        #                 row_i -= min_row
        #                 col_i -= min_col
        #                 _val = matrix[row_i][col_i]

        #                 for r_i, c_i in utils.get_adjacent(
        #                     row_i, col_i, matrix=matrix, include_corners=False
        #                 ):
        #                     if matrix[r_i][c_i] != _val:
        #                         region_map[region] += 1

        #             counted_regions.append(_region)
        #             break

    _sum = 0
    for region, perimiter in region_map.items():
        _sum += len(region) * perimiter

    return _sum


def flood_fill(matrix: list[list[str]]) -> None:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    perimiter = [
        *[(0, j) for j in range(num_cols)],
        *[(num_rows - 1, j) for j in range(num_cols)],
        *[(i, 0) for i in range(num_rows)],
        *[(i, num_cols - 1) for i in range(num_rows)],
    ]

    visited = set()
    while perimiter:
        (row_i, col_i) = node = perimiter.pop(-1)

        if node in visited:
            continue

        if matrix[row_i][col_i] != ".":
            continue

        visited.add(node)
        matrix[row_i][col_i] = "*"
        for next_node in utils.get_adjacent(
            row_i, col_i, matrix=matrix, include_corners=False
        ):
            if next_node in visited:
                continue

            perimiter.append(next_node)

    for line in matrix:
        print("".join(line))
    print()


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

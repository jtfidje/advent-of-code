import math
from typing import Dict, List, Tuple


def read_height_map(path: str) -> List[List[int]]:
    with open(path, "r") as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def check_low_point(i: int, j: int, height_map: List[List[int]]) -> bool:
    neighbours = []

    if i > 0:
        # Above
        neighbours.append(height_map[i - 1][j])

    if i < len(height_map) - 1:
        # Below
        neighbours.append(height_map[i + 1][j])

    if j > 0:
        # Left
        neighbours.append(height_map[i][j - 1])

    if j < len(height_map[0]) - 1:
        # Right
        neighbours.append(height_map[i][j + 1])

    loc = height_map[i][j]
    return all(loc < x for x in neighbours)


def calculate_basin_size(
    i: int, j: int, height_map: List[List[int]], visited: Dict[Tuple[int], bool]
) -> int:
    count = 0
    visited[(i, j)] = True
    if height_map[i][j] == 9:
        return count

    if i > 0:
        # Above
        n_i, n_j = i - 1, j
        if (n_i, n_j) not in visited:
            count += calculate_basin_size(n_i, n_j, height_map, visited)

    if i < len(height_map) - 1:
        # Below
        n_i, n_j = i + 1, j
        if (n_i, n_j) not in visited:
            count += calculate_basin_size(n_i, n_j, height_map, visited)

    if j > 0:
        # Left
        n_i, n_j = i, j - 1
        if (n_i, n_j) not in visited:
            count += calculate_basin_size(n_i, n_j, height_map, visited)

    if j < len(height_map[0]) - 1:
        # Right
        n_i, n_j = i, j + 1
        if (n_i, n_j) not in visited:
            count += calculate_basin_size(n_i, n_j, height_map, visited)

    return count + 1


def solve_1(path: str) -> int:
    height_map = read_height_map(path)
    risk_lvl_sum = 0
    for i, row in enumerate(height_map):
        for j, col in enumerate(row):
            if check_low_point(i, j, height_map):
                risk_lvl_sum += col + 1

    return risk_lvl_sum


def solve_2(path: str) -> int:
    height_map = read_height_map(path)
    basin_sizes = []
    visited = {}
    for i, row in enumerate(height_map):
        for j, col in enumerate(row):
            if (i, j) not in visited:
                size = calculate_basin_size(i, j, height_map, visited)
                basin_sizes.append(size)

    basin_sizes = sorted(basin_sizes)
    return math.prod(basin_sizes[-3:])


if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)

    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")

import math
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        lines = [[int(x) for x in line] for line in lines]
        return lines


def check_low_point(i, j, data):
    neighbours = []

    if i > 0:
        # Above
        neighbours.append(data[i - 1][j])
    
    if i < len(data) - 1:
        # Below
        neighbours.append(data[i + 1][j])
    
    if j > 0:
        # Left
        neighbours.append(data[i][j - 1])
    
    if j < len(data[0]) - 1:
        # Right
        neighbours.append(data[i][j + 1])

    loc = data[i][j]
    return all(loc < x for x in neighbours)
            

def measure_basin(i, j, data, basin_map, visited):
    visited.append((i, j))
    if data[i][j] == 9:
        return 0
    
    count = 1

    if i > 0:
        # Above
        n_i, n_j = i - 1, j
        if (n_i, n_j) not in visited:
            count += measure_basin(n_i, n_j, data, basin_map, visited)
    
    if i < len(basin_map) - 1:
        # Below
        n_i, n_j = i + 1, j
        neighbour = basin_map[n_i][n_j]
        if (n_i, n_j) not in visited:
            count += measure_basin(n_i, n_j, data, basin_map, visited)
    
    if j > 0:
        # Left
        n_i, n_j = i, j - 1
        neighbour = basin_map[n_i][n_j]
        if (n_i, n_j) not in visited:
            count += measure_basin(n_i, n_j, data, basin_map, visited)
    
    if j < len(basin_map[0]) - 1:
        # Right
        n_i, n_j = i, j + 1
        neighbour = basin_map[n_i][n_j]
        if (n_i, n_j) not in visited:
            count += measure_basin(n_i, n_j, data, basin_map, visited)

    return count


def solve_1(path: str) -> int:
    data = read_lines(path)
    locations = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if check_low_point(i, j, data):
                locations.append(col)

    return sum(map(lambda x: x + 1, locations))


def solve_2(path: str) -> int:
    data = read_lines(path)
    basin_map = [[0 for _ in row] for row in data]
    basin_sizes = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == 9:
                continue
        
            basin_map[i][j] = 1
    
    visited = []
    for i, row in enumerate(basin_map):
        for j, col in enumerate(row):
            if (i, j) not in visited:
                size = measure_basin(i, j, data, basin_map, visited)
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

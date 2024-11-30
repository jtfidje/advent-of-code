import numpy as np
import re
from typing import List
import sparse

def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]

        lines = list(map(lambda x: x.split(" "), lines))

        return lines


def parse_ranges(line):
    return list(re.findall(r"([-]?\d+\.\.[-]?\d+)", line))


def parse_ranges_2(line):
    x_range, y_range, z_range = list(re.findall(r"([-]?\d+\.\.[-]?\d+)", line))
    x_range = list(map(int, x_range.split("..")))
    y_range = list(map(int, y_range.split("..")))
    z_range = list(map(int, z_range.split("..")))
    return (x_range, y_range, z_range)

"""
def check_overlap(range_line_1, range_line_2):
    x_range_1, y_range_1, z_range_1 = parse_ranges_2(ranges_1)
    x_range_2, y_range_2, z_range_2 = parse_ranges_2(ranges_2)

    if x_range_2[0] <= x_range_1[0] and x_range_2[1] <=:
        # x2 overlaps x1 from the left. 
        # Check how far inn x1 goes
        ...

    if x_range_2[0] > x_range_1[0]:
        # x2 overlaps x1 from the left
"""

def solve_1(path: str):
    data = read_lines(path)
    
    locations = {}
    for (command, range_line) in data:
        ranges = parse_ranges(range_line)
        x_range, y_range, z_range = ranges
        
        x_start, x_stop = list(map(int, x_range.split("..")))
        x_start = max(x_start, -50)
        x_stop = min(x_stop, 50)
        for x in range(x_start, x_stop + 1):
            y_start, y_stop = list(map(int, y_range.split("..")))
            y_start = max(y_start, -50)
            y_stop = min(y_stop, 50)
            for y in range(y_start, y_stop + 1):
                z_start, z_stop = list(map(int, z_range.split("..")))
                z_start = max(z_start, -50)
                z_stop = min(z_stop, 50)
                for z in range(z_start, z_stop + 1):
                    locations[(x,y,z)] = 1 if command == "on" else 0
    return sum(locations.values())

"""
def solve_2(path: str):
    data = read_lines(path)
    max_x, max_y, max_z = -np.inf, -np.inf, -np.inf
    min_x, min_y, min_z = np.inf, np.inf, np.inf
    for _, range_line in data:
        x_range, y_range, z_range = parse_ranges(range_line)
        x_range = list(map(int, x_range.split("..")))
        min_x = min(min_x, x_range[0])
        max_x = max(max_x, x_range[1])

        y_range = list(map(int, y_range.split("..")))
        min_y = min(min_y, y_range[0])
        max_y = max(max_y, y_range[1])

        z_range = list(map(int, z_range.split("..")))
        min_z = min(min_z, z_range[0])
        max_z = max(max_z, z_range[1])

    dx, dy, dz = (
        abs(min_x - max_x),
        abs(min_y - max_y),
        abs(min_z - max_z),
    )

    main_matrix = sparse.DOK((dx, dy, dz), dtype=np.int8, fill_value=0)
    for command, range_line in data:
        x_range, y_range, z_range = parse_ranges(range_line)
        x_range = list(map(int, x_range.split("..")))
        y_range = list(map(int, y_range.split("..")))
        z_range = list(map(int, z_range.split("..")))

        x_start = x_range[0] + min_x
        x_stop = x_range[1] + min_x

        y_start = y_range[0] + min_y
        y_stop = y_range[1] + min_y

        z_start = z_range[0] + min_z
        z_stop = z_range[1] + min_z

        main_matrix[x_start: x_stop, y_start:y_stop, z_start:z_stop] = 1 if command == "on" else 0
            
"""

if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    path = "example_2.txt"
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")

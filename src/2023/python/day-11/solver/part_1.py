# flake8: noqa: F401
import math
from itertools import combinations
from pathlib import Path
from typing import Self

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str):
    data = utils.read_lines(path)

    empty_rows = []
    empty_cols = []
    
    for row, line in enumerate(data):
        for col in line:
            if col != ".":
                break
        else:
            # Empty row
            empty_rows.append(row)

    for col in range(len(data[0])):
        for row in data:
            if row[col] != ".":
                break
        else:
            # Empty col
            empty_cols.append(col)
            continue

    # Insert rows
    for row in sorted(empty_rows, reverse=True):
        data.insert(row, ["."] * len(data[0]))

    # Insert cols
    for col in sorted(empty_cols, reverse=True):
        for row, line in enumerate(data):
            temp = list(line)
            temp.insert(col, ".")
            data[row] = "".join(temp)

    
    # Enumerate galaxies
    galaxy_map: dict[int, tuple[int, int]] = {}
    counter = 1
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                galaxy_map[counter] = (row, col)
                counter += 1


    # Find path between all galaxy pairs
    result = 0
    for start, stop in combinations(list(galaxy_map.keys()), 2):
        start_pos = galaxy_map[start]
        stop_pos = galaxy_map[stop]
        result += manhatten_distance(start_pos, stop_pos)
    
    return result


def manhatten_distance(pos_1, pos_2):
    return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
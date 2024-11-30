# flake8: noqa: F401
from itertools import combinations
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str, expansion_rate: int):
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

    
    # Enumerate galaxies
    galaxy_map: dict[int, tuple[int, int]] = {}
    counter = 1
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "#":
                galaxy_map[counter] = (row, col)
                counter += 1


    # Find path between all galaxy pairs
    def manhatten_distance(pos_1, pos_2):
        min_row = min([pos_1[0], pos_2[0]])
        max_row = max([pos_1[0], pos_2[0]])

        min_col = min([pos_1[1], pos_2[1]])
        max_col = max([pos_1[1], pos_2[1]])
        
        rows_to_expand = [i for i in empty_rows if i > min_row and i < max_row]
        cols_to_expand = [i for i in empty_cols if i > min_col and i < max_col]

        row_term = abs(pos_1[0] - pos_2[0]) - len(rows_to_expand) + (len(rows_to_expand) * expansion_rate)
        col_term = abs(pos_1[1] - pos_2[1]) - len(cols_to_expand) + (len(cols_to_expand) * expansion_rate)

        return row_term + col_term

    result = 0
    for start, stop in combinations(list(galaxy_map.keys()), 2):
        start_pos = galaxy_map[start]
        stop_pos = galaxy_map[stop]
        result += manhatten_distance(start_pos, stop_pos)
    
    return result



if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"), expansion_rate=1_000_000)
    #answer = solve(Path(data_path, "example_2.txt"), expansion_rate=10)
    if answer is not None:
        print(f"Problem 2: {answer}")
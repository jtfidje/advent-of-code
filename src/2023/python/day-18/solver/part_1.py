import re
# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def flood_fill_outer(matrix):
    # Flood-fill matrix perimiter
    to_visit = [
        *[(0, col) for col in range(len(matrix[0]))],
        *[(len(matrix) - 1, col) for col in range(len(matrix[0]))],
        *[(row, 0) for row in range(len(matrix))],
        *[(row, len(matrix[0]) - 1) for row in range(len(matrix))],
    ]

    visited = {}
    while to_visit:
        pos = to_visit.pop(0)
        visited[pos] = None

        row, col = pos
        symbol = matrix[row][col]

        if symbol != ".":
            continue
        
        temp = list(matrix[row])
        temp[col] = "x"
        matrix[row] = "".join(temp)

        for new_pos in utils.get_adjacent(*pos, matrix=matrix, include_corners=True):
            if new_pos in visited or new_pos in to_visit:
                continue

            to_visit.append(new_pos)

    for line in matrix:
        print(line)


def solve(path: str):
    data = utils.read_lines(path)
    data = [line.split(" (")[0] for line in data]

    pos = (0,0)
    points = []
    min_col = 0
    min_row = 0
    max_col = 0
    max_row = 0
    for line in data:
        direction, number = line.split()
        number = int(number)

        match direction:
            case "R":
                for _ in range(number):
                    pos = (
                        pos[0], 
                        pos[1] + 1
                    )
                    points.append(pos)

                    max_col = max(max_col, pos[1])
                    
            case "L":
                for _ in range(number):
                    pos = (
                        pos[0], 
                        pos[1] - 1
                    )
                    points.append(pos)

                    min_col = min(min_col, pos[1])

            case "U":
                for _ in range(number):
                    pos = (
                        pos[0] - 1, 
                        pos[1]
                    )
                    points.append(pos)

                    min_row = min(min_row, pos[0])

            case "D":
                for _ in range(number):
                    pos = (
                        pos[0] + 1, 
                        pos[1]
                    )
                    points.append(pos)

                    max_row = max(max_row, pos[0])

    matrix = []
    for _ in range(max_row + abs(min_row) + 1):
        line = ["."] * (max_col + abs(min_col) + 1)
        matrix.append(line)

    for point in points:
        row = point[0] + abs(min_row)
        col = point[1] + abs(min_col)

        matrix[row][col] = "#"

    
    flood_fill_outer(matrix)

    with open("/tmp/res.txt", "w") as f:
        for line in matrix:
            f.write("".join(line) + "\n")

    string = ""
    for line in matrix:
        string += "".join(line)

    return string.count("#") + string.count(".")




if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    #answer = solve(Path(data_path, "example_1.txt"))
    print(f"Problem 1: {answer}")
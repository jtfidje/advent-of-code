# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_lines(path)
    # data = [list(map(int, line)) for line in data]
    data = [list(line) for line in data]

    starting_points = [
        (row_i, col_i)
        for row_i, row in enumerate(data)
        for col_i, col in enumerate(row)
        if col == "0"
    ]

    total_score = 0
    for starting_point in starting_points:
        stack = [starting_point]
        visited = set()
        score = 0
        tops = set()
        while stack:
            pos = stack.pop(-1)
            row_i, col_i = pos
            value = data[row_i][col_i]

            if pos in visited:
                continue

            if value == "9":
                if pos not in tops:
                    score += 1
                    tops.add(pos)
                continue

            visited.add(pos)

            adjacent = utils.get_adjacent(row_i, col_i, data, include_corners=False)
            for point in adjacent:
                if data[point[0]][point[1]] == str(int(value) + 1):
                    stack.append(point)

        total_score += score

    return total_score


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

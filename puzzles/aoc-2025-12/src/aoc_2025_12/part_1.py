# flake8: noqa: F401
import re
from pathlib import Path
from copy import deepcopy

from advent_of_code import utils
from aoc_2025_12 import DATA_PATH


def print_grid(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))


def rotate_piece(piece: list[list[str]]) -> list[list[str]]:
    new_piece = []

    for ci in range(len(piece[0])):
        row = [piece[ri][ci] for ri in range(len(piece))][::-1]
        new_piece.append(row)

    return new_piece


def worker(grid: list[list[str]], pieces: list[list[list[str]]]) -> bool:
    if not pieces:
        print_grid(grid)
        print()
        return True

    piece = pieces[0]
    num_to_fit = sum(row.count("#") for row in piece)

    height = len(piece)
    width = len(piece[0])

    for row_i in range(0, len(grid) - height + 1):
        for col_i in range(0, len(grid[0]) - width + 1):
            box = [row[col_i : col_i + width] for row in grid[row_i : row_i + height]]

            box_points = []
            # Get coordinates for the box
            for r in range(row_i, row_i + height):
                for c in range(col_i, col_i + width):
                    box_points.append((r, c))

            # naively check if the piece actually would fit in the box
            if sum(grid[r][c] == "." for r, c in box_points) < num_to_fit:
                continue

            for i in range(4):
                if i > 0:
                    piece = rotate_piece(piece)

                will_fit = True
                for i, row in enumerate(piece):
                    for j, col in enumerate(row):
                        if col == "#" and box[i][j] == "#":
                            will_fit = False
                            break
                    else:
                        continue

                    break

                if not will_fit:
                    continue

                new_grid = deepcopy(grid)

                for value, (r, c) in zip(
                    (col for row in piece for col in row), box_points
                ):
                    if value == "#":
                        new_grid[r][c] = value

                res = worker(grid=new_grid, pieces=pieces[1:])

                if res:
                    return True

    return False


def solve(path: str | Path):
    data = utils.read_data(path)
    pattern = r":\n((?:[#\.]+\n)+)"

    piece_map = {
        i: piece.strip().split() for i, piece in enumerate(re.findall(pattern, data))
    }
    data = data.strip().split("\n\n")[-1]

    regions = []
    for line in data.split("\n"):
        x, y, *qty = utils.parse_integers(line)
        regions.append((x, y, qty))

    result = 0
    for x, y, target in regions:
        grid = [["."] * x for _ in range(y)]

        pieces = []
        for i, num in enumerate(target):
            if num:
                pieces.extend([piece_map[i]] * num)

        result += worker(grid, pieces)

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "example_1_1.txt")
    # answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

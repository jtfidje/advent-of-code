# flake8: noqa: F401
import re
from pathlib import Path
from copy import deepcopy
import numpy as np

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


def worker(grid: np.ndarray, pieces: list[np.ndarray]) -> bool:
    if not pieces:
        print(grid)
        print()
        return True

    num_to_fit = pieces[0].sum()

    p_height, p_width = pieces[0].shape
    g_height, g_width = grid.shape
    for row_i in range(0, g_height - p_height + 1):
        for col_i in range(0, g_width - p_width + 1):
            box = grid[row_i : row_i + p_height, col_i : col_i + p_width]

            # naively check if the piece actually would fit in the box
            if np.logical_not(box).sum() < num_to_fit:
                continue

            for i in range(4):
                piece = np.rot90(pieces[0], k=i)

                combined = np.logical_not(np.logical_and(box, piece))

                if np.all(combined):
                    new_grid = grid.copy()
                    new_grid[row_i : row_i + p_height, col_i : col_i + p_width] |= piece

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
        grid = np.zeros(shape=(x, y), dtype=bool)

        pieces: list[np.ndarray] = []
        for i, num in enumerate(target):
            if num:
                p = piece_map[i]
                piece = np.array([[col == "#" for col in row] for row in p], dtype=bool)
                pieces.extend([piece] * 2)

        result += worker(grid, pieces)

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "example_1_1.txt")
    # answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

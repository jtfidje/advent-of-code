import json
from typing import Generator


def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def sliding_window(
    array: list, window: int, step: int | None = None
) -> Generator[list, None, None]:
    if step is None:
        step = window
    for i in range(0, len(array) - window + 1, step):
        yield array[i : i + window]


def out_of_bounds(row: int, col: int, matrix: list[list]):
    if row < 0 or row >= len(matrix):
        return True
    
    if col < 0 or col >= len(matrix[0]):
        return True
    
    return False


def get_adjacent(row: int, col: int, matrix: list[list], width: int = 1, height: int = 1) -> tuple[int, int]:
    skip_positions = [(row + i, col + j) for i in range(height) for j in range(width)]
    adjacent = []
    for i in range(row - 1, row + 1 + height):
        for j in range(col - 1, col + 1 + width):
            # Skip current position
            if (i, j) in skip_positions:
                continue

            # Check if out of bounds
            if out_of_bounds(row, col, matrix):
                continue
            
            adjacent.append((i, j))
    
    return adjacent

import math
import numpy as np
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        lines = [np.array(list(map(int, line)), dtype=np.float64) for line in lines]
        lines = np.array(lines)
        return lines


def adjacent_cells(grid, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if 0 <= (x + i) < len(grid) and 0 <= y + j < len(grid[0]) and not (i == 0 and j == 0):
                yield [x + i, y + j]


def solve_1(path: str) -> int:
    data = read_lines(path)
    flash_count = 0
    for _ in range(100):
        data += 1

        while indices := np.where(data > 9):
            rows, cols = indices

            if len(rows) == 0:
                break

            for flash_x, flash_y in zip(rows, cols):
                data[flash_x, flash_y] = -math.inf
                flash_count += 1

                idx = adjacent_cells(data, flash_x, flash_y)
                data[tuple(zip(*idx))] += 1
                
        rows, cols = np.where(data == -math.inf)
        data[rows, cols] = 0
    return flash_count


def solve_2(path: str) -> int:
    data = read_lines(path)
    step = 0
    while True:
        step += 1
        data += 1

        while indices := np.where(data > 9):
            rows, cols = indices

            if len(rows) == 0:
                break

            for flash_x, flash_y in zip(rows, cols):
                data[flash_x, flash_y] = -math.inf

                idx = adjacent_cells(data, flash_x, flash_y)
                data[tuple(zip(*idx))] += 1
                
        if np.all(data == -math.inf):
            return step

        rows, cols = np.where(data == -math.inf)
        data[rows, cols] = 0

        # Failsafe....
        if step > 1_000_000:
            break

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

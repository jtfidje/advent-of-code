import math
import numpy as np
from typing import Iterator, List, Tuple

def read_energy_levels(path: str) -> np.array:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [list(map(float, line.strip())) for line in lines]
        return np.array(lines)


def adjacent_cells(grid: np.array, x: int, y: int) -> Iterator[Tuple[int]]:
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if all((
                0 <= (x + i) < len(grid),   # Out-of-bounds check for x
                0 <= y + j < len(grid[0]),  # Out-of-bounds check for y
                not (i == 0 and j == 0)     # Skip origin point (x, y)
            )):
                yield (x + i, y + j)


def solve_1(path: str) -> int:
    energy_levels = read_energy_levels(path)
    
    flash_count = 0
    for _ in range(100):
        energy_levels += 1

        while True:
            rows, cols = np.where(energy_levels > 9)

            if rows.size == 0:
                break

            for flash_x, flash_y in zip(rows, cols):
                flash_count += 1

                # Set flashing octopus level to -inf avoids multiple flashes in one step
                energy_levels[flash_x, flash_y] = -math.inf

                # Increase energy level to all adjacent octopi after a flash
                # ( -inf will not be increased )
                cells = adjacent_cells(energy_levels, flash_x, flash_y)
                energy_levels[tuple(zip(*cells))] += 1
                
        # Reset energy level of all octopi that flashed this step
        energy_levels[np.where(energy_levels == -math.inf)] = 0
    
    return flash_count


def solve_2(path: str) -> int:
    energy_levels = read_energy_levels(path)
    
    step = 0
    while True:
        step += 1
        energy_levels += 1

        while True:
            rows, cols = np.where(energy_levels > 9)

            if rows.size == 0:
                break

            for flash_x, flash_y in zip(rows, cols):
                # Set flashing octopus level to -inf avoids multiple flashes in one step
                energy_levels[flash_x, flash_y] = -math.inf

                # Increase energy level to all adjacent octopi after a flash
                # ( -inf will not be increased )
                cells = adjacent_cells(energy_levels, flash_x, flash_y)
                energy_levels[tuple(zip(*cells))] += 1
                
        # Check to see if all octopi has flashed!
        if np.all(energy_levels == -math.inf):
            return step

        # Reset energy level of all octopi that flashed this step
        energy_levels[np.where(energy_levels == -math.inf)] = 0

        # Failsafe....
        if step > 1_000_000:
            return -1


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

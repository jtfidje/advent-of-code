import numpy as np
import pyperclip
from typing import List

def read_crab_positions(path: str) -> np.array:
    with open(path, "r") as f:
        line = f.read().strip()
        return np.array(list(map(int, line.split(","))))


def solve_1(path: str) -> int:
    crab_positions = read_crab_positions(path)
    possible_positions = np.array(range(
        min(crab_positions),
        max(crab_positions) + 1
    ))
    
    # Turn crab positions into matrix for easier numpy magic
    position_matrix = crab_positions.reshape(len(crab_positions), 1)

    # Calculate distances between crap positions and all possible new positions
    result = position_matrix - possible_positions

    # Make sure the distances are positive integers
    result = np.absolute(result)

    # Calculate total fuel consumption from the sum of all distances
    result = np.sum(result, axis=0)

    # Find the minimum amount of fuel spent
    result = np.min(result)

    return result


def solve_2(path: str) -> int:
    crab_positions = read_crab_positions(path)
    possible_positions = np.array(range(
        min(crab_positions),
        max(crab_positions) + 1
    ))

    # Turn crab positions into matrix for easier numpy magic
    position_matrix = crab_positions.reshape(len(crab_positions), 1)
    
    # Calculate distances between crap positions and all possible new positions
    result = position_matrix - possible_positions
    
    # Make sure the distances are positive integers
    result = np.absolute(result)

    # Calculate fuel as the sum of the number series 0..distance for all distances
    result = result * (result + 1) // 2

    # Calculate the total fuel from all distances
    result = np.sum(result, axis=0)

    # Find the minimum amount of fuel spent
    result = np.min(result)

    return result



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

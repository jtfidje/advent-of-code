from typing import List
from collections import defaultdict

def read_line(path: str) -> List[str]:
    with open(path, "r") as f:
        return f.read().strip()


def solve_1(path: str) -> int:
    data = read_line(path)
    fishes = list(map(int, data.split(",")))
    
    for _ in range(80):
        fishes = list(map(lambda x: x - 1, fishes))
        for i, fish in enumerate(fishes[:]):
            if fish == -1:
                fishes.append(8)
                fishes[i] = 6
    return len(fishes)


def solve_2(path: str) -> int:
    data = read_line(path)
    fishes = list(map(int, data.split(",")))
    population = defaultdict(int)
    count = len(fishes)

    for fish in fishes:
        population[256 - fish] += 1

    for day in range(256, 0, -1):
        if population[day] == 0:
            continue
            
        fish_count = population[day]
        population[day - 7] += fish_count
        population[day - 9] += fish_count
        count += fish_count

    return count


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

from typing import List
from collections import defaultdict


def simulate_lantern_population(initial_population_ages: List[int], days: int):
    growth_schedule = defaultdict(int)
    population_size = len(initial_population_ages)

    # Seed growth schedule with next spawn from the initial ages list
    for age in initial_population_ages:
        growth_schedule[days - age] += 1

    for day in range(days, 0, -1):
        schedule = growth_schedule[day]
        if not schedule:
            continue

        population_size += schedule
        growth_schedule[day - 7] += schedule
        growth_schedule[day - 9] += schedule

    return population_size


def read_initial_population_ages(path: str) -> List[str]:
    with open(path, "r") as f:
        data = f.read().strip()
        return list(map(int, data.split(",")))


def solve_1(path: str) -> int:
    initial_population_ages = read_initial_population_ages(path)
    return simulate_lantern_population(initial_population_ages, 80)


def solve_2(path: str) -> int:
    initial_population_ages = read_initial_population_ages(path)
    return simulate_lantern_population(initial_population_ages, 256)


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

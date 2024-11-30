from copy import copy
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

def read_polymer_instructions(path: str) -> Tuple[str, List[str]]:
    with open(path, "r") as f:
        polymer_template = f.readline().strip()
        
        # Get rid of emtpy line between template and pair insertions
        f.readline()

        pair_insertion = [line.strip() for line in f.readlines() if line]
        return polymer_template, pair_insertion


def solve(input_path: str, runs: int) -> int:
    polymer_template, pair_insertions = read_polymer_instructions(input_path)
    
    insertion_pair_count = defaultdict(int)
    molecule_count = Counter(polymer_template)

    pair_insertion_map = {}
    pair_insertion_result_map = {}
    for insertion_rule in pair_insertions:
        pair, insertion = insertion_rule.split(" -> ")
        pair_insertion_map[pair] = insertion

        a, b = pair
        pair_insertion_result_map[pair] = (f"{a}{insertion}", f"{insertion}{b}")

    # Init. pair count
    for i in range(len(polymer_template) - 1):
        window = polymer_template[i:i + 2]
        pair = "".join(window)
        insertion_pair_count[pair] += 1

    for _ in range(runs):
        for pair, count in copy(insertion_pair_count).items():        
            insertion_pair_count[pair] -= count
            letter = pair_insertion_map[pair]
            molecule_count[letter] += count
            for insertion_pair in pair_insertion_result_map[pair]:
                insertion_pair_count[insertion_pair] += count

    molecules = sorted(molecule_count.values())
    return molecules[-1] - molecules[0]


if __name__ == "__main__":
    ans_1_example = solve(input_path="example.txt", runs=10)    
    ans_2_example = solve(input_path="example.txt", runs=40)

    ans_1_input = solve(input_path="input.txt", runs=10)    
    ans_2_input = solve(input_path="input.txt", runs=40)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")

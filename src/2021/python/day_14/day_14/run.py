from copy import copy
from collections import Counter, defaultdict
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        polymer = f.readline().strip()
        f.readline()
        rules = [line.strip() for line in f.readlines() if line]
        return polymer, rules


def solve_1(path: str):
    polymer, rules = read_lines(path)
    
    rule_map = {}
    for rule in rules:
        left, right = rule.split(" -> ")
        rule_map[left] = right


    for _ in range(10):
        j = 1
        _polymer = polymer[:]
        for i in range(len(_polymer) - 1):
            window = _polymer[i:i + 2]
            pair = "".join(window)
            
            if pair in rule_map:
                polymer = [*polymer[:j], rule_map[pair], *polymer[j:]]
                j += 2
    items = sorted(Counter(polymer).values())
    return items[-1] - items[0]



def solve_2(path: str):
    polymer, rules = read_lines(path)
    
    rule_map = {}
    for rule in rules:
        left, right = rule.split(" -> ")
        rule_map[left] = right

    pair_count = defaultdict(int)
    pair_map = {}
    letter_count = Counter(polymer)

    for pair, char in rule_map.items():
        a, b = pair
        pair_map[pair] = (f"{a}{char}", f"{char}{b}")

    # Init. pair count
    for i in range(len(polymer) - 1):
        window = polymer[i:i + 2]
        pair = "".join(window)
        pair_count[pair] += 1

    for _ in range(40):
        for pair, count in copy(pair_count).items():
            pair_count[pair] -= count
            
            letter = rule_map[pair]
            letter_count[letter] += count
            
            for new in pair_map[pair]:
                pair_count[new] += count

    items = sorted(letter_count.values())
    return items[-1] - items[0]


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

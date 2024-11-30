from collections import defaultdict
from typing import List


def read_navigation_system(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


character_scores = {
    ")": {
        "corrupt": 3,
        "incomplete": 1,
    },
    "]": {
        "corrupt": 57,
        "incomplete": 2,
    },
    "}": {
        "corrupt": 1197,
        "incomplete": 3,
    },
    ">": {
        "corrupt": 25137,
        "incomplete": 4,
    },
}

open_characters = ["(", "[", "{", "<"]
close_characters = [")", "]", "}", ">"]


def calculate_corrupt_syntax_score(corrupt_chars: List[str]) -> int:
    return sum(character_scores[char]["corrupt"] for char in corrupt_chars)


def calculate_incomplete_syntax_score(incomplete_lines: List[List[str]]) -> int:
    scores = []
    for open_chunks in incomplete_lines:
        score = 0
        for open_char in open_chunks[::-1]:
            # Get the corresponding close char
            idx = open_characters.index(open_char)
            close_char = close_characters[idx]

            score *= 5
            score += character_scores[close_char]["incomplete"]

        scores.append(score)
    
    scores = sorted(scores)
    return scores[len(scores) // 2]

def solve_1(path: str) -> int:
    navigation_system = read_navigation_system(path)

    open_chunks = []
    corrupt_chars = []
    for line in navigation_system:
        for char in line:
            if char in open_characters:
                open_chunks.append(char)
            else:
                _char = open_chunks.pop(-1)
                if open_characters.index(_char) != close_characters.index(char):
                    corrupt_chars.append(char)
                    break

    return calculate_corrupt_syntax_score(corrupt_chars)


def solve_2(path: str) -> int:
    navigation_system = read_navigation_system(path)
    incomplete_lines = []

    for line in navigation_system:
        open_chunks = []
        for char in line:
            if char in open_characters:
                open_chunks.append(char)
            else:
                _char = open_chunks.pop(-1)
                if open_characters.index(_char) != close_characters.index(char):
                    break
        else:
            if open_chunks:
                incomplete_lines.append(open_chunks)

    return calculate_incomplete_syntax_score(incomplete_lines)


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

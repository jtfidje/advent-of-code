from collections import defaultdict
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


corrupt_character_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

incomplete_character_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


open_characters = ["(", "[", "{", "<"]
close_characters = [")", "]", "}", ">"]


def solve_1(path: str) -> int:
    data = read_lines(path)
    
    corrupt_syntax_score = 0
    open_chunks = []

    for line in data:
        for char in line:
            if char in open_characters:
                open_chunks.append(char)
            else:
                _char = open_chunks.pop(-1)
                if open_characters.index(_char) != close_characters.index(char):
                    corrupt_syntax_score += corrupt_character_scores[char]
                    break

    return corrupt_syntax_score



def solve_2(path: str) -> int:
    data = read_lines(path)
    
    incomplete_syntax_scores = []
    for line in data:
        incomplete_syntax_score = 0
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
                for open_char in open_chunks[::-1]:
                    idx = open_characters.index(open_char)
                    close_char = close_characters[idx]
                    incomplete_syntax_score *= 5
                    incomplete_syntax_score += incomplete_character_scores[close_char]
                incomplete_syntax_scores.append(incomplete_syntax_score)

    middle_score = len(incomplete_syntax_scores) // 2
    incomplete_syntax_scores = sorted(incomplete_syntax_scores)
    return incomplete_syntax_scores[middle_score]


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

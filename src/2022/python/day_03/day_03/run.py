import string
from collections import defaultdict
from functools import reduce
def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_numbers(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str):
    data = read_lines(path)
    import string
    score = 0
    for line in data:
        part_1 = line[:int(len(line) / 2)]
        part_2 = line[int(len(line) / 2):]

        union = set(part_1).intersection(part_2)
        for char in union:
            s = string.ascii_letters.index(char) + 1
            score += s

    return score



def solve_2(path: str):
    data = read_lines(path)
    score = 0
    for i in range(0, len(data), 3):
        line_1, line_2, line_3 = data[i: i + 3]
        #inter_1 = set(line_1[:int(len(line_1) / 2)]).intersection(line_1[int(len(line_1) / 2):])
        #inter_2 = set(line_2[:int(len(line_2) / 2)]).intersection(line_2[int(len(line_2) / 2):])
        #inter_3 = set(line_3[:int(len(line_3) / 2)]).intersection(line_3[int(len(line_3) / 2):])

        #union = inter_1.intersection(inter_2).intersection(inter_3)
        union = set(line_1).intersection(line_2).intersection(line_3)
        for char in union:
            s = string.ascii_letters.index(char) + 1
            score += s

    return score


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

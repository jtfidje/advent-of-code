
from functools import reduce
def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip().split() for line in lines]
        return lines

    
map_1 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

map_2 = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

def get_move(a, b):
    x = {
        "X": {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        },
        "Y": {
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors"
        },
        "Z": {
            "rock": "paper",
            "scissors": "rock",
            "paper": "scissors"
        }
    }
    
    return x[a][b]

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def check_win(a, b):
    if a == "rock":
        if b == "scissors":
            return 0

        elif b == "paper":
            return 6
        
        else:
            return 3
        
    if a == "scissors":
        if b == "paper":
            return 0
        elif b == "rock":
            return 6
        else:
            return 3
        
    if a == "paper":
        if b == "scissors":
            return 6
        elif b == "rock":
            return 0
        else:
            return 3



def solve_1(path: str):
    data = read_lines(path)
    score = 0
    for line in data:
        a = map_1[line[0]]
        b = map_2[line[1]]

        score += points[b]
        score += check_win(a, b)
    return score

    


def solve_2(path: str):
    data = read_lines(path)
    data = read_lines(path)
    score = 0
    for line in data:
        a = map_1[line[0]]
        b = map_2[line[1]]
        b = get_move(line[1], a)
        
        score += points[b]
        score += check_win(a, b)
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

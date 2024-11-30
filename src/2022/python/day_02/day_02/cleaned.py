def read_data(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip().split() for line in lines]
        return lines

    
map_1 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

map_2 = {
    "A": {
        "X": "scissors",
        "Y": "rock",
        "Z": "paper"
    },
    "B": {
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"       
    },
    "C": {
        "X": "paper",
        "Y": "scissors",
        "Z": "rock"
    }
}

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def score(opponent: str, me: str) -> int:
    if opponent == me:
        return points[me] + 3

    if opponent == "rock":
        return points[me] + (0 if me == "scissors" else 6)

    if opponent == "paper":
        return points[me] + (0 if me == "rock" else 6)

    if opponent == "scissors":
        return points[me] + (0 if me == "paper" else 6)


def solve_1(path: str) -> int:
    data = read_data(path)

    _sum = 0
    for line in data:
        opponent, me = map_1[line[0]], map_1[line[1]]
        _sum += score(opponent, me)

    return _sum

    
def solve_2(path: str) -> int:
    data = read_data(path)

    _sum = 0
    for line in data:
        opponent = map_1[line[0]]
        me = map_2[line[0]][line[1]]
        _sum += score(opponent, me)

    return _sum


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")

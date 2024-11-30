
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines

def read_boards(path: str):
    with open(path, "r") as f:
        numbers = f.readline()
        numbers = list(map(int, numbers.split(",")))

        raw = f.read()
        raw = raw.split("\n\n")

        boards = [[row.replace("  ", " ") for row in board.split("\n") if row] for board in raw if board]

        for board in boards:
            for j, row in enumerate(board):
                row = row.strip().split(" ")
                row = list(map(int, row))
                board[j] = row

        return numbers, boards


def check_rows(board, numbers) -> bool:
    for row in board:
        if all(x in numbers for x in row):
            return True
    
    return False


def check_cols(board, numbers) -> bool:
    for i in range(len(board[0])):
        col = []
        for row in board:
            col.append(row[i])

        if all(x in numbers for x in col):
            return True
    return False



def solve_1(path: str) -> int:
    numbers, boards = read_boards(path)
    
    read_numbers = []

    while numbers:
        read_numbers.append(numbers.pop(0))

        for board in boards:
            if check_cols(board, read_numbers) or check_rows(board, read_numbers):
                _sum = 0
                for row in board:
                    for num in row:
                        if num not in read_numbers:
                            _sum += num
                return _sum * read_numbers[-1]

def solve_2(path: str) -> int:
    numbers, boards = read_boards(path)
    winning_boards = []

    boards = [{"board": board, "numbers": [], "winning": False} for board in boards]

    while numbers:
        num = numbers.pop(0)

        for obj in boards:
            if obj["winning"]:
                continue

            board = obj["board"]
            obj["numbers"].append(num)
            if check_cols(board, obj["numbers"]) or check_rows(board, obj["numbers"]):
                winning_boards.append(obj)
                obj["winning"] = True

    _sum = 0
    obj = winning_boards[-1]
    board = obj["board"]
    numbers = obj["numbers"]
    for row in board:
        for num in row:
            if num not in numbers:
                _sum += num

    return _sum * numbers[-1]


if __name__ == "__main__":
    path = "example.txt"
    ans_1 = solve_1(path)
    print(f"Example 1: {ans_1}")
    
    ans_2 = solve_2(path)
    print(f"Example 2: {ans_2}")

    print("\n---\n")

    path = "input.txt"
    ans_1 = solve_1(path)
    print(f"Problem 1: {ans_1}")
    
    ans_2 = solve_2(path)
    print(f"Problem 2: {ans_2}")

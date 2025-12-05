from pathlib import Path

from advent_of_code import utils
from aoc_2015_11 import DATA_PATH

MIN = ord("a")
MAX = ord("z")
ILLEGAL = {ord("i"), ord("o"), ord("l")}


def check_rules(password: list[int]) -> bool:
    # Check illegal
    for char in ILLEGAL:
        if char in password:
            return False

    # Check consecutive
    for x, y, z in utils.sliding_window(array=password, window_size=3, step=1):
        if x + 1 == y and y + 1 == z:
            break
    else:
        return False

    # Check equal
    equals = {}
    for x, y in utils.sliding_window(array=password, window_size=2, step=1):
        if x == y:
            equals[(x, y)] = True

        if len(equals) == 2:
            break
    else:
        return False

    return True


def rotate_password(password: list[int]) -> list[int]:
    password[-1] += 1
    password[-1] += password[-1] in ILLEGAL

    i = -1
    while password[i] > MAX:
        password[i] = MIN
        password[i - 1] += 1
        password[i - 1] += password[i - 1] in ILLEGAL

        i -= 1
    return password


def solve(password: list[int]) -> list[int]:
    while True:
        password = rotate_password(password)
        if check_rules(password):
            return password


def encode_password(password: str) -> list[int]:
    return list(map(ord, password))


def decode_password(password: list[int]) -> str:
    return "".join(map(chr, password))


def solve_1(path: Path):
    data = utils.read_data(path)
    password = encode_password(data)
    password = solve(password)

    return decode_password(password)


def solve_2(path: Path):
    data = utils.read_data(path)
    password = encode_password(data)
    password = solve(password)
    password = solve(password)

    return decode_password(password)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")

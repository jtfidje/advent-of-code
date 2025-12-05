# flake8: noqa: F401

from pathlib import Path

from advent_of_code import utils
from aoc_2015_11 import DATA_PATH

MIN = ord("a")
MAX = ord("z")
ILLEGAL = [ord("i"), ord("o"), ord("l")]


def check_rules(password: list[int]) -> bool:
    # Check consecutive
    for x, y, z in utils.sliding_window(array=password, window_size=3, step=1):
        if x + 1 == y and y + 1 == z:
            break
    else:
        return False

    # Check illegal
    for char in ILLEGAL:
        if char in password:
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
    i = -1
    while password[i] > MAX:
        password[i] = MIN
        password[i - 1] += 1
        i -= 1
    return password


def solve(path: str | Path):
    data = utils.read_data(path)
    password = list(map(ord, data))

    for _ in range(2):
        while True:
            password = rotate_password(password)
            if check_rules(password):
                break
    return "".join(map(chr, password))


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input_2.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")

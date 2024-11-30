# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def check_mirror(pattern):
    results = 0
    for i in range(len(pattern) - 1):
        j = i + 1

        horizontal_start = i
        is_mirror = False
        while True:
            if pattern[i] != pattern[j]:
                break

            i -= 1
            j += 1


            if i < 0 or j >= len(pattern):
                is_mirror = True
                break

        if is_mirror:
            results += horizontal_start + 1

    return results


def solve(path: str):
    patterns = utils.read_data(path).split("\n\n")
    patterns = list(map(lambda x: x.split(), patterns))

    horizontal_res = 0
    vertical_res = 0
    for pattern in patterns:
        horizontal_res += check_mirror(pattern)

        # check columns
        _pattern = []
        for i in range(len(pattern[0])):
            column = [row[i] for row in pattern]
            _pattern.append(column)

        vertical_res += check_mirror(_pattern)

    return vertical_res + (horizontal_res * 100)



if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
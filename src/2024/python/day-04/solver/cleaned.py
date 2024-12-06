import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def count_word(word: str, string: str) -> int:
    return len(re.findall(f"{word}|{word[::-1]}", string))


def solve_1(path: Path):
    data = utils.read_data(path)
    word_count = 0

    # Count words in rows
    word_count += count_word("XMAS", data)

    # Count words in cols
    word_count += count_word(
        "XMAS", "\n".join(utils.rotate_clockwise(data.split(), rotations=1))
    )

    return word_count


def solve_2(path: Path):
    data = utils.read_data(path)


if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")

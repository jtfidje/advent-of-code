# flake8: noqa: F401
import itertools
import re
from pathlib import Path

from advent_of_code import utils
from aoc_2025_10 import DATA_PATH


@utils.performance_timer
def solve(path: str | Path):
    data = utils.read_lines(path)

    result = 0
    for line in data:
        target, buttons, _ = re.findall(r"\[([\.#]+)\] (\(.*\)) (\{[\d,]+\})", line)[0]

        target = [c == "#" for c in target]
        buttons = list(map(utils.parse_integers, buttons.split(" ")))

        for i in range(1, len(buttons) + 1):
            for to_press in itertools.combinations(buttons, i):
                state = [False for _ in range(len(target))]
                for button in to_press:
                    for i in button:
                        state[i] = not state[i]

                if state == target:
                    result += len(to_press)
                    break
            else:
                continue

            break

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

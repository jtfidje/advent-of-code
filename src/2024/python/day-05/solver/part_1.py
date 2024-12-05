# flake8: noqa: F401

from collections import defaultdict
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    rules, updates = utils.read_data(path).split("\n\n")

    rules = rules.split()
    updates = updates.split()

    rule_map: dict[str, set[str]] = defaultdict(set)

    for rule in rules:
        a, b = rule.split("|")
        rule_map[a].add(b)

    total = 0
    for update in updates:
        numbers = update.split(",")

        seen = set()
        for num in numbers:
            rule = rule_map[num]

            if rule.intersection(seen):
                break

            seen.add(num)
        else:
            total += int(numbers[int(len(numbers) / 2)])

    return total


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

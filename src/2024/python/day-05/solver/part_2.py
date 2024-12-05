# flake8: noqa: F401
from collections import defaultdict
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def check_update(numbers: list[str], rule_map: dict[str, set[str]]) -> list[str]:
    seen = set()
    for i, num in enumerate(numbers):
        rule = rule_map[num]

        if rule.intersection(seen):
            if i == 0:
                raise Exception

            numbers = numbers[:]
            x = numbers.pop(i)
            numbers.insert(i - 1, x)

            return check_update(numbers, rule_map)

        seen.add(num)

    return numbers


def solve(path: str | Path):
    rules, updates = utils.read_data(path).split("\n\n")

    rules = rules.split()
    updates = updates.split()

    rule_map: dict[str, set[str]] = defaultdict(set)

    for rule in rules:
        a, b = rule.split("|")
        rule_map[a].add(b)

    incorrect_updates = []
    for update in updates:
        numbers = update.split(",")

        seen = set()
        for num in numbers:
            rule = rule_map[num]

            if rule.intersection(seen):
                incorrect_updates.append(numbers)
                break

            seen.add(num)

    total = 0
    for update in incorrect_updates:
        correct_update = check_update(update, rule_map)

        total += int(correct_update[int(len(correct_update) / 2)])

    return total


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")

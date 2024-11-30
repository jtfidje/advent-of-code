import re
import sys
from dataclasses import dataclass
from functools import reduce
from pathlib import Path

from solver import utils

sys.setrecursionlimit(1_000_000)

data_path = Path(__file__).parent.parent.absolute() / "data"


@dataclass
class Rule:
    key: str | None
    operand: str | None
    value: int | None
    result: str


def worker(key: str, ratings: dict[str, range], workflows: dict[str, list[Rule]]) -> int:
        if key == "A":
            return reduce(lambda x, y: x * y, ((r.stop - r.start) + 1 for r in ratings.values()))

        if key == "R":
            return 0
        
        results = 0
        for rule in workflows[key]:
            match rule.operand:
                case None:
                    results += worker(
                        key=rule.result,
                        ratings=ratings,
                        workflows=workflows
                    )
                    break

                case ">":
                    rating = ratings[rule.key]
                    if rating.stop <= rule.value:
                        continue

                    if rating.start <= rule.value:
                        results += worker(
                            key=rule.result,
                            ratings={**ratings, rule.key: range(rule.value + 1, rating.stop)},
                            workflows=workflows
                        )

                        results += worker(
                            key=key,
                            ratings={**ratings, rule.key: range(rating.start, rule.value)},
                            workflows=workflows
                        )
                        
                        break

                case "<":
                    rating = ratings[rule.key]
                    if rating.start >= rule.value:
                        continue

                    if rating.stop >= rule.value:
                        results += worker(
                            key=rule.result,
                            ratings={**ratings, rule.key: range(rating.start, rule.value - 1)},
                            workflows=workflows
                        )
                        
                        results += worker(
                            key=key,
                            ratings={**ratings, rule.key: range(rule.value, rating.stop)},
                            workflows=workflows
                        )

                        break

        return results

def solve(path: str):
    data = utils.read_data(path)
    workflow_data, _ = data.split("\n\n")

    workflows = {}
    for w_name, rule_string in re.findall(r"(\w+){(.*)}", workflow_data):
        rule_list = rule_string.split(",")
        rules = []
        for r in rule_list:
            match = re.match(r"([xmas])([<>])(\d+)\:([a-zAR]+)", r)
            if match is None:
                rule = Rule(key=None, operand=None, value=None, result=r)
            else:
                key, operand, value, result = match.groups()
                rule = Rule(key, operand, int(value), result)
            
            rules.append(rule)

        workflows[w_name] = rules

    return worker(
        "in", ratings={c: range(1, 4000) for c in "xmas"},
        workflows=workflows
    )


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    #answer = solve(Path(data_path, "example_2.txt"))

    if answer is not None:
        print(f"Problem 2: {answer}")
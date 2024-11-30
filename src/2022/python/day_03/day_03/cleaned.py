import string
from functools import reduce

def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


class Rucksack:
    @staticmethod
    def get_priority(item: str):
        return string.ascii_letters.index(item) + 1

    def __init__(self, items: str):
        num_items = len(items)

        self.compartments = {
            "1": items[:int(num_items / 2)],
            "2": items[int(num_items / 2):]
        }

    def unique_items(self):
        return set(self.compartments["1"]).union(self.compartments["2"])

    def get_score(self):
        score = 0
        
        for item in set(self.compartments["1"]).intersection(self.compartments["2"]):
            score += self.get_priority(item)

        return score


def solve_1(path: str):
    data = read_lines(path)
    
    total_score = 0
    for line in data:
        rucksack = Rucksack(line)
        total_score += rucksack.get_score()

    return total_score


def solve_2(path: str):
    data = read_lines(path)
    total_score = 0

    for i in range(0, len(data), 3):
        rucksacks = [Rucksack(items) for items in data[i: i + 3]]

        badge = reduce(lambda x, y: x.intersection(y), [rucksack.unique_items() for rucksack in rucksacks]).pop()
        total_score += Rucksack.get_priority(badge)

    return total_score


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")

import re
from pathlib import Path

from solver.utils import (
    read_lines,
)

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str):
    data = read_lines(path)

    game_cards = {}
    my_cards = {}

    for game_number, line in enumerate(data, start=1):
        line = line.split(": ")[1]
        line = re.sub("[ ]{2,}", " ", line)
        winning, numbers = line.split(" | ")
        winning = set(map(int, re.findall(r"\d+", winning)))
        numbers = set(map(int, re.findall(r"\d+", numbers)))

        game_cards[game_number] = (winning, numbers)
        my_cards[game_number] = 1
    
    total = len(game_cards)
    for game_number, num_games in my_cards.items():
        for _ in range(num_games):
            winning, numbers = game_cards[game_number]
            result = winning & numbers
            for i in range(game_number + 1, game_number + len(result) + 1):
                total += 1
                my_cards[i] += 1
    
    return total


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
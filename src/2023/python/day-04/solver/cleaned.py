from pathlib import Path

from solver.utils import read_lines

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve_1(path: str):
    data = read_lines(path)

    total = 0
    for line in data:
        line = line.split(": ")[1]
        winning, numbers = list(map(lambda x: set(x.split()), line.split(" | ")))
        
        if (num_winning := len(winning & numbers)) > 0:
            total += 2 ** (num_winning - 1)

    return total


def solve_2(path: str):
    data = read_lines(path)

    game_cards = {i: 1 for i in range(1, len(data) + 1)}
    for game_id, line in enumerate(data, start=1):
        line = line.split(": ")[1]
        winning, numbers = list(map(lambda x: set(x.split()), line.split(" | ")))

        for i in range(1, len(winning & numbers) + 1):
            game_cards[game_id + i] += game_cards[game_id]

    return sum(game_cards.values())



if __name__ == "__main__":
    answer = solve_1(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

    answer = solve_2(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
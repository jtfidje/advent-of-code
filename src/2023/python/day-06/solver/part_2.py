from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"



def solve(path: str):
    data = utils.read_lines(path)

    time = int("".join(data[0].split(": ")[1].split()))
    record = int("".join(data[1].split(": ")[1].split()))

    wins = 0
    for t in range(1, time):
        speed = t * 1
        distance = (time - t) * speed
        if distance > record:
            wins += 1
    return wins


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
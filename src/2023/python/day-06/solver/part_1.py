from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

def solve(path: str):
    data = utils.read_lines(path)

    acc = 1

    time_list = list(map(int, data[0].split(": ")[1].split()))
    distance_list = list(map(int, data[1].split(": ")[1].split()))

    total = 1
    for race, (time, record) in enumerate(zip(time_list, distance_list)):
        wins = 0
        for t in range(1, time):
            speed = t * acc
            distance = (time - t) * speed
            if distance > record:
                wins += 1
        total *= max(1, wins)

    return total

if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
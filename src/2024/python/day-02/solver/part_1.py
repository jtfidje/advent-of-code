# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    data = utils.read_lines(path)
    numbers_arr = []
    for line in data:
        numbers_arr.append(list(map(int, line.split(" "))))

    safe_count = 0
    for numbers in numbers_arr:
        is_safe = True
        method = "INC" if numbers[0] < numbers[1] else "DEC"
        for window in utils.sliding_window(array=numbers, window_size = 2, step=1):
            match method:
                case "INC":
                    if window[0] > window[1]:
                        break
                case "DEC":
                    if window[0] < window[1]:
                        break

            diff = abs(window[0] - window[1])
            if diff < 1 or diff > 3:
                break
        else:
            safe_count += 1
        
    return safe_count




if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")

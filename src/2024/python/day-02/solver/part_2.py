# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

def check_diff(a, b):
    diff = abs(a - b)
    return 1 <= diff <= 3

def solve(path: str | Path):
    data = utils.read_lines(path)
    numbers_arr = []
    for line in data:
        numbers_arr.append(list(map(int, line.split(" "))))

    safe_count = 0
    for numbers in numbers_arr:
        # Check increase
        has_skipped = False
        skip_index = None
        for i, (x, y, z) in enumerate(utils.sliding_window(numbers, 3, 1)):
            if x > y:
                if has_skipped:
                    break
                
                has_skipped = True
                skip_index = i + 1
                if x > z:
                    break

                if check_diff(x, z):
                    continue

            else:
                if not check_diff:
                    break

                continue
        else:
            is_safe = True

            if skip_index == len(numbers) - 2:
                ...

            else:
                x, y = numbers[-2:]
                
                if x > y:
                    if not check_diff(x, z):
                        is_safe = False

            safe_count += int(is_safe)
            continue

        # Check decrease
        has_skipped = False
        for x, y, z in utils.sliding_window(numbers[:-1], 3, 1):
            if x < y:
                if has_skipped:
                    break
                
                has_skipped = True
                if x < z:
                    break

                if check_diff(x, z):
                    continue

            else:
                if not check_diff(x, y):
                    break

                continue
        else:
            # Check last window
            safe_count += 1
            continue
        
    return safe_count
            







if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")

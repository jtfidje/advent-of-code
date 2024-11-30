# flake8: noqa: F401

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str):
    data = utils.read_lines(path)
    data = [list(map(int, line.split())) for line in data]
    

    result = 0
    for line in data:
        temp = [line.copy()]
        current = line.copy()
        while not all(_t == 0 for _t in temp[-1]):
            diffs = []
            for window in utils.sliding_window(array=current, window_size=2, step=1):
                x, y = window
                diffs.append(y - x)
            temp.append(diffs.copy())
            current = diffs.copy()
        
        for l_1, l_2 in utils.sliding_window(temp, window_size=2, step=1, reverse=True):
            x = l_1[-1]
            y = l_2[-1]
            l_1.append(x + y)
        z = temp[0][-1]

        result += z

    return result


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
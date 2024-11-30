# flake8: noqa: F401
from collections import defaultdict
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def compute_hash(char, current_value):
    _ascii = ord(char)
    
    current_value += _ascii
    current_value *= 17
    current_value %= 256

    return current_value


def solve(path: str):
    data = utils.read_data(path).split(",")

    results =0

    boxes = {i: {} for i in range(256)}

    for element in data:
        if "=" in element:
            str_label, focal_len = element.split("=")
            int_label = 0
            for char in str_label:
                int_label = compute_hash(char,int_label)
            
            box = boxes[int_label]

            box[str_label] = int(focal_len)


        else:
            str_label = element[:-1]
            int_label = 0
            for char in str_label:
                int_label = compute_hash(char, int_label)
            
            box = boxes[int_label]
            
            try:
                box.pop(str_label, None)
            except ValueError:
                continue


    for i, box in enumerate(boxes.values(), start=1):
        for j, lens in enumerate(box.values(), start=1):
            results += (i * j * lens)



    return results


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    if answer is not None:
        print(f"Problem 2: {answer}")
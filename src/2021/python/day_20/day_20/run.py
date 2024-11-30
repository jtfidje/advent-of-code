import numpy as np
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        algorithm = f.readline().strip()
        algorithm = algorithm.replace(".", "0").replace("#", "1")
        algorithm = list(map(int, algorithm))

        f.readline()
        image = f.read()
        image = image.replace(".", "0",).replace("#", "1")
        image = image.split("\n")
        image = np.array([list(line) for line in image if line], dtype=np.int8)
        return algorithm, image


def rolling_window(a, shape):
    s = (a.shape[0] - shape[0] + 1,) + (a.shape[1] - shape[1] + 1,) + shape
    strides = a.strides + a.strides
    return np.lib.stride_tricks.as_strided(a, shape=s, strides=strides)


def create_windows(arr, shape=(3, 3), pad_value=0):
    r_extra = np.floor(shape[0] / 2).astype(int)
    c_extra = np.floor(shape[1] / 2).astype(int)
    out = np.empty((arr.shape[0] + 2 * r_extra, arr.shape[1] + 2 * c_extra), dtype=np.int8)
    out[:] = pad_value
    out[r_extra:-r_extra, c_extra:-c_extra] = arr
    view = rolling_window(out, shape)
    return view


def enhance_image(image, algorithm, pad_value=0):
    image = np.pad(image, ((1, 1), (1, 1)), constant_values=[pad_value])
    windows = create_windows(image, shape=(3, 3), pad_value=pad_value)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = windows[i][j]
            window_str = "".join([str(x) for line in window for x in line])
            
            pixel_val = algorithm[int(window_str, 2)]
            image[i][j] = pixel_val
    return image


def solve_1(path: str):
    algorithm, image = read_lines(path)
    pad_value = 0
    for i in range(2):
        image = enhance_image(image, algorithm, pad_value=pad_value)
        pad_value = algorithm[int(str(pad_value) * 9, 2)]

    return np.count_nonzero(image == 1)


def solve_2(path: str):
    algorithm, image = read_lines(path)
    pad_value = 0
    for i in range(50):
        image = enhance_image(image, algorithm, pad_value=pad_value)
        pad_value = algorithm[int(str(pad_value) * 9, 2)]

    return np.count_nonzero(image == 1)


if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")

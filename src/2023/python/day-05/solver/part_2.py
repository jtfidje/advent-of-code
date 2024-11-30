import math
import re
from functools import cache
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


maps = []


def calculate(start, r, map_index):
    if map_index == len(maps):
        return start
    
    results = []
    while r > 0:
        for dest, source, _r in maps[map_index]:
            if (start < source and start + r <= source) or start >= source + _r:
                continue

            if start < source:
                temp_r = r - (source - start)
                results.append(calculate(start, temp_r, map_index=map_index))

                start = source
                r = temp_r

            new_start = dest + (start - source)
            new_r = (start + r) - (source + _r)
            if new_r <= 0:
                results.append(calculate(new_start, r, map_index + 1))
                r = 0
                break
            
            else:
                results.append(calculate(new_start, r - new_r, map_index + 1))
                start = start + (r - new_r)
                r = new_r
                break

        else:
            results.append(calculate(start, r, map_index + 1))
            break

    return min(results)


def solve(path: str):
    data = utils.read_data(path)
    data = re.sub(r"[\n]{2,}", "\n", data)
    seeds = list(map(int, re.search(r"seeds:\s((?:\d+\s)+)", data).groups()[0].split()))
    
    maps.append([list(map(int, line.split())) for line in re.search(r"seed-to-soil map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line])
    maps.append([list(map(int, line.split())) for line in re.search(r"soil-to-fertilizer map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line])
    maps.append([list(map(int, line.split())) for line in re.search(r"fertilizer-to-water map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line])
    maps.append([list(map(int, line.split())) for line in re.search(r"water-to-light map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line])
    maps.append([list(map(int, line.split())) for line in re.search(r"light-to-temperature map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line])
    maps.append([list(map(int, line.split())) for line in re.search(r"temperature-to-humidity map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line])
    maps.append([list(map(int, line.split())) for line in re.search(r"humidity-to-location map:\s((?:\d+\s*)+)", data).groups()[0].split("\n") if line])

    
    ranges = list(utils.sliding_window(array=seeds, window=2, step=2))
    best = math.inf
    for start, r in ranges:
        res = calculate(start, r, map_index=0)
        best = min(best, res)

    return best
                




if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
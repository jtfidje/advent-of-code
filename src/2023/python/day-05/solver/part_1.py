import math
import re

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str):
    data = utils.read_data(path)
    data = re.sub(r"[\n]{2,}", "\n", data)
    seeds = list(map(int, re.search(r"seeds:\s((?:\d+\s)+)", data).groups()[0].split()))
    maps = {
        "seed_to_soil": [list(map(int, line.split())) for line in re.search(r"seed-to-soil map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line],
        "soil_to_fertilizer": [list(map(int, line.split())) for line in re.search(r"soil-to-fertilizer map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line],
        "fertilizer_to_water": [list(map(int, line.split())) for line in re.search(r"fertilizer-to-water map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line],
        "water_to_light": [list(map(int, line.split())) for line in re.search(r"water-to-light map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line],
        "light_to_temp": [list(map(int, line.split())) for line in re.search(r"light-to-temperature map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line],
        "temp_to_humidity": [list(map(int, line.split())) for line in re.search(r"temperature-to-humidity map:\s((?:\d+\s)+)", data).groups()[0].split("\n") if line],
        "humidity_to_location": [list(map(int, line.split())) for line in re.search(r"humidity-to-location map:\s((?:\d+\s*)+)", data).groups()[0].split("\n") if line],
    }

    min_loc = math.inf
    # Find max seed
    for element in seeds:
        next_index = element
        for _map in maps.values():
            for (dest, start, r) in _map:
                _range = range(start, start + r)
                if next_index in _range:
                    _index = _range.index(next_index)
                    next_index = range(dest, dest + r)[_index]
                    break

        min_loc = min(min_loc, next_index)


    return min_loc



if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")
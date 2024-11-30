import itertools
import numpy as np
from collections import defaultdict
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        data = f.read()
        scanners = data.split("\n\n")
        scanners = [scanner.split("\n")[1:] for scanner in scanners]
        scanners = [[tuple(map(lambda x: int(x), point.split(","))) for point in scanner] for scanner in scanners]
        return scanners

class Beacon:
    def __init__(self, idx, relative_position):
        self.relative_position = np.array(relative_position)
        self._absolute_position = None

    @property
    def absolute_position(self):
        return self._absolute_position

    @absolute_position.setter
    def absolute_position(self, position):
        if self._absolute_position is None:
            self._absolute_position = position


class Scanner:
    def __init__(self, idx, scanner_report):
        self.idx = idx
        self.scanner_report = scanner_report
        self._absolute_position = None
        
        self.overlapping_scanners = []
        self.overlapping_beacons = defaultdict(list)

        self.beacons = [Beacon(idx, position) for idx, position in enumerate(scanner_report)]
        self.beacon_distance_vectors = {}
        self.create_beacon_map()


    @property
    def absolute_position(self):
        return self._absolute_position

    @absolute_position.setter
    def absolute_position(self, position):
        self._absolute_position = position
        for beacon in self.beacons:
            beacon.absolute_position = beacon.relative_position + position


    def create_beacon_map(self):
        for i in range(len(self.scanner_report) - 1):
            for j in range(i + 1, len(self.scanner_report)): 
                distance_vector = get_distance_vector(
                    self.beacons[i],
                    self.beacons[j]
                )

                self.beacon_distance_vectors[distance_vector] = (i, j)

    def __repr__(self):
        return f"Scanner {self.idx}"


def get_distance_vector(beacon_a, beacon_b):
    vector_a = np.array(beacon_a.relative_position)    
    vector_b = np.array(beacon_b.relative_position)
        
    vector = vector_a - vector_b
    return np.linalg.norm(vector)


def overlapping_beacons(scanner_a, scanner_b):
    beacons = set()
    overlap_a = defaultdict(lambda: defaultdict(int))
    overlab_b = defaultdict(lambda: defaultdict(int))
    for beacon_vector in scanner_b.beacon_distance_vectors:
        if beacon_vector in scanner_a.beacon_distance_vectors:
            a_beacons = list(scanner_a.beacon_distance_vectors[beacon_vector])
            b_beacons = list(scanner_b.beacon_distance_vectors[beacon_vector])
            
            for i, a_beacon in enumerate(a_beacons):
                for j, b_beacon in enumerate(b_beacons):
                    overlap_a[a_beacon][b_beacon] += 1
                    overlab_b[b_beacon][a_beacon] += 1

            beacons = beacons.union(b_beacons)

    if len(beacons) >= 12:
        # Update overlap_map
        for a, _overlap in overlap_a.items():
            b = max(_overlap, key=_overlap.get)
            scanner_a.overlapping_beacons[scanner_b.idx].append((a, b))
            scanner_b.overlapping_beacons[scanner_a.idx].append((b, a))

    return beacons


def find_scanner_position(scanner_a, scanner_b):
    def update_set(point_set, a, b):
        _set = set((
            a - b,
            a + b,
        ))
        return point_set.intersection(_set) if point_set else _set

    x_set, y_set, z_set = set(), set(), set()
    for a, b in scanner_a.overlapping_beacons[scanner_b.idx]:
        vector_a = scanner_a.beacons[a].absolute_position
        vector_b = scanner_b.beacons[b].relative_position

        x_set = update_set(x_set, vector_a[0], vector_b[0])
        y_set = update_set(y_set, vector_a[1], vector_b[1])
        z_set = update_set(z_set, vector_a[2], vector_b[2])
        
    return np.array(next(zip(x_set, y_set, z_set)))


def solve_1(path: str) -> int:
    scanner_reports = read_lines(path)

    # Init. scanners and choose Scanner 0 as our base
    scanners = [Scanner(idx, scanner_report) for idx, scanner_report in enumerate(scanner_reports)]
    scanners[0].absolute_position = np.array((0, 0, 0))

    # Find scanner pairs and overlapping beacons
    for idx, scanner_a in enumerate(scanners[:-1], start=1):
        for scanner_b in scanners[idx:]:
            beacons = overlapping_beacons(scanner_a, scanner_b)
            if len(beacons) == 12:
                scanner_a.overlapping_scanners.append(scanner_b)
                scanner_b.overlapping_scanners.append(scanner_a)
                continue

    # Loop through scanner pairs and calculate absolute scanner positions
    visited = []
    open_list = [scanners[0]]  # Start with Scanner 0
    while open_list:
        scanner_a = open_list.pop(0)
        if scanner_a in visited:
            continue

        visited.append(scanner_a)
        for scanner_b in scanner_a.overlapping_scanners:
            if scanner_b in visited:
                continue
            open_list.append(scanner_b)
            print(scanner_a, "-->", scanner_b)
            scanner_b_pos = find_scanner_position(scanner_a, scanner_b)
            scanner_b.absolute_position = scanner_b_pos + scanner_a.absolute_position

            breakpoint()

            print(scanner_b, "position:", scanner_b.absolute_position)


def solve_2(path: str) -> int:
    ...


if __name__ == "__main__":
    solve_1("input.txt")
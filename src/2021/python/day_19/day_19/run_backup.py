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
    def __init__(self, idx, pos):
        self.idx = idx
        self.relative_pos = pos
        self._true_pos = None
        self.distance_vectors = {}
        
    def add_distance_vector(self, beacon_idx, vector):
        self.distance_vectors[beacon_idx] = vector


    @property
    def true_position(self):
        return self._true_pos

    @true_position.setter
    def true_position(self, pos):
        if self._true_pos is None:
            self._true_pos = pos


class Scanner:
    def __init__(self, idx, scanner_report):
        self.scanner_report = scanner_report
        self.idx = idx
        self.overlapping_beacons = defaultdict(list)
        self.beacon_vectors = {}
        self.beacon_positions = {}
        self.position = None
        
        self.beacons = [Beacon(idx, pos) for idx, pos in enumerate(self.scanner_report)]

        self.create_beacon_map()

    def __repr__(self):
        return f"Scanner {self.idx}"

    def create_beacon_map(self):
        for i in range(len(self.scanner_report) - 1):
            for j in range(i + 1, len(self.scanner_report)):
                distance_vector = get_distance_vector(
                    self.scanner_report[i],
                    self.scanner_report[j]
                )

                self.beacons[i].add_distance_vector(j, distance_vector)
                self.beacons[j].add_distance_vector(i, distance_vector)
                self.beacon_vectors[distance_vector] = (i, j)


def get_distance_vector(beacon_a, beacon_b):
    if not isinstance(beacon_a, np.ndarray):
        beacon_a = np.array(beacon_a)
        
    if not isinstance(beacon_b, np.ndarray):
        beacon_b = np.array(beacon_b)
        
    vector = beacon_a - beacon_b
    return np.linalg.norm(vector)


def overlapping_beacons(scanner_a, scanner_b):
    beacons = set()
    overlap_a = defaultdict(lambda: defaultdict(int))
    overlab_b = defaultdict(lambda: defaultdict(int))
    for beacon_vector in scanner_b.beacon_vectors:
        if beacon_vector in scanner_a.beacon_vectors:
            a_beacons = list(scanner_a.beacon_vectors[beacon_vector])
            b_beacons = list(scanner_b.beacon_vectors[beacon_vector])
            
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
            b + a,
        ))
        return point_set.intersection(_set) if point_set else _set

    x_set, y_set, z_set = set(), set(), set()
    for a, b in scanner_a.overlapping_beacons[scanner_b.idx]:
        vector_a = scanner_a.scanner_report[a]
        vector_b = scanner_b.scanner_report[b]

        x_set = update_set(x_set, vector_a[0], vector_b[0])
        y_set = update_set(y_set, vector_a[1], vector_b[1])
        z_set = update_set(z_set, vector_a[2], vector_b[2])
        
    return list(next(zip(x_set, y_set, z_set)))


def solve_1(path: str):
    scanner_reports = read_lines(path)

    scanners = [Scanner(idx, scanner_report) for idx, scanner_report in enumerate(scanner_reports)]
    scanners[0].position = (0, 0, 0)

    scanner_pairs = []
    while scanners:
        scanner_a = scanners.pop(0)
        for scanner_b in scanners:
            beacons = overlapping_beacons(scanner_a, scanner_b)
            if len(beacons) >= 12:
                scanner_pairs.append((scanner_a, scanner_b))
                #break

    print(scanner_pairs)
    beacons = {}
    for (scanner_a, scanner_b) in scanner_pairs:
        print(scanner_a, "-->", scanner_b)
        scanner_b.position = find_scanner_position(scanner_a, scanner_b)
        print(scanner_b.position)
        break


    return 1


def solve_2(path: str):
    data = read_lines(path)
    ...


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

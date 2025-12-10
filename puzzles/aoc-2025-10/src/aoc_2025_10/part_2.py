# flake8: noqa: F401

import math
import re
from pathlib import Path
from typing import Self

import numpy as np

from advent_of_code import utils
from aoc_2025_10 import DATA_PATH


class Node:
    def __init__(self, press_id: int, state: np.ndarray, parent: None | Self = None):
        self.press_id = press_id
        self.state = state
        self.state_tuple: tuple[np.int64, ...] = tuple(state)
        self.parent = parent

    def get_state_path(self) -> list[tuple[int, tuple[np.int64, ...]]]:
        node = self
        states = [(node.press_id, node.state_tuple)]
        while node.parent:
            node = node.parent
            states.append((node.press_id, node.state_tuple))
        return states


@utils.performance_timer
def solve(path: str | Path):
    data = utils.read_lines(path)

    result = 0
    for line in data:
        _, buttons_data, joltage = re.findall(
            r"\[([\.#]+)\] (\(.*\)) (\{[\d,]+\})", line
        )[0]

        target = np.array(utils.parse_integers(joltage))
        buttons = []
        for idx in sorted(
            list(map(utils.parse_integers, buttons_data.split(" "))),
            reverse=False,
            key=lambda x: len(x),
        ):
            arr = np.zeros(shape=target.shape, dtype=np.int64)
            for i in idx:
                arr[i] += 1

            buttons.append(arr)

        best = math.inf
        visited: dict[tuple[np.int64, ...], int] = {}
        to_visit = [
            Node(press_id=0, state=np.zeros(shape=target.shape, dtype=np.int64))
        ]

        while to_visit:
            node = to_visit.pop(-1)

            if all(node.state == target):
                if node.press_id < best:
                    best = node.press_id
                    to_visit = [n for n in to_visit if n.press_id < best]
                    visited = {
                        state: press_id for press_id, state in node.get_state_path()
                    }

                continue

            new_nodes: list[Node] = []
            for button in buttons:
                new_state = node.state.copy()
                new_state += button

                if any(new_state == target):
                    continue

                new_node = Node(press_id=node.press_id + 1, state=new_state)

                if new_node.press_id >= best:
                    continue

                if new_node.state_tuple in visited:
                    if new_node.press_id >= visited[new_node.state_tuple]:
                        continue
                    else:
                        del visited[new_node.state_tuple]

                new_nodes.append(new_node)

            new_nodes.sort(key=lambda n: sum(target - n.state), reverse=True)
            to_visit.extend(new_nodes)
        result += best

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "example_1_1.txt")
    # answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")

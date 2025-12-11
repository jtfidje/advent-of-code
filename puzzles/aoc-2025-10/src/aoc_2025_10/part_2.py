# flake8: noqa: F401

import math
import re
from pathlib import Path
from typing import Self

from advent_of_code import utils
from aoc_2025_10 import DATA_PATH


class Node:
    def __init__(
        self, press_id: int, state: dict[int, int], parent: None | Self = None
    ):
        self.press_id = press_id
        self.state = state
        self.state_tuple = tuple(self.state[i] for i in range(len(self.state)))
        self.parent = parent

    def get_state_path(self) -> list[tuple[int, tuple[int, ...]]]:
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
        _, buttons, joltage = re.findall(r"\[([\.#]+)\] (\(.*\)) (\{[\d,]+\})", line)[0]

        target = {i: x for i, x in enumerate(utils.parse_integers(joltage))}
        buttons = sorted(
            list(map(utils.parse_integers, buttons.split(" "))),
            reverse=False,
            key=lambda x: len(x),
        )

        best = math.inf
        visited: dict[tuple[int, ...], int] = {}
        to_visit = [Node(press_id=0, state={key: 0 for key in target})]
        while to_visit:
            node = to_visit.pop(-1)

            if node.state == target:
                best = min(node.press_id, best)
                to_visit = [n for n in to_visit if n.press_id < best]
                for press_id, state in node.get_state_path():
                    visited[state] = press_id

                continue

            new_nodes: list[Node] = []
            for button in buttons:
                if any(node.state[i] == target[i] for i in button):
                    continue

                new_state = {key: value for key, value in node.state.items()}
                for i in button:
                    new_state[i] += 1

                new_node = Node(
                    press_id=node.press_id + 1, state=new_state, parent=node
                )

                if new_node.press_id >= best:
                    continue

                if new_node.state_tuple in visited:
                    if new_node.press_id >= visited[new_node.state_tuple]:
                        continue
                    else:
                        del visited[new_node.state_tuple]

                new_nodes.append(new_node)

            new_nodes.sort(
                key=lambda n: sum(target[i] - n.state[i] for i in target.keys()),
                reverse=True,
            )
            to_visit.extend(new_nodes)
        result += best

    return result


if __name__ == "__main__":
    # answer = solve(DATA_PATH / "example_1_1.txt")
    answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")

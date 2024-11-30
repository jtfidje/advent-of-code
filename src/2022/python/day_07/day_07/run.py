import json
from functools import reduce


class Node:
    def __init__(self, name, size, is_dir, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.is_dir = is_dir
        self.children: dict[str, "Node"] = {}

    def calculate_size(self):
        if self.size > 0:
            return self.size

        for child in self.children.values():
            if child.is_dir:
                size = child.calculate_size()
                self.size += size
            else:
                self.size += child.size
        return self.size

    def pwd(self):
        node = self
        pwd = [node.name]
        while node.parent:
            node = node.parent
            pwd.insert(0, node.name)

        res = "/".join(pwd)
        res = res.replace("//", "/")
        return res

    
def json_print(obj):
    print(json.dumps(obj, indent=4))


def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_numbers(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str):
    #data = read_lines(path)
    cwd = Node("/", size=0, is_dir=True)
    tree = {"/": cwd}
    
    with open(path) as f:
        f.readline()
        while (line := f.readline().strip()):
            if line.startswith("$ cd"):
                name = line.split()[-1]
                if name == "..":
                    cwd = cwd.parent
                else:
                    pwd = cwd.pwd() + "/" + line.split()[-1]
                    pwd = pwd.replace("//", "/")
                    cwd = tree.get(pwd)

            elif line.startswith("$ ls"):
                ...

            elif line.startswith("dir"):
                name = line.split()[-1]
                node = Node(name, size=0, is_dir=True, parent=cwd)
                tree[node.pwd()] = node
                cwd.children[node.pwd()] = node

            else:
                size, name = line.split()
                node = Node(name, size=int(size), is_dir=False, parent=cwd)
                tree[node.pwd()] = node
                cwd.children[node.pwd()] = node
    
    tree["/"].calculate_size()
    total = 0
    for node in tree.values():
        if node.is_dir and node.size <= 100000:
            total += node.size
    return total

    
                
def solve_2(path: str):
    cwd = Node("/", size=0, is_dir=True)
    tree = {"/": cwd}
    
    with open(path) as f:
        f.readline()
        while (line := f.readline().strip()):
            if line.startswith("$ cd"):
                name = line.split()[-1]
                if name == "..":
                    cwd = cwd.parent
                else:
                    pwd = cwd.pwd() + "/" + line.split()[-1]
                    pwd = pwd.replace("//", "/")
                    cwd = tree.get(pwd)

            elif line.startswith("$ ls"):
                ...

            elif line.startswith("dir"):
                name = line.split()[-1]
                node = Node(name, size=0, is_dir=True, parent=cwd)
                tree[node.pwd()] = node
                cwd.children[node.pwd()] = node

            else:
                size, name = line.split()
                node = Node(name, size=int(size), is_dir=False, parent=cwd)
                tree[node.pwd()] = node
                cwd.children[node.pwd()] = node
    tree["/"].calculate_size()
    sizes = [node.size for node in tree.values() if node.is_dir]
    sizes.sort()
    
    free_space = 70000000 - tree["/"].size
    for size in sizes:
        if free_space + size >= 30000000:
            return size


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")

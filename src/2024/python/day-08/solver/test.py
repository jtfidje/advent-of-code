from pprint import pprint

from solver import utils

i = 4
matrix = []
for x in range(i):
    row = []
    for y in range(1 + (x * i), (i * x) + i + 1):
        row.append(y)

    matrix.append(row)

for line in matrix:
    print(" ".join(map(lambda x: str(x).zfill(2), line)))
print()

utils.rotate_45(matrix, 1, 1)

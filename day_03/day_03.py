from pathlib import Path
from functools import reduce

def find(lines, right, down):
    line_idx = 0
    char_idx = 0
    num_trees = 0
    while True:
        char_idx += right
        line_idx += down
        if line_idx >= len(lines):
            break
        line = lines[line_idx]
        i = char_idx % len(line)
        num_trees += line[i] == '#'
    return num_trees

lines = Path('input.txt').read_text().splitlines()
# count = 0
# for i, line in enumerate(lines[1:], start=1):
#     index = (3 * i) % len(line)
#     count += line[index] == '#'

assert find(lines, 3, 1) == 198

inputs = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)
trees = (find(lines, right, down) for (right, down) in inputs)
print(reduce(lambda x, y: x * y, trees))

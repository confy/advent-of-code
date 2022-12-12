import numpy as np
with open("./2022/12/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
from operator import itemgetter

grid = {}
queue = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            grid[(x, y)] = ["a", None]
            queue.append([(x, y), 0])
        elif char == "E":
            grid[(x, y)] = ["z", None]
            target = (x, y)
        else:
            grid[(x, y)] = [char, None]

grid[queue[0][0]][1] = 0  # steps to reach cell


def near(pos):
    return {(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)}


def search():
    while True:
        queue.sort(key=itemgetter(1))
        cell = queue.pop(0)
        for i in near(cell[0]):
            if i in grid and grid[i][1] is None and ord(grid[i][0]) - 1 <= ord(grid[cell[0]][0]):
                if i == target:
                    return cell[1]+1
                grid[i][1] = cell[1]+1
                queue.append([i, cell[1]+1])


print(search())

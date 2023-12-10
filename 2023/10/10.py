from collections import defaultdict

with open("./2023/10/input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]

smol = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

smol_2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

# grid = [list(line) for line in smol.splitlines()]
# grid = [list(line) for line in smol_2.splitlines()]


def find_start(grid: list) -> tuple:
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "S":
                return x, y


def find_connections(grid: list) -> dict:
    connections = defaultdict(list)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            cell = grid[x][y]
            if cell in "|LJ":
                connections[x, y].append((x - 1, y))
            if cell in "-J7":
                connections[x, y].append((x, y - 1))
            if cell in "|7F":
                connections[x, y].append((x + 1, y))
            if cell in "-LF":
                connections[x, y].append((x, y + 1))
    return connections


start = find_start(grid)
connections = find_connections(grid)

for n, m in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
    if start in connections[start[0] + n, start[1] + m]:
        connections[start].append((start[0] + n, start[1] + m))

this_cell = start
last_cell = -1, -1
size = 0
points = []

while True:
    next_cell = (
        connections[this_cell][1]
        if connections[this_cell][0] == last_cell
        else connections[this_cell][0]
    )
    last_cell = this_cell
    this_cell = next_cell
    points.append(this_cell)

    size += 1
    if this_cell == start:
        break

print(f"Part 1: {size/2:.0f}")

M = {
    "|": "010010010",
    "-": "000111000",
    "L": "010011000",
    "J": "010110000",
    "7": "000110010",
    "F": "000011010",
    ".": "000000000",
}

M["S"] = M["J"]  # TODO Manual hack - find the S tile type without this


def create_area_map(grid, points):
    area_map = []
    for x in range(len(grid)):
        area_map.extend(([], [], []))
        for y in range(len(grid[x])):
            v = [int(x) for x in M[grid[x][y] if (x, y) in points else "."]]
            area_map[-3].extend(v[:3])
            area_map[-2].extend(v[3:6])
            area_map[-1].extend(v[6:])
    return area_map


area_map = create_area_map(grid, points)
visited = set()
queue = [(1, 1)]
area = set()

while queue:
    x, y = queue.pop()
    if (x, y) in visited:
        continue
    visited.add((x, y))
    area_point = (x // 3, y // 3)
    if area_point not in points:
        area.add(area_point)
    for n, m in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        new_x, new_y = x + n, y + m
        if (
            0 <= new_x < len(area_map)
            and 0 <= new_y < len(area_map[0])
            and (new_x, new_y) not in visited
            and not area_map[new_x][new_y]
        ):
            queue.append((new_x, new_y))

area_size = len(grid) * len(grid[0]) - len(points) - len(area)
print(f"Part 2: {area_size}")

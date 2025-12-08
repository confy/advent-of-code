import functools

smol = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

with open("./2025/04/input.txt", "r") as f:
    data = [s.strip() for s in f.readlines()]

# data = smol.split("\n")

grid = [list(row) for row in data]

# print(grid)


@functools.lru_cache(maxsize=None)
def get_adjacent_rolls(x, y):
    rolls = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            rolls.append((nx, ny))
    return rolls

p1 = p2 = 0
changed_last_iteration = True

while changed_last_iteration:
    changed_last_iteration = False
    removed_this_iteration = 0
    new_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            rolls = get_adjacent_rolls(i, j)
            roll_count = sum(1 for x, y in rolls if grid[x][y] == '@')
            # print(f"Cell ({i}, {j}) has {roll_count} adjacent rolls.")
            if grid[i][j] == '@' and roll_count < 4:
                new_grid[i][j] = '.'
                changed_last_iteration = True
                removed_this_iteration += 1
    # print(f"Removed {removed_this_iteration} rolls this iteration.")
    grid = new_grid

    if p1 == 0:
        p1 += removed_this_iteration
    p2 += removed_this_iteration

print("Part 1:", p1)
print("Part 2:", p2)

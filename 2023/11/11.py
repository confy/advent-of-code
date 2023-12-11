from itertools import combinations

with open("./2023/11/input.txt") as f:
    grid = [list(line) for line in f.read().split("\n")]


smol = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

# grid = smol.splitlines()


def solve(grid: list[list], expansion: int) -> int:
    cols_to_expand = {
        col
        for col in range(len(grid[0]))
        if all(grid[row][col] == "." for row in range(len(grid)))
    }
    galaxies = []
    row_offset = 0
    for row, line in enumerate(grid):
        if all(char == "." for char in line):
            row_offset += expansion
            continue
        col_offset = 0
        for col, char in enumerate(line):
            if col in cols_to_expand:
                col_offset += expansion
                continue
            if char == "#":
                galaxies.append((row + row_offset, col + col_offset))
    return sum(
        abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
        for galaxy1, galaxy2 in combinations(galaxies, r=2)
    )


print(f"Part 1: {solve(grid, 1)}")
print(f"Part 2: {solve(grid, 999_999)}")

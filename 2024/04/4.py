smol = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
with open("input.txt") as f:
    input_text = f.read()
    
# input_text = smol

grid = [list(row) for row in input_text.split("\n")]

def xmas_search(directions, grid, x, y):
    xmas_count = 0
    xmas = "XMAS"

    for x_dir, y_dir in directions:
        for i in range(4):
            new_x = x + i * x_dir
            new_y = y + i * y_dir
            if (not (0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid))) or grid[new_y][new_x] != xmas[i]:
                break
            if i == 3:
                xmas_count += 1
    return xmas_count


def part1(grid):
    total_xmas = 0
    movements = [-1, 0, 1]
    directions = [(x, y) for x in movements for y in movements if x != 0 or y != 0]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "X":
                xmas_count = xmas_search(directions, grid, x, y)
                total_xmas += xmas_count
    return total_xmas

def x_mas_search(grid, x, y): 
    if (x+1 >= len(grid[0]) or x-1 < 0 or 
        y+1 >= len(grid) or y-1 < 0):
        return False
    
    patterns = [
        (grid[y+1][x-1], grid[y-1][x+1]),
        (grid[y+1][x+1], grid[y-1][x-1])
    ]
    
    return sum(1 for p in patterns if set(p) == {'M', 'S'}) == 2

def part2(grid):
    total_xmas = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "A":
                if x_mas_search(grid, x, y):
                    total_xmas += 1
    return total_xmas


print(part1(grid))
print(part2(grid))


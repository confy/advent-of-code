from collections import deque
with open("./2022/12/input.txt") as f:
    data = f.read().splitlines()

grid = {}
queue = deque()
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == "S":
            grid[(x, y)] = ["a", None]
            # queue.append([(x, y), 0]) # part 1
        elif char == "E":
            grid[(x, y)] = ["z", None]
            # target = (x,y) # part 1
            queue.append([(x, y), 0])  # part 2
        else:
            grid[(x, y)] = [char, None]

grid[queue[0][0]][1] = 0  # steps to reach cell


def near(pos):
    return {(pos[0] + 1, pos[1]), (pos[0], pos[1] + 1), (pos[0] - 1, pos[1]), (pos[0], pos[1] - 1)}


def search(grid, queue):
    while True:
        cell = queue.popleft()
        for i in near(cell[0]):
          # if i in grid and grid[i][1] == None and ord(grid[i][0])-1 <= ord(grid[cell[0]][0]): # part 1
            #   if i == target: return cell[1]+1
            if i in grid and grid[i][1] is None and ord(grid[i][0]) >= ord(grid[cell[0]][0]) - 1:
                if grid[i][0] == "a":
                    return cell[1]+1
                grid[i][1] = cell[1]+1
                queue.append([i, cell[1]+1])


print(search(grid, queue))

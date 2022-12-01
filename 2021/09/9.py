def read_input(filename):
    with open(filename) as f:
        return f.read().split()


def get_adj(x, y, grid):
    adj_idxs = []
    if x > 0:
        adj_idxs.append((x-1, y))
    if x < len(grid[0])-1:
        adj_idxs.append((x+1, y))
    if y > 0:
        adj_idxs.append((x, y-1))
    if y < len(grid)-1:
        adj_idxs.append((x, y+1))
    return adj_idxs


if __name__ == '__main__':
    # just part 1 :sadge:
    lines = read_input('./09/input.txt')
    risk_vals = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            adj_nodes = get_adj(x, y, lines)
            low_point = all(int(char) < int(
                lines[node[1]][node[0]]) for node in adj_nodes)
            if low_point:
                risk_vals += int(char) + 1
    print(risk_vals)

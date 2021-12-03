def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def part_1(instructions):
    dist = 0
    depth = 0
    for line in instructions:
        if "forward" in line:
            dist += int(line[-1])
        elif "up" in line:
            depth -= int(line[-1])
        elif "down" in line:
            depth += int(line[-1])
    return dist, depth

def part_2(instructions):
    dist = 0
    depth = 0
    aim = 0
    for line in instructions:
        if "down" in line:
            aim += int(line[-1])
        elif "up" in line:
            aim -= int(line[-1])
        elif "forward" in line:
            dist += int(line[-1])
            if aim != 0:
                depth += int(line[-1]) * aim
    return dist, depth


if __name__ == '__main__':
    filename = './02/input.txt'
    instructions = read_input(filename)
    dist, depth = part_1(instructions)
    print(f"Part 1 - Distance={dist} Depth={depth} Multiplied={dist * depth}")
    dist, depth = part_2(instructions)
    print(f"Part 2 - Distance={dist} Depth={depth} Multiplied={dist * depth}")


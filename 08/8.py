from collections import Counter

def read_input(filename):
    with open(filename, 'r') as f:
        return [x.strip().split("|") for x in f.readlines()]
        
if __name__ == '__main__':
    data = read_input('./08/input.txt')
    best_map = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
    best_mapping = Counter(best_map)
    map_key = {
        sum([*map(best_mapping.get, nums)]): i
        for i, nums in zip(range(10), best_map.split())
    }
    part1 = 0
    part2 = 0
    for front, back in data:
        part1 += len([x for x in back.split() if len(x) in (2, 3, 4, 7)])
        _map = Counter(front)
        part2 += int("".join([str(map_key[sum([*map(_map.get, nums)])]) for nums in back.split()]))
    print(part1, part2)
def read_input(filename):
    with open(filename, 'r') as f:
        nums = f.readline().strip().split(',')
    return [int(n) for n in nums]


def part_1_naive():
    """ bad for 256 iterations :)"""
    nums = read_input("./06/input.txt")
    for i in range(80):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 6
                nums.append(8)
            else:
                nums[i] -= 1
    print(f"Part 1: {len(nums)}")


def read_input_to_dict(filename):
    with open(filename, 'r') as f:
        nums = f.readline().strip().split(',')
    nums = [int(n) for n in nums]
    return {i: nums.count(i) for i in range(9)}


def tick(fish):
    tadpoles = fish[0]
    for i in range(8):
        fish[i] = fish[i + 1] if i != 6 else fish[i+1] + tadpoles
    fish[8] = tadpoles
    return fish


def fishies(fish):
    for i in range(256):
        fish = tick(fish)
    print(f"Part 2: {sum(fish.values())}")


if __name__ == '__main__':
    part_1_naive()
    fish = read_input_to_dict('./06/input.txt')
    fishies(fish)

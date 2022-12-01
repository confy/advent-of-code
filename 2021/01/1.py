def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return [int(line) for line in lines]
    
    
def part_1(nums):
    increased_count = 0
    last_num = nums[0]
    curr_num = nums[1]
    for i in range(len(nums)):
        if curr_num > last_num:
            increased_count += 1
        last_num = curr_num
        curr_num = nums[i]
    print(increased_count)
    
    
def part_2(nums):
    increased_count = 0
    curr_sum = 0
    last_sum = 0
    for i in range(len(nums)-2):
        curr_sum = sum(nums[i:i+3])
        if curr_sum > last_sum and last_sum != 0:
            increased_count += 1
        last_sum = curr_sum
    print(increased_count)

if __name__ == '__main__':
    filename = './01/input.txt'
    nums = read_input(filename)
    part_1(nums)
    part_2(nums)
        

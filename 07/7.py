def read_input(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.read().strip().split(',')]


if __name__ == '__main__':
    nums = read_input('./07/input.txt')

    # part 1
    sums = []
    for num in nums:
        c = sum(abs(n - num) for n in nums)
        sums.append(c)
    print(min(sums))

    # part 2 pssshhh off by one errors lol
    sums = []
    for i in range(max(nums) + 1):
        c = 0
        for j in nums:
            dist = abs(i - j)
            c += dist * (dist + 1) // 2
        sums.append(c)
    print(min(sums))

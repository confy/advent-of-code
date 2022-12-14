from itertools import zip_longest


def compare_pairs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right
    elif isinstance(left, list) and isinstance(right, list):
        for left_elem, right_elem in zip_longest(left, right):
            if left_elem is None:
                return True
            if right_elem is None:
                return False
            result = compare_pairs(left_elem, right_elem)
            if result is not None:
                return result
        return None

    elif isinstance(left, int):
        return compare_pairs([left], right)
    elif isinstance(right, int):
        return compare_pairs(left, [right])
    else:
        return None


def bubble_sort(packets):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(packets) - 1):
            if not compare_pairs(packets[i], packets[i + 1]):
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                swapped = True
    return packets


# with open("./2022/13/smol.txt") as f:
#     data = f.read().splitlines()
with open("./2022/13/input.txt") as f:
    data = f.read().splitlines()


packets = [eval(line) for line in data if line.startswith("[")]
packets.extend([[[2]], [[6]]])  # divider packets
sorted_packets = bubble_sort(packets)
ret = 1
for i, packet in enumerate(sorted_packets):
    if packet in [[[2]], [[6]]]:
        ret *= i+1
    print(packet)
print(ret)

from itertools import zip_longest

def compare_pairs(left, right):
    # If both values are integers, compare them directly
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right

    elif isinstance(left, list) and isinstance(right, list):
        for left_elem, right_elem in zip_longest(left, right):
            # zip_longest will return None for missing elements
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
    
    
    
# [1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]


with open("./2022/13/smol.txt") as f:
    data = f.read().splitlines()
    
# with open("./2022/13/input.txt") as f:
#     data = f.read().splitlines()
    
packet_pairs = []
first = None
for line in data:
    if not line.startswith("["):
        continue
    if first is not None:
        packet_pairs.append((first,eval(line)))
        first = None
    else: 
        first = eval(line)
        
print(packet_pairs)


correct_pair_idxs = []
for i, pair in enumerate(packet_pairs):
    print(pair)
    result = compare_pairs(*pair)
    print(result)
    if result == True:
        correct_pair_idxs.append(i+1)
    
print(sum(correct_pair_idxs))


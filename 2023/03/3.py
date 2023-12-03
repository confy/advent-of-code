import re

with open('./2023/03/input.txt') as f:
    lines = [l.strip() for l in f.readlines()]


symbols_with_indices = []
numbers_with_indices = []

for line in lines:
    numbers = [
        {'n': match.group(1), 'start': match.start()-1, 'end': match.end()}
        for match in re.finditer(r'(\d+)', line)
    ]
    symbols = [
        {'symbol': match.group(1), 'i': match.start()} 
        for match in re.finditer(r'([^.\d])', line)
    ]
    numbers_with_indices.append(numbers)
    symbols_with_indices.append(symbols)


def get_lines(lines, i):
    return lines[i] + (lines[i-1] if i > 0 else []) + (lines[i+1] if i < len(lines) - 1 else [])


p1 = []
for i, numbers in enumerate(numbers_with_indices):
    symbols = get_lines(symbols_with_indices, i)
    for num in numbers:
        for symbol in symbols:
            if num['start'] <= symbol['i'] <= num['end']:
                p1.append(int(num['n']))

print(sum(p1))


p2 = []
for i, symbols in enumerate(symbols_with_indices):
    numbers = get_lines(numbers_with_indices, i)
    for symbol in symbols:
        adjacents = []
        if symbol['symbol'] != '*':
            continue
        for num in numbers:
            if num['start'] <= symbol['i'] <= num['end']:
                adjacents.append(int(num['n']))
        
        if len(adjacents) == 2:
            p2.append(adjacents[0] * adjacents[1])

print(sum(p2))
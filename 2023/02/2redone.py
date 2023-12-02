import re
with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def max_color(line, color):
    return max(int(match.group(1)) for match in re.finditer(r'(\d+) ' + color, line))

p1 = []
p2 = []

for i, line in enumerate(lines):
    red_max = max_color(line, 'red')
    green_max = max_color(line, 'green')
    blue_max = max_color(line, 'blue')
    p2.append(red_max * green_max * blue_max)
    if not(red_max > 12 or green_max > 13 or blue_max > 14):
        p1.append(i+1)

print(sum(p1), sum(p2))
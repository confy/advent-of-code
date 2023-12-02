import re
with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

# Part 1
good_games = []
for line in lines:
    game_num = re.search(r'Game (\d+)', line).group(1)
    if max([int(match.group(1)) for match in re.finditer(r'(\d+) red', line)]) > 12 \
    or max([int(match.group(1)) for match in re.finditer(r'(\d+) green', line)]) > 13 \
    or max([int(match.group(1)) for match in re.finditer(r'(\d+) blue', line)]) > 14:
        continue
    good_games.append(int(game_num))

print(sum(good_games))

# Part 2
powers = []
for line in lines:
    red_max = max([int(match.group(1)) for match in re.finditer(r'(\d+) red', line)])
    green_max = max([int(match.group(1)) for match in re.finditer(r'(\d+) green', line)])
    blue_max = max([int(match.group(1)) for match in re.finditer(r'(\d+) blue', line)])
    powers.append(red_max * green_max * blue_max)

print(sum(powers))

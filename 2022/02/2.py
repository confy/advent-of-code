with open('./2022/02/input.txt') as f:
        games = [line.strip().split() for line in f.readlines()]
score = {
    'X': 1,   # rock
    'Y': 2,   # paper
    'Z': 3    # scissors
}
my_codes = {
    'A': ['Y', 'X', 'Z'],
    'B': ['Z', 'Y', 'X'],
    'C': ['X', 'Z', 'Y']
}
WIN = 6
DRAW = 3
LOSE = 0
scores = [WIN, DRAW, LOSE]
game_codes = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}
part_1 = 0
part_2 = 0
for opp_code, my_code in games:
    part_1 += score[my_code] + scores[my_codes[opp_code].index(my_code)]
    part_2 += game_codes[my_code] + score[my_codes[opp_code][scores.index(game_codes[my_code])]]
print(part_1, part_2)
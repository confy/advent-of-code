with open("./2023/04/input.txt") as file:
    games = file.read().strip().split("\n")

smol = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# games = smol.split("\n")

scores = []
row = 0
part2 = True

""" Very slow, but it works! """
while row < len(games):
    card, rest = games[row].strip().split(': ')
    card = card[5:]
    split = rest.split(" | ")
    win = {int(n) for n in split[0].split(" ") if n != ""}
    game = {int(n) for n in split[1].split(" ") if n != ""}
    matches = len(win.intersection(game))
    score = 0
    row += 1
    if matches > 0:
        score = 1
        for i in range(matches-1):
            score *= 2
        scores.append(score)
    if part2:
        for i in range(matches):
            card = int(card)
            games.append(games[card+i])

print(sum(scores), len(games))

with open('./2023/06/input.txt')as f:
    lines = [line.strip() for line in f.readlines()]

smol = """Time:      7  15   30
Distance:  9  40  200"""

# lines = smol.split('\n')

times = [int(x) for x in lines[0].split(':')[1].split()]
dists = [int(x) for x in lines[1].split(':')[1].split()]

time_p2 = int("".join(str(x) for x in times))
dist_p2 = int("".join(str(x) for x in dists))

races = list(zip(times, dists))
race_p2 = (time_p2, dist_p2)


def run_test_race(race_time: int, hold_time: int):
    boat_speed = hold_time
    race_time -= hold_time
    return boat_speed*race_time


def get_possible_wins(race: tuple):
    wins = 0
    for hold_time in range(1, race[0]):
        dist = run_test_race(race[0], hold_time)
        if dist > race[1]:
            wins += 1
    return wins


# part 1
p1 = 1
for race in races:
    wins = get_possible_wins(race)
    p1 *= wins
print(p1)

# part 2
# brute force... :shrug:
print(get_possible_wins(race_p2))

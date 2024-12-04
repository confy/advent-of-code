with open("./2023/12/input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

from itertools import combinations

smol = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

# lines = smol.split("\n")
CACHE = {}

def calc_clue(spring, groups, current_run):
    key = (spring, tuple(groups), current_run)
    if key in CACHE:
        return CACHE[key]

    ret = 0
    if spring == ".":
        if len(groups) == 0 and current_run == 0:
            ret += 1

    elif spring[0] == "?":
        if current_run == 0 or len(groups) > 0 and groups[0] == current_run:
            ret += calc_clue(f".{spring[1:]}", groups, current_run)
        if len(groups) > 0:
            ret += calc_clue(f"#{spring[1:]}", groups, current_run)

    elif spring[0] == "#":
        if len(groups) != 0:
            if groups[0] == current_run + 1:
                if spring[1] == ".":
                    ret += calc_clue(spring[1:], groups[1:], 0)
                elif spring[1] == "?":
                    ret += calc_clue(f".{spring[2:]}", groups[1:], 0)
            elif current_run < groups[0] and spring[1] == "#":
                ret += calc_clue(spring[1:], groups, current_run + 1)
            elif current_run < groups[0] and spring[1] == "?":
                ret += calc_clue(f"#{spring[2:]}", groups, current_run + 1)

    elif spring[0] == ".":
        if current_run == 0:
            ret += calc_clue(spring[1:], groups, 0)

    CACHE[key] = ret
    return ret


def solve(lines, part2=True):
    ret = 0
    for row in lines:
        spring, groups = row.split(" ")
        if part2:
            spring = "?".join([spring] * 5)
            groups = ",".join([groups] * 5)
        groups = [int(x) for x in groups.split(",")]
        spring += "."
        ret += calc_clue(spring, groups, 0)

    return ret


print(solve(lines, part2=False))
print(solve(lines, part2=True))

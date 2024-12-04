smol = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
with open('input.txt') as f:
    lines = [[int(n) for n in l.split(" ")] for l in f.readlines()]

# lines = smol.strip().split("\n")
# lines = [[int(n) for n in l.split(" ")] for l in lines]

def check_report(report):
    for i in range(1, len(report)):
        if abs(report[i] - report[i - 1]) > 3:
            return False
        if report[i] == report[i - 1]:
            return False
    return report in [sorted(report), sorted(report, reverse=True)]

def check_with_dampener(report):
    for i in range(len(report)):
        new_report = report.copy()
        del new_report[i]
        if check_report(new_report):
            return True
    return False

p1 = 0
p2 = 0
for report in lines:
    if check_report(report):
        p1 += 1
        p2 += 1
    elif check_with_dampener(report):
        p2 += 1

print(p1, p2)
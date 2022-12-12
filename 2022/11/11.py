

with open("./2022/11/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


# input.txt contains the following type of data in lines

# Monkey 3:
#   Starting items: 69, 82, 69, 56, 68
#   Operation: new = old + 5
#   Test: divisible by 2
#     If true: throw to monkey 0
#     If false: throw to monkey 2


# parse the data into a list of dictionaries


#
monkeys = []
last_id = 0
for line in lines:
    if line.startswith("Monkey"):
        m = {"id": int(line[7]), "items": [], "op": "", "op_sign": "",
             "inspections": 0, "test": 0, "if_true": 0, "if_false": 0}

    elif line.startswith("Starting items"):
        m["items"] = [int(i) for i in line[15:].split(", ")]
    elif line.startswith("Operation"):
        m["op"] = int(line[23:]) if line[23:].isdigit() else line[23:]
        if "new = old + " in line:
            m["op_sign"] = "+"
        elif "new = old * " in line:
            m["op_sign"] = "*"
    elif line.startswith("Test"):
        m["test"] = int(line[-1])
    elif line.startswith("If true"):
        m["if_true"] = int(line[-1])
    elif line.startswith("If false"):
        m["if_false"] = int(line[-1])
        monkeys.append(m)

# Each monkey has several attributes:

# Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.
# Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
# Test shows how the monkey uses your worry level to decide where to throw an item next.
# If true shows what happens with an item if the Test was true.
# If false shows what happens with an item if the Test was false.
# After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

# The monkeys take turns inspecting and throwing items. On a single monkey's turn, it inspects and throws all of the items it is holding one at a time and in the order listed. Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn. The process of each monkey taking a single turn is called a round.

# When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. A monkey that starts a round with no items could end up inspecting and throwing many items by the time its turn comes around. If a monkey is holding no items at the start of its turn, its turn ends.


# Iterate through the monkeys and perform the operations on their items


for r in range(20):
    # use the modulo operator to get the index of the monkey for this round
    monkey_index = r % len(monkeys)
    monkey = monkeys[monkey_index]

    for item in sorted(monkey["items"], reverse=True):
        if monkey["op_sign"] == "+":
            new_item = item + item if monkey["op"] == "old" else item + monkey["op"]
        elif monkey["op_sign"] == "*":
            new_item = item * item if monkey["op"] == "old" else item * monkey["op"]
        new_item = new_item // 3
        monkey["items"].remove(item)
        monkey["items"].append(new_item)

        # increment the counter for this monkey
        monkey["inspections"] += 1

        # test the item
        print(new_item, monkey["test"])
        if new_item % monkey["test"] == 0:
            # if true, throw to monkey if_true
            monkeys[monkey["if_true"]]["items"].append(new_item)

        else:
            # if false, throw to monkey if_false
            monkeys[monkey["if_false"]]["items"].append(new_item)
# sort the monkeys by the number of inspections
monkeys.sort(key=lambda x: x["inspections"], reverse=True)

# multiply together the number of inspections for the first two monkeys
monkey_business = monkeys[0]["inspections"] * monkeys[1]["inspections"]

print(monkey_business)

with open("./2022/10/input.txt") as input_file:
    operations = [line.strip() for line in input_file.readlines()]

current_position = 1
cycle_count = 0
total = 0
beam_position = 0
processing = False
operation_index = 0
for i in range(240):
    if beam_position > 39:
        beam_position = 0
        print("")
    if beam_position <= current_position+1 and beam_position >= current_position-1:
        print("#", end='')
    else:
        print(" ", end='')
    if cycle_count in [20, 60, 100, 140, 180, 220]:
        total += (cycle_count*current_position)
    if processing == False:
        if operations[operation_index] == "noop":
            cycle_count += 1
            beam_position += 1
            operation_index += 1
        elif operations[operation_index][:4] == "addx":
            processing = True
            cycle_count += 1
            beam_position += 1
    elif processing == True:
        cycle_count += 1
        beam_position += 1
        current_position += int(operations[operation_index][4:])
        operation_index += 1
        processing = False


print()
print(cycle_count)
print(total)

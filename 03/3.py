def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def part_1(diagnostics):
    gamma = ""
    for i in range(len(diagnostics[0])):
        one_count = 0
        zero_count = 0
        for line in diagnostics:
            if line[i] == '1':
                one_count += 1
            else:
                zero_count += 1
        gamma += '1' if one_count > zero_count else '0'
    epsilon = "".join('1' if x == '0' else '0' for x in gamma)
    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    return gamma_int * epsilon_int


def remove_with_char_at_index(list, char, i):
    return [value for value in list if value[i] != char ]


def prune_diagnostics(diagnostics, pref):
    rating = 0
    for i in range(len(diagnostics[0])):
        one_count = 0
        zero_count = 0
        for line in diagnostics:
            if line[i] == '1':
                one_count += 1
            else:
                zero_count += 1
        if one_count >= zero_count:
            prune_char = '0' if pref == 'max' else '1'
            diagnostics = remove_with_char_at_index(diagnostics, prune_char, i)
        else:
            reverse_char = '1' if pref == 'max' else '0'
            diagnostics = remove_with_char_at_index(diagnostics, reverse_char, i)
        if len(diagnostics) == 1:
            rating = int(diagnostics[0],2)
            break

    return rating

def part_2(diagnostics):
    diagnostics_for_c02 = diagnostics
    oxygen_generator_rating = prune_diagnostics(diagnostics_for_c02, 'max')
    co2_generator_rating = prune_diagnostics(diagnostics_for_c02, 'min')
    return oxygen_generator_rating, co2_generator_rating
            
if __name__ == '__main__':
    filename = './03/input.txt'
    diagnostics = read_input(filename)
    print(part_1(diagnostics))
    oxygen_generator_rating, co2_generator_rating = part_2(diagnostics)
    print(oxygen_generator_rating * co2_generator_rating)

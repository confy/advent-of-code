import itertools


def read_input(filename):
    f = open(filename, 'r').read().rstrip()
    calls, *boards = f.split('\n\n')
    calls = calls.split(',')
    calls = [int(c) for c in calls]

    boards = [b.split() for b in boards]
    final_boards = []
    for board in boards:
        final_board = []
        for i in range(5):
            line = [int(num) for num in board[i*5:i*5+5]]
            final_board.append(line)
        final_boards.append(final_board)

    return calls, final_boards


def check_row(row, called_so_far):
    return all(num in called_so_far for num in row)


def check_board(board, called_so_far):
    board_cols = list(map(list, itertools.zip_longest(*board, fillvalue=None)))
    for row in board:
        if check_row(row, called_so_far):
            return True
    return any(check_row(col, called_so_far) for col in board_cols)


def print_result(board, called_so_far):
    vals_to_sum = []
    for row in board:
        for val in row:
            if val not in called_so_far:
                vals_to_sum.append(val)
    print(sum(vals_to_sum)*called_so_far[-1])

if __name__ == '__main__':
    calls, boards = read_input('./04/input.txt')
    called_so_far = calls[:5]
    calls = calls[5:]

    for call in calls:
        for i, board in enumerate(boards):
            if board == []:
                continue
            result = check_board(board, called_so_far)
            if result == True:
                print_result(board, called_so_far)
                boards[i] = []
        if any(board != [] for board in boards):
            called_so_far.append(call)
    
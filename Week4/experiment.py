def is_solved(board):
    lines = []

    # rows
    for i in range(3):
        lines.append(board[i])

    # columns
    for j in range(3):
        lines.append([board[i][j] for i in range(3)])

    # diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    # check winner
    for line in lines:
        if line == [1, 1, 1]:
            return 1
        if line == [2, 2, 2]:
            return 2

    # check unfinished
    if any(0 in row for row in board):
        return -1

    return 0

def check_winner(board):
    # Winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)  # Diagonal
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None


def check_draw(board):
    return ' ' not in board.values()
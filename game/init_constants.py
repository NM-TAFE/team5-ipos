# Initialise game board and current player
state = {'board': {i: ' ' for i in range(9)}, 'current_player': 'X'}

# Stack used to store the history of player moves.
# Each move is pushed onto this list when a player clicks a cell.
# The undo feature will pop the most recent move from this stack.
move_history = []
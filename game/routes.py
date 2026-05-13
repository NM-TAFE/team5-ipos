from flask import Blueprint, render_template, redirect, url_for

from game.logic import check_winner, check_draw

game_routes = Blueprint('game_routes', __name__)

# Initialise game board and current player
board = {i: ' ' for i in range(9)}
current_player = 'X'

# Stack used to store the history of player moves.
# Each move is pushed onto this list when a player clicks a cell.
# The undo feature will pop the most recent move from this stack.
move_history = []


@game_routes.route('/')
def index():
    winner = check_winner(board)
    draw = check_draw(board)
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@game_routes.route('/play/<int:cell>')
def play(cell):
    global current_player, move_history

    # Do not allow more moves after the game has ended.
    if check_winner(board) or check_draw(board):
        return redirect(url_for('game_routes.index'))

    # Only allow the move if the selected cell is empty.
    if board[cell] == ' ':
        # Push the move onto the stack before changing players.
        move_history.append((cell, current_player))

        board[cell] = current_player

        if not check_winner(board):
            current_player = 'O' if current_player == 'X' else 'X'

    return redirect(url_for('game_routes.index'))


@game_routes.route('/undo')
def undo():
    global current_player, move_history

    # Undo uses stack behaviour:
    # pop() removes the most recent move from move_history.
    if move_history:
        cell, player = move_history.pop()
        board[cell] = ' '
        current_player = player

    return redirect(url_for('game_routes.index'))


@game_routes.route('/reset')
def reset():
    global board, current_player, move_history

    board = {i: ' ' for i in range(9)}
    current_player = 'X'
    move_history = []

    return redirect(url_for('game_routes.index'))

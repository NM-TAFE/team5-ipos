from flask import Blueprint, render_template, redirect, url_for

from game.logic import check_winner, check_draw

game_routes = Blueprint('game_routes', __name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'


@game_routes.route('/')
def index():
    winner = check_winner(board)
    draw = check_draw(board)
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@game_routes.route('/play/<int:cell>')
def play(cell):
    # breakpoint()
    global current_player
    game_over = check_winner(board) or check_draw(board)
    if not game_over and 0 <= cell < len(board) and board[cell] == ' ':
        board[cell] = current_player
        if not check_winner(board):
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('game_routes.index'))


@game_routes.route('/reset')
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('game_routes.index'))

from flask import Blueprint, render_template, redirect, url_for

from game.board_loop import check_winner, check_draw
from game.init_constants import state, move_history

game_routes = Blueprint('game_routes', __name__)

@game_routes.route('/')
def index():
    winner = check_winner(state['board'])
    draw = check_draw(state['board'])
    return render_template('index.html', board=state['board'], current_player=state['current_player'], winner=winner, draw=draw)


@game_routes.route('/play/<int:cell>')
def play(cell):
    # Do not allow more moves after the game has ended.
    if check_winner(state['board']) or check_draw(state['board']):
        return redirect(url_for('game_routes.index'))

    # breakpoint()
    if state['board'][cell] == ' ':
        move_history.append((cell, state['current_player']))
        state['board'][cell] = state['current_player']
        if not check_winner(state['board']):
            state['current_player'] = 'O' if state['current_player'] == 'X' else 'X'
    return redirect(url_for('game_routes.index'))

@game_routes.route('/undo')
def undo():
    # Undo uses stack behaviour:
    # pop() removes the most recent move from move_history.
    if move_history:
        cell, player = move_history.pop()
        state['board'][cell] = ' '
        state['current_player'] = player
    return redirect(url_for('game_routes.index'))

@game_routes.route('/reset')
def reset():
    state['board'] = {i: ' ' for i in range(9)}
    state['current_player'] = 'X'
    move_history.clear()
    return redirect(url_for('game_routes.index'))
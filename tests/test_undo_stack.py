from app import app
import game.board_actions as routes


def setup_function():
    """Reset the game before each test."""
    routes.state['board'] = [' '] * 9
    routes.state['current_player'] = 'X'
    routes.move_history.clear()


def test_play_adds_move_to_stack():
    """A valid move should be pushed onto the move_history stack."""
    client = app.test_client()

    client.get('/play/0')

    assert routes.state['board'][0] == 'X'
    assert routes.move_history == [(0, 'X')]
    assert routes.state['current_player'] == 'O'


def test_undo_removes_last_move_from_stack():
    """Undo should pop the most recent move from the stack."""
    client = app.test_client()

    client.get('/play/0')
    client.get('/play/1')
    client.get('/undo')

    assert routes.state['board'][1] == ' '
    assert routes.move_history == [(0, 'X')]
    assert routes.state['current_player'] == 'O'


def test_reset_clears_move_history_stack():
    """Reset should clear the board and the move_history stack."""
    client = app.test_client()

    client.get('/play/0')
    client.get('/reset')

    assert routes.state['board'] == [' '] * 9
    assert routes.move_history == []
    assert routes.state['current_player'] == 'X'
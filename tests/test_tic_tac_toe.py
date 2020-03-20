import io
from unittest.mock import patch

import pytest

from tic_tac_toe import TicTacToeGame


def test_board_empty():
    game = TicTacToeGame()

    for key in game.board.keys():
        assert game.board[key] == "-"


def test_place_already_taken():
    game = TicTacToeGame()
    game.place(3)
    game.place(3)

    with patch('sys.stdout', new=io.StringIO()) as stdout:
        game.place(3)
    assert stdout.getvalue() == "Position already taken, please try again:\n"


def test_place_valid():
    game = TicTacToeGame()
    game.place(3)
    assert game.board[3] == "X"


def test_is_board_full():
    game = TicTacToeGame()
    assert game.is_board_full() == False

    game.steps = 9
    assert game.is_board_full() == True

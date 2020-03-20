import io
from unittest.mock import patch

import pytest

import tic_tac_toe
from tic_tac_toe import TicTacToeGame


def test_board_empty():
    game = TicTacToeGame()

    for key in game.board.keys():
        assert game.board[key] == "-"


def test_place_already_taken():
    game = TicTacToeGame()
    game.place(3)
    game.place(3)

    with patch("sys.stdout", new=io.StringIO()) as stdout:
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


def test_random_ai_move():
    game = TicTacToeGame()
    with patch("tic_tac_toe.randint") as mock_random:
        mock_random.return_value = 5
        game.random_ai_move()

    with patch("sys.stdout", new=io.StringIO()) as stdout:
        game.place(5)
    assert stdout.getvalue() == "Position already taken, please try again:\n"


def test_draw():
    game = TicTacToeGame()

    with patch("tic_tac_toe.randint") as mock_random:
        game.place(5)
        mock_random.return_value = 3
        game.ai_move()

        game.place(7)
        mock_random.return_value = 9
        game.ai_move()

        game.place(6)
        mock_random.return_value = 4
        game.ai_move()

        game.place(2)
        mock_random.return_value = 8
        game.ai_move()

    with patch("sys.stdout", new=io.StringIO()) as stdout:
        game.place(1)

    assert stdout.getvalue().split("\n")[-2] == "Its a TIE!"


def test_player_win__board_not_full():
    game = TicTacToeGame()

    with patch("tic_tac_toe.randint") as mock_random:
        game.place(7)
        mock_random.return_value = 1
        game.ai_move()

        game.place(8)
        mock_random.return_value = 2
        game.ai_move()

    with patch("sys.stdout", new=io.StringIO()) as stdout:
        game.place(9)

    assert stdout.getvalue().split("\n")[-2] == "Congratulations! You win!"


def test_ai_win__board_not_full():
    game = TicTacToeGame()

    with patch("tic_tac_toe.randint") as mock_random:
        game.place(7)
        mock_random.return_value = 1
        game.ai_move()

        game.place(8)
        mock_random.return_value = 2
        game.ai_move()

        game.place(5)
        mock_random.return_value = 3

        with patch("sys.stdout", new=io.StringIO()) as stdout:
            game.ai_move()

    assert stdout.getvalue().split("\n")[-2] == "Sorry you lost, keep trying!"


def test_player_win__board_full():
    game = TicTacToeGame()

    with patch("tic_tac_toe.randint") as mock_random:
        game.place(5)
        mock_random.return_value = 1
        game.ai_move()

        game.place(8)
        mock_random.return_value = 2
        game.ai_move()

        game.place(3)
        mock_random.return_value = 7
        game.ai_move()

        game.place(4)
        mock_random.return_value = 9
        game.ai_move()

    with patch("sys.stdout", new=io.StringIO()) as stdout:
        game.place(6)

    assert stdout.getvalue().split("\n")[-2] == "Congratulations! You win!"

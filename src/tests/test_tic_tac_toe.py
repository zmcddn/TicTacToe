import io
from unittest.mock import patch

import pytest

import ai_moves
from tic_tac_toe import TicTacToeGame, handle_game_end
from exceptions import TicTacToeException


def test_board_empty():
    game = TicTacToeGame()

    for key in game.board.keys():
        assert game.board[key] == "-"


def test_check_position():
    game = TicTacToeGame()

    with pytest.raises(TicTacToeException):
        game.check_position(0)

    with pytest.raises(TicTacToeException):
        game.check_position(10)

    with pytest.raises(TicTacToeException):
        game.check_position(564)

    with pytest.raises(TicTacToeException):
        game.check_position("SA")

    with pytest.raises(TicTacToeException):
        game.check_position("=")


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
    with patch("ai_moves.randint") as mock_random:
        mock_random.return_value = 5
        game.random_ai_move()

    with patch("sys.stdout", new=io.StringIO()) as stdout:
        game.place(5)
    assert stdout.getvalue() == "Position already taken, please try again:\n"


def test_draw():
    game = TicTacToeGame()

    with patch("ai_moves.randint") as mock_random:
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

    with patch("ai_moves.randint") as mock_random:
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

    with patch("ai_moves.randint") as mock_random:
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

    with patch("ai_moves.randint") as mock_random:
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


def test_game_reset():
    game = TicTacToeGame()

    game.place(8)
    game.reset()

    assert game.steps == 0
    for key in game.board.keys():
        assert game.board[key] == "-"


def test_game_restart():
    game = TicTacToeGame()

    game.place(8)
    game.restart()

    assert game.steps == 0
    for key in game.board.keys():
        assert game.board[key] == "-"


def test_game_row_win():
    game = TicTacToeGame()
    game.place(7)
    game.place(8)
    game.place(9)

    assert game._check_row_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"
    game.restart()

    game.place(4)
    game.place(5)
    game.place(6)

    assert game._check_row_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"
    game.restart()

    game.place(1)
    game.place(2)
    game.place(3)

    assert game._check_row_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"


def test_game_col_win():
    game = TicTacToeGame()
    game.place(7)
    game.place(4)
    game.place(1)

    assert game._check_col_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"
    game.restart()

    game.place(8)
    game.place(5)
    game.place(2)

    assert game._check_col_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"
    game.restart()

    game.place(9)
    game.place(6)
    game.place(3)

    assert game._check_col_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"


def test_game_diag_win():
    game = TicTacToeGame()
    game.place(7)
    game.place(5)
    game.place(3)

    assert game._check_diag_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"
    game.restart()

    game.place(9)
    game.place(5)
    game.place(1)

    assert game._check_diag_win(game.board, "X") == True
    assert game.check_winner(game.board) == "Player"


def test_handle_game_end():
    game = TicTacToeGame()
    game.place(8)

    with patch("builtins.input", return_value="y"):
        handle_game_end(game)

    assert game.board[8] == "-"

    with pytest.raises(TicTacToeException):
        with patch("builtins.input", return_value="n"):
            handle_game_end(game)

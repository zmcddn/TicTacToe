from tic_tac_toe import TicTacToeGame


def test_board_empty():
    game = TicTacToeGame()

    for key in game.board.keys():
        assert game.board[key] == "-"


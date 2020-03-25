from exceptions import TicTacToeException
from ai_moves import AIMoves


class TicTacToeGame(AIMoves):
    def __init__(self, *args, **kwargs):
        self.board = {
            1: "-",
            2: "-",
            3: "-",
            4: "-",
            5: "-",
            6: "-",
            7: "-",
            8: "-",
            9: "-",
        }

        self.steps = 0

        self.print_greatings()

    def print_board(self, is_greating=False, add_board_spacing=True):
        if add_board_spacing:
            spacing = " " * 2
        else:
            spacing = ""

        for i in range(7, 0, -3):
            print(f"{spacing}+---+---+---+")
            if is_greating:
                print(f"{spacing}| {i} | {i+1} | {i+2} |")
            else:
                print(
                    f"{spacing}| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |"
                )
        print(f"{spacing}+---+---+---+\n")

    def print_greatings(self, board=None):
        print("\nWelcome to the Tic Tac Toe game, here is the board layout.")
        print("  i.e. its the same as the numeric key pad layout.\n")

        self.print_board(is_greating=True)

        print("Type in the location in the cell to place your token.")
        print("For example, input 7 to place in the top left corner.")
        print("You can use your numeric key pad to play!")
        print("\nNow lets get started, you go first, have fun!\n")
        print("===" * 20, "\n")

        self.print_board()

    @staticmethod
    def check_position(position):
        try:
            # Convert user input to 1 <= position <= 9
            # Quit game if input is invalid

            position = int(position)
            if not 1 <= position <= 9:
                raise TicTacToeException
        except ValueError:
            raise TicTacToeException

        return position

    def place(self, position):
        position = self.check_position(position)

        has_valid_position = False

        if self.board[position] != "-":
            print("Position already taken, please try again:")
        else:
            self.board[position] = "X"
            has_valid_position = True

        if has_valid_position:
            self.steps += 1
            self.print_board()

        # Check if game is finished at end of each step
        return has_valid_position, self.is_game_finished()

    def is_board_full(self):
        """Return True if board is full otherwise False"""
        return self.steps == 9

    def ai_move(self):
        position = self.random_ai_move()

        print(f"AI moves to {position}:")
        self.steps += 1
        self.print_board()

        # Check if game is finished at end of each step
        return self.is_game_finished()

    def is_game_finished(self):
        """Game is finished whenever there is a winner or board is full"""

        is_finished = True
        winner = self.check_winner(self.board)

        if winner == "AI":
            print("Sorry you lost, keep trying!")
        elif winner == "Player":
            print("Congratulations! You win!")
        else:
            if self.is_board_full():
                print("Its a TIE!")
            else:
                is_finished = False

        return is_finished

    @classmethod
    def check_winner(cls, board):
        if (
            cls._check_row_win(board, "X")
            or cls._check_col_win(board, "X")
            or cls._check_diag_win(board, "X")
        ):
            return "Player"
        elif (
            cls._check_row_win(board, "O")
            or cls._check_col_win(board, "O")
            or cls._check_diag_win(board, "O")
        ):
            return "AI"
        else:
            return None

    @classmethod
    def _check_row_win(cls, board, target):
        return (
            (
                board[1] == target
                and board[2] == target
                and board[3] == target
            )
            or (
                board[4] == target
                and board[5] == target
                and board[6] == target
            )
            or (
                board[7] == target
                and board[8] == target
                and board[9] == target
            )
        )

    @classmethod
    def _check_col_win(cls, board, target):
        return (
            (
                board[1] == target
                and board[4] == target
                and board[7] == target
            )
            or (
                board[2] == target
                and board[5] == target
                and board[8] == target
            )
            or (
                board[3] == target
                and board[6] == target
                and board[9] == target
            )
        )

    @classmethod
    def _check_diag_win(cls, board, target):
        return (
            board[1] == target
            and board[5] == target
            and board[9] == target
        ) or (
            board[3] == target
            and board[5] == target
            and board[7] == target
        )

    def reset(self):
        self.steps = 0
        for key in self.board.keys():
            self.board[key] = "-"

    def restart(self):
        self.reset()
        self.print_board()


def start_game():
    game = TicTacToeGame()

    step = 0
    while True:
        print("Your move (press any key other than 1~9 to quit):")
        position = input()
        try:
            position_valid, _is_game_end = game.place(position)
            if not position_valid:
                continue

            if _is_game_end:
                handle_game_end(game)

            is_game_end = game.ai_move()
            if is_game_end:
                handle_game_end(game)
            step += 1
        except TicTacToeException:
            print("\nThanks for playing, have a great day!\n")
            break


def check_restart():
    while True:
        user_input = input()

        if user_input.upper() != "Y" and user_input.upper() != "N":
            print("Invalid input, please input either Y or N")
            continue
        else:
            return user_input.upper() == "Y"


def handle_game_end(game):
    print("Would you like to restart: [Y or N]:")
    restart = check_restart()
    if restart:
        print("\nHere we go! Game restarted!\n")
        game.restart()
        step = 0
    else:
        raise TicTacToeException


if __name__ == "__main__":
    start_game()

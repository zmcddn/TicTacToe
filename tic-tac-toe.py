from random import randint


class TicTacToeGame(object):
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

        for i in range(1, 10, 3):
            print(f"{spacing}+---+---+---+")
            if is_greating:
                print(f"{spacing}| {i} | {i+1} | {i+2} |")
            else:
                print(
                    f"{spacing}| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |"
                )
        print(f"{spacing}+---+---+---+\n")

    def print_greatings(self, board=None):
        print("Welcome to the Tic Tac Toe game, here is the board layout.\n")

        self.print_board(is_greating=True)

        print("\nType in the location in the cell to place your token.")
        print("For example, input 1 to place in the top left corner.")
        print("\nNow lets get started, you go first, have fun!\n")
        print("===" * 20, "\n")

        self.print_board()

    def place(self, position):
        if not 1 <= position <= 9:
            print("Invalid position")
        elif self.board[position] != "-":
            print("Position already taken")
        else:
            self.board[position] = "X"

        self.steps += 1

        self.print_board()

    def is_board_full(self):
        """Return True if board is full otherwise False"""
        return self.steps == 9

    def ai_move(self):
        """AI makes a random legal move"""

        iteration = 0
        position = 0
        while iteration < 10:
            _position = randint(1, 9)
            if self.board[_position] == "-":
                position = _position
                break
            else:
                iteration += 1

        if position == 0 and not self.is_board_full():
            # Theoritically this should not happen
            for key, value in self.board.items():
                if value == "-":
                    position = key
                    break

        self.board[position] = "O"

        print("AI moves:")
        self.steps += 1
        self.print_board()

        # Check if game is finished at end of each step
        return self.is_game_finished()

    def is_game_finished(self):
        """Game is finished whenever there is a winner or board is full"""

        is_finished = True
        winner = self.check_winner()

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

    def check_winner(self):
        if (
            self.check_row_win("X")
            or self.check_col_win("X")
            or self.check_diag_win("X")
        ):
            return "Player"
        elif (
            self.check_row_win("O")
            or self.check_col_win("O")
            or self.check_diag_win("O")
        ):
            return "AI"
        else:
            return None

    def check_row_win(self, target):
        return (
            (
                self.board[1] == target
                and self.board[2] == target
                and self.board[3] == target
            )
            or (
                self.board[4] == target
                and self.board[5] == target
                and self.board[6] == target
            )
            or (
                self.board[7] == target
                and self.board[8] == target
                and self.board[9] == target
            )
        )

    def check_col_win(self, target):
        return (
            (
                self.board[1] == target
                and self.board[4] == target
                and self.board[7] == target
            )
            or (
                self.board[2] == target
                and self.board[5] == target
                and self.board[8] == target
            )
            or (
                self.board[3] == target
                and self.board[6] == target
                and self.board[9] == target
            )
        )

    def check_diag_win(self, target):
        return (
            self.board[1] == target
            and self.board[5] == target
            and self.board[9] == target
        ) or (
            self.board[3] == target
            and self.board[5] == target
            and self.board[7] == target
        )


def start_game():
    game = TicTacToeGame()
    for i in range(9):
        print("Your move:")
        position = input()
        game.place(int(position))
        game.ai_move()


if __name__ == "__main__":
    start_game()

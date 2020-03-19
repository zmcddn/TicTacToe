from random import randint


class TicTacToeGame(object):
    def __init__(self, *args, **kwargs):
        self.board = {
            1: '-',
            2: '-',
            3: '-',
            4: '-',
            5: '-',
            6: '-',
            7: '-',
            8: '-',
            9: '-',
        }

        self.steps = 0

        self.print_greatings()

    def print_board(self, is_greating=False):
        for i in range(1, 10, 3):
            print(" "*2, "+---+---+---+")
            if is_greating:
                print(" "*2, f"| {i} | {i+1} | {i+2} |")
            else:
                print(" "*2, f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |")
        print(" "*2, "+---+---+---+\n")

    def print_greatings(self, board=None):
        print("Welcome to the Tic Tac Toe game, here is the board layout.\n")

        self.print_board(is_greating=True)

        print("\nType in the location in the cell to place your token.")
        print("For example, input 1 to place in the top left corner.")
        print("\nNow lets get started, you go first, have fun!\n")
        print("==="*20, "\n")

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

        # Check board to make sure its not full and game is still on
        if self.is_board_full():
            print("Game over!")
            # If board is full then check winner

    def check_winner(self):
        pass


if __name__ == "__main__":
    game = TicTacToeGame()
    for i in range(9):
        print("Your move:")
        position = input()
        game.place(int(position))
        game.ai_move()
        # print(game.is_board_full())

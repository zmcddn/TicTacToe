from random import randint


class AIMoves:
    def __init__(self, board, *args, **kwargs):
        super().__init__()

    def random_ai_move(self):
        """AI makes a random legal move"""

        # We could use random.choice() instead of the following logic
        # but I don't want to
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
            # After a few iterations there should be a position chosen
            # if not we iterate through the board to assign the first
            # empyt cell as the position
            # if we are lucky enough this should not happen
            for key, value in self.board.items():
                if value == "-":
                    position = key
                    break

        self.board[position] = "O"

        return position

    def ai_move(self):
        raise NotImplementedError

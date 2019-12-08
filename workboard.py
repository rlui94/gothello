import board


class Workboard(board.Board):
    def __init__(self):
        self.best_move = None
        super().__init__()

    def copy(self, wb):
        super().copy(wb)
        self.best_move = wb.best_move

    def heval(self):
        """
        Evaluate board state from pov of current player
        :return: score as int
        """
        nstones = 0
        ostones = 0
        for i in range(board.BOARD_SIZE):
            for j in range(board.BOARD_SIZE):
                if self.grid[i][j] == self.to_move:
                    nstones += 1
                elif self.grid[i][j] == self.opponent(self.to_move):
                    ostones += 1
        return nstones - ostones


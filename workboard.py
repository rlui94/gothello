import board


INF = pow(board.BOARD_SIZE, 2)


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

    def minimax(self, depth, max_player):
        if depth <= 0 or self.game_state == board.GAME_OVER:
            return self.heval()
        mvs = self.gen_moves()
        if max_player:
            max_eval = -INF
            for mv in mvs:
                scratch = Workboard()
                scratch.copy(self)
                status = scratch.try_move(mv)
                if status == board.ILLEGAL_MOVE:
                    raise Exception("unexpectedly illegal move")
                if status == board.GAME_OVER:
                    raise Exception("unexpectedly game over")
                child_eval = scratch.minimax(depth-1, False)
                max_eval = max(max_eval, child_eval)
            return max_eval
        else:
            min_eval = INF
            for mv in mvs:
                scratch = Workboard()
                scratch.copy(self)
                status = scratch.try_move(mv)
                if status == board.ILLEGAL_MOVE:
                    raise Exception("unexpectedly illegal move")
                if status == board.GAME_OVER:
                    raise Exception("unexpectedly game over")
                child_eval = scratch.minimax(depth - 1, True)
                min_eval = min(min_eval, child_eval)
            return min_eval

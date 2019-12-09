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
        # if target depth reached or game over
        if depth <= 0 or self.game_state == board.GAME_OVER:
            return self.heval()
        mvs = self.gen_moves()
        # if no possible moves remain
        if len(mvs) == 0:
            scratch = Workboard()
            scratch.copy(self)
            status = scratch.try_move(scratch.best_move)
            if status != board.GAME_OVER:
                return 0  # not sure about this
            # if game is over, return INF/-INF depending on who won
            result = scratch.referee()
            if result == self.to_move:
                return INF
            elif result == self.opponent(self.to_move):
                return -INF
            else:
                return 0
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

    def find_best_move(self, depth):
        best_move = None
        best_val = -INF
        mvs = self.gen_moves()
        for mv in mvs:
            scratch = Workboard()
            scratch.copy(self)
            status = scratch.try_move(mv)
            if status == board.ILLEGAL_MOVE:
                raise Exception("unexpectedly illegal move")
            if status == board.GAME_OVER:
                raise Exception("unexpectedly game over")
            move_val = scratch.minimax(depth-1, False)
            if move_val > best_val:
                best_move = mv
                best_val = move_val
        return best_move


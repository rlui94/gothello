import board


INF = pow(board.BOARD_SIZE, 2)


class Workboard(board.Board):
    def __init__(self):
        super().__init__()

    def copy(self, wb):
        super().copy(wb)

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

    def minimax(self, depth, alpha, beta, max_player):
        """
        Recursive Minimax function w/ alpha-beta pruning
        :param depth: depth to which to search as int
        :param alpha: value to compare with beta for pruning as int
        :param beta: value to compare with alpha for pruning as int
        :param max_player: True if current player is maximizing, false if current player is minimizing
        :return: score as int
        """
        mvs = self.gen_moves()
        # if no possible moves remain
        if len(mvs) == 0:
            result = self.heval()
            if result > 0:
                return INF
            elif result < 0:
                return -INF
            else:
                return 0
        # if target depth reached or game over
        if depth <= 0 or self.game_state == board.GAME_OVER:
            return self.heval()
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
                child_eval = scratch.minimax(depth-1, alpha, beta, False)
                max_eval = max(max_eval, child_eval)
                alpha = max(alpha, child_eval)
                if beta <= alpha:
                    break
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
                child_eval = scratch.minimax(depth - 1, alpha, beta, True)
                min_eval = min(min_eval, child_eval)
                beta = min(beta, child_eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self, depth):
        """
        Find best move from current board state using minimax()
        :param depth: depth to which we search as int
        :return: best move as Move object
        """
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
            move_val = scratch.minimax(depth-1, -INF, INF, False)
            if move_val > best_val:
                best_move = mv
                best_val = move_val
        if best_move is None:
            return board.Move.from_desc("pass")
        return best_move


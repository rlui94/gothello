import board


class Workboard(board.Board):
    def __init__(self):
        self.best_move = None
        super().__init__()

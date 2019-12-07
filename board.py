

GAME_OVER = 1
CONTINUE = 0
ILLEGAL_MOVE = -1
WHITE = 1
BLACK = 2
OBSERVER = 3
BOARD_SIZE = 5


class Board:
    """
    Board class containing information about a single instance of the board.
    grid: BOARD_SIZE by BOARD_SIZE list of lists of integers. Each list is a column from bottom to top.
    """
    def __init__(self):
        """
        """
        self.grid = [[0 in range(BOARD_SIZE)] * 2]  # initialize grid to all 0s
        self.game_state = CONTINUE
        self.to_move = BLACK
        self.previous_move = ''

    @classmethod
    def from_board(cls, board):
        cls.grid = board.grid.copy()
        cls.game_state = board.game_state
        cls.to_move = board.to_move
        cls.previous_move = board.previous_move
        return cls()

    def print_board(self):
        def get_square(sq):
            switcher = {
                WHITE: 'W',
                BLACK: 'B',
                0: '.'
            }
            return switcher.get(sq, "*")
        for j in range(BOARD_SIZE-1, -1, -1):
            line = ''
            for i in range(BOARD_SIZE):
                line += get_square(self.grid[i][j])
            print(line)

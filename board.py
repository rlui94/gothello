

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
        """
        print the current grid state with W for white, B for black, . for empty square, * for error
        :return:
        """
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

    def scratch_board():
        """
        create a BOARD_SIZE sized board as a list of lists of bools init to all False
        :return:
        """
        return [[False in range(BOARD_SIZE)] * 2]

    def flood(self, scratch, color, x, y):
        """
        Floods scratch board to find the borders.
        :param scratch: BOARD_SIZE sized board as a list of lists of bools (use method scratch_board())
        :param color: color to flood board with as int
        :param x: x coord to flood at as int
        :param y: y coord to flood at as int
        :return:
        """
        #  off board
        if not (0 <= x <= BOARD_SIZE - 1 and 0 <= y <= BOARD_SIZE - 1):
            return
        # already done
        if scratch[x][y]:
            return
        # wrong color
        if self.grid[x][y] != color:
            return
        # ok
        scratch[x][y] = True
        self.flood(scratch, color, x - 1, y)
        self.flood(scratch, color, x + 1, y)
        self.flood(scratch, color, x, y - 1)
        self.flood(scratch, color, x, y + 1)

    def group_border(self, scratch, x, y):
        """
        Check if coord x,y is a border square
        :param scratch: BOARD_SIZE sized board as a list of lists of bools that has been flooded with flood()
        :param x: x coord of square as int
        :param y: y coord of square as int
        :return: True if square is a border square, false otherwise
        """
        if scratch[x][y]:
            return False
        if x > 0 and scratch[x - 1][y]:
            return True
        if x < BOARD_SIZE-1 and scratch[x + 1][y]:
            return True
        if y > 0 and scratch[x][y - 1]:
            return True
        if y < BOARD_SIZE-1 and scratch[x][y + 1]:
            return True
        return False

    def liberties(self, x, y):
        """
        Find the number of liberties for position xy
        :param x: x coord as int
        :param y: y coord as int
        :return: number of liberties as int
        """
        scratch = scratch_board()
        self.flood(scratch, self.grid[x][y], x, y)
        n = 0
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.grid[i][j] == 0 and self.group_border(scratch, i, j):
                    n += 1
        return n


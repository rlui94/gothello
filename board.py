# Heavily based on
# https://github.com/pdx-cs-ai/gothello-gthd/blob/35757a7525dac383e23065097f9a35b2385eef82/Board.java
from move import Move


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
        self.grid = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # initialize grid to all 0s
        self.game_state = CONTINUE
        self.to_move = BLACK
        self.previous_move = ''

    def copy(self, board):
        """
        Copy another board object
        :param board: board to be copied
        :return: new board copy
        """
        self.grid = board.grid.copy()
        self.game_state = board.game_state
        self.to_move = board.to_move
        self.previous_move = board.previous_move

    @staticmethod
    def opponent(color):
        """
        Return color of opponent
        :param color: color of player as int
        :return: color of opponent as int
        """
        if color == WHITE:
            return BLACK
        elif color == BLACK:
            return WHITE
        else:
            raise Exception("Bad color argument")

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

    @staticmethod
    def scratch_board():
        """
        create a BOARD_SIZE sized board as a list of lists of bools init to all False
        :return:
        """
        return [[False]*BOARD_SIZE for _ in range(BOARD_SIZE)]

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

    @staticmethod
    def group_border(scratch, x, y):
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
        scratch = self.scratch_board()
        self.flood(scratch, self.grid[x][y], x, y)
        n = 0
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.grid[i][j] == 0 and self.group_border(scratch, i, j):
                    n += 1
        return n

    def move_ok(self, mv: Move):
        """
        Find if move is legal
        :param mv: move to check
        :return: True if legal, False otherwise
        """
        if mv.is_pass():
            return True
        elif self.grid[mv.x][mv.y] != 0:
            return False
        else:
            self.grid[mv.x][mv.y] = self.to_move
            libs = self.liberties(mv.x, mv.y)
            self.grid[mv.x][mv.y] = 0
            if libs == 0:
                return False
            else:
                return True

    def gen_moves(self):
        """
        Generate list of legal moves
        :return: list of move objects
        """
        res = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if self.grid[i][j] == 0:
                    m = Move(i, j)
                    if self.move_ok(m):
                        res.append(m)
        return res

    def capture(self, x, y):
        """
        Attempt to capture a square of the board
        :param x: x coord as int
        :param y: y coord as int
        :return:
        """
        if self.liberties(x, y) > 0:
            return
        else:
            scratch = self.scratch_board()
            self.flood(scratch, self.grid[x][y], x, y)
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if scratch[i][j]:
                        self.grid[i][j] = self.to_move

    def do_captures(self, m: Move):
        """
        For a given move, compute the resulting captures
        :param m: move as Move object
        :return:
        """
        if m.x > 0 and self.grid[m.x - 1][m.y] == self.opponent(self.to_move):
            self.capture(m.x - 1, m.y)
        if m.x < BOARD_SIZE-1 and self.grid[m.x + 1][m.y] == self.opponent(self.to_move):
            self.capture(m.x + 1, m.y)
        if m.y > 0 and self.grid[m.x][m.y - 1] == self.opponent(self.to_move):
            self.capture(m.x, m.y - 1)
        if m.y < BOARD_SIZE-1 and self.grid[m.x][m.y + 1] == self.opponent(self.to_move):
            self.capture(m.x, m.y + 1)


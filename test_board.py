import unittest
from board import Board
from move import Move


letter_grid = [['a1', 'a2', 'a3','a4','a5'],
               ['b1', 'b2', 'b3','b4','b5'],
               ['c1','c2','c3','c4','c5'],
               ['d1','d2','d3','d4','d5'],
               ['e1','e2','e3','e4','e5'],
               ]
number_grid = [[0, 1, 0, 0, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 0, 2, 1],
               [0, 2, 0, 1, 0],
               [2, 0, 2, 0, 1],
               ]


class BoardTest(unittest.TestCase):
    def test_print(self):
        b = Board()
        b.grid = number_grid
        b.print_board()

    def test_legal(self):
        b = Board()
        b.grid = number_grid
        mv = Move.from_desc("b2")
        self.assertEqual(b.move_ok(mv), False)
        mv = Move.from_desc("b1")
        self.assertEqual(b.move_ok(mv), True)

    def test_gen_move(self):
        b = Board()
        b.grid = number_grid
        mvs = b.gen_moves()
        for mv in mvs:
            print(mv.name())


if __name__ == '__main__':
    unittest.main()

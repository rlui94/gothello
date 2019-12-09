import unittest
from workboard import Workboard


number_grid = [[0, 1, 0, 0, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 0, 2, 1],
               [0, 2, 0, 2, 0],
               [2, 0, 2, 1, 2],
               ]

cap_grid = [[0, 1, 0, 1, 1],
            [1, 1, 2, 1, 1],
            [0, 0, 2, 2, 2],
            [0, 2, 0, 2, 0],
            [2, 0, 2, 1, 2],
            ]


class WorkboardTests(unittest.TestCase):
    def test_constructor(self):
        wb = Workboard()
        self.assertEqual(wb.best_move, None)

    def test_heval(self):
        wb = Workboard()
        wb.grid = number_grid
        # blk first so 6-7=-1
        self.assertEqual(wb.heval(), -1)

    def test_minimax(self):
        wb = Workboard()
        wb.grid = cap_grid
        print(wb.minimax(3, True))

    def test_find_best(self):
        wb = Workboard()
        wb.grid = cap_grid
        print(wb.find_best_move(3).name())


if __name__ == '__main__':
    unittest.main()

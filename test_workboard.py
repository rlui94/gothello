import unittest
from workboard import Workboard


number_grid = [[0, 1, 0, 0, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 0, 2, 1],
               [0, 2, 0, 2, 0],
               [2, 0, 2, 1, 2],
               ]


class WorkboardTests(unittest.TestCase):
    def test_constructor(self):
        wb = Workboard()
        self.assertEqual(wb.best_move, None)


if __name__ == '__main__':
    unittest.main()

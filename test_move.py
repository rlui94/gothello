import unittest
from move import Move


class MyTestCase(unittest.TestCase):
    def test_digit(self):
        # mv = Move.from_coords(0, 2)
        mv = Move("a3")
        self.assertEqual(mv.move_digit('1'), 0)
        self.assertEqual(mv.move_letter('c'), 2)
        self.assertEqual(mv.name(), "a3")


if __name__ == '__main__':
    unittest.main()
